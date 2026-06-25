# Manuscript Sources & Sync State

*Last verified: 2026-06-24. Refresh this section whenever the sources move.*

## What the source files are

The manuscript exists in three parallel forms; they share a common ancestor
and are kept loosely in sync:

| Location | Role | Format |
|---|---|---|
| `source/raw/2026-06-23-novelcrafter-export/novel.md` | **Frozen baseline** — the newest Novelcrafter export (2026-06-23). Treat as read-only. Covers ch1–47. | `###`/`####` headers, `* * *` scene breaks |
| `source/book{1,2,3}.txt` | Plain-text compile used by the `tools/` analysis scripts. Synced from the export. | `Chapter N:` / `Scene N` + title line, no blank separators |
| `chapters/book{1,2,3}/*.md` | **Working copy** (the readable manuscript), ch1–48. | `# Chapter N: Title` / `## Scene K: Title`, blank-line separated |

The `2026-01-21 *.docx` files under `source/raw/` are the **older** January
export and are superseded — kept only as historical artifacts.

## Provenance

- The `.md` chapters were originally extracted from `book*.txt`.
- Commit `52f6961` ("Sync from Novelcrafter full export") added the 2026-06-23
  export and re-synced both `book*.txt` and most `.md` chapters from it. So all
  three forms descend from the same newest export — the `.txt` files are **not**
  stale leftovers from the January docx.
- Since that sync: ch33 was edited (Dan Miller→Dan Mercer), ch46–47 were
  copy-edited, ch47 gained a new Scene 5 ("Homecoming"), and ch48 ("Undertow")
  was written fresh. **Chapters 46–48 in the `.md` files are the most recent
  text and are ahead of the export.** See `EDITS-FROM-NOVELCRAFTER.md`.

## Where the `.md` working copy stands vs the newest export

Verified by diffing `chapters/*.md` directly against the export (normalising
quotes/dashes/whitespace). **43 of 47 chapters are identical to the export.**
The only divergences:

- **ch14** — carries a stray `Bonus?` draft note at the top of Scene 1
  (a deliberate author reminder, kept on request; not in the export/`.txt`).
- **ch33** — Dan Mercer rename (intentional, logged).
- **ch46** — islands-arc copy-edit, ~16 blocks (intentional, logged).
- **ch47** — copy-edit + added Scene 5 "Homecoming", ~12 blocks (intentional, logged).
- **ch48** — entirely new chapter, not in the export (intentional).

Scene structure is fully intact: every chapter's scene count and titles match
the export (ch47 has the extra "Homecoming"; ch48's five titles are original).
**No scene titles are missing.**

## Formatting/sync cleanup done 2026-06-24

- Reformatted ch12–48 `.md` to the canonical `#`/`## Scene K:` + blank-line
  layout chapter 1 uses (they had degraded: lost markdown headers, scene titles
  on bare lines, no paragraph separators). Structure only — no prose changed.
  Tool: `tools/reformat_chapters.py` (idempotent, validates against the export).
- **ch15** — removed a stray `Freefall` line (an arc-divider that had leaked
  onto the end of the file during the original extraction).
- **ch20** — restored a final paragraph that the `.md` had dropped ("Ian
  wondered how he could continue pretending…"), and re-synced its opening two
  paragraphs to the export's newer wording (the `.md` had an older draft that
  repeated "aggressive"; export/`.txt` agree on the cleaner phrasing).

## How to re-verify

```bash
# Drift of book*.txt vs the export (human summary in EDITS-FROM-NOVELCRAFTER.md):
python3 tools/diff_export.py --out guidelines/divergence-from-export.md
# Re-normalise chapter markdown (dry run lists anything off-format):
python3 tools/reformat_chapters.py
```

Note: `diff_export.py` compares `book*.txt` to the export, **not** the `.md`
files. The ch14/ch20 `.md`-only differences above don't show up there because
they live in the `.md` working copy, which `diff_export.py` doesn't read.
