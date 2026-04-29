---
title: Flow audit request
date: 2026-03-19
project: Shopify Flow Bug Fix (SHA256 Hash)
status: completed
score: 4/5
uuid: 6d6b73c9-7965-4c48-916f-31443bc44aad
---

#chat/light #project/shopify-flow-bug-fix-sha256-hash #status/completed #topic/redirect #topic/shopify

# Flow audit request

- **Date:** [[2026-03-19]]
- **Project:** [[Projects/Shopify Flow Bug Fix (SHA256 Hash)]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, 5+turns, project-keyword)
- **Messages:** 6
- **Chat URL:** https://claude.ai/chat/6d6b73c9-7965-4c48-916f-31443bc44aad
- **Medium view:** [[Chat/Medium/2026-03-19-flow-audit-request-6d6b73]]
- **Full transcript:** [[Chat/Full/2026-03-19-flow-audit-request-6d6b73]]

## Summary

**Conversation Overview**

The person is working with Shopify Flow and needed help auditing and fixing an existing workflow file called "Auto-redirect archived products to category." The flow's purpose is to automatically create URL redirects when products are archived, routing visitors to an appropriate category page using a three-tier fallback: a custom metafield value, the product's first collection handle, or the homepage.

Claude audited the uploaded `.flow` file and identified one critical bug: the action step referenced `product.breadcrumb.value` instead of the correct Shopify Flow Liquid path `product.metafields.tgg.breadcrumb` (namespace: `tgg`, key: `breadcrumb`). This meant the primary redirect logic was unreachable and all redirects silently fell through to the collection handle fallback. Claude also noted minor observations about the missing false branch on the condition node and the `overwrite_target: true` setting.

Claude then recreated the corrected `.flow` file, but the initial recreation failed to import into Shopify Flow. Claude diagnosed the issue as a hash mismatch: the `.flow` format uses a SHA256 hash of the JSON payload as a file prefix, and since the content changed, the original hash was invalid. Claude recomputed the correct SHA256 hash of the updated payload using Python, rebuilt the file with the matching hash prefix, verified the round-trip hash match, and confirmed the corrected metafield path was present and the broken path absent before presenting the final file for download.

## First user message

> audit this flow that came from this conversation: audit this flow that came from this conversation:

## Topics

[[topic/redirect]], [[topic/shopify]]

## Skills referenced

none detected
