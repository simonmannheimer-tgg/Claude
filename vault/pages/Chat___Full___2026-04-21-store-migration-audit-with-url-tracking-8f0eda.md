---
title: Store migration audit with URL tracking (full)
parent: Chat/Light/2026-04-21-store-migration-audit-with-url-tracking-8f0eda
uuid: 8f0eda00-e60c-4bd7-ab4d-ab103e22cb8c
---

#chat/full #project/main #status/completed

# Store migration audit with URL tracking — Full Transcript

→ Light view: [[Chat/Light/2026-04-21-store-migration-audit-with-url-tracking-8f0eda]]
→ Medium view: [[Chat/Medium/2026-04-21-store-migration-audit-with-url-tracking-8f0eda]]

**Messages:** 8 | **Date:** 2026-04-21

---

### 1. **Human** — 2026-04-21T01:49

see how this migration audit is happening cross brands? i want one for stores - see their pre and post urls (geelong > /stores/geelong) and include (sum) their ?utm urls as these are also indicators. I want to know if anything happened.
see how this migration audit is happening cross brands? i want one for stores - see their pre and post urls (geelong > /stores/geelong) and include (sum) their ?utm urls as these are also indicators. I want to know if anything happened.

---

### 2. **Claude** — 2026-04-21T01:54

Let me read the uploaded files to understand what's happening with the migration audit, then figure out what's needed for stores.
```
This block is not supported on your current device yet.
```

Now let me look at the HTML file to understand how the brand migration audit is structured.
```
This block is not supported on your current device yet.
```

Let me check the actual content of that HTML to understand the migration audit logic - particularly what pre and post URLs look like and how they were analyzed.
```
This block is not supported on your current device yet.
```

Now let me look at the atleo.csv file to understand the date+page structure.
```
This block is not supported on your current device yet.
```

That's a Google Business Profile performance data file, not a GSC URL data file. Let me look at the main CSV to understand the stores URL pattern and think about what I need to do.

The main CSV has:
- page (URL)
- Clicks, Impressions, CTR, Avg Position (GSC metrics)
- Sessions, Key Events, Revenue (GA4 metrics)

I need to:
1. Filter for store pages (pre-migration: maybe `/store/` or `/store-locator/` type patterns, post-migration: `/stores/[store-name]`)
2. Group clean URLs (without UTM params) and their UTM variants


3. Aggregate the clicks and impressions across UTM variants for each clean URL, then figure out what the pre-migration structure looked like compared to the new `/stores/[store-name]` format

Let me search through the CSV to identify the actual store URL patterns.
```
This block is not supported on your current device yet.
```

Now I can see the pattern:
- Pre-migration: `/[store-name]/store` (e.g., `/geelong/store`, `/artarmon/store`, `/bankstown/store`)
- Post-migration: `/stores/[store-name]` (e.g., `/stores/geelong`, `/stores/cairns`)

Wait, I'm not seeing `/geelong/store` - let me check more carefully.
```
This block is not supported on your current device yet.
```

I see. The pre-migration pattern is very sparse in this data (only 1 URL: `/townsville/store` with 0 clicks). The bulk of this data is post-migration. Let me check what the pre-migration URLs look like more broadly - maybe it's `/[store]/store` or maybe it's another pattern like `/store-locator` and individual store pages. Let me check all the patterns.

Actually wait - looking at the path patterns earlier I saw things like `/artarmon/store`, `/bankstown/store` etc. 

So those URLs with the location prefix followed by `/store` are likely the pre-migration format I'm looking for.
```
This block is not supported on your current device yet.
```

OK so the data has:
- Very few pre-migration URLs (only `/townsville/store` with 0 clicks is showing up)
- 1,185 post-migration clean URLs (`/stores/[slug]`)
- 6,849 post-migration UTM URLs

The pre-migration pattern was `/[city]/store` but there's almost no data for those - probably because the migration happened before the data window starts (migration was end of June 2024, and the data might start from a period after that).

But wait, the user said "see their pre and post urls (geelong > /stores/geelong)". 

I need to look at all the path patterns in the data to figure out what the pre-migration URLs actually looked like and whether there are any with actual traffic.
```
This block is not supported on your current device yet.
```

So pre-migration store URLs have zero traffic in this dataset. This makes sense because the migration was June 2024 and the data probably starts after that point. 

But the user still wants an audit similar to the brand pages one. Let me think about what I can actually do here:

1. The data shows post-migration `/stores/[slug]` URLs - both clean and UTM variants
2. I can aggregate clicks/impressions by store (summing clean + UTM variants)
3. I can show which stores are performing and which aren't


4. The pre-migration URLs follow the `/[city]/store` pattern, and while they appear in the data, they're showing zero traffic - likely just residual entries with no meaningful activity to compare against.

The user wants to see old URL, new URL, and combined performance, but without actual traffic on the pre-migration side, I'll need to focus on what the post-migration data reveals about store performance.

Since there's only one GSC file here, I'm really doing a post-migration analysis where I'll group all the `/stores/[slug]` URLs together with their UTM variants, sum the clicks across them, and show the clean URL performance alongside. The pre-migration URL format will be shown as a reference point based on the migration pattern the user described. I need to map the pre-migration store URLs to their post-migration equivalents and pull together the performance data with UTM variants summed up, though I'm realizing the export only has post-migration data so I'll need to note that limitation. Let me check the data timeframe to give proper context around what happened.
```
This block is not supported on your current device yet.
```

Interesting - the `clean_clicks` is 0 for all of these. That means there are NO clean `/stores/[slug]` URLs with traffic - all the traffic is coming through UTM URLs from Google My Business. This is a big finding!

Let me verify this is accurate and understand what's happening with the clean URLs.
```
This block is not supported on your current device yet.
```

Good, so the clean store URLs DO have clicks. My earlier code had a bug - it was using `.lower()` on the slug when looking up in `store_data`, but the keys were lowercase. Let me re-examine why the clean_clicks showed as 0.

Oh I see the issue - the `clean_clicks` assignment was overwriting, not accumulating. Some slugs might have multiple clean URLs (because some stores have multiple variations). Let me redo the aggregation properly.

Also - the key insight: 73.5% of store page clicks come through UTM-tagged URLs (Google My Business links). This is crucial.


Now I'm structuring the audit output with all the key metrics for each store - pre and post URLs, click and impression counts for both clean and UTM traffic, average position, and UTM URL variations. I'll sort by total clicks and also flag any stores showing UTM traffic without corresponding clean URL traffic, which could indicate indexing problems.
```
This block is not supported on your current device yet.
```

Good - now I can see the data. Let me now build this into an Excel file with proper formatting. Let me also check for any stores with 0 clean clicks but UTM traffic (indexing issue candidates).
```
This block is not supported on your current device yet.
```

Now I have a clear picture. Let me now look at the skill for Excel to create a proper output file.

Key findings:
1. 126 store slugs in the post-migration data
2. 73.5% of store page traffic comes via GMB UTM URLs, only 26.5% is organic GSC traffic
3. 13 stores have zero traffic: some are home delivery centres (HDC), there's 'undefined', 'gegng' (typo for geelong?), 'darw in' (Darwin with a space - URL slug error!), state-level slugs (act, nsw, nt)


4. Pre-migration data isn't available in this export since the migration happened in June 2024, so I can only assess post-migration performance
5. The "darw in" slug with the embedded space is a clear URL bug that needs fixing

Since we're working with post-migration data only, the key story is that GMB UTM traffic is driving the majority of visits while organic GSC traffic lags behind, plus there are some broken slugs and zero-traffic categories that stand out. Now I'm building the Excel file to present these findings.
```
This block is not supported on your current device yet.
```

Now let me build the Excel file. I'll create a store migration audit with:
1. A summary sheet with key findings
2. A detailed store-by-store table with pre/post URLs, clean clicks, UTM clicks, total, impressions, position, UTM count, etc.
3. Highlight anomalous slugs (broken ones, zeros)

Let me write this in openpyxl.
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

Three sheets: **Summary**, **Store Detail** (126 stores, sortable), **Anomalies**.

**What happened:**

The pre-migration URL pattern (`/geelong/store`) is confirmed. Only one pre-migration URL survives in this GSC export with 0 clicks. The data window post-dates the migration, so there's no before/after click delta. What the data does show is structural.

**The main finding: 73.5% of store page traffic enters via GMB UTM links, not organic search.** Of 1.81M total store page clicks, 1.33M come through `?utm_campaign=Google+My+Business` URLs and only 481k are clean organic. This means Google My Business is the dominant entry point for store pages, which makes sense for a physical retailer. But it also means:

1. Any ranking issue on `/stores/[slug]` would be partially masked by GMB traffic continuing to flow.
2. The clean organic positions (avg ~5–8 for top stores) are reasonable, but impressions are high for some stores with weaker positions, suggesting ranking dilution or low CTR from branded navigational queries.

**Anomalies flagged (13):**
- `darw in` — space in the slug. That URL is broken. Should be `/stores/darwin`.
- `gegng` — looks like a typo for geelong (but `/stores/geelong` exists separately, so this is a duplicate stub).
- 7 HDC (home delivery centre) slugs with zero traffic. Expected if not public-facing, worth confirming they aren't indexed.
- `act`, `nsw`, `nt` — state-level hub pages with zero traffic. Check if live and whether they should be indexable.
 
Three sheets: **Summary**, **Store Detail** (126 stores, sortable), **Anomalies**.

**What happened:**

The pre-migration URL pattern (`/geelong/store`) is confirmed. Only one pre-migration URL survives in this GSC export with 0 clicks. The data window post-dates the migration, so there's no before/after click delta. What the data does show is structural.

**The main finding: 73.5% of store page traffic enters via GMB UTM links, not organic search.** Of 1.81M total store page clicks, 1.33M come through `?utm_campaign=Google+My+Business` URLs and only 481k are clean organic. This means Google My Business is the dominant entry point for store pages, which makes sense for a physical retailer. But it also means:

1. Any ranking issue on `/stores/[slug]` would be partially masked by GMB traffic continuing to flow.
2. The clean organic positions (avg ~5–8 for top stores) are reasonable, but impressions are high for some stores with weaker positions, suggesting ranking dilution or low CTR from branded navigational queries.

**Anomalies flagged (13):**
- `darw in` — space in the slug. That URL is broken. Should be `/stores/darwin`.
- `gegng` — looks like a typo for geelong (but `/stores/geelong` exists separately, so this is a duplicate stub).
- 7 HDC (home delivery centre) slugs with zero traffic. Expected if not public-facing, worth confirming they aren't indexed.
- `act`, `nsw`, `nt` — state-level hub pages with zero traffic. Check if live and whether they should be indexable.

---

### 3. **Human** — 2026-04-21T01:56

chart showing traffic and potential issues
chart showing traffic and potential issues

---

### 4. **Claude** — 2026-04-21T01:57

The user wants a chart showing traffic and potential issues from the stores audit data. Let me build an interactive visualization using the data I already have.
```
This block is not supported on your current device yet.
```

Now I'll build an interactive chart showing store traffic by store (clean vs UTM) with anomalies highlighted. Let me use Chart.js with the data I already computed.

The key data points:
- Top stores by total clicks (clean + UTM)
- Show clean vs UTM split as a stacked bar
- Highlight anomalies (zero traffic, slug errors)
- Maybe add a donut showing the 73.5% GMB share
- Show the anomaly list

I have 126 stores - I'll show the top 30 by total clicks in a horizontal bar chart, then a summary panel.


I'll structure this with metric cards displaying the key stats at the top, a stacked horizontal bar chart for the top 30 stores showing the organic versus GMB UTM breakdown, and then list out the anomalies below.
```
This block is not supported on your current device yet.
```

The GMB UTM dominance (73.5%) is the main structural finding. Organic GSC clicks are real but secondary — meaning store page rankings mostly matter for impression share and brand presence, while the actual foot traffic driver is Google My Business. If GMB listing quality drops or gets suspended for any store, you'd lose the majority of that page's traffic immediately, with almost no organic fallback for the weaker-positioned stores.

The three red anomalies (`darw in`, `gegng`, `undefined`) need CMS fixes. The state pages (`act`, `nsw`, `nt`) worth checking whether they're meant to be indexable hub pages or just internal routing.
 
The GMB UTM dominance (73.5%) is the main structural finding. Organic GSC clicks are real but secondary — meaning store page rankings mostly matter for impression share and brand presence, while the actual foot traffic driver is Google My Business. If GMB listing quality drops or gets suspended for any store, you'd lose the majority of that page's traffic immediately, with almost no organic fallback for the weaker-positioned stores.

The three red anomalies (`darw in`, `gegng`, `undefined`) need CMS fixes. The state pages (`act`, `nsw`, `nt`) worth checking whether they're meant to be indexable hub pages or just internal routing.

---

### 5. **Human** — 2026-04-21T02:08

in a html on the side
in a html on the side

---

### 6. **Claude** — 2026-04-21T02:08

The user wants the chart as an artifact/HTML file displayed on the side (as an artifact in the sidebar), not inline.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

There you go. Opens as a standalone file, no dependencies beyond the Chart.js CDN.
 
There you go. Opens as a standalone file, no dependencies beyond the Chart.js CDN.

---

### 7. **Human** — 2026-04-21T02:10

anything in the audit? for any errors in urls, how much traffic, does it need redirection
anything in the audit? for any errors in urls, how much traffic, does it need redirection

---

### 8. **Claude** — 2026-04-21T02:11

The user wants to know about URL errors in the audit, how much traffic those anomalous slugs have, and whether redirection is needed. Let me check the data for the anomalous slugs specifically.
```
This block is not supported on your current device yet.
```

All the anomalies have zero traffic - which makes sense since they're "zero traffic" anomalies. Let me look more carefully:

1. `darw in` - the URL itself has a space, so the actual URL in the CSV is garbled (`/stores/darw in?utm mf+GZoryveood+Guys+Darlb .win+-+Millner=`). This is Darwin. But `/stores/darwin` might exist separately with traffic. Let me check.

2. `gegng` - zero traffic, possibly a typo for geelong but geelong already exists


3. `act`, `nsw`, `nt` - these are actually state sub-paths like `/stores/act/canberra`, `/stores/nsw/dubbo`, `/stores/nt/darwin` rather than state-level slugs. Now I need to verify if `/stores/darwin` exists as its own page with traffic, since the GMB listing might be pointing to a broken URL.
```
This block is not supported on your current device yet.
```

Now I have a clear picture. Let me summarize the findings:

1. **`darw in`** (space in slug): The GSC data contains a garbled URL (`/stores/darw in?utm...`) which has 0 clicks. But `/stores/darwin` exists and has 20,769 total clicks (15,287 GMB UTM + 5,482 organic). So this broken slug is just a data artifact from a malformed GMB UTM parameter. The actual Darwin page is fine. No redirect needed - it's a GMB listing issue where the URL was entered incorrectly. The page itself is working.


2. **`gegng`**: Zero traffic with a clean URL in GSC - this is clearly a typo since geelong already pulls in 40,182 clicks. It's either a test page or misconfigured entry that needs a 301 redirect to `/stores/geelong` if it's live, otherwise no action required.
3. **`undefined`**: Zero traffic appearing as a literal slug in the URL structure - this is a CMS or JavaScript error where a store ID isn't being populated correctly. It's a backend issue, not a redirect problem.
4. **HDC slugs** (5 of them): All showing zero traffic and probably shouldn't be publicly indexable - they either need noindex tags or shouldn't have public URLs at all.
5. **State sub-paths** (`/stores/act/canberra`, `/stores/nsw/dubbo`, `/stores/nt/darwin`): Zero traffic, suggesting a routing structure that's not functioning properly. The actual store pages exist at simpler paths like `/stores/darwin`, which is performing well with 20,769 clicks.
6. **`burwood`**: Zero traffic - need to check if this store is actually live or if there's a GMB listing issue.

The "darw in" slug turned out to be a GSC artifact from a malformed GMB UTM parameter, not an actual broken page. Darwin's real URL is healthy and driving solid traffic.

So the actual fixes needed are straightforward: `gegng` needs a 301 redirect to `geelong`, the `undefined` slug requires a developer fix, HDCs should be noindexed or removed entirely, and those state sub-paths are just routing quirks that don't need redirects.Here's what's actually happening for each:

**`darw in` (space in slug) — no action needed on the page.** Darwin's real page (`/stores/darwin`) is healthy: 20,769 combined clicks (15,287 GMB UTM + 5,482 organic). The garbled slug is just a bad URL string in a single GMB UTM parameter. The page is fine. Fix the GMB listing URL if it's still live with that typo, but no redirect required.

**`gegng` — 301 to `/stores/geelong`.** Zero traffic, but it's a live clean URL in GSC. Geelong itself has 40,182 clicks and is healthy. This is a duplicate stub. If it resolves to a page, redirect it.

**`undefined` — dev fix, not a redirect.** Appears on both `www` and `checkout` subdomains with zero traffic. A store ID is being passed as the literal string "undefined" somewhere in the CMS or JS. That's a null-value bug, not a routing issue. No redirect will fix it.

**HDC slugs (5 of them) — noindex or remove, no redirect needed.** All zero traffic, zero impressions. These are internal home delivery centres that shouldn't be public-facing. If the pages are live, add `noindex`. No redirect target makes sense since there's no public store to redirect to.

**State sub-paths (`/stores/act/canberra`, `/stores/nsw/dubbo`, `/stores/nt/darwin`) — investigate routing only.** These have zero traffic but Darwin's real URL (`/stores/darwin`) is working fine. These look like leftover routing artifacts from a state-level navigation structure that never launched. No redirect needed unless they're currently indexed.

**`burwood` — check if the store is open.** Zero clicks and impressions. No GMB UTM traffic either, which means either the GMB listing is missing/suspended or the store closed. Verify before taking action.

**Summary: one redirect (`gegng` → `/stores/geelong`), one dev bug (`undefined`), the rest are noindex/GMB hygiene issues. No traffic is being lost to any of these.**
 
Here's what's actually happening for each:

**`darw in` (space in slug) — no action needed on the page.** Darwin's real page (`/stores/darwin`) is healthy: 20,769 combined clicks (15,287 GMB UTM + 5,482 organic). The garbled slug is just a bad URL string in a single GMB UTM parameter. The page is fine. Fix the GMB listing URL if it's still live with that typo, but no redirect required.

**`gegng` — 301 to `/stores/geelong`.** Zero traffic, but it's a live clean URL in GSC. Geelong itself has 40,182 clicks and is healthy. This is a duplicate stub. If it resolves to a page, redirect it.

**`undefined` — dev fix, not a redirect.** Appears on both `www` and `checkout` subdomains with zero traffic. A store ID is being passed as the literal string "undefined" somewhere in the CMS or JS. That's a null-value bug, not a routing issue. No redirect will fix it.

**HDC slugs (5 of them) — noindex or remove, no redirect needed.** All zero traffic, zero impressions. These are internal home delivery centres that shouldn't be public-facing. If the pages are live, add `noindex`. No redirect target makes sense since there's no public store to redirect to.

**State sub-paths (`/stores/act/canberra`, `/stores/nsw/dubbo`, `/stores/nt/darwin`) — investigate routing only.** These have zero traffic but Darwin's real URL (`/stores/darwin`) is working fine. These look like leftover routing artifacts from a state-level navigation structure that never launched. No redirect needed unless they're currently indexed.

**`burwood` — check if the store is open.** Zero clicks and impressions. No GMB UTM traffic either, which means either the GMB listing is missing/suspended or the store closed. Verify before taking action.

**Summary: one redirect (`gegng` → `/stores/geelong`), one dev bug (`undefined`), the rest are noindex/GMB hygiene issues. No traffic is being lost to any of these.**
