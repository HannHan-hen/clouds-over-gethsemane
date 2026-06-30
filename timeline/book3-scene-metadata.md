# Book 3 — Scene Metadata

This file holds the *interpretive* layer that the timeline deliberately leaves
out — POV, theme, mood, purpose. It is the second source the CSV builder joins
onto the facts in `book3-timeline.md`. Keys match the timeline exactly:
`## Chapter <n>` and `### Scene <n>`. Higher-level themes (Book / Arc / Chapter)
are written **once** here and broadcast down onto every scene row by the
builder — so the CSV carries them on every line without anyone hand-repeating.

Each field sits on its own line with a hard line-break (two trailing spaces),
matching the timeline files, so it renders one-per-line on GitHub. Keep the
controlled-vocabulary columns disciplined — their value dies if every scene
invents its own word.

Run `python3 tools/build_timeline_csv.py` after editing to regenerate
`timeline-events.csv`. The builder warns if a scene here has no timeline match
(or vice-versa), which catches renumbering drift.

<!--
LEGEND — controlled vocabularies.

Arcs are fixed 5-chapter blocks (4 per 20-chapter book):
  Arc 1 = ch 41-45 · Arc 2 = ch 46-50 (Book 3 in progress; 46-48 written here).

Central theme — pick exactly ONE per scene from this closed list (extend only
when a scene genuinely fits none; check the list first):
  denial/unnamed feeling · trust · class & money · past wound · protection ·
  domesticity/belonging · work & competence · repressed desire ·
  parallel isolation · power imbalance · ritual/new tradition · external threat

Motifs — free, evocative, pipe-separated ("|"). Secondary recurring images;
filter by substring in the spreadsheet. This is where "ghosts-of-the-past"
lives. (Renamed from "Themes" so it doesn't blur with Central theme.)

Mood — ONE word, the most prevalent tone, from this closed list:
  serene · tender · warm · playful · giddy · comic · anxious · longing ·
  charged · tense · hollow · bittersweet · elegiac · festive
(Mood is the tone/valence; Tension is the separate charge axis below.)

Setting — ONE canonical place, the primary location, from this closed list
(reuse names rather than minute detail, so the column stays filterable):
  Jay's apartment · Jay's old flat · Ian's penthouse · T&A · Rus's gym ·
  restaurant · riverside · pub/bar · tailor's · Hathaway's · concert hall ·
  the gala · Frostbay Sanctuary · Songbird Islands · the cruise ·
  the Palm House · hotel penthouse · Jay's hometown · travel

POV — Jay · Ian · Mixed. (Best-effort inference; correct as needed.)

Tension — integer 1-7, calm->charged (a slice-of-life mostly lives 2-4):
  1 serene/idyllic   2 light, easy   3 mild undercurrent
  4 steady, real stakes present   5 charged (friction or longing pressure)
  6 near-rupture / breaking point  7 crisis/peak

PARKED (concept, not built): per-lead feeling KPIs (Jay->Ian regard ladder,
Ian->Jay trust curve). Dropped because both saturate by end of Book 2 and the
scale then flatlines — revisit only if a use appears.
-->

## Book
Theme: Summer into winter — wanting; desire surfaces and goes unclaimed, and the fake-couple pretence dissolves the line between game and truth.

## Arc 1: chapters 41-45
Theme: Building a shared world — new traditions, the fortieth-birthday gala, and a hot-springs retreat where closeness first tips past the safe line.

## Arc 2: chapters 46-50
Theme: The island pretence dissolves the line between game and truth; the undertow home makes desire undeniable.

## Chapter 41
Theme: Settling into the post-Gal calm; rituals that braid their lives together.

### Scene 1: Companions
POV: Jay  
Central theme: ritual/new tradition  
Motifs: denial | belonging | gratitude  
Mood: tender  
Weather: warm, still late-summer evening  
Setting: restaurant  
Keywords: two-year anniversary, "companions", not-a-business-dinner, confession-to-self  
Tension: 2  
Purpose: Sets the year's emotional baseline — the "companions" frame both will spend the book failing to name — and confirms Jay is fully, privately in love.

### Scene 2: Obvious favouritism
POV: Jay  
Central theme: denial/unnamed feeling  
Motifs: friendship | class & money | scheming-Leo  
Mood: playful  
Weather: warm summer Saturday  
Setting: T&A  
Keywords: Rus and the Gal story, tailor fitting, Leo's champagne scheme, "test the waters"  
Tension: 2  
Purpose: Outside eyes (Leo) name Jay's feeling before Jay will, and fire the starting gun on the gala that drives the whole arc.

### Scene 3: Vanilla and spices
POV: Jay  
Central theme: class & money  
Motifs: love-language | craft | inadequacy  
Mood: warm  
Weather: warm, slow summer week  
Setting: Jay's apartment  
Keywords: homemade tinctures, grandfather's craft, Tia chosen, "no party hats, no speeches"  
Tension: 2  
Purpose: Turns the class gap into a love language — Jay's answer to "what do you give a man who has everything" is the one thing only he can make.

### Scene 4: Safe love
POV: Jay  
Central theme: denial/unnamed feeling  
Motifs: repressed desire | past wound | self-effacement  
Mood: longing  
Weather: warm late summer  
Setting: T&A  
Keywords: "safe love", intrusive thoughts of being touched, "broke my heart", the frightened early days  
Tension: 3  
Purpose: Names Jay's coping doctrine — want nothing, demand nothing, just keep showing up — the denial engine of the book, while Ian rewrites Jay's shame about who he was at the start.

### Scene 5: Running
POV: Jay  
Central theme: ritual/new tradition  
Motifs: intimacy | care | belonging  
Mood: warm  
Weather: warm late-summer evenings by the river  
Setting: riverside  
Keywords: Tuesday runs begin, patient coaching, swimming, Friday dinner  
Tension: 2  
Purpose: Establishes the Tuesday-run ritual whose loss and revival will track their closeness across the rest of the book.

## Chapter 42
Theme: The gala's gravity pulls everyone in; old ghosts and small jealousies surface.

### Scene 1: Excessive is the minimum
POV: Jay  
Central theme: class & money  
Motifs: generosity | found-family | runaway-scale  
Mood: comic  
Weather: warm late August  
Setting: T&A  
Keywords: co-funding Tim's car, embossed invitations, "about a hundred people" (a lie), vacation argument  
Tension: 2  
Purpose: Sets the gala's runaway scale and re-states the wealth gulf, while Ian quietly wins the right to share Jay's vacation.

### Scene 2: Complications
POV: Mixed  
Central theme: past wound  
Motifs: ghosts-of-the-past | distrust | self-blame  
Mood: tense  
Weather: late-August evening  
Setting: concert hall  
Keywords: the concert, Sam Connelly's ghost, Ian goes distant, Ema's invitation surfaces  
Tension: 4  
Purpose: Surfaces Ian's defining wound to show how it still sabotages tenderness — the haunted concert the island will later be written over.

### Scene 3: The most proper man
POV: Jay  
Central theme: class & money  
Motifs: inadequacy | family-friction | anxiety  
Mood: anxious  
Weather: early September  
Setting: tailor's  
Keywords: tailoring complete, Leo's three-country gift hunt, tincture doubt, mother refuses  
Tension: 3  
Purpose: Sharpens Jay's worth-anxiety — his homemade gift weighed against Leo's globe-spanning one — the doubt the gala's payoff exists to answer.

### Scene 4: Tia Larson
POV: Mixed  
Central theme: work & competence  
Motifs: wariness | possessiveness | found-family  
Mood: playful  
Weather: early September  
Setting: T&A  
Keywords: Tia starts, ex-military and blunt, welcome drinks, Ian leaves early (privately annoyed)  
Tension: 2  
Purpose: Replaces Gal with her opposite so the office threat recedes — and shows Ian's quiet possessiveness over their Friday ritual.

### Scene 5: Daring outfit
POV: Mixed  
Central theme: denial/unnamed feeling  
Motifs: jealousy | self-presentation | transformation  
Mood: playful  
Weather: early September  
Setting: Hathaway's  
Keywords: bold floral blazer, Eli the clerk, day-of hairstylist, Ema cleared, Ian pettily jealous  
Tension: 3  
Purpose: Plants Ian's first overt jealousy (over Eli) and Jay's transformation into someone who can hold the gala's stage.

## Chapter 43
Theme: Jay enters Ian's glittering world; the gift that says what neither will.

### Scene 1: Gold lions and carved dragons
POV: Jay  
Central theme: denial/unnamed feeling  
Motifs: love-language | anticipation | scheming-Leo  
Mood: warm  
Weather: mid-September  
Setting: Jay's apartment  
Keywords: Eli's invitation secured, Tim's car hunt, boxing the three best tinctures, the handwritten note  
Tension: 3  
Purpose: Loads the gala's emotional payload — the boxed tinctures and the note — and lets Leo again name the thing Jay won't.

### Scene 2: Incandescent
POV: Mixed  
Central theme: repressed desire  
Motifs: transformation | longing | sabotage-comedy  
Mood: charged  
Weather: rain cancels the Tuesday run; gala Saturday  
Setting: the gala  
Keywords: Cinderella treatment, Leo's sabotage errands, the staircase entrance, "incandescent"  
Tension: 4  
Purpose: Delivers the first overwhelming image of Ian's desire — he forgets the entire party at the sight of Jay — the wanting made undeniable to him.

### Scene 3: Ian's world
POV: Jay  
Central theme: class & money  
Motifs: outsider | belonging | live-up-to-it  
Mood: charged  
Weather: September night  
Setting: the gala  
Keywords: five hundred guests, old money and an openly queer crowd, orbiting Ian, guarding Ema and Lam  
Tension: 4  
Purpose: Shows the full scale of the world Jay is an outsider to — and his choice to rise to it rather than flee.

### Scene 4: Not boyfriend
POV: Mixed  
Central theme: denial/unnamed feeling  
Motifs: longing | deflection | the-world-sees-it  
Mood: longing  
Weather: September night  
Setting: the gala  
Keywords: the "boyfriend" mistake, deflected advances, Eli meets Ian, fireworks and orchestra  
Tension: 4  
Purpose: Stages the book's central denial out loud — the room reads them as a couple and both refuse it — Ian aching to claim what he won't.

### Scene 5: You deserve every good thing
POV: Ian  
Central theme: repressed desire  
Motifs: love-language | possessiveness | the-gift  
Mood: longing  
Weather: pre-dawn into Sunday  
Setting: Ian's penthouse  
Keywords: three crystal bottles, "You deserve every good thing", red-currant tincture "tastes like his lips", won't share a drop  
Tension: 4  
Purpose: The gala's emotional climax from Ian's side — a homemade gift outweighs a city of luxury, and his wanting turns nakedly physical and possessive.

## Chapter 44
Theme: Coming down from the gala into a shared autumn; the vacation is born.

### Scene 1: Early darkness
POV: Jay  
Central theme: ritual/new tradition  
Motifs: seasons-turning | care | over-apology  
Mood: bittersweet  
Weather: autumn dark and cold closing in  
Setting: T&A  
Keywords: gala apology, the gift "warehouse", Tuesday runs paused until spring, reporting season looming  
Tension: 2  
Purpose: Marks the seasonal turn — warmth to winter, runs suspended — and sets the housekeeping that will birth the vacation.

### Scene 2: Thoughtful gifts
POV: Jay  
Central theme: domesticity/belonging  
Motifs: intimacy | found-family | seed-planting  
Mood: playful  
Weather: cool autumn Saturday  
Setting: Ian's penthouse  
Keywords: two-person sauna voucher, matching gym hoodie, botanical-garden tickets, Leo's gem brooch, the November vacation  
Tension: 2  
Purpose: The most domestic beat yet — an afternoon on Ian's floor — that quietly plants every later payoff: the sauna, the spring garden date, the vacation itself.

### Scene 3: Smooth sailing
POV: Jay  
Central theme: work & competence  
Motifs: ease | anticipation | the-machine-hums  
Mood: warm  
Weather: early October  
Setting: T&A  
Keywords: Q4 reports with no overtime, Songbird Islands booked, hot-springs prize trip set, a lost Friday dinner  
Tension: 3  
Purpose: Shows how frictionless their working life has become and books the two trips that structure the rest of the book.

### Scene 4: Lovesick
POV: Jay  
Central theme: repressed desire  
Motifs: longing | hunger | missed-rituals  
Mood: longing  
Weather: mid-October, cooling  
Setting: T&A  
Keywords: missed dinners, "why does it feel like I'm starving?", Tim's car delivered, a third lost Friday  
Tension: 4  
Purpose: Names the hunger directly — starving despite daily contact — denial straining against appetite.

### Scene 5: Pining
POV: Mixed  
Central theme: domesticity/belonging  
Motifs: generosity | found-family | longing  
Mood: longing  
Weather: mid-October  
Setting: Jay's hometown  
Keywords: Ian pines alone, Tim's 18th birthday, the car reveal, the stepfather thaws, the botanical-garden truth  
Tension: 3  
Purpose: Splits the screen — Ian alone with Jay's tincture, Jay's gift healing his family — measuring how far each has come and how much they miss the other.

## Chapter 45
Theme: The retreat strips away distance; the plea Ian must pretend he didn't hear.

### Scene 1: Salt-ocean smell
POV: Jay  
Central theme: domesticity/belonging  
Motifs: anticipation | found-family | proximity-engineered  
Mood: giddy  
Weather: cold north; cliff-side hot springs  
Setting: Frostbay Sanctuary  
Keywords: winter gear, the ridiculous earflap hat, even Ray comes, paired rooms (Ian with Jay)  
Tension: 3  
Purpose: Opens the retreat and engineers the proximity — paired rooms — on which the chapter's whole pressure depends.

### Scene 2: Aurora
POV: Mixed  
Central theme: repressed desire  
Motifs: beauty | quiet-happiness | the-most-to-lose  
Mood: serene  
Weather: freezing clear night, aurora over an ocean-edge hot pool  
Setting: Frostbay Sanctuary  
Keywords: the aurora, floor-cushion dinner, wine and heat, "may never have been this happy"  
Tension: 2  
Purpose: Sets a peak of shared wonder against Ian's private realisation of happiness — raising the stakes of everything he could lose.

### Scene 3: Very interesting wood
POV: Jay  
Central theme: repressed desire  
Motifs: comedy-of-restraint | the-body | near-disaster  
Mood: comic  
Weather: dangerous cold; recovering on a heated terrace  
Setting: Frostbay Sanctuary  
Keywords: near-freeze (no base layers), Ian marches him back, nude northern sauna, "very interesting wood"  
Tension: 4  
Purpose: Pushes physical desire into the open through comedy — Jay can no longer not-see Ian's body — priming the night's collapse.

### Scene 4: Pitiful plea
POV: Mixed  
Central theme: denial/unnamed feeling  
Motifs: confession | longing | deniable-truth  
Mood: longing  
Weather: bitter cold night  
Setting: Frostbay Sanctuary  
Keywords: over-drinking, "hold me for the rest of my life… just tonight", "I would. God help me, I would.", the unremembered answer  
Tension: 6  
Purpose: The retreat's emotional peak — both say the truest thing they've said, in the one frame (drunk, dark) that lets them disown it by morning.

### Scene 5: Cruel joke
POV: Mixed  
Central theme: denial/unnamed feeling  
Motifs: retreat | grief | the-mask-back-on  
Mood: hollow  
Weather: grey flight home  
Setting: Frostbay Sanctuary  
Keywords: "nothing happened", the migraine excuse, fraught quiet, Ian falls apart alone  
Tension: 5  
Purpose: Snaps the denial back into place and pays its cost — Ian undone, in private, by getting exactly what he wanted and refusing it.

## Chapter 46
Theme: The island resets them; rescues and confessions; Ian's breaking point.

### Scene 1: Dispelling doubts
POV: Jay  
Central theme: trust  
Motifs: reassurance | self-worth | reset  
Mood: warm  
Weather: late October, pre-trip city  
Setting: T&A  
Keywords: punishing handover pace, "stop treating it as something you need to earn back", factor-fifty sunscreen  
Tension: 3  
Purpose: Resets the post-retreat damage — Ian dismantles Jay's debt-anxiety — clearing the ground for the island.

### Scene 2: Encounters
POV: Jay  
Central theme: protection  
Motifs: jealousy | protectiveness | the-running-pattern  
Mood: warm  
Weather: island sun and sea  
Setting: Songbird Islands  
Keywords: two-bedroom suite over the sea, ten days, a woman flirts, Ian's invented dinner reservation  
Tension: 3  
Purpose: Opens the island and the trip's running engine — Jay draws attention, Ian rescues — the pretext the fake-couple game will soon formalise.

### Scene 3: Nuisance
POV: Jay  
Central theme: protection  
Motifs: harassment | reassurance | sulking-comedy  
Mood: playful  
Weather: bright island morning  
Setting: Songbird Islands  
Keywords: a pushy man by the pool, "your warmth isn't a flaw", pointed sulking, Ian's hour of email  
Tension: 3  
Purpose: Reframes Jay's oldest shame — harassment as his fault — into Ian's protective care, re-healing the wound from his first job.

### Scene 4: Past relationships
POV: Mixed  
Central theme: past wound  
Motifs: confession | trust | parallel-isolation  
Mood: bittersweet  
Weather: warm island evening  
Setting: Songbird Islands  
Keywords: Ian's full history (a conditional father, Sam, seven years alone), Jay's (a non-event, "not interesting enough", the harassment)  
Tension: 4  
Purpose: The mutual confession — each lays out the whole romantic ledger — the deepest trust exchange of the book so far.

### Scene 5: Breaking point
POV: Mixed  
Central theme: repressed desire  
Motifs: breaking-point | role-reversal | care  
Mood: charged  
Weather: warm island evening  
Setting: Songbird Islands  
Keywords: "Jay is not available", "beautiful" (the second time ever), Ian drinks to a shutdown, Jay rescues him  
Tension: 6  
Purpose: Breaks Ian under the weight of unclaimable nearness and reverses the dynamic — Jay tends Ian — earning the sunset-cruise promise.

## Chapter 47
Theme: The fake-couple game makes the wanting real; the happiest days.

### Scene 1: The game
POV: Jay  
Central theme: denial/unnamed feeling  
Motifs: pretence | first-kiss-feeling | reparation  
Mood: charged  
Weather: bright island day  
Setting: Songbird Islands  
Keywords: "play into the assumption", the knuckle kiss, "this should do it", the violin promise, the concert apology  
Tension: 5  
Purpose: Launches the book's central device — the pretence that licenses real touch — and lands the knuckle kiss like a first kiss on both.

### Scene 2: The cruise
POV: Jay  
Central theme: repressed desire  
Motifs: slow-dance | inheritance | bickering-comedy  
Mood: playful  
Weather: open sea, two days  
Setting: the cruise  
Keywords: the loathed cruise, fathers and inheritance, "committing to the bit", a slow dance that becomes real  
Tension: 4  
Purpose: Lets the pretence shade into the genuine — a "bit" slow dance that becomes a real embrace — while deepening the fathers theme.

### Scene 3: The storm
POV: Mixed  
Central theme: denial/unnamed feeling  
Motifs: domesticity | declaration | inside-the-frame  
Mood: tender  
Weather: a storm confining them indoors  
Setting: Songbird Islands  
Keywords: the Brussels/Geneva plan, the dark-green rug, Jay's mortgage, "This is what I want"  
Tension: 4  
Purpose: Ian's plainest declaration yet — stripped of obligation — still smuggled inside the "friendship" frame they both keep.

### Scene 4: Doing nothing
POV: Jay  
Central theme: repressed desire  
Motifs: near-kiss | hand-holding | bliss  
Mood: serene  
Weather: calm bright island day, warm surf  
Setting: Songbird Islands  
Keywords: the doorway near-kiss, an entire day hand-in-hand, the shared sweater that smells of Ian, "never been happier"  
Tension: 2  
Purpose: The book's calm crest — a whole day hand-in-hand — the wanting briefly satisfied without ever being named.

### Scene 5: Homecoming
POV: Mixed  
Central theme: repressed desire  
Motifs: ending | grief | the-promise  
Mood: elegiac  
Weather: leaving the sun for a grey, wintry city  
Setting: Jay's apartment  
Keywords: the last day, "Next weekend. Dinner and a drink.", grieving on the floor, the wanting that won't end  
Tension: 5  
Purpose: Ends the idyll and converts it into a forward promise — the wanting survives the flight home, now without the pretence to hold it.

## Chapter 48
Theme: Grief of re-entry, then desire that can no longer be called anything else.

### Scene 1: The Palm House
POV: Jay  
Central theme: protection  
Motifs: refuge | grief | wordless-care  
Mood: tender  
Weather: cold grey November; glasshouse warmth  
Setting: the Palm House  
Keywords: the four-digit inbox, the Palm House, Ian's own old refuge, soup and candied orange peel  
Tension: 3  
Purpose: Ian answers Jay's re-entry grief wordlessly by sharing his own private sanctuary — intimacy through place, not speech.

### Scene 2: Friday, Restored
POV: Jay  
Central theme: ritual/new tradition  
Motifs: reframe | restoration | swallowed-words  
Mood: warm  
Weather: cold November  
Setting: restaurant  
Keywords: the spoiled food critic, "I miss being yours" (swallowed), "an engineering problem, not a moral failing", "a Friday and a Saturday"  
Tension: 3  
Purpose: Restores the Friday ritual and reframes the post-vacation gloom as solvable — while Jay swallows the truest line he has.

### Scene 3: Climate Adjustment
POV: Jay  
Central theme: repressed desire  
Motifs: keepsake | violin | rebuilding-the-island  
Mood: tender  
Weather: cold November  
Setting: Ian's penthouse  
Keywords: linen-bound photo albums, Ian plays violin (promise kept), the penthouse pool, "not the island"  
Tension: 3  
Purpose: Pays off the violin promise and shows Ian literally rebuilding the island at home — refusing to let the closeness end.

### Scene 4: Heat
POV: Jay  
Central theme: repressed desire  
Motifs: desire | sauna | the-dream  
Mood: charged  
Weather: cold November  
Setting: Ian's penthouse  
Keywords: the home gym, hands correcting his form, the private sauna (no holiday excuse), the explicit dream, the faked cold  
Tension: 5  
Purpose: Strips away every alibi — holiday, drink — so Jay's desire becomes undeniable in plain daylight; the dream forces it into consciousness.

### Scene 5: Still Time
POV: Jay  
Central theme: denial/unnamed feeling  
Motifs: care | Christmas-hook | surrender  
Mood: festive  
Weather: cold late November, the festive season creeping in  
Setting: Ian's penthouse  
Keywords: soup and a medical thermometer, the cold that doesn't exist, "There's still time", Christmas floated, the desire finally accepted  
Tension: 4  
Purpose: Closes the written book on the turn — Jay stops fighting the desire — and floats Christmas as the next pressure, ending on appetite, not resolution.
