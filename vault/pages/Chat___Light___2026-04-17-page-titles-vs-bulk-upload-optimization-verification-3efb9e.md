---
title: Page titles vs bulk upload optimization verification
date: 2026-04-17
project: main
status: completed
score: 4/5
uuid: 3efb9e85-e28f-4f8a-a87e-1773b6e167af
---

#chat/light #project/main #status/completed #topic/contentful #topic/crawl #topic/shopify #topic/sitemap

# Page titles vs bulk upload optimization verification

- **Date:** [[2026-04-17]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 4/5: deliverable, 5+turns, project-keyword, lasting-effect)
- **Messages:** 12
- **Chat URL:** https://claude.ai/chat/3efb9e85-e28f-4f8a-a87e-1773b6e167af
- **Medium view:** [[Chat/Medium/2026-04-17-page-titles-vs-bulk-upload-optimization-verification-3efb9e]]
- **Full transcript:** [[Chat/Full/2026-04-17-page-titles-vs-bulk-upload-optimization-verification-3efb9e]]

## Summary

**Conversation Overview**

The person is working on an SEO title tag implementation project for TGG, auditing whether bulk-uploaded optimised page titles from an implementation plan (Sheet14) have correctly gone live on the site. The workflow involves cross-referencing multiple data sources: a Screaming Frog crawl (page_titles_all), an internal links crawl (internal_all), a full product export (Sheet13, columns K-M for Shopify IDs and handles), and a Shopify import template (Import_2026-04-16_V3.xlsx) used as the format reference.

Claude ran a full cross-reference of 6,771 planned title changes against the live crawl, identifying 87 URLs needing remediation across three issue types: 67 not implemented (still showing old title), 13 unexpected titles (differing from both old and optimised), and 7 encoding/mojibake issues in the plan where the live site was already correct. The person then requested a Shopify-format import file (V4, dated 2026-04-17) combining all three issue types, using the live title as the import value for encoding-issue rows. IDs were sourced from the full product export in Sheet13 columns K-M after the V3 template only covered a subset. A recrawl (redone_internal_all) confirmed 85 of 87 resolved; the 2 apparent remainders were identified as out-of-scope rows with no colour change planned, so no V5 was needed.

The person caught that the V5 draft targets lacked colour in the titles, prompting Claude to re-examine those rows in Sheet14, which confirmed they were marked "No change" with no colour data — correctly excluding them. The final output format mirrors the V3 import structure exactly: a Products sheet (ID, Handle, Metafield: title_tag [string]) and an Export Summary sheet. The person's correction pattern was direct and precise — spotting missing colour and immediately flagging it — indicating familiarity with the dataset and expectation of accurate title content, not just structural formatting.

## First user message

> please check if page titles all matches the implementation plan in sheet 14, sheet 14 is bulk uploaded optimisation, titles all is latest crawl. please check if page titles all matches the implementation plan in sheet 14, sheet 14 is bulk uploaded optimisation, titles all is latest crawl.

## Topics

[[topic/contentful]], [[topic/crawl]], [[topic/shopify]], [[topic/sitemap]]

## Skills referenced

none detected
