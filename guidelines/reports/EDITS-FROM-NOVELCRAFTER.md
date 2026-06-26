# Edits since the Novelcrafter export

> **Frozen 2026-06-25 — no longer hand-maintained.** This repo is now the
> source of truth; the Novelcrafter export is legacy. Divergence is no longer
> logged by hand — git history records every change, and the *complete, current*
> divergence can be regenerated on demand from the frozen export (see
> "Regenerating" below). This file is kept only as a historical snapshot of the
> early divergence; it is not appended to going forward.

Snapshot of how the working manuscript had diverged from the last Novelcrafter
import, as of the freeze date. If Novelcrafter is ever resubscribed, the best
course is **not** this log but a fresh `tools/diff_export.py` run against the
frozen export, which lists exactly which chapters changed so only those need
re-importing.

## Baseline

- **Export:** `source/raw/2026-06-23-novelcrafter-export/novel.md` (frozen
  snapshot, 2026-06-23). Treat it as read-only — do not edit it, or it stops
  being a faithful baseline.
- **Coverage:** Chapters **1–47**. Chapter 48 did **not** exist at export time.
- **Sync commit:** `52f6961` ("Sync from Novelcrafter full export"). Everything
  in this log happened after it.

## Structural difference (whole manuscript)

The working text (`source/book*.txt`, `chapters/`) uses **named scene titles**
(e.g. "The gift", "Arrival") where the export uses `* * *` scene breaks, and
keeps the **part/arc titles** ("The Arrangement", "Emotional Stakes", …) as
in-line lines rather than `##` headers. This is a global reformatting of the
import, not a content change — a re-import would reintroduce the `* * *` style.

## Prose edits (verified against the export)

Generated and verifiable via `tools/diff_export.py` (see below). As of the
latest run, **3 chapters changed + 1 new chapter**:

### Chapter 33 — character rename
- **Dan Miller → Dan Mercer** (the external senior partner Jay meets).
  Renamed to clear a surname clash with **Ms. Miller** (HR, ch40), who is a
  different person and keeps the Miller name. Commit `494cb7e`.

### Chapter 46 — copy-edit (islands arc), 16 blocks
- AI-tic and repetition pruning, e.g. "Jay returned to his desk and worked" →
  "Jay went back to work"; varied repeated trigrams; cut a "grim efficiency"
  flourish. Commits `c88effc`, `64721e0`, `005acab`.

### Chapter 47 — copy-edit + new scene, 12 blocks
- Same islands-arc AI-tic/copy-edit pass as ch46 (`c88effc`, `64721e0`,
  `005acab`).
- **Added Scene 5**: a "homecoming" draft folded in as a new scene
  (`fa8a376`). This scene is not in the export.

### Chapter 48 — entirely new (not in export)
- Written after the export: drafts "Borrowed reality" then "Undertow"
  (`f81b336`, `f34b771`), plus continuity fixes — vacation chain re-dated into
  early–mid November (`572ee36`), Friday-dinner fix (`a894e48`), market-plan
  fix (`bd85510`). A re-import would not contain this chapter; preserve it.

### Chapter 14 — scene-title typo fix
- **"Quaterly reports" → "Quarterly reports"** (Scene 1 heading). A misspelling
  carried in from the export, corrected in the working copy. The export keeps
  the typo, so `reformat_chapters.py` now reports this title as diverging — that
  warning is expected and advisory.
- Also carries a deliberate `Bonus?` author note at the top of Scene 1 (kept on
  request; not in the export).

> Note: chapters 1–45 (excluding 14 and 33) are unchanged from the export at the
> prose level — only the structural reformatting above applies.

## Regenerating / verifying

The detailed, line-level divergence report is auto-generated at
`guidelines/reports/divergence-from-export.md`. Refresh it any time:

```bash
python3 tools/diff_export.py --out guidelines/reports/divergence-from-export.md
```

It normalises away the cosmetic differences (scene-break style, smart quotes,
dashes) and lists every changed/added/removed paragraph per chapter. **This is
the canonical way to see divergence** — it catches every edit regardless of
whether anything was written up here, which is exactly why hand-logging was
retired. No need to update this file when you edit prose; git history and this
command already have it covered.
