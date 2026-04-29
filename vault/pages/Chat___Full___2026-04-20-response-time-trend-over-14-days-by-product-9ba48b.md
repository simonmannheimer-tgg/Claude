---
title: Response time trend over 14 days by product (full)
parent: Chat/Light/2026-04-20-response-time-trend-over-14-days-by-product-9ba48b
uuid: 9ba48b82-e7c8-40f0-bcd8-083a9edd0846
---

#chat/full #project/main #status/completed

# Response time trend over 14 days by product — Full Transcript

→ Light view: [[Chat/Light/2026-04-20-response-time-trend-over-14-days-by-product-9ba48b]]
→ Medium view: [[Chat/Medium/2026-04-20-response-time-trend-over-14-days-by-product-9ba48b]]

**Messages:** 28 | **Date:** 2026-04-20

---

### 1. **Human** — 2026-04-20T00:06

help me rewrite this query:

// Response time trend 
// Chart request duration over the last 12 hours. 
// To create an alert for this query, click '+ New alert rule'
requests
| where timestamp > ago(12h) 
| summarize avgRequestDuration=avg(duration) by bin(timestamp, 10m) // use a time grain of 10 minutes
| render timechart

i want response time last 14 days

for products, so URLs like the attached - you may want to make some sort of regex handling sequential numbers and only 3 / slashes
help me rewrite this query:

// Response time trend 
// Chart request duration over the last 12 hours. 
// To create an alert for this query, click '+ New alert rule'
requests
| where timestamp > ago(12h) 
| summarize avgRequestDuration=avg(duration) by bin(timestamp, 10m) // use a time grain of 10 minutes
| render timechart

i want response time last 14 days

for products, so URLs like the attached - you may want to make some sort of regex handling sequential numbers and only 3 / slashes

---

### 2. **Claude** — 2026-04-20T00:06

The user is asking me to:
1. Rewrite a query (appears to be KQL - Kusto Query Language for Azure/Application Insights)
2. Change the time window from 12 hours to 14 days
3. Filter for products (not all requests)
4. Handle URLs with sequential numbers and 3 slashes using regex

Looking at the document provided, these are product URLs from thegoodguys.com.au:
- https://www.thegoodguys.com.au/sharp-trim-kit-stainless-steel-for-r321cafst-and-r395est-ebr39st
- https://www.thegoodguys.com.au/sedko-pty-ltd-melody-tv-cabinet-1600mm-oak-24-melody-1600-oak
- https://www.thegoodguys.com.au/schweigen-60cm-black-undermount-rangehood-900m3hr-um1170-6bst
etc.

The pattern appears to be:
- Protocol + domain: https://www.thegoodguys.com.au/
- Then a product slug
- Some product URLs have sequential numbers at the end

The user wants to filter for just product URLs. Looking at the pattern, they seem to want:
- https:// (protocol)
- www.thegoodguys.com.au/ (domain)
- product slug (contains hyphens, letters, numbers)
- Potentially ends with sequential numbers

The "3 slashes" constraint likely means:
- 1st slash in https://
- 2nd slash in www.thegoodguys.com.au/
- 3rd slash at the end of the domain

So the regex should match URLs with exactly 3 slashes up to the product part, then optionally capture sequential numbers at the end.


I need to update the time range to 14 days instead of 12 hours using `ago(14d)`. For the product URL filtering in KQL, I'll add a `where` clause that uses regex matching. The pattern should target the TGG domain structure with product slugs, capturing the hyphenated product names and any trailing numbers like "24-melody-1600-oak" or "um1170-6bst".**Rewritten query for 14-day product response times:**

```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(-\d+)?$"
| summarize avgRequestDuration=avg(duration) by bin(timestamp, 10m)
| render timechart
```

**What changed:**

1. `ago(12h)` → `ago(14d)` for 14-day window.
2. Added `where url matches regex` to filter product URLs only. The pattern matches:
   - Domain `https://www.thegoodguys.com.au/`
   - Product slug (letters, numbers, hyphens)
   - Optional trailing sequential numbers (e.g., `-1600`, `-9bst`)
   - Exactly 3 slashes total (two in protocol, one after domain).

If your product URLs vary in structure (nested categories, query params), adjust the regex. Post an example of an outlier URL and I'll refine it.
**Rewritten query for 14-day product response times:**

```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(-\d+)?$"
| summarize avgRequestDuration=avg(duration) by bin(timestamp, 10m)
| render timechart
```

**What changed:**

1. `ago(12h)` → `ago(14d)` for 14-day window.
2. Added `where url matches regex` to filter product URLs only. The pattern matches:
   - Domain `https://www.thegoodguys.com.au/`
   - Product slug (letters, numbers, hyphens)
   - Optional trailing sequential numbers (e.g., `-1600`, `-9bst`)
   - Exactly 3 slashes total (two in protocol, one after domain).

If your product URLs vary in structure (nested categories, query params), adjust the regex. Post an example of an outlier URL and I'll refine it.

---

### 3. **Human** — 2026-04-20T00:08

change this to match my new url
change this to match my new url

---

### 4. **Claude** — 2026-04-20T00:08

The user is showing me a KQL (Kusto Query Language) query from what looks like Azure Application Insights or similar. They want me to update it to match the product URL regex I just created.

Looking at the query in the image:
```kusto
browserTimings
| where timestamp > ago(14d)
| where url = "/"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```

They want to change `where url = "/"` to match the product URLs using the regex pattern I created.

So I should replace:
`| where url = "/"`

with:
`| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(-\d+)?$"`

Let me provide the updated query.```kusto
browserTimings
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(-\d+)?$"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```

Changed `where url = "/"` to the product URL regex. This filters to product pages only over the 14-day window.
```kusto
browserTimings
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(-\d+)?$"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```

Changed `where url = "/"` to the product URL regex. This filters to product pages only over the 14-day window.

---

### 5. **Human** — 2026-04-20T00:09

no findings in that range
no findings in that range

---

### 6. **Claude** — 2026-04-20T00:09

The user is saying there are no findings in that range with the regex filter. This could mean:

1. The regex is too strict and is filtering out all the product URLs
2. The product URLs don't actually match that pattern
3. The data itself might not have any requests in that 14-day window for products

Looking back at the document they provided, I can see example URLs like:
- https://www.thegoodguys.com.au/sharp-trim-kit-stainless-steel-for-r321cafst-and-r395est-ebr39st
- https://www.thegoodguys.com.au/sedko-pty-ltd-melody-tv-cabinet-1600mm-oak-24-melody-1600-oak
- https://www.thegoodguys.com.au/schweigen-60cm-black-undermount-rangehood-900m3hr-um1170-6bst

These all have more than just sequential numbers at the end. Some have complex slugs with lots of hyphens and numbers throughout. My regex `@"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(-\d+)?$"` is too restrictive because it only allows:
- One slug of letters/numbers/hyphens
- Optionally followed by a dash and digits

But the actual URLs have multiple parts separated by hyphens, with numbers and letters mixed throughout.

I should loosen the regex to match the actual URL structure better. The safest approach would be to just filter for the domain and path structure without being overly specific about the slug pattern.

Let me suggest removing the regex constraint first to see if there's actually data, then we can refine if needed.The regex is likely too strict. Remove the URL filter to check if there's data at all:

```kusto
browserTimings
| where timestamp > ago(14d)
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```

If this returns data, then the issue is the regex pattern. Post a real URL from your logs and I'll match it properly. Your product URLs are more complex (e.g. `sedko-pty-ltd-melody-tv-cabinet-1600mm-oak-24-melody-1600-oak`) than the simple pattern I used.
The regex is likely too strict. Remove the URL filter to check if there's data at all:

```kusto
browserTimings
| where timestamp > ago(14d)
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```

If this returns data, then the issue is the regex pattern. Post a real URL from your logs and I'll match it properly. Your product URLs are more complex (e.g. `sedko-pty-ltd-melody-tv-cabinet-1600mm-oak-24-melody-1600-oak`) than the simple pattern I used.

---

### 7. **Human** — 2026-04-20T00:17

what does this mean?

tried to do a regex for product urls, sequential numbers, only one slash etc.
 
yeah that is UTC too
what does this mean?

tried to do a regex for product urls, sequential numbers, only one slash etc.
 
yeah that is UTC too

---

### 8. **Claude** — 2026-04-20T00:17

The user is asking what "tried to do a regex for product urls, sequential numbers, only one slash etc." and "yeah that is UTC too" means.

Looking back at the conversation:
1. I suggested a regex pattern `@"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(-\d+)?$"` to filter product URLs
2. The user said "no findings in that range"
3. I suggested removing the URL filter to see if there's any data at all
4. Now the user is saying "tried to do a regex for product urls, sequential numbers, only one slash etc. yeah that is UTC too"

I think the user is saying:
- They tried to use the regex I provided for product URLs
- It was looking for sequential numbers and one slash (after the domain)
- And mentioning that the timestamp is in UTC

The issue is that the regex I gave didn't match their actual URLs because:
1. The product URLs have multiple hyphens and mixed formats (like `sedko-pty-ltd-melody-tv-cabinet-1600mm-oak-24-melody-1600-oak`)
2. My pattern was too restrictive with the optional trailing numbers `(-\d+)?` - it only allowed an optional group of numbers at the end
3. The "one slash" part refers to the single `/` after the domain before the product slug

The user is clarifying what they were trying to accomplish with the regex - they want to match product URLs that have:
- Sequential/trailing numbers (like `-1600` or `-9bst`)
- Only one slash (the one separating domain from slug)

Since no data came back, it means either:
1. The regex is too strict (most likely)
2. There is no browserTimings data in that date range
3. The UTC timezone might matter for the date range

I should clarify what went wrong with the regex and ask for real URL examples so I can write a proper pattern.You're saying the regex I provided was too strict—it was trying to match product URLs with trailing sequential numbers and exactly one slash (after the domain), but your actual URLs don't fit that pattern.

The UTC note means the `ago(14d)` query is running against UTC timestamps. If you're in a different timezone, the 14-day window might not align with your local view.

The real issue: your product URLs have complex slugs like `sedko-pty-ltd-melody-tv-cabinet-1600mm-oak-24-melody-1600-oak`. My regex `[a-z0-9\-]+(-\d+)?` expected mostly letters/numbers and an optional trailing number group—it didn't account for that level of slug complexity.

Give me 2-3 real product URLs from your logs (not the sitemap) and I'll write a regex that actually matches them.
You're saying the regex I provided was too strict—it was trying to match product URLs with trailing sequential numbers and exactly one slash (after the domain), but your actual URLs don't fit that pattern.

The UTC note means the `ago(14d)` query is running against UTC timestamps. If you're in a different timezone, the 14-day window might not align with your local view.

The real issue: your product URLs have complex slugs like `sedko-pty-ltd-melody-tv-cabinet-1600mm-oak-24-melody-1600-oak`. My regex `[a-z0-9\-]+(-\d+)?` expected mostly letters/numbers and an optional trailing number group—it didn't account for that level of slug complexity.

Give me 2-3 real product URLs from your logs (not the sitemap) and I'll write a regex that actually matches them.

---

### 9. **Human** — 2026-04-20T00:21

can you create a few other regexes for pages types with large number of representations, e.g. /store/ or categories (more levels than a product, etc)
can you create a few other regexes for pages types with large number of representations, e.g. /store/ or categories (more levels than a product, etc)

---

### 10. **Claude** — 2026-04-20T00:23

The user wants me to:
1. Look at the sitemap audit file to understand URL patterns
2. Create regexes for different page types (products, store pages, categories with multiple levels)
3. Understand what constitutes "large number of representations"

Let me read the file first to see what URL patterns exist.
```
This block is not supported on your current device yet.
```

The file is a binary Excel file (.xlsx), so I can't read it directly through the view tool. I need to use the xlsx skill to actually extract and work with the content. Let me load that skill first.

Actually, let me check the skill first to see how to properly read this file.
```
This block is not supported on your current device yet.
```

Now I need to extract the data from the Excel file. Let me use the extract-text command mentioned in the skill to quickly dump the contents.
```
This block is not supported on your current device yet.
```

Perfect! Now I can see the URL patterns. Let me identify the different page types:

1. **Products** - complex slugs with brand + description + model numbers, e.g.:
   - `/schweigen-90cm-blk-undermount-rangehood-1600m3hr-um1170-9bsp`
   - `/homedics-hot-and-cold-relief-gel-sleeve-elbow-sr-gem700-au`
   - `/franke-franke-pzx220-39-ta9641-pack-pzx22039ta9641`

2. **Stores/Store Locations** - `/stores/[store-name]`, e.g.:
   - `/stores/marion`
   - `/stores/bathurst`
   - `/stores/sydney-home-delivery-centre`

3. **Categories** - Based on the breadcrumb data shown, there appear to be nested categories like:
   - `/cooking-and-dishwashers/rangehoods/undermount-rangehoods`
   - `/health-and-grooming/personal-care/heating-pads`
   - `/cooking-and-dishwashers/sinks-and-taps/kitchen-sink-and-tap-packages`

Let me look for some category URLs in the data to understand the full pattern. Let me grep for categories.
```
This block is not supported on your current device yet.
```

Let me try a different approach to see the category URLs more clearly.
```
This block is not supported on your current device yet.
```

The output is limited. Let me use a different approach - I'll read the entire file using pandas to get better structure and look at all the different URL patterns.
```
This block is not supported on your current device yet.
```

The columns might have different names or leading spaces. Let me check the column names first.
```
This block is not supported on your current device yet.
```

The Excel file wasn't parsed correctly - it looks like the header row is being treated as data. Let me skip the first row and read again.
```
This block is not supported on your current device yet.
```

OK so the data appears to be truncated - there are only 73 rows in this file even though the sitemap audit had 12,086 URLs. It looks like this might be a sample or the file got cut off. But I have enough to see the main patterns:

1. **Products**: Complex slugs with brand + description + specs
   - `/schweigen-90cm-blk-undermount-rangehood-1600m3hr-um1170-9bsp`
   - `/homedics-hot-and-cold-relief-gel-sleeve-elbow-sr-gem700-au`
   - `/sharp-trim-kit-stainless-steel-for-r321cafst-and-r395est-ebr39st`
   - `/franke-franke-pzx220-39-ta9641-pack-pzx22039ta9641`

2. **Stores**: Simple `/stores/[location-name]`
   - `/stores/marion`
   - `/stores/bathurst`
   - etc.

Looking at the breadcrumb URLs from earlier, I can also infer categories exist (e.g. `/cooking-and-dishwashers/rangehoods/undermount-rangehoods`).

Let me create the regexes based on what I found.Based on the sitemap audit, here are regexes for your main page types:
```
This block is not supported on your current device yet.
```

Good, now I have the regexes. Let me present these to Simon with clear explanations and test them against his known URLs to make sure they work.**Four regexes covering your main page types:**

**1. Products** (single-level slugs)
```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```
Matches only `/brand-product-name-model`, e.g. `/schweigen-90cm-blk-undermount-rangehood-1600m3hr-um1170-9bsp`.

**2. Stores** (locales)
```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```
Matches `/stores/location-name`.

**3. Categories** (2+ levels, excludes stores)
```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$"
| where url !matches regex @"^https://www\.thegoodguys\.com\.au/stores"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```
Matches multi-level slugs like `/cooking-and-dishwashers/rangehoods/undermount-rangehoods`.

**4. All structured pages** (products + categories + stores)
```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+)*$"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```

The key difference: regex 1 uses `$` (end-of-line), while regex 4 uses `*` to allow optional additional levels. The category regex explicitly requires 2+ levels using `{1,}`.

Test one against your logs. If you hit unexpected URLs (query params, redirects, legacy pages), post an example and I'll adjust.
Based on the sitemap audit, here are regexes for your main page types:
**Four regexes covering your main page types:**

**1. Products** (single-level slugs)
```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```
Matches only `/brand-product-name-model`, e.g. `/schweigen-90cm-blk-undermount-rangehood-1600m3hr-um1170-9bsp`.

**2. Stores** (locales)
```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```
Matches `/stores/location-name`.

**3. Categories** (2+ levels, excludes stores)
```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$"
| where url !matches regex @"^https://www\.thegoodguys\.com\.au/stores"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```
Matches multi-level slugs like `/cooking-and-dishwashers/rangehoods/undermount-rangehoods`.

**4. All structured pages** (products + categories + stores)
```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+)*$"
| summarize AvgPageLoadSec = avg(totalDuration) / 1000.0 by Day = bin(timestamp, 1d)
| order by Day asc
| render timechart
```

The key difference: regex 1 uses `$` (end-of-line), while regex 4 uses `*` to allow optional additional levels. The category regex explicitly requires 2+ levels using `{1,}`.

Test one against your logs. If you hit unexpected URLs (query params, redirects, legacy pages), post an example and I'll adjust.

---

### 11. **Human** — 2026-04-20T00:25

summarize' operator: Failed to resolve scalar expression named 'totalDuration' Request id: 144295d7-916e-4444-8106-13f1472e5508
summarize' operator: Failed to resolve scalar expression named 'totalDuration' Request id: 144295d7-916e-4444-8106-13f1472e5508

---

### 12. **Claude** — 2026-04-20T00:25

The error is that 'totalDuration' doesn't exist in the requests table. Looking back at the original query the user showed me, it was using 'duration' for the requests table. Let me check what the correct field name is.

Looking at the original queries:
- For `requests` table: `avg(duration)`
- For `browserTimings` table: `avg(totalDuration)`

So I made an error - I mixed the two. For the `requests` table (Application Insights), the field is `duration`, not `totalDuration`. The `totalDuration` is for `browserTimings`.

Let me fix this.The field is `duration`, not `totalDuration`. That's for `browserTimings`. Fix:

```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d)
| order by timestamp asc
| render timechart
```

Apply the same change to all four queries: replace `AvgPageLoadSec = avg(totalDuration) / 1000.0` with `AvgRequestDuration = avg(duration)`.
The field is `duration`, not `totalDuration`. That's for `browserTimings`. Fix:

```kusto
requests
| where timestamp > ago(14d)
| where url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d)
| order by timestamp asc
| render timechart
```

Apply the same change to all four queries: replace `AvgPageLoadSec = avg(totalDuration) / 1000.0` with `AvgRequestDuration = avg(duration)`.

---

### 13. **Human** — 2026-04-20T00:26

any way to show each as its own colour line
any way to show each as its own colour line

---

### 14. **Claude** — 2026-04-20T00:26

The user wants to show multiple URL pattern types as separate colored lines on the same timechart. In Kusto, you can do this by adding a dimension to the summarize clause. Instead of filtering for one regex and running separate queries, you can create a categorization column and summarize by that column along with time.

Let me create a single query that categorizes each request by type and then plots them all together.Yes. Categorize each URL type and plot them together:

```kusto
requests
| where timestamp > ago(14d)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), UrlType
| order by timestamp asc
| render timechart
```

Each URL type (Product, Category, Store) will render as its own line with distinct colour.
Yes. Categorize each URL type and plot them together:

```kusto
requests
| where timestamp > ago(14d)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), UrlType
| order by timestamp asc
| render timechart
```

Each URL type (Product, Category, Store) will render as its own line with distinct colour.

---

### 15. **Human** — 2026-04-20T00:27

what about bot types like google, llms etc
what about bot types like google, llms etc

---

### 16. **Claude** — 2026-04-20T00:27

The user wants to filter for or show different bot types (Google, LLMs, etc.) in the requests data. In Azure Application Insights / Kusto Query Language, user agent information is typically stored in the `client_Browser` field or similar, or you might need to parse the `user_Agent` field directly.

I should provide a query that:
1. Extracts/identifies bot types from user agent
2. Shows them as separate lines like the URL types

Common bot types to look for:
- Googlebot
- GPTBot (OpenAI)
- Gemini (Google)
- Claude (Anthropic)
- Bingbot
- etc.

Let me create a query that categorizes bots.Add bot detection to the user agent:

```kusto
requests
| where timestamp > ago(14d)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
),
BotType = case(
    user_Agent contains "Googlebot", "Googlebot",
    user_Agent contains "GPTBot", "OpenAI",
    user_Agent contains "Claude-Web", "Anthropic",
    user_Agent contains "Gemini", "Google AI",
    user_Agent contains "Bingbot", "Bing",
    user_Agent contains "Applebot", "Apple",
    user_Agent contains "facebookexternalhit", "Facebook",
    user_Agent contains "Slurp", "Yahoo",
    "Human"
)
| where UrlType != "Other"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), BotType
| order by timestamp asc
| render timechart
```

This splits by bot type (Googlebot, OpenAI, Anthropic, etc.) instead of URL type. Combine both by adding `, UrlType` to the `summarize` grouping if you want a grid.
Add bot detection to the user agent:

```kusto
requests
| where timestamp > ago(14d)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
),
BotType = case(
    user_Agent contains "Googlebot", "Googlebot",
    user_Agent contains "GPTBot", "OpenAI",
    user_Agent contains "Claude-Web", "Anthropic",
    user_Agent contains "Gemini", "Google AI",
    user_Agent contains "Bingbot", "Bing",
    user_Agent contains "Applebot", "Apple",
    user_Agent contains "facebookexternalhit", "Facebook",
    user_Agent contains "Slurp", "Yahoo",
    "Human"
)
| where UrlType != "Other"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), BotType
| order by timestamp asc
| render timechart
```

This splits by bot type (Googlebot, OpenAI, Anthropic, etc.) instead of URL type. Combine both by adding `, UrlType` to the `summarize` grouping if you want a grid.

---

### 17. **Human** — 2026-04-20T00:28

'extend' operator: Failed to resolve scalar expression named 'user_Agent' Request id: 1423e1e5-10a7-4259-b1f1-1cabc0a499f8
'extend' operator: Failed to resolve scalar expression named 'user_Agent' Request id: 1423e1e5-10a7-4259-b1f1-1cabc0a499f8

---

### 18. **Claude** — 2026-04-20T00:28

The field name is likely different. It could be `userAgent` (camelCase) or `useragent` (lowercase) or something else. Let me suggest checking what the actual field name is, or use a common alternative.Check your actual user agent field name. Common variations:

```kusto
requests
| where timestamp > ago(14d)
| extend BotType = case(
    client_Browser contains "Googlebot", "Googlebot",
    client_Browser contains "GPTBot", "OpenAI",
    client_Browser contains "Claude-Web", "Anthropic",
    client_Browser contains "Gemini", "Google AI",
    client_Browser contains "Bingbot", "Bing",
    "Human"
)
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), BotType
| order by timestamp asc
| render timechart
```

If that fails, run this first to see available fields:

```kusto
requests
| where timestamp > ago(1h)
| take 1
```

Post the output and I'll match the right column name.
Check your actual user agent field name. Common variations:

```kusto
requests
| where timestamp > ago(14d)
| extend BotType = case(
    client_Browser contains "Googlebot", "Googlebot",
    client_Browser contains "GPTBot", "OpenAI",
    client_Browser contains "Claude-Web", "Anthropic",
    client_Browser contains "Gemini", "Google AI",
    client_Browser contains "Bingbot", "Bing",
    "Human"
)
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), BotType
| order by timestamp asc
| render timechart
```

If that fails, run this first to see available fields:

```kusto
requests
| where timestamp > ago(1h)
| take 1
```

Post the output and I'll match the right column name.

---

### 19. **Human** — 2026-04-20T00:29

url success resultCode duration performanceBucket customDimensions operation_Id itemType operation_ParentId client_Type client_IP client_City client_StateOrProvince client_CountryOrRegion appId appName iKey
Key Value timestamp [UTC]	2026-04-19T23:43:54.621Z	id	e2c474d8-9c83-41b2-b742-6e11c5725d1a-1776642234621	source	13.236.87.116	name	GET /__manifest	url	https://www.thegoodguys.com.au/__manifest?paths=%2Freolink-4k-dual-lens-wireless-security-camera-plus-solar-panel-bwptdb4k10sp64%2C%2Ftp-link-2k-solar-powered-pantilt-4g-lte-security-camera-tapo-c615g-kit%2C%2Ftp-link-3k-solar-powered-pantilt-security-camera-kit-tapo-c630-kit&version=df4d3487	success	True	resultCode	200	duration	0	performanceBucket	<250ms	itemType	request	customDimensions	{"requestHeaders":"{\"accept-language\":\"en-US,en;q=0.9\",\"oxygen-buyer-city\":\"Sydney\",\"oxygen-buyer-continent\":\"OC\",\"oxygen-buyer-country\":\"AU\",\"oxygen-buyer-deployment-id\":\"4413233\",\"oxygen-buyer-region\":\"New South Wales\",\"oxygen-buyer-region-code\":\"NSW\",\"oxygen-buyer-shop-id\":\"64193888321\",\"oxygen-buyer-storefront-id\":\"1000035166\",\"oxygen-buyer-timezone\":\"Australia/Sydney\",\"referer\":\"https://www.thegoodguys.com.au/\",\"sec-ch-ua\":\"\\\"Chromium\\\";v=\\\"146\\\", \\\"Not-A.Brand\\\";v=\\\"24\\\", \\\"Avast Secure Browser\\\";v=\\\"146\\\"\",\"sec-ch-ua-mobile\":\"?0\",\"sec-ch-ua-platform\":\"\\\"Windows\\\"\",\"sec-fetch-mode\":\"cors\",\"sec-fetch-site\":\"same-origin\",\"user-agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Avast/146.0.34394.179\"}"}	operation_Id	e2c474d8-9c83-41b2-b742-6e11c5725d1a-1776642234621	operation_ParentId	e2c474d8-9c83-41b2-b742-6e11c5725d1a-1776642234621	client_Type	PC	client_IP	0.0.0.0	client_City	Sydney	client_StateOrProvince	New South Wales	client_CountryOrRegion	Australia	appId	087645db-4b50-4de4-8545-8036b26761a2	appName	/subscriptions/6b918676-dcf2-43a5-9c34-8c79cf481597/resourcegroups/prd-shopify-logging-rgp/providers/microsoft.insights/components/prd-shopify-logging-ain	iKey	d5f27066-c097-4a4d-a900-81cf6eed961f	sdkVersion	oxygen-server-custom	itemId	9fb6f2b5-3c49-11f1-9d1d-002248d3ad86	itemCount	1	_ResourceId	/subscriptions/6b918676-dcf2-43a5-9c34-8c79cf481597/resourcegroups/prd-shopify-logging-rgp/providers/microsoft.insights/components/prd-shopify-logging-ain
url success resultCode duration performanceBucket customDimensions operation_Id itemType operation_ParentId client_Type client_IP client_City client_StateOrProvince client_CountryOrRegion appId appName iKey
Key Value timestamp [UTC]	2026-04-19T23:43:54.621Z	id	e2c474d8-9c83-41b2-b742-6e11c5725d1a-1776642234621	source	13.236.87.116	name	GET /__manifest	url	https://www.thegoodguys.com.au/__manifest?paths=%2Freolink-4k-dual-lens-wireless-security-camera-plus-solar-panel-bwptdb4k10sp64%2C%2Ftp-link-2k-solar-powered-pantilt-4g-lte-security-camera-tapo-c615g-kit%2C%2Ftp-link-3k-solar-powered-pantilt-security-camera-kit-tapo-c630-kit&version=df4d3487	success	True	resultCode	200	duration	0	performanceBucket	<250ms	itemType	request	customDimensions	{"requestHeaders":"{\"accept-language\":\"en-US,en;q=0.9\",\"oxygen-buyer-city\":\"Sydney\",\"oxygen-buyer-continent\":\"OC\",\"oxygen-buyer-country\":\"AU\",\"oxygen-buyer-deployment-id\":\"4413233\",\"oxygen-buyer-region\":\"New South Wales\",\"oxygen-buyer-region-code\":\"NSW\",\"oxygen-buyer-shop-id\":\"64193888321\",\"oxygen-buyer-storefront-id\":\"1000035166\",\"oxygen-buyer-timezone\":\"Australia/Sydney\",\"referer\":\"https://www.thegoodguys.com.au/\",\"sec-ch-ua\":\"\\\"Chromium\\\";v=\\\"146\\\", \\\"Not-A.Brand\\\";v=\\\"24\\\", \\\"Avast Secure Browser\\\";v=\\\"146\\\"\",\"sec-ch-ua-mobile\":\"?0\",\"sec-ch-ua-platform\":\"\\\"Windows\\\"\",\"sec-fetch-mode\":\"cors\",\"sec-fetch-site\":\"same-origin\",\"user-agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Avast/146.0.34394.179\"}"}	operation_Id	e2c474d8-9c83-41b2-b742-6e11c5725d1a-1776642234621	operation_ParentId	e2c474d8-9c83-41b2-b742-6e11c5725d1a-1776642234621	client_Type	PC	client_IP	0.0.0.0	client_City	Sydney	client_StateOrProvince	New South Wales	client_CountryOrRegion	Australia	appId	087645db-4b50-4de4-8545-8036b26761a2	appName	/subscriptions/6b918676-dcf2-43a5-9c34-8c79cf481597/resourcegroups/prd-shopify-logging-rgp/providers/microsoft.insights/components/prd-shopify-logging-ain	iKey	d5f27066-c097-4a4d-a900-81cf6eed961f	sdkVersion	oxygen-server-custom	itemId	9fb6f2b5-3c49-11f1-9d1d-002248d3ad86	itemCount	1	_ResourceId	/subscriptions/6b918676-dcf2-43a5-9c34-8c79cf481597/resourcegroups/prd-shopify-logging-rgp/providers/microsoft.insights/components/prd-shopify-logging-ain

---

### 20. **Claude** — 2026-04-20T00:30

The user is showing me the actual field names from their Application Insights schema. I can see that `user-agent` is nested inside the `customDimensions` JSON, not as a top-level field. This is a JSON field that contains request headers including the user-agent.

To extract the user-agent from the JSON, I need to parse the customDimensions field. In Kusto, I can use `dynamic` parsing and the `parse_json` function or direct JSON extraction.

Let me provide a query that extracts the user-agent from the customDimensions JSON.The user agent is nested in `customDimensions` JSON. Extract it:

```kusto
requests
| where timestamp > ago(14d)
| extend UserAgent = tostring(parse_json(customDimensions).requestHeaders)
| extend BotType = case(
    UserAgent contains "Googlebot", "Googlebot",
    UserAgent contains "GPTBot", "OpenAI",
    UserAgent contains "Claude-Web", "Anthropic",
    UserAgent contains "Gemini", "Google AI",
    UserAgent contains "Bingbot", "Bing",
    UserAgent contains "Applebot", "Apple",
    "Human"
)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), BotType, UrlType
| order by timestamp asc
| render timechart
```

This splits by both bot type and URL type. If you want only bot type, remove `UrlType` from the `summarize` grouping.
The user agent is nested in `customDimensions` JSON. Extract it:

```kusto
requests
| where timestamp > ago(14d)
| extend UserAgent = tostring(parse_json(customDimensions).requestHeaders)
| extend BotType = case(
    UserAgent contains "Googlebot", "Googlebot",
    UserAgent contains "GPTBot", "OpenAI",
    UserAgent contains "Claude-Web", "Anthropic",
    UserAgent contains "Gemini", "Google AI",
    UserAgent contains "Bingbot", "Bing",
    UserAgent contains "Applebot", "Apple",
    "Human"
)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), BotType, UrlType
| order by timestamp asc
| render timechart
```

This splits by both bot type and URL type. If you want only bot type, remove `UrlType` from the `summarize` grouping.

---

### 21. **Human** — 2026-04-20T00:31

06/04/2026, 00:00:00.000	Human	Store	171.1945147679325	Key Value timestamp [UTC]	2026-04-06T00:00:00Z	BotType	Human	UrlType	Store	AvgRequestDuration	171.1945147679325		06/04/2026, 00:00:00.000	Google AI	Product	490.2692307692308	06/04/2026, 00:00:00.000	Google AI	Category	621.3770491803278	06/04/2026, 00:00:00.000	Apple	Store	316.5508196721311	06/04/2026, 00:00:00.000	Apple	Category	388.05454545454546	06/04/2026, 00:00:00.000	Apple	Product	515.453744493392	06/04/2026, 00:00:00.000	Googlebot	Store	331.22127659574465	06/04/2026, 00:00:00.000	Bing	Store	366.953125	06/04/2026, 00:00:00.000	Bing	Product	590.6588898525586	06/04/2026, 00:00:00.000	Googlebot	Category	338.0252844500632	06/04/2026, 00:00:00.000	Bing	Category	466.72380619205876	06/04/2026, 00:00:00.000	Googlebot	Product	496.5496595043378
06/04/2026, 00:00:00.000	Human	Store	171.1945147679325	Key Value timestamp [UTC]	2026-04-06T00:00:00Z	BotType	Human	UrlType	Store	AvgRequestDuration	171.1945147679325		06/04/2026, 00:00:00.000	Google AI	Product	490.2692307692308	06/04/2026, 00:00:00.000	Google AI	Category	621.3770491803278	06/04/2026, 00:00:00.000	Apple	Store	316.5508196721311	06/04/2026, 00:00:00.000	Apple	Category	388.05454545454546	06/04/2026, 00:00:00.000	Apple	Product	515.453744493392	06/04/2026, 00:00:00.000	Googlebot	Store	331.22127659574465	06/04/2026, 00:00:00.000	Bing	Store	366.953125	06/04/2026, 00:00:00.000	Bing	Product	590.6588898525586	06/04/2026, 00:00:00.000	Googlebot	Category	338.0252844500632	06/04/2026, 00:00:00.000	Bing	Category	466.72380619205876	06/04/2026, 00:00:00.000	Googlebot	Product	496.5496595043378

---

### 22. **Claude** — 2026-04-20T00:31

The query is working and returning results. Simon is showing me the output - it's showing response times broken down by BotType and UrlType for April 6, 2026.

The data shows:
- Human users on Store pages: 171ms avg
- Google AI on Products: 490ms
- Google AI on Categories: 621ms
- Apple on Stores: 316ms
- Apple on Categories: 388ms
- Apple on Products: 515ms
- Googlebot on Stores: 331ms
- Bing on Stores: 367ms
- Bing on Products: 591ms
- Googlebot on Categories: 338ms
- Bing on Categories: 467ms
- Googlebot on Products: 497ms

This is interesting data - it shows that bots are generally slower than humans on product pages (490-591ms for bots vs likely lower for humans), and categories are even slower for bots (466-621ms).

But Simon hasn't asked a question - he's just showing me the output. I should acknowledge that the query is working and ask what insight he's looking for, or wait for clarification on what he wants to do next.Query's working. Data shows bots are slower across the board—Google AI averaging 490–621ms depending on page type, while humans hit stores at 171ms. Googlebot and Bing both ~330–590ms.

What's the next step? Do you want to:

1. Filter to humans only to see organic user experience.
2. Exclude bots entirely from the view.
3. Compare bot slowness against a baseline or SLA threshold.
4. Drill into a specific bot or page type.
Query's working. Data shows bots are slower across the board—Google AI averaging 490–621ms depending on page type, while humans hit stores at 171ms. Googlebot and Bing both ~330–590ms.

What's the next step? Do you want to:

1. Filter to humans only to see organic user experience.
2. Exclude bots entirely from the view.
3. Compare bot slowness against a baseline or SLA threshold.
4. Drill into a specific bot or page type.

---

### 23. **Human** — 2026-04-20T00:34

requests
| where timestamp > ago(14d)
| extend UserAgent = tostring(parse_json(customDimensions).requestHeaders)
| extend BotType = case(
    UserAgent contains "Googlebot", "Googlebot",
    UserAgent contains "GPTBot", "OpenAI",
    UserAgent contains "Claude-Web", "Anthropic",
    UserAgent contains "Gemini", "Google AI",
    UserAgent contains "Bingbot", "Bing",
    UserAgent contains "Applebot", "Apple",
    "Human"
)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), BotType, UrlType
| order by timestamp asc
| render timechart

// Response time trend 
// Chart request duration over the last 12 hours. 
// To create an alert for this query, click '+ New alert rule'
requests
| where timestamp > ago(12h) 
| summarize avgRequestDuration=avg(duration) by bin(timestamp, 10m) // use a time grain of 10 minutes
| render timechart

is avg request duration the same as respojse time
requests
| where timestamp > ago(14d)
| extend UserAgent = tostring(parse_json(customDimensions).requestHeaders)
| extend BotType = case(
    UserAgent contains "Googlebot", "Googlebot",
    UserAgent contains "GPTBot", "OpenAI",
    UserAgent contains "Claude-Web", "Anthropic",
    UserAgent contains "Gemini", "Google AI",
    UserAgent contains "Bingbot", "Bing",
    UserAgent contains "Applebot", "Apple",
    "Human"
)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), BotType, UrlType
| order by timestamp asc
| render timechart

// Response time trend 
// Chart request duration over the last 12 hours. 
// To create an alert for this query, click '+ New alert rule'
requests
| where timestamp > ago(12h) 
| summarize avgRequestDuration=avg(duration) by bin(timestamp, 10m) // use a time grain of 10 minutes
| render timechart

is avg request duration the same as respojse time

---

### 24. **Claude** — 2026-04-20T00:34

The user is asking if "avg request duration" is the same as "response time". 

In the context of Application Insights (which this is), the `duration` field in the `requests` table represents the time taken for the request to complete, measured in milliseconds. This is typically what's referred to as "response time" or "request duration".

So yes, `avg(duration)` = average response time.

The user has two queries - one that's more granular (breaking down by bot type and URL type over 1-day bins), and one that's simpler (just average duration over 10-minute bins for the last 12 hours).

Both are measuring the same thing (response time via the duration field), but:
1. First query: avg duration grouped by day, bot type, and URL type
2. Second query: avg duration grouped by 10-minute intervals

So the answer is: yes, they're the same metric. The difference is just the grouping granularity and what dimensions you're breaking it down by.Yes. `avg(duration)` = average response time. Both queries measure the same thing—the `duration` field in requests is response time in milliseconds.

The difference:

- **First query**: Groups by day + bot type + URL type. Shows how each bot/page combo performs over time.
- **Second query**: Groups by 10-minute intervals. Finer granularity, no bot/page breakdowns—just overall trend.

For bot analysis, the first is better. For detecting spikes in real-time, the second (10m bins) catches them faster.
Yes. `avg(duration)` = average response time. Both queries measure the same thing—the `duration` field in requests is response time in milliseconds.

The difference:

- **First query**: Groups by day + bot type + URL type. Shows how each bot/page combo performs over time.
- **Second query**: Groups by 10-minute intervals. Finer granularity, no bot/page breakdowns—just overall trend.

For bot analysis, the first is better. For detecting spikes in real-time, the second (10m bins) catches them faster.

---

### 25. **Human** — 2026-04-20T00:34

can i do breakdown of page type by bots
can i do breakdown of page type by bots

---

### 26. **Claude** — 2026-04-20T00:34

The user is asking if they can show a breakdown of page type by bots - I think they mean they want to see the data visualized in a way that shows page types broken down by bots, or bots broken down by page types. Looking at their current query, it already does this - it groups by both BotType and UrlType.

However, the timechart render might be cramped with all those dimensions. They might want a different visualization or a different grouping structure. Let me suggest a few options:

1. Keep the current query but explain what it's showing
2. Pivot to show page types as rows and bots as columns
3. Use a different rendering (table, barchart, etc.)
4. Create separate queries for each view

Let me suggest the most useful options.Your current query already does this—it groups by both `BotType` and `UrlType`. The timechart just gets crowded with many lines.

For clearer breakdown, use a table instead:

```kusto
requests
| where timestamp > ago(14d)
| extend UserAgent = tostring(parse_json(customDimensions).requestHeaders)
| extend BotType = case(
    UserAgent contains "Googlebot", "Googlebot",
    UserAgent contains "GPTBot", "OpenAI",
    UserAgent contains "Claude-Web", "Anthropic",
    UserAgent contains "Gemini", "Google AI",
    UserAgent contains "Bingbot", "Bing",
    UserAgent contains "Applebot", "Apple",
    "Human"
)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgDuration = avg(duration), RequestCount = count() by BotType, UrlType
| order by AvgDuration desc
| render table
```

This pivots to show each bot/page combo as a row, with average duration and request count. Or pivot differently:

```kusto
| summarize AvgDuration = avg(duration) by BotType, UrlType
| render piechart
```

Which view do you prefer—table, timeline, or pivot chart?
Your current query already does this—it groups by both `BotType` and `UrlType`. The timechart just gets crowded with many lines.

For clearer breakdown, use a table instead:

```kusto
requests
| where timestamp > ago(14d)
| extend UserAgent = tostring(parse_json(customDimensions).requestHeaders)
| extend BotType = case(
    UserAgent contains "Googlebot", "Googlebot",
    UserAgent contains "GPTBot", "OpenAI",
    UserAgent contains "Claude-Web", "Anthropic",
    UserAgent contains "Gemini", "Google AI",
    UserAgent contains "Bingbot", "Bing",
    UserAgent contains "Applebot", "Apple",
    "Human"
)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgDuration = avg(duration), RequestCount = count() by BotType, UrlType
| order by AvgDuration desc
| render table
```

This pivots to show each bot/page combo as a row, with average duration and request count. Or pivot differently:

```kusto
| summarize AvgDuration = avg(duration) by BotType, UrlType
| render piechart
```

Which view do you prefer—table, timeline, or pivot chart?

---

### 27. **Human** — 2026-04-20T00:47

and over time?
and over time?

---

### 28. **Claude** — 2026-04-20T00:47

The user wants to see the breakdown by page type and bots over time. So they want a time series view that shows how each bot/page type combination performs across the 14 days. They could either:

1. Keep the timechart with all lines (it will be crowded)
2. Create a separate timechart for each bot type
3. Use a heatmap/matrix
4. Multiple stacked charts

The easiest is to either:
- Facet/split the timechart by BotType
- Or create multiple queries

In Kusto, they can use the existing query with timechart and it will show each BotType/UrlType combo as a separate line. But that might be too many lines.

They could also add a filter to focus on specific bots, or use a different visualization.

Let me suggest the timechart with faceting or just the straightforward approach of showing it split by bot type.Add the timestamp bin back:

```kusto
requests
| where timestamp > ago(14d)
| extend UserAgent = tostring(parse_json(customDimensions).requestHeaders)
| extend BotType = case(
    UserAgent contains "Googlebot", "Googlebot",
    UserAgent contains "GPTBot", "OpenAI",
    UserAgent contains "Claude-Web", "Anthropic",
    UserAgent contains "Gemini", "Google AI",
    UserAgent contains "Bingbot", "Bing",
    UserAgent contains "Applebot", "Apple",
    "Human"
)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgDuration = avg(duration) by bin(timestamp, 1d), BotType, UrlType
| order by timestamp asc
| render timechart
```

This is your original query. It plots each bot/page combo as a separate line over 14 days. Will be dense with ~18+ lines.

To declutter, filter to specific bots:

```kusto
| where BotType in ("Human", "Googlebot", "Google AI")
```

Or split by page type with separate charts:

```kusto
| where UrlType == "Product"
```

Which approach—see all bots at once, or focus on a subset?
Add the timestamp bin back:

```kusto
requests
| where timestamp > ago(14d)
| extend UserAgent = tostring(parse_json(customDimensions).requestHeaders)
| extend BotType = case(
    UserAgent contains "Googlebot", "Googlebot",
    UserAgent contains "GPTBot", "OpenAI",
    UserAgent contains "Claude-Web", "Anthropic",
    UserAgent contains "Gemini", "Google AI",
    UserAgent contains "Bingbot", "Bing",
    UserAgent contains "Applebot", "Apple",
    "Human"
)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgDuration = avg(duration) by bin(timestamp, 1d), BotType, UrlType
| order by timestamp asc
| render timechart
```

This is your original query. It plots each bot/page combo as a separate line over 14 days. Will be dense with ~18+ lines.

To declutter, filter to specific bots:

```kusto
| where BotType in ("Human", "Googlebot", "Google AI")
```

Or split by page type with separate charts:

```kusto
| where UrlType == "Product"
```

Which approach—see all bots at once, or focus on a subset?
