---
title: Screaming Frog exclusion list for parameter filtering
date: 2026-03-18
project: main
status: completed
score: 5/5
uuid: 143c91e7-b8d2-4bf0-b0ca-2cfe65198b41
---

#chat/light #project/main #status/completed #topic/plp #topic/regex #topic/screaming-frog #topic/shopify #topic/youtube

# Screaming Frog exclusion list for parameter filtering

- **Date:** [[2026-03-18]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 16
- **Chat URL:** https://claude.ai/chat/143c91e7-b8d2-4bf0-b0ca-2cfe65198b41
- **Medium view:** [[Chat/Medium/2026-03-18-screaming-frog-exclusion-list-for-parameter-filtering-143c91]]
- **Full transcript:** [[Chat/Full/2026-03-18-screaming-frog-exclusion-list-for-parameter-filtering-143c91]]

## Summary

**Conversation Overview**

The person is an SEO professional working on a Screaming Frog crawl configuration for thegoodguys.com.au, a large Australian retail site. They provided an existing exclusion list and a CSV file of queued URLs containing query string parameters, and asked Claude to audit the CSV and produce an updated, comprehensive exclusion list that covers all non-search parameters while explicitly preserving search-related params like `?q=`, `?searchTerm=`, `/DisplaySearch`, and `/SearchDisplay`.

Claude analysed the CSV to extract all query parameter keys and path patterns, then produced a merged exclusion list adding new rules across several categories: Algolia faceted navigation params (`sortBy`, `range%5B`), legacy WCS/HCL Commerce platform params (`storeId`, `catalogId`, `langId`, `krypto`, `beginIndex` and many others), Google Ads CQ auto-tag params (collapsed to `.*cq_.*=.*`), Particular Audience recommendation params, account/auth and order/transaction page patterns, and miscellaneous tracking params. The `refinementList` and `cf=` rules were subsequently removed at the person's request.

The person pushed back on unnecessary complexity twice: first requesting removal of specific rules, then asking Claude to deduplicate and simplify (e.g. collapsing all `cq_*` params into one wildcard rule). When Claude added `[?&]` anchors to query param patterns and over-explained the rationale, the person correctly challenged the logic — pointing out that the `=` sign already prevents false path matches, making `[?&]` redundant. Claude agreed and stripped it back to the simpler `.*param=.*` style throughout. The person's explicit preference is for straightforward, minimal regex with no over-engineering.

## First user message

> i need a screamingfrog exclusion list that covers params in here, except any search ones like ?search/q=  this is my current list:  https://analytics.thegoodguys.com.au/.* https://googleads.g.doubleclick.net/.* https://obseu.yougreencolumn.com/.* https://.*.snapchat.com/.* https://pixel.tapad.com/.* https://www.paypal.* https://www.google.com/maps.* .*maps.google.* https://recs-1a.particularaudien

## Topics

[[topic/plp]], [[topic/regex]], [[topic/screaming-frog]], [[topic/shopify]], [[topic/youtube]]

## Skills referenced

none detected
