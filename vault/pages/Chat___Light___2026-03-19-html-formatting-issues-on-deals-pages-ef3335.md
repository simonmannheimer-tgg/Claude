---
title: HTML formatting issues on deals pages
date: 2026-03-19
project: main
status: completed
score: 4/5
uuid: ef3335b2-e56c-4de1-a0b0-d51c1b639e88
---

#chat/light #project/main #status/completed #topic/bfcm #topic/contentful #topic/copy #topic/crawl #topic/deals #topic/inlink #topic/regex

# HTML formatting issues on deals pages

- **Date:** [[2026-03-19]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, 5+turns, project-keyword)
- **Messages:** 12
- **Chat URL:** https://claude.ai/chat/ef3335b2-e56c-4de1-a0b0-d51c1b639e88
- **Medium view:** [[Chat/Medium/2026-03-19-html-formatting-issues-on-deals-pages-ef3335]]
- **Full transcript:** [[Chat/Full/2026-03-19-html-formatting-issues-on-deals-pages-ef3335]]

## Summary

**Conversation Overview**

The person works on SEO/content operations for The Good Guys (thegoodguys.com.au), managing Contentful CMS entries for product listing pages (PLPs) in the /deals/ section. The conversation centred on a multi-step technical task: auditing and restoring missing internal link blocks that previously pointed to Black Friday and Boxing Day sub-pages across 23 /deals/ category pages.

The workflow began with Claude parsing an uploaded CSV (a saved crawl of PLP intro copy HTML) that had formatting issues — specifically, multi-paragraph HTML blocks split across multiple rows with orphaned content. Claude reconstructed the correct HTML by merging orphaned rows back to their parent URLs. Claude then visited all 23 /deals/ pages live, identified that 22 of them were missing the Black Friday/Boxing Day internal link section above the FAQs, and confirmed that /deals/dishwashers was the only page still carrying the old block — serving as the template. The person confirmed this audit was correct.

For the final deliverable, the person provided a concatenated string of /deals/ slugs paired with their Contentful entry URLs, and asked Claude to: verify all inlinks return 200, fix mojibake encoding characters (e.g. `â€™` → `'`), normalise CSS class names from `_link_g2ewd_15` to `_link_1fbwu_19`, and produce a clean three-column CSV (TGG page URL, Contentful entry URL, cleaned HTML). All 302 inlinks returned 200. The final CSV covers 21 pages ready for manual Contentful entry. One notable flag raised: /deals/kitchen and /deals/fridge-and-laundry share the same Contentful entry ID (`XBZkeU8Nymy6Zz4wQ1BPh`). A key correction the person made: Claude initially second-guessed the CSV HTML for microwaves and kitchenware pages, suggesting the links might be incomplete. The person firmly clarified that the CSV is the source of truth representing the correct pre-existing state to restore, not the live pages — and Claude should use it as-is without editorial judgement.

## First user message

> i need to see the html copy for the /deals/ pages - theres ome issues with the formatting so try to use the html to match it to the correct page i need to see the html copy for the /deals/ pages - theres ome issues with the formatting so try to use the html to match it to the correct page

## Topics

[[topic/bfcm]], [[topic/contentful]], [[topic/copy]], [[topic/crawl]], [[topic/deals]], [[topic/inlink]], [[topic/regex]]

## Skills referenced

none detected
