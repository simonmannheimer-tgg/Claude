---
title: Extracting JSON-LD schema
date: 2026-04-22
project: main
status: completed
score: 4/5
uuid: 4cf0112c-85fd-4d9a-bae2-a46705dc47b5
---

#chat/light #project/main #status/completed #topic/schema #topic/shopify

# Extracting JSON-LD schema

- **Date:** [[2026-04-22]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, project-keyword, lasting-effect)
- **Messages:** 4
- **Chat URL:** https://claude.ai/chat/4cf0112c-85fd-4d9a-bae2-a46705dc47b5
- **Medium view:** [[Chat/Medium/2026-04-22-extracting-json-ld-schema-4cf011]]
- **Full transcript:** [[Chat/Full/2026-04-22-extracting-json-ld-schema-4cf011]]

## Summary

**Conversation Overview**

The person is working with HTML source files from The Good Guys (thegoodguys.com.au), an Australian retail site, and needs to extract structured data from them. In this session, they uploaded two versions of an HTML file — initially the wrong version, then corrected to the right one — and asked Claude to extract only the JSON-LD schema markup, specifically filtered to Product type only.

Claude used Python regex to parse the HTML files and identify all `<script type="application/ld+json">` blocks, then filtered results to return only blocks where `@type` matched "Product." The correct file contained a single Product schema for the Dyson V8 Cyclone Cordless Vacuum (SKU: 50096116, model 226890-01), which was returned in full, including offers, aggregate ratings, ten individual reviews, shipping details, return policy, and product dimensions. Claude also flagged that the `priceValidUntil` field in the offer was expiring that same day.

The person's workflow involves uploading raw HTML files and extracting specific schema types from them, suggesting ongoing work with structured data or SEO-related tasks on Good Guys product pages. The correction mid-conversation ("wrong file version, here") indicates they are working across multiple file versions and want precise, type-filtered extraction rather than all schema blocks.

## First user message

> get me only the schema (json LD) bits from here get me only the schema (json LD) bits from here

## Topics

[[topic/schema]], [[topic/shopify]]

## Skills referenced

none detected
