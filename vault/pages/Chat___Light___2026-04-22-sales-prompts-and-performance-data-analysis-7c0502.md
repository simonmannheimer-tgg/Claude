---
title: Sales prompts and performance data analysis
date: 2026-04-22
project: EOFY
status: completed
score: 4/5
uuid: 7c0502b2-846a-4ba9-a962-ef9f7518cf3e
---

#chat/light #project/eofy #status/completed #topic/aeo #topic/deals #topic/eofy #topic/profound

# Sales prompts and performance data analysis

- **Date:** [[2026-04-22]]
- **Project:** [[Projects/EOFY]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, 5+turns, project-keyword)
- **Messages:** 8
- **Chat URL:** https://claude.ai/chat/7c0502b2-846a-4ba9-a962-ef9f7518cf3e
- **Medium view:** [[Chat/Medium/2026-04-22-sales-prompts-and-performance-data-analysis-7c0502]]
- **Full transcript:** [[Chat/Full/2026-04-22-sales-prompts-and-performance-data-analysis-7c0502]]

## Summary

**Conversation overview**

The person is working on an AI search visibility and content strategy project for The Good Guys (thegoodguys.com.au), a major Australian consumer electronics retailer. They were analysing Profound AI monitoring data alongside query fanout data to understand which prompts related to sales, deals, offers, discounts, EOFY, and affordability are relevant to a specific set of The Good Guys deals and sale landing pages spanning categories including TVs, fridges, washing machines, dryers, dishwashers, vacuums, cooking appliances, small kitchen appliances, coffee machines, air conditioners, heaters, headphones, health and beauty, laptops, phones, and smart home products.

The person provided two data files: a Profound raw data export (covering April 14–20 2026) and a query fanout export (point-in-time from April 22 2026), along with a list of 24 specific The Good Guys URLs to map prompts against. The work progressed through several iterations. The first attempt produced a URL-centric format mapping prompts to each deals page. The second attempt restructured this as a prompt-first layout with category header rows and fanout sub-rows, which the person rejected as having poor formatting with heavy row heights. The final accepted format was a clean two-tab Excel workbook: one tab ("Prompts") with all 86 sale-intent prompts, their category, TGG mention %, mention count, and total runs sorted by mention rate; and a second tab ("Fanout Breakdown") with one row per fanout query showing category, prompt, TGG mention %, fanout query text, and fanout count, with top 5 fanouts per prompt. Both tabs have autofilter, frozen headers, and minimal formatting with only mention % cells colour-coded green/amber/red.

The person's clear preference is for simple, lightweight spreadsheet formatting — no merged cells, no thick row heights, no heavy styling. They want data organised by prompt rather than by URL, with fanout queries expanded into individual rows rather than concatenated. Key domain terminology used includes: Profound (AI monitoring platform), mention rate/mention %, query fanouts, AEO (Answer Engine Optimisation), and citation visibility. A noted data limitation is that the Profound export covers only 7 days rather than the requested 28-day window.

## First user message

> which prompts are about sales or could relate to sale or offer or discounts?  e.g. which could be relevant for these? also their latest data for visibility and citation etc. (last 28 days) and query fanouts.   https://www.thegoodguys.com.au/eofy-sale https://www.thegoodguys.com.au/deals/air-conditioners-and-fans https://www.thegoodguys.com.au/deals/bbqs https://www.thegoodguys.com.au/deals/bundle 

## Topics

[[topic/aeo]], [[topic/deals]], [[topic/eofy]], [[topic/profound]]

## Skills referenced

none detected
