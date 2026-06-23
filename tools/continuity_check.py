#!/usr/bin/env python3
"""Continuity ledger -- the class of bug that got hand-fixed in ch48.

Three self-contained checks, all advisory:

  1. Day/time ledger
     Every weekday/relative-day reference, per scene, with line numbers.
     Scenes that name two *different* weekdays are flagged as possible
     contradictions (the kind of date wrinkle fixed by hand in ch48).

  2. Eye / hair colour consistency
     Collects "<colour> eyes/hair" descriptions and attributes each to the
     nearest named character on the line. A character credited with more
     than one colour for a feature is flagged.

  3. Name-variant suspects
     Capitalised tokens that are one edit away from a known character's
     first name but aren't themselves a known name -- likely misspellings.

Names come from the '### Name' headers in characters.md.

Zero third-party dependencies. Python 3.8+.
"""
from __future__ import annotations

import argparse
import glob
import re
import sys
from collections import defaultdict

from textlib import iter_lines, load_names, STOPWORDS

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday",
            "saturday", "sunday"]
_WD = "|".join(WEEKDAYS)
WEEKDAY_RE = re.compile(r"\b(" + _WD + r")\b", re.I)
# A weekday anchored to the *current* day of the scene (not "last Friday").
CUR_DAY_RE = re.compile(
    r"\b(?:it\s+was|it\s+is|it's|today\s+is|this)\s+(" + _WD + r")\b"
    r"|\b(" + _WD + r")\s+(?:morning|afternoon|evening|night)\b", re.I)
COLOURS = {
    "blue", "green", "brown", "hazel", "grey", "gray", "dark", "black",
    "blonde", "blond", "red", "auburn", "golden", "silver", "white",
    "pale", "amber", "light", "chestnut", "copper", "ginger",
}
# Vague descriptors that don't make a colour *conflict* on their own.
VAGUE_COLOURS = {"dark", "light", "pale"}
# Context words signalling a weekday is recalled or anticipated, not present.
NONPRESENT_MARKERS = (
    "had ", "would ", "tomorrow", "yesterday", "next ", "last ", "earlier",
    "later", "upcoming", "coming ", "prospect of", "ago", "by ", "until ",
    "since ", "every ", "before ",
)
FEATURE_RE = re.compile(r"\b([a-z]+)[ -](eyes|eyed|hair|haired)\b", re.I)
NAME_TOKEN_RE = re.compile(r"\b([A-Z][a-z]{2,})\b")
COMMON_CAPS = {
    "the", "he", "she", "it", "they", "but", "and", "his", "her", "their",
    "ian", "jay", "yes", "no", "okay", "monday", "tuesday", "wednesday",
    "thursday", "friday", "saturday", "sunday", "january", "february",
    "march", "april", "may", "june", "july", "august", "september",
    "october", "november", "december", "god", "mr", "mrs", "ms", "dr",
    "turner", "associates", "sir", "mom", "dad", "christmas",
}


# --------------------------------------------------------------------------- #
def day_ledger(lines):
    """Return (mentions, anchored) keyed by (book,chap,scene).

    mentions = every weekday reference (full ledger, reference only).
    anchored = only weekdays tied to the scene's *current* day, used for
    conflict detection so 'last Friday' talk doesn't trip a false alarm.
    """
    mentions = defaultdict(list)
    anchored = defaultdict(list)
    for ln in lines:
        key = (ln.book, ln.chapter, ln.scene)
        for m in WEEKDAY_RE.finditer(ln.text):
            mentions[key].append((ln.lineno, m.group(1).lower()))
        for m in CUR_DAY_RE.finditer(ln.text):
            # Skip anchors inside dialogue (odd number of quotes before the
            # match): characters planning 'Friday dinner' isn't the scene's day.
            if ln.text[:m.start()].count('"') % 2 == 1:
                continue
            # Skip recollection / anticipation ('had explained Thursday',
            # 'prospect of Monday morning') -- not the scene's present day.
            window = ln.text[max(0, m.start() - 35):m.start()].lower()
            if any(w in window for w in NONPRESENT_MARKERS):
                continue
            day = (m.group(1) or m.group(2)).lower()
            anchored[key].append((ln.lineno, day))
    return mentions, anchored


def colour_consistency(lines, first_names):
    # name -> feature -> {colour: [(book,chap,lineno)]}
    seen = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for ln in lines:
        low = ln.text.lower()
        present = [(m.start(), m.group(1))
                   for m in re.finditer(r"\b([a-z]+)\b", low)
                   if m.group(1) in first_names]
        if not present:
            continue
        for m in FEATURE_RE.finditer(ln.text):
            colour = m.group(1).lower()
            if colour not in COLOURS:
                continue
            feature = "hair" if "hair" in m.group(2).lower() else "eyes"
            # require a named character *before* the description on the line;
            # otherwise attribution is a guess, so skip it.
            before = [n for p, n in present if p <= m.start()]
            if not before:
                continue
            owner = before[-1]
            seen[owner][feature][colour].append((ln.book, ln.chapter, ln.lineno))
    return seen


def name_variants(lines, first_names, full_names):
    def edit1(a, b):
        if abs(len(a) - len(b)) > 1:
            return False
        if a == b:
            return False
        # classic DP within distance 1
        la, lb = len(a), len(b)
        if la == lb:
            return sum(x != y for x, y in zip(a, b)) == 1
        # insertion/deletion
        if la > lb:
            a, b = b, a
            la, lb = lb, la
        i = j = 0
        diff = 0
        while i < la and j < lb:
            if a[i] != b[j]:
                diff += 1
                j += 1
                if diff > 1:
                    return False
            else:
                i += 1
                j += 1
        return True

    suspects = defaultdict(lambda: [0, set()])  # token -> [count, {names}]
    for ln in lines:
        for m in NAME_TOKEN_RE.finditer(ln.text):
            # Skip sentence-initial words: capitalised 'Let', 'Time', 'Live'
            # at a sentence start are ordinary words, not misspelled names.
            pre = ln.text[:m.start()].rstrip()
            if not pre or pre[-1] in '.!?:"”':
                continue
            tok = m.group(1)
            low = tok.lower()
            if low in full_names or low in COMMON_CAPS or low in STOPWORDS:
                continue
            for name in first_names:
                if len(name) >= 3 and edit1(low, name):
                    suspects[tok][0] += 1
                    suspects[tok][1].add(name)
                    break
    # A real misspelling is rare; a frequent token is just another word/name.
    return {tok: v for tok, v in suspects.items() if v[0] <= 4}


# --------------------------------------------------------------------------- #
def render(mentions, anchored, colours, variants):
    out = ["# Continuity ledger (auto-generated)", ""]
    out.append("Advisory. Generated by `tools/continuity_check.py`. "
               "Review flags by hand against the timeline/ and characters.md.")
    out.append("")

    # --- weekday conflicts (anchored to the scene's current day) ---
    out.append("## Day/time — scenes spanning more than one current-day weekday")
    out.append("")
    out.append("Counts only weekdays tied to the present (‘it was Friday’, "
               "‘Tuesday morning’); recollection/anticipation/dialogue are "
               "filtered out. A week-summary *montage* legitimately spans "
               "several days — verify those are intentional and that a "
               "single-day scene hasn't drifted. Triage aid, not a verdict.")
    out.append("")
    conflicts = 0
    for key in sorted(k for k in anchored if k[2] is not None):
        days = {d for _l, d in anchored[key]}
        if len(days) > 1:
            conflicts += 1
            refs = ", ".join(f"{d}@L{l}" for l, d in anchored[key])
            out.append(f"- {key[0]} ch{key[1]:02d} scene {key[2]}: "
                       f"{', '.join(sorted(days))} — {refs}")
    if not conflicts:
        out.append("- (none)")
    out.append("")
    out.append("<details><summary>Full weekday-mention ledger (reference)</summary>")
    out.append("")
    for key in sorted(k for k in mentions if k[2] is not None):
        days = ", ".join(f"{d}@L{l}" for l, d in mentions[key])
        out.append(f"- {key[0]} ch{key[1]:02d} sc{key[2]}: {days}")
    out.append("")
    out.append("</details>")
    out.append("")

    # --- colour conflicts (>=2 *specific*, non-vague colours) ---
    out.append("## Eye / hair colour — characters with conflicting descriptions")
    out.append("")
    out.append("Conflict = two specific colours for one feature; vague terms "
               "(dark/light/pale) are listed but don't trigger a flag. "
               "Attribution is to the nearest preceding name and may err.")
    out.append("")
    found = False
    for name in sorted(colours):
        for feature, cmap in colours[name].items():
            specific = [c for c in cmap if c not in VAGUE_COLOURS]
            if len(specific) > 1:
                found = True
                parts = []
                for colour, refs in sorted(cmap.items()):
                    where = ", ".join(f"{b} ch{c:02d}:L{l}" for b, c, l in refs[:3])
                    parts.append(f"**{colour}** ({where})")
                out.append(f"- {name.title()} {feature}: " + " vs ".join(parts))
    if not found:
        out.append("- (no conflicts)")
    out.append("")
    out.append("<details><summary>All colour descriptions collected</summary>")
    out.append("")
    for name in sorted(colours):
        for feature, cmap in colours[name].items():
            summary = ", ".join(f"{col}×{len(refs)}" for col, refs in cmap.items())
            out.append(f"- {name.title()} {feature}: {summary}")
    out.append("")
    out.append("</details>")
    out.append("")

    # --- name variants ---
    out.append("## Name-variant suspects (one edit from a known first name)")
    out.append("")
    ranked = sorted(variants.items(), key=lambda kv: -kv[1][0])
    if not ranked:
        out.append("- (none)")
    for tok, (count, names) in ranked:
        out.append(f"- {tok} — {count}x, near: {', '.join(sorted(names))}")
    out.append("")
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--books", nargs="+",
                    default=sorted(glob.glob("source/book*.txt")))
    ap.add_argument("--characters", default="characters.md")
    ap.add_argument("--out", default="-")
    args = ap.parse_args(argv)
    if not args.books:
        ap.error("no book files found; pass --books")

    lines = list(iter_lines(args.books))
    first_names, full_names = load_names(args.characters)
    mentions, anchored = day_ledger(lines)
    text = render(
        mentions, anchored,
        colour_consistency(lines, first_names),
        name_variants(lines, first_names, full_names),
    )
    if args.out == "-":
        sys.stdout.write(text)
    else:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
