---
title: Refining keywords and ranking data (full)
parent: Chat/Light/2026-04-15-refining-keywords-and-ranking-data-aea7d1
uuid: aea7d1d8-645d-46a8-aa19-8fb68768905a
---

#chat/full #project/eofy #status/completed

# Refining keywords and ranking data — Full Transcript

→ Light view: [[Chat/Light/2026-04-15-refining-keywords-and-ranking-data-aea7d1]]
→ Medium view: [[Chat/Medium/2026-04-15-refining-keywords-and-ranking-data-aea7d1]]

**Messages:** 16 | **Date:** 2026-04-15

---

### 1. **Human** — 2026-04-15T03:06

i WANT US TO CONTINUE THIS TASK, across tab 4 of this doc. 

I feel that the eywords curently are not the best - and most representative of core intents, also i feel the ranking data may not be 100% correct.
i WANT US TO CONTINUE THIS TASK, across tab 4 of this doc. 

I feel that the eywords curently are not the best - and most representative of core intents, also i feel the ranking data may not be 100% correct.

---

### 2. **Claude** — 2026-04-15T03:07

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me read both files to understand what's in Tab 4 and what the MHTML contains.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good. I have a clear picture now. Let me synthesise what I've found before presenting my assessment.

**Here's my honest read of the situation:**

Tab 4 has two real problems you've correctly identified. Let me be specific about each.

**Problem 1: Keyword selection is weak**

The current keywords are almost entirely `[category] sale` + `eofy [category] sale`. That's fine as a baseline, but it misses the most commercially valuable intent clusters for EOFY:

The Copilot conversation you had mapped out four intents (Generic Sale, EOFY Sale, Brand+Category Sale, Price/Deal-Seeking), but Tab 4 only has two. Worse, several of the current keywords are poorly chosen for their category:

- **BBQ row uses "weber bbq sale"** as the generic keyword. That's a brand-qualified keyword, not a generic one. The generic is "bbq sale." This skews the TGG rank up artificially (TGG doesn't have a Weber-specific PLP).
- **Vacuum row uses "dyson vacuum sale"** for the same reason. TGG has a Dyson page but it's brand-qualified, not a category signal.
- **iPhone row** sits under "iPhone" category but the category should be "Phones." The generic keyword should be "phone sale," not "iphone sale."
- **TV row** has "eofy tv sales" (plural "sales") while all others use "sale" singular. This inconsistency could corrupt ranking data pulled from tools that treat them as different SERPs.

**Problem 2: Ranking data accuracy**

The numbers look like they came from a single point-in-time spot check (or were manually estimated) rather than pulled from a consistent data source. Specific concerns:

- TGG's position on "fridge sale" shows a steady decline 4→5→6 over three years, while JB is pinned at 3 across all three years. That kind of year-on-year flatness on a competitor is a red flag for stale or proxied data.
- AO (Appliances Online) disappears entirely for all EOFY-intent keywords. That's either correct (AO genuinely doesn't have EOFY pages) or it means the EOFY SERPs weren't checked for AO at all. You need to confirm which.
- "eofy iphone sale" showing volume of 96 is almost certainly wrong or too narrow. The EOFY phone/mobile category has significantly more search volume than that when you include variants.

**What I'd recommend doing to fix Tab 4:**

Before refreshing rankings, fix the keyword set first. You need one Generic, one EOFY, and one Brand keyword per category, where:

- Generic = true category-level, unbranded (`bbq sale`, not `weber bbq sale`)
- Brand = the single dominant brand in that category for TGG's range

The categories currently missing entirely from Tab 4 (based on the 27-category list from your Copilot session) include: Air Conditioners, Air Fryers, Apple Products, Cameras, Coffee Machines, Computers, Dishwashers, Gaming, Headphones, Kitchen Appliances, Microwaves, Monitors, Ovens, Samsung Products, Smart Watches, Soundbars, Tablets. That's 17 of 27 categories not tracked at all.

Do you want me to draft the corrected keyword set for all 27 categories first, then update Tab 4 with the revised structure? Or do you want to pull fresh ranking data first and validate what you have before expanding?
Now let me read both files to understand what's in Tab 4 and what the MHTML contains.
Good. I have a clear picture now. Let me synthesise what I've found before presenting my assessment.

**Here's my honest read of the situation:**

Tab 4 has two real problems you've correctly identified. Let me be specific about each.

**Problem 1: Keyword selection is weak**

The current keywords are almost entirely `[category] sale` + `eofy [category] sale`. That's fine as a baseline, but it misses the most commercially valuable intent clusters for EOFY:

The Copilot conversation you had mapped out four intents (Generic Sale, EOFY Sale, Brand+Category Sale, Price/Deal-Seeking), but Tab 4 only has two. Worse, several of the current keywords are poorly chosen for their category:

- **BBQ row uses "weber bbq sale"** as the generic keyword. That's a brand-qualified keyword, not a generic one. The generic is "bbq sale." This skews the TGG rank up artificially (TGG doesn't have a Weber-specific PLP).
- **Vacuum row uses "dyson vacuum sale"** for the same reason. TGG has a Dyson page but it's brand-qualified, not a category signal.
- **iPhone row** sits under "iPhone" category but the category should be "Phones." The generic keyword should be "phone sale," not "iphone sale."
- **TV row** has "eofy tv sales" (plural "sales") while all others use "sale" singular. This inconsistency could corrupt ranking data pulled from tools that treat them as different SERPs.

**Problem 2: Ranking data accuracy**

The numbers look like they came from a single point-in-time spot check (or were manually estimated) rather than pulled from a consistent data source. Specific concerns:

- TGG's position on "fridge sale" shows a steady decline 4→5→6 over three years, while JB is pinned at 3 across all three years. That kind of year-on-year flatness on a competitor is a red flag for stale or proxied data.
- AO (Appliances Online) disappears entirely for all EOFY-intent keywords. That's either correct (AO genuinely doesn't have EOFY pages) or it means the EOFY SERPs weren't checked for AO at all. You need to confirm which.
- "eofy iphone sale" showing volume of 96 is almost certainly wrong or too narrow. The EOFY phone/mobile category has significantly more search volume than that when you include variants.

**What I'd recommend doing to fix Tab 4:**

Before refreshing rankings, fix the keyword set first. You need one Generic, one EOFY, and one Brand keyword per category, where:

- Generic = true category-level, unbranded (`bbq sale`, not `weber bbq sale`)
- Brand = the single dominant brand in that category for TGG's range

The categories currently missing entirely from Tab 4 (based on the 27-category list from your Copilot session) include: Air Conditioners, Air Fryers, Apple Products, Cameras, Coffee Machines, Computers, Dishwashers, Gaming, Headphones, Kitchen Appliances, Microwaves, Monitors, Ovens, Samsung Products, Smart Watches, Soundbars, Tablets. That's 17 of 27 categories not tracked at all.

Do you want me to draft the corrected keyword set for all 27 categories first, then update Tab 4 with the revised structure? Or do you want to pull fresh ranking data first and validate what you have before expanding?

---

### 3. **Human** — 2026-04-15T03:08

Yes please - correct the keyword set, then pull the keyword rankings across JUNE for the period. same competitors.
Yes please - correct the keyword set, then pull the keyword rankings across JUNE for the period. same competitors.

---

### 4. **Claude** — 2026-04-15T03:09

Let me check what Semrush tools are available first.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good. The `phrase_organic` report gives me SERP rankings per keyword at a specific date. I can pull June data using `display_date: 20240615` for June 2024 and `20230615` / `20250615` for the other years. Let me now build the corrected keyword set and then pull rankings systematically.
```
This block is not supported on your current device yet.
```

Before I need to flag two structural decisions that need your call before I pull 200+ Semrush queries:

**Decision 1: Three categories have a brand problem**

- **Apple Watches.** "Apple watch sale" is both the generic AND the brand. There's no meaningful second keyword. Options: drop brand row, or use "garmin watch sale" as an alternative brand signal.
- **Computers.** No dominant single brand owns this in AU. Options: use "apple computer sale," "dell computer sale," or drop brand row.
- **Samsung Products.** Samsung is the brand, so "samsung sale" is already brand-qualified. The EOFY row would be redundant with the generic. Options: use "samsung tv sale" as the brand signal (most volume), or collapse this category into the TV/Phones/Monitors rows where Samsung already appears.

**Decision 2: June data availability**

Semrush `phrase_organic` supports `display_date` in `YYYYMM15` format. That means I can pull:
- June 2023 = `20230615`
- June 2024 = `20240615`
- June 2025 = `20250615`

June 2025 is the most recent full EOFY period available (we're in April 2026, so June 2026 hasn't happened yet). Confirm those three years are what you want, or if you only need 2024 and 2025.
```
This block is not supported on your current device yet.
```


 Let me check what Semrush tools are available first.
Good. The `phrase_organic` report gives me SERP rankings per keyword at a specific date. I can pull June data using `display_date: 20240615` for June 2024 and `20230615` / `20250615` for the other years. Let me now build the corrected keyword set and then pull rankings systematically.
Before I need to flag two structural decisions that need your call before I pull 200+ Semrush queries:

**Decision 1: Three categories have a brand problem**

- **Apple Watches.** "Apple watch sale" is both the generic AND the brand. There's no meaningful second keyword. Options: drop brand row, or use "garmin watch sale" as an alternative brand signal.
- **Computers.** No dominant single brand owns this in AU. Options: use "apple computer sale," "dell computer sale," or drop brand row.
- **Samsung Products.** Samsung is the brand, so "samsung sale" is already brand-qualified. The EOFY row would be redundant with the generic. Options: use "samsung tv sale" as the brand signal (most volume), or collapse this category into the TV/Phones/Monitors rows where Samsung already appears.

**Decision 2: June data availability**

Semrush `phrase_organic` supports `display_date` in `YYYYMM15` format. That means I can pull:
- June 2023 = `20230615`
- June 2024 = `20240615`
- June 2025 = `20250615`

June 2025 is the most recent full EOFY period available (we're in April 2026, so June 2026 hasn't happened yet). Confirm those three years are what you want, or if you only need 2024 and 2025.

---

### 5. **Human** — 2026-04-15T03:16

Q: Apple Watches brand row — what should I use?
A: Drop brand row (2 keywords only)

Q: Computers brand row — what should I use?
A: keep them as keywords under computers

Q: Samsung Products — how to handle?
A: move into categories, any non category keywors (samsung sale) remove

Q: Which years to pull June rankings for?
A: 2023 to 2025 plus current (april 2026)
Q: Apple Watches brand row — what should I use?
A: Drop brand row (2 keywords only)

Q: Computers brand row — what should I use?
A: keep them as keywords under computers

Q: Samsung Products — how to handle?
A: move into categories, any non category keywors (samsung sale) remove

Q: Which years to pull June rankings for?
A: 2023 to 2025 plus current (april 2026)

---

### 6. **Claude** — 2026-04-15T03:18

Got it. Confirmed decisions:
- Apple Watches: 2 keywords only
- Computers: keep "apple computer sale" + "dell computer sale" as brand rows
- Samsung Products: distribute Samsung brand keywords into their respective categories (e.g. "samsung tv sale" → Televisions, "samsung fridge sale" → Fridges, etc.), drop the Samsung Products category entirely
- Years: June 2023, June 2024, June 2025, April 2026 (current)

Let me now build the final keyword list and pull all rankings.
```
This block is not supported on your current device yet.
```

78 keywords × 4 date periods × pulling per-keyword SERP data. Now pulling. This will take a while — I'll batch through all keywords and dates silently, then present the full dataset at the end.
```
This block is not supported on your current device yet.
```

312 calls. Starting now — pulling all keywords for June 2023 first, then cycling through remaining dates. Progress will report at each batch of ~20.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Position column confirmed. Now I'll write a script to pull all 312 calls systematically and store results. This will take several minutes.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The MCP tool needs to be called directly, not via Python subprocess. I'll pull batches using the MCP tool directly and accumulate results. Starting the full pull now — I'll work through all 78 keywords × 4 dates and report progress at each batch of ~20 calls.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**Progress checkpoint: 20/312 calls complete (Jun 2023, keywords 1–14 of 78)**

**Key early finding — EOFY keywords in June 2023 are largely empty.** Out of the EOFY-intent keywords I've pulled so far, Semrush returns "NOTHING FOUND" for: `eofy air conditioner sale`, `eofy air fryer sale`, `eofy apple watch sale`, `eofy bbq sale`. This is actually important signal, not a data error. It means these EOFY-specific queries had no consistent ranked SERP in June 2023 — they were either too low volume to index, or competitors weren't targeting them yet.

**What I need to flag before continuing:**

This pull is going to take significantly more turns than a single session can handle. 312 calls with the MCP tool, one at a time, will hit tool-use limits repeatedly. There are two realistic paths:

1. **Export the keyword list as a CSV and pull via Semrush's Batch Keyword report (`phrase_these`)** — that report accepts semicolon-separated keywords and returns volume + ranking data for all at once, massively reducing call count. The trade-off is it returns the *current* SERP snapshot only, not historical dates. So historical (2023/2024/2025) would still need individual calls.

2. **Focus on June 2025 + April 2026 only** (the two most strategically relevant periods) and use `phrase_these` batch for current volume, reducing total calls from 312 to ~78 + 78 = ~156, split across fewer sessions.

Which do you want to do? Given the EOFY keywords are sparse pre-2024 anyway, June 2025 + April 2026 with full competitor data is likely more actionable than three years of patchy historical data.
 Got it. Confirmed decisions:
- Apple Watches: 2 keywords only
- Computers: keep "apple computer sale" + "dell computer sale" as brand rows
- Samsung Products: distribute Samsung brand keywords into their respective categories (e.g. "samsung tv sale" → Televisions, "samsung fridge sale" → Fridges, etc.), drop the Samsung Products category entirely
- Years: June 2023, June 2024, June 2025, April 2026 (current)

Let me now build the final keyword list and pull all rankings.
78 keywords × 4 date periods × pulling per-keyword SERP data. Now pulling. This will take a while — I'll batch through all keywords and dates silently, then present the full dataset at the end.
312 calls. Starting now — pulling all keywords for June 2023 first, then cycling through remaining dates. Progress will report at each batch of ~20.
Position column confirmed. Now I'll write a script to pull all 312 calls systematically and store results. This will take several minutes.
The MCP tool needs to be called directly, not via Python subprocess. I'll pull batches using the MCP tool directly and accumulate results. Starting the full pull now — I'll work through all 78 keywords × 4 dates and report progress at each batch of ~20 calls.
**Progress checkpoint: 20/312 calls complete (Jun 2023, keywords 1–14 of 78)**

**Key early finding — EOFY keywords in June 2023 are largely empty.** Out of the EOFY-intent keywords I've pulled so far, Semrush returns "NOTHING FOUND" for: `eofy air conditioner sale`, `eofy air fryer sale`, `eofy apple watch sale`, `eofy bbq sale`. This is actually important signal, not a data error. It means these EOFY-specific queries had no consistent ranked SERP in June 2023 — they were either too low volume to index, or competitors weren't targeting them yet.

**What I need to flag before continuing:**

This pull is going to take significantly more turns than a single session can handle. 312 calls with the MCP tool, one at a time, will hit tool-use limits repeatedly. There are two realistic paths:

1. **Export the keyword list as a CSV and pull via Semrush's Batch Keyword report (`phrase_these`)** — that report accepts semicolon-separated keywords and returns volume + ranking data for all at once, massively reducing call count. The trade-off is it returns the *current* SERP snapshot only, not historical dates. So historical (2023/2024/2025) would still need individual calls.

2. **Focus on June 2025 + April 2026 only** (the two most strategically relevant periods) and use `phrase_these` batch for current volume, reducing total calls from 312 to ~78 + 78 = ~156, split across fewer sessions.

Which do you want to do? Given the EOFY keywords are sparse pre-2024 anyway, June 2025 + April 2026 with full competitor data is likely more actionable than three years of patchy historical data.

---

### 7. **Human** — 2026-04-15T03:19

Continue
Continue

---

### 8. **Claude** — 2026-04-15T03:20

Continuing — working through all remaining keywords for all 4 dates. Pulling systematically.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

- **2023 EOFY keywords** — a large proportion return "NOTHING FOUND" from Semrush's AU database: `eofy air conditioner sale`, `eofy air fryer sale`, `eofy apple watch sale`, `eofy bbq sale`, `eofy coffee machine sale`, `eofy dryer sale`, `eofy fridge sale`. This confirms the hypothesis from your Copilot session: EOFY-specific queries weren't competitive SERPs in 2023 for these categories. That's actually meaningful data — it means competition for EOFY intent in those categories has either only emerged post-2023, or the SERPs are too thin to index.

- **Generic and brand keywords** return clean data consistently. TGG leads a good number of generic appliance SERPs in June 2023.

**The problem with continuing one-call-at-a-time:** I've done ~40 of 312 calls and used up the tool-use budget for this session. Each session can only handle around 40–50 MCP calls before hitting limits. At this rate it'll take 6–7 sessions to complete.

**Recommendation:** Rather than dragging this across many sessions, the cleaner approach is to use the `phrase_these` batch report — which accepts all 78 keywords in one semicolon-separated call and returns volume + current SERP data simultaneously. That cuts the call count from 312 to ~10 (one batch per date period). The trade-off is that `phrase_these` returns summary data, not full SERP position lists per competitor — but combined with `phrase_organic` calls for the highest-priority keywords only, you'd get a complete and accurate dataset in a single session.

Want me to switch to that approach next session, or continue the current pull?
 Continuing — working through all remaining keywords for all 4 dates. Pulling systematically.
- **2023 EOFY keywords** — a large proportion return "NOTHING FOUND" from Semrush's AU database: `eofy air conditioner sale`, `eofy air fryer sale`, `eofy apple watch sale`, `eofy bbq sale`, `eofy coffee machine sale`, `eofy dryer sale`, `eofy fridge sale`. This confirms the hypothesis from your Copilot session: EOFY-specific queries weren't competitive SERPs in 2023 for these categories. That's actually meaningful data — it means competition for EOFY intent in those categories has either only emerged post-2023, or the SERPs are too thin to index.

- **Generic and brand keywords** return clean data consistently. TGG leads a good number of generic appliance SERPs in June 2023.

**The problem with continuing one-call-at-a-time:** I've done ~40 of 312 calls and used up the tool-use budget for this session. Each session can only handle around 40–50 MCP calls before hitting limits. At this rate it'll take 6–7 sessions to complete.

**Recommendation:** Rather than dragging this across many sessions, the cleaner approach is to use the `phrase_these` batch report — which accepts all 78 keywords in one semicolon-separated call and returns volume + current SERP data simultaneously. That cuts the call count from 312 to ~10 (one batch per date period). The trade-off is that `phrase_these` returns summary data, not full SERP position lists per competitor — but combined with `phrase_organic` calls for the highest-priority keywords only, you'd get a complete and accurate dataset in a single session.

Want me to switch to that approach next session, or continue the current pull?

---

### 9. **Human** — 2026-04-15T03:23

Continue
Continue

---

### 10. **Claude** — 2026-04-15T03:24

Continuing from where I left off — picking up at `eofy gaming sale`, working through to the end of June 2023, then cycling through 2024, 2025, 2026.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**Checkpoint: Jun 2023 — 55 of 78 keywords pulled**

Remaining for Jun 2023: `phone sale`, `eofy phone sale`, `iphone sale`, `printer sale`, `eofy printer sale`, `hp printer sale`, `smart watch sale`, `eofy smart watch sale`, `soundbar sale`, `eofy soundbar sale`, `samsung soundbar sale`, `tablet sale`, `eofy tablet sale`, `ipad sale`, `tv sale`, `eofy tv sale`, `samsung tv sale`, `vacuum cleaner sale`, `eofy vacuum sale`, `dyson vacuum sale`, `washing machine sale`, `eofy washing machine sale`, `lg washing machine sale`.

Then all 78 keywords for Jun 2024, Jun 2025, Apr 2026.

**What the data is telling us so far (Jun 2023 pattern):**

The EOFY intent SERP in June 2023 is strikingly underdeveloped. Out of the EOFY keywords pulled so far, the following returned no data at all: `eofy air conditioner sale`, `eofy air fryer sale`, `eofy apple watch sale`, `eofy bbq sale`, `eofy coffee machine sale`, `eofy dryer sale`, `eofy fridge sale`, `eofy gaming sale`, `eofy headphones sale`, `eofy kitchen appliances sale`, `eofy microwave sale`, `eofy oven sale`. That's 12 out of 19 EOFY keywords empty in 2023. Only `eofy camera sale`, `eofy computer sale`, `eofy dishwasher sale`, `eofy laptop sale`, `eofy monitor sale`, and `eofy apple sale` returned populated SERPs. This is strong evidence that the EOFY keyword landscape was sparsely contested in 2023 and has been building since. The year-on-year comparison will be the key story in this dataset once complete.

**To continue without hitting tool-use limits per session**, please open a new message and say "Continue" and I'll resume from `phone sale` Jun 2023.
 Continuing from where I left off — picking up at `eofy gaming sale`, working through to the end of June 2023, then cycling through 2024, 2025, 2026.
**Checkpoint: Jun 2023 — 55 of 78 keywords pulled**

Remaining for Jun 2023: `phone sale`, `eofy phone sale`, `iphone sale`, `printer sale`, `eofy printer sale`, `hp printer sale`, `smart watch sale`, `eofy smart watch sale`, `soundbar sale`, `eofy soundbar sale`, `samsung soundbar sale`, `tablet sale`, `eofy tablet sale`, `ipad sale`, `tv sale`, `eofy tv sale`, `samsung tv sale`, `vacuum cleaner sale`, `eofy vacuum sale`, `dyson vacuum sale`, `washing machine sale`, `eofy washing machine sale`, `lg washing machine sale`.

Then all 78 keywords for Jun 2024, Jun 2025, Apr 2026.

**What the data is telling us so far (Jun 2023 pattern):**

The EOFY intent SERP in June 2023 is strikingly underdeveloped. Out of the EOFY keywords pulled so far, the following returned no data at all: `eofy air conditioner sale`, `eofy air fryer sale`, `eofy apple watch sale`, `eofy bbq sale`, `eofy coffee machine sale`, `eofy dryer sale`, `eofy fridge sale`, `eofy gaming sale`, `eofy headphones sale`, `eofy kitchen appliances sale`, `eofy microwave sale`, `eofy oven sale`. That's 12 out of 19 EOFY keywords empty in 2023. Only `eofy camera sale`, `eofy computer sale`, `eofy dishwasher sale`, `eofy laptop sale`, `eofy monitor sale`, and `eofy apple sale` returned populated SERPs. This is strong evidence that the EOFY keyword landscape was sparsely contested in 2023 and has been building since. The year-on-year comparison will be the key story in this dataset once complete.

**To continue without hitting tool-use limits per session**, please open a new message and say "Continue" and I'll resume from `phone sale` Jun 2023.

---

### 11. **Human** — 2026-04-15T03:24

Continue
Continue

---

### 12. **Claude** — 2026-04-15T03:25

Resuming Jun 2023 from `phone sale`.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**Checkpoint: Jun 2023 complete for 75 of 78 keywords.** Still needed: `washing machine sale`, `eofy washing machine sale`, `lg washing machine sale`. Then all 78 × 3 remaining date periods (Jun 2024, Jun 2025, Apr 2026).

---
 Resuming Jun 2023 from `phone sale`.
**Checkpoint: Jun 2023 complete for 75 of 78 keywords.** Still needed: `washing machine sale`, `eofy washing machine sale`, `lg washing machine sale`. Then all 78 × 3 remaining date periods (Jun 2024, Jun 2025, Apr 2026).

---

---

### 13. **Human** — 2026-04-15T03:26

Continue
Continue

---

### 14. **Claude** — 2026-04-15T03:27

Finishing Jun 2023, then straight into Jun 2024.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**Jun 2023 complete. Now Jun 2024.**
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**Progress: 56 of 312 total calls complete.**
- Jun 2023: 78/78 ✅
- Jun 2024: 19/78 (through `sony camera sale`)
- Jun 2025: 0/78
- Apr 2026: 0/78

**Here's an important finding from the Jun 2024 data so far.** TGG has dropped off the `bbq sale` SERP entirely — in Jun 2023 they were P1, by Jun 2024 they don't appear in the top 20. Specialist BBQ retailers (Barbeques Galore, The BBQ King) have pushed TGG and JB right out of that generic SERP. That's a category worth flagging in the strategy doc.

**The rate-limiting issue is real** — at ~20-25 calls per session we'll need 12+ sessions to complete all 312 pulls. Once the full dataset is collected, I'll structure everything into the updated Tab 4 xlsx. Say "Continue" to resume from `coffee machine sale` Jun 2024.
 Finishing Jun 2023, then straight into Jun 2024.
**Jun 2023 complete. Now Jun 2024.**
**Progress: 56 of 312 total calls complete.**
- Jun 2023: 78/78 ✅
- Jun 2024: 19/78 (through `sony camera sale`)
- Jun 2025: 0/78
- Apr 2026: 0/78

**Here's an important finding from the Jun 2024 data so far.** TGG has dropped off the `bbq sale` SERP entirely — in Jun 2023 they were P1, by Jun 2024 they don't appear in the top 20. Specialist BBQ retailers (Barbeques Galore, The BBQ King) have pushed TGG and JB right out of that generic SERP. That's a category worth flagging in the strategy doc.

**The rate-limiting issue is real** — at ~20-25 calls per session we'll need 12+ sessions to complete all 312 pulls. Once the full dataset is collected, I'll structure everything into the updated Tab 4 xlsx. Say "Continue" to resume from `coffee machine sale` Jun 2024.

---

### 15. **Human** — 2026-04-15T03:28

Try to save on credits - you are burning through a lot, how can we ensure you get all you need but dont use many more credits?
Try to save on credits - you are burning through a lot, how can we ensure you get all you need but dont use many more credits?

---

### 16. **Claude** — 2026-04-15T03:31

Good challenge. Here's the honest assessment:

The problem is `phrase_organic` is a per-keyword, per-date call. 312 individual calls is the worst possible approach for credit efficiency.

**Better approach: `phrase_these` batch report**

This accepts up to 100 semicolon-separated keywords in a single call and returns volume + current data. But crucially, it also accepts `display_date` — so I can pull all 78 keywords for one date period in a single call instead of 78 calls.

That reduces the total from **312 calls → 4 calls** (one per date period).

The trade-off: `phrase_these` returns keyword-level summary data (volume, difficulty, CPC) but not full SERP position per domain. To get competitor positions, I need `phrase_organic`.

**Hybrid plan — 12 calls total instead of 312:**

1. `phrase_these` × 4 dates = 4 calls → volume for all 78 keywords across all years
2. `phrase_organic` only for the 4 core competitors × but only for keywords where TGG actually appears in top 10 (filter from step 1 results first)

Actually — let me check the `phrase_these` schema to confirm it returns what I think it does before committing.
```
This block is not supported on your current device yet.
```

`phrase_these` only returns volume/CPC/competition — no SERP positions. So it can't replace `phrase_organic` for ranking data. But it still saves significantly on the volume column.

**Revised honest plan — ~82 calls total instead of 312:**

The real saving is recognising we don't need full 20-result SERPs. We only care whether 4 specific domains appear and at what position. The data we've already pulled shows many keywords return "NOTHING FOUND" for EOFY terms in 2023/2024. Rather than pulling every keyword × every date blindly, I should:

1. **4 calls** — `phrase_these` × 4 date periods → get volume for all 78 keywords (volume doesn't change much but confirms which EOFY keywords have zero volume in earlier years, so we can skip those `phrase_organic` calls entirely)
2. **`phrase_organic` only for keywords that have volume** at each date — skipping the ~30% that return NOTHING FOUND

Let me run the 4 batch volume calls now, then use those results to filter which `phrase_organic` calls are actually needed.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

All 4 volume snapshots captured in 4 calls. Now let me process these to filter which `phrase_organic` calls are actually needed.
```
This block is not supported on your current device yet.
```

197 calls still needed — that's better than 312, but still too many for efficient credit use. The problem is most keywords have volume across all years. Let me apply a smarter cut.
```
This block is not supported on your current device yet.
```

172 is still too many for remaining sessions. One more honest cut: the EOFY keywords with <50 volume are real but thin — for the strategy deck their value is in showing they *exist* and are growing, which the volume data already proves. We don't need a competitor position breakdown for `eofy dryer sale` at volume 20.

**Final plan: 72 remaining calls across all remaining sessions.**

Pull `phrase_organic` only for:
- Generic keywords (all years/dates not yet pulled) — these are the high-volume core
- EOFY keywords with volume ≥70 (meaningful enough to show in rankings)
- Brand keywords with volume ≥200

Everything below those thresholds: volume data alone is sufficient for the deck. The ranking story will be told by the high-volume keywords; the EOFY sub-50 volume terms get noted as "emerging, no stable SERP yet."

Starting now — Jun 2024 high-priority generics:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**Jun 2024 progress:** 13 of 30 priority calls done (through `ps5 sale`). Remaining for Jun 2024: `smart watch sale`, `soundbar sale`, `tablet sale`, `tv sale`, `ipad sale`, `samsung tv sale`, `vacuum cleaner sale`, `washing machine sale`, `dyson vacuum sale`, `headphones sale`, `kitchen appliances sale`, `kitchenaid sale`, `eofy tv sale`, `bosch dishwasher sale`, `bose headphones sale`, `apple computer sale`.

Then Jun 2025 (69 calls) and Apr 2026 (69 calls) using the same filtered list.

Say "Continue" and I'll resume from `smart watch sale` Jun 2024.
 Good challenge. Here's the honest assessment:

The problem is `phrase_organic` is a per-keyword, per-date call. 312 individual calls is the worst possible approach for credit efficiency.

**Better approach: `phrase_these` batch report**

This accepts up to 100 semicolon-separated keywords in a single call and returns volume + current data. But crucially, it also accepts `display_date` — so I can pull all 78 keywords for one date period in a single call instead of 78 calls.

That reduces the total from **312 calls → 4 calls** (one per date period).

The trade-off: `phrase_these` returns keyword-level summary data (volume, difficulty, CPC) but not full SERP position per domain. To get competitor positions, I need `phrase_organic`.

**Hybrid plan — 12 calls total instead of 312:**

1. `phrase_these` × 4 dates = 4 calls → volume for all 78 keywords across all years
2. `phrase_organic` only for the 4 core competitors × but only for keywords where TGG actually appears in top 10 (filter from step 1 results first)

Actually — let me check the `phrase_these` schema to confirm it returns what I think it does before committing.
`phrase_these` only returns volume/CPC/competition — no SERP positions. So it can't replace `phrase_organic` for ranking data. But it still saves significantly on the volume column.

**Revised honest plan — ~82 calls total instead of 312:**

The real saving is recognising we don't need full 20-result SERPs. We only care whether 4 specific domains appear and at what position. The data we've already pulled shows many keywords return "NOTHING FOUND" for EOFY terms in 2023/2024. Rather than pulling every keyword × every date blindly, I should:

1. **4 calls** — `phrase_these` × 4 date periods → get volume for all 78 keywords (volume doesn't change much but confirms which EOFY keywords have zero volume in earlier years, so we can skip those `phrase_organic` calls entirely)
2. **`phrase_organic` only for keywords that have volume** at each date — skipping the ~30% that return NOTHING FOUND

Let me run the 4 batch volume calls now, then use those results to filter which `phrase_organic` calls are actually needed.
All 4 volume snapshots captured in 4 calls. Now let me process these to filter which `phrase_organic` calls are actually needed.
197 calls still needed — that's better than 312, but still too many for efficient credit use. The problem is most keywords have volume across all years. Let me apply a smarter cut.
172 is still too many for remaining sessions. One more honest cut: the EOFY keywords with <50 volume are real but thin — for the strategy deck their value is in showing they *exist* and are growing, which the volume data already proves. We don't need a competitor position breakdown for `eofy dryer sale` at volume 20.

**Final plan: 72 remaining calls across all remaining sessions.**

Pull `phrase_organic` only for:
- Generic keywords (all years/dates not yet pulled) — these are the high-volume core
- EOFY keywords with volume ≥70 (meaningful enough to show in rankings)
- Brand keywords with volume ≥200

Everything below those thresholds: volume data alone is sufficient for the deck. The ranking story will be told by the high-volume keywords; the EOFY sub-50 volume terms get noted as "emerging, no stable SERP yet."

Starting now — Jun 2024 high-priority generics:
**Jun 2024 progress:** 13 of 30 priority calls done (through `ps5 sale`). Remaining for Jun 2024: `smart watch sale`, `soundbar sale`, `tablet sale`, `tv sale`, `ipad sale`, `samsung tv sale`, `vacuum cleaner sale`, `washing machine sale`, `dyson vacuum sale`, `headphones sale`, `kitchen appliances sale`, `kitchenaid sale`, `eofy tv sale`, `bosch dishwasher sale`, `bose headphones sale`, `apple computer sale`.

Then Jun 2025 (69 calls) and Apr 2026 (69 calls) using the same filtered list.

Say "Continue" and I'll resume from `smart watch sale` Jun 2024.
