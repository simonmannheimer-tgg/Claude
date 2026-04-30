---
title: Regex pattern for sale terminology (full)
parent: Chat/Light/2026-04-22-regex-pattern-for-sale-terminology-f945f3
uuid: f945f382-3a40-4c0c-a8ad-2fd78d8f26af
---

#chat/full #project/main #status/completed

# Regex pattern for sale terminology — Full Transcript

→ Light view: [[Chat/Light/2026-04-22-regex-pattern-for-sale-terminology-f945f3]]
→ Medium view: [[Chat/Medium/2026-04-22-regex-pattern-for-sale-terminology-f945f3]]

**Messages:** 2 | **Date:** 2026-04-22

---

### 1. **Human** — 2026-04-22T03:18

regex for any type of sale term"

sale|offer etc.
regex for any type of sale term"

sale|offer etc.

---

### 2. **Claude** — 2026-04-22T03:18

The user wants a regex for sale/offer type terms. Let me think about common sale terms in ecommerce/retail context.```regex
\b(sale|offer|deal|discount|clearance|promo(?:tion)?|markdown|price.?drop|saving|bargain|special|reduced|off(?:er)?|bundle|freebie|cashback|rebate|bonus|gift|free\s+shipping|limited.?time|flash\s+sale|daily\s+deal|mega\s+sale|super\s+sale|big\s+sale|hot\s+deal|best\s+deal|buy\s+one|BOGO|half.?price|percent\s+off|%\s*off)\b
```

Case-insensitive flag (`i`) assumed. Adjust word boundary behaviour if matching inside URLs or slugs, where `\b` can fail on hyphens.

Want a PCRE version, or scoped to a specific context (GSC, Shopify metafields, Python)?
 
```regex
\b(sale|offer|deal|discount|clearance|promo(?:tion)?|markdown|price.?drop|saving|bargain|special|reduced|off(?:er)?|bundle|freebie|cashback|rebate|bonus|gift|free\s+shipping|limited.?time|flash\s+sale|daily\s+deal|mega\s+sale|super\s+sale|big\s+sale|hot\s+deal|best\s+deal|buy\s+one|BOGO|half.?price|percent\s+off|%\s*off)\b
```

Case-insensitive flag (`i`) assumed. Adjust word boundary behaviour if matching inside URLs or slugs, where `\b` can fail on hyphens.

Want a PCRE version, or scoped to a specific context (GSC, Shopify metafields, Python)?
