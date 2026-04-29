---
title: Fixing comma linebreaks in GMC feed
date: 2026-04-07
project: main
status: completed
score: 5/5
uuid: 28b9d837-95a4-48b8-9587-aeb766abd343
---

#chat/light #project/main #status/completed #topic/feed #topic/regex #topic/shopify

# Fixing comma linebreaks in GMC feed

- **Date:** [[2026-04-07]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 14
- **Chat URL:** https://claude.ai/chat/28b9d837-95a4-48b8-9587-aeb766abd343
- **Medium view:** [[Chat/Medium/2026-04-07-fixing-comma-linebreaks-in-gmc-feed-28b9d8]]
- **Full transcript:** [[Chat/Full/2026-04-07-fixing-comma-linebreaks-in-gmc-feed-28b9d8]]

## Summary

**Conversation Overview**

This conversation continues an ongoing Google Merchant Center (GMC) feed audit focused on a delimiter conflict in the `product_highlight` field. Simon, SEO Lead at TGG, is managing the audit while colleague Peter Ioannides is on leave, with Overdose Digital (SEO agency) and Searchspring/Intelligent Reach (feed management platform) also involved. The core issue is that commas within individual feature values in the `tgg.key_features` JSON metafield are being misinterpreted as field separators during CSV export, breaking GMC's `product_highlight` field parsing.

In this session, Simon asked Claude to identify which products in the Shopify export (`Export_2026-04-07_123605.xlsx`) contain internal commas within their `tgg.key_features` JSON values. Claude ran a Python/pandas script against the uploaded file using the regex pattern `"value":"[^"]*,[^"]*"` to extract all affected SKUs and their specific problematic feature strings. Simon also asked Claude to write a quick regex for matching comma-containing JSON values, and Claude provided `"value":"[^"]*,[^"]*"` with explanation of why the negated character class `[^"]*` is preferable to `.*` for precision within JSON structure.

**Tool Knowledge**

For parsing the Shopify Excel export, Claude used `pandas.read_excel()` targeting the column `Metafield: tgg.key_features [json]` (exact column name required) and applied `re.findall(r'"value":"([^"]*,[^"]*)"', key_features)` to extract matching feature strings per row. The script iterated over all rows, checked for non-null string values, and collected both the product Handle and Title alongside the offending feature strings. This approach successfully identified 12 affected SKUs across vacuum, kitchen tap, cooking, and storage categories directly from the raw Shopify metafield export without requiring JSON parsing of the full metafield structure.

## First user message

> our product highlights in gmc feed has commas, it breaks the feed:  how can i fix it?  Intelligent reach said theres no good way to dis-allow comma breaks in these... we likely need a bulk replace option [12:04 PM] and it needs to work in various formats, whether the comma is for a list, for emphasis... [12:04 PM] is there a comma symbol that wouldnt register as a linebreak? our product highlights

## Topics

[[topic/feed]], [[topic/regex]], [[topic/shopify]]

## Skills referenced

none detected
