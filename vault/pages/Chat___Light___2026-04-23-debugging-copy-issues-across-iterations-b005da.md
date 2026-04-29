---
title: Debugging copy issues across iterations
date: 2026-04-23
project: testing pdpd
status: active
score: 5/5
uuid: b005da02-14d5-405a-8b12-a6be1d3e9603
---

#chat/light #project/testing-pdpd #status/active #topic/blog #topic/feed #topic/keyword #topic/pdp #topic/regex #skill/docx-human-style

# Debugging copy issues across iterations

- **Date:** [[2026-04-23]]
- **Project:** [[Projects/testing pdpd]]
- **Status:** #status/active (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 90
- **Chat URL:** https://claude.ai/chat/b005da02-14d5-405a-8b12-a6be1d3e9603
- **Medium view:** [[Chat/Medium/2026-04-23-debugging-copy-issues-across-iterations-b005da]]
- **Full transcript:** [[Chat/Full/2026-04-23-debugging-copy-issues-across-iterations-b005da]]

## Summary

**Conversation Overview**

This was a lengthy, multi-session working conversation focused on building, testing, and iterating a production-ready AI prompt system for generating Google Merchant Centre product descriptions for TGG (The Good Guys), an Australian consumer electronics retailer. The person appears to work in a digital content or ecommerce role and was developing an automated product description workflow using AI tools including Claude (various models) and Copilot. The work centred on a set of 38 product descriptions across appliances, electronics, and accessories.

The conversation progressed through several distinct phases: auditing existing AI-generated copy against client feedback from an Excel spreadsheet, identifying root causes in the original prompt, iteratively fixing the prompt through multiple test runs, building a QA checklist prompt, and ultimately producing a final DOCX document containing all deliverables. Claude performed extensive Python-based auditing of Excel files and CSVs throughout, cross-referencing generated descriptions against 18 rules derived from the client feedback. Key rules covered opening word requirements (The/This/A), exact H1 title reproduction, spec placement, closing sentence format (Model [SKU] in [colour] comes with a [X] year manufacturer's warranty), warranty duration, colour appearing in both body and closing, filler word bans, headphone battery life placement, and word count gates (90–150 words hard minimum).

The person was direct and critical when outputs didn't meet expectations — explicitly flagging that Claude's default DOCX styling looked "AI generated" (navy headers, dark table fills, branded colours), leading to creation of a skill file (`docx-human-style/SKILL.md`) to enforce plain Word aesthetics going forward. The person also noted that Claude consistently over-formatted and over-styled documents without being asked, and wanted this corrected at a systemic level. Multiple AI tools were tested against the same prompt across the conversation: Claude Haiku 4.5 (best run: 32/38 pass), ChatGPT (1 description completed before hitting attachment limits), and Microsoft 365 Copilot Premium (3/3 pass on completed descriptions, best quality of any run, but stopped after 3 products citing response size limits). The final finding was that Copilot produced the highest quality output — natural prose, correct word counts, no filler, proper structure — while Haiku consistently treated the 90-word minimum as a ceiling rather than a floor across all runs. Final deliverables produced were an updated `PROMPT.txt` (generation prompt), `QA-CHECKLIST.md` (18-rule QA prompt), and a formatted `TGG-Product-Description-Final.docx` containing all four sections.

## First user message

> I need you to go over the tabs, the iterations, the feedbacks - identify where things are going wrong - check the prompt, then create a bullet list explaining what is wrong and needs fixing (in the copy, not prompt, but look at the prompt to ground your feedback) I need you to go over the tabs, the iterations, the feedbacks - identify where things are going wrong - check the prompt, then create a 

## Topics

[[topic/blog]], [[topic/feed]], [[topic/keyword]], [[topic/pdp]], [[topic/regex]]

## Skills referenced

[[skill/docx-human-style]]
