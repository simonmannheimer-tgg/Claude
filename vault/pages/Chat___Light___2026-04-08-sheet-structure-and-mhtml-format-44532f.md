---
title: Sheet structure and MHTML format
date: 2026-04-08
project: Product Meta Title Colour Standardisation (8,582 Titles)
status: completed
score: 4/5
uuid: 44532fa9-eb75-4acb-86fd-f4ee5d2576c7
---

#chat/light #project/product-meta-title-colour-standardisatio #status/completed #topic/keyword #topic/meta #topic/monday #topic/regex #topic/shopify #skill/mhtml-reader

# Sheet structure and MHTML format

- **Date:** [[2026-04-08]]
- **Project:** [[Projects/Product Meta Title Colour Standardisation (8,582 Titles)]]
- **Status:** #status/completed (score 4/5: deliverable, 5+turns, project-keyword, lasting-effect)
- **Messages:** 69
- **Chat URL:** https://claude.ai/chat/44532fa9-eb75-4acb-86fd-f4ee5d2576c7
- **Medium view:** [[Chat/Medium/2026-04-08-sheet-structure-and-mhtml-format-44532f]]
- **Full transcript:** [[Chat/Full/2026-04-08-sheet-structure-and-mhtml-format-44532f]]

## Summary

**Conversation Overview**

This conversation continued an e-commerce SEO project for The Good Guys (thegoodguys.com.au), optimizing 8,582 product meta titles by adding standardized colour terms for organic search visibility. The core business rule is that people search "black headphones" not "midnight headphones," so supplier colour terms that don't contain a standard colour word need bracket clarification (e.g., "Midnight (Black)", "Stainless Steel (Silver)"). The person identified a specific data quality problem — a Bowers and Wilkins product producing a malformed title with duplicated colour terms — and demanded a rigorous row-by-row logic check rather than accepting previous validation passes that had let issues slip through.

Claude conducted multiple full audit passes, each uncovering and fixing additional issues. The provided Model # column was used directly to eliminate extraction errors. Key fixes included: correcting the Bowers and Wilkins duplication caused by uppercase colour terms in the model number, expanding the exclusion list for non-colour supplier values like "Integrated," preserving non-colour bracketed content such as generation info "(6 Gen)" rather than stripping all brackets, fixing orphaned brackets from malformed source data like "(Black))", cleaning double dashes, and excluding multi-word material descriptions containing terms like ceramic, glass, effect, and trimming. After three audit passes with zero blocking issues, the file was confirmed against a staging import result (Import_Result_2026-04-08_125028.xlsx) showing 1,653 products all marked "OK" with "UPDATE: Found by ID," achieving a 100% match rate on spot checks.

Before bulk upload, the person flagged a specific product — "Sedko Pty Ltd Melody TV Cabinet 1600mm 24 Oak (Beige) MELODY 1600 - OAK" — as appearing to have "Oak" repeated oddly. Claude traced this to manufacturer SKU convention: the model number itself contains "OAK," making duplication unavoidable while still being logically correct (the title needs "Beige" for search, and "Oak" appears as the supplier colour with bracket clarification). Investigation found only 36 products (0.4%) share this pattern, all driven by manufacturer model number conventions, and the outcome was confirmed as correct and acceptable for production deployment. The person's key correction pattern throughout was demanding stricter validation rather than accepting clean audit reports at face value.

## First user message

> Does the sheet reflect the correct structure?  start with the MHTML Does the sheet reflect the correct structure?  start with the MHTML

## Topics

[[topic/keyword]], [[topic/meta]], [[topic/monday]], [[topic/regex]], [[topic/shopify]]

## Skills referenced

[[skill/mhtml-reader]]
