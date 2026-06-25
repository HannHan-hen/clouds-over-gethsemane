# Clouds Over Gethsemane

## What this project is

This is a **writing project** — a long-form fiction series — and nothing more
commercial than that. I (the human) am weaving a story for myself: I invent the
plot and the characters, and I direct everything that happens. The AI's job is
to **execute the prose** and do the technical work around it. I steer; the robot
writes and tidies.

It has been going for over a year, and we are currently deep into **Book Three**.
The characters started as bare templates and have since grown into people with
pasts, habits, quirks, hopes, and dreams — Ian and Jay especially. A lot of who
they are crystallized through the act of writing them.

**The order of operations is: write first, edit later.** The point is to keep the
story moving. We *do* maintain a small toolkit for checking and editing the prose
(see `tools/`), and we occasionally run it over older chapters, but polishing
never blocks new material. Earlier chapters will get a proper revision pass at
some point, and character details that surface as we write get folded back into
the reference files.

So a session here is some mix of:

- **Intake** — landing a finished chapter into the repo in the established format.
- **Editing** — the AI-tic / cleanup pass on a freshly-landed chapter.
- **Everything else** — brainstorming, untangling a scene, checking for errors,
  and asking whether the prose actually does what I intended and what should change.

## How this repo came to be

The novel was originally written and managed in **Novelcrafter** — that's where
the `source/raw/` exports come from. I've since cancelled that subscription and
am moving the workflow into this repo to see what works. The newest export
(`source/raw/2026-06-23-novelcrafter-export/`) is the state of the novel at the
moment of the switch and serves as the **frozen baseline**; everything after
ch48 is written the new way.

We *did* work in this repo on and off before the switch, but only sporadically,
so **expect the occasional old leftover** — a stray draft note, an out-of-sync
chapter, a half-finished experiment. When something looks off or contradicts the
rest, it's probably one of these; flag it rather than treating it as canon.
`SOURCES.md` tracks how the manuscript forms relate and what's currently in sync.

## How we work

Drafting happens in **regular Claude chat**, where a scene can be re-rolled until
it's right. This repo is where finished text gets **stored, edited, and
quality-checked** — not generated. The usual loop:

1. I write a whole chapter's worth of scenes in chat.
2. I paste them here; they get assembled into the next chapter `.md` file in the
   canonical format.
3. The AI runs the editing pass against the guidelines.
4. I do a final manual pass, cutting whatever I don't like.

The full process — intake rules, the canonical chapter format, and the editing
passes — lives in **`WORKFLOW.md`**. The writing/style rules the editing pass
enforces live in **`guidelines/guidelines.md`** (with the fuller AI-tic list in
`guidelines/ai-tics-watchlist.md` and worked examples in
`guidelines/editing-guidelines.md`). Read those before editing prose.

---

## The story so far

**Clouds Over Gethsemane** is a slowburn BL (Boys' Love) romance set in
high-stakes finance. It follows the gradual development of feelings between
**Ian Hagen**, a brilliant but emotionally guarded CFO, and **Jay Hall**, his
new assistant escaping a traumatic workplace. Against the backdrop of Turner &
Associates, a prestigious investment firm, the two navigate their growing
attraction while grappling with past wounds, class disparity, and the power
imbalance between boss and assistant. It is a story told through accumulated
moments rather than dramatic declarations.

- **Book 1** (complete, 20 ch) — Jay's first year: from his desperate arrival
  after fleeing harassment to becoming Ian's indispensable assistant. Ian moves
  from paranoid suspicion to acknowledged (but hopeless) love; Jay refuses a
  promotion to stay, still reading his own feelings as admiration.
- **Book 2** (complete, 20 ch) — deepening intimacy through shared trauma and
  domestic closeness: revealed pasts, a job-search crisis Jay resolves by
  staying, and Ian destroying a predator's career to protect him. Their bond is
  unbreakable; neither names it.
- **Book 3** (in progress, 8 ch) — Ian's 40th birthday, new traditions, a
  hot-springs retreat and a ten-day island vacation where a "fake couple"
  pretense dissolves the line between game and truth. Both are deeper in love
  than ever and still haven't confessed.

The **relationship dynamic** runs on a power imbalance (boss/assistant,
wealthy/struggling), mutual protection, parallel isolation, and slow mutual
denial — each reads romantic feeling as professional respect. The slowburn works
because both have real reasons to keep distance yet are genuinely compatible.

For a brief chapter-by-chapter overview, see **`summary.md`**; for the
detailed, dated, scene-by-scene chronology, see **`timeline/`**.

---

## Main characters

The two leads are the heart of the project. These are the working sketches; the
full, evolving cast — supporting team, family, antagonists, walk-ons, and
relationship dynamics — lives in **`characters.md`**, which is where new detail
gets recorded as it surfaces.

### Ian Hagen

- **Age:** 38 at series start, turns 40 in Book 3.
- **Position:** Chief Financial Officer at Turner & Associates.
- **Background:** Old money, elite education, extreme privilege — effortless
  sophistication.
- **Core:** Brilliant, disciplined, intensely private, emotionally guarded.
  Legendary in the office for his coldness toward romance and a punishing work
  ethic; a patient teacher and quietly protective beneath the reserve. Plays
  violin, has essentially no personal life, best friends with Leo Turner.
- **Wound:** Betrayed years ago by Sam Connelly, a corporate spy posing as his
  secretary whom he'd fallen for. It cost him his job, his father's respect, and
  left him with deep trust issues — which is exactly why his feelings for an
  attractive new assistant terrify him.
- **Arc:** Suspicion → reluctant respect → protective care → acknowledged love
  he believes is hopeless and impossible.

### Jay Hall

- **Age:** 29 at series start, turns 30 in Book 1.
- **Position:** Executive Assistant to Ian Hagen.
- **Background:** Modest upbringing — born to an unwed teenage mother, raised by
  a bitter grandmother, third-tier university on a tight budget. Always an
  outsider.
- **Core:** Earnest, diligent, deeply anxious about his credentials and worth.
  Introverted and socially exhausted but performs normalcy; intellectually
  curious, studies economics to compensate for a "lesser" education. Genuinely
  kind, no hidden agendas. Values safety and stability above advancement;
  financially cautious and disciplined.
- **Wound:** Fled his previous job over sexual harassment; carries shame about
  his background and a fear of being valued only for his looks rather than his
  competence.
- **Arc:** A scared, broke man hiding in plain sight → genuine happiness and
  belonging, and feelings he can't yet name. By the end of Book 1 he refuses a
  promotion because being Ian's assistant is what he truly wants.

---

## Repository map

Where to look — and where things belong:

| Path | What it holds |
|---|---|
| `chapters/book{1,2,3}/` | The working manuscript (`.md`), the readable copy we edit. |
| `summary.md` | Brief chapter-by-chapter overview, condensed from `timeline/` (Books 1–2; further books added as their timelines are built). |
| `characters.md` | Full character reference — leads, supporting cast, family, walk-ons. |
| `timeline/` | Detailed scene-by-scene, dated chronology — the source of truth the summaries condense (Books 1–2 complete). |
| `WORKFLOW.md` | The chapter pipeline: intake, format, and the editing passes. |
| `guidelines/` | Writing rules (`guidelines.md`), AI-tic watchlist, editing playbook, and generated QA reports. |
| `tools/` | The check/edit scripts (lint, repetition scan, continuity, reformat). See `tools/README.md`. |
| `source/` | Source forms of the manuscript (`book*.txt`, the Novelcrafter export, pristine chat drafts). |
| `SOURCES.md` | How the three manuscript forms relate and their current sync state. |
| `EDITS-FROM-NOVELCRAFTER.md` | Log of where the working copy diverges from the frozen export. |
| `plans/` | Notes and plans for possible variations/spin-offs. |
