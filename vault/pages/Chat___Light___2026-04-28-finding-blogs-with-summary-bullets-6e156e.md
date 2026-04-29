---
title: Finding blogs with summary bullets
date: 2026-04-28
project: main
status: active
score: 4/5
uuid: 6e156e24-4ea7-4906-a49d-1026f49e449c
---

#chat/light #project/main #status/active #topic/aeo #topic/bfcm #topic/blog #topic/eofy

# Finding blogs with summary bullets

- **Date:** [[2026-04-28]]
- **Project:** [[Projects/main]]
- **Status:** #status/active (score 4/5: deliverable, named-tgg, 5+turns, project-keyword)
- **Messages:** 17
- **Chat URL:** https://claude.ai/chat/6e156e24-4ea7-4906-a49d-1026f49e449c
- **Medium view:** [[Chat/Medium/2026-04-28-finding-blogs-with-summary-bullets-6e156e]]
- **Full transcript:** [[Chat/Full/2026-04-28-finding-blogs-with-summary-bullets-6e156e]]

## Summary

**Conversation Overview**

The person is working on an SEO/AEO (Answer Engine Optimization) content audit for The Good Guys Australia website (thegoodguys.com.au). They uploaded a zip file containing 984 HTML files representing rendered pages from the site and asked Claude to identify which blogs and guides contain key takeaways or summary bullet sections.

Claude initially ran a Python/BeautifulSoup script scanning for explicit keyword patterns like "key takeaways," "summary," "highlights," and similar terms, identifying 22 pages total with 10 in the /whats-new/ section. The person caught two errors: a miscounted list (2 paragraph-format pages stated but only 1 shown) and missing pages they knew had summary sections ("how to move a fridge" and "fridge temperature"). This prompted the person to instruct Claude to look beyond literal keyword matching and detect summary sections semantically and conceptually — a key correction to Claude's methodology.

The conversation then shifted to AEO impact analysis. The person provided a concrete example of the summary format in question (an intro paragraph plus "Key Takeaways From This Article" bullet list at the top of a page) and asked which /whats-new/ pages would be negatively impacted by adding this structure. Claude developed a risk-scoring script analyzing question-driven H2/H3 headings and definitional intro structures, categorizing pages as HIGH, MEDIUM, or LOW risk. The analysis concluded that 565 /whats-new/ pages would be negatively impacted because their existing question-focused or procedural heading structures function as the AEO strategy themselves — adding a summary block at the top would push optimized answer content further down the HTML, diluting featured snippet extraction and AIO surfacing. Only 191 /whats-new/ pages were deemed LOW RISK for adding the summary format.

**Tool Knowledge**

Claude used bash and Python scripts with BeautifulSoup throughout, running them against extracted HTML files in /tmp. The file naming convention for the site's rendered HTML follows the pattern `rendered_https_www_thegoodguys_com_au_[path-with-underscores].html`, where URL path separators become underscores. Reconstructing clean URLs required stripping the `rendered_https_www_thegoodguys_com_au_` prefix, removing `.html`, URL-decoding, and reformatting separators. Scanning with `Path('.').rglob('*whats-new*.html')` was the reliable method for filtering to the /whats-new/ section. The key lesson from this conversation is that semantic/conceptual detection of summary sections requires broader pattern matching beyond explicit "key takeaway" text — the script needed expansion to detect functional equivalents like "things to know," "need to know," "at a glance," "overview," and similar constructs to avoid missing known positive cases.

## First user message

> I want you to look through all of these blogs and guides and tell me which have a key takeways or blog summary bullets of some sort. I want you to look through all of these blogs and guides and tell me which have a key takeways or blog summary bullets of some sort.

## Topics

[[topic/aeo]], [[topic/bfcm]], [[topic/blog]], [[topic/eofy]]

## Skills referenced

none detected
