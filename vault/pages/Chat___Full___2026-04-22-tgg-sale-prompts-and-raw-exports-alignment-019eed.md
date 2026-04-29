---
title: TGG sale prompts and raw exports alignment (full)
parent: Chat/Light/2026-04-22-tgg-sale-prompts-and-raw-exports-alignment-019eed
uuid: 019eed46-9838-48f2-b3c1-0c29d0f8fe60
---

#chat/full #project/main #status/completed

# TGG sale prompts and raw exports alignment — Full Transcript

→ Light view: [[Chat/Light/2026-04-22-tgg-sale-prompts-and-raw-exports-alignment-019eed]]
→ Medium view: [[Chat/Medium/2026-04-22-tgg-sale-prompts-and-raw-exports-alignment-019eed]]

**Messages:** 10 | **Date:** 2026-04-22

---

### 1. **Human** — 2026-04-22T04:06

does tgg sale prompts align to the raw exports?
does tgg sale prompts align to the raw exports?

---

### 2. **Claude** — 2026-04-22T04:07

Let me read the skill files and then examine both files to answer this question.

Let me first read the uploaded files to understand their contents.
```
This block is not supported on your current device yet.
```

Now let me read both files.
```
This block is not supported on your current device yet.
```

Now I need to compare the prompts in the xlsx against the prompts in the CSV. The xlsx has prompts in the "Prompts" sheet. The CSV has a "prompt" column. Let me check if all prompts in the xlsx exist in the CSV.
```
This block is not supported on your current device yet.
```

So the situation is clear:
- XLSX has 86 prompts, all of which are present in the CSV
- CSV has 391 unique prompts, of which 305 are NOT in the XLSX

The XLSX appears to be a curated subset (sale/transactional intent prompts), while the CSV is a much broader export covering many more intent types (best, reliable, trusted, quality, compare, how to choose, etc.).

So the XLSX is a subset of the CSV, not a mismatch. Every XLSX prompt exists in the CSV. The 305 extra prompts in the CSV are different intent clusters that weren't included in the XLSX.All 86 XLSX prompts exist in the CSV. No mismatches.

The CSV is a broader export, 391 unique prompts vs 86 in the XLSX. The 305 extra prompts in the CSV are distinct intent clusters not covered by the XLSX: best/recommend queries ("What are the best..."), reliability/trust queries ("Which trusted...", "Who sells quality..."), how-to-choose queries ("How do I compare..."), and a set of more specific transactional prompts ("Best place to get a 55-inch smart TV near me", "Retailers offering Bosch dishwashers", etc.).

The XLSX looks intentionally scoped to sale/affordability/deals intent. The CSV is the full fanout export across all intent types. If the XLSX is meant to be exhaustive for that intent cluster, it's clean. If it was supposed to cover more of the CSV's transactional prompts (the "Best place to get..." and "Retailers offering..." rows), those are missing.

Want me to pull out the transactional-intent prompts from the CSV that aren't in the XLSX?
 
All 86 XLSX prompts exist in the CSV. No mismatches.

The CSV is a broader export, 391 unique prompts vs 86 in the XLSX. The 305 extra prompts in the CSV are distinct intent clusters not covered by the XLSX: best/recommend queries ("What are the best..."), reliability/trust queries ("Which trusted...", "Who sells quality..."), how-to-choose queries ("How do I compare..."), and a set of more specific transactional prompts ("Best place to get a 55-inch smart TV near me", "Retailers offering Bosch dishwashers", etc.).

The XLSX looks intentionally scoped to sale/affordability/deals intent. The CSV is the full fanout export across all intent types. If the XLSX is meant to be exhaustive for that intent cluster, it's clean. If it was supposed to cover more of the CSV's transactional prompts (the "Best place to get..." and "Retailers offering..." rows), those are missing.

Want me to pull out the transactional-intent prompts from the CSV that aren't in the XLSX?

---

### 3. **Human** — 2026-04-22T04:09

ensure tgg_sale includes ALL of the data scoped to sale/deals intent.
ensure tgg_sale includes ALL of the data scoped to sale/deals intent.

---

### 4. **Claude** — 2026-04-22T04:12

Let me look at the full CSV to identify all sale/deals intent prompts, then compare against the XLSX.
```
This block is not supported on your current device yet.
```

Now I need to classify all 391 prompts into intent buckets to identify which ones are "sale/deals intent". Let me think about what constitutes sale/deals intent vs other intents:

**Sale/deals intent** (transactional, price-driven):
- "Deals on...", "...on sale", "...specials", "Cheapest...", "...under $X", "...affordable...", "...budget...", "...clearance...", "...interest-free finance...", "Best place to get...", "Retailers offering...", "Retailers selling...", "Shops that...", "Shops with...", "Stores stocking...", "Stores with...", "...available online", "...in stock", "Current sales on...", "...with delivery included", "...with free delivery", "...with installation", "...same-day pickup"


- "Best place to get a 55-inch smart TV near me"
- "Best place to get a French door fridge with water dispenser"
- "Best place to get freestanding ovens with delivery"
- "Best place to get vacuums for pet hair"
- "Best place to get washer-dryer combos with delivery"
- "Best place to get washing machines with installation included"

Now I'm cross-referencing the CSV against the 86 prompts already in the XLSX to find the sale/deals intent ones that haven't been captured yet.

Continuing through the list, I see more product-specific queries like compact benchtop ovens in Australia, compact dishwashers and dryers for apartments, and various retailer-focused prompts about TVs, washing machines, and kitchen appliances with specific features like delivery, installation, warranties, or energy efficiency.

Now I'm looking at the second batch of search queries to categorize. These include more retailer-specific searches for items like Bosch dishwashers, second fridges, wall-mount TV bundles, and slimline dishwashers, along with informational queries that don't indicate purchase intent. I'm also identifying the patterns for non-sale prompts—those asking about reliability, trustworthiness, or general information rather than deals or product availability. The XLSX file already covers the deals and pricing cluster pretty well with prompts about affordable options, clearance, and in-stock items. But I'm noticing a gap—there are several location-specific and availability-focused queries missing, like "best place to get [product] near me" and "available now" variations. These seem to fall into that same transactional intent but with a local or immediate availability angle that isn't captured yet. I'm adding those two missing prompts to the classification and recognizing that several items in the list blur the line between product availability and deals—they're really about where to purchase rather than pure discounts. Now I need to pull the full CSV data for these sale/deals prompts and populate the XLSX sheets with the metrics like mention percentages and run counts.

Looking at what's available, the CSV contains fanout metrics but the XLSX needs TGG mention data that must be coming from a separate Profound aggregation, so I'll need to map the fanout information from the CSV while sourcing the mention statistics from elsewhere. The CSV columns include fanout metrics like fanout_query, fanout_count, and fanout_share, but it's missing the TGG Mention data entirely. The XLSX sheets need both fanout information and TGG metrics, which means I'd need to pull TGG Mention %, TGG Mentions, and Total Runs from Profound's prompt-level data—data that isn't in this CSV export. I should let Simon know about this gap before I can fully populate the missing prompts. I need to take a more systematic approach here. Let me classify all the prompts in the CSV by intent, identify which sale/deals prompts are missing from the XLSX, and then add those rows with their fanout data. For the TGG metrics that aren't in the CSV, I should ask Simon where those come from before proceeding. I'll categorize the prompts using keyword matching against the existing product categories from the XLSX. For sale/deals intent, I'm looking for clear signals like "on sale," "deals on," "specials," "clearance," "cheapest," "affordable," "budget," and price-related terms—these are the strongest indicators I should use to filter the CSV data.

I'm also considering borderline cases like availability signals ("in stock," "available now," "where to find," "best place to get") and service-related terms ("with delivery," "with installation," "interest-free finance," "package deals"). Even though these aren't explicitly about price, they're still shopping-intent queries, so I'll include them in my classification. Purely informational questions like "How big should a TV be?" don't count as deals intent, so I'll exclude those.

Looking at what's clearly not deals-related—queries about reliability, comparisons, recommendations, and brand trust—I notice these are already captured in the XLSX, which is helpful. The gap I'm identifying is in specific sale/deals prompts that aren't yet in the spreadsheet, like "Best place to get a 55-" which seems to be cut off but points to a shopping-specific intent I should track. I'm continuing through the rest of the search queries, covering dishwashers with free delivery, cooktops with installation, energy-efficient washers, fridges with removal services, integrated appliances, robot vacuums, current Bosch sales, garage fridges, same-day vacuum pickup, TV bundles, compact fridges, slimline dishwashers, dual-fuel cookers, washer warranties, and plumbed-in fridge delivery options—totaling 33 distinct product and service queries.

Now I'm noticing the CSV is missing TGG mention percentage data that exists in the XLSX structure. I should flag this gap to Simon since he wants the tgg_sale sheet to include all sale/deals intent data, but I can still populate the sheets with the fanout data I have and leave the TGG columns blank with a note explaining what's missing.

Writing the Python script...
```
This block is not supported on your current device yet.
```

Good. 33 missing sale/deals prompts. Now I need to add them to the XLSX. I'll need to:
1. Load the existing XLSX with openpyxl
2. Add the 33 missing prompts to the Prompts sheet (with category inferred, TGG columns blank)
3. Add their fanout data to the Fanout Breakdown sheet
4. Save

For categories, I'll infer from the prompt text based on the existing categories in the XLSX.

Let me also check the XLSX skill for how to properly handle it, but since I'm just adding rows, I can use openpyxl directly.


Now I'm mapping the missing prompts to their categories—TVs and AV for the screen-related ones, Fridges & Freezers for the refrigerator prompts, Ovens, Cooktops & Rangehoods for the cooking appliances, and Vacuums for the cleaning products. ", "compact vacuums", "high-suction cordless vacuums", "shops offering same-day pickup for vacuums", "retailers selling robot vacuums", "vacuum cleaners with extended warranty" → Vacuums
- Washing Machines: "washer-dryer combos", "washing machines with installation", "large-capacity washing machines", "energy-efficient washing machines", "extended warranty options for washers" → Washing Machines
- Dishwashers: "compact dishwasher", "quiet dishwasher", "dishwashers with extended warranty", "dishwashers with free delivery", "integrated dishwashers", "Bosch dishwashers", "slimline dishwashers" → Dishwashers
- Dryers: "compact dryers" → Dryers
- Ovens/Cooktops: "Compact benchtop ovens", "electric cooktops", "dual-fuel cookers" → Ovens, Cooktops & Rangehoods
- Fridges: "free removal with new fridge purchase" → Fridges & Freezers
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now I need to build the updated XLSX. The issue is that TGG Mention %, TGG Mentions, Total Runs aren't in the CSV. I should flag this and ask Simon before adding blank rows, or add them with blanks.

Actually, I'll just produce the file with the fanout data populated from the CSV, and leave TGG columns blank for the new rows. I'll note this clearly in my response.

Let me now build the category mapping and add the rows.
```
This block is not supported on your current device yet.
```

All 33 prompts exist in CSV with fanout data. But there are a huge number of fanout rows per prompt (300-555 each). The XLSX Fanout Breakdown currently has 430 rows for 86 prompts, so it seems like it's not including ALL fanout rows per prompt, just the top N. Let me check what the existing fanout breakdown looks like - how many rows per prompt.
```
This block is not supported on your current device yet.
```

The XLSX keeps the top 5 fanout rows by fanout_count for each prompt. Now I need to:
1. For each of the 33 missing prompts, get the top 5 fanout rows from CSV
2. Add them to the Fanout Breakdown sheet
3. Add the prompts to the Prompts sheet (TGG columns blank since that data isn't in the CSV)

Note: The CSV `fanout_count` in the XLSX vs CSV - let me check if the counts match. The XLSX shows `fanout_count` as 70, 16, 9, 9, 7 for the fans prompt. 

The CSV has those same top rows sorted by fanout_count descending, which is what I need. For the Prompts sheet, I'm missing TGG Mention %, TGG Mentions, and Total Runs—those aren't in the CSV, so I'll flag this to Simon and add the prompts with blanks for those columns, noting they need to be populated from Profound.

Building the updated XLSX now...
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

33 prompts added. Prompts sheet: 86 → 119. Fanout Breakdown: 430 → 595 rows (top 5 fanout queries per new prompt, by fanout_count).

One gap to flag: **TGG Mention %, TGG Mentions, and Total Runs are blank for all 33 new rows** on both sheets. That data isn't in the CSV export. You'll need to pull it from Profound for those 33 prompts and backfill.
 
33 prompts added. Prompts sheet: 86 → 119. Fanout Breakdown: 430 → 595 rows (top 5 fanout queries per new prompt, by fanout_count).

One gap to flag: **TGG Mention %, TGG Mentions, and Total Runs are blank for all 33 new rows** on both sheets. That data isn't in the CSV export. You'll need to pull it from Profound for those 33 prompts and backfill.

---

### 5. **Human** — 2026-04-22T04:38

this is 3 month export - in early feb we added more prompts.
this is 3 month export - in early feb we added more prompts.

---

### 6. **Claude** — 2026-04-22T04:41

Simon is providing context that the 3-month export is split into two halves, and in early February they added more prompts. This likely explains why the TGG Mention % data isn't in the CSV I was working with - these split files might contain that data. Let me read both files to understand their structure.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Half 2 has a corrupt date column. Let me dig into that. The date range for half 2 is clearly garbage. Let me investigate more carefully. The file seems to have some embedded response text bleeding into the date column. I should parse it more carefully.

Also, I should understand the context: this is a raw Profound export with individual run data (run_id, date, platform, prompt, mentions, etc.). From this I can compute TGG Mention % for each prompt. The "mentioned?" column is likely boolean for whether TGG was mentioned.

Let me figure out the date issue with half 2 and then compute TGG mention stats per prompt.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

So the prompt count jumped from ~60 to 390 on Feb 3. That's when the bulk of the prompts were added. Let me now compute TGG Mention % per prompt across the full dataset, and then figure out how to handle prompts that were only active for part of the period.

The key question is: how to compute TGG Mention % for the Prompts sheet. The 'mentioned?' column has Yes/No values. I need to compute:
- TGG Mentions = count of runs where mentioned? == 'Yes'
- Total Runs = total count of runs


- TGG Mention % = TGG Mentions / Total Runs

But I need to be careful about the prompt expansion on Feb 3 - prompts added then have fewer total runs than prompts that were active from Jan 22. So I'll calculate these stats individually for each prompt.
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

All TGG columns are now fully populated from the raw run data. Quick summary of what changed:

**Data source:** 234,741 clean rows across Jan 22 to Apr 21. Prompt count jumped from ~60 to 390 on Feb 3, so the 33 new prompts have proportionally fewer total runs than the original 86. That's reflected accurately in the figures rather than normalised out.

**File state:**
- Prompts sheet: 119 rows, 0 blank TGG cells
- Fanout Breakdown: 595 rows, all TGG % backfilled

One thing worth flagging: the TGG Mention % figures in this file will differ from the previous XLSX for the original 86 prompts, because those were calculated over the full 3-month window rather than whatever window Profound used for the earlier export. Worth a spot-check on a few known prompts before you use this as a source of truth.
 
All TGG columns are now fully populated from the raw run data. Quick summary of what changed:

**Data source:** 234,741 clean rows across Jan 22 to Apr 21. Prompt count jumped from ~60 to 390 on Feb 3, so the 33 new prompts have proportionally fewer total runs than the original 86. That's reflected accurately in the figures rather than normalised out.

**File state:**
- Prompts sheet: 119 rows, 0 blank TGG cells
- Fanout Breakdown: 595 rows, all TGG % backfilled

One thing worth flagging: the TGG Mention % figures in this file will differ from the previous XLSX for the original 86 prompts, because those were calculated over the full 3-month window rather than whatever window Profound used for the earlier export. Worth a spot-check on a few known prompts before you use this as a source of truth.

---

### 7. **Human** — 2026-04-22T04:41

what from this prompt tracking are sales / deals type proompts we could think of adding? remove dupes add as a tab
what from this prompt tracking are sales / deals type proompts we could think of adding? remove dupes add as a tab

---

### 8. **Claude** — 2026-04-22T04:43

Let me read the prompt tracking Excel file to understand its structure and content.
```
This block is not supported on your current device yet.
```

That's a lot of data. Now I need to:
1. Extract the unique prompts from the "Profound Prompts" sheet
2. Compare against what's already in tgg_sale_prompts_final.xlsx
3. Identify which ones are sale/deals intent and not already included
4. Add them as a new tab

Let me parse the prompts from the Profound Prompts sheet. Looking at the data, I can see the prompts are in the 7th column (after platform, topic, tags, region, persona, type, prompt). 

I'll write a script to extract all the prompts from that column programmatically.Now let me extract the prompts from the Profound sheet and compare against the existing file.
```
This block is not supported on your current device yet.
```

The "Profound Prompts" sheet seems to have the column headers not where I expected. Let me look at the actual structure more carefully, and also check the other sheets.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The Profound Prompts sheet has 61 unique prompts, all of which are already the ones we know about. The Adthena and Peec prompts are the 240 that are new.

Let me look at what those 240 new prompts are, and filter for sale/deals intent ones.
```
This block is not supported on your current device yet.
```

Now I need to filter the 104 "sale" prompts to remove:
1. Duplicates (same prompt appearing with different casing)
2. Prompts that are clearly off-topic (like "Can I buy replacement shelves or drawers for my fridge?" which snuck in via "buy")
3. The "find me the best price for [specific product]" and "where to buy [specific product]" prompts are interesting - they're specific product queries. These seem valid as sale/deals intent. But the ones that are duplicated (uppercase/lowercase) need deduplication.

Let me clean this up and also note that several prompts appear to be duplicated (e.g., "Find me the best price for FFALCON..." and "find me the best price for ffalcon..."). I should deduplicate case-insensitively.

 
Now let me extract the prompts from the Profound sheet and compare against the existing file.

---

### 9. **Human** — 2026-04-22T04:44

goo into each tab, noot just profound one? ignore accuranker and keyword tagging tabs and AIO kws - only focus on prompts for AI  we could consider adding (not yet tracked)
goo into each tab, noot just profound one? ignore accuranker and keyword tagging tabs and AIO kws - only focus on prompts for AI  we could consider adding (not yet tracked)

---

### 10. **Claude** — 2026-04-22T04:47

Let me look at each relevant tab more carefully: Profound Prompts, Profound 2, Peec Prompts, Adthena LLM Prompts. I need to extract all prompts from these tabs and find sale/deals ones not yet in the sale file.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now I need to curate this list. Before adding all 80 to the file, I need to make some judgment calls:

1. **Clear duplicates** (same prompt, different casing/format from different tabs) - e.g., "Find me the best price for FFALCON 43\" 4K UHD Google TV 24" (Peec) and "find me the best price for ffalcon 43 4k uhd google tv 24\"" (Adthena). I need to use the cleaner version.

2. **Borderline misclassified** as sale/deals - some things my signal matching picked up that shouldn't really be in the sale tab:
   - Cashback offers on fridges are genuinely sale-related, but questions about replacement parts, accessories, store locations, and brand reliability don't belong here. I need to filter out the trust/brand queries and product-specific accessory questions, keeping only the ones with clear deal intent.

Now I'm thinking through the broader categories—price comparisons and market research questions about where Australians buy appliances are too general and don't signal someone looking for deals. The specific product queries like finding the best price for a FFALCON TV or JBL headphones are transactional and worth including, though they'll need updating as products change. Seasonal queries around Black Friday are solid deal indicators, so I should definitely add those.

Let me narrow down the full list to the strongest candidates that actually reflect deal-seeking behavior. then deduplicate cross-tab duplicates.

The clean list of genuinely sale/deals intent (removing weak signals and keeping canonical versions):

**KEEP - clear sale/deals:**
- Are there any cashback offers on fridges this month?
- best fridge deals today
- best vacuum cleaner deals
- best washing machine deals
- Can I buy a fridge online & get installation included? (borderline - buying intent + installation)
- Can I buy online and pick up in-store at The Good Guys? (transactional)
- cheapest fridge australia
- cheapest front load washing machine
- Does The Good Guys offer free delivery on big appliances?
- Does The Good Guys price match competitors?
- Find me the best price for [specific products] - keep canonical (Peec) versions
- Where to buy [specific products] - keep canonical (Peec) versions
- french door fridge price comparison
- Is The Good Guys cheaper than Harvey Norman or JB Hi-Fi?
- stick vacuum price comparison
- vacuum cleaner price comparison
- washing machine price comparison australia
- what are the best black friday deals on [category] (all 13)
- Where can I buy a new fridge with free delivery?
- where can i find the best fridge deals in australia?
- where can i get good deals on tvs this month in australia?
- where should i buy a new washing machine in australia?
- Where's the easiest place to buy appliances online in australia?
- which appliance retailers offer fast delivery?
- Which Australian retailers offer the best fridge deals?
- which store has the best range of washing machines in australia?
- Which stores have fridge sales right now?
- who usually has cheaper washing machines, jb hi-fi or the good guys?
- who's cheaper for fridges in australia - the good guys or harvey norman?
- what's the best place to buy a fridge and washer together in australia?
- what's the best place to buy a tv in australia?
- How do I use a discount code on The Good Guys website?
- are online appliance prices cheaper than in-store in australia?
- is the good guys cheaper than other appliance stores in australia?
- where should i buy appliances for a full home renovation?

Now I'm being more precise about what actually qualifies for this tracking. I need prompts where someone's actively looking to purchase and The Good Guys should show up, or they're comparing prices and deals across retailers. The market research questions about where Australians generally shop are too broad for what we're measuring here. Let me finalize this list and set up the new tracking tab.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**64 candidate prompts** added as a new "Candidate Prompts" tab, tagged by source and grouped into 6 intent types:

**Deals discovery (15)** — "best fridge deals today", "Which stores have fridge sales right now?", "where can i get good deals on tvs this month in australia?", etc. Direct sale/deals queries where TGG should be visible.

**TGG purchase/price intent (9)** — "Does The Good Guys price match?", "Is The Good Guys cheaper than Harvey Norman?", "Can I buy online and pick up in-store?" etc. These are explicitly TGG-branded commercial queries from Peec/Adthena.

**Price comparison (6)** — "french door fridge price comparison", "vacuum cleaner price comparison", "washing machine price comparison australia" etc.

**Retailer discovery (8)** — "what's the best place to buy a tv in australia?", "which appliance retailers offer fast delivery?" etc. High TGG relevance.

**Product price/purchase (18)** — The "Find me the best price for..." and "Where to buy [specific product]" queries from Peec. Flagged for refresh when range changes.

**Seasonal/event (13)** — All Black Friday category queries. Flagged to refresh annually.

Two things worth flagging: the specific product queries (FFALCON, JBL, LG model numbers) will go stale quickly as range turns over. And the "where do australians usually buy whitegoods?" type queries are borderline — they're retailer discovery but more market research than purchase intent, so call those if you think they're worth tracking.
 
**64 candidate prompts** added as a new "Candidate Prompts" tab, tagged by source and grouped into 6 intent types:

**Deals discovery (15)** — "best fridge deals today", "Which stores have fridge sales right now?", "where can i get good deals on tvs this month in australia?", etc. Direct sale/deals queries where TGG should be visible.

**TGG purchase/price intent (9)** — "Does The Good Guys price match?", "Is The Good Guys cheaper than Harvey Norman?", "Can I buy online and pick up in-store?" etc. These are explicitly TGG-branded commercial queries from Peec/Adthena.

**Price comparison (6)** — "french door fridge price comparison", "vacuum cleaner price comparison", "washing machine price comparison australia" etc.

**Retailer discovery (8)** — "what's the best place to buy a tv in australia?", "which appliance retailers offer fast delivery?" etc. High TGG relevance.

**Product price/purchase (18)** — The "Find me the best price for..." and "Where to buy [specific product]" queries from Peec. Flagged for refresh when range changes.

**Seasonal/event (13)** — All Black Friday category queries. Flagged to refresh annually.

Two things worth flagging: the specific product queries (FFALCON, JBL, LG model numbers) will go stale quickly as range turns over. And the "where do australians usually buy whitegoods?" type queries are borderline — they're retailer discovery but more market research than purchase intent, so call those if you think they're worth tracking.
