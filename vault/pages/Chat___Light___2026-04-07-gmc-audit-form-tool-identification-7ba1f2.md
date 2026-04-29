---
title: GMC audit form tool identification
date: 2026-04-07
project: main
status: completed
score: 4/5
uuid: 7ba1f251-2057-46d7-b5d2-e50b2c2c0fd7
---

#chat/light #project/main #status/completed #topic/feed #topic/regex

# GMC audit form tool identification

- **Date:** [[2026-04-07]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, project-keyword, lasting-effect)
- **Messages:** 4
- **Chat URL:** https://claude.ai/chat/7ba1f251-2057-46d7-b5d2-e50b2c2c0fd7
- **Medium view:** [[Chat/Medium/2026-04-07-gmc-audit-form-tool-identification-7ba1f2]]
- **Full transcript:** [[Chat/Full/2026-04-07-gmc-audit-form-tool-identification-7ba1f2]]

## Summary

**Conversation Overview**

The person is working in an e-commerce or digital merchandising context, conducting a Google Merchant Center (GMC) product feed audit. The conversation centered on identifying a tool shown in a GMC audit form screenshot, which Claude identified as a Google Merchant Center product feed diagnostic export showing attribute-value pairs for a Shark vacuum cleaner product. Several fields carried an "im_" prefix (e.g., `im_beauty_brand`, `im_product_category`), identified as custom internal merchant labels belonging to TGG, distinct from standard Google Shopping taxonomy fields.

The core technical issue discussed was a delimiter problem with the `product_highlight` field, where commas were being used instead of Google's required pipe (`|`) separator for multi-value fields. The person relayed guidance from their SEO agency (referenced contextually alongside Overdose Digital and Searchspring as relevant platforms) confirming the fix is to switch to pipe-delimited separation when pulling in key product features. The person expressed frustration that their feed management team had not independently identified and resolved this straightforward fix, noting it should require minimal technical effort — Claude validated this and provided example code showing how trivial the change is, along with suggested escalation language the person could use to push for a resolution timeline.

The conversation references Searchspring as a likely feed management platform and raises the question of whether Overdose Digital or TGG controls the Searchspring feed configuration, which remained unresolved. The person communicates directly and informally, including candid expressions of frustration, and appears to want Claude to validate technical assessments and provide ready-to-use language for stakeholder escalations.

## First user message

> what tool is this gmc audit form? what tool is this gmc audit form?

## Topics

[[topic/feed]], [[topic/regex]]

## Skills referenced

none detected
