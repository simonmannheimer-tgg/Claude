# 01 — PLP Intro Copy (2-Sentence)

**Last updated:** 27 March 2026
**Status:** Active
**Version:** 2.1 — incorporates batch 2–4 production learnings

---

## Purpose

Write 2-sentence intro paragraphs for Product Listing Pages on The Good Guys website. Copy must be viewport-safe (≤5 lines on ~360px mobile), SEO-correct, intent-aligned, and human-sounding.

---

## Inputs required

- **Page URL** — to classify page type and extract brand/category
- **EAV data** — from `eav-researcher` agent: entities, attributes, purchase drivers, specific product lines
- **Keyword signal** — from `seo-keyword-researcher` (Semrush `url_organic`, database: au) ONLY if `Non brand clicks (3mnt)` > 200. Below threshold: use brand knowledge + EAV output only.

---

## Page Type Classification

Classify every URL before writing. Type affects which rules apply.

| Type | URL Pattern | Examples |
|------|-------------|---------|
| A — Generic Category | No brand slug | `/audio`, `/coffee-machines`, `/washing-machines` |
| B — Brand Hub | Brand slug only (1 segment after root) | `/samsung`, `/lg`, `/dyson` |
| C — Brand + Category | Brand slug + category (2+ segments) | `/samsung/fridges`, `/dyson/vacuums`, `/lg/washing-machines/top-load` |
| D — Promo / Deals | `/deals/` path | `/deals/black-friday-fridges` |

CSV codes from source file: **B1 = Type B**, **B2 = Type C**, **B3 = Type C (deeper path)**

---

## Character Count

- **Range:** 220–250 characters (every letter, space, punctuation mark)
- **Target:** 225–235 (lower end preferred)
- **Floor:** 220 — never below. Too short to carry entity depth.
- **Ceiling:** 250 — hard stop. If S1 runs long, shorten S2 first.

Count every character including spaces, commas, full stops, ampersands, hyphens. Use an exact counter — do not eyeball it.

---

## The Fundamental Goal

A user landing on `/samsung/washing-machines` already knows what a washing machine does. They chose Samsung. S1 must tell them what **Samsung washing machines** do differently.

**Test every S1:** Could you copy-paste this onto a competitor's page (LG, Bosch, Hisense) with minimal word changes and have it still make sense? If yes — rewrite it. It isn't specific enough.

---

## What Good Copy Does

### S1 — Semantic Anchor
- Opens with something specific to **this brand in this category** — not a generic category benefit
- Names at least one entity anchor (see Entity Anchor Types below)
- Opener angles to rotate: outcome-first, feature-first, format-first, spec-first, problem-first
- **Never opens S1 with:** Discover, Explore, Shop (these suit S2)

### S2 — Entity Inventory + TGG Anchor
- Names 2–3 specific sub-types, series names, tech references, or capacity ranges
- Contains "The Good Guys" exactly once (placement varies — not always end of S2)
- S2 openers to rotate: Find, Shop, Discover, Explore, Choose
- S2 must be **shorter than S1**

---

## Entity Anchor Types — What Counts as Specific

Entity anchoring is not about finding trademark names for their own sake. It's about saying something that would be false or misleading on a competitor's page. These forms all qualify:

### 1. Named Proprietary Technology (highest preference for major brands)
Technology trademarked or closely associated with a specific brand. Use where it genuinely exists.

| Brand | Technologies |
|-------|-------------|
| Samsung (fridges) | Twin Cooling Plus, SpaceMax, Family Hub, Door-in-Door, All-Around Cooling |
| Samsung (washing) | BubbleWash, Hygiene Steam, QuickDrive, AI Wash |
| LG (fridges) | InstaView, LinearCooling, Door-in-Door, HygieneFRESH+, ThinQ |
| LG (washing) | TurboWash, Steam+, ThinQ, AI DD |
| Bosch (washing) | i-DOS, EcoSilence Drive, AutoDry, SpeedPerfect |
| Miele (washing) | TwinDos, CapDosing, HoneyComb drum, T1 heat pump |
| Fisher & Paykel | ActiveSmart Foodcare, SmartDrive, SpacePlus |
| Westinghouse | FreshSeal, SensorBake |
| Dyson | Supersonic, Air Multiplier, Hyperdymium, HEPA filtration |
| Breville | ThermoJet, ThermoCoil, Barista Express, Oracle Touch, Bambino Plus |
| Nespresso | Vertuo/Centrifusion, Original line, Creatista, Lattissima |
| Apple | M-series chips, Retina display, MagSafe, AirPods Pro/Max |
| Samsung (TVs) | Neo QLED, Quantum Matrix, Neural Quantum Processor |
| LG (TVs) | OLED evo, QNED, webOS, α-series processor |
| Kindle | E Ink Paperwhite, Scribe, warm light |
| Incase | CL90052-compliant hardshell, Woolenex fabric |
| Mophie | Juice Pack, GaN fast-charge, Powerstation |
| Cygnett | ArmourShield, GaN, MagSafe |
| Belkin | BoostCharge Pro, GaN, Kevlar-reinforced |

### 2. Named Product Line or Series (works for most brands)
Model or series names anchor the copy to a specific brand reality.

| Brand | Product Lines |
|-------|-------------|
| Nespresso | Vertuo, Original, Creatista, Lattissima, Essenza, Citiz |
| Smeg | 50s Style, retro pastels (cream, pastel green, pink) |
| KitchenAid | Artisan stand mixers, bowl-lift, K400 blender |
| BeefEater | Signature, Proline, Discovery series |
| eufy | SpaceView, Babycare, RoboVac, HomeBase |
| Oliveri | Santorini, Regatta (sink bowls), pullout/pulldown taps |
| Garmin | Forerunner, Fenix, Venu, MARQ |
| Fitbit | Charge, Inspire, Sense, Versa |
| Husqvarna | Automower 305, 430X, EPOS |
| Sandisk | UHS-I, UHS-II microSD/SD, Extreme Pro SSD |
| Norton | AntiVirus Plus, 360 Standard, 360 Deluxe |
| Sony TVs | BRAVIA 7, 8, 9 series; Cognitive Processor XR; Triluminos Pro |
| Microsoft Surface | Surface Pro, Surface Laptop, Surface Go; Copilot+; PixelSense |
| Baileys | Irish Cream flavour pods, capsule format |
| Milo | Action Communicator, helmet mounts, action clips |

### 3. Specific Product Attribute + Real Value (for brands without strong trademark names)
Format + spec + finish. More than one specific value is required.

| Brand | Good Entity Anchors |
|-------|---------------------|
| Solt (fridges) | Frost-free performance, adjustable glass shelving, 280L to 450L |
| CHiQ | Frost-free multi-airflow cooling, adjustable glass shelving, French door/top mount/bar |
| Haier | Total No Frost, MultiAirFlow, ZoneFlex drawers |
| TCL (fridges) | Frost-free multi-airflow, LED interiors, top/bottom/French door to 550L |
| Westinghouse (cooktops) | Induction/ceramic/gas, 60cm and 90cm, wok burner options |
| Oliveri (taps) | Ceramic cartridge valves, braided hose, spray and stream modes, chrome/matte black |
| La Germania | Gas/dual fuel/induction, spacious 90cm cavities, multi-function oven |
| ASKO | Logic Series, stainless steel drums, Active Drum technology |
| Schweigen | Silent external motor (key brand differentiator), undermount rangehoods |
| Artusi | Gas, dual fuel, black glass finishes, 54cm to 90cm |

### 4. Brand-Defining Characteristic (specific and verifiable)
Something real about the brand that makes it recognisable.

| Brand | Characteristic |
|-------|---------------|
| Smeg | Retro 50s design, pastel and cream colour options |
| Laura Ashley | Floral pattern detail on benchtop appliances |
| Baileys | Irish Cream signature flavour in capsule coffee format |
| Milo | Group communication device for outdoor activities (cyclists, hikers, skiers) |
| Vegepod | Self-watering design, raised beds with protective mesh covers |
| Pacifica | Laundry organisation — airers, hampers, vacuum bags, stacking kits |
| Singer | Sewing machines — multiple stitch options, metal frames |
| Husqvarna (outdoor) | Cordless battery platform, brushless motors across trimmers/blowers/mowers |

### What FAILS the Test — Always Rewrite These
These phrases have zero entity value because they describe the category, not the brand:

- "flexible storage, compact bar options" — any fridge brand
- "precise temperature control and generous capacities" — any oven brand  
- "powerful purification, smart sensors" — any air purifier brand
- "stable connections and fast data transfer" — any accessories brand
- "efficient cycles and gentle fabric care" — any washer brand
- "fast processors, vivid displays, ample storage" — any laptop brand
- "strong suction, cordless convenience" — any vacuum brand
- "clear audio, long battery life" — any headphone brand

---

## Page Type Rules

### Type A — Generic Category
- S1 anchors the category with 2–3 named brands + a meaningful differentiator
- S2 adds product format breadth (sub-types, use cases)
- This is the only type where naming multiple brands in S1 is appropriate
- No brand hub restrictions apply

### Type B — Brand Hub (B1)
- S1 MUST name the brand + at least one proprietary technology or defining product line
- Copy must feel specific to THIS brand — not interchangeable with any other brand hub
- S2 names 2–3 specific product formats, series, or capacity ranges available at TGG
- No competitor mentions, no comparison language
- No discovery-stage language ("options to suit everyone", "explore the range")
- **Additional banned words (brand PLPs only):** trusted, reliable, enjoy, features
  - Reason: these make every brand hub feel identical. "Enjoy Samsung's trusted features" says nothing about Samsung.

### Type C — Brand + Category (B2, B3)
- S1: brand name + 1–2 specific technologies or formats that distinguish this brand in this specific category
- S2: 2–3 specific sub-types, series names, capacities, or product variants at TGG
- Brand name in S1
- **Same additional bans as Type B:** trusted, reliable, enjoy, features

### Type D — Promo / Deals
- S1 must contain ONE of: `{Category} deals 2026` / `{Category} Black Friday sale 2026` / `{Category} offers 2026`
- Include year immediately after intent phrase
- Do not stack multiple intent phrases
- Year rule: currently 2026

---

## Sentence Structure Rules

- **Exactly 2 sentences.** No run-ons as comma splices. No extra clauses for padding.
- **S2 shorter than S1.** Long S2 creates orphaned text on mobile. If S1 runs long, trim S2 first.
- **Both sentences must end with a full stop.** Truncated copy (ending mid-sentence, ending with comma) is a hard fail.
- Sentence case only — capitalise first word + proper nouns only.

---

## Batch Variation Rules

Scan the full batch every 20 URLs before continuing. Flag and rewrite if:

- 3+ consecutive S1 openers use the same verb or structure
- 3+ consecutive S2 openers use the same word (Find/Shop/Discover/Explore/Choose)
- Same benefit angle leads more than 30% of the sub-batch
- TGG appears in the same S2 position (early/mid/late) in more than 60% of the sub-batch
- "Save time with" opens S1 on more than 5% of the full batch (it's a weak generic opener)
- "Stay comfortable with" opens S1 on more than 5% of the full batch

---

## Hard Bans (never use in any copy)

| Banned | Why | Use Instead |
|--------|-----|-------------|
| sale / sales | SEM compliance | deal / deals |
| save / saving (as price framing) | SEM compliance | pay less / get a great deal on |
| discount | SEM compliance | deal / offer |
| exclusive (re deals) | Legal | best deals, great deals |
| Australia's trusted choice | SEM compliance | — |
| quality brands | SEM compliance | big brands, best brands |
| get great value | SEM compliance | — |
| perfect for all needs | Vague | be specific |
| amazing, stunning, wonderful | Generic, oversold | describe the actual benefit |
| busy homes, hearty meals, sleek design | Cliché AI-sounding | describe the real scenario |

**Critical save/saving distinction:** "save money", "save on [product]", "save with Price Beat" = BANNED (price framing). "Save time", "save water", "save energy" as functional outcomes = fine.

---

## Semrush Keyword Pull — Conditional

Only pull if `Non brand clicks (3mnt)` > 200.

```
report:          url_organic
database:        au
display_limit:   8
display_sort:    tr_desc
export_columns:  Ph, Po, Nq, Tr
```

Use ranking terms as entity signal — if a URL ranks for "LG twin cooling fridge" that term belongs in the copy. Below threshold: write on brand knowledge + EAV output only.

---

## Validation — Run Before Writing to Output

| Check | Pass Condition |
|-------|----------------|
| Character count | 220–250 inclusive |
| Sentence count | Exactly 2 |
| Both sentences end with full stop | Yes |
| S2 shorter than S1 | Yes |
| TGG mention | Exactly 1 |
| Hard-banned words | None present |
| Brand bans (B/C pages) | trusted / reliable / enjoy / features absent |
| Entity anchor present | At least one specific fact that would be wrong on a competitor's page |
| Truncation | Copy does not end mid-sentence or with a comma |
| Australian English | Correct spelling |

On validation failure: mark row `FAIL` with specific reason. Do not silently drop. Do not leave Flag cell blank.

---

## Output Format

**File:** `seo/outputs/plp-brand-cat-batch[X]-[YYYY-MM-DD].csv`

| Column | Content |
|--------|---------|
| `URL` | Full URL from source CSV |
| `Batch` | Batch 2 / Batch 3 / Batch 4 |
| `Page_Type` | A / B / C |
| `Copy` | Final 2-sentence copy, plain text, no HTML |
| `Chars` | Exact character count |
| `Status` | PASS or FAIL |
| `Flag` | Empty if PASS. Specific failure reason if FAIL |

Encoding: UTF-8. No BOM. No smart quotes or encoding artefacts.

---

## QA Checklist

### Mechanical
- [ ] Exactly 2 sentences
- [ ] 220–250 characters (225–235 ideal)
- [ ] Both sentences end with full stop
- [ ] S2 shorter than S1
- [ ] "The Good Guys" appears exactly once
- [ ] No hard-banned words
- [ ] Sentence case throughout
- [ ] No encoding artefacts
- [ ] No links, HTML, or markdown
- [ ] Australian English

### Intent & Quality
- [ ] Page type classification matches URL
- [ ] S1 contains an entity anchor specific to this brand (passes the competitor substitution test)
- [ ] S2 names at least 2 specific sub-types, series, tech references, or capacity ranges
- [ ] Brand PLPs (B/C): no trusted, reliable, enjoy, features
- [ ] Brand PLPs (B/C): no competitor mentions, no generic benefit language
- [ ] Copy reads naturally — not templated, not a keyword list
- [ ] Does not replicate the angle or phrasing from any existing copy in the `Current Intro` column

### Batch
- [ ] No 3+ consecutive S1 openers with same verb/structure
- [ ] No 3+ consecutive S2 openers with same word
- [ ] TGG placement varies across batch
- [ ] Benefit angles vary
- [ ] "Save time with" not overused as S1 opener
- [ ] "Stay comfortable with" not overused as S1 opener

---

## Notes

- This process was significantly revised after batch 2–4 production (March 2026). The original over-emphasis on proprietary trademark names caused the agent to incorrectly flag valid copy for brands that have no trademarks, and to miss genuinely generic copy that had no specific anchoring.
- The entity anchor standard (Section "Entity Anchor Types") is the canonical reference for what counts as "specific enough". It supersedes the earlier rule of "named technology in S1".
- Cross-reference `00-tov.md` for all language bans and Australian English rules.
- See `PLP-Batch-Production-Brief-2026-03-19.md` for the original batch brief.
- See `seo/outputs/plp-fix-candidates-2026-03-19.csv` for the 658-row outstanding fix backlog.
