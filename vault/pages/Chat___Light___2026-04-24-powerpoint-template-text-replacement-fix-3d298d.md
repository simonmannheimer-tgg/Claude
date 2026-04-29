---
title: PowerPoint template text replacement fix
date: 2026-04-24
project: Monthly SEO Update
status: active
score: 5/5
uuid: 3d298d4f-846c-4adb-8582-7a41677a0d4c
---

#chat/light #project/monthly-seo-update #status/active #topic/blog #topic/feed #topic/ga4 #topic/keyword #topic/pdp #topic/profound #topic/semrush #skill/tgg-chart-creator #skill/tgg-pptx-style

# PowerPoint template text replacement fix

- **Date:** [[2026-04-24]]
- **Project:** [[Projects/Monthly SEO Update]]
- **Status:** #status/active (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 98
- **Chat URL:** https://claude.ai/chat/3d298d4f-846c-4adb-8582-7a41677a0d4c
- **Medium view:** [[Chat/Medium/2026-04-24-powerpoint-template-text-replacement-fix-3d298d]]
- **Full transcript:** [[Chat/Full/2026-04-24-powerpoint-template-text-replacement-fix-3d298d]]

## Summary

**Conversation overview**

Simon Mannheimer, SEO Lead at The Good Guys, continued a multi-session project building a reusable monthly SEO PowerPoint deck system in Python using python-pptx. The core goal this session was to produce a correctly filled March 2026 deck (`TGG_MARCH_2026_FILLED.pptx`) from a master template (`TGG_MONTHLY_SEO_MASTER_TEMPLATE.pptx`), with all data sourced verbatim from files Simon provided rather than invented by Claude. Simon also uploaded chart images (`CHARTS.pptx`), focus tables and project screenshots (`TABLES_AND_IMAGES.pptx`), and multiple iterations of the correct source deck, ultimately settling on `TGG_MARCH_-_USE_THIS_ONE_2.pptx` as the definitive data source.

The session was marked by repeated corrections: Claude invented data and narrative copy instead of copying verbatim from Simon's source files, incorrectly greyed out emoji status indicators (🟢🟡⚪), applied wrong fonts, missed MoM values for January and February in the sessions table, and broke slide 6 project captions through a known template bug (TextBox 2 and TextBox 3 default to `{{PROJECT_1_CAPTION}}`). Simon's explicit and repeated instruction was to copy the source deck exactly and make only two targeted changes: fill the sessions table MoM column with real figures (Jan `-28.57%`, Feb `-22.19%`, Mar `+10.34%`, future months `-`), and replace the duplicate Blog Briefs entry in slide 6 bottom-right (TextBox 11) with `🟡 PDP AI Content Optimisation`. The correct approach established by end of session was to `shutil.copy()` the source deck as the base and apply only those two surgical edits, never substituting invented content.

For charts and focus tables, the correct method is transplanting directly from source files: chart images injected via `add_picture()` using source image blobs at coordinates taken from removed placeholder text boxes, and focus tables copied by appending `copy.deepcopy(src_table._element)` to the destination slide's `_spTree` after removing the existing template table. Simon flagged that Claude incorrectly edited `slide-recipes.md` without reading it first, adding a sessions table MoM rule section that conflicted with existing content and referenced slide structures (avg rank chart, non-brand clicks table, Factor slides) that never existed in the deck. Simon confirmed those references were wrong and should be stripped. The session ended with a correct output file delivered and documentation partially updated, with Simon requesting the erroneous additions to `slide-recipes.md` be removed.

Key confirmed rules for future fills: never invent narrative, bullet, or card data — use only what is in the provided source deck; never convert coloured emoji to grey; KPI card values use Poppins font at 28pt; MoM label text is bold but the numeric value is not bold, requiring two separate `<a:r>` runs; the `{{focus_and_outcomes}}` placeholder is split across multiple runs in the template XML and must be merged before replacement; TextBox 2 and TextBox 3 on slide 6 have both a split-run title bug and a wrong caption bug that must be corrected programmatically on every fill run.

## First user message

> _(no user message)_

## Topics

[[topic/blog]], [[topic/feed]], [[topic/ga4]], [[topic/keyword]], [[topic/pdp]], [[topic/profound]], [[topic/semrush]]

## Skills referenced

[[skill/tgg-chart-creator]], [[skill/tgg-pptx-style]]
