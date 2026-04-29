---
title: Missing delivery schema spreadsheet
date: 2026-04-22
project: main
status: completed
score: 5/5
uuid: 5a87f256-8439-422c-8752-b5431ed674bb
---

#chat/light #project/main #status/completed #topic/feed #topic/jira #topic/pdp #topic/redirect #topic/regex #topic/schema #topic/shopify

# Missing delivery schema spreadsheet

- **Date:** [[2026-04-22]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 153
- **Chat URL:** https://claude.ai/chat/5a87f256-8439-422c-8752-b5431ed674bb
- **Medium view:** [[Chat/Medium/2026-04-22-missing-delivery-schema-spreadsheet-5a87f2]]
- **Full transcript:** [[Chat/Full/2026-04-22-missing-delivery-schema-spreadsheet-5a87f2]]

## Summary

**Conversation overview**

This was a long-running technical project session focused on building an interactive HTML reference tool and Jira ticket for implementing dynamic schema.org Product JSON-LD on The Good Guys (TGG) Australia's Shopify PDPs. The person works in SEO and was preparing implementation documentation for a development team. The core task involved mapping purchase state and lifecycle metafield combinations to correct schema outputs (availability, shippingDetails, handlingTime, transitTime), replacing hardcoded values with dynamic ones driven by three Shopify metafields: `tgg.purchase_state`, `tgg.product_life_cycle`, and `tgg.product_state_message`, plus `tgg.web_ready_rule_checks` for lowest lead time.

The person has a direct, impatient communication style and prefers terse corrections ("why the fuck would you include it", "WAY too big"). They catch errors quickly and expect Claude to self-audit before presenting output. They communicate strong preferences: no redundant documentation (e.g. removing "shippingDetails | Yes — include block" rows since it's implicit), no Dyson V8 product references in example JSON (just clean filler values), no fields documented that aren't being actively changed, and Australian English throughout. They flagged multiple mistakes across the session including 0/N transit values that should be locked N/N, a stray `availableAtOrFrom` reference after agreeing to remove it, incorrect price removal from NOT AVAILABLE scenarios, and an SVG scaling issue where `width="100%"` caused the visual to balloon on wider screens. The key correction pattern: Claude added defensive documentation for things not being implemented, and the person consistently removed it.

Confirmed schema rules: all transit values locked min=max (1/1, 2/2, 3/3); PREMIUM OOS transit is 2/2 matching BIG-BULKY; AGENCY-*/DROPSHIP-BB/BUY AT Miele remove `availability`, `seller`, and `shippingDetails` from within the offers block (block stays); only COMING SOON removes the entire offers block; STAND-ALONE-SERVICE and ORDER NOW suppress the entire Product `<script type="application/ld+json">` block while leaving FAQPage and BreadcrumbList unaffected; INCORRECT COMBO removed from documentation entirely; `mainEntityOfPage @type` changes from WebPage to ItemPage globally (one before/after only, not repeated per scenario); current live schema missing `@type: "QuantitativeValue"` on handlingTime/transitTime to be fixed as bundled deployment. Final deliverables: `schema_tool.html` (interactive matrix + Decision Flow SVG tab, dark theme, clickable cells opening a 50vw drawer with before/after JSON, amber/red diff highlighting), `TGG_Schema_Jira_v3.md` (full implementation brief with 19+ before/after JSON pairs), and `tgg_schema_tool.zip` (GitHub-ready Streamlit package). The Decision Flow tab is set as default, contains a node-and-connector SVG tree with clickable outcome cards that open the same drawer as the matrix, and uses fixed 960px width with flex layout filling viewport height via `flex:1; overflow:auto` on panes. TGG logo uses `https://upload.wikimedia.org/wikipedia/commons/3/3b/The_Good_Guys_Logo.png` at 28px height.

## First user message

> _(no user message)_

## Topics

[[topic/feed]], [[topic/jira]], [[topic/pdp]], [[topic/redirect]], [[topic/regex]], [[topic/schema]], [[topic/shopify]]

## Skills referenced

none detected
