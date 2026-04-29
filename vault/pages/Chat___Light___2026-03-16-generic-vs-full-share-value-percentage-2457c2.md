---
title: Generic vs full share value percentage
date: 2026-03-16
project: BFCM 2025 Post-Mortem Deck
status: completed
score: 5/5
uuid: 2457c2d2-5fd5-4b12-89ae-8f84e05a4b6f
---

#chat/light #project/bfcm-2025-post-mortem-deck #status/completed #topic/aeo #topic/bfcm #topic/crawl #topic/deals #topic/ga4 #topic/gsc #topic/inlink #topic/keyword #topic/plp #topic/profound #topic/semrush

# Generic vs full share value percentage

- **Date:** [[2026-03-16]]
- **Project:** [[Projects/BFCM 2025 Post-Mortem Deck]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 175
- **Chat URL:** https://claude.ai/chat/2457c2d2-5fd5-4b12-89ae-8f84e05a4b6f
- **Medium view:** [[Chat/Medium/2026-03-16-generic-vs-full-share-value-percentage-2457c2]]
- **Full transcript:** [[Chat/Full/2026-03-16-generic-vs-full-share-value-percentage-2457c2]]

## Summary

**Conversation overview**

Simon is an SEO strategist working on a post-mortem presentation deck for The Good Guys (TGG), a major Australian electronics retailer, covering Black Friday/Cyber Monday (BFCM) 2025 organic search performance. The deck argues that management's decision to replace dedicated Black Friday pages with generic `/deals/[category]-sale/` pages — combined with removing BF pages from sitewide navigation — caused a concentrated, measurable BFCM traffic loss during a period when the overall site grew 11.3%. The presentation is being built in PowerPoint (PPTX) and will be walked through live with senior leadership, not distributed for independent reading.

The session focused on copy advisory and narrative strategy rather than direct file editing. Simon's working style is direct and exacting: he pushes back hard on AI-sounding phrasing, rejects constructions like "X isn't Y, it's Z," dislikes one-line answers to complex questions, and expects the advisor role to include genuine challenge rather than agreement. When he approves specific wording, it must be preserved exactly. He corrected Claude multiple times for introducing unsupported causal claims (e.g., "rankings followed" when slide data showed rankings held), for mixing data frames inappropriately (comparing non-brand clicks to sessions, which GA4 cannot split by brand/non-brand), and for removing approved copy while iterating. He explicitly wants the advisor to identify problems and immediately recommend the full fix, not just flag the issue.

Key decisions reached: slide 7 intro copy was finalised ("Dedicated BF pages had grown sessions for three consecutive years..."); slide 8 intro was finalised ("Non-brand clicks collapsed across every page type..."); slide 13 ranking recovery copy was agreed; slide 10 generic category intro needs updating to the agreed version; slide 11 (pre/post migration traffic) was cut entirely because the February 2026 recovery data risked giving senior leadership ammunition to claim BFCM exposure boosted `/deals/` page authority. Two slides are confirmed missing and must be built: a dual-page strategy explainer (BF pages and generic pages serve different keyword intent and should run simultaneously, not as replacements) and a forward-looking "How We Win in 2026" closing slide. The narrative tension between market headwinds (non-retailers entering SERPs, AI Overviews) and TGG's structural choices was resolved as: the market set the floor, TGG's choices determined how far above it they landed, with JB Hi-Fi as the comparative evidence. A detailed handover document was written and saved to `/mnt/user-data/outputs/HANDOVER_BF2025_DECK.md` covering slide-by-slide status, all finalised copy, missing slide briefs, key data points, and immediate next steps in order.

**Tool knowledge**

PPTX editing in this project uses a specific skill-based workflow: unpack with `/mnt/skills/public/pptx/scripts/office/unpack.py`, edit slide XML directly, repack with `/mnt/skills/public/pptx/scripts/office/pack.py` using `--validate false`, convert to PDF with `soffice.py --headless --convert-to pdf`, then render slides to JPEG using `pdftoppm -jpeg -r 110`. The working unpacked directory is `/home/claude/unpacked_v7new/` based on the v8 upload. Slide XML files do not map sequentially to presentation order — slide 12 in the filesystem may be slide 8 in the deck; always cross-reference the relationship IDs in `ppt/_rels/presentation.xml.rels` to confirm ordering. The TGG design system uses `#0055A5` left accent bar, `#E4312A` bottom bar and section labels, `#002060` table headers, and table style ID `{E9C73C4C-22A7-4AF0-ABD2-4BB855E4A49D}`. Slide dimensions are 12192000 × 6858000 EMU. OD (Overdose Digital) purple dot logos remain on slides 15 and 20 and must be removed before presentation.

## First user message

> calculate the % share values for generic vs full as i have on bf vs full: calculate the % share values for generic vs full as i have on bf vs full:

## Topics

[[topic/aeo]], [[topic/bfcm]], [[topic/crawl]], [[topic/deals]], [[topic/ga4]], [[topic/gsc]], [[topic/inlink]], [[topic/keyword]], [[topic/plp]], [[topic/profound]], [[topic/semrush]]

## Skills referenced

none detected
