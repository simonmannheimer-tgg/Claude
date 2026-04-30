---
title: Sales prompts and performance data analysis (full)
parent: Chat/Light/2026-04-22-sales-prompts-and-performance-data-analysis-7c0502
uuid: 7c0502b2-846a-4ba9-a962-ef9f7518cf3e
---

#chat/full #project/eofy #status/completed

# Sales prompts and performance data analysis — Full Transcript

→ Light view: [[Chat/Light/2026-04-22-sales-prompts-and-performance-data-analysis-7c0502]]
→ Medium view: [[Chat/Medium/2026-04-22-sales-prompts-and-performance-data-analysis-7c0502]]

**Messages:** 8 | **Date:** 2026-04-22

---

### 1. **Human** — 2026-04-22T03:42

which prompts are about sales or could relate to sale or offer or discounts?

e.g. which could be relevant for these? also their latest data for visibility and citation etc. (last 28 days) and query fanouts. 

https://www.thegoodguys.com.au/eofy-sale
https://www.thegoodguys.com.au/deals/air-conditioners-and-fans
https://www.thegoodguys.com.au/deals/bbqs
https://www.thegoodguys.com.au/deals/bundle
https://www.thegoodguys.com.au/deals/coffee-machines
https://www.thegoodguys.com.au/deals/cooking
https://www.thegoodguys.com.au/deals/dishwashers
https://www.thegoodguys.com.au/deals/dryers
https://www.thegoodguys.com.au/deals/fridge-and-laundry
https://www.thegoodguys.com.au/deals/fridges
https://www.thegoodguys.com.au/deals/health-fitness-beauty
https://www.thegoodguys.com.au/deals/headphones-and-soundbars
https://www.thegoodguys.com.au/deals/heaters
https://www.thegoodguys.com.au/deals/kitchen
https://www.thegoodguys.com.au/deals/kitchen-appliances
https://www.thegoodguys.com.au/deals/kitchenware-sinks-and-taps
https://www.thegoodguys.com.au/deals/laptops
https://www.thegoodguys.com.au/deals/microwaves
https://www.thegoodguys.com.au/deals/phone-and-smart-watches
https://www.thegoodguys.com.au/deals/smart-home
https://www.thegoodguys.com.au/deals/technology
https://www.thegoodguys.com.au/deals/tvs
https://www.thegoodguys.com.au/deals/vacuums-and-cleaning
https://www.thegoodguys.com.au/deals/washing-machines
which prompts are about sales or could relate to sale or offer or discounts?

e.g. which could be relevant for these? also their latest data for visibility and citation etc. (last 28 days) and query fanouts. 

https://www.thegoodguys.com.au/eofy-sale
https://www.thegoodguys.com.au/deals/air-conditioners-and-fans
https://www.thegoodguys.com.au/deals/bbqs
https://www.thegoodguys.com.au/deals/bundle
https://www.thegoodguys.com.au/deals/coffee-machines
https://www.thegoodguys.com.au/deals/cooking
https://www.thegoodguys.com.au/deals/dishwashers
https://www.thegoodguys.com.au/deals/dryers
https://www.thegoodguys.com.au/deals/fridge-and-laundry
https://www.thegoodguys.com.au/deals/fridges
https://www.thegoodguys.com.au/deals/health-fitness-beauty
https://www.thegoodguys.com.au/deals/headphones-and-soundbars
https://www.thegoodguys.com.au/deals/heaters
https://www.thegoodguys.com.au/deals/kitchen
https://www.thegoodguys.com.au/deals/kitchen-appliances
https://www.thegoodguys.com.au/deals/kitchenware-sinks-and-taps
https://www.thegoodguys.com.au/deals/laptops
https://www.thegoodguys.com.au/deals/microwaves
https://www.thegoodguys.com.au/deals/phone-and-smart-watches
https://www.thegoodguys.com.au/deals/smart-home
https://www.thegoodguys.com.au/deals/technology
https://www.thegoodguys.com.au/deals/tvs
https://www.thegoodguys.com.au/deals/vacuums-and-cleaning
https://www.thegoodguys.com.au/deals/washing-machines

---

### 2. **Claude** — 2026-04-22T03:46

Let me read both CSV files to understand what data is available.
```
This block is not supported on your current device yet.
```

Let me read both CSV files.
```
This block is not supported on your current device yet.
```

Now I understand the data structure. Let me load both CSVs fully to find sale/discount-related prompts and then match them to the given URLs.

The profound data has: prompt, topic, tags, mentions, normalized_mentions, position, mentioned?, platform, date, etc.
The fanout data has: prompt, query_count, fanout_query, fanout_count, fanout_share, etc.

I need to:
1. Find prompts in the profound data that are about sales, offers, discounts
2. Get their last 28 days data (visibility metrics)


3. Cross-reference their query fanouts from the fanout file
4. Map them to the given URLs

Let me load all unique prompts from both files and filter for sale/discount-related ones.
```
This block is not supported on your current device yet.
```

Now let me identify sale/discount/offer-related prompts from this list, then get their metrics and fanout data.

Sale/discount/offer-related prompts:
1. "Best deals on the latest LG OLED models"
2. "Best deals on upright freezers this week"
3. "Clearance specials on rangehoods"
4. "Cordless stick vacuums on sale in Australia"
5. "Current sales on Samsung televisions this month"
6. "Deals on pyrolytic ovens in Australia"
7. "Dyson vacuum deals with bonus accessories"


8. "Front-load washing machines for sale in Australia"
9. "Heat pump dryers available on sale"
10. "Induction cooktops on sale this month"
11. "Oven and cooktop package deals in stock"
12. "Retailers offering energy-efficient fridges on sale"
13. "Sales on Bosch dishwashers right now"
14. "Side-by-side fridge specials with ice makers"
15. "Stainless steel dishwasher specials near me"
16. "Stores with budget TVs under $500"
17. "TV deals available for same-day pickup"
18. "What are the best-value..." and continuing through the rest of the sale-related queries.

I'm seeing a lot of queries focused on specific product categories with price points and availability, then moving into "best-value" and "affordable" searches. I should prioritize the direct sale and discount queries, then cross-reference the "best-value" and "affordable" ones against the provided URLs to see which are most relevant.

Now I'm looking at the deals URLs available—there's a comprehensive list covering everything from air conditioners to washing machines, plus a general EOFY sale page. I need to match the sale-specific search prompts to these deal categories to identify which queries align with the actual inventory and promotions available.

The profound data only covers a week (April 14-20, 2026) rather than the full 28 days I'd ideally want, so I'll work with what's available and compute metrics per prompt using the mentioned status, ranking positions, and brand mentions from that dataset. Then I'll cross-reference with the fanout data to see how these prompts are performing across different query variations.

Looking at the metrics I have access to—whether a prompt was mentioned, its position, the brands cited, and normalized mention counts—I don't see a direct visibility share or citation rate metric, so I'll need to derive those from the available data points.
```
This block is not supported on your current device yet.
```

Now I need to:
1. Compute visibility/mention metrics per prompt from profound data
2. Get fanout data per prompt
3. Map to the given URLs

Let me compute mention rate, avg position for each sale prompt, then join with fanout data.

The question asks for "last 28 days" but data is only April 14-20 (7 days). I'll use all available data.

Let me now categorize these prompts against the given URLs, compute metrics, and get fanout data.
```
This block is not supported on your current device yet.
```

Now I have all the data I need. Let me now create the final output mapping each prompt to the relevant URL(s) and showing the key metrics.

Let me now build the URL-to-prompt mapping and present it clearly.

URL categories:
- /eofy-sale - general sale, could apply to everything but especially TVs, fridges, appliances
- /deals/air-conditioners-and-fans - air conditioners, fans
- /deals/bbqs - BBQs (no direct prompts about BBQs)
- /deals/bundle - bundle deals, package deals


- /deals/coffee-machines - coffee machines
- /deals/cooking - cooking (ovens, cooktops, etc.)
- /deals/dishwashers - dishwashers
- /deals/dryers - dryers
- /deals/fridge-and-laundry - fridges + washing machines
- /deals/fridges - fridges
- /deals/health-fitness-beauty - health, fitness, beauty (shavers, hair dryers, hair straighteners, fitness trackers)
- /deals/headphones-and-soundbars - headphones, soundbars
- /deals/heaters - heaters
- /deals/kitchen - kitchen appliances (mixers, blenders, kettles, toasters, etc.)
- /deals/kitchen-appliances - kitchen appliances
- /deals/kitchenware-sinks-and-taps - kitchenware (less direct)
- /deals/laptops - laptops, tablets
- /deals/microwaves - microwaves
- /deals/phone-and-smart-watches - phones, smart watches
- /deals/smart-home - smart home (robot vacuums, smart watches?)
- /deals/technology - technology (general)
- /deals/tvs - TVs
- /deals/vacuums-and-cleaning - vacuums
- /deals/washing-machines - washing machines

Now I'm mapping the most commercially relevant prompts with high mention rates to these URLs, focusing on transactional queries rather than trying to cover all 86 possibilities. I'll create a focused table showing each URL with its best matching prompts and their mention rates.

I'm filtering out the low-performing "best-value" informational prompts and concentrating on the ones that actually drive deals traffic: explicit sale-related queries like "for sale," "deals," "on sale," and "clearance," plus the "where can I buy affordable" prompts and price-point searches. I'll organize this by URL with the matched prompts, their mention rates, and the top fanout queries so it's actually useful.Now I have everything. Let me compile the mapping.
```
This block is not supported on your current device yet.
```

I have all the data. Now let me present this in a clean, structured table format that's easy to use. I'll present it by URL with the most relevant prompts (filtering to keep it readable - I'll exclude the "best-value" prompts where TGG mention rate is very low, unless it's the only relevant prompt for that URL).

The data note: profound data covers April 14-20 (7 days), not 28 days. The fanout data is a point-in-time snapshot. I should note this.

Also note: /deals/dryers has "Where can I buy affordable hair dryers for home use?" matched - that's a false match. "Hair dryers" matched "dryers". 

I need to filter out these false positives - hair dryers aren't clothes dryers, and dishwashers aren't washing machines - then create a clean table with only the relevant prompts for each URL. I'm noticing some inconsistencies in the URL mappings—like headphones being categorized under phone-and-smart-watches when they don't quite fit, and smart watches under smart-home which feels like a stretch. For the EOFY sale, I'll note that it's broad enough to cover most sale and affordability prompts, then focus on highlighting the top performers in a clean markdown table format that shows each URL with its relevant prompts and metrics clearly.

I should also flag that the Profound data only spans April 14-20, which is just a week rather than the full 28-day window, so that limitation needs to be visible in the output.Now I'll format this into a clean reference doc.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

A few things worth flagging:

**Data coverage:** The Profound export only runs April 14–20 (7 days), not 28. If you have a fuller export, the mention rates will be more stable.

**Two URLs with zero coverage:** /deals/bbqs and /deals/kitchenware-sinks-and-taps have no matching prompts at all. BBQs aren't in the Profound prompt set.

**Pattern worth noting:** The "What are the best-value X" prompts are consistently weak for TGG. Most are under 15% mention rate, several near 0%. The transactional prompts ("X on sale in Australia", "cheapest store for X", "affordable X where to buy") are where TGG actually gets cited. That's the AEO content angle worth prioritising on these deals pages.

**Standout performers for EOFY specifically:** Pyrolytic ovens (91.5%), cordless stick vacuums (83%), OLED TVs (85.4%), front-load washing machines (77.1%) and energy-efficient fridges (72.3%) are all strong. Those are the categories where TGG is already being recommended in AI responses when people are searching with deal/sale intent.
 
Now I have everything. Let me compile the mapping.
Now I'll format this into a clean reference doc.
A few things worth flagging:

**Data coverage:** The Profound export only runs April 14–20 (7 days), not 28. If you have a fuller export, the mention rates will be more stable.

**Two URLs with zero coverage:** /deals/bbqs and /deals/kitchenware-sinks-and-taps have no matching prompts at all. BBQs aren't in the Profound prompt set.

**Pattern worth noting:** The "What are the best-value X" prompts are consistently weak for TGG. Most are under 15% mention rate, several near 0%. The transactional prompts ("X on sale in Australia", "cheapest store for X", "affordable X where to buy") are where TGG actually gets cited. That's the AEO content angle worth prioritising on these deals pages.

**Standout performers for EOFY specifically:** Pyrolytic ovens (91.5%), cordless stick vacuums (83%), OLED TVs (85.4%), front-load washing machines (77.1%) and energy-efficient fridges (72.3%) are all strong. Those are the categories where TGG is already being recommended in AI responses when people are searching with deal/sale intent.

---

### 3. **Human** — 2026-04-22T03:53

as a sheet
as a sheet

---

### 4. **Claude** — 2026-04-22T03:54

The user wants this as a spreadsheet (.xlsx file).
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

One sheet, columns: URL, Prompt, Total Runs, TGG Mentions, TGG Mention %, then Fanout Query/Count for the top 3 fanout queries. Mention % cells are colour-coded green (60%+), amber (30–59%), red (<30%). Rows are banded by URL group, sortable via auto-filter.
 
One sheet, columns: URL, Prompt, Total Runs, TGG Mentions, TGG Mention %, then Fanout Query/Count for the top 3 fanout queries. Mention % cells are colour-coded green (60%+), amber (30–59%), red (<30%). Rows are banded by URL group, sortable via auto-filter.

---

### 5. **Human** — 2026-04-22T03:57

this isnt goood format - it should be all prompts about deals, savings, offers, eofy etc. categorised, then each fanout under each prompt, several rows
this isnt goood format - it should be all prompts about deals, savings, offers, eofy etc. categorised, then each fanout under each prompt, several rows

---

### 6. **Claude** — 2026-04-22T03:59

The user wants a different format - not URL-centric, but prompt-centric. Each prompt gets its own section, with each fanout query on a separate row beneath it. So the structure should be:

Category | Prompt | Fanout Query | Fanout Count | TGG Mention % | TGG Mentions | Total Runs

With the prompt repeated for each fanout row, or merged. Let me think about what "categorised" means - probably by topic category (TVs, Fridges, Vacuums, etc.) rather than by URL.

So the format would be something like:
- Category (e.g. TVs, Fridges, Washing Machines, Vacuums, etc.)


- Prompt (the Profound prompt)
- TGG Mention %
- TGG Mentions
- Total Runs
- Fanout Query (one per row)
- Fanout Count

Each prompt has multiple fanout rows. So if a prompt has 3 fanout queries, it takes 3 rows, with the prompt/metrics info in the first row (or repeated). Let me organize this by product category, with each prompt showing its associated fanout queries and metrics stacked vertically. I'm continuing to map out appliance categories—now looking at dishwashers, vacuums, and cooking appliances with similar search queries around affordability, availability, and specific features like cordless options, energy efficiency, and package deals. I'm continuing to map out product categories and where people can find affordable options—moving through climate control, electronics, and personal care items. I'm also noting that I should think about best-value recommendations across these various categories, though I'm reconsidering how to organize this.

Now I'm refining the category structure to better match the deals pages themselves. I'm looking at a cleaner list of sixteen main categories like TVs, major appliances, climate control, electronics, and smart home products. For each category, I'd track the prompt, mention percentages, total runs, and the fanout queries that branch from it—capturing all variations rather than just the top few.
```
This block is not supported on your current device yet.
```

OK, so there are 19,960 fanout rows across 86 prompts. That's way too many to put in a sheet (183 per prompt on average). I should limit to top 5 or top 10 fanout queries per prompt. Let me do top 5.

The structure the user wants:
- Category (e.g. TVs, Fridges, etc.)
- Prompt
- TGG Mention %
- TGG Mentions
- Total Runs
- Fanout Query
- Fanout Count

With each fanout on its own row. 

Limiting to the top 5 fanout queries per prompt brings this down to around 430 rows, which is much more workable. I'll repeat the prompt details across all its fanout rows for better filtering. Now I need to manually map each prompt to its appropriate category.19k rows total — I'll cap at top 5 fanout queries per prompt (manageable, still useful).
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

436 rows. Structure: blue category header rows (TVs & AV, Fridges, Vacuums, etc.), then each prompt with its mention %, mention count, and total runs on the first row, followed by the top 5 fanout queries as sub-rows beneath it. Mention % cells are green/amber/red. Prompts sorted highest mention rate first within each category.
 
19k rows total — I'll cap at top 5 fanout queries per prompt (manageable, still useful).
436 rows. Structure: blue category header rows (TVs & AV, Fridges, Vacuums, etc.), then each prompt with its mention %, mention count, and total runs on the first row, followed by the top 5 fanout queries as sub-rows beneath it. Mention % cells are green/amber/red. Prompts sorted highest mention rate first within each category.

---

### 7. **Human** — 2026-04-22T04:00

i need one tab all prompts and the stats, then another with fanout breakdown per prompt, simple style, no heavy formatting or thick rows.
i need one tab all prompts and the stats, then another with fanout breakdown per prompt, simple style, no heavy formatting or thick rows.

---

### 8. **Claude** — 2026-04-22T04:01

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Two tabs:

**Prompts** — 86 rows, one per prompt. Columns: Category, Prompt, TGG Mention %, TGG Mentions, Total Runs. Sorted highest mention rate first. Filterable.

**Fanout Breakdown** — 430 rows. Same Category, Prompt, TGG Mention % repeated per row, then Fanout Query and Fanout Count. Top 5 fanouts per prompt, grouped by category. Filterable by any column.

Mention % cells are green/amber/red, everything else plain.
 
Two tabs:

**Prompts** — 86 rows, one per prompt. Columns: Category, Prompt, TGG Mention %, TGG Mentions, Total Runs. Sorted highest mention rate first. Filterable.

**Fanout Breakdown** — 430 rows. Same Category, Prompt, TGG Mention % repeated per row, then Fanout Query and Fanout Count. Top 5 fanouts per prompt, grouped by category. Filterable by any column.

Mention % cells are green/amber/red, everything else plain.
