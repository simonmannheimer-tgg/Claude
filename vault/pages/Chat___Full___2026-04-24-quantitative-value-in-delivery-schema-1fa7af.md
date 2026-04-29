---
title: Quantitative value in delivery schema (full)
parent: Chat/Light/2026-04-24-quantitative-value-in-delivery-schema-1fa7af
uuid: 1fa7afec-7a5d-41e5-a4a2-9bd900bdb6f7
---

#chat/full #project/main #status/active

# Quantitative value in delivery schema — Full Transcript

→ Light view: [[Chat/Light/2026-04-24-quantitative-value-in-delivery-schema-1fa7af]]
→ Medium view: [[Chat/Medium/2026-04-24-quantitative-value-in-delivery-schema-1fa7af]]

**Messages:** 4 | **Date:** 2026-04-24

---

### 1. **Human** — 2026-04-24T04:27

during our chats aboout delivery schema you said quantitative value was missing - show proof of this?
during our chats aboout delivery schema you said quantitative value was missing - show proof of this?

---

### 2. **Claude** — 2026-04-24T04:27

```
This block is not supported on your current device yet.
```

Found it. Here's the relevant excerpt from the April 22 session:

> The Before blocks reflect the current live schema, which omits explicit `@type` on nested objects. The After blocks add `"@type": "OfferShippingDetails"`, `"@type": "ShippingDeliveryTime"`, **`"@type": "QuantitativeValue"`**.

That note was written at your request, under the Scenarios section of `TGG_Schema_Jira_v3.md`. The claim was that the live schema omits `@type` on `handlingTime` and `transitTime`, meaning parsers were left to infer `QuantitativeValue` from context rather than it being declared explicitly.

That was the framing used. Worth noting: this was written as a rationale you drafted the prompt for, not something surfaced independently by analysis of your actual live schema output. If you want to verify whether `"@type": "QuantitativeValue"` is genuinely absent from your current live JSON-LD, that requires pulling a real PDP and checking the rendered schema, not the Jira doc.
Found it. Here's the relevant excerpt from the April 22 session:

> The Before blocks reflect the current live schema, which omits explicit `@type` on nested objects. The After blocks add `"@type": "OfferShippingDetails"`, `"@type": "ShippingDeliveryTime"`, **`"@type": "QuantitativeValue"`**.

That note was written at your request, under the Scenarios section of `TGG_Schema_Jira_v3.md`. The claim was that the live schema omits `@type` on `handlingTime` and `transitTime`, meaning parsers were left to infer `QuantitativeValue` from context rather than it being declared explicitly.

That was the framing used. Worth noting: this was written as a rationale you drafted the prompt for, not something surfaced independently by analysis of your actual live schema output. If you want to verify whether `"@type": "QuantitativeValue"` is genuinely absent from your current live JSON-LD, that requires pulling a real PDP and checking the rendered schema, not the Jira doc.

---

### 3. **Human** — 2026-04-24T04:28

was it ever shown?
was it ever shown?

---

### 4. **Claude** — 2026-04-24T04:28

No. The search results show the claim appeared only in the Jira note you asked me to write. There's no transcript evidence of anyone pulling a live PDP, running a schema validator, or displaying actual rendered JSON-LD that confirmed `"@type": "QuantitativeValue"` was missing.

It was asserted in a note, not demonstrated.
 No. The search results show the claim appeared only in the Jira note you asked me to write. There's no transcript evidence of anyone pulling a live PDP, running a schema validator, or displaying actual rendered JSON-LD that confirmed `"@type": "QuantitativeValue"` was missing.

It was asserted in a note, not demonstrated.
