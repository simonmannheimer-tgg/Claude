---
title: Screaming Frog exclusion list for parameter filtering (full)
parent: Chat/Light/2026-03-18-screaming-frog-exclusion-list-for-parameter-filtering-143c91
uuid: 143c91e7-b8d2-4bf0-b0ca-2cfe65198b41
---

#chat/full #project/main #status/completed

# Screaming Frog exclusion list for parameter filtering — Full Transcript

→ Light view: [[Chat/Light/2026-03-18-screaming-frog-exclusion-list-for-parameter-filtering-143c91]]
→ Medium view: [[Chat/Medium/2026-03-18-screaming-frog-exclusion-list-for-parameter-filtering-143c91]]

**Messages:** 16 | **Date:** 2026-03-18

---

### 1. **Human** — 2026-03-18T09:33

i need a screamingfrog exclusion list that covers params in here, except any search ones like ?search/q=

this is my current list:

https://analytics.thegoodguys.com.au/.*
https://googleads.g.doubleclick.net/.*
https://obseu.yougreencolumn.com/.*
https://.*.snapchat.com/.*
https://pixel.tapad.com/.*
https://www.paypal.*
https://www.google.com/maps.*
.*maps.google.*
https://recs-1a.particularaudience.com/.*
https://truerewards.com.au/.*
https://use.typekit.net/.*
https://www.google-analytics.com/.*
https://www.googleadservices.com/.*
https://www.youtube.com/.*
https://cdn.shopify.com/.*.pdf.*
.*AjaxLogonForm.*
.*utm_.*=.*
.*ga_.*=.*
.*gclid=.*
.*fbclid=.*
.*cid=.*
.*scid=.*
.*ecid=.*
.*mcid=.*
.*?gStoreCode=.*
.*campaign=.*
.*ref=.*
.*referrer=.*
.*source=.*
.*session=.*
.*sid=.*
.*phpsessid=.*
.*sess=.*
.*id=.*
.*nid=.*
.*pid=.*
.*sku=.*
.*productId=.*
.*PayOnlineView.*
.*AjaxOrderItemDisplayView.*
.*pageno=.*
.*pagenum=.*
.*sort=.*
.*order=.*
.*filter=.*
.*store=.*
.*branch=.*
.*location=.*
.*track=.*
.*tracking=.*
.*trace=.*
.*commercial.thegoodguys.com.au.*
.*?_ga=.*
.*checkout.thegoodguys.com.au/web-pixels.*
.*web-pixel.*
.*wpm@.*
https://www.thegoodguys.com.au/payonline/verify?hash=.*
i need a screamingfrog exclusion list that covers params in here, except any search ones like ?search/q=

this is my current list:

https://analytics.thegoodguys.com.au/.*
https://googleads.g.doubleclick.net/.*
https://obseu.yougreencolumn.com/.*
https://.*.snapchat.com/.*
https://pixel.tapad.com/.*
https://www.paypal.*
https://www.google.com/maps.*
.*maps.google.*
https://recs-1a.particularaudience.com/.*
https://truerewards.com.au/.*
https://use.typekit.net/.*
https://www.google-analytics.com/.*
https://www.googleadservices.com/.*
https://www.youtube.com/.*
https://cdn.shopify.com/.*.pdf.*
.*AjaxLogonForm.*
.*utm_.*=.*
.*ga_.*=.*
.*gclid=.*
.*fbclid=.*
.*cid=.*
.*scid=.*
.*ecid=.*
.*mcid=.*
.*?gStoreCode=.*
.*campaign=.*
.*ref=.*
.*referrer=.*
.*source=.*
.*session=.*
.*sid=.*
.*phpsessid=.*
.*sess=.*
.*id=.*
.*nid=.*
.*pid=.*
.*sku=.*
.*productId=.*
.*PayOnlineView.*
.*AjaxOrderItemDisplayView.*
.*pageno=.*
.*pagenum=.*
.*sort=.*
.*order=.*
.*filter=.*
.*store=.*
.*branch=.*
.*location=.*
.*track=.*
.*tracking=.*
.*trace=.*
.*commercial.thegoodguys.com.au.*
.*?_ga=.*
.*checkout.thegoodguys.com.au/web-pixels.*
.*web-pixel.*
.*wpm@.*
https://www.thegoodguys.com.au/payonline/verify?hash=.*

---

### 2. **Claude** — 2026-03-18T09:34

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now I have a complete picture. Let me build the exclusion list.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's what was added and why, grouped by source:

**Algolia faceted nav** (4,605 occurrences). `refinementList`, `range%5B`, `sortBy` — all filter/facet params from the Algolia PLP layer. These generate massive URL duplication.

**Legacy WCS/HCL Commerce params** (high volume). `storeId`, `catalogId`, `langId`, `categoryId`, `catentryId`, `krypto`, `beginIndex`, `pageSize`, `orderBy`, `searchSource`, `compareReturnName`, `returnUrl` and a dozen more — all from the old Commerce platform, still appearing in compare/search views.

**CQ Google Ads auto-tag params** (~4,400 combined). The full `cq_src`, `cq_cmp`, `cq_term`, `cq_med`, `cq_net`, `cq_pos`, `cq_plt`, `cq_loci`, `cq_locp`, `cq_mtype`, `cq_dvic`, `cq_dvicm`, `cq_trg`, `cq_pdid`, `cq_con` family. These appear as arrays with `[0]`, `[1]` suffixes — covered by the wildcard pattern.

**Pay/verify pages** (3,705 `hash=` occurrences). The existing rule used a literal `?` which Screaming Frog may not interpret as a regex anchor. Replaced with `.*payonline/verify.*hash=.*` for reliability.

**Account/auth** — `LogonForm`, `ResetPasswordForm`, `account/login`, `checkout_url`, `validationCode`, `token`.

**Order/transaction** — `OrderShippingBillingConfirmationView`, `orderId`, `workorderno`, `storeDocketNumber`.

**Particular Audience** — `istItemId`, `istCompanyId`, `istFeedId`, `istBi`, `patest`, `rrec`.

**Pagination** — `page=` (729 occurrences, distinct from `pageno`/`pagenum` already in your list).

**Preserved as intended:** `/search?q=`, `/search?searchTerm=`, `/DisplaySearch?searchTerm=`, `/SearchDisplay?searchTerm=` — none of those are excluded.
Now I have a complete picture. Let me build the exclusion list.
Here's what was added and why, grouped by source:

**Algolia faceted nav** (4,605 occurrences). `refinementList`, `range%5B`, `sortBy` — all filter/facet params from the Algolia PLP layer. These generate massive URL duplication.

**Legacy WCS/HCL Commerce params** (high volume). `storeId`, `catalogId`, `langId`, `categoryId`, `catentryId`, `krypto`, `beginIndex`, `pageSize`, `orderBy`, `searchSource`, `compareReturnName`, `returnUrl` and a dozen more — all from the old Commerce platform, still appearing in compare/search views.

**CQ Google Ads auto-tag params** (~4,400 combined). The full `cq_src`, `cq_cmp`, `cq_term`, `cq_med`, `cq_net`, `cq_pos`, `cq_plt`, `cq_loci`, `cq_locp`, `cq_mtype`, `cq_dvic`, `cq_dvicm`, `cq_trg`, `cq_pdid`, `cq_con` family. These appear as arrays with `[0]`, `[1]` suffixes — covered by the wildcard pattern.

**Pay/verify pages** (3,705 `hash=` occurrences). The existing rule used a literal `?` which Screaming Frog may not interpret as a regex anchor. Replaced with `.*payonline/verify.*hash=.*` for reliability.

**Account/auth** — `LogonForm`, `ResetPasswordForm`, `account/login`, `checkout_url`, `validationCode`, `token`.

**Order/transaction** — `OrderShippingBillingConfirmationView`, `orderId`, `workorderno`, `storeDocketNumber`.

**Particular Audience** — `istItemId`, `istCompanyId`, `istFeedId`, `istBi`, `patest`, `rrec`.

**Pagination** — `page=` (729 occurrences, distinct from `pageno`/`pagenum` already in your list).

**Preserved as intended:** `/search?q=`, `/search?searchTerm=`, `/DisplaySearch?searchTerm=`, `/SearchDisplay?searchTerm=` — none of those are excluded.

---

### 3. **Human** — 2026-03-18T09:35

remove any refinementlist or ?cf
remove any refinementlist or ?cf

---

### 4. **Claude** — 2026-03-18T09:35

```
This block is not supported on your current device yet.
```

---

### 5. **Human** — 2026-03-18T09:35

deduplicate - e.g. .*cq_.*

keep simple
deduplicate - e.g. .*cq_.*

keep simple

---

### 6. **Claude** — 2026-03-18T09:35

```
This block is not supported on your current device yet.
```

---

### 7. **Human** — 2026-03-18T09:35

no comments, sort logically
no comments, sort logically

---

### 8. **Claude** — 2026-03-18T09:36

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done. Key consolidations made:

- All 16 `cq_*` params collapsed to `.*[?&]cq_.*=.*`
- `ist*` params (4) kept individual — too distinct to wildcard safely
- `page`, `pageno`, `pagenum`, `pageSize`, `pageView` kept separate as they match different things
- Existing `.*sort=.*`, `.*order=.*`, `.*filter=.*` etc. from your original list were superseded by the more precise `[?&]` anchored versions and removed to avoid redundancy
 
Done. Key consolidations made:

- All 16 `cq_*` params collapsed to `.*[?&]cq_.*=.*`
- `ist*` params (4) kept individual — too distinct to wildcard safely
- `page`, `pageno`, `pagenum`, `pageSize`, `pageView` kept separate as they match different things
- Existing `.*sort=.*`, `.*order=.*`, `.*filter=.*` etc. from your original list were superseded by the more precise `[?&]` anchored versions and removed to avoid redundancy

---

### 9. **Human** — 2026-03-18T09:37

whats [?&] and why did you add it?
whats [?&] and why did you add it?

---

### 10. **Claude** — 2026-03-18T09:37

It's a regex character class matching either `?` or `&`. The idea was to anchor the pattern so it only matches when the param appears as an actual query string key — not when the string appears anywhere else in the URL path.

For example, `.*id=.*` (your original style) would also match URLs like `/products/solid-state-drive/...` or `/brands/android/...` because `id` appears mid-word. The `[?&]` prefix tightens it to only fire when `id` follows the start of the query string or a param separator.

That said — Screaming Frog's exclude field matches against the full URL string, so the looser `.*id=.*` style from your original list would catch those mid-path false positives. Worth knowing, but in practice most of your original params (`sid`, `pid`, `nid` etc.) are unlikely to appear in TGG's clean URL paths anyway, so it's a minor distinction.

Want me to revert to the simpler `.*param=.*` style throughout for consistency with your original list?
 It's a regex character class matching either `?` or `&`. The idea was to anchor the pattern so it only matches when the param appears as an actual query string key — not when the string appears anywhere else in the URL path.

For example, `.*id=.*` (your original style) would also match URLs like `/products/solid-state-drive/...` or `/brands/android/...` because `id` appears mid-word. The `[?&]` prefix tightens it to only fire when `id` follows the start of the query string or a param separator.

That said — Screaming Frog's exclude field matches against the full URL string, so the looser `.*id=.*` style from your original list would catch those mid-path false positives. Worth knowing, but in practice most of your original params (`sid`, `pid`, `nid` etc.) are unlikely to appear in TGG's clean URL paths anyway, so it's a minor distinction.

Want me to revert to the simpler `.*param=.*` style throughout for consistency with your original list?

---

### 11. **Human** — 2026-03-18T09:38

but .*ga=.* would do tht too
but .*ga=.* would do tht too

---

### 12. **Claude** — 2026-03-18T09:38

You're right. `[?&]` only helps if the pattern is otherwise ambiguous — like `.*id=.*` matching `/solid-state-drive/`. But `.*ga=.*` vs `.*[?&]ga=.*` makes no practical difference since `ga=` won't appear in a TGG path anyway.

The only cases where it actually matters are the short/common ones — `id`, `page`, `code`, `ref`, `source`, `token`, `hash`, `cr`, `fm`, `tp`, `hl`, `pi`, `pp` — where the string could plausibly appear in a URL path or product name.

Want me to strip `[?&]` back out and just use `.*param=.*` throughout for consistency?
 You're right. `[?&]` only helps if the pattern is otherwise ambiguous — like `.*id=.*` matching `/solid-state-drive/`. But `.*ga=.*` vs `.*[?&]ga=.*` makes no practical difference since `ga=` won't appear in a TGG path anyway.

The only cases where it actually matters are the short/common ones — `id`, `page`, `code`, `ref`, `source`, `token`, `hash`, `cr`, `fm`, `tp`, `hl`, `pi`, `pp` — where the string could plausibly appear in a URL path or product name.

Want me to strip `[?&]` back out and just use `.*param=.*` throughout for consistency?

---

### 13. **Human** — 2026-03-18T09:38

like `.*id=.*` matching `/solid-state-drive/`. unless theres a = in the url after id no?
like `.*id=.*` matching `/solid-state-drive/`. unless theres a = in the url after id no?

---

### 14. **Claude** — 2026-03-18T09:38

Correct — the `=` already anchors it. `/solid-state-drive/` has no `=` so `.*id=.*` wouldn't match it. I overcomplicated it.

The `[?&]` adds nothing useful. Want me to strip it back to `.*param=.*` throughout?
 Correct — the `=` already anchors it. `/solid-state-drive/` has no `=` so `.*id=.*` wouldn't match it. I overcomplicated it.

The `[?&]` adds nothing useful. Want me to strip it back to `.*param=.*` throughout?

---

### 15. **Human** — 2026-03-18T09:39

yeah keep it simple stupid
yeah keep it simple stupid

---

### 16. **Claude** — 2026-03-18T09:39

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done.
Done.
