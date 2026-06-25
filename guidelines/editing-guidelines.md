# Editing guidelines — first round

The playbook for Step 2 of the chapter workflow (see `/WORKFLOW.md`). This is
how a freshly-landed chapter gets the AI scrubbed out of it. The examples below
are real before/after pairs from the chapter 48 edit.

**Golden rule:** when in doubt, cut. The drafting model overwrites. A shorter,
plainer line almost always beats a richer one that repeats a pattern the model
has used in ten other chapters. Minimal > repetitive. We edit *down*.

Edits go straight into `chapters/book*/chapterNN.md`. The untouched original is
safe in `source/raw/chat-drafts/`, so cut freely — that copy is the safety net.

---

## 1. Phrase / AI-tic pruning

Source lists: `guidelines.md` (style rules + the "avoid these words" line) and
`ai-tics-watchlist.md` (graded word/phrase list, always growing). The model
treats its pet phrases as vivid writing; the problem is it reaches for the same
ones every chapter. "The grim determination of a man preparing for battle" might
land once — it does not land as a recurring default.

**Default action is removal, not rewriting into a different flourish.**

- Worst offenders (delete or rephrase plainly): `for the first time`,
  `glass wall`, `professional/professionally`, `efficient/efficiency`,
  `thoroughness`, `with grim/cheerful/quiet determination`, `found himself`,
  `the truth was`, `neutral`, `settle`, `rather than`. See the watchlist for the
  full graded set.
- Kill the model's **reflex reflection sentences** — the little summarizing
  coda it tacks onto an emotional beat:
  - *"That was all he said about it, and it was enough. Jay understood the
    whole gesture without a word of it being explained, and he was grateful
    that Ian didn't explain it, because an explanation would have made it
    smaller."* → *"That was all he said about it. Jay understood the whole
    gesture without a word of it being explained."*
  - The trailing "and it was enough" / "made it smaller" / "for the first time
    all week" clauses are filler. Cut them.
- Watch the **subject-opener drumbeat** (the `He … He … He …` / `Jay … Jay …`
  cadence — see the MC-cadence note in `guidelines.md`). Merge runs:
  - *"He took off his jacket and laid it over a chair. He rolled his sleeves to
    the elbow. He took the violin…"* → *"He took off his jacket, laid it over a
    chair, and rolled his sleeves to the elbow. He took the violin…"*
- Cut dead redundancy: *"turned soft and absorbed at once, both at the same
  time"* → *"turned soft and absorbed."*

Don't sanitize a word out of *dialogue* where it's deliberate character voice
or a running joke (e.g. Jay calling a dessert "perfect" three times to be
difficult). Tics are a narration problem first.

---

## 2. Speech tags

Almost every conversation in this book is **Ian and Jay, alone**. In a clean
two-person exchange the alternation tells the reader who's speaking, so `Ian
said` / `Jay said` on every line is noise. Strip it.

**Keep a tag only when it earns its place:**

- the **first** speaker of an exchange (establishes who starts);
- the **first line after a paragraph of narration** (re-anchors the voice);
- to **disambiguate** — two consecutive lines by the same speaker, or a line
  where the alternation could be misread;
- **group scenes.** When the office team or the gym crowd is talking, several
  people speak and the reader needs names — keep the tags there.

When you remove a tag, **fix the punctuation**: the comma that fed the tag
becomes a full stop (or keeps the `?`/`!`).

- *"It's been a week. Grown men recover faster than this," Jay said.* →
  *"It's been a week. Grown men recover faster than this."*
- *"The sentence was finished. Yes. What time," Jay said.* →
  *"The sentence was finished. Yes. What time."* (note: the dangling `,"` must
  become `."`)

Worked example (two-person, tags thinned to anchors only):

> "You're not being silly. … I wouldn't wish that condition on you," **Ian
> said.** ← anchor after narration
> "It's been a week. Grown men recover faster than this."
> "Grown men say so, anyway. I've never seen evidence."
> "And Monday through Wednesday I was useless."
> "Monday through Wednesday you cleared three hundred emails… not a moral
> failing," **Ian said.** ← re-anchor after a long turn

---

## 3. Sensory / setting descriptions

The model's single most repetitive habit: describing a place — café, bar,
restaurant, hotel lobby, spa, gym — with the same shape every time (a list of
furnishings, materials, lighting, a texture or two). They're interchangeable
across chapters and add nothing. **Cut them. Prefer none.**

- *"The café occupied a corner of the conservatory under the palms: marble
  tables, bentwood chairs, lamps with green glass shades. They ate potato soup
  with dark bread…"* → *"They ate potato soup in the café…"*
- *"It was the city's flagship and it behaved like one: a lobby of marble and
  brass, staff who materialized soundlessly, a list of restaurants longer than
  some menus."* → *"It was the city's flagship and it behaved like one."*

**Keep a setting detail only if it's load-bearing** — if a later line depends on
it. Then keep *that detail* and cut the decoration around it:

- The gilded restaurant: drop the mirrors/velvet/leather-menu inventory, but
  **keep the trumpeting cherubs** — Jay jokes about them twice and they pay off
  at the end of the scene.
- The home gym: drop the rowing machine / bench / resistance-band list, but
  **keep the mirrored wall** (Jay catches Ian's reflection in it later) and the
  **two treadmills** (the whole "redundancy" gag and a scene-5 callback).
- The sauna suite: keep the **stove/stones** and **lamp** (both referenced in
  the scene), cut the towel basket and bucket.

Same logic for bodily/sensory pile-ups: keep the ones doing real emotional work
(a character's dawning attraction), cut the ones that are just inventory.

---

## 4. Continuity

Editing prose shouldn't introduce new facts, but **a cut can strand a
reference** — delete a sentence and a later "as he'd said earlier" dangles.
After the prose passes, sanity-check the chapter against the world:

- names and spellings (`characters.md`, including the walk-on registry);
- timeline and sequencing (`timeline/`);
- established facts and relationships;
- both leads' established voices.

Run `tools/continuity_check.py` to catch name/fact drift, and skim for any
reference left hanging by a cut.

---

## Finishing

- Re-validate format: `python3 tools/reformat_chapters.py` (should report no
  changes; it trims stray whitespace and confirms the `#`/`## Scene` layout).
- Re-run `lint_guidelines.py` / `scan_text.py` to confirm the tic count dropped.
- This round is **subtractive**: prune the draft, don't rewrite the story. Keep
  the plot, the jokes, the beats, and both voices — remove the model's
  fingerprints, nothing else.
