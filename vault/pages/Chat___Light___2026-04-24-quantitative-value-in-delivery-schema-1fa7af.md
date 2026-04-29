---
title: Quantitative value in delivery schema
date: 2026-04-24
project: main
status: active
score: 2/5
uuid: 1fa7afec-7a5d-41e5-a4a2-9bd900bdb6f7
---

#chat/light #project/main #status/active #topic/jira #topic/pdp #topic/schema

# Quantitative value in delivery schema

- **Date:** [[2026-04-24]]
- **Project:** [[Projects/main]]
- **Status:** #status/active (score 2/5: deliverable, project-keyword)
- **Messages:** 4
- **Chat URL:** https://claude.ai/chat/1fa7afec-7a5d-41e5-a4a2-9bd900bdb6f7
- **Medium view:** [[Chat/Medium/2026-04-24-quantitative-value-in-delivery-schema-1fa7af]]
- **Full transcript:** [[Chat/Full/2026-04-24-quantitative-value-in-delivery-schema-1fa7af]]

## Summary

**Conversation Overview**

The person asked Claude to provide proof of a prior claim made during previous conversations about a delivery schema — specifically that a quantitative value type was missing from the live schema. Claude used a conversation search tool to locate the relevant reference, which appeared in a document called `TGG_Schema_Jira_v3.md` from an April 22 session. The document described before/after schema blocks where `"@type": "QuantitativeValue"` was identified as absent from the live schema's `handlingTime` and `transitTime` nested objects.

The person then followed up asking whether the missing value had ever actually been demonstrated. Claude clarified that no, it had not — the claim existed only as an assertion within the Jira note, and there was no evidence in the conversation history of anyone pulling a live PDP, running a schema validator, or displaying real rendered JSON-LD to confirm the omission. Claude distinguished between the claim being written into a document versus being independently verified against actual live schema output.

The key domain context involves JSON-LD structured data schema work, likely for product detail pages (PDPs), using vocabulary including `OfferShippingDetails`, `ShippingDeliveryTime`, and `QuantitativeValue`. The project references a Jira documentation file (`TGG_Schema_Jira_v3.md`), suggesting an ongoing technical schema implementation effort.

## First user message

> during our chats aboout delivery schema you said quantitative value was missing - show proof of this? during our chats aboout delivery schema you said quantitative value was missing - show proof of this?

## Topics

[[topic/jira]], [[topic/pdp]], [[topic/schema]]

## Skills referenced

none detected
