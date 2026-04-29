---
title: Refining Shopify flow redirects with URL pattern matching
date: 2026-04-07
project: main
status: abandoned
score: 5/5
uuid: 4c640f7a-8395-4200-ba4a-a38476d6c48e
---

#chat/light #project/main #status/abandoned #topic/plp #topic/redirect #topic/shopify #topic/sitemap

# Refining Shopify flow redirects with URL pattern matching

- **Date:** [[2026-04-07]]
- **Project:** [[Projects/main]]
- **Status:** #status/abandoned (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 34
- **Chat URL:** https://claude.ai/chat/4c640f7a-8395-4200-ba4a-a38476d6c48e
- **Medium view:** [[Chat/Medium/2026-04-07-refining-shopify-flow-redirects-with-url-pattern-matching-4c640f]]
- **Full transcript:** [[Chat/Full/2026-04-07-refining-shopify-flow-redirects-with-url-pattern-matching-4c640f]]

## Summary

**Conversation overview**

This session focused on auditing and refining Shopify Flow redirect automation for The Good Guys (TGG) Shopify store. The person's core instruction was that breadcrumb URLs should be the primary redirect destination, with redirect rules only added as refinements when the breadcrumb is genuinely too generic—using the iPad tier rules as the paradigm example of when a rule is justified. The person directed Claude to look properly at the actual breadcrumb metafield in the product export before proposing any new opportunities.

Claude read the products export (`Export_2026-04-07_123605.xlsx`) to examine the real breadcrumb metafield structure (`Metafield: tgg.breadcrumb [single_line_text_field]`), which uses underscore-delimited L1_L2_L3 format (e.g., `cooking-and-dishwashers_rangehoods_undermount-rangehoods`). Claude then cross-referenced 199 products against the sitemap audit (12,086 URLs, `sitemap-audit_2026-03-19.csv`) to identify any cases where a product's breadcrumb L3 was vaguer than its handle suggested and a more specific sitemap page existed. The audit found no additional broad redirect rule opportunities—existing breadcrumbs are already specific and correctly aligned with sitemap L3 pages across all major appliance categories examined.

A critical finding emerged regarding Rule 1 (Apple Product Tiers): the March 2026 sitemap audit does not contain dedicated L3 pages for `apple-ipad-pro`, `ipad-air`, or `apple-ipad-mini`—all iPads appear to roll into the generic `/ipad` L3. This means Rule 1 as currently written would redirect to non-existent destinations. The recommendation documented is to verify with Overdose Digital whether these pages exist on the live site before deploying the Flow, and to disable Rule 1 if they don't. Rule 2 (Installation Services remapping old structure to `/home-services/`) remains fully validated. Findings were written to `/mnt/user-data/outputs/redirect_opportunities_audit.md`.

**Tool knowledge**

Python with `openpyxl` was used to read the Excel exports throughout this project. The breadcrumb metafield is at column index 11 (0-based) in the Products sheet of `Export_2026-04-07_123605.xlsx`. The sitemap audit CSV uses `URL` and `Previous Breadcrumb URL` as the relevant column headers. Parsing the sitemap's `Previous Breadcrumb URL` field (stripping leading slashes and splitting on `/`) reliably extracts L1, L2, and L3 slugs. Breadcrumb underscore parsing (`bc.split('_')`) maps directly to URL path segments for cross-referencing. When handle-keyword matching returned zero results, the issue was mismatched field names between the Excel columns and the lookup logic—re-reading raw headers first resolved the confusion.

## First user message

> I have this flow in shopify flow:  it currently auto redirects based on breadcrumb, however sometimes it is limited (breadcrumbs less detailed than actual opportunity to redirect)  for example, an ipad air product redirects to ipad, not ipad air.  I will attach our list of redirects, and youll be able to see the ipad air, pro etc. and macbook pages (and any others you can see) that have been re-do

## Topics

[[topic/plp]], [[topic/redirect]], [[topic/shopify]], [[topic/sitemap]]

## Skills referenced

none detected
