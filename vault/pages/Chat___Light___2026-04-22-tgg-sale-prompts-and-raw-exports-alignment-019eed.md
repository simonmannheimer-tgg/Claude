---
title: TGG sale prompts and raw exports alignment
date: 2026-04-22
project: main
status: completed
score: 5/5
uuid: 019eed46-9838-48f2-b3c1-0c29d0f8fe60
---

#chat/light #project/main #status/completed #topic/bfcm #topic/keyword #topic/profound

# TGG sale prompts and raw exports alignment

- **Date:** [[2026-04-22]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 10
- **Chat URL:** https://claude.ai/chat/019eed46-9838-48f2-b3c1-0c29d0f8fe60
- **Medium view:** [[Chat/Medium/2026-04-22-tgg-sale-prompts-and-raw-exports-alignment-019eed]]
- **Full transcript:** [[Chat/Full/2026-04-22-tgg-sale-prompts-and-raw-exports-alignment-019eed]]

## Summary

**Conversation overview**

The person is working on AI visibility and prompt tracking analysis for The Good Guys (TGG), an Australian consumer electronics retailer. The work involves reconciling and enriching a curated Excel file of sale/deals-intent prompts (`tgg_sale_prompts.xlsx`) against raw Profound platform exports and a broader prompt tracking workbook (`The_Good_Guys_-_KW___Prompt_Tracking_FY_25_26.xlsx`). The conversation progressed through several analytical tasks: first verifying alignment between the sale prompts XLSX and a raw CSV export, then identifying 33 missing sale/deals-intent prompts to add, then backfilling TGG mention metrics (TGG Mention %, TGG Mentions, Total Runs) from split raw export files, and finally mining the prompt tracking workbook for additional candidate prompts not yet being tracked.

A key contextual detail the person provided mid-conversation was that the raw export covered three months and that additional prompts were added in early February — this explained a gap in TGG metric coverage for newer prompts. Claude identified the prompt expansion occurred on approximately February 3, jumping from ~60 to ~390 prompts, and computed mention stats per prompt from 234,741 clean rows spanning January 22 to April 21. For the final task, the person clarified that Claude should inspect all AI-relevant tabs in the tracking workbook (Profound Prompts, Peec Prompts, Adthena LLM Prompts) rather than just the Profound tab, and explicitly exclude Accuranker, keyword tagging, and AIO keyword tabs. The output was 64 curated candidate prompts added as a new "Candidate Prompts" tab, tagged by source (Peec, Adthena LLM, Profound) and grouped into intent types: deals discovery, TGG purchase/price intent, price comparison, retailer discovery, product price/purchase, and seasonal/event.

The person works with Profound as the primary AI visibility measurement platform, alongside Peec and Adthena LLM as additional prompt sources. Key file conventions include maintaining a Prompts sheet (category, prompt, TGG Mention %, TGG Mentions, Total Runs) and a Fanout Breakdown sheet (top 5 fanout queries per prompt by fanout count). The person's working style favors Claude flagging data gaps and caveats proactively — for example, noting when TGG metric columns can't be populated from available data, when product-specific prompts will go stale, and when seasonal prompts need annual refresh.

## First user message

> does tgg sale prompts align to the raw exports? does tgg sale prompts align to the raw exports?

## Topics

[[topic/bfcm]], [[topic/keyword]], [[topic/profound]]

## Skills referenced

none detected
