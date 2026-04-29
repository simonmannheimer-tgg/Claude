---
title: Semantic review and link validation
date: 2026-04-27
project: EOFY Blog Briefs — Two URL Errors Outstanding
status: active
score: 5/5
uuid: f9ad183a-5e51-478d-b519-c0c7968aa633
---

#chat/light #project/eofy-blog-briefs-two-url-errors-outstand #status/active #topic/404 #topic/aeo #topic/blog #topic/contentful #topic/crawl #topic/deals #topic/eofy #topic/inlink #topic/keyword #topic/meta #topic/plp #topic/redirect #topic/schema #topic/screaming-frog #topic/semrush #topic/shopify #skill/tgg-seo-specialist

# Semantic review and link validation

- **Date:** [[2026-04-27]]
- **Project:** [[Projects/EOFY Blog Briefs — Two URL Errors Outstanding]]
- **Status:** #status/active (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 36
- **Chat URL:** https://claude.ai/chat/f9ad183a-5e51-478d-b519-c0c7968aa633
- **Medium view:** [[Chat/Medium/2026-04-27-semantic-review-and-link-validation-f9ad18]]
- **Full transcript:** [[Chat/Full/2026-04-27-semantic-review-and-link-validation-f9ad18]]

## Summary

**Conversation overview**

This conversation involved a detailed SEO and content audit for The Good Guys (TGG) Australia, focused on five EOFY 2026 blog briefs: Best Tech Buys for EOFY, EOFY Most Popular Home Appliances, EOFY Sales Tips for University Students, Guide to EOFY TV Deals, and Maximise Your Tax Return. The person works in an SEO specialist capacity for TGG and uploaded the five blog DOCX files, a content cluster diagram HTML file, and a Screaming Frog crawl export (internal_all_iwth_API_data.xlsx) for review. The primary asks were semantic review, URL validation, and identification of 301 and 404 links across all inlinks in the new content.

Claude extracted all unique TGG URLs from the documents, checked HTTP status codes against live endpoints without following redirects, and produced a full audit covering 301 redirects in new content, 301s in existing live content, semantic issues, anchor-destination mismatches, and meta title character counts. Four DOCX files were rebuilt with fixes applied directly to the XML layer (relationships files and document.xml), preserving all other content exactly. The person then uploaded revised versions of the Students and Tax Return docs with their own manual changes applied, and Claude re-assessed what remained outstanding. Throughout the conversation, the person corrected Claude's output format multiple times, pushing toward simpler plain-language presentation: one page name, then a flat list of fixes with anchor text and URL changes only, no markdown tables or nested structure.

Key outstanding issues identified by end of conversation were: the Tax Return new closing still had /store-locator instead of /stores; the Students FAQ 5 "iPad" anchor still pointed to /apple instead of /computers-tablets-and-gaming/ipad-and-tablets; and a live site issue where /guide-to-eofy-tv-deals (301 to /whats-new/guide-to-eofy-tv-deals) had 4 internal pages linking to it not covered by these briefs, requiring a Screaming Frog inlinks report to resolve. The person confirmed that 301s appearing only in "Current" content columns require no action since that copy is replaced entirely on publish. FAQPage schema was flagged as missing but the person noted it was already automated. FAQ placement feedback was clarified as not applicable to blog content. The person's preferred working format is minimal: page name as header, fixes as a plain flat list with anchor text and before/after URLs, no markdown formatting or section labels beyond the page name.

## First user message

> check these and any issues around semantics. any recommendations? ensure that all inlinks are correct and none are 301 or 404. check these and any issues around semantics. any recommendations? ensure that all inlinks are correct and none are 301 or 404.

## Topics

[[topic/404]], [[topic/aeo]], [[topic/blog]], [[topic/contentful]], [[topic/crawl]], [[topic/deals]], [[topic/eofy]], [[topic/inlink]], [[topic/keyword]], [[topic/meta]], [[topic/plp]], [[topic/redirect]], [[topic/schema]], [[topic/screaming-frog]], [[topic/semrush]], [[topic/shopify]]

## Skills referenced

[[skill/tgg-seo-specialist]]
