# Wraith: The Oblivion Library — Cross-Book Index

## Books in this collection
- `wraith-20th-anniversary/` — ***Wraith: The Oblivion — 20th Anniversary Edition*** (WR20; White Wolf / Onyx Path, 2018), 594 pages. **The core of this library**: the baseline for rules, setting and terminology.
- `dark-kingdom-of-jade/` — ***Wraith: The Oblivion — The Dark Kingdom of Jade*** (DKoJ; White Wolf, 1995, WW6010), 138 pages. A supplementary sourcebook written for an **earlier edition**. It is the detailed treatment of the Chinese afterlife, and it can serve as **crossover material for a *Kindred of the East* chronicle** (that line is not in this library).

## How to use this file
This file synthesizes across the two books. For one book's details read its own `book_index.md`; for exact wording query its `book_chunks.db`, or search both at once:

```bash
python3 scripts/query_library.py wraith-20th-anniversary/book_chunks.db dark-kingdom-of-jade/book_chunks.db "Immortal Guard" --brief
```

(`py -3` instead of `python3` on Windows.) Page numbers below are **printed** page numbers: WR20 printed = PDF − 65, DKoJ printed = PDF − 2. The scripts print both.

## Canon policy (read this before answering a Jade question)
1. **WR20 is the baseline.** Use its rules, terminology and setting by default.
2. **DKoJ adds depth on China and the Jade Kingdom** (history, government, Hell, the living world, Martial Arts, Backgrounds) and WR20 mostly agrees with it, because WR20's own Jade chapter (Ch. 13, pp. 433–441, 458–462) is a short update of DKoJ and reuses its stat blocks.
3. **Where they conflict, WR20 wins**, unless the Storyteller decides otherwise. Most conflicts are small (see the table below).
4. **Neither book mentions Kindred of the East or Kuei-jin.** Anything about that line below is a suggestion for the Storyteller, not canon from these books.

## Where to find the same topic in each book
| Topic | WR20 (printed pp.) | DKoJ (printed pp.) |
|---|---|---|
| Hun and p'o; the Chinese model of the soul | Ch. 13 pp. 433–434 | Ch. 1 pp. 19–22 |
| Qin Shihuang's rise; Lung Wang; the Ju-i | Ch. 13 pp. 436–438 | Ch. 2 pp. 27–47 (esp. 29–35) |
| Stygia–Jade war and treaty; WWII | Ch. 2 pp. 29–30, 40 (brief mentions only) | Ch. 2 pp. 41–45 |
| Government (the four departments) | Ch. 13 pp. 435–436 | Ch. 3 pp. 49–61 |
| Immortal Guard; Chains of the Emperor | Ch. 13 p. 439; pp. 462 | Ch. 3 pp. 59–61; Ch. 8 pp. 134–135 |
| Families, rebels, religion | Ch. 13 pp. 435–436 | Ch. 4 pp. 63–71 |
| Regions and Conquered Territories | Ch. 13 pp. 434–436 | Ch. 5 pp. 73–85 |
| Hell: Feng Tu, Ti Yu, Mrs. Meng, White Jade | Ch. 13 pp. 439–440 | Ch. 6 pp. 87–103 |
| Sacrifices, funerals, exorcists, mediums, feng shui | Ch. 13 p. 436 (Economics of Pathos) | Ch. 7 pp. 105–121 |
| Kuei and kuei-go; Eunuchs | Ch. 13 pp. 438–439 | Ch. 1 pp. 23–25; Ch. 6 pp. 91, 103 |
| Jade Arcanoi (Ways, Chains) | Ch. 13 pp. 458–462 | Ch. 8 pp. 127–135 |
| Martial Arts, Merits & Flaws, Living/Wraith Family | — | Ch. 8 pp. 123–127 |
| Chronicle ideas for Jade | Ch. 7 pp. 266–273 ("Ambassador to New Lands") | Ch. 8 pp. 135–136 |
| Other Dark Kingdoms (India, Americas, Africa, Australia, Caribbean) | Ch. 13 pp. 441–467 | brief mentions only (e.g., Swar, p. 82) |

## Cross-cutting themes

### The divided soul
- **WR20:** every wraith is a Psyche plus a Shadow whose Angst, Thorns and Shadow Dice drive Catharsis and Harrowings (`wraith-20th-anniversary/book_index.md`, Ch. 6).
- **DKoJ:** a Chinese wraith is a *failed separation* of the **hun** and the **p'o**; the hun is the Psyche and the p'o is played as the Shadow "with the same rules, archetypes and conventions" (DKoJ pp. 19–20).
- **WR20 Ch. 13** states the same idea more loosely (p. 434) and then reprints the Way of the Soul in Shadow terms (pp. 461–462). The same split recurs in Svarga (Gunas), the Flayed Lands, the Bush of Ghosts and the Mirrorlands (WR20 pp. 441–458).

### The afterlife as an empire
- **WR20:** Stygia is a decaying empire of Deathlords, Legions and banned Guilds (Ch. 2); other Dark Kingdoms are shown as peers (Ch. 13).
- **DKoJ:** the Jade Kingdom is a more stable, more oppressive bureaucracy: four Branches, corrupt but functional; stability is bought by enslaving foreign souls (Ch. 1, 3, 5).
- Both stress families and status; both treat rebellion as a recurring cycle.

### Souls as raw material
- **WR20:** souls become soulsteel, obolus coins, soulfire and Skin Artifacts (Ch. 2 pp. 42–45; Ch. 12 pp. 424–431).
- **DKoJ and WR20 Ch. 13:** hell exists to make **White Jade** from sentenced wraiths; **True Jade** is jade buried with a corpse; the Way of the Artisan can craft either (DKoJ pp. 23, 97, 103, 128–130; WR20 pp. 439–440, 459).

### Where Pathos comes from
- **WR20:** Passions, Memoriam, and (for Risen) the Conduit; Pathos is also the cost of most arts.
- **DKoJ:** the living family's sacrifices dominate: Hell notes, paper goods and buried goods become Pathos or relics; the **Living Family** Background replaces Memoriam for most Jade wraiths; the **Way of the Merchant** converts and transfers it (DKoJ pp. 106–111, 126–132; WR20 p. 436, 460–461).

### Contact with the living
- **WR20:** the Dictum Mortuum forbids it; the Shroud and Fog enforce it; mediums, secret orders and ghost hunters exist (Ch. 2, 8, 12).
- **DKoJ:** contact is *normal*: ancestor tablets, shrine Fetters, mediums, exorcists, talismans and feng shui (Ch. 7). The tension between the two attitudes is a story engine, not an error: Jade wraiths are bound by obligation to the living, Stygian wraiths by law against them.

### Power and its limits: Arcanoi
- **WR20:** 16 Guild Arcanoi, each with Common and Initiate arts gated by Guild Status (Ch. 5).
- **DKoJ and WR20 Ch. 13:** Jade wraiths use the Stygian Arcanoi except Castigate (replaced by the Way of the Soul), do not have Guilds, and add five native Arcanoi plus the Immortal Guard's Chains of the Emperor.

### Relations between kingdoms
- **DKoJ:** a Stygia–Jade war from the railroad and Gold Rush era (roughly the 19th century) ended in a treaty (p. 42) dividing souls by ancestry: Chinese, Japanese, Korean, Tibetan, Vietnamese, Thai, Cambodian and Laotian souls belong to the Emperor wherever they die, Western souls to Stygia. A Midnight Express stop at Hong Kong.
- **WR20:** brief early contacts (pp. 29–30), Pacific clashes in WWII (p. 40), Chinatowns inside London, New York and San Francisco and a Hong Kong Midnight Express stop (p. 440), and rumors that Yu Huang is eyeing North America (p. 434); WR20's Stygian history (Ch. 2) mentions Jade only on pp. 30 and 40 and says nothing of the war or treaty.

## Points of agreement
- Qin Shihuang died in 210 BCE and became Yu Huang, ruler of the Chinese dead; Fu Xia, the Immortal Guard (three regiments of 6,000), and the Ju-i that defeated the Malfean Lung Wang.
- Xi'an is the Shadowlands capital; the Jade Palace sits in the Tempest and holds 251 palaces; the Imperial Highway links them.
- The government has four branches: the Protectorate/Protectors of the Prosperous Realm, the Judges of the Dead, the Imperial Army and the Jade Censors; only soldiers may bear arms.
- Kuei are hungry ghosts (not Spectres), die in sunlight, last about three years and can be sealed with jade on the eyes and tongue; kuei-go are tamed attack dogs.
- White Jade is made from wraiths in Hell; True Jade is buried jade and cuts White Jade at difficulty 4; Ti Yu is reached from Feng Tu over seven days; Mrs. Meng's rest-house offers an alternative path.
- Chains of the Emperor are secret to the Guard and consist of Brilliance, Shackles, Snare, Lariat and Net. The Guard cannot gain Pathos normally and must be fed souls (several hundred Pathos each).
- The WR20 sample kuei and Immortal Guard stat blocks are DKoJ's, nearly word for word.
- Charon's disappearance (WR20: 1945) is consistent with DKoJ's references to the time "since the disappearance of Charon" (DKoJ p. 47).

## Points of disagreement or tension
| # | Topic | DKoJ (1995) | WR20 (2018) | Suggested ruling |
|---|---|---|---|---|
| 1 | Does a Jade wraith have a Shadow? | The p'o **is** the Shadow, played with the standard Shadow rules (p. 20). | Flavor text says Jade wraiths "would no sooner manifest a Shadow" (p. 433), yet the Way of the Soul uses Shadow Dice, Thorns and Angst on the p'o (pp. 461–462). | Use the standard Shadow rules for the p'o; call it a p'o in play. |
| 2 | Format of the Ways | Each Way has a free **Basic Ability** plus five powers, e.g., Studious Nature, Hear Jade's Tale, Kuei Howl, Jingle Jingle, Negotiation (pp. 127–134). | Only the five-power ladders are printed (pp. 458–462). | Use WR20's text; treat DKoJ's Basic Abilities as optional extras, or drop them. |
| 3 | Common vs. Initiate arts | Not used. | Every Stygian Arcanos dot has a Common and an Initiate art; Chapter 13 says non-Stygian Arcanoi have none (p. 457) and Jade has stamped out Guilds (p. 458). | Suggested: Jade wraiths know Stygian Common arts; Initiate arts need Guild Status, which Jade doesn't offer. (Inference, not stated in either book.) |
| 4 | How fast Qin conquered | Sole sovereign of the Chinese dead in under a year (p. 31). | Held "the eastern Shadowlands in less than a decade" before taking the title Yu Huang (p. 438). | Either: a year for China, a decade for the wider East. |
| 5 | Where the Guard is fed | At the **Necropolis at Xi'an**, by the Emperor (p. 61). | "At the Jade Palace at Xi'an" (p. 439) although the Palace is in the Tempest (p. 435). | Use DKoJ's Necropolis. |
| 6 | Ti Yu | An **underground** walled city beneath Feng-tu (pp. 39, 89–91). | "A thriving city in the Tempest" reached only from Feng Tu (p. 440). | Consistent if Feng Tu's caves open on the Tempest; either works. |
| 7 | Abilities in stat blocks | **Martial Arts** is an Ability that replaces Brawl, with hard and soft styles (pp. 125–126). | Reuses the Guard stat block with *Martial Arts: Shuai-Chiao* as a Talent (p. 439), although in WR20 Martial Arts is only a Brawl or Melee Specialty (pp. 133, 137). | Use DKoJ's Martial Arts for Jade characters, or Brawl with a Martial Arts Specialty. |
| 8 | Starting Pathos / family | **Living Family** replaces Memoriam; Pathos from family at difficulty 6 (pp. 106, 126). | Pathos = 5 + Memoriam; Passion rolls difficulty 6 or 8 (Ch. 4, Ch. 8). | Treat Living Family like a Memoriam-style Background for Jade wraiths (suggestion). |
| 9 | Catharsis / calming the p'o | Older fixed numbers for Negotiation (p. 132). | Catharsis is temporary Angst vs. permanent Willpower + Eidolon, difficulty 6 (WR20 p. 236). | Use WR20's roll. |
| 10 | The Dark Kingdom of Ivory | The Ivory Queen, in her own conflict with Stygia, threatens alliance with the Emperor, wins concessions (including New Orleans) and signs the treaty (p. 42). | The "Dark Kingdom of Ivory" is a front with a figurehead queen who "wields no real power" (p. 452). | Treat the Queen as a front for the real African kingdoms; the treaty signature was made on their behalf. |
| 11 | Present day | Mid-1990s (Hong Kong still a British possession, p. 75; the 1989 democracy movement). | 2010s (modern high-rises, Stygian enclaves in Macau, Singapore, Shanghai). | Pick a year for the chronicle. |
| 12 | Names | Protectorate; Feng-tu. | Protectors; Feng Tu. | Interchangeable. |
| 13 | Chinatowns and the treaty | Chinese souls belong to the Emperor wherever they die (p. 42). | Large Chinatowns in Stygian Necropoli (p. 440). | Treat them as Jade-aligned enclaves. |
| 14 | Harrowings in Hell | A Hell torc blocks Arcanoi; a Harrowing escape returns you near where Corpus was lost (pp. 90–93). | A Harrowing success returns you to a Fetter, Haunt or safe spot; failure goes to the Tempest (p. 242). | Hell is a special case; use DKoJ inside Ti Yu. |

## Chronology / influence
- **1995:** DKoJ published (WW6010), the first "Dark Kingdoms" book; it expands the Zhongguo section of the *Wraith Players' Guide* (DKoJ p. 15).
- **1999:** the original Wraith line ended with *Ends of Empire* (WR20 p. 470); the *Orpheus* core book followed (WR20 p. 470 says "four years later").
- **2018:** WR20 revises the setting, folds the Jade material into one short chapter and adds Svarga, Obsidian, the Bush of Ghosts, Karta and the Mirrorlands.
- **In-world:** Qin dies 210 BCE (WR20 p. 437); the Third Great Maelstrom is after the Flaying of Obsidian in the 16th century (WR20 p. 36); Charon vanishes in 1945 (WR20 p. 41); DKoJ's present is the mid-1990s.

## Using DKoJ material in a WR20 game (conversion cheat sheet)
- **Dice:** both use ten-sided pools at difficulty 6; no conversion is needed.
- **Arcanoi:** play Jade natives with the WR20 five-power Ways (WR20 pp. 458–462), optionally adding DKoJ's free Basic Ability for each Way (DKoJ pp. 127–134).
- **Shadow:** build the p'o with WR20 Chapter 6; use the Way of the Soul as written.
- **Backgrounds:** add Living Family, Wraith Family and Magisterial Office (DKoJ pp. 126–127) alongside WR20's list; Martial Arts replaces Brawl (DKoJ pp. 125–126).
- **Merits & Flaws** (DKoJ pp. 123–124) are optional extras that WR20 lacks.
- **Hell:** use DKoJ Ch. 6 (torc, Seven Days) for the Jade Hell; WR20 p. 440 is only a summary.
- **Monsters:** use the kuei stat block (identical in both); WR20 Ch. 10 supplies Spectres; WR20's Malfean guidelines (p. 374) can stat Lung Wang.

## Using this library for a *Kindred of the East* chronicle
*Neither book mentions Kindred of the East (the Eastern vampire line of Vampire: The Masquerade, whose vampires are called Kuei-jin). The ideas below are suggestions; check them against your own Kindred of the East books and keep those books' cosmology authoritative where they differ.*

**What DKoJ can supply**
- A ghost-side view of the **two-soul** model (hun and p'o) and what happens when they fail to separate (DKoJ pp. 19–22).
- **Hungry ghosts** and the Festival of the Hungry Ghosts, funerals that decide whether a death yields a wraith or a kuei, and the living practices that feed or banish the dead (DKoJ pp. 25, 108–111).
- A bureaucratic **Hell** with Feng-tu, the Seven Days, torturers and smelters, and Mrs. Meng's rest-house (DKoJ Ch. 6), usable as scenery for rescue or descent stories (the Introduction itself suggests "a mission to rescue a soul from Hell", p. 15).
- **Exorcists, talismans, mediums and feng shui** as hazards for any supernatural coterie (DKoJ pp. 112–121), including the Hong Kong "Unheeded Warnings" nihils (p. 121).
- A ready-made ghost empire: **Yu Huang, the four Branches, the Immortal Guard** and its Chains, **Conquered Territories** such as Japan, Korea, Tibet and Southeast Asia, plus rebel movements (DKoJ Ch. 3–5).

**What WR20 supplies for ghost-and-vampire encounters**
- Ch. 12 (pp. 409–417): vampires are described as having a Blood Pool that works like Pathos; Disciplines are mapped to the nearest Arcanoi; sample neonate, elder, Tremere and Giovanni templates; some vampires can detect wraith auras but only if they are looking for wraiths (p. 409), and the Tremere usually have Auspex and can perceive them (p. 410); how each Arcanos affects vampires (frenzy via Requiem, Blood Points stolen by Usury, Willpower diff. 7 to resist Puppetry).
- Ch. 11: a **Risen** wraith (pp. 385–403) can walk among the living with Pathos-fuelled Celerity, Fortitude and Potence, and bring a ghost's unfinished business into a vampire story.
- Ch. 12 (pp. 405–409): mediums, ghost hunters and secret orders as mortal-side tools.

**Story hooks (suggestions)**
1. A coterie's ancestral graveyard goes quiet, then the **Festival of the Hungry Ghosts** brings a surge of kuei.
2. A Jade wraith who died at the vampires' hands rises as a **Risen** to hunt the killer.
3. A vampire's mortal family keeps a **shrine Fetter** for an ancestor wraith who wants something done.
4. A rescue run into **Ti Yu** to retrieve a soul sold to the smelters.
5. A faction of **Immortal Guard** crosses into the Skinlands to recover a stolen relic of True Jade.
6. A Hong Kong or Beijing chronicle where wraith, vampire and mortal exorcist interests collide.
7. A **Chinatown** in a Western city that is also a Jade enclave (WR20 p. 440).

**Cautions**
- DKoJ's **kuei** are mindless hungry ghosts, not vampires; do not conflate them with Kuei-jin, even though the word shares a root.
- Decide how the ghost empire relates to your Eastern-vampire cosmology: **parallel** (the wraith world sits beside it), **overlapping** (Yu Huang's Hell is the ghost-visible face of the same underworld), or **separate** (treat DKoJ as a self-contained dead realm). The books give no answer.
- Stats for vampires in WR20 are Western-vampire approximations; Kuei-jin will need your Storyteller's conversion.

## Cross-book query examples
```bash
# Same topic in both books
python3 scripts/query_library.py wraith-20th-anniversary/book_chunks.db dark-kingdom-of-jade/book_chunks.db "Chains of the Emperor" --brief
python3 scripts/query_library.py wraith-20th-anniversary/book_chunks.db dark-kingdom-of-jade/book_chunks.db "hun p'o" --limit 4

# One book, one chapter
python3 wraith-20th-anniversary/scripts/query_chunks.py wraith-20th-anniversary/book_chunks.db "Way of the Soul" --chapter "Chapter 13:"
python3 dark-kingdom-of-jade/scripts/query_chunks.py dark-kingdom-of-jade/book_chunks.db "Basic Ability" --chapter "Chapter Eight"

# Look up a printed page
python3 wraith-20th-anniversary/scripts/query_chunks.py wraith-20th-anniversary/book_chunks.db --printed 439
python3 dark-kingdom-of-jade/scripts/query_chunks.py dark-kingdom-of-jade/book_chunks.db --printed 61
```
