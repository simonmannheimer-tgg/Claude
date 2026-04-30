---
title: SEO keyword report consolidation and restructuring
date: 2026-04-13
project: EOFY
status: completed
score: 5/5
uuid: 4f6611d6-9f77-4a57-8233-2278a56e064d
---

#chat/light #project/eofy #status/completed #topic/bfcm #topic/deals #topic/eofy #topic/keyword #topic/mcp #topic/semrush

# SEO keyword report consolidation and restructuring

- **Date:** [[2026-04-13]]
- **Project:** [[Projects/EOFY]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 22
- **Chat URL:** https://claude.ai/chat/4f6611d6-9f77-4a57-8233-2278a56e064d
- **Medium view:** [[Chat/Medium/2026-04-13-seo-keyword-report-consolidation-and-restructuring-4f6611]]
- **Full transcript:** [[Chat/Full/2026-04-13-seo-keyword-report-consolidation-and-restructuring-4f6611]]

## Summary

**Conversation Overview**

The person is an SEO analyst or digital marketing professional working on a comprehensive EOFY (End of Financial Year) keyword report for TGG (The Good Guys, an Australian electronics retailer). The project involved consolidating legacy SEO data with fresh Semrush datasets to produce a structured keyword analysis covering product categories TGG competes in, including laptops, fridges, TVs, washing machines, dishwashers, air conditioners, coffee machines, vacuum cleaners, and many others. The person demonstrated strong domain knowledge throughout, using SEO-specific terminology fluently (KD, CPC, search volume, trend index, bulk exports, position tracking, MCP) and pushed back firmly when outputs were incomplete, miscategorised, or methodologically wrong.

The core task evolved through multiple iterations: starting from a request to merge a legacy visual report with Semrush CSV exports, it grew into a full keyword universe rebuild covering 881 keywords across 22 EOFY categories and 28 Generic categories, with Jan–Dec monthly volumes for 2023, 2024, and 2025, plus 2026 YTD (Jan–Apr), and YoY Jun comparisons. The person explicitly corrected several significant issues during the process: poor initial categorisation (a "Sale" catch-all dumping 80+ keywords), insufficient EOFY keyword coverage (only 34 rows initially), wrong time window (Jan–Jun 2026 instead of historical full years), a fundamental formula error in how monthly volumes were derived from Semrush trend data, and EOFY product-specific keywords being incorrectly collapsed into Cross-Category. Each correction was stated directly and without elaboration, expecting immediate resolution.

A critical methodological discovery occurred mid-conversation: the formula used to derive monthly absolute volumes from Semrush's trend index was wrong. The initial approach used `trend_i / max(trend) × Volume`, which incorrectly set the peak month equal to the reported Search Volume. The correct formula is `trend_i × (Volume × 12 / sum(trend))`, which preserves Search Volume as the 12-month monthly average. For highly seasonal keywords like "eofy sale", this changed the Jun 2025 peak figure from ~8,100 to ~69,400 — a roughly 8x distortion. The person prompted this investigation by questioning why the Volume metric works the way it does, leading to the fix being applied retroactively across all 537+ keywords. The final dataset used Semrush bulk exports (6 initial batches of 99 keywords each, then 4 more batches for the "not covered" list) combined with Semrush MCP live pulls for cross-category terms and zero-coverage keywords, all processed with the corrected formula.

**Tool Knowledge**

Semrush MCP was used via `execute_report` with the `phrase_these` report type, targeting the `au` database with `export_columns: ['Ph', 'Nq', 'Td']` (keyword, volume, trend). Batching up to 25 keywords per MCP call worked reliably. The Trend field returned by MCP uses a 12-value comma-separated decimal string (e.g. `0.44,0.29,...`) where index 0 = oldest month and index 11 = current month (April 2026 at time of export). Semrush bulk XLSX exports use the same 12-value structure but sometimes in integer format (e.g. `44,29,...` on a 0–100 scale) rather than 0–1 decimal — both formats require normalisation before applying the volume scaling formula. The correct derivation is `monthly_vol_i = trend_i × (Volume × 12 / sum(all_12_trend_values))`, which guarantees the mean of all 12 derived monthly values equals the reported Search Volume. Using `trend_i / max(trend) × Volume` instead is a common but incorrect approach that sets peak = Volume rather than average = Volume, causing severe distortion for seasonal keywords.

For historical monthly data, the 29mb position-tracking CSV exports (12 files, ~1.3M rows, 72,975 unique keywords) each contain a `Trends` field and `Timestamp` (daily). To reconstruct monthly volumes for a target period (e.g. June 2025), the best approach is finding the snapshot where that target month falls closest to index 11 (i.e. the snapshot taken in or just after the target month), since the trend array is

## First user message

> Role: Expert Data Analyst and SEO Specialist. Task: Reconstruct a consolidated SEO keyword report by merging a legacy visual report (attached image) with new, high-precision SEMrush datasets (provided below). Data Sources:  1. Reference Image: Contains legacy metrics (Position, CPC, Traffic %, Keyword Difficulty). 2. SEMRush Files (Raw Text/Uploads): Contains the updated "EOFY" and "Generic" categ

## Topics

[[topic/bfcm]], [[topic/deals]], [[topic/eofy]], [[topic/keyword]], [[topic/mcp]], [[topic/semrush]]

## Skills referenced

none detected
