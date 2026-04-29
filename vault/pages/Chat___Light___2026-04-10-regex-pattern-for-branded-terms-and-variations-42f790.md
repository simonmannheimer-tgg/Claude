---
title: Regex pattern for branded terms and variations
date: 2026-04-10
project: main
status: completed
score: 4/5
uuid: 42f7902b-ae3c-4edd-8e5d-3df8311dd364
---

#chat/light #project/main #status/completed #topic/gsc #topic/keyword #topic/regex

# Regex pattern for branded terms and variations

- **Date:** [[2026-04-10]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, 5+turns, project-keyword)
- **Messages:** 6
- **Chat URL:** https://claude.ai/chat/42f7902b-ae3c-4edd-8e5d-3df8311dd364
- **Medium view:** [[Chat/Medium/2026-04-10-regex-pattern-for-branded-terms-and-variations-42f790]]
- **Full transcript:** [[Chat/Full/2026-04-10-regex-pattern-for-branded-terms-and-variations-42f790]]

## Summary

**Conversation Overview**

The person is working on SEO analysis for The Good Guys (thegoodguys.com.au), an Australian retailer, and needed help building an optimized regex pattern to identify branded search queries in Google Search Console (GSC) data. The work was done in the context of a tool called SEOGets, which applies regex filters to classify branded vs. non-branded queries. The person uploaded multiple CSV files containing GSC query data and filter outputs for comparison and analysis.

The conversation involved two phases. In the first, Claude analyzed approximately 59,397 unique queries across two GSC data files to build an initial branded term regex covering core brand name variations, typos, delimiter variations, "the" prefix misspellings, and the TGG abbreviation. In the second phase, the person ran three datasets through comparison: the full keyword list, Claude's regex output, and the current default SEOGets filter output. Claude performed a detailed diff analysis to identify false positives in the current regex (approximately 1,915 queries including "5 guys," "gift ideas for guys," "air con guys," and similar non-brand terms), gaps in Claude's v1 regex (missing product+brand concatenations like "airpods goodguys" and high-volume typos like "good fuys" with 8,295 clicks), and model number false positives from Omega appliance product codes ending in "tgg" (e.g., "obo691tgg," "ocg64ffetgg").

The final recommended regex uses PCRE with case-insensitive matching, negative lookaheads to block model numbers (`(?![a-z])`), isolated word boundaries for the TGG abbreviation (`(?<![a-z0-9])tgg(?![a-z0-9])`), and `s{1,2}` to accommodate double-s typos like "goodguyss." The final pattern captures 16,535 queries with zero false positives, representing a gain of 300 legitimate branded queries and elimination of 1,915 false positives compared to the current SEOGets default filter. A detailed markdown report documenting the regex breakdown, match/block examples, performance comparison table, and migration impact was produced as a deliverable.

## First user message

> create a simple regex that catches all branded terms and any variations of brand you can notice from the full data. create a simple regex that catches all branded terms and any variations of brand you can notice from the full data.

## Topics

[[topic/gsc]], [[topic/keyword]], [[topic/regex]]

## Skills referenced

none detected
