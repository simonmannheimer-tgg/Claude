---
title: Shopify redirect sheet creation from archived products (medium)
parent: Chat/Light/2026-03-20-shopify-redirect-sheet-creation-from-archived-products-011429
uuid: 011429c6-dcdb-4e20-b1ca-b0af8bf42264
---

#chat/medium #project/main #status/completed

# Shopify redirect sheet creation from archived products — Key User Messages

→ Light view: [[Chat/Light/2026-03-20-shopify-redirect-sheet-creation-from-archived-products-011429]]
→ Full transcript: [[Chat/Full/2026-03-20-shopify-redirect-sheet-creation-from-archived-products-011429]]

**Total user messages:** 11

---

### Message 1 — 2026-03-19T22:46

I will give you a number of archived products out of shopify - I want you to use the spreadsheets and the same logic shared in this flow to create a shopify Redirect Sheet import:

2977b26c27efcd10f0883172b7fc881800d46505d4392bdebba64aceccce3116:{"__metadata":{"version":0.1},"root":{"steps":[{"step_id":"12e4e0b3-a3af-484f-9ae2-6f8367843372","step_position":[0,0],"config_field_values":[],"task_id":"shopify::admin::product_status_updated","task_version":"0.1","task_type":"TRIGGER","description":null,"note":null,"name":null},{"step_id":"fb69a597-af7f-4a65-b515-cc268d78c968","step_position":[0,200],"config_field_values":[{"config_field_id":"condition","value":"{\"uuid\":\"01KM2QPS5X0FRDK72K10ZR44H7\",\"lhs\":{\"uuid\":\"01KM2QPS5XJVRXAAN3596NT6XB\",\"parent_uuid\":\"01KM2QPS5X0FRDK72K10ZR44H7\",\"lhs\":{\"uuid\":\"01KM2QPS5XRKNSM1J7XXNDXHHA\",\"parent_uuid\":\"01KM2QPS5XJVRXAAN3596NT6XB\",\"value\":\"oldStatus\",\"comparison_value_type\":\"EnvironmentValue\",\"full_environment_path\":\"oldStatus\"},\"rhs\":{\"uuid\":\"01KM2QPS5XFN3R28YRY25XR8MD\",\"parent_uuid\":\"01KM2QPS5XJVRXAAN3596NT6XB\",\"value\":\"ACTIVE\",\"comparison_value_type\":\"LiteralValue\"},\"value_type\":\"EnvironmentEnumDefinition:ProductStatus\",\"operator\":\"==\",\"operation_type\":\"Comparison\"},\"rhs\":{\"uuid\":\"01KM2QPS5X83GCGBABWMARE4TK\",\"parent_uuid\":\"01KM2QPS5X0FRDK72K10ZR44H7\",\"lhs\":{\"uuid\":\"01KM2QPS5XYPSDZGQ5SXCQ2JVW\",\"parent_uuid\":\"01KM2QPS5X83GCGBABWMARE4TK\",\"value\":\"product.sta

[truncated — see full transcript]

### Message 2 — 2026-03-19T22:47

no, sitemap audit doc is not for broken URLs - it is to understand the logic of URLs and build a logic by similarity, my thinking:

if i give you a broken URL and it is 99% similar to a live URL, then use that Live URls breadcrumb as the recommended redirect
no, sitemap audit doc is not for broken URLs - it is to understand the logic of URLs and build a logic by similarity, my thinking:

if i give you a broken URL and it is 99% similar to a live URL, then use that Live URls breadcrumb as the recommended redirect

### Message 3 — 2026-03-19T23:10

you already have the list - i attached it before
you already have the list - i attached it before

### Message 4 — 2026-03-19T23:11

dont forget about using the breadcrumb from the export, like i shared from shopofy floow
dont forget about using the breadcrumb from the export, like i shared from shopofy floow

### Message 5 — 2026-03-19T23:12

soo theres 2 versions:

1. exports where status is not active - create import doc for shopipfy redirecting to the breadcrumb url after having cleanied itup 
2. 404s that arent in shopofy, that we need to use logic to redirect.
soo theres 2 versions:

1. exports where status is not active - create import doc for shopipfy redirecting to the breadcrumb url after having cleanied itup 
2. 404s that arent in shopofy, that we need to use logic to redirect.

### Message 6 — 2026-03-19T23:12

do the ones we know 100% are 404s (archived ones)
do the ones we know 100% are 404s (archived ones)

### Message 7 — 2026-03-19T23:26



### Message 8 — 2026-03-19T23:37

Continue
Continue

### Message 9 — 2026-03-19T23:38

do the currently archived ones in shopify - use the breadcrumb logic from shopify flow i shared to map and produce a import sheet
do the currently archived ones in shopify - use the breadcrumb logic from shopify flow i shared to map and produce a import sheet

### Message 10 — 2026-03-19T23:39

dont include default sku or anything that loooks like its part of a bigger process
dont include default sku or anything that loooks like its part of a bigger process

### Message 11 — 2026-03-19T23:39

no ignore that last, just dont redirect default-sku
no ignore that last, just dont redirect default-sku
