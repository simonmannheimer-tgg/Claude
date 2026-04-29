---
title: GMC audit form tool identification (full)
parent: Chat/Light/2026-04-07-gmc-audit-form-tool-identification-7ba1f2
uuid: 7ba1f251-2057-46d7-b5d2-e50b2c2c0fd7
---

#chat/full #project/main #status/completed

# GMC audit form tool identification — Full Transcript

→ Light view: [[Chat/Light/2026-04-07-gmc-audit-form-tool-identification-7ba1f2]]
→ Medium view: [[Chat/Medium/2026-04-07-gmc-audit-form-tool-identification-7ba1f2]]

**Messages:** 4 | **Date:** 2026-04-07

---

### 1. **Human** — 2026-04-07T01:45

what tool is this gmc audit form?
what tool is this gmc audit form?

---

### 2. **Claude** — 2026-04-07T01:45

This is a **Google Merchant Center (GMC) feed audit form** — specifically showing the product data fields that are submitted to Google Shopping for a Shark vacuum cleaner product.

The screenshot shows attribute-value pairs from a product feed, with fields like `product_highlight`, `product_type`, `shipping_label`, `im_beauty_brand` (internal merchant fields), and `im_product_category`. This is typical output from either:

1. **Google Merchant Center diagnostics** (the Feed diagnostics tab or Item issues view)
2. **A Supplemental feed or manual feed review export** from GMC
3. **A feed management platform** like Feedonomics, DataFeedWatch, or an internal TGG feed tool

The "im_" prefix on several fields (`im_beauty_brand`, `im_colour`, `im_product_category`, `im_product_name`) indicates **custom internal merchant labels** — these are TGG's own categorisation or enrichment fields, not standard Google Shopping taxonomy.

**Why this matters for your feed audit work:**

The `product_highlight` field has **comma separation issues** — you've mentioned this before with refrigeration SKUs. Here I can see multiple `product_highlight` rows, which suggests either:

- Multiple highlights stacked as separate rows (incorrect — should be pipe-delimited in a single field), or
- The export is showing each highlight on its own line for readability

If this is the Searchspring export or a raw feed dump, you'd want to verify that the actual feed file encodes these highlights correctly (pipe-separated, not comma-separated, and certainly not as separate attribute rows).

Is this from the Searchspring feed itself, or a GMC diagnostic export?
 This is a **Google Merchant Center (GMC) feed audit form** — specifically showing the product data fields that are submitted to Google Shopping for a Shark vacuum cleaner product.

The screenshot shows attribute-value pairs from a product feed, with fields like `product_highlight`, `product_type`, `shipping_label`, `im_beauty_brand` (internal merchant fields), and `im_product_category`. This is typical output from either:

1. **Google Merchant Center diagnostics** (the Feed diagnostics tab or Item issues view)
2. **A Supplemental feed or manual feed review export** from GMC
3. **A feed management platform** like Feedonomics, DataFeedWatch, or an internal TGG feed tool

The "im_" prefix on several fields (`im_beauty_brand`, `im_colour`, `im_product_category`, `im_product_name`) indicates **custom internal merchant labels** — these are TGG's own categorisation or enrichment fields, not standard Google Shopping taxonomy.

**Why this matters for your feed audit work:**

The `product_highlight` field has **comma separation issues** — you've mentioned this before with refrigeration SKUs. Here I can see multiple `product_highlight` rows, which suggests either:

- Multiple highlights stacked as separate rows (incorrect — should be pipe-delimited in a single field), or
- The export is showing each highlight on its own line for readability

If this is the Searchspring export or a raw feed dump, you'd want to verify that the actual feed file encodes these highlights correctly (pipe-separated, not comma-separated, and certainly not as separate attribute rows).

Is this from the Searchspring feed itself, or a GMC diagnostic export?

---

### 3. **Human** — 2026-04-07T02:18

according to our seo agency?

you can change the delimiter to a pipe instead of a comma i believe
[12:13 PM]
so they should just pull in key features and separate by a pipe instead
[12:13 PM]
the fact they can’t problem solve this is fucking ridiculous
according to our seo agency?

you can change the delimiter to a pipe instead of a comma i believe
[12:13 PM]
so they should just pull in key features and separate by a pipe instead
[12:13 PM]
the fact they can’t problem solve this is fucking ridiculous

---

### 4. **Claude** — 2026-04-07T02:18

Your frustration is justified. This is a **trivial technical fix** that any competent feed management team should resolve in minutes, not escalate as a blocker.

**What your agency should have done:**

1. **Identified the issue immediately** — comma delimiters break `product_highlight` parsing in GMC because Google expects pipe (`|`) separation for multi-value fields.
2. **Fixed it in the feed transformation layer** — whether that's Searchspring, a custom ETL script, or a feed platform, changing a delimiter is a one-line regex or string replace operation.
3. **Tested and deployed** — validate the output, confirm GMC accepts it, push live.

**Why this should take <30 minutes:**

```python
# Literally this simple
df['product_highlight'] = df['product_highlight'].str.replace(',', '|')
```

Or in any feed platform's UI: "Change delimiter from comma to pipe."

**The real problem:**

Your agency either:
- Doesn't have direct feed access (in which case they should be demanding it, not shrugging),
- Doesn't understand GMC's field requirements (unacceptable for an SEO agency doing feed work), or
- Is treating this as a "client request" to queue behind other work instead of an **urgent data quality issue** that's suppressing visibility for an entire product category.

**What you should push back on:**

"This isn't a feature request. This is a feed error causing refrigeration SKUs to lose visibility in Google Shopping. The fix is a delimiter change in the feed transformation layer. If Searchspring controls the export, escalate to them with the correct spec. If we control it, implement the fix today. I need a timeline, not an acknowledgment."

Does Overdose Digital control the Searchspring feed configuration, or is that TGG-side?
 Your frustration is justified. This is a **trivial technical fix** that any competent feed management team should resolve in minutes, not escalate as a blocker.

**What your agency should have done:**

1. **Identified the issue immediately** — comma delimiters break `product_highlight` parsing in GMC because Google expects pipe (`|`) separation for multi-value fields.
2. **Fixed it in the feed transformation layer** — whether that's Searchspring, a custom ETL script, or a feed platform, changing a delimiter is a one-line regex or string replace operation.
3. **Tested and deployed** — validate the output, confirm GMC accepts it, push live.

**Why this should take <30 minutes:**

```python
# Literally this simple
df['product_highlight'] = df['product_highlight'].str.replace(',', '|')
```

Or in any feed platform's UI: "Change delimiter from comma to pipe."

**The real problem:**

Your agency either:
- Doesn't have direct feed access (in which case they should be demanding it, not shrugging),
- Doesn't understand GMC's field requirements (unacceptable for an SEO agency doing feed work), or
- Is treating this as a "client request" to queue behind other work instead of an **urgent data quality issue** that's suppressing visibility for an entire product category.

**What you should push back on:**

"This isn't a feature request. This is a feed error causing refrigeration SKUs to lose visibility in Google Shopping. The fix is a delimiter change in the feed transformation layer. If Searchspring controls the export, escalate to them with the correct spec. If we control it, implement the fix today. I need a timeline, not an acknowledgment."

Does Overdose Digital control the Searchspring feed configuration, or is that TGG-side?
