---
title: Dynamic schema mapping for lifecycle states
date: 2026-04-24
project: Delivery Schema — 9x5 Purchase State Matrix
status: active
score: 5/5
uuid: c6151f6e-501e-45a9-8586-87da6d825d77
---

#chat/light #project/delivery-schema-9x5-purchase-state-matri #status/active #topic/feed #topic/jira #topic/schema #topic/shopify

# Dynamic schema mapping for lifecycle states

- **Date:** [[2026-04-24]]
- **Project:** [[Projects/Delivery Schema — 9x5 Purchase State Matrix]]
- **Status:** #status/active (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 9
- **Chat URL:** https://claude.ai/chat/c6151f6e-501e-45a9-8586-87da6d825d77
- **Medium view:** [[Chat/Medium/2026-04-24-dynamic-schema-mapping-for-lifecycle-states-c6151f]]
- **Full transcript:** [[Chat/Full/2026-04-24-dynamic-schema-mapping-for-lifecycle-states-c6151f]]

## Summary

**Conversation Overview**

Simon Mannheimer, SEO Lead at The Good Guys (thegoodguys.com.au), is working on a structured data implementation project mapping product purchase states to Schema.org JSON-LD markup. The session involved resuming interrupted work from a prior compacted conversation. The source material is a spreadsheet (`Delivery_Schema.xlsx`) containing a 9×5 matrix where rows represent nine purchase states (In Stock, OOS, Order Now/Services, Buy at Miele, Sold Out, Pre-Order, Coming Soon, Not Available, In-Store Only) and columns represent five fulfilment lifecycle types (Parcelised, Big & Bulky, Digital, Agency/Doorship, Pre-Order Type), with each cell containing handling (H) and transit (D) day values.

The prior session had produced an interactive HTML visualisation board and begun a Jira brief, both of which were delivered in this session. However, Simon provided several important corrections: the HTML file had a height compression issue; the token/field references should draw from actual product feed exports rather than native Shopify fields; dynamic tokens should only be applied to the parts of the schema that actually change between products, not structural elements; and critically, the original intent was a Miro board-style interface and a Jira ticket format, not the general Markdown brief that was produced. The session ended with Simon articulating these corrections before revised deliverables were created.

Key domain terminology in use includes: schema.org availability values (`InStock`, `BackOrder`, `OutOfStock`, `PreOrder`, `PreSale`, `Discontinued`, `InStoreOnly`), `shippingDetails`, `OfferShippingDetails`, `ShippingDeliveryTime`, `transitTime`, `handlingTime`, JSON-LD, and the `tgg` metafield namespace. Simon's working style favours precision in implementation specs and is attentive to the distinction between static schema structure and dynamic populated values. The corrections in this session establish a clear pattern: future work should reference export-based field names, minimise tokenisation to genuinely variable fields only, and match the requested output format (Miro board aesthetic for the visual, single Jira ticket format for the brief) rather than interpreting the format loosely.

## First user message

> I need you to create a miro board file that maps each instance to an example schema snippet - it should be dynamic like {{Lifecyle}} and {{Pre-order available date}} etc.  I need a visualisation and also a Jira brief for what schema should be used for each combionation of states and what it should pull from where. I need you to create a miro board file that maps each instance to an example schema 

## Topics

[[topic/feed]], [[topic/jira]], [[topic/schema]], [[topic/shopify]]

## Skills referenced

none detected
