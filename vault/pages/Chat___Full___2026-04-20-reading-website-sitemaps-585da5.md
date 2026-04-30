---
title: Reading website sitemaps (full)
parent: Chat/Light/2026-04-20-reading-website-sitemaps-585da5
uuid: 585da513-8328-4d75-b1b6-23000a0efb19
---

#chat/full #project/eofy #status/completed

# Reading website sitemaps — Full Transcript

→ Light view: [[Chat/Light/2026-04-20-reading-website-sitemaps-585da5]]
→ Medium view: [[Chat/Medium/2026-04-20-reading-website-sitemaps-585da5]]

**Messages:** 16 | **Date:** 2026-04-20

---

### 1. **Human** — 2026-04-20T05:31

can you read sitemaps?https://www.thegoodguys.com.au/sitemap.xml
can you read sitemaps?https://www.thegoodguys.com.au/sitemap.xml

---

### 2. **Claude** — 2026-04-20T05:31

Let me fetch the sitemap.
```
This block is not supported on your current device yet.
```

Binary data returned. Let me try bash_tool with curl.
```
This block is not supported on your current device yet.
```

Yes, I can read it via curl. The sitemap index has 9 child sitemaps.Yes. The `web_fetch` tool returns binary for XML, but `curl` via bash works fine.

The sitemap index at `https://www.thegoodguys.com.au/sitemap.xml` contains 9 child sitemaps (all on `sitemap.thegoodguys.com.au`, last modified today):

| Sitemap | Type |
|---|---|
| product_sitemap_1–4 | Products (4 files) |
| brand_sitemap_1 | Brand pages |
| category_sitemap_1 | Category/PLP pages |
| content_sitemap_1 | Content pages |
| article_sitemap_1 | Blog/articles |
| storelocation_sitemap_1 | Store locations |

What do you need from them?
 
Yes. The `web_fetch` tool returns binary for XML, but `curl` via bash works fine.

The sitemap index at `https://www.thegoodguys.com.au/sitemap.xml` contains 9 child sitemaps (all on `sitemap.thegoodguys.com.au`, last modified today):

| Sitemap | Type |
|---|---|
| product_sitemap_1–4 | Products (4 files) |
| brand_sitemap_1 | Brand pages |
| category_sitemap_1 | Category/PLP pages |
| content_sitemap_1 | Content pages |
| article_sitemap_1 | Blog/articles |
| storelocation_sitemap_1 | Store locations |

What do you need from them?

---

### 3. **Human** — 2026-04-20T05:32

any content around EOFY, blogs, guides, anything
any content around EOFY, blogs, guides, anything

---

### 4. **Claude** — 2026-04-20T05:33

Let me fetch the content and article sitemaps to find EOFY-related content.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good. Let me also check the category sitemap for any EOFY category pages.
```
This block is not supported on your current device yet.
```

Here's everything EOFY-indexed across sitemaps:

**Content (1)**
- https://www.thegoodguys.com.au/eofy-sale

**Articles/Blog (5)**
- https://www.thegoodguys.com.au/whats-new/eofy-deals
- https://www.thegoodguys.com.au/whats-new/guide-to-eofy-tv-deals
- https://www.thegoodguys.com.au/whats-new/best-tech-buys-for-eofy
- https://www.thegoodguys.com.au/whats-new/eofy-most-popular-home-appliances
- https://www.thegoodguys.com.au/whats-new/eofy-sales-tips-for-university-students

**Category (0)** — nothing in the category sitemap.

No tax-time or financial-year variants showing. Want me to pull the live content from any of these, or check status codes first?
 
Here's everything EOFY-indexed across sitemaps:

**Content (1)**
- https://www.thegoodguys.com.au/eofy-sale

**Articles/Blog (5)**
- https://www.thegoodguys.com.au/whats-new/eofy-deals
- https://www.thegoodguys.com.au/whats-new/guide-to-eofy-tv-deals
- https://www.thegoodguys.com.au/whats-new/best-tech-buys-for-eofy
- https://www.thegoodguys.com.au/whats-new/eofy-most-popular-home-appliances
- https://www.thegoodguys.com.au/whats-new/eofy-sales-tips-for-university-students

**Category (0)** — nothing in the category sitemap.

No tax-time or financial-year variants showing. Want me to pull the live content from any of these, or check status codes first?

---

### 5. **Human** — 2026-04-20T05:36

use semrush skill to identify potential blog topics from core competitors - topic gaps
use semrush skill to identify potential blog topics from core competitors - topic gaps

---

### 6. **Claude** — 2026-04-20T05:41

Simon wants me to use the Semrush MCP to identify blog topic gaps for EOFY content by analyzing core competitors. Let me first use the tool_search to load the Semrush tools, then identify competitors and find topic gaps.

Core TGG competitors for electronics/appliances in AU would be: JB Hi-Fi, Harvey Norman, Appliances Online, Bing Lee, Officeworks.

Let me search for the Semrush tools first.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


I'll use the `domain_domains` report for keyword gap analysis between TGG and competitors. Let me first get the schema for this report, then also I should check competitors first using `domain_organic_organic` to confirm who the main competitors are. Let me use JB Hi-Fi, Harvey Norman, Appliances Online as the main competitors since those are well known.

Actually let me get the schema for `domain_domains` first.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


Now I'll run the keyword gap report. I want to find keywords that competitors rank for but TGG doesn't, specifically around EOFY blog/guide content. I'll use the "untapped" format:

`*|or|jbhifi.com.au|+|or|harveynorman.com.au|+|or|appliancesonline.com.au|-|or|thegoodguys.com.au`

This will show keywords that competitors rank for but TGG doesn't. I'll filter for EOFY-related keywords.

Actually, I need to think about this differently. The domain_domains report shows keyword-level gap data. 

I'm deciding between looking at competitor blog subfolders directly for EOFY content or running a keyword gap report filtered for EOFY terms. The keyword gap approach would be more efficient—it'll show me exactly which EOFY-related keywords competitors are ranking for that TGG is missing.

I'll apply a filter to include only keywords containing "eofy" and run the report.
```
This block is not supported on your current device yet.
```


Looking at this data, most of the "untapped" keywords for TGG are things like clothing, furniture, mattresses, cars, wine. These are not relevant to TGG's product range. However, let me look at what IS relevant:

- "eofy pcs" - 140 searches, KD 9, JB Hi-Fi ranks 1st
- "eofy meaning" - 1600 searches, KD 19 - Harvey Norman/JB HiFi ranking
- "officeworks eofy" - branded, not relevant
- "eofy sale 2024" - stale


The relevant ones for TGG are pretty limited from this set. I should try a broader approach and run keyword research specifically for EOFY-related terms in the electronics and appliances space where TGG actually competes.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


Now let me also look at questions-based keywords for EOFY content in the electronics/appliances space, and also look at what competitor subfolders have for EOFY content.

Let me also get the phrases_questions for EOFY to identify blog topic opportunities.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


The tax-related results are too generic (ATO, tax return, etc.) - not relevant to TGG's product EOFY content.

Now let me look at what competitor blog content is driving EOFY traffic that TGG doesn't have. I'll use subfolder_research on JB Hi-Fi and Harvey Norman blog sections.Now let me check what competitors are actually ranking for in their blog/guide sections.
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


Now let me look at what JB Hi-Fi blog content is ranking for EOFY specifically and what TGG's blog section is ranking for to confirm the gaps.

I already have enough data. Let me also quickly check Officeworks blog/guide content since they came up in the keyword data.

Actually, I have enough data. Let me also check what keywords TGG's /whats-new/ section is already ranking for with EOFY to understand the current baseline.Now let me check TGG's current EOFY ranking baseline in /whats-new/.
```
This block is not supported on your current device yet.
```

---

**TGG's EOFY blog baseline.** 5 articles in /whats-new/ covering: EOFY deals (generic), TV guide, best tech buys, popular appliances, university students. All are ranking, some competitively (position 2–16 for "good guys eofy sale," "eofy fridge sales," "eofy tv sales").

**Topic gaps. These have search volume, competitors rank for them, TGG has nothing:**

| Topic | Volume | KD | Who covers it |
|---|---|---|---|
| EOFY laptop buying guide | 260–390 | 28–36 | JB Hi-Fi (office tech refresh guide) |
| EOFY sale dates / when does it end | 260–720 | 22–38 | Harvey Norman (/eofy-sale page, not editorial) |
| Best EOFY sales / where to shop | 480 | 26 | Harvey Norman |
| EOFY TV deals guide | 880 | 28 | Partial (TGG has one, ranking 8) |
| EOFY fridge/appliance buying guide | 110–210 | 10 | Gap, TGG only has a list post |
| EOFY meaning / what is EOFY | 1,600 | 19 | JB Hi-Fi, Harvey Norman, not TGG |
| EOFY home office tech refresh | ~170 | 28 | JB Hi-Fi specifically |
| Tax return spending guide (what to buy) | 50–210 | low | TGG has /whats-new/maximise-your-tax-return (low pos) |

**Highest-priority gaps for TGG editorial:**

1. **"What is EOFY / EOFY meaning"** (1,600 vol, KD 19). Pure informational, low difficulty, neither competitor owns it editorially. Good hook for an explainer that funnels into TGG's sale page.
2. **"When do EOFY sales start / end"** (260–720 vol, KD 22–38). Harvey Norman's sale page captures this by accident. A dedicated editorial answer would rank better.
3. **EOFY laptop buying guide** (combined cluster ~650 vol). JB Hi-Fi's office tech refresh angle is their only coverage. A proper "best laptops to buy at EOFY" guide is unclaimed.
4. **EOFY fridge and appliance buying guide** (cluster ~300 vol, KD 10). TGG ranks for "eofy fridge sales" at position 16 off a list post. A dedicated guide would be defensible and on-brand.
5. **EOFY home office tech refresh** (JB Hi-Fi's exact angle). A TGG version covering monitors, laptops, chairs (where stocked), printers covers similar intent with less overlap.

Want me to build a content brief for any of these, or export this as a structured brief doc?
 
Now let me check what competitors are actually ranking for in their blog/guide sections.
Now let me check TGG's current EOFY ranking baseline in /whats-new/.
---

**TGG's EOFY blog baseline.** 5 articles in /whats-new/ covering: EOFY deals (generic), TV guide, best tech buys, popular appliances, university students. All are ranking, some competitively (position 2–16 for "good guys eofy sale," "eofy fridge sales," "eofy tv sales").

**Topic gaps. These have search volume, competitors rank for them, TGG has nothing:**

| Topic | Volume | KD | Who covers it |
|---|---|---|---|
| EOFY laptop buying guide | 260–390 | 28–36 | JB Hi-Fi (office tech refresh guide) |
| EOFY sale dates / when does it end | 260–720 | 22–38 | Harvey Norman (/eofy-sale page, not editorial) |
| Best EOFY sales / where to shop | 480 | 26 | Harvey Norman |
| EOFY TV deals guide | 880 | 28 | Partial (TGG has one, ranking 8) |
| EOFY fridge/appliance buying guide | 110–210 | 10 | Gap, TGG only has a list post |
| EOFY meaning / what is EOFY | 1,600 | 19 | JB Hi-Fi, Harvey Norman, not TGG |
| EOFY home office tech refresh | ~170 | 28 | JB Hi-Fi specifically |
| Tax return spending guide (what to buy) | 50–210 | low | TGG has /whats-new/maximise-your-tax-return (low pos) |

**Highest-priority gaps for TGG editorial:**

1. **"What is EOFY / EOFY meaning"** (1,600 vol, KD 19). Pure informational, low difficulty, neither competitor owns it editorially. Good hook for an explainer that funnels into TGG's sale page.
2. **"When do EOFY sales start / end"** (260–720 vol, KD 22–38). Harvey Norman's sale page captures this by accident. A dedicated editorial answer would rank better.
3. **EOFY laptop buying guide** (combined cluster ~650 vol). JB Hi-Fi's office tech refresh angle is their only coverage. A proper "best laptops to buy at EOFY" guide is unclaimed.
4. **EOFY fridge and appliance buying guide** (cluster ~300 vol, KD 10). TGG ranks for "eofy fridge sales" at position 16 off a list post. A dedicated guide would be defensible and on-brand.
5. **EOFY home office tech refresh** (JB Hi-Fi's exact angle). A TGG version covering monitors, laptops, chairs (where stocked), printers covers similar intent with less overlap.

Want me to build a content brief for any of these, or export this as a structured brief doc?

---

### 7. **Human** — 2026-04-20T05:41

Continue
Continue

---

### 8. **Claude** — 2026-04-20T05:42

Simon said "Continue" - he wants me to keep going with the topic gap analysis. Let me think about what's left to do. I've covered the main gaps. Let me dig deeper into a few more areas:

1. Check what keywords are driving traffic to JB Hi-Fi's office tech EOFY article specifically
2. Look at category-specific EOFY clusters - washing machines, dishwashers, air conditioners (seasonal)
3. Check Officeworks blog since they ranked for "officeworks eofy" (110 vol)
4. Maybe look at the whats-new subfolder more broadly to see TGG's full blog EOFY footprint vs competitors


5. Now I'm diving into JB Hi-Fi's specific EOFY article to see what keywords are actually pulling traffic there, and examining how category-specific EOFY terms cluster across different product types.
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


Now I have a comprehensive picture. Let me compile this into a clear, prioritized topic gap analysis for blog content. Let me organize the findings:

**Confirmed gaps - high value:**

1. "What is EOFY / EOFY meaning" - 1,600 vol, KD 19. Nobody owns this editorially in the electronics space. Harvey Norman's sale page accidentally ranks. An actual explainer page at /whats-new/ would likely outrank it.

2. "When do EOFY sales start/end" cluster - 720+260+320+390 = ~1,700 vol combined, KD 22-40. 

Again only Harvey Norman's sale page dominates with no real editorial content competing.

3. "Best EOFY deals / best EOFY buys" - 110-480 vol, KD 10-32. TGG has /whats-new/eofy-deals but it ranks 42 for "eofy deals". Better structured content could do more.

4. "EOFY laptop sale" cluster - 260+210+140+140+110+50 = ~910 vol combined, KD 28-36. No dedicated buyer's guide from TGG. JB Hi-Fi's only coverage is a weak office tech refresh piece

.

5. "EOFY washing machine sale" - 90 vol, KD 31. TGG has this buried in /whats-new/eofy-most-popular-home-appliances rather than as a standalone guide.

6. "EOFY apple / EOFY iphone" - 90+50+140 = ~280 vol combined, and nobody's really targeting this specifically.

7. "What can I claim on tax Australia" - 170 vol, KD 32. This sits adjacent to EOFY buying intent and could work as a tax deductible purchases guide.

8. "EOFY sale meaning" - 110 vol, KD 19. Should merge with the "what is EOFY" topic.

9. "EOFY TV deals/guide" - TGG partially covers this and ranks 8 for "tv deals eofy".

There's room to optimize what's already out there. "Best EOFY sales" is a big one at 480 vol with KD 26 - Harvey Norman owns this space right now, but TGG could capture it with a comprehensive editorial guide. I should exclude furniture, mattresses, clothing, and cars since they're outside TGG's scope, and skip anything too generic like ATO or tax returns. Now I'm ready to pull together the final recommendations.Now I have the full picture. Here's the complete topic gap analysis:

---

## EOFY Blog Topic Gaps. TGG vs Competitors

### What TGG already has (baseline)
5 articles: generic EOFY deals, TV guide, best tech buys, popular appliances, university students. Strongest rankings: "good guys eofy sale" (pos 2–3), "eofy fridge sales" (pos 16), "eofy tv sales" (pos 13).

---

### Confirmed gaps, prioritised

**Tier 1. High volume, low-to-mid KD, no editorial owner**

| Topic | Keyword cluster | Combined vol | KD | Competitor coverage |
|---|---|---|---|---|
| What is EOFY / EOFY meaning | eofy meaning, what is eofy, eofy sale meaning | ~2,040 | 10–19 | HN sale page (accidental), no editorial |
| When do EOFY sales start/end | when do eofy sales start, when does eofy end, eofy sale dates, eofy date | ~1,560 | 22–38 | HN sale page only, no guide |
| Best EOFY deals / best buys | best eofy deals, best eofy sales, best things to buy at eofy | ~730 | 10–32 | HN sale page, TGG has weak list post (pos 42) |

**Tier 2. Category-specific guides, unclaimed**

| Topic | Keyword cluster | Combined vol | KD | Notes |
|---|---|---|---|---|
| EOFY laptop buying guide | eofy laptop sale/sales/deals, laptop eofy sale, eofy pcs | ~910 | 9–36 | JB Hi-Fi office tech piece is weak (pos 26 for "office tech"). No proper buyer's guide exists. |
| EOFY Apple / iPhone deals | eofy apple, eofy iphone, apple eofy | ~380 | 20–48 | Nobody owns this editorially. High commercial intent. |
| EOFY washing machine / appliance guide | eofy washing machine sale, eofy fridge, eofy vacuum, eofy robot vacuum | ~240 | 0–31 | TGG's appliances list post doesn't go deep enough on any one category. |
| EOFY home office setup | eofy home office, work from home tax deductions australia, what can i claim on tax australia | ~240 | 26–32 | JB Hi-Fi has one thin piece. Tax deductible angle (monitors, laptops, headsets) is genuinely useful and untapped. |

**Tier 3. Lower volume, but TGG-specific brand intent**

| Topic | Vol | KD | Notes |
|---|---|---|---|
| EOFY TV deals guide (refresh) | 880 | 0–28 | TGG ranks 8 already. Update and expand rather than new article. |
| EOFY Dyson / vacuum deals | ~140 | 0–32 | Small but high commercial intent. Could be a hub or FAQ block rather than a full article. |

---

### Topics to skip
Furniture, mattresses, clothing, cars. Appear in the keyword gap data because Harvey Norman's breadth inflates the competitive set. Not TGG categories.

"Tax return" as a standalone topic (9,900+ vol). Way too generic, dominated by ATO and financial content. The angle only works when framed as "what to spend your tax return on" feeding into product categories, which TGG already has a weak article for.

---

### Recommended build order

1. **"What is EOFY and when does it start?"** (combines the two Tier 1 informational clusters into one evergreen explainer). Anchors to the /eofy-sale page. Low KD, nobody owns it editorially.
2. **EOFY laptop buying guide** (highest commercial intent gap in TGG's core category range).
3. **EOFY home office tech guide** with a tax deductible angle (differentiates from JB Hi-Fi's version, seasonally relevant before 30 June).
4. **EOFY Apple deals guide** (brand-specific, high intent, unclaimed).
5. **Refresh existing TV article** rather than a new one.

Want content briefs for any of these, or should I pull SERP composition data on the top one or two to inform structure?
 
Now I have the full picture. Here's the complete topic gap analysis:

---

## EOFY Blog Topic Gaps. TGG vs Competitors

### What TGG already has (baseline)
5 articles: generic EOFY deals, TV guide, best tech buys, popular appliances, university students. Strongest rankings: "good guys eofy sale" (pos 2–3), "eofy fridge sales" (pos 16), "eofy tv sales" (pos 13).

---

### Confirmed gaps, prioritised

**Tier 1. High volume, low-to-mid KD, no editorial owner**

| Topic | Keyword cluster | Combined vol | KD | Competitor coverage |
|---|---|---|---|---|
| What is EOFY / EOFY meaning | eofy meaning, what is eofy, eofy sale meaning | ~2,040 | 10–19 | HN sale page (accidental), no editorial |
| When do EOFY sales start/end | when do eofy sales start, when does eofy end, eofy sale dates, eofy date | ~1,560 | 22–38 | HN sale page only, no guide |
| Best EOFY deals / best buys | best eofy deals, best eofy sales, best things to buy at eofy | ~730 | 10–32 | HN sale page, TGG has weak list post (pos 42) |

**Tier 2. Category-specific guides, unclaimed**

| Topic | Keyword cluster | Combined vol | KD | Notes |
|---|---|---|---|---|
| EOFY laptop buying guide | eofy laptop sale/sales/deals, laptop eofy sale, eofy pcs | ~910 | 9–36 | JB Hi-Fi office tech piece is weak (pos 26 for "office tech"). No proper buyer's guide exists. |
| EOFY Apple / iPhone deals | eofy apple, eofy iphone, apple eofy | ~380 | 20–48 | Nobody owns this editorially. High commercial intent. |
| EOFY washing machine / appliance guide | eofy washing machine sale, eofy fridge, eofy vacuum, eofy robot vacuum | ~240 | 0–31 | TGG's appliances list post doesn't go deep enough on any one category. |
| EOFY home office setup | eofy home office, work from home tax deductions australia, what can i claim on tax australia | ~240 | 26–32 | JB Hi-Fi has one thin piece. Tax deductible angle (monitors, laptops, headsets) is genuinely useful and untapped. |

**Tier 3. Lower volume, but TGG-specific brand intent**

| Topic | Vol | KD | Notes |
|---|---|---|---|
| EOFY TV deals guide (refresh) | 880 | 0–28 | TGG ranks 8 already. Update and expand rather than new article. |
| EOFY Dyson / vacuum deals | ~140 | 0–32 | Small but high commercial intent. Could be a hub or FAQ block rather than a full article. |

---

### Topics to skip
Furniture, mattresses, clothing, cars. Appear in the keyword gap data because Harvey Norman's breadth inflates the competitive set. Not TGG categories.

"Tax return" as a standalone topic (9,900+ vol). Way too generic, dominated by ATO and financial content. The angle only works when framed as "what to spend your tax return on" feeding into product categories, which TGG already has a weak article for.

---

### Recommended build order

1. **"What is EOFY and when does it start?"** (combines the two Tier 1 informational clusters into one evergreen explainer). Anchors to the /eofy-sale page. Low KD, nobody owns it editorially.
2. **EOFY laptop buying guide** (highest commercial intent gap in TGG's core category range).
3. **EOFY home office tech guide** with a tax deductible angle (differentiates from JB Hi-Fi's version, seasonally relevant before 30 June).
4. **EOFY Apple deals guide** (brand-specific, high intent, unclaimed).
5. **Refresh existing TV article** rather than a new one.

Want content briefs for any of these, or should I pull SERP composition data on the top one or two to inform structure?

---

### 9. **Human** — 2026-04-20T05:43

go to each competitors robots.txt, find their sitemaps, find all their eofy content,

JB HIFI 
HARVEY NORMAN
APPLIANCES ONLINE
OFFICEWORKS
go to each competitors robots.txt, find their sitemaps, find all their eofy content,

JB HIFI 
HARVEY NORMAN
APPLIANCES ONLINE
OFFICEWORKS

---

### 10. **Claude** — 2026-04-20T05:45

Let me fetch robots.txt for each competitor to find their sitemaps, then crawl those sitemaps for EOFY content.
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

Harvey Norman is behind Incapsula (bot protection). Let me try a different approach for HN - use Semrush to find their EOFY URLs instead.

Let me continue with Appliances Online and Officeworks.
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

Harvey Norman is fully behind Incapsula. I'll use Semrush's subfolder_organic to find their EOFY blog/editorial content instead.

For Officeworks, there's no EOFY-specific content in their sitemaps at all, which is itself a finding.

Let me now use Semrush to find Harvey Norman's EOFY editorial content since we can't access their sitemap directly. And also check JB Hi-Fi's blogs sitemap 2 to see all blog content.
```
This block is not supported on your current device yet.
```

Now I have a comprehensive picture. Let me compile findings:

**JB Hi-Fi EOFY content (from sitemaps):**
1. `https://www.jbhifi.com.au/blogs/guides-tips/eofy` - a general EOFY hub/guide page (found in sitemap 2)
2. `https://www.jbhifi.com.au/blogs/guides-tips/refresh-your-essential-office-tech-this-eofy` - office tech refresh guide (found in sitemap 2, confirmed this is in guides-tips not the older URL from blogs)


3. `https://www.jbhifi.com.au/blogs/guides-tips/have-you-got-all-the-right-tech-tools-for-tax-time` - tax time tech tools
4. `https://www.jbhifi.com.au/blogs/tech/aim-to-claim-top-tax-time-tech-tips` - tax time tech tips (in tech section)

I'm also noticing a back-to-school piece that appeared in EOFY-related rankings, which suggests there's some content overlap between seasonal campaigns.

Now looking at the other retailers: Harvey Norman's blocked by Incapsula so I can only rely on Semrush data showing a single `/eofy-sale` page carrying most of the weight with no editorial support. Appliances Online is taking a different approach with heavy reliance on faceted category filter pages and promo hubs rather than blog content, though they do have one tax deduction article. Officeworks doesn't appear to have any EOFY content indexed across their sitemaps.Here's the complete picture across all four competitors.

---

## EOFY Content Audit. Competitor Sitemaps

### JB Hi-Fi

Robots.txt sitemap: `https://www.jbhifi.com.au/sitemap.xml`

**EOFY and tax-time editorial content confirmed in sitemap:**

| URL | Type |
|---|---|
| https://www.jbhifi.com.au/blogs/guides-tips/eofy | Hub/landing page |
| https://www.jbhifi.com.au/blogs/guides-tips/refresh-your-essential-office-tech-this-eofy | Guide |
| https://www.jbhifi.com.au/blogs/guides-tips/have-you-got-all-the-right-tech-tools-for-tax-time | Guide |
| https://www.jbhifi.com.au/blogs/tech/aim-to-claim-top-tax-time-tech-tips | Guide |

Four pieces. JB Hi-Fi has a dedicated EOFY hub page (`/blogs/guides-tips/eofy`) that TGG has no equivalent of, plus two distinct tax-time angles (tools and claims tips) that are separate articles. Their office tech refresh guide covers monitors, laptops, desks, and peripherals together.

---

### Harvey Norman

Robots.txt sitemap: `https://www.harveynorman.com.au/media/sitemap.xml` — **blocked by Incapsula**. Sitemap not accessible from this environment.

Confirmed via Semrush instead: Harvey Norman runs a single `/eofy-sale` commercial page that ranks for nearly every EOFY query through sheer domain authority. No editorial blog content identified in Semrush subfolder data. Their strategy is pure transactional, no guides.

---

### Appliances Online

Robots.txt sitemaps: 9 files. Blog sitemap (`sitemap-blog.xml`) returns empty for EOFY. All EOFY content is structural, not editorial.

**EOFY URLs confirmed:**

*Commercial/promo pages (hub + 17 subcategories):*
- https://www.appliancesonline.com.au/promo/eofy-sale/
- /promo/eofy-sale/refrigeration/
- /promo/eofy-sale/laundry/
- /promo/eofy-sale/dishwashers/
- /promo/eofy-sale/cooking-appliances/
- /promo/eofy-sale/heating-cooling/
- /promo/eofy-sale/small-appliances/
- /promo/eofy-sale/tvs-audio-electronics/
- /promo/eofy-sale/health-beauty-fitness/
- /promo/eofy-sale/outdoor-living/
- /promo/eofy-sale/sinks-and-taps/
- /promo/eofy-sale/furniture-bedding/
- /promo/eofy-sale/bedroom-furniture/
- /promo/eofy-sale/furniture/
- + brand variants: /bosch/, /westinghouse/, /electrolux/, /lg/, /fisher-paykel/, /haier/, /artusi/, /smeg/, /sony/, /ninja/, /shark/, /sunbeam/, /vintec/

*Faceted filter pages (32 indexed):*
- https://www.appliancesonline.com.au/filter/eofy-sale/ (root)
- /filter/eofy-sale/fridges-freezers/
- /filter/eofy-sale/washing-machines/
- /filter/eofy-sale/dishwashers/
- /filter/eofy-sale/ovens-cooking/
- /filter/eofy-sale/tv-audio-electronics/
- /filter/eofy-sale/coffee-machines/
- /filter/eofy-sale/small-appliances/
- /filter/eofy-sale/heating-cooling-/
- + more (dryers, cooktops, BBQ, fitness, home office, furniture, bedding, etc.)
- https://www.appliancesonline.com.au/filter/eofy-supersale/ (separate supersale tier)

*Editorial/content:*
- https://www.appliancesonline.com.au/article/claiming-tax-deduction-on-appliances-for-business/
- https://www.appliancesonline.com.au/brand/instant-tax-write-offs/

**Key observation:** Appliances Online has no EOFY blog content whatsoever. Their entire strategy is faceted navigation and promo pages by category and brand. The one editorial piece targets business tax deductions specifically, not consumer buying guides.

---

### Officeworks

Robots.txt sitemaps: campaigns, content, categories, products, stores.

**EOFY content:** Zero. Nothing in campaigns, content, or categories matches EOFY, end-of-financial-year, or tax-time terms. The only financial-year references are product category pages for physical diaries, planners, and calendars. No editorial EOFY content exists anywhere in their sitemap.

---

## Summary Table

| Competitor | EOFY Hub page | Editorial guides | Tax-time content | Category/filter pages |
|---|---|---|---|---|
| JB Hi-Fi | Yes (`/blogs/guides-tips/eofy`) | 3 guides | 2 articles | No |
| Harvey Norman | Yes (`/eofy-sale`) | None found | No | No |
| Appliances Online | Yes (`/promo/eofy-sale/`) | 0 | 1 (business tax deductions) | 32 faceted + 17 promo subcats |
| Officeworks | No | 0 | No | No |

**The clearest gaps for TGG:**
- JB Hi-Fi is the only competitor with actual editorial EOFY content. Their hub page and four guides are the entire editorial landscape. Three of those four articles are directly replicable with TGG's product range.
- Nobody has a consumer-facing "what appliances can I claim on tax" guide. Appliances Online targets businesses only.
- Officeworks has zero EOFY editorial presence despite EOFY being a major seasonal moment for office/tech purchasing. That's a flanking opportunity for TGG on home office queries.
 
Here's the complete picture across all four competitors.

---

## EOFY Content Audit. Competitor Sitemaps

### JB Hi-Fi

Robots.txt sitemap: `https://www.jbhifi.com.au/sitemap.xml`

**EOFY and tax-time editorial content confirmed in sitemap:**

| URL | Type |
|---|---|
| https://www.jbhifi.com.au/blogs/guides-tips/eofy | Hub/landing page |
| https://www.jbhifi.com.au/blogs/guides-tips/refresh-your-essential-office-tech-this-eofy | Guide |
| https://www.jbhifi.com.au/blogs/guides-tips/have-you-got-all-the-right-tech-tools-for-tax-time | Guide |
| https://www.jbhifi.com.au/blogs/tech/aim-to-claim-top-tax-time-tech-tips | Guide |

Four pieces. JB Hi-Fi has a dedicated EOFY hub page (`/blogs/guides-tips/eofy`) that TGG has no equivalent of, plus two distinct tax-time angles (tools and claims tips) that are separate articles. Their office tech refresh guide covers monitors, laptops, desks, and peripherals together.

---

### Harvey Norman

Robots.txt sitemap: `https://www.harveynorman.com.au/media/sitemap.xml` — **blocked by Incapsula**. Sitemap not accessible from this environment.

Confirmed via Semrush instead: Harvey Norman runs a single `/eofy-sale` commercial page that ranks for nearly every EOFY query through sheer domain authority. No editorial blog content identified in Semrush subfolder data. Their strategy is pure transactional, no guides.

---

### Appliances Online

Robots.txt sitemaps: 9 files. Blog sitemap (`sitemap-blog.xml`) returns empty for EOFY. All EOFY content is structural, not editorial.

**EOFY URLs confirmed:**

*Commercial/promo pages (hub + 17 subcategories):*
- https://www.appliancesonline.com.au/promo/eofy-sale/
- /promo/eofy-sale/refrigeration/
- /promo/eofy-sale/laundry/
- /promo/eofy-sale/dishwashers/
- /promo/eofy-sale/cooking-appliances/
- /promo/eofy-sale/heating-cooling/
- /promo/eofy-sale/small-appliances/
- /promo/eofy-sale/tvs-audio-electronics/
- /promo/eofy-sale/health-beauty-fitness/
- /promo/eofy-sale/outdoor-living/
- /promo/eofy-sale/sinks-and-taps/
- /promo/eofy-sale/furniture-bedding/
- /promo/eofy-sale/bedroom-furniture/
- /promo/eofy-sale/furniture/
- + brand variants: /bosch/, /westinghouse/, /electrolux/, /lg/, /fisher-paykel/, /haier/, /artusi/, /smeg/, /sony/, /ninja/, /shark/, /sunbeam/, /vintec/

*Faceted filter pages (32 indexed):*
- https://www.appliancesonline.com.au/filter/eofy-sale/ (root)
- /filter/eofy-sale/fridges-freezers/
- /filter/eofy-sale/washing-machines/
- /filter/eofy-sale/dishwashers/
- /filter/eofy-sale/ovens-cooking/
- /filter/eofy-sale/tv-audio-electronics/
- /filter/eofy-sale/coffee-machines/
- /filter/eofy-sale/small-appliances/
- /filter/eofy-sale/heating-cooling-/
- + more (dryers, cooktops, BBQ, fitness, home office, furniture, bedding, etc.)
- https://www.appliancesonline.com.au/filter/eofy-supersale/ (separate supersale tier)

*Editorial/content:*
- https://www.appliancesonline.com.au/article/claiming-tax-deduction-on-appliances-for-business/
- https://www.appliancesonline.com.au/brand/instant-tax-write-offs/

**Key observation:** Appliances Online has no EOFY blog content whatsoever. Their entire strategy is faceted navigation and promo pages by category and brand. The one editorial piece targets business tax deductions specifically, not consumer buying guides.

---

### Officeworks

Robots.txt sitemaps: campaigns, content, categories, products, stores.

**EOFY content:** Zero. Nothing in campaigns, content, or categories matches EOFY, end-of-financial-year, or tax-time terms. The only financial-year references are product category pages for physical diaries, planners, and calendars. No editorial EOFY content exists anywhere in their sitemap.

---

## Summary Table

| Competitor | EOFY Hub page | Editorial guides | Tax-time content | Category/filter pages |
|---|---|---|---|---|
| JB Hi-Fi | Yes (`/blogs/guides-tips/eofy`) | 3 guides | 2 articles | No |
| Harvey Norman | Yes (`/eofy-sale`) | None found | No | No |
| Appliances Online | Yes (`/promo/eofy-sale/`) | 0 | 1 (business tax deductions) | 32 faceted + 17 promo subcats |
| Officeworks | No | 0 | No | No |

**The clearest gaps for TGG:**
- JB Hi-Fi is the only competitor with actual editorial EOFY content. Their hub page and four guides are the entire editorial landscape. Three of those four articles are directly replicable with TGG's product range.
- Nobody has a consumer-facing "what appliances can I claim on tax" guide. Appliances Online targets businesses only.
- Officeworks has zero EOFY editorial presence despite EOFY being a major seasonal moment for office/tech purchasing. That's a flanking opportunity for TGG on home office queries.

---

### 11. **Human** — 2026-04-20T05:50

map existing tgg to optimise, new based on gaps.
map existing tgg to optimise, new based on gaps.

---

### 12. **Claude** — 2026-04-20T05:52

Simon wants me to map TGG's existing 5 EOFY articles against optimization opportunities, and recommend new articles based on the gaps identified. Let me compile this into a clear, actionable table/plan.

TGG existing EOFY content:
1. /whats-new/eofy-deals
2. /whats-new/guide-to-eofy-tv-deals
3. /whats-new/best-tech-buys-for-eofy
4. /whats-new/eofy-most-popular-home-appliances


5. /whats-new/eofy-sales-tips-for-university-students

Plus the commercial page and the tax return guide that's ranking well for EOFY sale queries. Now I'm looking at the gaps—there's strong search demand around what EOFY actually means (1,600 volume, KD 19), when the sales run (combined 1,700 volume), and specific buying guides for laptops and Apple products that aren't currently covered.

I'm also seeing opportunities around home office tax deductions and appliance guides, plus JB Hi-Fi's already built out an EOFY hub with office tech refresh and tax tools. Let me organize this into a table that shows what we're currently optimizing and where the new content should go.Let me pull the current rankings data first to baseline each existing article properly.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now I have a clear picture. Let me compile the optimization map and new content plan.

**Existing 5 articles + tax return article:**

1. `/whats-new/eofy-deals` - the generic hub. Ranking for many terms but at poor positions. Scattered coverage.
2. `/whats-new/guide-to-eofy-tv-deals` - performing best: pos 8 "tv deals eofy", pos 10 "eofy tv sale", pos 13 "eofy tv sales", pos 9 "good guys eofy sale", pos 14 "tv eofy sale"


3. `/whats-new/best-tech-buys-for-eofy` - cannibalizing with eofy-deals. Pos 76 "tv deals eofy", pos 32 "eofy laptop deals australia", pos 34 "eofy laptop"
4. `/whats-new/eofy-most-popular-home-appliances` - strongest on appliance-specific terms: pos 2-3 "good guys eofy sale", pos 16 "eofy fridge sales", pos 16 "eofy washing machine sale", pos 80 "dyson eofy"
5. `/whats-new/eofy-sales` - need to check performance on this one
6. `/whats-new/eofy-tips-for-university-students` - pos 13/35 "good guys eofy sale", also competing on laptop cluster
7. `/whats-new/maximise-your-tax-return` - pos 23/35/40/51 "good guys eofy sale" - clearly diluted

The core issue is that `/whats-new/eofy-deals` is trying to cover everything at once—laptops, TVs, appliances, timing—which means it's directly competing with every other article. The tech-focused pieces are cannibalizing each other on laptop and tech keywords, there's no dedicated page for date-related queries like "when is eofy", and "good guys eofy sale" is scattered across six different URLs instead of being consolidated. Now I need to map out how to restructure this.Now I have everything. Here's the full map.

---

## TGG EOFY Content. Optimise Existing + New Builds

### Diagnosis first: what's broken

`/whats-new/eofy-deals` is trying to rank for everything — timing queries, laptops, TVs, appliances, Apple — and doing none of them well. It's cannibalising every other EOFY article and diluting the whole cluster. "Good guys eofy sale" is split across **6 URLs**. "When is eofy" has no dedicated home and fragments across 4 articles at positions 40–86.

---

### Existing articles. Optimise

| Article | Current best rankings | Problem | Optimisation action |
|---|---|---|---|
| `/whats-new/eofy-deals` | "good guys eofy sale" pos 2, "eofy deals" pos 42, laptop/TV clusters split poorly | Scope creep. Ranking for everything weakly. Cannibalising all other articles. | Refocus as the **EOFY deals hub** only. Strip timing/explainer content (move to new article 1). Strip deep laptop/TV/appliance content (let dedicated articles own those). Add an H2 per category section with anchor links to dedicated guides. This becomes the index, not the content. |
| `/whats-new/guide-to-eofy-tv-deals` | "tv deals eofy" pos 8, "eofy tv sale" pos 10, "eofy tv sales" pos 13 | Performing well. Needs freshening for 2025 models. Minor cannibalisation from `/best-tech-buys-for-eofy`. | **Refresh only.** Update TV recommendations for 2025 range. Add FAQ block: "When do EOFY TV sales start?", "Are EOFY TV prices the best of the year?" Internal link to new timing article. Kill TV content in `/best-tech-buys-for-eofy` to resolve cannibalisation. |
| `/whats-new/eofy-most-popular-home-appliances` | "eofy fridge sales" pos 16, "eofy washing machine sale" pos 16, "good guys eofy sale" pos 3 | Good appliance rankings. "Dyson eofy" pos 80 is underperforming. Generic list format — no depth per category. | **Expand into a proper appliance buying guide.** Split the content: fridge section, washing machine section, dishwasher section, vacuum section. Each gets a buying consideration paragraph, not just a list. Add FAQ: "Is EOFY a good time to buy appliances?" Target "eofy fridge", "eofy washing machine sale" as primary terms. |
| `/whats-new/best-tech-buys-for-eofy` | "tv deals eofy" pos 76 (cannibalising guide-to-eofy-tv-deals), "eofy laptop deals australia" pos 32, "eofy mobile phone deals" pos 33 | Scope too broad. Cannibalises TV article on TV terms, cannibalises eofy-deals on laptop terms. No clear primary intent. | **Repurpose as EOFY laptop + mobile guide** (its strongest non-conflicting cluster). Remove all TV content. Deepen laptop buying section: what to look for, recommended specs, internal links to laptop PLPs. Add mobile phone section. Target: "eofy laptop sale", "eofy phone deals", "eofy laptop deals australia". |
| `/whats-new/eofy-sales-tips-for-university-students` | "good guys eofy sale" pos 13/35, laptop cluster pos 42–83 | Cannibalising the laptop terms now owned by `/best-tech-buys-for-eofy`. Student angle is good but untapped. | **Tighten to student-specific angle.** Remove generic laptop content (let repurposed tech article own that). Focus on: student tax deductions, budget laptop picks for uni, backpacks/monitors/accessories for campus. Target: "laptop eofy sale" in a student context, "eofy sales tips for students". Internal link to dedicated laptop guide for deeper product info. |
| `/whats-new/maximise-your-tax-return` | "good guys eofy sale" pos 23/35/40/51 — clearly diluted | Competing on "good guys eofy sale" against five other articles. Tax-return angle is distinct and defensible but currently unfocused. | **Refocus on "what to buy with your tax return" + "what's tax deductible"**. Target "maximise your tax return", "what to buy with tax return australia", "tax deductible appliances australia". Add clear product sections: home office equipment, appliances for rental properties, small business purchases. Link to Appliances Online's gap: they target businesses, TGG can own the **consumer** tax deductible angle. |

---

### New articles. Build

Priority order based on volume, KD, and gap size.

**1. "What is EOFY? Dates, Meaning and When Sales Start" (Evergreen)**
- Target cluster: "eofy meaning" (1,600), "what is eofy" (320), "when is eofy" (1,600), "when do eofy sales start" (720), "when do eofy sales end" (260), "eofy date" (720), "eofy sale dates" (260) — combined ~5,500 vol
- KD: 6–38 (mostly under 25)
- Why: Harvey Norman's sale page accidentally captures this. JB Hi-Fi's hub page (`/blogs/guides-tips/eofy`) likely covers it. No TGG editorial equivalent exists. This is the entry-point query for millions of Australians before they buy anything.
- Structure: What does EOFY stand for / mean → When does the financial year end in Australia → When do retailers start EOFY sales → When do they end → What's typically on sale → CTA to TGG's `/eofy-sale` page
- URL: `/whats-new/what-is-eofy`
- This also serves as the AEO anchor article. Google AI Mode will pull from a clean explainer like this directly.

**2. "EOFY Laptop Buying Guide" (Seasonal, refreshed annually)**
- Target cluster: "eofy laptop sale" (260), "eofy laptop sales" (210), "eofy laptop deals australia" (110), "eofy sale laptops" (140), "laptop eofy sale" (140), "best eofy laptop deals" (50), "eofy pcs" (140) — combined ~1,010 vol
- KD: 9–36
- Why: JB Hi-Fi's only coverage is a thin "office tech refresh" piece. No competitor has a dedicated laptop buying guide for EOFY. TGG's `/best-tech-buys-for-eofy` will be repurposed to cover this intent properly once its TV content is removed.
- Structure: Why EOFY is a good time to buy a laptop → What specs to prioritise at each budget tier → Top picks from TGG's range → FAQs (Is a laptop tax deductible? What's the best laptop for under $X?) → Internal links to laptop PLP
- URL: `/whats-new/eofy-laptop-buying-guide` (repurpose `/best-tech-buys-for-eofy` or create new and redirect)

**3. "EOFY Home Office Tech Guide: What You Can Claim on Tax" (Seasonal)**
- Target cluster: "home office tax deduction australia" (20), "work from home tax deductions australia" (70), "what can i claim on tax australia" (170), "eofy home office" (no vol yet but JB Hi-Fi targets it), "office tech" (50) — combined ~310 vol + long-tail
- KD: low (0–32)
- Why: JB Hi-Fi has one thin piece. Nobody owns this for electronics/appliances in consumer language. Appliances Online targets businesses. The angle — what you can legitimately claim as a work-from-home employee — is unanswered by any competitor.
- Structure: What home office equipment is tax deductible for employees → Monitors, laptops, headsets, chairs, desks → How to calculate the claim → Links to relevant TGG PLPs → FAQ block
- URL: `/whats-new/eofy-home-office-tax-deductions`
- Note: Add a one-liner caveat to consult an accountant. Don't give specific ATO advice.

**4. "EOFY Apple Deals: iPhone, iPad, MacBook and AirPods" (Seasonal)**
- Target cluster: "eofy apple" (90), "apple eofy" (110), "eofy iphone sale" (110), "iphone eofy sale" (140), "apple eofy sale" (140) — combined ~590 vol
- KD: 20–48
- Why: No competitor has a dedicated Apple EOFY article. TGG stocks Apple and has PLP pages. High commercial intent — people searching "eofy apple" are ready to buy.
- Structure: Is Apple discounted at EOFY? → What Apple products are worth buying at EOFY → iPhone, iPad, MacBook, AirPods sections with TGG product links → Trade-in angle → FAQ block
- URL: `/whats-new/eofy-apple-deals`

**5. "Best EOFY Sales in Australia: What's Worth Buying" (Seasonal hub)**
- Target cluster: "best eofy sales" (480), "best eofy deals" (110), "best eofy sales australia" (210), "best things to buy at eofy" (140) — combined ~940 vol
- KD: 10–32
- Why: Harvey Norman's sale page ranks 14th for "best eofy sales" — purely by domain authority. No editorial content exists anywhere covering this query. TGG's `/whats-new/eofy-deals` could theoretically own this but it's too diluted.
- Structure: Year-by-year or category-by-category breakdown of what genuinely goes on sale vs. what doesn't → TVs (EOFY is one of the best times) → Large appliances (yes) → Laptops (yes) → Phones (variable) → Small appliances (yes) → Gaming (limited) → Internal links to all other EOFY articles and category PLPs
- URL: `/whats-new/best-eofy-sales-australia` (or consolidate `/whats-new/eofy-deals` into this with a redirect if the existing URL doesn't have strong link equity)

---

### Internal linking structure

Once built, these six articles (5 existing, 5 new) should link to each other following this hierarchy:

```
/eofy-sale (commercial hub)
    ↑ linked from all articles
    
/whats-new/what-is-eofy (informational entry point)
    → links to: eofy-deals hub, best-eofy-sales-australia, guide-to-eofy-tv-deals

/whats-new/best-eofy-sales-australia (consideration hub)
    → links to: all category guides below

/whats-new/guide-to-eofy-tv-deals
/whats-new/eofy-laptop-buying-guide  
/whats-new/eofy-most-popular-home-appliances (expanded)
/whats-new/eofy-apple-deals
/whats-new/eofy-home-office-tax-deductions
/whats-new/eofy-sales-tips-for-university-students (tightened)
/whats-new/maximise-your-tax-return (refocused)
```

No circular linking between peer articles except where intent genuinely overlaps (e.g. laptop guide ↔ student tips, home office ↔ tax return).
 
Let me pull the current rankings data first to baseline each existing article properly.
Now I have everything. Here's the full map.

---

## TGG EOFY Content. Optimise Existing + New Builds

### Diagnosis first: what's broken

`/whats-new/eofy-deals` is trying to rank for everything — timing queries, laptops, TVs, appliances, Apple — and doing none of them well. It's cannibalising every other EOFY article and diluting the whole cluster. "Good guys eofy sale" is split across **6 URLs**. "When is eofy" has no dedicated home and fragments across 4 articles at positions 40–86.

---

### Existing articles. Optimise

| Article | Current best rankings | Problem | Optimisation action |
|---|---|---|---|
| `/whats-new/eofy-deals` | "good guys eofy sale" pos 2, "eofy deals" pos 42, laptop/TV clusters split poorly | Scope creep. Ranking for everything weakly. Cannibalising all other articles. | Refocus as the **EOFY deals hub** only. Strip timing/explainer content (move to new article 1). Strip deep laptop/TV/appliance content (let dedicated articles own those). Add an H2 per category section with anchor links to dedicated guides. This becomes the index, not the content. |
| `/whats-new/guide-to-eofy-tv-deals` | "tv deals eofy" pos 8, "eofy tv sale" pos 10, "eofy tv sales" pos 13 | Performing well. Needs freshening for 2025 models. Minor cannibalisation from `/best-tech-buys-for-eofy`. | **Refresh only.** Update TV recommendations for 2025 range. Add FAQ block: "When do EOFY TV sales start?", "Are EOFY TV prices the best of the year?" Internal link to new timing article. Kill TV content in `/best-tech-buys-for-eofy` to resolve cannibalisation. |
| `/whats-new/eofy-most-popular-home-appliances` | "eofy fridge sales" pos 16, "eofy washing machine sale" pos 16, "good guys eofy sale" pos 3 | Good appliance rankings. "Dyson eofy" pos 80 is underperforming. Generic list format — no depth per category. | **Expand into a proper appliance buying guide.** Split the content: fridge section, washing machine section, dishwasher section, vacuum section. Each gets a buying consideration paragraph, not just a list. Add FAQ: "Is EOFY a good time to buy appliances?" Target "eofy fridge", "eofy washing machine sale" as primary terms. |
| `/whats-new/best-tech-buys-for-eofy` | "tv deals eofy" pos 76 (cannibalising guide-to-eofy-tv-deals), "eofy laptop deals australia" pos 32, "eofy mobile phone deals" pos 33 | Scope too broad. Cannibalises TV article on TV terms, cannibalises eofy-deals on laptop terms. No clear primary intent. | **Repurpose as EOFY laptop + mobile guide** (its strongest non-conflicting cluster). Remove all TV content. Deepen laptop buying section: what to look for, recommended specs, internal links to laptop PLPs. Add mobile phone section. Target: "eofy laptop sale", "eofy phone deals", "eofy laptop deals australia". |
| `/whats-new/eofy-sales-tips-for-university-students` | "good guys eofy sale" pos 13/35, laptop cluster pos 42–83 | Cannibalising the laptop terms now owned by `/best-tech-buys-for-eofy`. Student angle is good but untapped. | **Tighten to student-specific angle.** Remove generic laptop content (let repurposed tech article own that). Focus on: student tax deductions, budget laptop picks for uni, backpacks/monitors/accessories for campus. Target: "laptop eofy sale" in a student context, "eofy sales tips for students". Internal link to dedicated laptop guide for deeper product info. |
| `/whats-new/maximise-your-tax-return` | "good guys eofy sale" pos 23/35/40/51 — clearly diluted | Competing on "good guys eofy sale" against five other articles. Tax-return angle is distinct and defensible but currently unfocused. | **Refocus on "what to buy with your tax return" + "what's tax deductible"**. Target "maximise your tax return", "what to buy with tax return australia", "tax deductible appliances australia". Add clear product sections: home office equipment, appliances for rental properties, small business purchases. Link to Appliances Online's gap: they target businesses, TGG can own the **consumer** tax deductible angle. |

---

### New articles. Build

Priority order based on volume, KD, and gap size.

**1. "What is EOFY? Dates, Meaning and When Sales Start" (Evergreen)**
- Target cluster: "eofy meaning" (1,600), "what is eofy" (320), "when is eofy" (1,600), "when do eofy sales start" (720), "when do eofy sales end" (260), "eofy date" (720), "eofy sale dates" (260) — combined ~5,500 vol
- KD: 6–38 (mostly under 25)
- Why: Harvey Norman's sale page accidentally captures this. JB Hi-Fi's hub page (`/blogs/guides-tips/eofy`) likely covers it. No TGG editorial equivalent exists. This is the entry-point query for millions of Australians before they buy anything.
- Structure: What does EOFY stand for / mean → When does the financial year end in Australia → When do retailers start EOFY sales → When do they end → What's typically on sale → CTA to TGG's `/eofy-sale` page
- URL: `/whats-new/what-is-eofy`
- This also serves as the AEO anchor article. Google AI Mode will pull from a clean explainer like this directly.

**2. "EOFY Laptop Buying Guide" (Seasonal, refreshed annually)**
- Target cluster: "eofy laptop sale" (260), "eofy laptop sales" (210), "eofy laptop deals australia" (110), "eofy sale laptops" (140), "laptop eofy sale" (140), "best eofy laptop deals" (50), "eofy pcs" (140) — combined ~1,010 vol
- KD: 9–36
- Why: JB Hi-Fi's only coverage is a thin "office tech refresh" piece. No competitor has a dedicated laptop buying guide for EOFY. TGG's `/best-tech-buys-for-eofy` will be repurposed to cover this intent properly once its TV content is removed.
- Structure: Why EOFY is a good time to buy a laptop → What specs to prioritise at each budget tier → Top picks from TGG's range → FAQs (Is a laptop tax deductible? What's the best laptop for under $X?) → Internal links to laptop PLP
- URL: `/whats-new/eofy-laptop-buying-guide` (repurpose `/best-tech-buys-for-eofy` or create new and redirect)

**3. "EOFY Home Office Tech Guide: What You Can Claim on Tax" (Seasonal)**
- Target cluster: "home office tax deduction australia" (20), "work from home tax deductions australia" (70), "what can i claim on tax australia" (170), "eofy home office" (no vol yet but JB Hi-Fi targets it), "office tech" (50) — combined ~310 vol + long-tail
- KD: low (0–32)
- Why: JB Hi-Fi has one thin piece. Nobody owns this for electronics/appliances in consumer language. Appliances Online targets businesses. The angle — what you can legitimately claim as a work-from-home employee — is unanswered by any competitor.
- Structure: What home office equipment is tax deductible for employees → Monitors, laptops, headsets, chairs, desks → How to calculate the claim → Links to relevant TGG PLPs → FAQ block
- URL: `/whats-new/eofy-home-office-tax-deductions`
- Note: Add a one-liner caveat to consult an accountant. Don't give specific ATO advice.

**4. "EOFY Apple Deals: iPhone, iPad, MacBook and AirPods" (Seasonal)**
- Target cluster: "eofy apple" (90), "apple eofy" (110), "eofy iphone sale" (110), "iphone eofy sale" (140), "apple eofy sale" (140) — combined ~590 vol
- KD: 20–48
- Why: No competitor has a dedicated Apple EOFY article. TGG stocks Apple and has PLP pages. High commercial intent — people searching "eofy apple" are ready to buy.
- Structure: Is Apple discounted at EOFY? → What Apple products are worth buying at EOFY → iPhone, iPad, MacBook, AirPods sections with TGG product links → Trade-in angle → FAQ block
- URL: `/whats-new/eofy-apple-deals`

**5. "Best EOFY Sales in Australia: What's Worth Buying" (Seasonal hub)**
- Target cluster: "best eofy sales" (480), "best eofy deals" (110), "best eofy sales australia" (210), "best things to buy at eofy" (140) — combined ~940 vol
- KD: 10–32
- Why: Harvey Norman's sale page ranks 14th for "best eofy sales" — purely by domain authority. No editorial content exists anywhere covering this query. TGG's `/whats-new/eofy-deals` could theoretically own this but it's too diluted.
- Structure: Year-by-year or category-by-category breakdown of what genuinely goes on sale vs. what doesn't → TVs (EOFY is one of the best times) → Large appliances (yes) → Laptops (yes) → Phones (variable) → Small appliances (yes) → Gaming (limited) → Internal links to all other EOFY articles and category PLPs
- URL: `/whats-new/best-eofy-sales-australia` (or consolidate `/whats-new/eofy-deals` into this with a redirect if the existing URL doesn't have strong link equity)

---

### Internal linking structure

Once built, these six articles (5 existing, 5 new) should link to each other following this hierarchy:

```
/eofy-sale (commercial hub)
    ↑ linked from all articles
    
/whats-new/what-is-eofy (informational entry point)
    → links to: eofy-deals hub, best-eofy-sales-australia, guide-to-eofy-tv-deals

/whats-new/best-eofy-sales-australia (consideration hub)
    → links to: all category guides below

/whats-new/guide-to-eofy-tv-deals
/whats-new/eofy-laptop-buying-guide  
/whats-new/eofy-most-popular-home-appliances (expanded)
/whats-new/eofy-apple-deals
/whats-new/eofy-home-office-tax-deductions
/whats-new/eofy-sales-tips-for-university-students (tightened)
/whats-new/maximise-your-tax-return (refocused)
```

No circular linking between peer articles except where intent genuinely overlaps (e.g. laptop guide ↔ student tips, home office ↔ tax return).

---

### 13. **Human** — 2026-04-20T05:52

create as a sheet pls
create as a sheet pls

---

### 14. **Claude** — 2026-04-20T05:56

Let me read the xlsx skill first.
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

Four sheets:

**1. Optimise Existing** — all 6 current articles with current rankings, problem diagnosis, rewrite brief, H1 suggestion, content additions, and internal links to add. Priority-coded (red/blue/amber).

**2. New Builds** — 5 new articles with proposed URL, H1, full keyword cluster, gap rationale, recommended structure, FAQ block, internal links, and competitor coverage summary.

**3. Internal Linking Map** — full linking architecture across all 11 articles, tiered T0–T2, with explicit "links out to" and "receives links from" columns so nothing gets orphaned.

**4. Keyword Master** — 41 keywords mapped to current TGG URL, current position, target URL, and action type (colour-coded: green = new article, orange = repurpose, blue = refresh, etc.).
 
Four sheets:

**1. Optimise Existing** — all 6 current articles with current rankings, problem diagnosis, rewrite brief, H1 suggestion, content additions, and internal links to add. Priority-coded (red/blue/amber).

**2. New Builds** — 5 new articles with proposed URL, H1, full keyword cluster, gap rationale, recommended structure, FAQ block, internal links, and competitor coverage summary.

**3. Internal Linking Map** — full linking architecture across all 11 articles, tiered T0–T2, with explicit "links out to" and "receives links from" columns so nothing gets orphaned.

**4. Keyword Master** — 41 keywords mapped to current TGG URL, current position, target URL, and action type (colour-coded: green = new article, orange = repurpose, blue = refresh, etc.).

---

### 15. **Human** — 2026-04-20T06:10

i like it, but the keywoords and positions should be one row per, and should be non-brand e.g.

tv deals eofy p8 should be its own row with position (header): 8  and the url repeated cross rows. same for volume (combine 1 time as sum and then show each kw per row).
i like it, but the keywoords and positions should be one row per, and should be non-brand e.g.

tv deals eofy p8 should be its own row with position (header): 8  and the url repeated cross rows. same for volume (combine 1 time as sum and then show each kw per row).

---

### 16. **Claude** — 2026-04-20T06:15

Simon wants the keyword data restructured so that each keyword gets its own row, with the URL repeated across rows. The current format has multiple keywords per cell. He wants:
- One row per keyword
- Position as its own column
- Volume per keyword (not combined)
- URL repeated across rows

This applies to Sheet 1 (Optimise Existing) - the "Current Best Rankings" column should be exploded into individual rows. And possibly Sheet 2 as well.

Let me think about what he wants specifically:

For Sheet 1 (Optimise Existing), the current structure is one row per article with multiple keywords in cells. He wants:
- Still one row per article but with keyword data expanded


- Actually, I think he's asking for the opposite - he wants to explode the "Current Best Rankings" column so each keyword-position pair becomes its own row, with the URL repeated across those new rows. That way position becomes its own column instead of being embedded in the keyword cell.

So the structure should be: Article URL repeated for each keyword, then Keyword, Volume, and Position as separate columns, with the other article-level data also repeated. And he wants a summary row at the top or bottom showing the total volume summed across all keywords for that article.

Let me restructure Sheet 1 to expand it this way - each keyword gets its own row, article metadata repeats, and I'll add a totals row per article grouping.

I should do the same for Sheet 2 with the New Builds, and check Sheet 4 to make sure position and volume are properly separated there too.

Now I'm mapping the existing articles to their keywords and positions from the Semrush data I pulled earlier. Starting with the first article...

Mapping keywords and their rankings for the EOFY deals article, which has a bunch of variations around "eofy" with positions ranging from 2 to 68 and search volumes between 90 and 480. Looking at more Semrush data for EOFY-related keywords, I'm seeing variations around TV and laptop sales with different search volumes and cost-per-click metrics pointing to similar landing pages on The Good Guys site. I'm looking at more search results for Good Guys EOFY sales, tracking different keyword variations and their performance metrics across pages and impressions, then moving into queries about when the 2025 EOFY sale occurs. I'm looking at search query data for EOFY sales, examining metrics like search volume, competition levels, and cost-per-click across different product categories and landing pages to identify the most valuable keywords for targeting. Now I'm looking at search performance data for laptop, phone, and appliance deals during EOFY, tracking metrics like search volume and cost per click across different product categories and landing pages. I'm looking at search volume data for EOFY-related keywords and need to filter out branded queries like "Good Guys EOFY sale" to focus only on non-branded terms. The keywords that qualify are general searches like TV deals, laptops, and broader EOFY sales queries.

Now I'm organizing these keywords by their best ranking positions across different article URLs, starting with the /whats-new/eofy-deals page and mapping which keywords perform strongest there. Looking at search performance data for related EOFY pages, I'm seeing strong traffic on TV deals content with "tv deals eofy" pulling 8,880 impressions, while home appliance guides are performing well with fridge and washing machine queries around 110-170 impressions each.

Now I'm mapping out the new spreadsheet structure where each keyword gets its own row with the article URL, search volume, current ranking position, keyword difficulty, and total article volume, so I can identify optimization gaps and prioritize which keywords need attention across all the EOFY content pieces.

For the layout, I'll use group header rows with a darker background to show each article URL and its total volume summary, then list the individual keywords underneath, keeping the article-level columns like Problem and Action only on the header rows to avoid repetition and keep it visually clean.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Restructured. What's changed:

**Sheet 1 & 2** — each article now has a navy group header row (showing the brief, action, H1, total vol) followed by individual keyword rows below it, one per line with its own Vol, Position, and KD columns. All brand terms ("good guys eofy sale") removed.

**Sheet 3 (Keyword Master)** — already one row per keyword, now cleaned up with a Type column (Informational / TV / Laptop / Appliances / Apple / Tax / Phone / Deals Hub) colour-coded separately from the Action column, so you can filter by either dimension.
 
Restructured. What's changed:

**Sheet 1 & 2** — each article now has a navy group header row (showing the brief, action, H1, total vol) followed by individual keyword rows below it, one per line with its own Vol, Position, and KD columns. All brand terms ("good guys eofy sale") removed.

**Sheet 3 (Keyword Master)** — already one row per keyword, now cleaned up with a Type column (Informational / TV / Laptop / Appliances / Apple / Tax / Phone / Deals Hub) colour-coded separately from the Action column, so you can filter by either dimension.
