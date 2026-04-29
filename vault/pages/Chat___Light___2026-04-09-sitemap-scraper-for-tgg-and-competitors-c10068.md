---
title: Sitemap scraper for TGG and competitors
date: 2026-04-09
project: main
status: completed
score: 5/5
uuid: c100681a-d68c-4e55-beb0-f66e550afbc7
---

#chat/light #project/main #status/completed #topic/airtable #topic/blog #topic/deals #topic/meta #topic/pdp #topic/plp #topic/regex #topic/schema #topic/sitemap

# Sitemap scraper for TGG and competitors

- **Date:** [[2026-04-09]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 8
- **Chat URL:** https://claude.ai/chat/c100681a-d68c-4e55-beb0-f66e550afbc7
- **Medium view:** [[Chat/Medium/2026-04-09-sitemap-scraper-for-tgg-and-competitors-c10068]]
- **Full transcript:** [[Chat/Full/2026-04-09-sitemap-scraper-for-tgg-and-competitors-c10068]]

## Summary

**Conversation Overview**

The person works in an SEO or digital strategy role and is building a competitive intelligence tool focused on sitemap analysis across major Australian consumer electronics and appliances retailers. Their goal is to understand content structure, page taxonomy, and competitive gaps between their company (TGG, The Good Guys) and three key competitors: JB Hi-Fi, Harvey Norman, and Appliances Online. They provided the full sitemap index URLs for all four competitors at the outset.

The conversation began with the person sharing an existing Jupyter notebook scraper (uploaded as a file) that had significant limitations for competitive intelligence purposes. Claude diagnosed five core problems with the original approach: no competitor differentiation in the data model, wrong data fields being collected (missing page type, taxonomy, and metadata), CSV-only output creating manual diff hell for monthly tracking, no persistent storage layer, and inadequate architecture for the stated dashboard requirement. The person confirmed their goals as comprehensive competitive intelligence, monthly change tracking, and a unified CSV plus dashboard output. Claude then built a complete replacement solution from scratch.

The delivered notebook (`competitive_sitemap_intelligence.ipynb`) includes: a multi-competitor scraper covering all four retailers with configurable sitemap lists, SQLite persistent storage with indexed schema, incremental update logic that skips unchanged URLs based on `lastmod` comparison (reducing repeat run time from ~30 minutes to ~5 minutes), URL-pattern-based page type classification per competitor, breadcrumb and URL-based taxonomy extraction (category, subcategory, brand), full metadata scraping (title, meta description, H1, canonical, HTTP status), automated competitive gap analysis identifying categories and content types competitors have that TGG lacks, a Chart.js HTML dashboard with TGG brand colors, and a unified CSV export. Claude noted key limitations around sitemap coverage blind spots, classification accuracy requiring post-first-run tuning, and rate limiting risks at `MAX_WORKERS=15`, recommending reduction to 5–8 if blocked.

## First user message

> I want to build this scraper:  But for TGG AND competitors - so i can understand what content they have and how its structured.  http://www.sitemaps.org/schemas/sitemap/0.9 chrome-extension://hoklmmgfnpapgjgcpechhaamimifchmp/frame_ant/frame_ant.js"/ https://www.jbhifi.com.au/sitemap_products_1.xml?from=1614264664162&to=1620458242146 https://www.jbhifi.com.au/sitemap_products_2.xml?from=16204583404

## Topics

[[topic/airtable]], [[topic/blog]], [[topic/deals]], [[topic/meta]], [[topic/pdp]], [[topic/plp]], [[topic/regex]], [[topic/schema]], [[topic/sitemap]]

## Skills referenced

none detected
