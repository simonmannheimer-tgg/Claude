---
title: Presentation refinement
date: 2026-03-12
project: main
status: completed
score: 5/5
uuid: 7fd9a0e3-3ef8-4cc0-bdb3-2d3a9050807c
---

#chat/light #project/main #status/completed #topic/aeo #topic/bfcm #topic/crawl #topic/deals #topic/ga4 #topic/gsc #topic/inlink #topic/keyword #topic/pdp #topic/plp #topic/profound

# Presentation refinement

- **Date:** [[2026-03-12]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 73
- **Chat URL:** https://claude.ai/chat/7fd9a0e3-3ef8-4cc0-bdb3-2d3a9050807c
- **Medium view:** [[Chat/Medium/2026-03-12-presentation-refinement-7fd9a0]]
- **Full transcript:** [[Chat/Full/2026-03-12-presentation-refinement-7fd9a0]]

## Summary

**Conversation overview**

Simon is working on a PowerPoint deck for a client report covering TGG's Black Friday/Cyber Monday (BFCM) 2025 SEO performance (Nov 1–Dec 4). The core narrative is that management's decision to use generic /deals pages instead of dedicated Black Friday pages caused a significant traffic drop, and the deck argues this through data rather than accusation. Simon has been collaborating across multiple sessions with Claude to restructure, clean, and rebuild the deck from v3 (26 slides) to v4 (now 20 slides).

This session focused on fixing a persistent file corruption issue where the PPTX wouldn't open in PowerPoint, rebuilding slide 5 (BFCM Snapshot) with stat cards and simplified tables, and applying global design changes across all slides. The root cause of the broken file was identified as the pack script stripping critical structural folders (docProps/, ppt/notesMasters/, ppt/theme/, etc.) — resolved by always using `--original` flag with pack.py and `--validate false` to bypass a benign script validation bug. Simon confirmed the file opens correctly after this fix. Key decisions made: remove BFCM Isolated slide from the deck, mark GA4 and GSC slides as done, remove the AI chart aside from slide 13's scope, remove the Overdose logo from all slides, and change all table header colours to `#002060`. Simon's standing instruction is that when asked to clean tables, apply changes to all tables across all slides without needing explicit permission for each one.

Simon's working style is direct and efficiency-focused — he gives short instructions and expects Claude to infer scope broadly rather than asking for clarification on each element. He corrected Claude multiple times for not using the proper PPTX skill workflow (unpack → edit → clean → pack with `--original`), for attempting manual zip manipulation instead of the skill scripts, and for not rendering slides to visually verify output before delivering. The deck's design system uses white background, left blue bar `#0055A5`, bottom red bar `#E4312A`, Calibri throughout, table headers `#002060` with white bold text, and colour-coded YoY cells (green `#D9EAD3`/`#276221` for positive, red `#F4CCCC`/`#CC0000` for negative). The session ended with Simon preparing to migrate to a new chat, with slides 1–6 complete and slides 7–20 still requiring review.

**Tool knowledge**

For PPTX editing, the correct workflow is: `unpack.py` → edit XML → `clean.py` → `pack.py --original [source.pptx] --validate false`. The `--validate false` flag is always required because the pack script has a benign Cython-related bug that causes false ID uniqueness validation failures even when IDs are genuinely unique. Skipping `--original` causes the pack to strip critical structural folders (docProps/, ppt/notesMasters/, ppt/notesSlides/, ppt/theme/, ppt/charts/, ppt/embeddings/) that PowerPoint requires to open the file — LibreOffice renders these broken files fine, masking the issue until PowerPoint testing. When adding new slides, always use `add_slide.py` rather than manually copying XML files, as manual copies miss relationship registration. After packing, always delete the existing PDF before running soffice conversion to prevent LibreOffice from serving a cached render — the pattern is `rm -f [file].pdf && soffice --convert-to pdf` then `pdftoppm`. When verifying which deck position a slide file occupies, check the sldIdLst rId order against the presentation.xml.rels mapping rather than assuming slide5.xml is deck position 5, as placeholder insertions and deletions shift the mapping.

## First user message

> I need help refining a presentation - see attached. I need help refining a presentation - see attached.

## Topics

[[topic/aeo]], [[topic/bfcm]], [[topic/crawl]], [[topic/deals]], [[topic/ga4]], [[topic/gsc]], [[topic/inlink]], [[topic/keyword]], [[topic/pdp]], [[topic/plp]], [[topic/profound]]

## Skills referenced

none detected
