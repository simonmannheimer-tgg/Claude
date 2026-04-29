---
title: Improving organic shopping keyword metrics
date: 2026-04-24
project: Monthly SEO Update
status: active
score: 5/5
uuid: 7028d212-ec6f-43f9-8300-8e1647f0619a
---

#chat/light #project/monthly-seo-update #status/active #topic/aeo #topic/feed #topic/ga4 #topic/gsc #topic/keyword #topic/plp #topic/semrush #topic/shopify #skill/tgg-chart-creator

# Improving organic shopping keyword metrics

- **Date:** [[2026-04-24]]
- **Project:** [[Projects/Monthly SEO Update]]
- **Status:** #status/active (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 83
- **Chat URL:** https://claude.ai/chat/7028d212-ec6f-43f9-8300-8e1647f0619a
- **Medium view:** [[Chat/Medium/2026-04-24-improving-organic-shopping-keyword-metrics-7028d2]]
- **Full transcript:** [[Chat/Full/2026-04-24-improving-organic-shopping-keyword-metrics-7028d2]]

## Summary

**Conversation Overview**

Simon works on SEO strategy and reporting for The Good Guys (TGG), an Australian electronics retailer. This conversation focused on rebuilding the data visualisation approach for Slide 3 of the TGG March 2026 Monthly SEO Update deck, specifically replacing an organic shopping keywords narrative (based on unreliable Semrush data) with charts grounded in GMC (Google Merchant Center) and GSC (Google Search Console) data. Simon had strong opinions about chart style throughout, repeatedly pushing back on designs that were too similar to each other, too angular, or that didn't match visual references he had previously provided.

The conversation involved iterative chart design across several rounds. Simon provided GMC performance data (clicks, impressions, CTR, purchases, purchase rate covering Jul 2025 to Mar 2026), a GSC non-brand merchant listings export (16 months), and a Shopify/GMC organic shopping CSV with daily purchases, revenue, and CVR for Feb and Mar 2026. The final chart set consisted of two charts: a dual-axis line chart showing GMC clicks (blue `#3c83f6`) and impressions (purple `#8762d0`) over 9 months with per-point raw data labels, and a day-by-day MoM comparison line chart for organic shopping purchases (green `#1e8c45`) with Mar solid and Feb dotted, normalised to 28 days, with difference shading (green where Mar exceeded Feb, red where it fell below). Both charts were injected into the PPTX slide replacing IMAGE placeholder shapes, with text headers added above each using two spaces as separator rather than dashes.

Simon also requested removal of the JB keyword footprint bullet from the slide (flagged as based on poor Semrush data) and considered replacement bullets before deciding to simply remove it. Several narrative angles were explored including GMC CTR resilience versus text search CTR compression, LLM-referred sessions growing alongside rather than displacing organic shopping traffic, and non-brand position improvement YoY. Simon's working style is direct, iterative, and correction-heavy — he expects Claude to remember prior instructions without being reminded, catches data accuracy errors immediately (e.g. smoothed vs raw label values showing 279K instead of 265K), and prefers concise questions over assumptions. At the end of the session, Simon requested three deliverables to enable future AI recreation of the charts: a design specification document, reusable Python template code with placeholder values, and a Claude skill file (`tgg-chart-creator.skill`) bundling all reference material.

**Tool Knowledge**

Chart generation used matplotlib with scipy gaussian smoothing. A critical lesson learned: gaussian smoothing must be applied to the line path only, never to data labels — labels must always display raw values. When sigma is set above 1.4 on monthly data with only 9 points, it distorts the seasonal shape materially (e.g. Nov/Dec peak flattens). For the dual-axis GMC chart, label collision between clicks and impressions was solved by anchoring impressions labels above the impressions line (+7pt offset) and clicks labels below the impressions line position (−22pt offset) rather than below the clicks line, because the two lines track closely in scale. The PPTX injection workflow requires sorting IMAGE placeholder shapes by `.top` value before removal to correctly assign top and bottom chart positions. Placeholder EMU coordinates for Slide 3 (index 2) of the TGG deck are: top slot left=824,555 top=1,920,575 width=5,899,428 height=2,214,064; bottom slot left=824,555 top=4,362,198 width=5,899,428 height=2,214,064. Revenue data in the Shopify GMC CSV was split across duplicate date rows (one row with clicks/purchases, another with revenue for the same date) and required a `groupby('Day').agg('sum')` merge before use.

## First user message

> help me continue on this line;  i dont like the organic shopping keywords narrative - its based on pretty poor data. I want something better. Clicks and impressions should be in there - and then maybe something with revenue/purchases?  keywords? help me continue on this line;  i dont like the organic shopping keywords narrative - its based on pretty poor data. I want something better. Clicks and i

## Topics

[[topic/aeo]], [[topic/feed]], [[topic/ga4]], [[topic/gsc]], [[topic/keyword]], [[topic/plp]], [[topic/semrush]], [[topic/shopify]]

## Skills referenced

[[skill/tgg-chart-creator]]
