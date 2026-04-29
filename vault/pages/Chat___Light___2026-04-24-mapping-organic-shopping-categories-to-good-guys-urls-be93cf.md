---
title: Mapping organic shopping categories to Good Guys URLs
date: 2026-04-24
project: main
status: active
score: 5/5
uuid: be93cf2e-ef97-4750-95ba-09f42bec990a
---

#chat/light #project/main #status/active #topic/deals #topic/eofy #topic/feed #topic/gsc #topic/keyword #topic/redirect #topic/regex #topic/shopify

# Mapping organic shopping categories to Good Guys URLs

- **Date:** [[2026-04-24]]
- **Project:** [[Projects/main]]
- **Status:** #status/active (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 51
- **Chat URL:** https://claude.ai/chat/be93cf2e-ef97-4750-95ba-09f42bec990a
- **Medium view:** [[Chat/Medium/2026-04-24-mapping-organic-shopping-categories-to-good-guys-urls-be93cf]]
- **Full transcript:** [[Chat/Full/2026-04-24-mapping-organic-shopping-categories-to-good-guys-urls-be93cf]]

## Summary

**Conversation Overview**

Simon is working on an organic shopping analytics project for The Good Guys (thegoodguys.com.au), an Australian electronics and appliance retailer. The goal is to map GMC (Google Merchant Center) organic shopping clicks and impressions to specific deals page URLs (e.g., `/deals/tvs`, `/deals/washing-machines`) so the team can understand which deal pages are driving organic shopping performance. Simon is working with multiple data files: GMC feed exports (June 2025 and a current 28-day window, Mar 27–Apr 23 2026), a Shopify products export, and a GSC page+query report.

The work progressed through several iterations of increasing sophistication. Claude initially mapped GMC L1/L2/L3 category data to deals slugs, then attempted SKU-level matching against the products export (which proved unreliable due to the export only containing ~3,560 products versus a much larger live catalogue). Claude then built a multi-layer mapping approach: TGG breadcrumb (from the products export, via VLOOKUP) as the primary signal, product title keyword matching as a secondary layer, and GMC L1/L2/L3 categories as fallback. Simon requested the title matching be derived from actual GSC query data showing what queries each deals page had ranked for or received clicks on, rather than hand-crafted rules. A key bug was identified where `"washer"` in `"dishwasher"` was incorrectly matching the washing-machines rule before the dishwashers rule could fire — fixed by reordering slug priority. Simon also flagged that the formula-driven workbook was returning zeros because Excel wasn't recalculating on open, and that kitchen-appliances was showing no clicks despite being a live page. Claude attempted to scrape all 23 deals pages to get ground-truth product type data, discovering that the SKU extraction pattern (`files/(\d{8})_\d+` from preloaded images) and a product title pattern from the React Router stream (`\"(\d{8})\",\"([^\"]{10,120})\"`) both worked via curl against the SSR HTML.

The final deliverable structure is a multi-tab Excel workbook: Raw GMC tab (12,743 rows, one per Product ID per period), Products tab (SKU/model → TGG breadcrumb lookup), Title Rules tab (keyword rules derived from GSC query data), Query-Derived Keywords tab (per-slug keyword sets from actual ranking queries), and Category Mapping tab (one row per unique Product ID with VLOOKUP for TGG breadcrumb in cols F–I, source flag in col J, title-based slug in col K, GMC slug in col L, agreement flag in col M, final slug in col N, query-derived title slug in col O, and a combined final slug in col P). Two separate output files were requested: one using title/query matching (col P) and one using GMC category only (col L). Simon corrected Claude when it described clicks as "estimated" — the clicks are actual, only the page attribution is inferred. Simon also explicitly asked for the scraping approach rather than accepting the products export as a proxy, noting that scraping wasn't working and pushing Claude to use rendered HTML with load-more pagination via Playwright, then curl with SSR HTML extraction when Playwright failed due to sandbox network constraints.

**Tool Knowledge**

The TGG website renders product data server-side via a React Router streaming pattern. Product titles and SKUs are embedded in `streamController.enqueue("...")` calls in the HTML, encoded as escaped JSON strings. The reliable extraction pattern for product titles is `re.findall(r'\\\"(\d{8})\\\",\\\"([^\\]{10,120})\\\"', biggest_chunk)` where `biggest_chunk` is the largest string found via `re.findall(r'enqueue\("(.{1000,}?)\)";', html, re.DOTALL)`. Product SKUs (8-digit numbers) also appear in preloaded image URLs matching `files/(\d{8})_\d+` — these can be used for SKU matching but not title extraction. Pagination uses `?page=N` query parameters and the presence of `page=N+1` in the HTML indicates a next page exists. The `/deals/bbqs` page returns near-zero bytes (likely seasonal/empty collection). TV product data on `/deals/tvs` appears to be loaded client-side only and is not present in the SS

## First user message

> I want Organic shopping sorted into categories using the l1 l2 l3 as insight of which products MAY have matched these pages:  https://www.thegoodguys.com.au/deals/air-conditioners-and-fans https://www.thegoodguys.com.au/deals/bbqs https://www.thegoodguys.com.au/deals/bundle https://www.thegoodguys.com.au/deals/coffee-machines https://www.thegoodguys.com.au/deals/cooking https://www.thegoodguys.com

## Topics

[[topic/deals]], [[topic/eofy]], [[topic/feed]], [[topic/gsc]], [[topic/keyword]], [[topic/redirect]], [[topic/regex]], [[topic/shopify]]

## Skills referenced

none detected
