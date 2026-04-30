---
title: Global Change schema markup verification (full)
parent: Chat/Light/2026-04-22-global-change-schema-markup-verification-9da14d
uuid: 9da14d14-2a4c-4ebe-a7df-eb290e1423f8
---

#chat/full #project/main #status/completed

# Global Change schema markup verification — Full Transcript

→ Light view: [[Chat/Light/2026-04-22-global-change-schema-markup-verification-9da14d]]
→ Medium view: [[Chat/Medium/2026-04-22-global-change-schema-markup-verification-9da14d]]

**Messages:** 2 | **Date:** 2026-04-22

---

### 1. **Human** — 2026-04-22T03:10

review: 

do reaserch, tell me if Global Change (apply to all PDPs regardless of state)
In mainEntityOfPage, change @type from "WebPage" to "ItemPage". is correct
review: 

do reaserch, tell me if Global Change (apply to all PDPs regardless of state)
In mainEntityOfPage, change @type from "WebPage" to "ItemPage". is correct

---

### 2. **Claude** — 2026-04-22T03:10

The user wants me to research whether changing mainEntityOfPage @type from "WebPage" to "ItemPage" is correct for product pages.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Let me check the Google product structured data docs more carefully and also the schema.org ItemPage definition.
```
This block is not supported on your current device yet.
```

The evidence is clear. ItemPage is the correct type for product detail pages. It's a subtype of WebPage specifically defined as "a page devoted to a single item, such as a particular product or hotel." This is correct for TGG PDPs.

Let me also quickly check if Google's own product structured data documentation mentions ItemPage specifically.The change is correct. Here's the verdict:

`ItemPage` is defined by Schema.org as "a page devoted to a single item, such as a particular product or hotel." It is a subtype of `WebPage`, so it is strictly more specific and semantically accurate for a PDP. Using `WebPage` is not wrong, but it is imprecise.

Schema.org's own documentation uses `ItemPage` wrapping a `Product` as the canonical example for product detail pages.

**Verdict: correct change, make it.**

One caveat worth flagging: Google's product structured data documentation does not explicitly mandate `ItemPage` over `WebPage` in `mainEntityOfPage`. Google focuses on the `Product` entity, not the page type wrapper. So this change improves semantic accuracy but is unlikely to directly unlock or break any rich result eligibility. It is still the right call.
 
The change is correct. Here's the verdict:

`ItemPage` is defined by Schema.org as "a page devoted to a single item, such as a particular product or hotel." It is a subtype of `WebPage`, so it is strictly more specific and semantically accurate for a PDP. Using `WebPage` is not wrong, but it is imprecise.

Schema.org's own documentation uses `ItemPage` wrapping a `Product` as the canonical example for product detail pages.

**Verdict: correct change, make it.**

One caveat worth flagging: Google's product structured data documentation does not explicitly mandate `ItemPage` over `WebPage` in `mainEntityOfPage`. Google focuses on the `Product` entity, not the page type wrapper. So this change improves semantic accuracy but is unlikely to directly unlock or break any rich result eligibility. It is still the right call.
