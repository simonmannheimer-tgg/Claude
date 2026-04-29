---
title: Product metafield feature breakdown and comma detection
date: 2026-04-08
project: main
status: completed
score: 3/5
uuid: 97af9d93-8a49-47c8-91a7-c5c8410fcb7a
---

#chat/light #project/main #status/completed

# Product metafield feature breakdown and comma detection

- **Date:** [[2026-04-08]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 3/5: deliverable, named-tgg, project-keyword)
- **Messages:** 2
- **Chat URL:** https://claude.ai/chat/97af9d93-8a49-47c8-91a7-c5c8410fcb7a
- **Medium view:** [[Chat/Medium/2026-04-08-product-metafield-feature-breakdown-and-comma-detection-97af9d]]
- **Full transcript:** [[Chat/Full/2026-04-08-product-metafield-feature-breakdown-and-comma-detection-97af9d]]

## Summary

**Conversation Overview**

The person is working on a product data quality audit for TGG (The Good Guys, based on context), specifically investigating a known issue with comma characters in product key features causing unwanted line breaks in a Google Merchant Center (GMC) feed managed through Intelligent Reach. They provided three files: an MHTML file documenting prior context about the comma/linebreak problem, a CSV file, and an Excel export of product data (`Export_2026-04-07_123605.xlsx`) containing the metafield `Metafield: tgg.key_features [json]`.

Claude parsed the JSON metafield across 8,390 products and 31,555 total key features, finding that 10,280 features (32.6%) contained commas, affecting 5,289 products (63% of the catalog). Claude identified four structural comma usage patterns: list separators, specification separators (e.g., measurements and capacities), registration numbers (e.g., WELS ratings), and capacity measurements (e.g., fridge/freezer litre specs). Claude produced a formatted Excel audit file (`TGG_Key_Features_Comma_Audit.xlsx`) with four sheets: a summary, a full feature breakdown with conditional formatting, a comma-features-only filtered view, and a top 100 products ranked by comma frequency. Claude also communicated a key analytical conclusion: the issue cannot be resolved with a universal bulk replacement, as commas serve multiple distinct structural roles, and only targeted per-pattern transformation rules — coordinated with Intelligent Reach — represent a viable fix.

**Tool Knowledge**

Claude used Python-based file parsing tools to read an MHTML file via BeautifulSoup, load the Excel export via pandas, and parse the `[json]` metafield column using Python's `json.loads()`. The key metafield column name is `Metafield: tgg.key_features [json]`, and each parsed JSON entry contains `value` and `order` keys. Output was written using `openpyxl` with manual conditional formatting (red fill for "YES", green for "NO" in the Has Comma column) and saved to `/home/claude/TGG_Key_Features_Comma_Audit.xlsx`.

## First user message

> I need you to break down the key features for each product as per the metafield, and flag in which there is a comma:  you can do better formatting than me, but thats the jist of it, goal is to understand how large this issue is (see mhtml) I need you to break down the key features for each product as per the metafield, and flag in which there is a comma:  you can do better formatting than me, but 

## Topics

none detected

## Skills referenced

none detected
