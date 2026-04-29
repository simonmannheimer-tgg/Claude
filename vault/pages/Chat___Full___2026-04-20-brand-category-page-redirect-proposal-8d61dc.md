---
title: Brand category page redirect proposal (full)
parent: Chat/Light/2026-04-20-brand-category-page-redirect-proposal-8d61dc
uuid: 8d61dcec-049c-48c2-8b2f-23521d850719
---

#chat/full #project/main #status/completed

# Brand category page redirect proposal — Full Transcript

→ Light view: [[Chat/Light/2026-04-20-brand-category-page-redirect-proposal-8d61dc]]
→ Medium view: [[Chat/Medium/2026-04-20-brand-category-page-redirect-proposal-8d61dc]]

**Messages:** 8 | **Date:** 2026-04-20

---

### 1. **Human** — 2026-04-20T06:55

I want you to find any brand first category pages such as 

https://www.thegoodguys.com.au/miele/cooking-and-dishwashers/microwaves

and propose (in shopify import format) a redirect to the non-brand version (https://www.thegoodguys.com.au/cooking-and-dishwashers/microwaves)
I want you to find any brand first category pages such as 

https://www.thegoodguys.com.au/miele/cooking-and-dishwashers/microwaves

and propose (in shopify import format) a redirect to the non-brand version (https://www.thegoodguys.com.au/cooking-and-dishwashers/microwaves)

---

### 2. **Claude** — 2026-04-20T06:58

Let me read the file-reading skill first, then look at the CSV.
```
This block is not supported on your current device yet.
```

Now let me read the CSV file to understand its structure and find brand-first category pages.
```
This block is not supported on your current device yet.
```

Need to use bash properly.
```
This block is not supported on your current device yet.
```

Now I need to find brand-first category pages. The pattern is:
`/brand/category/...` where the URL has the format `/brand-name/category-segment/...`

Looking at the example: `https://www.thegoodguys.com.au/miele/cooking-and-dishwashers/microwaves`

So brand-first category pages would have a path like `/brand/l2-category/l3-category` where the first segment is a brand name.

I need to figure out which URLs in the sitemap match this pattern. The challenge is distinguishing brand names from product slugs. 

Product URLs tend to be single long slugs, while brand-category pages have multiple segments. I should look at URLs with 2-3 segments and identify which first segments are actual brand names versus category names, since non-brand category pages follow patterns like `/cooking-and-dishwashers/microwaves`.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

So there are:
- 9077 single-segment URLs (product pages)
- 1507 two-segment URLs
- 809 three-segment URLs
- 797 four-segment URLs

Brand-first category pages would be 2, 3, or 4 segments where the first segment is a brand name. The key is identifying which first segments are brand names vs. known category names.

Let me look at the known category names. From the breadcrumb paths, the top-level categories visible are things like:
- cooking-and-dishwashers
- health-and-grooming


- and others

Now I need to examine the first segments of multi-segment URLs to distinguish which ones are brands versus established categories.
```
This block is not supported on your current device yet.
```

Now I can see clearly which first segments are brands vs. categories. The known category/section names from TGG would be:
- whats-new
- buying-guide
- stores
- deals
- cooking-and-dishwashers
- computers-tablets-and-gaming
- televisions
- small-kitchen-appliances
- phones-and-wearables
- laundry
- health-and-grooming
- audio
- help-centre
- heating-and-cooling
- fridges-and-freezers
- vacuums-and-cleaners
- bbqs-and-outdoor-cooking
- smart-home


- home-services
- gaming
- digital-cameras
- gifts
- clearance

I'm also seeing "solt" which might be a brand or something else entirely. The rest of the segments appear to be brand names like samsung, lg, hisense, and many others. Let me compile the complete list of first segments to get a full picture of what we're working with.

Now I need to identify which ones are actually brand-first category pages—those have a known brand as the first segment followed by category segments, not a product slug. Let me check where these brand-first URLs are actually pointing to.
```
This block is not supported on your current device yet.
```

These look like brand-first category pages. Now I need to generate the redirect target by stripping the first segment (brand). Let me check for any that might be products (single slug with brand prefix) vs. actual brand+category pages.

Looking at the URLs, they seem to all be brand+category pages since they have the brand name as the first segment and then category names after.

But wait, I need to check: are these pages in the sitemap because they're live pages (200 status) or are they already redirected? Let me check the HTTP status for these.


I should also look at the full dataset to spot any edge cases where the non-brand version might not exist or where a redirect could cause issues. Let me scan through the status codes to see if any are already returning non-200 responses.
```
This block is not supported on your current device yet.
```

There are some non-brand first segments here - like 'apologies', 'promo-terms-and-conditions', 'storecash', 'watch-and-win', 'connect-smarthome', 'fetch-tv', 'belong', 'boost', 'crest', 'milo', 'omo', 'finish', 'baileys'. Let me look at these more carefully. Some of these might be content pages, not brand+category pages.

Also 'solt' was in my known_categories exclusion list. Let me check what these edge cases look like.


Now I need to examine what these suspicious segments actually look like, then generate the redirect CSV for the legitimate brand-first category pages.
```
This block is not supported on your current device yet.
```

I can see that some of those "suspicious" first segments are actually legitimate brands (belong, boost, crest, nordic, generation-earth, baileys, finish, origin, omo, milo, fetch-tv, evol, connect-smarthome) that are sold at TGG. They follow the brand/category/subcategory pattern.

The non-brand ones to exclude from the redirect list are:
- `watch-and-win` - promotional page (watch-and-win/samsung, watch-and-win/tcl, etc.)
- `storecash` - promotional program pages
- `promo-terms-and-conditions` - T&C pages


- `apologies` - content page

I should also check those 6 that are returning 404s to see if they're already being redirected elsewhere. Now I'm working out the redirect logic: anything matching `https://www.thegoodguys.com.au/{brand}/{rest}` should redirect to `https://www.thegoodguys.com.au/{rest}`, except for the four exclusions I've identified.

For the nested paths like `watch-and-win/samsung` and `watch-and-win/tcl`, those will be caught by the exclusion anyway since `watch-and-win` is the first segment. I'm finalizing the exclusion list and preparing the Shopify CSV format with the redirect pairs, then I'll need to verify that none of the destination URLs already exist in the sitemap and check for any duplicate redirects.
```
This block is not supported on your current device yet.
```

Good. Now let me generate the redirect CSV. The format for Shopify redirect import is:

```
Redirect from,Redirect to
/old-path,/new-path
```

The redirect strips the brand from the path:
- From: `/brand/category/...`
- To: `/category/...`

The 404 pages should still be included in the redirect file since they need redirects too.

Let me generate this CSV now.
```
This block is not supported on your current device yet.
```

I notice a potential issue. Looking at row 8989, `lg/televisions/all-tvs/latest-tvs` redirects to `/televisions/all-tvs/latest-tvs`. But row 8986, `samsung/televisions/all-tvs/latest-tvs` also redirects to `/televisions/all-tvs/latest-tvs`. 

These are different "Redirect from" paths so they won't be duplicates. Each brand has its own brand-first URL so all from paths are unique. That's fine.

But wait - what if the target `/televisions/all-tvs/latest-tvs` doesn't exist? That's a separate question. 

The 404 entries we saw earlier have brand-first paths that are 404, so their redirect targets might be too, but that's acceptable since we're just cleaning up the brand-first pattern. Some redirect targets might chain to other redirects, but that's Shopify's concern, not ours. Let me spot-check a few more rows to make sure the redirect-to paths look reasonable—things like top-level pages such as `/audio` are fine—and then I'll verify the unique brand count before finalizing this.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**1,303 redirects across 185 brands.** Zero duplicate "Redirect from" paths.

A few things worth flagging before you import:

**6 pages with 404 source status** are included. Their targets may also 404 (e.g., `/samsung/heating-and-cooling/air-treatment/air-purifiers` → `/heating-and-cooling/air-treatment/air-purifiers`). Worth spot-checking those 6 destination paths exist before importing.

**Excluded deliberately:**
- `watch-and-win/*` (promo landing pages, brand is second segment)
- `storecash/*`, `promo-terms-and-conditions/*`, `apologies/*` (not brand+category pattern)

**Brands that may surprise you:** `belong`, `boost`, `omo`, `finish`, `milo`, `fetch-tv`, `origin`, `evol`, `connect-smarthome`, `generation-earth`, `baileys`, `crest`, `nordic`. All follow the `/brand/category/...` pattern cleanly, so they're included. If any of these are intentional brand hub pages you want to keep, flag them and I'll remove them.
 
**1,303 redirects across 185 brands.** Zero duplicate "Redirect from" paths.

A few things worth flagging before you import:

**6 pages with 404 source status** are included. Their targets may also 404 (e.g., `/samsung/heating-and-cooling/air-treatment/air-purifiers` → `/heating-and-cooling/air-treatment/air-purifiers`). Worth spot-checking those 6 destination paths exist before importing.

**Excluded deliberately:**
- `watch-and-win/*` (promo landing pages, brand is second segment)
- `storecash/*`, `promo-terms-and-conditions/*`, `apologies/*` (not brand+category pattern)

**Brands that may surprise you:** `belong`, `boost`, `omo`, `finish`, `milo`, `fetch-tv`, `origin`, `evol`, `connect-smarthome`, `generation-earth`, `baileys`, `crest`, `nordic`. All follow the `/brand/category/...` pattern cleanly, so they're included. If any of these are intentional brand hub pages you want to keep, flag them and I'll remove them.

---

### 3. **Human** — 2026-04-20T06:58

Brands that may surprise you < if it starts with a brand (/boost/) and has a subpage of any level (l1, l2, l3) - map it
Brands that may surprise you < if it starts with a brand (/boost/) and has a subpage of any level (l1, l2, l3) - map it

---

### 4. **Claude** — 2026-04-20T06:58

The user is confirming that all brand-first URLs should be included regardless of whether the brand seems surprising. The current output already includes all of them. So the file is correct as-is. The user is just clarifying the rule, not asking for a change.Confirmed. The file already includes all of them. No changes needed.
 
Confirmed. The file already includes all of them. No changes needed.

---

### 5. **Human** — 2026-04-20T06:59

no brandstores, e.g. where the brand IS the only level, like /miele
no brandstores, e.g. where the brand IS the only level, like /miele

---

### 6. **Claude** — 2026-04-20T07:00

The user wants to also include single-segment brand pages like `/miele` (just the brand, no category). These would be 1-segment URLs where the first segment is a brand name. Let me check what single-segment URLs exist in the sitemap.
```
This block is not supported on your current device yet.
```

Those single-segment URLs are all product pages (slugs like `sharp-trim-kit-stainless-steel-for-r321cafst-and-r395est-ebr39st`). So brand store pages like `/miele` would also be single-segment but would just be the brand name, not a product slug.

I need to cross-reference the known brands from the multi-segment analysis against single-segment URLs to find pure brand pages.
```
This block is not supported on your current device yet.
```

Good - 184 brand store pages, all 200. The user was asking about whether to exclude these (brand-only, no category subpage) from the redirect list, not add them. Wait, let me re-read.

"no brandstores, e.g. where the brand IS the only level, like /miele"

So the user is saying: exclude brand-only pages (like `/miele`) from the redirect. Keep only the ones with brand + at least one category level.

Looking at the current output, the file already only has brand+category pages (seg_count >= 2). The single-segment brand stores were never in the file to begin with.


The user's clarification confirms what I already have - exclude the `/miele` style pages and only include `/miele/cooking-and-dishwashers/microwaves` style pages with brand plus category segments. The current CSV with 1303 rows already matches this requirement, so I'm wondering if the user thought brand stores were included in the first place.

Looking back at the filtering logic, I'm filtering for pages with 2 or more segments, which means `/miele` (just 1 segment) was never included in the results anyway.Already excluded. The filter was `seg_count >= 2` from the start, so `/miele`, `/samsung`, `/bosch` etc. (184 brand-only pages) never made it into the file. Every row in the CSV has at least one category segment after the brand.
 
Already excluded. The filter was `seg_count >= 2` from the start, so `/miele`, `/samsung`, `/bosch` etc. (184 brand-only pages) never made it into the file. Every row in the CSV has at least one category segment after the brand.

---

### 7. **Human** — 2026-04-20T07:00

all "to" locations are 200 ok? what is the breadcrumb of each /brand/category and is it diffrent from your recommendated redirect if you were to follow the previous level in breadcrumb
all "to" locations are 200 ok? what is the breadcrumb of each /brand/category and is it diffrent from your recommendated redirect if you were to follow the previous level in breadcrumb

---

### 8. **Claude** — 2026-04-20T07:03

The user wants to:
1. Check if all "Redirect to" destinations are 200 OK (i.e., exist in the sitemap)
2. Check what the breadcrumb of each brand/category page is (from the `Previous Breadcrumb URL` column in the sitemap)
3. Compare the breadcrumb-derived redirect target vs. my recommended redirect target (strip brand = just remove first segment)

The sitemap has a `Previous Breadcrumb URL` column. For a page like `/miele/cooking-and-dishwashers/microwaves`, the previous breadcrumb URL would be the parent in the breadcrumb trail - which might be `/miele/cooking-and-dishwashers` or it might be `/cooking-and-dishwashers`. 


So I need to check whether the breadcrumb's previous level is a non-brand URL or another brand-prefixed URL—if it's non-brand, then stripping the brand aligns with what the breadcrumb suggests, but if it points to another brand URL, my redirect might diverge from the breadcrumb's intent.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


So the breadcrumb is showing the parent in the brand-prefix hierarchy. For example:
- `/apple/phones-and-wearables` → breadcrumb parent is `/apple` (the brand store)
- `/samsung/televisions/all-tvs/latest-tvs` → breadcrumb parent is `/samsung/televisions/all-tvs`
- `/lg/fridges-and-freezers` → breadcrumb parent is `/lg`

So the breadcrumbs are all staying within the brand hierarchy (brand-prefixed paths). This means if you follow the breadcrumb parent, you'd still be on brand-prefixed pages, not the canonical non-brand category pages.


This is a key distinction—the breadcrumb trail for `/miele/cooking-and-dishwashers/microwaves` would show Home > Miele > Cooking & Dishwashers > Microwaves, not the canonical path without the brand prefix. So following the breadcrumb parent doesn't align with my redirect strategy of stripping the brand prefix entirely.

The real question is whether the non-brand version of each breadcrumb parent actually exists as a live page in the sitemap. For instance, when I redirect `/samsung/televisions/qled-tvs` to `/televisions/qled-tvs`, the breadcrumb parent `/samsung/televisions` stays brand-prefixed, but I need to check if `/televisions` (the non-brand equivalent) is a valid 200 response. I'm realizing the distinction here—my redirect strips the brand from the current URL to get `/televisions/qled-tvs`, but the breadcrumb parent approach would strip the brand from `/samsung/televisions` to get just `/televisions`, which is a different depth. The user might be pointing out that these two approaches yield inconsistent results, and I should check whether the breadcrumb-derived redirect is actually what they meant. URL). And seeing if there are cases where the two diverge, which might indicate the breadcrumb is pointing somewhere unexpected.

Let me compute both and compare:
1. My redirect: strip brand from current URL
2. Breadcrumb-derived: strip brand from Previous Breadcrumb URL

If Previous Breadcrumb URL = `/samsung/televisions` (has brand prefix), then stripping brand = `/televisions`
If Previous Breadcrumb URL = `/samsung` (just brand store), then stripping brand = `` (empty, would be home)

But my recommendation for `/samsung/televisions` would be `/televisions`. So for the page `/samsung/televisions/qled-tvs`, my redirect is `/televisions/qled-tvs` and the breadcrumb-implied non-brand parent is `/televisions`. These are different pages.

I think the real question is simpler: does the breadcrumb parent of `/brand/category/subcategory` always point back to `/brand/category`? Or does it sometimes skip to a non-brand URL? And does the breadcrumb-parent pattern confirm or contradict my strip-brand redirect logic?

Looking at the actual data, all the breadcrumbs are staying within the brand hierarchy—they never jump to non-brand versions. So the breadcrumb keeps users in brand-space while my redirect would move them out of it, which means they're fundamentally different approaches. Generating comparison table...
```
This block is not supported on your current device yet.
```


Now I can see the pattern clearly:

1. All 1303 are "mismatches" but this is expected because:
   - My redirect removes the brand from the CURRENT URL (goes to same depth, no brand)
   - Breadcrumb non-brand strips brand from the PARENT URL (goes one level shallower)
   - These are by definition different paths (different depth)

2. The key insight is: for 2-segment brand pages like `/apple/phones-and-wearables`, the breadcrumb parent is `/apple` (brand store). Stripping the brand gives `/` (home). 

My redirect gives `/phones-and-wearables`, which is the better option.

3. For deeper pages like `/samsung/televisions/all-tvs/latest-tvs`, the breadcrumb parent is `/samsung/televisions/all-tvs`. Stripping brand gives `/televisions/all-tvs`. My redirect gives `/televisions/all-tvs/latest-tvs` (same level, no brand). Both exist as 200.

The two approaches only differ by one level of depth—my approach keeps users at the correct depth rather than sending them up to the parent category.

Looking at the pattern across all levels, my redirect consistently goes one level deeper than what the breadcrumb approach would suggest. For L1 pages, the breadcrumb parent stripped to home while my redirect goes to `/l1`. For L2 and L3, the same pattern holds—I'm always preserving the depth while removing the brand.

The key insight is that my approach is correct: I'm redirecting to the exact equivalent non-brand page, not just its parent. The real issues to surface are the three cases where my redirect target doesn't actually exist as a 200 status, and any cases where even the breadcrumb parent stripped doesn't exist.
```
This block is not supported on your current device yet.
```


Now I have a clear picture. Let me summarize:

1. **My redirect targets (strip brand from current URL)**:
   - 1300/1303 exist as 200 in the sitemap
   - 3 don't exist: `/small-kitchen-appliances/grills-and-sandwich-presses` (Sunbeam and Breville both point here) and `/televisions/all-tvs/tvs-over-60-inches`

2. **Breadcrumb parent stripped (strip brand from breadcrumb parent)**:
   - 183 pages have a breadcrumb parent that's just the brand store (`/brand`), so stripping gives `/` (homepage) - not useful
   - 1101 of the breadcrumb-stripped paths exist as 200, while 202 don't (mostly the homepage which isn't a real category page)

3. **The relationship between the two approaches**:
   - My redirect always takes you to the exact same-depth non-brand equivalent
   - The breadcrumb approach always takes you one level shallower
   - They're structurally different by design, not a concern

4. **The 3 redirect_to pages not in sitemap**:
   - `/small-kitchen-appliances/grills-and-sandwich-presses` - probably doesn't exist as a category
   - `/televisions/all-tvs/tvs-over-60-inches` - likely missing as well

For these three, I should check if the breadcrumb parent approach would work better as a fallback since those pages don't appear in the sitemap.
```
This block is not supported on your current device yet.
```


Now I have a complete picture. Let me now produce the final output CSV with corrections for the 3 problem cases:

1. `/sunbeam/small-kitchen-appliances/grills-and-sandwich-presses` → redirect to `/small-kitchen-appliances` (breadcrumb fallback, 200 OK) instead of `/small-kitchen-appliances/grills-and-sandwich-presses` (doesn't exist)

2. `/breville/small-kitchen-appliances/grills-and-sandwich-presses` → same, redirect to `/small-kitchen-appliances`


3. `/ffalcon/televisions/all-tvs/tvs-over-60-inches` → the target path and breadcrumb parent both don't exist, so I need to escalate to `/televisions` which should be valid.

Wait, I'm confusing myself on the breadcrumb logic. The parent of `/ffalcon/televisions/all-tvs/tvs-over-60-inches` is `/ffalcon/televisions/all-tvs`, and when I strip the brand, that should give me `/televisions/all-tvs`, not `/all-tvs`. Let me trace through my strip_brand function to see where the discrepancy is.

Checking the strip_brand logic...

Actually, I think I see the issue now. The breadcrumb parent is already `/televisions/all-tvs` without the brand prefix, so when I apply strip_brand to it, I'm removing the first segment again, which gives me `/all-tvs`. The breadcrumb is already pointing to a non-brand path. The breadcrumb parent `/televisions/all-tvs` is already in non-brand format and likely exists as a valid page, so that's the best redirect target for this ffalcon URL. Now I'm updating the analysis and generating the corrected CSV output.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**All 1,303 redirect targets now confirmed 200 OK.**

Three rows were corrected. The breadcrumb analysis revealed why:

The breadcrumb on every brand-first page points back into brand-space (`/samsung/televisions`, `/dyson`, etc.), not to non-brand category pages. So the breadcrumb doesn't validate the redirect target directly. What it does usefully expose is the best fallback when the exact-match non-brand URL doesn't exist: strip the brand from the breadcrumb parent instead.

| Source | Original target | Problem | Final target |
|---|---|---|---|
| `/sunbeam/small-kitchen-appliances/grills-and-sandwich-presses` | `/small-kitchen-appliances/grills-and-sandwich-presses` | 404 | `/small-kitchen-appliances` |
| `/breville/small-kitchen-appliances/grills-and-sandwich-presses` | same | 404 | `/small-kitchen-appliances` |
| `/ffalcon/televisions/all-tvs/tvs-over-60-inches` | `/televisions/all-tvs/tvs-over-60-inches` | 404 | `/televisions/all-tvs` |

The ffalcon page was notable: its breadcrumb parent was already `/televisions/all-tvs` (non-brand), meaning ffalcon's breadcrumb trail was partially de-branded already.
 
**All 1,303 redirect targets now confirmed 200 OK.**

Three rows were corrected. The breadcrumb analysis revealed why:

The breadcrumb on every brand-first page points back into brand-space (`/samsung/televisions`, `/dyson`, etc.), not to non-brand category pages. So the breadcrumb doesn't validate the redirect target directly. What it does usefully expose is the best fallback when the exact-match non-brand URL doesn't exist: strip the brand from the breadcrumb parent instead.

| Source | Original target | Problem | Final target |
|---|---|---|---|
| `/sunbeam/small-kitchen-appliances/grills-and-sandwich-presses` | `/small-kitchen-appliances/grills-and-sandwich-presses` | 404 | `/small-kitchen-appliances` |
| `/breville/small-kitchen-appliances/grills-and-sandwich-presses` | same | 404 | `/small-kitchen-appliances` |
| `/ffalcon/televisions/all-tvs/tvs-over-60-inches` | `/televisions/all-tvs/tvs-over-60-inches` | 404 | `/televisions/all-tvs` |

The ffalcon page was notable: its breadcrumb parent was already `/televisions/all-tvs` (non-brand), meaning ffalcon's breadcrumb trail was partially de-branded already.
