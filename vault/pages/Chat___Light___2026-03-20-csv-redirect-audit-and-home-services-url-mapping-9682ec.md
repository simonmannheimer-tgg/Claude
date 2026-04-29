---
title: CSV redirect audit and home services URL mapping
date: 2026-03-20
project: main
status: completed
score: 2/5
uuid: 9682ec55-02a3-4a67-97c0-a6f32029c854
---

#chat/light #project/main #status/completed #topic/404 #topic/redirect #topic/shopify #topic/sitemap

# CSV redirect audit and home services URL mapping

- **Date:** [[2026-03-20]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 2/5: deliverable, project-keyword)
- **Messages:** 4
- **Chat URL:** https://claude.ai/chat/9682ec55-02a3-4a67-97c0-a6f32029c854
- **Medium view:** [[Chat/Medium/2026-03-20-csv-redirect-audit-and-home-services-url-mapping-9682ec]]
- **Full transcript:** [[Chat/Full/2026-03-20-csv-redirect-audit-and-home-services-url-mapping-9682ec]]

## Summary

**Conversation Overview**

The person is working on SEO redirect management for The Good Guys (thegoodguys.com.au), an Australian retailer running on Shopify. They provided a previously generated CSV of redirect recommendations and asked Claude to audit and correct it based on live test results. The core task involved cross-referencing the recommended redirects against existing Shopify redirects and a sitemap audit to identify and resolve several categories of issues: FROM URLs that already have 301s in Shopify (check alignment before including), TO URLs that are themselves 301s (follow the chain to the final destination), and TO URLs that are 404s (replace with valid 200 OK destinations).

A significant portion of the work involved remapping all home installation/services URLs. The person specified that any URLs pointing to the old `/installation-and-services/*` path structure must be remapped to the new `/home-services/*` structure, providing the full list of valid destination URLs. They also provided 22 breadcrumb category URLs (also on the old `/installation-and-services/installs-and-services/*` pattern) that were 404ing and needed new 301 redirects created for them, with specific mappings to the appropriate `/home-services/*` equivalents (e.g., `/dryer-installs` → `/home-services/laundry-installation`, `/tech-zone-support` → `/home-services/tech-support`, `/extended-warranty` → `/gold-service-extras`).

Claude processed the audit programmatically using Python with pandas, cross-referencing three data sources: the input CSV, the existing Shopify redirects export, and the sitemap audit. The script applied rules in priority order: remap installation-and-services paths, follow 301 chains to final destinations, replace 404 TO destinations, check against existing Shopify redirects for conflicts, and validate all final destinations against the sitemap. The output included a clean two-column Shopify import CSV, a multi-sheet Excel audit report (import-ready sheet, full audit, conflicts requiring action, all changes, skipped items, and summary), and a text summary. All destination URLs were validated against the sitemap with zero invalid destinations in the final import file.

## First user message

> I have run some tests on your recommended csv: there are 301s in the 404 list, need to check if your recommended 301 aligns to the current, if so leave it out, if you disagree with the 301 replace it and flag to me from what to what and why. there are also 301 and 404s on your "to" list - you need to also replace the TO in that case, if a 404, you need to replace it with a 200 ok instead - flag to

## Topics

[[topic/404]], [[topic/redirect]], [[topic/shopify]], [[topic/sitemap]]

## Skills referenced

none detected
