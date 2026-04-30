---
title: Shopify redirect sheet creation from archived products
date: 2026-03-20
project: main
status: completed
score: 5/5
uuid: 011429c6-dcdb-4e20-b1ca-b0af8bf42264
---

#chat/light #project/main #status/completed #topic/404 #topic/crawl #topic/pdp #topic/plp #topic/redirect #topic/shopify #topic/sitemap

# Shopify redirect sheet creation from archived products

- **Date:** [[2026-03-20]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 21
- **Chat URL:** https://claude.ai/chat/011429c6-dcdb-4e20-b1ca-b0af8bf42264
- **Medium view:** [[Chat/Medium/2026-03-20-shopify-redirect-sheet-creation-from-archived-products-011429]]
- **Full transcript:** [[Chat/Full/2026-03-20-shopify-redirect-sheet-creation-from-archived-products-011429]]

## Summary

**Conversation overview**

The person is working on an SEO redirect project for The Good Guys (thegoodguys.com.au), a large Australian retail site running on Shopify. The core task was to create a Shopify-compatible URL redirect import CSV for archived products, using breadcrumb metadata to determine redirect destinations. The person shared a Shopify Flow automation as the reference logic, which extracts a product's `tgg.breadcrumb` metafield, replaces underscores with forward slashes, and prepends a `/` to construct the redirect destination URL. This Flow logic was the authoritative standard the person wanted applied consistently throughout the work.

The person defined two distinct workflows: Workflow 1 covering archived products already in Shopify (known 404s with full data), and Workflow 2 covering external 404s not in Shopify requiring semantic matching logic. The session focused entirely on Workflow 1. The person provided a product export file containing 3,429 archived products, a sitemap audit CSV with live URLs, existing redirect exports, and multiple active product export files. When Claude initially over-engineered the solution by adding fallback category mapping and sitemap validation logic, the person redirected to keep it simple and faithful to the Flow logic. The only explicit filter requested was to exclude products with "default-sku" in the handle, as these are part of a larger internal process rather than standalone retail products. The final output was a CSV of 3,418 redirects using the pure breadcrumb-to-URL conversion matching the Shopify Flow exactly, formatted with `Redirect from` and `Redirect to` columns ready for direct Shopify import.

## First user message

> I will give you a number of archived products out of shopify - I want you to use the spreadsheets and the same logic shared in this flow to create a shopify Redirect Sheet import:  2977b26c27efcd10f0883172b7fc881800d46505d4392bdebba64aceccce3116:{"__metadata":{"version":0.1},"root":{"steps":[{"step_id":"12e4e0b3-a3af-484f-9ae2-6f8367843372","step_position":[0,0],"config_field_values":[],"task_id":

## Topics

[[topic/404]], [[topic/crawl]], [[topic/pdp]], [[topic/plp]], [[topic/redirect]], [[topic/shopify]], [[topic/sitemap]]

## Skills referenced

none detected
