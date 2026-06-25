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

**Bookkeeping:** keep the chapter-count line in `CLAUDE.md`'s status up to date.
No need to log the new chapter anywhere else — this repo is the source of truth,
and divergence from the legacy Novelcrafter export is computed on demand with
`tools/diff_export.py`, not hand-maintained (see `SOURCES.md`).

---

## Step 2 — First editing round (cut the AI out of it)

**Trigger:** a chapter has landed via Step 1 and is ready to be edited in place.

**Premise:** the drafting model writes well but has *tics* — pet phrases,
repeated descriptive patterns, and reflexive habits it reuses across chapters
regardless of the guiding prompt. The job of this round is to strip those out so
the prose reads like one deliberate book and not like a model's defaults. The
result is often shorter and more minimal, and that is the point: **minimal beats
repetitive every time.** When a tic can't be fixed in place, cut it.

Edits are made **directly to `chapters/book*/chapterNN.md`**. The pristine chat
output is preserved in `source/raw/chat-drafts/`, so nothing here is
destructive — that copy is the thing to diff against if a cut goes too far.

The four passes, in order:

1. **Phrase / AI-tic pruning.** Work against the two living lists:
   `guidelines/guidelines.md` (the "avoid these words" line + style rules) and
   `guidelines/ai-tics-watchlist.md` (the graded word/phrase list). Remove,
   replace, or shorten flagged words and phrases. Default to **removal** — a
   tic like "with the grim determination of a man preparing for battle" is cut
   wholesale, not rewritten into a different flourish. Also kill the reflexive
   *reflection* sentences the model adds after a beat ("and it was enough",
   "which would have made it smaller", "for the first time all week") — they
   read as filler.

2. **Speech tags.** Most dialogue in this book is **just Ian and Jay**, so most
   `"…," Ian said` / `"…," Jay said` tags are dead weight — the alternation and
   the voices already say who's talking. Strip them. **Keep a tag only when it
   earns its place:** the first speaker of an exchange, the first line after a
   block of narration (to re-anchor), to disambiguate two lines by the same
   speaker in a row, or in a **group scene** (the office kitchen, the gym
   crowd) where several people speak and the reader needs the name. When you
   drop a tag, fix the punctuation — `"…fine," Jay said.` becomes `"…fine."`,
   not `"…fine,"`.

3. **Sensory / setting descriptions.** The model loves to describe a café, bar,
   restaurant, hotel, or room in the same near-identical pattern every time
   (a list of furnishings, lighting, textures). **Cut these.** Prefer none at
   all. Keep a setting detail **only if it's load-bearing** — it sets up a joke,
   a plot beat, or a callback later in the chapter (e.g. a mirrored wall a
   character later catches a reflection in). Trim everything decorative around
   the one detail that does work. Same rule for over-long bodily/sensory
   pile-ups: keep the ones doing emotional work, cut the inventory.

4. **Continuity.** Make sure the new chapter stays true to the world: names,
   timeline, established facts, character voices. Cross-check against
   `characters.md`, `timeline/`, and the continuity tooling.
   Editing prose shouldn't introduce new facts, but cuts can strand a
   reference — verify nothing dangles.

A fuller, example-driven version of all four passes — including the
keep/cut calls that aren't obvious — lives in
**`guidelines/editing-guidelines.md`**. Read it before editing.

**Tooling.** The `tools/` scripts surface candidates and verify the result;
they don't edit for you:

```bash
python3 tools/lint_guidelines.py      # flags guideline/watchlist hits
python3 tools/scan_text.py            # n-gram / skip-gram repetition scan
python3 tools/echo_check.py           # repeated phrasing across nearby text
python3 tools/continuity_check.py     # name/fact continuity
python3 tools/reformat_chapters.py    # re-validate canonical format when done
```

**Important at this stage:** this is *subtractive* editing — pruning the
draft, not rewriting the story. Don't add plot, don't change what happens,
don't invent new prose to replace a cut. Preserve the jokes, the beats, and
both characters' voices; just remove the model's fingerprints.

---

*Later steps (further editing passes, sync bookkeeping) will be documented
here as we define them.*
