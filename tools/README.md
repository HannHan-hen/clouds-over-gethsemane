# tools/

Manuscript-analysis scripts for building the editing knowledge base while
drafting. **Write first, edit later** — these only generate reports/flags
into `guidelines/`; none of them touch the prose. All are pure Python 3.8+,
zero dependencies, and share `textlib.py` (chapter/scene/line parsing, the
stopword set, dispersion, the character roster).

Run the whole suite:

```bash
for t in scan_text lint_guidelines style_metrics continuity_check echo_check; do
  python3 tools/$t.py --out guidelines/${t/_*/}-*.md   # see each tool's --out below
done
```

| Script | Report | Catches |
|---|---|---|
| `scan_text.py` | `scan-candidates.md` | repeating phrases / cadence tics |
| `lint_guidelines.py` | `lint-report.md` | banned words & constructions |
| `style_metrics.py` | `style-metrics.md` | per-chapter style drift |
| `continuity_check.py` | `continuity-report.md` | day/colour/name continuity |
| `echo_check.py` | `echo-report.md` | distinctive-word echoes |

## scan_text.py

Scans the manuscript for repeating-phrase AI tics, going beyond a plain
contiguous-trigram pass.

Three techniques, each ranked by Gries' **deviation of proportions (DP)** —
how unevenly a phrase is spread across the 48 chapters. A phrase used 18×
evenly (DP≈0.1) is probably the book's voice; 18× clustered in three scenes
(DP≈0.7) is a localized tic worth pruning.

1. **Extended contiguous n-grams (n=3–5)** — the trigram pass, widened.
2. **Templated n-grams** — n-grams with one variable slot (`felt <> a` →
   like / productive / surreal). Merges variant phrasings a fixed trigram
   can't, but only when the slot is a *small closed set* (2–12 fills), so
   "subject + anything" noise is filtered out.
3. **Sentence openers** — the first 1–3 words of every sentence. Catches
   cadence tics ("Jay …", "Through the glass …") invisible to content
   n-grams.

Phrases already in `guidelines/ai-tics-watchlist.md` are tagged `[known]`.

### Usage

```bash
# Full report over source/book*.txt -> guidelines/scan-candidates.md
python3 tools/scan_text.py --out guidelines/scan-candidates.md

# Print to stdout, only frequent phrases, more rows
python3 tools/scan_text.py --min-count 20 --top 60

# Scan one book / arc
python3 tools/scan_text.py --books source/book3.txt
```

Key flags: `--min-count` (whole-manuscript threshold, default 6),
`--min-fillers` / `--max-fillers` (templated slot-diversity window, 2–12),
`--top` (rows per section), `--books`, `--watchlist`, `--out`.

Output is advisory: review hits and promote real ones into the graded tiers
of `guidelines/ai-tics-watchlist.md`.

## lint_guidelines.py

Turns `guidelines.md` from a passive doc into an active check. Flags banned
words and banned constructions per chapter with clickable `file:line` refs.
The banned-word list is **parsed live** from the "Avoid these words" line of
`guidelines.md`, so promoting a word there starts flagging it here the same
day. Construction rules marked `(heuristic)` are deliberately loose (expect
false positives). Advisory — every hit shows the matched text.

```bash
python3 tools/lint_guidelines.py --out guidelines/lint-report.md
```

## style_metrics.py

Per-chapter metrics table to catch **drift**, not single sins — the value is
the time-series. Columns: sentence length mean/SD (low SD = monotone),
filter-verb rate, `-ly` adverb rate, body-part rate, dialogue share. Outliers
(>1 SD worse than the book mean) are marked `!`.

```bash
python3 tools/style_metrics.py --out guidelines/style-metrics.md
```

## continuity_check.py

Three advisory continuity checks, keyed off the `### Name` headers in
`characters.md` and the Novelcrafter character slugs:

1. **Day/time** — weekdays anchored to a scene's present day; scenes spanning
   more than one are surfaced (montages are legitimate — it's a triage aid,
   not a verdict; recollection/anticipation/dialogue are filtered out).
2. **Eye/hair colour** — a character described with two *specific* colours
   for one feature (vague dark/light/pale don't trigger). Attribution is to
   the nearest preceding name and can err.
3. **Name variants** — rare capitalised tokens one edit from a known first
   name (likely misspellings); sentence-initial words are excluded.

```bash
python3 tools/continuity_check.py --out guidelines/continuity-report.md
```

## echo_check.py

Flags *uncommon* content words (length ≥ 7, low book-wide count so names and
ordinary words drop out) reused within a short token window — the local
repeats a reader actually snags on, distinct from the phrase scanner. Rarest
and closest-together first.

```bash
python3 tools/echo_check.py --out guidelines/echo-report.md
```

## textlib.py

Shared library — not a CLI. Single source of truth for manuscript-format
assumptions (the `Chapter N:` / `Scene N` markers), tokenizing, sentence
splitting, the stopword set, Gries' dispersion, and the character roster.
Edit format assumptions here so every tool stays in sync.
