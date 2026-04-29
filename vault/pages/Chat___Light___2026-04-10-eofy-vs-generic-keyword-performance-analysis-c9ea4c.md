---
title: EOFY vs generic keyword performance analysis
date: 2026-04-10
project: EOFY
status: completed
score: 4/5
uuid: c9ea4cee-c142-44bd-a97f-e0ad2f4c936d
---

#chat/light #project/eofy #status/completed #topic/bfcm #topic/deals #topic/eofy #topic/ga4 #topic/gsc #topic/inlink #topic/keyword #topic/plp

# EOFY vs generic keyword performance analysis

- **Date:** [[2026-04-10]]
- **Project:** [[Projects/EOFY]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, project-keyword, lasting-effect)
- **Messages:** 4
- **Chat URL:** https://claude.ai/chat/c9ea4cee-c142-44bd-a97f-e0ad2f4c936d
- **Medium view:** [[Chat/Medium/2026-04-10-eofy-vs-generic-keyword-performance-analysis-c9ea4c]]
- **Full transcript:** [[Chat/Full/2026-04-10-eofy-vs-generic-keyword-performance-analysis-c9ea4c]]

## Summary

**Conversation Overview**

The person works in SEO strategy, likely at or for The Good Guys (TGG), an Australian electronics retailer. They were working on a structured analysis project to determine how EOFY (End of Financial Year) sale intent compares to generic sale intent across keyword performance, URL rankings, and page strategy — with the goal of deciding whether TGG should invest in dedicated EOFY pages or prioritize generic deals and category pages year-round.

The person provided four GSC (Google Search Console) date-page-query CSV exports covering approximately May 2024 to April 2026, along with a detailed brief document outlining scope requirements. The brief specified six analysis components: dataset reconstruction and validation, trend analysis comparing generic vs EOFY monthly search volume, ranking analysis by URL and period, intent decisions per category, page strategy recommendations, and category validation with SKU placeholders. Deliverable format requirements were explicit — focused tabs only, no redundant summaries, no unvalidated assumptions, and no new page recommendations without ranking evidence.

Claude initially built an XLSX with filtered data, having reduced the 1.56 million total rows to approximately 634,000 by pre-filtering to only sale and EOFY intent queries before analysis. The person identified this as a significant error, noting the output was biased because Claude removed data and merged things rather than using the full dataset to combine the documents. In response, Claude rebuilt the analysis using all 1.56M rows, adding classification columns (intent_type, page_type, category, period) without removing any rows, and delivered both a complete enriched CSV and an 8-tab XLSX with aggregate views including Intent × Month, Page Type × Month, Category × Intent × Period, Top 500 Queries, Top 500 URLs, a focused EOFY vs Generic Sale comparison tab, URL × Period Performance, and a Query × Page tab showing which URLs rank for the top 200 queries. Key competitors referenced throughout the brief included Harvey Norman, Appliances Online, and JB Hi-Fi. The person's core correction — preserve all data and let the structure serve the task rather than pre-filtering based on assumptions about relevance — should govern similar data analysis tasks going forward.

## First user message

> I need you to work across this data and turn it into a few xlsx tabs - it should align with the task we are doing below, but your focus is to get and combine all helpful data:You are an SEO strategist and data analyst.  Your task is to define a complete, execution-ready scope for analysing EOFY vs generic sale intent, using the provided datasets and process documents.  Objective  Determine:  How g

## Topics

[[topic/bfcm]], [[topic/deals]], [[topic/eofy]], [[topic/ga4]], [[topic/gsc]], [[topic/inlink]], [[topic/keyword]], [[topic/plp]]

## Skills referenced

none detected
