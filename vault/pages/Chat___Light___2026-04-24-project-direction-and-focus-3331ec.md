---
title: Project direction and focus
date: 2026-04-24
project: main
status: active
score: 5/5
uuid: 3331eca5-1533-46a5-8883-776ac7b7f6eb
---

#chat/light #project/main #status/active #topic/blog #topic/feed #topic/gsc #topic/keyword #topic/pdp #topic/profound

# Project direction and focus

- **Date:** [[2026-04-24]]
- **Project:** [[Projects/main]]
- **Status:** #status/active (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 25
- **Chat URL:** https://claude.ai/chat/3331eca5-1533-46a5-8883-776ac7b7f6eb
- **Medium view:** [[Chat/Medium/2026-04-24-project-direction-and-focus-3331ec]]
- **Full transcript:** [[Chat/Full/2026-04-24-project-direction-and-focus-3331ec]]

## Summary

**Conversation Overview**

The person is working on a monthly SEO reporting deck for TGG (The Good Guys, an Australian retailer), building a PowerPoint presentation for March 2026. The work involved finalising a near-complete PPTX file, redesigning charts for the organic shopping slide (slide 3), and preparing the deck for conversion into a reusable `{{}}` template. The person works with data across organic sessions, revenue, AI/LLM visibility, and organic shopping performance, and references competitors including HN (Harvey Norman), AO, and JB (JB Hi-Fi).

The main tasks were: injecting clean chart images into slide 3, fixing a stale AI tracking result on slide 4, correcting a wrong title and duplicate label on slide 6 (the "adapting" slide), and redesigning both shopping charts (GMC Clicks and Shopping Keywords) to be cleaner and more reusable. The person explicitly rejected red colouring on the clicks chart as visually negative, rejected the JB dual-axis normalisation approach, and wanted JB added back as a regular dashed line on the keywords chart. After reviewing three design options (A, B, C), the person chose Option A — vertical bars for clicks, clean competitor lines for keywords — and requested JB be included. The session ended with the JB scale problem re-emerging (41K vs ~15K range) and a recommendation pending on how to handle it.

The person's working style is direct and correction-oriented: they caught slide numbering confusion (slides were referenced out of order), trimmed scope aggressively (removed competitor mini-table, AIO keywords chart), and gave terse approvals or rejections. They referenced a previous separate conversation where daily GSC charts (clicks, impressions, purchases) were being built in a different style, and Claude confirmed those were superseded by the Option A direction from this session. Key stated preferences: no red on neutral data, no dual-axis complexity, no grid backgrounds unless helpful, charts must be dynamic and reusable with documented specs (colours, fonts, chart type recorded in script comments).

**Tool Knowledge**

PPTX manipulation used `python-pptx` throughout. Rendering slides to images for visual QA required a two-step process: convert PPTX to PDF using a local `soffice.py` script at `/mnt/skills/public/pptx/scripts/office/soffice.py`, then rasterise with `pdftoppm -jpeg -r 150`. Shape replacement for image slots worked by identifying shapes by name (e.g. `Rectangle 398`, `Rectangle 399`), capturing their position and size attributes, removing them via `shape._element.getparent().remove(shape._element)`, then inserting pictures at the same coordinates using `slide.shapes.add_picture()`. Text fixes in runs required iterating `shape.text_frame.paragraphs` then `para.runs` and checking `run.text` for substring matches — table cell text was not always reachable this way and required separate handling. The working output path for deliverables is `/mnt/user-data/outputs/`.

## First user message

> ive been working on this project, i feel we may have gotten lost. ive been working on this project, i feel we may have gotten lost.

## Topics

[[topic/blog]], [[topic/feed]], [[topic/gsc]], [[topic/keyword]], [[topic/pdp]], [[topic/profound]]

## Skills referenced

none detected
