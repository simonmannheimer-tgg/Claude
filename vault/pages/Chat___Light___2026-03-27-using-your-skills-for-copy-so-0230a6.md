---
title: using your skills for copy, so...
date: 2026-03-27
project: main
status: tactical
score: 5/5
uuid: 0230a6e0-22c0-45cd-b098-13c41578a0e7
---

#chat/light #project/main #status/tactical #topic/aeo #topic/agent #topic/airtable #topic/bfcm #topic/blog #topic/contentful #topic/copy #topic/deals #topic/keyword #topic/mcp #topic/plp #topic/semrush #skill/tgg-content-strategist #skill/tgg-copywriting #skill/tgg-marketing-analyst #skill/tgg-repo-manager #skill/tgg-seo-specialist #skill/tgg-template-generator

# using your skills for copy, so...

- **Date:** [[2026-03-27]]
- **Project:** [[Projects/main]]
- **Status:** #status/tactical (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 72
- **Chat URL:** https://claude.ai/chat/0230a6e0-22c0-45cd-b098-13c41578a0e7
- **Medium view:** [[Chat/Medium/2026-03-27-using-your-skills-for-copy-so-0230a6]]
- **Full transcript:** [[Chat/Full/2026-03-27-using-your-skills-for-copy-so-0230a6]]

## Summary

**Conversation overview**

Simon Mannheimer is an SEO Strategist working on The Good Guys (thegoodguys.com.au), managing a Claude Code workflow via a GitHub repository to produce SEO copy at scale. The session focused on two interconnected problems: correcting a fundamental misunderstanding in how Claude Code was approaching entity depth in PLP (Product Listing Page) intro copy, and then building a complete, production-ready set of repo files to govern the remaining work.

The core issue Simon identified was that Claude Code had become too mechanical in its interpretation of the entity anchor standard, treating "named proprietary technology" as the only valid form of specificity. Simon pointed out this was wrong — entity anchoring is EAV (Entity-Attribute-Value) thinking applied to the core topic, not a trademark hunt. Claude Code had flagged 658 rows as needing entity fixes but left them unwritten because it couldn't find a trademark for brands like Solt, CHiQ, Belkin, or Baileys. The corrected standard introduced four valid anchor forms: named proprietary technology, named product line or series, specific attribute plus real value, and brand-defining characteristic. The competitor substitution test was established as the practical check: if S1 still makes sense with a competitor's name swapped in, it fails.

From this, Claude produced a full suite of repo files: a corrected process file (`01-plp-intros.md` v2.1), a rewritten `plp-copywriter` agent, a new `plp-fix-pass` agent for the 658-row backlog, a QA audit Python script, a repo housekeeping audit identifying seven specific issues across three severity levels, a `CLAUDE.md` entry covering project status and storage rules, and two Claude Code briefs — one for repo cleanup (four sequential commits with exact bash commands and verification checks) and one for PLP copy production covering Batches 2–4 (843 URLs) and a deferred Page Description shortening task (567 generic category pages currently over 250 chars). Simon confirmed he committed the files under the title "CLAUDE RECOMMENDATIONS 27032026" and asked how to structure the GitHub issue trigger. Claude clarified the distinction between the brief (a reference doc that lives in `seo/docs/` and is read by Claude Code when it starts) and the issue trigger (a short six-line prompt that acts as the start button), and produced both. The session ended with Simon confirming the todo order: repo cleanup first, then Batches 2–4 copy, then the Page Description shortening task — with Simon providing batch CSV files when that phase begins.

## First user message

> using your skills for copy, some light seo research with semrush and the copy rulesets you have - can we start a brand category PLP intro rewrite?  for batches 2-4 off of the attached CSV, lets start in small batches, first 10 using your skills for copy, some light seo research with semrush and the copy rulesets you have - can we start a brand category PLP intro rewrite?  for batches 2-4 off of th

## Topics

[[topic/aeo]], [[topic/agent]], [[topic/airtable]], [[topic/bfcm]], [[topic/blog]], [[topic/contentful]], [[topic/copy]], [[topic/deals]], [[topic/keyword]], [[topic/mcp]], [[topic/plp]], [[topic/semrush]]

## Skills referenced

[[skill/tgg-content-strategist]], [[skill/tgg-copywriting]], [[skill/tgg-marketing-analyst]], [[skill/tgg-repo-manager]], [[skill/tgg-seo-specialist]], [[skill/tgg-template-generator]]
