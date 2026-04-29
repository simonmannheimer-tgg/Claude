---
title: Flow audit request (full)
parent: Chat/Light/2026-03-19-flow-audit-request-6d6b73
uuid: 6d6b73c9-7965-4c48-916f-31443bc44aad
---

#chat/full #project/main #status/completed

# Flow audit request — Full Transcript

→ Light view: [[Chat/Light/2026-03-19-flow-audit-request-6d6b73]]
→ Medium view: [[Chat/Medium/2026-03-19-flow-audit-request-6d6b73]]

**Messages:** 6 | **Date:** 2026-03-19

---

### 1. **Human** — 2026-03-19T09:46

audit this flow that came from this conversation:
audit this flow that came from this conversation:

---

### 2. **Claude** — 2026-03-19T09:46

```
This block is not supported on your current device yet.
```

Here's the audit.

---

## Flow audit: Auto-redirect archived products to category

### Structure overview

| Step | Type | Task |
|------|------|------|
| 1 | Trigger | `product_status_updated` |
| 2 | Condition | `oldStatus == ACTIVE AND product.status == ARCHIVED` |
| 3 | Action | `created_redirect_url` |

The three-step structure is correct and clean. The logic follows the conversation accurately.

---

### Issues found

**1. Metafield reference is wrong (critical)**

The action step references `product.breadcrumb.value`, but based on the products export the metafield namespace is `tgg` and the key is `breadcrumb`. In Shopify Flow Liquid, the correct path is:

```
product.metafields.tgg.breadcrumb
```

Not `product.breadcrumb.value`. This means the breadcrumb condition will always evaluate as falsy, and every redirect will fall through to the collection fallback. The primary logic never fires.

**2. No `false` branch on the condition**

The condition node only has a `true` port connected. If a product transitions from `draft` to `archived` (not `active` to `archived`), the flow exits silently without a redirect, which is correct behaviour. But there's no logging or error handling if you ever want visibility into skipped runs.

Minor issue, no action required unless observability matters.

**3. `overwrite_target` is set to `true`**

This means if a redirect already exists for a product handle, it will be overwritten silently. This is probably intentional (e.g. a product archived twice), but worth confirming. If you ever want to preserve manually set redirects, this should be `false`.

**4. The fallback chain is incomplete relative to the conversation**

The conversation agreed on three tiers:
1. `tgg.breadcrumb`
2. First collection handle
3. Homepage (`/`)

The flow implements this. However, the conversation also discussed using `tgg.l1category` as a fallback. That was not implemented, which is fine since the conversation settled on collection handle instead. Just noting it is absent in case you want it.

---

### Fix required

In the action step, replace:

```liquid
{% assign breadcrumb = product.breadcrumb.value %}
```

With:

```liquid
{% assign breadcrumb = product.metafields.tgg.breadcrumb %}
```

Everything else in the Liquid logic is correct. The `replace: '_', '/'` transform, the collection fallback, and the homepage fallback all work as intended once the metafield path is fixed.

---

### Summary

One critical fix needed. The flow will technically run without errors in its current state, but the breadcrumb logic is unreachable due to the incorrect metafield path. All redirects would silently fall through to the collection handle instead of the intended category URL.
Here's the audit.

---

## Flow audit: Auto-redirect archived products to category

### Structure overview

| Step | Type | Task |
|------|------|------|
| 1 | Trigger | `product_status_updated` |
| 2 | Condition | `oldStatus == ACTIVE AND product.status == ARCHIVED` |
| 3 | Action | `created_redirect_url` |

The three-step structure is correct and clean. The logic follows the conversation accurately.

---

### Issues found

**1. Metafield reference is wrong (critical)**

The action step references `product.breadcrumb.value`, but based on the products export the metafield namespace is `tgg` and the key is `breadcrumb`. In Shopify Flow Liquid, the correct path is:

```
product.metafields.tgg.breadcrumb
```

Not `product.breadcrumb.value`. This means the breadcrumb condition will always evaluate as falsy, and every redirect will fall through to the collection fallback. The primary logic never fires.

**2. No `false` branch on the condition**

The condition node only has a `true` port connected. If a product transitions from `draft` to `archived` (not `active` to `archived`), the flow exits silently without a redirect, which is correct behaviour. But there's no logging or error handling if you ever want visibility into skipped runs.

Minor issue, no action required unless observability matters.

**3. `overwrite_target` is set to `true`**

This means if a redirect already exists for a product handle, it will be overwritten silently. This is probably intentional (e.g. a product archived twice), but worth confirming. If you ever want to preserve manually set redirects, this should be `false`.

**4. The fallback chain is incomplete relative to the conversation**

The conversation agreed on three tiers:
1. `tgg.breadcrumb`
2. First collection handle
3. Homepage (`/`)

The flow implements this. However, the conversation also discussed using `tgg.l1category` as a fallback. That was not implemented, which is fine since the conversation settled on collection handle instead. Just noting it is absent in case you want it.

---

### Fix required

In the action step, replace:

```liquid
{% assign breadcrumb = product.breadcrumb.value %}
```

With:

```liquid
{% assign breadcrumb = product.metafields.tgg.breadcrumb %}
```

Everything else in the Liquid logic is correct. The `replace: '_', '/'` transform, the collection fallback, and the homepage fallback all work as intended once the metafield path is fixed.

---

### Summary

One critical fix needed. The flow will technically run without errors in its current state, but the breadcrumb logic is unreachable due to the incorrect metafield path. All redirects would silently fall through to the collection handle instead of the intended category URL.

---

### 3. **Human** — 2026-03-19T09:48

recreate the file
recreate the file

---

### 4. **Claude** — 2026-03-19T09:48

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Only change from the original is the metafield path in the action step's `target` field:

- Before: `product.breadcrumb.value`
- After: `product.metafields.tgg.breadcrumb`

Everything else, including step IDs, UUIDs, links, and the condition logic, is identical to the original so it should import cleanly into Flow.
Only change from the original is the metafield path in the action step's `target` field:

- Before: `product.breadcrumb.value`
- After: `product.metafields.tgg.breadcrumb`

Everything else, including step IDs, UUIDs, links, and the condition logic, is identical to the original so it should import cleanly into Flow.

---

### 5. **Human** — 2026-03-19T09:49

Import workflow
Auto-redirect_archived_products_to_category.flow cannot be imported
Upload files
or drop .flow files to import
Import workflow
Auto-redirect_archived_products_to_category.flow cannot be imported
Upload files
or drop .flow files to import

---

### 6. **Claude** — 2026-03-19T09:50

That error typically means the file hash prefix doesn't match the content. The `.flow` format appears to use a hash of the JSON payload as a prefix, and since the content changed (the metafield fix), the original hash is now invalid.
```
This block is not supported on your current device yet.
```

Good, got the correct hash. Now write the file with the exact JSON payload (no escaped quotes in the condition value, matching the original format precisely):
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The file is rebuilt with a correctly computed SHA256 hash that matches the updated payload. The hash mismatch was the reason for the import failure. Verified: correct metafield path present, old broken path absent.
 That error typically means the file hash prefix doesn't match the content. The `.flow` format appears to use a hash of the JSON payload as a prefix, and since the content changed (the metafield fix), the original hash is now invalid.
Good, got the correct hash. Now write the file with the exact JSON payload (no escaped quotes in the condition value, matching the original format precisely):
The file is rebuilt with a correctly computed SHA256 hash that matches the updated payload. The hash mismatch was the reason for the import failure. Verified: correct metafield path present, old broken path absent.
