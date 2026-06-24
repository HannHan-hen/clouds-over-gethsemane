# Chapter workflow

How a chapter travels from Claude chat into this repo. This is the living
process doc — each numbered step is a discrete, repeatable stage. Right now
only **Step 1 (intake)** is defined; later editing/QA stages will be added as
we work them out.

The division of labour, briefly: drafting stays in **Claude chat**, where the
prompt can be re-rolled until a scene is right. This repo is where finished
text gets **stored, hand-edited, and quality-checked** — not generated.

---

## Step 1 — Intake (add new material)

**Trigger:** all five scenes of a chapter are finished in chat.

**Input:** the five scenes sent here as Markdown files (one per scene).

**What I do with them:**

1. **Archive the originals, untouched.** Drop the files exactly as received
   into `source/raw/chat-drafts/chapter-NN/` (e.g. `chapter-49/scene-1.md` …
   `scene-5.md`). This folder is read-only — it's the pristine record of what
   came out of chat, kept *because* the working copy gets edited directly. It's
   the baseline a later step can diff hand-edits against, the same way
   `tools/diff_export.py` diffs the manuscript against the Novelcrafter export.

2. **Assemble the working chapter.** Stitch the five scenes into a single
   chapter file in the canonical format (below) and save it as the next chapter
   in sequence:

   - Path: `chapters/book3/chapterNN.md` (Book 3 uses `chapterNN.md`, no
     hyphen, no zero-pad). The next chapter is **49** →
     `chapters/book3/chapter49.md`.
   - Preserve the formatting used by every existing chapter: chapter name at
     the top, then each scene under its own scene-name heading.

3. **Validate the format.** Run the reformatter in dry-run mode — it confirms
   the new file parses to the canonical shape and won't silently merge scenes:

   ```bash
   python3 tools/reformat_chapters.py        # dry run: lists anything off-format
   python3 tools/reformat_chapters.py --write # apply if it flags formatting drift
   ```

   (Note: this tool validates pre-export chapters' scene titles against the
   frozen export. A brand-new chapter like 49 isn't in the export, so it only
   gets the structural/format check — that's expected.)

**Canonical chapter format** (what every `chapters/**.md` file looks like):

```
# Chapter N: Chapter Title

## Scene 1: Scene Title

First paragraph.

Second paragraph.

## Scene 2: Scene Title

...
```

- `#` chapter heading, `##` scene headings.
- One blank line between every heading and paragraph.
- Scene titles come from chat; the chapter title goes on the `#` line.

**Important at this stage:** intake is *additive only* — no copy-editing, no
AI-tic pruning, no continuity fixes. The job here is purely to land the new
material faithfully. Editing the chapter file directly happens afterward (a
later step), with the `source/raw/chat-drafts/` copy preserved as the original.

**Bookkeeping:** because chapter 48+ are ahead of the Novelcrafter export, a new
chapter is a divergence worth logging. Add a one-line note to
`EDITS-FROM-NOVELCRAFTER.md` ("Chapter NN — entirely new, not in export") and
keep the chapter-count line in `claude.md`'s status up to date.

---

*Later steps (editing passes, lint/continuity/echo checks, sync bookkeeping)
will be documented here as we define them.*
