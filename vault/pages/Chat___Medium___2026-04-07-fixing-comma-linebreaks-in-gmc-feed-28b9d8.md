---
title: Fixing comma linebreaks in GMC feed (medium)
parent: Chat/Light/2026-04-07-fixing-comma-linebreaks-in-gmc-feed-28b9d8
uuid: 28b9d837-95a4-48b8-9587-aeb766abd343
---

#chat/medium #project/gmc-feed-audit-delimiter-conflict #status/completed

# Fixing comma linebreaks in GMC feed — Key User Messages

→ Light view: [[Chat/Light/2026-04-07-fixing-comma-linebreaks-in-gmc-feed-28b9d8]]
→ Full transcript: [[Chat/Full/2026-04-07-fixing-comma-linebreaks-in-gmc-feed-28b9d8]]

**Total user messages:** 7

---

### Message 1 — 2026-04-07T02:05

our product highlights in gmc feed has commas, it breaks the feed:

how can i fix it?

Intelligent reach said theres no good way to dis-allow comma breaks in these... we likely need a bulk replace option
[12:04 PM]
and it needs to work in various formats, whether the comma is for a list, for emphasis...
[12:04 PM]
is there a comma symbol that wouldnt register as a linebreak?
our product highlights in gmc feed has commas, it breaks the feed:

how can i fix it?

Intelligent reach said theres no good way to dis-allow comma breaks in these... we likely need a bulk replace option
[12:04 PM]
and it needs to work in various formats, whether the comma is for a list, for emphasis...
[12:04 PM]
is there a comma symbol that wouldnt register as a linebreak?

### Message 2 — 2026-04-07T02:19

what tool is this gmc audit form?
11:45
This is a Google Merchant Center (GMC) feed audit form — specifically showing the product data fields that are submitted to Google Shopping for a Shark vacuum cleaner product.
The screenshot shows attribute-value pairs from a product feed, with fields like `product_highlight`, `product_type`, `shipping_label`, `im_beauty_brand` (internal merchant fields), and `im_product_category`. This is typical output from either:
1. Google Merchant Center diagnostics (the Feed diagnostics tab or Item issues view)
2. A Supplemental feed or manual feed review export from GMC
3. A feed management platform like Feedonomics, DataFeedWatch, or an internal TGG feed tool
The "im_" prefix on several fields (`im_beauty_brand`, `im_colour`, `im_product_category`, `im_product_name`) indicates custom internal merchant labels — these are TGG's own categorisation or enrichment fields, not standard Google Shopping taxonomy.
Why this matters for your feed audit work:
The `product_highlight` field has comma separation issues — you've mentioned this before with refrigeration SKUs. Here I can see multiple `product_highlight` rows, which suggests either:
* Multiple highlights stacked as separate rows (incorrect — should be pipe-delimited in a single field), or
* The export is showing each highlight on its own line for readability
If this is the Searchspring export or a raw feed dump, you'd want to verify that the actual feed file encodes these highlights correctly (pipe

[truncated — see full transcript]

### Message 3 — 2026-04-07T02:34

there is no scenario where we will be able to tell people to never use commas when entering key features (each of which becomes a line)

there are two things:

one is the csv line that pulls in the key features:

Carpet stain remover for cleaning carpets and rugs,1 Litre capacity for multiple uses

then in some cases there may be issues where it separates due to commas WITHIN each feature:

1.6 Litre bin capacity with bagless design,1700 Watt power, 3D fine dust and D11 filter, for hard floors, tiles and carpets,Pet friendly design tackles animal hair with ease,3 Tools in one for dusting, upholstery and crevices

see the difference between a comma WITHIN a feature and a comma separating a feature?
there is no scenario where we will be able to tell people to never use commas when entering key features (each of which becomes a line)

there are two things:

one is the csv line that pulls in the key features:

Carpet stain remover for cleaning carpets and rugs,1 Litre capacity for multiple uses

then in some cases there may be issues where it separates due to commas WITHIN each feature:

1.6 Litre bin capacity with bagless design,1700 Watt power, 3D fine dust and D11 filter, for hard floors, tiles and carpets,Pet friendly design tackles animal hair with ease,3 Tools in one for dusting, upholstery and crevices

see the difference between a comma WITHIN a feature and a comma separating a feature?

### Message 4 — 2026-04-07T03:22

this is how they are set up in our shopify system (see metafield) - I need a list of any key feature that has comma within it
this is how they are set up in our shopify system (see metafield) - I need a list of any key feature that has comma within it

### Message 5 — 2026-04-07T03:24

within these?

Metafield: tgg.key_features [json]
within these?

Metafield: tgg.key_features [json]

### Message 6 — 2026-04-07T03:26

write a quick regex for 

"value":".*,.*"
write a quick regex for 

"value":".*,.*"

### Message 7 — 2026-04-07T03:27

these?
these?
