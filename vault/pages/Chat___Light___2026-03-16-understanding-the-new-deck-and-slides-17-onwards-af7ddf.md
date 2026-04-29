---
title: Understanding the new deck and slides 17 onwards
date: 2026-03-16
project: main
status: completed
score: 4/5
uuid: af7ddfd8-979a-4b2b-93af-bd98db351f45
---

#chat/light #project/main #status/completed #topic/aeo #topic/bfcm #topic/copy #topic/deals #topic/keyword #topic/semrush

# Understanding the new deck and slides 17 onwards

- **Date:** [[2026-03-16]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, project-keyword, lasting-effect)
- **Messages:** 4
- **Chat URL:** https://claude.ai/chat/af7ddfd8-979a-4b2b-93af-bd98db351f45
- **Medium view:** [[Chat/Medium/2026-03-16-understanding-the-new-deck-and-slides-17-onwards-af7ddf]]
- **Full transcript:** [[Chat/Full/2026-03-16-understanding-the-new-deck-and-slides-17-onwards-af7ddf]]

## Summary

**Conversation Overview**

The person is working on a Black Friday performance review deck for The Good Guys (TGG), an internal presentation analysing BFCM 2025 SEO outcomes and recommending a forward strategy. They are Simon Mannheimer, working in SEO at The Good Guys. The task involved reviewing a handover document alongside the current working deck (`TGG___Black_Friday_Review_2025__NEW___8_.pptx`, referred to as v8new, 22 slides) and an older purple reference deck used only for contextual understanding of prior comments. Claude's role was explicitly defined as advisory — challenging thinking, recommending specific copy and structure, and pushing back where needed rather than simply agreeing.

The conversation covered a detailed slide-by-slide audit of slides 17 onward (plus several upstream fixes), with Claude producing specific recommendations per slide before beginning a live build. Key decisions included: collapsing the slide 17 divider title to "Winning the Next BFCM"; replacing the slide 10 intro copy with an approved version from the handover doc; removing all Overdose Digital (OD) branding references from slides 2, 15, and 20; fixing non-standard header colours across slides 18 and 19 to `#002060` navy; inserting two new slides (a dual-page strategy explainer and a forward-looking "How We Win in 2026" outcomes slide); and deleting slide 1 entirely. A data conflict was identified and flagged before proceeding: slide 18 cited "−19.9%" for combined sale page sessions while slide 7 cited "−23.5%", with Claude unable to reconcile the figure from available data and requesting clarification before continuing the build.

Claude began executing changes directly in the unpacked PPTX XML, completing fixes to slides 2, 10, and 17 before pausing on slide 18 pending resolution of the data discrepancy. The person's stated preference is for recommendations delivered as bullet points per slide first, then a rebuild — a pattern Claude followed in this session. Key colleagues referenced include Simon Mannheimer as the deck author and presenter. The deck's central argument is that TGG replaced dedicated Black Friday pages with generic `/deals/` URLs in 2025, removed BF pages from navigation, and suffered concentrated BFCM traffic losses as a result, while competitor JB Hi-Fi maintained a dual-page strategy that performed better.

**Tool Knowledge**

Claude used a PPTX skill workflow involving `markitdown` for text extraction, a `thumbnail.py` script at `/mnt/skills/public/pptx/scripts/thumbnail.py` for visual QA, and an `unpack.py` script at `/mnt/skills/public/pptx/scripts/office/unpack.py` to decompress the PPTX into editable XML. The thumbnail script produced multi-slide grid images named with a `-1.jpg` / `-2.jpg` suffix pattern. The presentation relationship file at `unpacked/ppt/_rels/presentation.xml.rels` maps rIds to slide files sequentially (rId6→slide1, rId7→slide2, etc.), which is the reliable way to confirm slide order before making structural changes. Direct XML `str_replace` edits were used for text changes, with `grep -n` used first to locate exact line numbers before editing. The working file was copied to `/home/claude/v8new.pptx` before unpacking to preserve the original.

## First user message

> The screenshots, the comments, the purple deck - thats the old deck, only care about the context for the comments there and how to do slides 17 and on. read ths handover deck alongsidce (new) and explain in detail your task and plan: The screenshots, the comments, the purple deck - thats the old deck, only care about the context for the comments there and how to do slides 17 and on. read ths hando

## Topics

[[topic/aeo]], [[topic/bfcm]], [[topic/copy]], [[topic/deals]], [[topic/keyword]], [[topic/semrush]]

## Skills referenced

none detected
