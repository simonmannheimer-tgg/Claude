---
title: Good Guys SEO performance tracking sheet
date: 2026-04-22
project: EOFY
status: completed
score: 5/5
uuid: 8b02198a-607b-455a-9986-729d86bf1271
---

#chat/light #project/eofy #status/completed #topic/aeo #topic/bfcm #topic/deals #topic/eofy #topic/feed #topic/gsc #topic/keyword #topic/mcp #topic/plp #topic/profound #topic/regex #topic/semrush #topic/shopify

# Good Guys SEO performance tracking sheet

- **Date:** [[2026-04-22]]
- **Project:** [[Projects/EOFY]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 22
- **Chat URL:** https://claude.ai/chat/8b02198a-607b-455a-9986-729d86bf1271
- **Medium view:** [[Chat/Medium/2026-04-22-good-guys-seo-performance-tracking-sheet-8b0219]]
- **Full transcript:** [[Chat/Full/2026-04-22-good-guys-seo-performance-tracking-sheet-8b0219]]

## Summary

**Conversation Overview**

The person is working on an EOFY (End of Financial Year) SEO strategy for The Good Guys (thegoodguys.com.au), an Australian consumer electronics and appliance retailer. The work involves building a performance tracking table covering a set of /deals/ category pages and the /eofy-sale hub page, with metrics spanning average ranking, non-brand organic traffic, organic shopping clicks (from Google Merchant Center), and AI visibility from Profound. The overarching business goal framing the targets is delivering +18% organic revenue growth by driving 7–10% incremental high-intent organic traffic while sustaining post-Shopify migration conversion gains.

The conversation involved iterative refinement of the tracking table, starting from placeholder example numbers, then correcting the organic shopping column from revenue to clicks, then recalibrating goals to be proportionate to current visibility rather than fixed targets, and finally grounding everything in real data from uploaded exports. Key domain terminology used throughout includes: EOFY, non-brand, sale-intent, impression-weighted average position, volume-weighted average position, pre-migration /buy/ architecture, post-Shopify /deals/ architecture, GMC (Google Merchant Center) organic shopping clicks, Profound AI visibility/citation rate, AccuRanker, Semrush position tracking, and GSC (Google Search Console).

A critical finding emerged during the analysis: most /deals/ pages did not exist in June 2025 because they launched as part of the post-Shopify migration around July 2025. The pre-migration equivalent pages sat under /buy/ (e.g., /buy/tv-sale, /buy/fridge-sale). This means true year-over-year ranking comparison for EOFY 2025 vs EOFY 2026 requires mapping /buy/ URLs to their /deals/ equivalents, and June 2026 will be the first genuine like-for-like EOFY measurement point for most pages. The person pushed back on Claude's initial attempt to source rankings from Semrush via MCP (which was not enabled in the session), then clarified that Average_Rank_(2) and Average_Rank_(3) files represent AccuRanker portfolio-level averages filtered by URL pattern and sale-intent keyword regex respectively, not individual page metrics.

**Tool Knowledge**

Several data files were processed via bash tool across this conversation. The GMC export was split into two files (split_half_1.csv, split_half_2.csv) with different header structures: split_half_1 requires `skiprows=3` and split_half_2 requires `skiprows=1` when reading with pandas. Both files are approximately 3.8 million rows each sorted alphabetically by product title, not by date, so filtering for specific months requires chunked processing rather than head sampling. The correct column names when manually assigned are: Product title, Day, Product ID, Currency, Product category (1st level), Product category (2nd level), Product category (3rd level), Product CTR, Product purchases, Product clicks, Product purchase rate, Product impressions, Product purchase value.

The Semrush data was split across 12 part files (semrush_merged_29mb_01.csv through _12.csv) that must be concatenated before filtering. The key filter combination for this use case is: URL contains /deals/ or /buy/ or /eofy-sale, Position Type equals Organic, and keyword does not match brand pattern `good.?guys|thegoodguys|tgg\b|goodguys`. The AccuRanker file naming convention distinguishes between exports: the file with hash `61c27e073b...` is the April 2026 snapshot; the file with hash `bff5397de8...` is the June 2025 snapshot. The `is_own_domain` column uses integer 1/0 not boolean True/False in the June 2025 file. Volume-weighted average position (not simple mean) is the correct aggregation method across all three ranking sources, using impressions as the weight for GSC and search_volume for Semrush and AccuRanker. For AccuRanker June 2025, the eofy-sale page showed an artificially high position of 66 because generic high-volume queries were being routed to it, and the /deals/tvs equivalent showed an inflated average of 22 due to the broad "tv" keyword (90,500 volume, position 25) dominating the volume weighting—

## First user message

> fill this in with example numbers:  Page Avg. RankingTrafficOrganic Shopping (category)AI Visibility (Sale prompts)CurrentGoalCurrentGoalCurrentGoalCurrentGoalhttps://www.thegoodguys.com.au/eofy-sale4.5< 336,50050,00-0+n/an/a44%50%+https://www.thegoodguys.com.au/deals/air-conditioners-and-fans$21,200$1M+https://www.thegoodguys.com.au/deals/bbqshttps://www.thegoodguys.com.au/deals/coffee-machinesht

## Topics

[[topic/aeo]], [[topic/bfcm]], [[topic/deals]], [[topic/eofy]], [[topic/feed]], [[topic/gsc]], [[topic/keyword]], [[topic/mcp]], [[topic/plp]], [[topic/profound]], [[topic/regex]], [[topic/semrush]], [[topic/shopify]]

## Skills referenced

none detected
