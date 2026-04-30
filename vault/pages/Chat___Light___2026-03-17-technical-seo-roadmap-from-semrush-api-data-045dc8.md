---
title: Technical SEO roadmap from Semrush API data
date: 2026-03-17
project: Technical SEO Roadmap from Semrush
status: completed
score: 4/5
uuid: 045dc8ba-d9de-432b-af35-06c8eddec622
---

#chat/light #project/technical-seo-roadmap-from-semrush #status/completed #topic/crawl #topic/inlink #topic/pdp #topic/plp #topic/redirect #topic/schema #topic/semrush #topic/sitemap

# Technical SEO roadmap from Semrush API data

- **Date:** [[2026-03-17]]
- **Project:** [[Projects/Technical SEO Roadmap from Semrush]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, project-keyword, lasting-effect)
- **Messages:** 2
- **Chat URL:** https://claude.ai/chat/045dc8ba-d9de-432b-af35-06c8eddec622
- **Medium view:** [[Chat/Medium/2026-03-17-technical-seo-roadmap-from-semrush-api-data-045dc8]]
- **Full transcript:** [[Chat/Full/2026-03-17-technical-seo-roadmap-from-semrush-api-data-045dc8]]

## Summary

**Conversation Overview**

The person requested that Claude use the Semrush API to generate a technical SEO to-do list and roadmap for The Good Guys Australia (www.thegoodguys.com.au), sorted by highest ROI. The site runs on Shopify and had two active Semrush site audit projects: "TGG - Weekly Site Audit" (project ID 8864038) and "TGG Site Audit (No Products)" (project ID 27257374). Claude pulled data from both projects and synthesized findings into a structured Excel deliverable.

The audit revealed a site health score of 86/100 and an AI Search Score of 71/100, with 1,240 errors, 806 warnings, and 23,020 notices. The most critical issues identified were 907 broken internal links, 311 4xx pages, invalid MerchantListing structured data affecting 7,836 product pages, sitemap contamination, and significant internal linking weaknesses (Internal Linking thematic score: 75/100). The deliverable was a five-tab Excel workbook covering an Executive Summary, a 20-item prioritised to-do list with ROI scores, a phased roadmap spanning Q2–Q3 2026, a structured data breakdown, and a crawl budget analysis showing 21.2% of crawled URLs wasted.

**Tool Knowledge**

Claude accessed Semrush via the Semrush MCP server. The working pattern was: first call `projects_research` with no parameters to list all available projects and retrieve project IDs, then call `execute_report` with `report: "info"` and `params: {'id': '<project_id>'}` to retrieve snapshot-level audit data for a specific project. The `meta_issues` report (called with the same project ID parameter) maps issue IDs to human-readable names and counts. The `get_report_schema` tool was used to explore available report types before executing them. Both `siteaudit_research` and `info` are valid report namespaces. The two TGG project IDs to use for future audits are 8864038 (full site including products) and 27257374 (non-product pages only).

## First user message

> Use semrush api - create a technical seo to-do list and roadmap based on issues detected, sort by highest ROI Use semrush api - create a technical seo to-do list and roadmap based on issues detected, sort by highest ROI

## Topics

[[topic/crawl]], [[topic/inlink]], [[topic/pdp]], [[topic/plp]], [[topic/redirect]], [[topic/schema]], [[topic/semrush]], [[topic/sitemap]]

## Skills referenced

none detected
