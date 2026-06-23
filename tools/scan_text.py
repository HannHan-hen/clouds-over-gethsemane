#!/usr/bin/env python3
"""Scan the manuscript for repeating-phrase AI tics.

Goes beyond a contiguous-trigram pass with three extra techniques:

  1. Skip-gram / templated n-grams
     Contiguous n-grams (n=3..5) where exactly one interior token is
     replaced by a wildcard slot ``<>``. Reported only when the slot is
     actually filled by >=2 distinct words, so it surfaces *variable-slot*
     templates that a fixed trigram can't merge -- e.g. "felt <> rise in
     his" (heat/blood), "with <> determination" (grim/cheerful), the
     "felt like a <>" simile crutch.

  2. Sentence-opener n-grams
     The first 1-3 tokens of every sentence, tallied separately. AI prose
     clusters hard on how sentences *begin* ("Jay ...", "The man ...",
     "For a moment ...", "Through the glass ...") -- a cadence tic that is
     invisible to content n-grams because the repetition is positional.

  3. Dispersion (Gries' DP)
     For every surviving candidate, measures how evenly it is spread
     across the 48 chapters. A phrase used 18x evenly is probably part of
     the voice; 18x clustered in three scenes is a tic you wrote on a bad
     day. DP ranges 0 (perfectly even) -> ~1 (all in one chapter).

Output is a graded markdown report in the same shape as
guidelines/ai-tics-watchlist.md. Phrases already on that watchlist are
tagged ``[known]`` so you can focus on what's new.

Zero third-party dependencies. Python 3.8+.
"""
from __future__ import annotations

import argparse
import glob
import os
import sys
from collections import Counter, defaultdict

from textlib import (
    WILDCARD, STOPWORDS, load_chapters, sentence_openers,
    deviation_of_proportions,
)


# --------------------------------------------------------------------------- #
# Pattern generators (yield string keys)
# --------------------------------------------------------------------------- #
def contiguous_ngrams(tokens, n):
    for i in range(len(tokens) - n + 1):
        yield " ".join(tokens[i : i + n])


def templated_ngrams(tokens, n):
    """n-grams with exactly one *interior* token blanked. Yields (key, filler)."""
    for i in range(len(tokens) - n + 1):
        window = tokens[i : i + n]
        for slot in range(1, n - 1):  # interior positions only
            filler = window[slot]
            key = " ".join(WILDCARD if j == slot else w for j, w in enumerate(window))
            yield key, filler


# --------------------------------------------------------------------------- #
# Watchlist parsing (to tag already-known phrases)
# --------------------------------------------------------------------------- #
def load_watchlist(path):
    known = set()
    if not path or not os.path.exists(path):
        return known
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line.startswith("- "):
                continue
            term = line[2:].split("(")[0].split("—")[0].split(" / ")[0].strip()
            term = term.lower().strip(" .")
            if term:
                known.add(term)
    return known


def is_known(key, known):
    base = key.replace(WILDCARD, "").replace("  ", " ").strip()
    if key in known or base in known:
        return True
    return any(k and k in base for k in known if len(k) > 6)


# --------------------------------------------------------------------------- #
# Main scan
# --------------------------------------------------------------------------- #
def run(chapters, mode, ngram_sizes, min_count, min_fillers, max_fillers, top):
    chap_sizes = [len(c.tokens) for c in chapters]

    totals = Counter()
    fillers = defaultdict(Counter)  # key -> {fill word: count} (for examples)
    per_chap = defaultdict(Counter)  # key -> {chap_idx: count}

    for idx, ch in enumerate(chapters):
        tokens, raw = ch.tokens, ch.text
        if mode == "opener":
            for _depth, key in sentence_openers(raw, ngram_sizes):
                totals[key] += 1
                per_chap[key][idx] += 1
            continue
        for n in ngram_sizes:
            if mode == "contiguous":
                for key in contiguous_ngrams(tokens, n):
                    totals[key] += 1
                    per_chap[key][idx] += 1
            elif mode == "templated":
                for key, filler in templated_ngrams(tokens, n):
                    totals[key] += 1
                    per_chap[key][idx] += 1
                    fillers[key][filler] += 1

    rows = []
    for key, total in totals.items():
        if total < min_count:
            continue
        if mode == "templated":
            # The template tic is a near-fixed phrase with a *small closed*
            # substitution set: it varies (>=min_fillers) but not freely
            # (<=max_fillers). A 168-filler slot is just "subject + anything".
            ndistinct = len(fillers[key])
            if ndistinct < min_fillers or ndistinct > max_fillers:
                continue
            # And it must be anchored by >=1 content word, else it is a bare
            # function-word frame ("the <> of") -- too generic to flag.
            fixed = [w for w in key.split() if w != WILDCARD]
            if all(w in STOPWORDS for w in fixed):
                continue
        if mode == "contiguous":
            if all(w in STOPWORDS for w in key.split()):
                continue
        if mode == "opener" and key in STOPWORDS and len(key.split()) == 1:
            continue  # a lone "i"/"he" opener is not informative on its own
        dp = deviation_of_proportions(per_chap[key], chap_sizes, total)
        examples = [w for w, _ in fillers[key].most_common(3)] if key in fillers else []
        rows.append((key, total, len(fillers.get(key, ())), dp, examples))

    # Rank by burstiness-weighted frequency: frequent AND clumpy floats up.
    rows.sort(key=lambda r: (r[1] * (0.4 + r[3])), reverse=True)
    return rows[:top]


def fmt_rows(rows, mode, known):
    lines = []
    for key, total, nfill, dp, examples in rows:
        tag = " [known]" if is_known(key, known) else ""
        extra = ""
        if mode == "templated":
            ex = ", ".join(examples)
            extra = f", {nfill} fills (e.g. {ex})"
        label = key
        if mode == "opener":
            label = f'"{key} …"'
        lines.append(f"- {label} — {total}x, DP={dp:.2f}{extra}{tag}")
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--books", nargs="+",
                    default=sorted(glob.glob("source/book*.txt")),
                    help="manuscript text files (default: source/book*.txt)")
    ap.add_argument("--watchlist", default="guidelines/ai-tics-watchlist.md",
                    help="watchlist file used to tag [known] phrases")
    ap.add_argument("--min-count", type=int, default=6,
                    help="minimum whole-manuscript occurrences (default 6)")
    ap.add_argument("--min-fillers", type=int, default=2,
                    help="templated: min distinct slot fills, i.e. it varies "
                         "(default 2)")
    ap.add_argument("--max-fillers", type=int, default=12,
                    help="templated: max distinct slot fills, i.e. a small "
                         "closed set not 'subject + anything' (default 12)")
    ap.add_argument("--top", type=int, default=40,
                    help="rows per section (default 40)")
    ap.add_argument("--out", default="-",
                    help="report path, or - for stdout (default -)")
    args = ap.parse_args(argv)

    if not args.books:
        ap.error("no book files found; pass --books")

    chapters = load_chapters(args.books)
    if not chapters:
        ap.error("no chapters parsed; check the 'Chapter N:' markers")
    known = load_watchlist(args.watchlist)
    total_words = sum(len(c.tokens) for c in chapters)

    out = []
    out.append("# Text-scan candidates (auto-generated)")
    out.append("")
    out.append(f"Source: {', '.join(args.books)} — "
               f"{len(chapters)} chapters, {total_words:,} words.")
    out.append(f"Filters: min-count={args.min_count}, "
               f"fillers={args.min_fillers}–{args.max_fillers}. "
               "DP = Gries' dispersion (0 even … 1 clumped); "
               "high DP at moderate count = localized tic. "
               "`[known]` = already on the watchlist.")
    out.append("")
    out.append("Generated by `tools/scan_text.py`. Review and promote real "
               "hits into `guidelines/ai-tics-watchlist.md`.")
    out.append("")

    sections = [
        ("## Extended contiguous n-grams (n=3–5)", "contiguous", [3, 4, 5]),
        ("## Templated n-grams — variable-slot phrases (n=3–5)",
         "templated", [3, 4, 5]),
        ("## Sentence openers (first 1–3 words)", "opener", [1, 2, 3]),
    ]
    for title, mode, sizes in sections:
        rows = run(chapters, mode, sizes, args.min_count,
                   args.min_fillers, args.max_fillers, args.top)
        out.append(title)
        out.append("")
        out.extend(fmt_rows(rows, mode, known) or ["- (none above thresholds)"])
        out.append("")

    text = "\n".join(out) + "\n"
    if args.out == "-":
        sys.stdout.write(text)
    else:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {args.out} ({len(chapters)} chapters, "
              f"{total_words:,} words)", file=sys.stderr)


if __name__ == "__main__":
    main()
