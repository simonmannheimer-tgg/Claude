---
title: Checking product highlight comma separation
date: 2026-03-31
project: GMC Feed Audit — Delimiter Conflict
status: completed
score: 3/5
uuid: 70a4c27b-e9ad-468c-8dc9-48c325219571
---

#chat/light #project/gmc-feed-audit-delimiter-conflict #status/completed

# Checking product highlight comma separation

- **Date:** [[2026-03-31]]
- **Project:** [[Projects/GMC Feed Audit — Delimiter Conflict]]
- **Status:** #status/completed (score 3/5: deliverable, project-keyword, lasting-effect)
- **Messages:** 2
- **Chat URL:** https://claude.ai/chat/70a4c27b-e9ad-468c-8dc9-48c325219571
- **Medium view:** [[Chat/Medium/2026-03-31-checking-product-highlight-comma-separation-70a4c2]]
- **Full transcript:** [[Chat/Full/2026-03-31-checking-product-highlight-comma-separation-70a4c2]]

## Summary

**Conversation Overview**

The person requested an audit of a Google Shopping feed spreadsheet for The Good Guys (Digital) — AU market, specifically checking the `product_highlight` column for comma separation issues. The file analyzed was `The_Good_Guys__Digital__-_Google_Shopping__AU____12_03_2026_.xlsx`. The task was framed as validation work connected to a Searchspring ticket, suggesting the person works in a digital merchandising, feed management, or ecommerce operations role.

Claude read the spreadsheet using pandas, identified the specific problematic pattern — `X Litre fridge, Y Litre freezer` — where commas within capacity specifications were being interpreted as field delimiters in Google Merchant Center. The analysis confirmed 140 SKUs (2.1% of 6,520 total feed SKUs) were affected, all refrigeration products across brands including Hisense, LG, Samsung, Fisher & Paykel, Westinghouse, and others. The proposed fix was replacing `, ` with ` and ` specifically within the fridge/freezer capacity pattern, preserving meaning while eliminating the delimiter conflict.

Claude produced two deliverables: a structured markdown analysis document (`Searchspring_Comma_Fix_Analysis.md`) formatted for sharing with the Searchspring team, including a summary table, pattern validation details, sample before/after rows, and recommended next steps; and a CSV export (`product_highlights_before_after.csv`) containing all 140 affected SKUs with their current and proposed `product_highlight` values for final visual inspection before implementation. Key domain terminology used throughout included: product_highlight, GMC (Google Merchant Center), feed delimiter, SKU, and Searchspring.

## First user message

> I need you to check product_highlight in this sheet for comma separation issues - refer to this conversation: I need you to check product_highlight in this sheet for comma separation issues - refer to this conversation:

## Topics

none detected

## Skills referenced

none detected
