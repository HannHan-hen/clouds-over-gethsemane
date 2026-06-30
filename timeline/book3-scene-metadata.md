# Book 3 — Scene Metadata

This file holds the *interpretive* layer that the timeline deliberately leaves
out — POV, theme, mood, purpose. It is the second source the CSV builder joins
onto the facts in `book3-timeline.md`. Keys match the timeline exactly:
`## Chapter <n>` and `### Scene <n>`. Higher-level themes (Book / Arc / Chapter)
are written **once** here and broadcast down onto every scene row by the
builder — so the CSV carries them on every line without anyone hand-repeating.

Run `python3 tools/build_timeline_csv.py` after editing to regenerate
`timeline-events.csv`. The builder warns if a scene here has no timeline match
(or vice-versa), which catches renumbering drift.

<!--
LEGEND — controlled vocabularies. Keep these disciplined; the value of the
counting columns dies if every scene invents its own word.

Central theme — pick exactly ONE per scene from this closed list (extend only
when a scene genuinely fits none; check the list first):
  denial/unnamed feeling · trust · class & money · past wound · protection ·
  domesticity/belonging · work & competence · repressed desire ·
  parallel isolation · power imbalance · ritual/new tradition · external threat

Themes — free, evocative, pipe-separated ("|"). Secondary motifs; filter by
substring in the spreadsheet. This is where "ghosts of the past" lives.

POV — Jay · Ian · Mixed. (Best-effort inference; correct as needed.)

Tension — integer 1–7, calm→charged (a slice-of-life mostly lives 2–4):
  1 serene/idyllic   2 light, easy   3 mild undercurrent
  4 steady, real stakes present   5 charged (friction or longing pressure)
  6 near-rupture / breaking point  7 crisis/peak
Mood carries the *tone* (serenity↔heaviness) in words; Tension is the *charge*.

PARKED (concept, not built): per-lead feeling KPIs (Jay→Ian regard ladder,
Ian→Jay trust curve). Dropped because both saturate by end of Book 2 and the
scale then flatlines — revisit only if a use appears.
-->

## Book
Theme: Summer into winter — wanting; desire surfaces and goes unclaimed, and the fake-couple pretence dissolves the line between game and truth.

## Arc 1: chapters 41-43
Theme: Building a shared world — new traditions and the fortieth-birthday gala; Jay steps fully into Ian's life.

## Arc 2: chapters 44-45
Theme: Closeness tips past the safe line — the gala's afterglow into the hot-springs retreat and the drunken plea neither can keep.

## Arc 3: chapters 46-48
Theme: The pretence dissolves the line — the island game makes the wanting real, and the undertow home makes desire undeniable.

## Chapter 41
Theme: Settling into the post-Gal calm; rituals that braid their lives together.

### Scene 1: Companions
POV: Jay
Central theme: ritual/new tradition
Themes: denial | belonging | gratitude
Mood: warm, tender
Weather: warm, still late-summer evening
Setting: office → after-work restaurant; Jay's flat
Keywords: two-year anniversary, "companions", not-a-business-dinner, confession-to-self
Tension: 2
Purpose: Sets the year's emotional baseline — the "companions" frame both will spend the book failing to name — and confirms Jay is fully, privately in love.

### Scene 2: Obvious favouritism
POV: Jay
Central theme: denial/unnamed feeling
Themes: friendship | class & money | scheming-Leo
Mood: bustling, conspiratorial
Weather: warm summer Saturday
Setting: gym; tailor's; office
Keywords: Rus and the Gal story, tailor fitting, Leo's champagne scheme, "test the waters"
Tension: 2
Purpose: Outside eyes (Leo) name Jay's feeling before Jay will, and fire the starting gun on the gala that drives the whole arc.

### Scene 3: Vanilla and spices
POV: Jay
Central theme: class & money
Themes: love-language | craft | inadequacy
Mood: industrious, fond
Weather: warm, slow summer week
Setting: Jay's kitchen-turned-distillery; office
Keywords: homemade tinctures, grandfather's craft, Tia chosen, "no party hats, no speeches"
Tension: 2
Purpose: Turns the class gap into a love language — Jay's answer to "what do you give a man who has everything" is the one thing only he can make.

### Scene 4: Safe love
POV: Jay
Central theme: denial/unnamed feeling
Themes: repressed desire | past wound | self-effacement
Mood: tender, aching
Weather: warm late summer
Setting: Jay's flat; office lounge
Keywords: "safe love", intrusive thoughts of being touched, "broke my heart", the frightened early days
Tension: 3
Purpose: Names Jay's coping doctrine — want nothing, demand nothing, just keep showing up — the denial engine of the book, while Ian rewrites Jay's shame about who he was at the start.

### Scene 5: Running
POV: Jay
Central theme: ritual/new tradition
Themes: intimacy | care | belonging
Mood: warm, effortful, easy
Weather: warm late-summer evenings by the river
Setting: riverside running path; pool; Friday restaurant
Keywords: Tuesday runs begin, patient coaching, swimming, Friday dinner
Tension: 2
Purpose: Establishes the Tuesday-run ritual whose loss and revival will track their closeness across the rest of the book.

## Chapter 42
Theme: The gala's gravity pulls everyone in; old ghosts and small jealousies surface.

### Scene 1: Excessive is the minimum
POV: Jay
Central theme: class & money
Themes: generosity | found-family | runaway-scale
Mood: brisk, comic excess
Weather: warm late August
Setting: office
Keywords: co-funding Tim's car, embossed invitations, "about a hundred people" (a lie), vacation argument
Tension: 2
Purpose: Sets the gala's runaway scale and re-states the wealth gulf, while Ian quietly wins the right to share Jay's vacation.

### Scene 2: Complications
POV: Mixed
Central theme: past wound
Themes: ghosts-of-the-past | distrust | self-blame
Mood: tender turning cold
Weather: late-August evening
Setting: classical concert hall
Keywords: the concert, Sam Connelly's ghost, Ian goes distant, Ema's invitation surfaces
Tension: 4
Purpose: Surfaces Ian's defining wound to show how it still sabotages tenderness — the haunted concert the island will later be written over.

### Scene 3: The most proper man
POV: Jay
Central theme: class & money
Themes: inadequacy | family-friction | anxiety
Mood: anxious, spiralling
Weather: early September
Setting: tailor's; Jay's flat
Keywords: tailoring complete, Leo's three-country gift hunt, tincture doubt, mother refuses
Tension: 3
Purpose: Sharpens Jay's worth-anxiety — his homemade gift weighed against Leo's globe-spanning one — the doubt the gala's payoff exists to answer.

### Scene 4: Tia Larson
POV: Mixed
Central theme: work & competence
Themes: wariness | possessiveness | found-family
Mood: brash, warm
Weather: early September
Setting: office; Friday welcome drinks
Keywords: Tia starts, ex-military and blunt, welcome drinks, Ian leaves early (privately annoyed)
Tension: 2
Purpose: Replaces Gal with her opposite so the office threat recedes — and shows Ian's quiet possessiveness over their Friday ritual.

### Scene 5: Daring outfit
POV: Mixed
Central theme: denial/unnamed feeling
Themes: jealousy | self-presentation | transformation
Mood: playful, prickly
Weather: early September
Setting: Hathaway's boutique
Keywords: bold floral blazer, Eli the clerk, day-of hairstylist, Ema cleared, Ian pettily jealous
Tension: 3
Purpose: Plants Ian's first overt jealousy (over Eli) and Jay's transformation into someone who can hold the gala's stage.

## Chapter 43
Theme: Jay enters Ian's glittering world; the gift that says what neither will.

### Scene 1: Gold lions and carved dragons
POV: Jay
Central theme: denial/unnamed feeling
Themes: love-language | anticipation | scheming-Leo
Mood: busy, fond, gathering
Weather: mid-September
Setting: Jay's tincture-filled kitchen; office
Keywords: Eli's invitation secured, Tim's car hunt, boxing the three best tinctures, the handwritten note
Tension: 3
Purpose: Loads the gala's emotional payload — the boxed tinctures and the note — and lets Leo again name the thing Jay won't.

### Scene 2: Incandescent
POV: Mixed
Central theme: repressed desire
Themes: transformation | longing | sabotage-comedy
Mood: hectic → breathtaking
Weather: rain cancels the Tuesday run; gala Saturday
Setting: salon prep; the gala staircase
Keywords: Cinderella treatment, Leo's sabotage errands, the staircase entrance, "incandescent"
Tension: 4
Purpose: Delivers the first overwhelming image of Ian's desire — he forgets the entire party at the sight of Jay — the wanting made undeniable to him.

### Scene 3: Ian's world
POV: Jay
Central theme: class & money
Themes: outsider | belonging | "live up to it"
Mood: dazzling, daunting
Weather: September night
Setting: the ballroom gala
Keywords: five hundred guests, old money and an openly queer crowd, orbiting Ian, guarding Ema and Lam
Tension: 4
Purpose: Shows the full scale of the world Jay is an outsider to — and his choice to rise to it rather than flee.

### Scene 4: Not boyfriend
POV: Mixed
Central theme: denial/unnamed feeling
Themes: longing | deflection | the-world-sees-it
Mood: glittering, aching
Weather: September night
Setting: the gala, late
Keywords: the "boyfriend" mistake, deflected advances, Eli meets Ian, fireworks and orchestra
Tension: 4
Purpose: Stages the book's central denial out loud — the room reads them as a couple and both refuse it — Ian aching to claim what he won't.

### Scene 5: You deserve every good thing
POV: Ian
Central theme: repressed desire
Themes: love-language | possessiveness | the-gift
Mood: intimate, raw
Weather: pre-dawn into Sunday
Setting: Ian's home (the gift mountain); Jay's flat
Keywords: three crystal bottles, "You deserve every good thing", red-currant tincture "tastes like his lips", won't share a drop
Tension: 4
Purpose: The gala's emotional climax from Ian's side — a homemade gift outweighs a city of luxury, and his wanting turns nakedly physical and possessive.

## Chapter 44
Theme: Coming down from the gala into a shared autumn; the vacation is born.

### Scene 1: Early darkness
POV: Jay
Central theme: ritual/new tradition
Themes: seasons-turning | care | over-apology
Mood: settling, autumnal
Weather: autumn dark and cold closing in
Setting: office
Keywords: gala apology, the gift "warehouse", Tuesday runs paused until spring, reporting season looming
Tension: 2
Purpose: Marks the seasonal turn — warmth to winter, runs suspended — and sets the housekeeping that will birth the vacation.

### Scene 2: Thoughtful gifts
POV: Jay
Central theme: domesticity/belonging
Themes: intimacy | found-family | seed-planting
Mood: cozy, playful
Weather: cool autumn Saturday
Setting: the floor of Ian's living room
Keywords: two-person sauna voucher, matching gym hoodie, botanical-garden tickets, Leo's gem brooch, the November vacation
Tension: 2
Purpose: The most domestic beat yet — an afternoon on Ian's floor — that quietly plants every later payoff: the sauna, the spring garden date, the vacation itself.

### Scene 3: Smooth sailing
POV: Jay
Central theme: work & competence
Themes: ease | anticipation | the-machine-hums
Mood: smooth, humming
Weather: early October
Setting: office; trip-planning evenings
Keywords: Q4 reports with no overtime, Songbird Islands booked, hot-springs prize trip set, a lost Friday dinner
Tension: 3
Purpose: Shows how frictionless their working life has become and books the two trips that structure the rest of the book.

### Scene 4: Lovesick
POV: Jay
Central theme: repressed desire
Themes: longing | hunger | missed-rituals
Mood: aching, restless
Weather: mid-October, cooling
Setting: office; the drive toward his hometown
Keywords: missed dinners, "why does it feel like I'm starving?", Tim's car delivered, a third lost Friday
Tension: 4
Purpose: Names the hunger directly — starving despite daily contact — denial straining against appetite.

### Scene 5: Pining
POV: Mixed
Central theme: domesticity/belonging
Themes: generosity | found-family | longing
Mood: warm, tender, lonely
Weather: mid-October
Setting: Ian's home (pining over the tincture); Jay's hometown
Keywords: Ian pines alone, Tim's 18th birthday, the car reveal, the stepfather thaws, the botanical-garden truth
Tension: 3
Purpose: Splits the screen — Ian alone with Jay's tincture, Jay's gift healing his family — measuring how far each has come and how much they miss the other.

## Chapter 45
Theme: The retreat strips away distance; the plea Ian must pretend he didn't hear.

### Scene 1: Salt-ocean smell
POV: Jay
Central theme: domesticity/belonging
Themes: anticipation | found-family | proximity-engineered
Mood: giddy, brisk
Weather: cold north; cliff-side hot springs
Setting: office; flight to Ashland; Frostbay Sanctuary
Keywords: winter gear, the ridiculous earflap hat, even Ray comes, paired rooms (Ian with Jay)
Tension: 3
Purpose: Opens the retreat and engineers the proximity — paired rooms — on which the chapter's whole pressure depends.

### Scene 2: Aurora
POV: Mixed
Central theme: repressed desire
Themes: beauty | quiet-happiness | the-most-to-lose
Mood: hushed, luminous
Weather: freezing clear night, aurora over an ocean-edge hot pool
Setting: cliff hot pool; the shared suite
Keywords: the aurora, floor-cushion dinner, wine and heat, "may never have been this happy"
Tension: 2
Purpose: Sets a peak of shared wonder against Ian's private realisation of happiness — raising the stakes of everything he could lose.

### Scene 3: Very interesting wood
POV: Jay
Central theme: repressed desire
Themes: comedy-of-restraint | the-body | near-disaster
Mood: comic, charged
Weather: dangerous cold; recovering on a heated terrace
Setting: a mountain hike gone wrong; the communal sauna
Keywords: near-freeze (no base layers), Ian marches him back, nude northern sauna, "very interesting wood"
Tension: 4
Purpose: Pushes physical desire into the open through comedy — Jay can no longer not-see Ian's body — priming the night's collapse.

### Scene 4: Pitiful plea
POV: Mixed
Central theme: denial/unnamed feeling
Themes: confession | longing | deniable-truth
Mood: drunk, desperate, tender
Weather: bitter cold night
Setting: outside in the cold; the suite
Keywords: over-drinking, "hold me for the rest of my life… just tonight", "I would. God help me, I would.", the unremembered answer
Tension: 6
Purpose: The retreat's emotional peak — both say the truest thing they've said, in the one frame (drunk, dark) that lets them disown it by morning.

### Scene 5: Cruel joke
POV: Mixed
Central theme: denial/unnamed feeling
Themes: retreat | grief | the-mask-back-on
Mood: hollow, fraught
Weather: grey flight home
Setting: Frostbay; the flight; Ian's home alone
Keywords: "nothing happened", the migraine excuse, fraught quiet, Ian falls apart alone
Tension: 5
Purpose: Snaps the denial back into place and pays its cost — Ian undone, in private, by getting exactly what he wanted and refusing it.

## Chapter 46
Theme: The island resets them; rescues and confessions; Ian's breaking point.

### Scene 1: Dispelling doubts
POV: Jay
Central theme: trust
Themes: reassurance | self-worth | reset
Mood: brisk, then gentle
Weather: late October, pre-trip city
Setting: office handovers; beach-clothes shops
Keywords: punishing handover pace, "stop treating it as something you need to earn back", factor-fifty sunscreen
Tension: 3
Purpose: Resets the post-retreat damage — Ian dismantles Jay's debt-anxiety — clearing the ground for the island.

### Scene 2: Encounters
POV: Jay
Central theme: protection
Themes: jealousy | protectiveness | the-running-pattern
Mood: sun-warm, easy
Weather: island sun and sea
Setting: the Songbird Islands cliff resort; the bar
Keywords: two-bedroom suite over the sea, ten days, a woman flirts, Ian's invented dinner reservation
Tension: 3
Purpose: Opens the island and the trip's running engine — Jay draws attention, Ian rescues — the pretext the fake-couple game will soon formalise.

### Scene 3: Nuisance
POV: Jay
Central theme: protection
Themes: harassment | reassurance | sulking-comedy
Mood: lazy, warm, faintly sulky
Weather: bright island morning
Setting: the terrace; the pool
Keywords: a pushy man by the pool, "your warmth isn't a flaw", pointed sulking, Ian's hour of email
Tension: 3
Purpose: Reframes Jay's oldest shame — harassment as his fault — into Ian's protective care, re-healing the wound from his first job.

### Scene 4: Past relationships
POV: Mixed
Central theme: past wound
Themes: confession | trust | parallel-isolation
Mood: candlelit, open
Weather: warm island evening
Setting: the resort's most romantic restaurant
Keywords: Ian's full history (a conditional father, Sam, seven years alone), Jay's (a non-event, "not interesting enough", the harassment)
Tension: 4
Purpose: The mutual confession — each lays out the whole romantic ledger — the deepest trust exchange of the book so far.

### Scene 5: Breaking point
POV: Mixed
Central theme: repressed desire
Themes: breaking-point | role-reversal | care
Mood: charged, then tender
Weather: warm island evening
Setting: the resort; the suite
Keywords: "Jay is not available", "beautiful" (the second time ever), Ian drinks to a shutdown, Jay rescues him
Tension: 6
Purpose: Breaks Ian under the weight of unclaimable nearness and reverses the dynamic — Jay tends Ian — earning the sunset-cruise promise.

## Chapter 47
Theme: The fake-couple game makes the wanting real; the happiest days.

### Scene 1: The game
POV: Jay
Central theme: denial/unnamed feeling
Themes: pretence | first-kiss-feeling | reparation
Mood: electric, playful
Weather: bright island day
Setting: the breakfast terrace; an evening concert
Keywords: "play into the assumption", the knuckle kiss, "this should do it", the violin promise, the concert apology
Tension: 5
Purpose: Launches the book's central device — the pretence that licenses real touch — and lands the knuckle kiss like a first kiss on both.

### Scene 2: The cruise
POV: Jay
Central theme: repressed desire
Themes: slow-dance | inheritance | bickering-comedy
Mood: gaudy, tender
Weather: open sea, two days
Setting: a tacky tourist cruise
Keywords: the loathed cruise, fathers and inheritance, "committing to the bit", a slow dance that becomes real
Tension: 4
Purpose: Lets the pretence shade into the genuine — a "bit" slow dance that becomes a real embrace — while deepening the fathers theme.

### Scene 3: The storm
POV: Mixed
Central theme: denial/unnamed feeling
Themes: domesticity | declaration | inside-the-frame
Mood: cozy, charged
Weather: a storm confining them indoors
Setting: the suite
Keywords: the Brussels/Geneva plan, the dark-green rug, Jay's mortgage, "This is what I want"
Tension: 4
Purpose: Ian's plainest declaration yet — stripped of obligation — still smuggled inside the "friendship" frame they both keep.

### Scene 4: Doing nothing
POV: Jay
Central theme: repressed desire
Themes: near-kiss | hand-holding | bliss
Mood: serene, blissful
Weather: calm bright island day, warm surf
Setting: pool, beach, a long barefoot walk in the surf
Keywords: the doorway near-kiss, an entire day hand-in-hand, the shared sweater that smells of Ian, "never been happier"
Tension: 2
Purpose: The book's calm crest — a whole day hand-in-hand — the wanting briefly satisfied without ever being named.

### Scene 5: Homecoming
POV: Mixed
Central theme: repressed desire
Themes: ending | grief | the-promise
Mood: elegiac, grey
Weather: leaving the sun for a grey, wintry city
Setting: the plane; Jay's cold flat
Keywords: the last day, "Next weekend. Dinner and a drink.", grieving on the floor, the wanting that won't end
Tension: 5
Purpose: Ends the idyll and converts it into a forward promise — the wanting survives the flight home, now without the pretence to hold it.

## Chapter 48
Theme: Grief of re-entry, then desire that can no longer be called anything else.

### Scene 1: The Palm House
POV: Jay
Central theme: protection
Themes: refuge | grief | wordless-care
Mood: grey turning green, tender
Weather: cold grey November; glasshouse warmth
Setting: the recycled-air office; a hidden Victorian glasshouse
Keywords: the four-digit inbox, the Palm House, Ian's own old refuge, soup and candied orange peel
Tension: 3
Purpose: Ian answers Jay's re-entry grief wordlessly by sharing his own private sanctuary — intimacy through place, not speech.

### Scene 2: Friday, Restored
POV: Jay
Central theme: ritual/new tradition
Themes: reframe | restoration | swallowed-words
Mood: warm, wry
Weather: cold November
Setting: the gilded Friday-dinner restaurant
Keywords: the spoiled food critic, "I miss being yours" (swallowed), "an engineering problem, not a moral failing", "a Friday and a Saturday"
Tension: 3
Purpose: Restores the Friday ritual and reframes the post-vacation gloom as solvable — while Jay swallows the truest line he has.

### Scene 3: Climate Adjustment
POV: Jay
Central theme: repressed desire
Themes: keepsake | violin | rebuilding-the-island
Mood: tender, indulgent
Weather: cold November
Setting: gym; Ian's home; a flagship-hotel penthouse pool
Keywords: linen-bound photo albums, Ian plays violin (promise kept), the penthouse pool, "not the island"
Tension: 3
Purpose: Pays off the violin promise and shows Ian literally rebuilding the island at home — refusing to let the closeness end.

### Scene 4: Heat
POV: Jay
Central theme: repressed desire
Themes: desire | sauna | the-dream
Mood: charged, feverish
Weather: cold November
Setting: Ian's home gym; the private sauna
Keywords: the home gym, hands correcting his form, the private sauna (no holiday excuse), the explicit dream, the faked cold
Tension: 5
Purpose: Strips away every alibi — holiday, drink — so Jay's desire becomes undeniable in plain daylight; the dream forces it into consciousness.

### Scene 5: Still Time
POV: Jay
Central theme: denial/unnamed feeling
Themes: care | Christmas-hook | surrender
Mood: festive-tinged, resolved
Weather: cold late November, the festive season creeping in
Setting: Ian's home; a roast hall in the industrial east
Keywords: soup and a medical thermometer, the cold that doesn't exist, "There's still time", Christmas floated, the desire finally accepted
Tension: 4
Purpose: Closes the written book on the turn — Jay stops fighting the desire — and floats Christmas as the next pressure, ending on appetite, not resolution.
