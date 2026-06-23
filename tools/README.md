# tools/

## scan_text.py

Scans the manuscript for repeating-phrase AI tics, going beyond a plain
contiguous-trigram pass. Zero dependencies (pure Python 3.8+).

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
