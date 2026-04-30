---
title: Building a copywriting skill from GitHub code
date: 2026-03-18
project: Skills Built (full set)
status: completed
score: 5/5
uuid: 63f3c699-be20-4241-9b4e-ec7a94d34c97
---

#chat/light #project/skills-built-full-set #status/completed #topic/copy #topic/deals #topic/inlink #topic/meta #topic/plp #skill/tgg-copywriting

# Building a copywriting skill from GitHub code

- **Date:** [[2026-03-18]]
- **Project:** [[Projects/Skills Built (full set)]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 18
- **Chat URL:** https://claude.ai/chat/63f3c699-be20-4241-9b4e-ec7a94d34c97
- **Medium view:** [[Chat/Medium/2026-03-18-building-a-copywriting-skill-from-github-code-63f3c6]]
- **Full transcript:** [[Chat/Full/2026-03-18-building-a-copywriting-skill-from-github-code-63f3c6]]

## Summary

**Conversation overview**

Simon worked with Claude to build a modular copywriting skill for The Good Guys (thegoodguys.com.au), an Australian electronics and appliances retailer. The goal was to package the existing SEO content processes (numbered 00–09) into a structured, reusable skill that could assess content requirements and apply the correct rules automatically. Simon provided his Claude Code GitHub repo as the source material, and Claude extracted the relevant copywriting processes while ignoring unrelated infrastructure (GTMetrix, Context Mode, shopping scraper).

Simon made several scoping decisions via structured input: the skill should cover all writing processes (01, 02, 03, 05, 08), use a modular structure (SKILL.md plus a references folder), and handle batch mode with cross-batch variation enforcement as a critical feature. Claude built a six-step workflow (identify content type → load references → classify page → write → batch-check → self-QA), a routing table mapping request types to reference files, and individual reference files for TOV/hard bans (00), PLP intros (01), metadata (02), inlink migration (03), FAQ and category copy (05), and EAV mapping (08). The skill enforces Australian English, hard-banned words (sale, save, discount, etc.), character limits, and cross-batch variation checks on openers, TGG placement, and benefit angles.

The conversation then clarified two important corrections to Claude's approach. First, when Simon asked to "host it fully in your skill repo so it is always updatable," Claude initially overengineered a solution with a skills directory, README, integration guide, and settings.json changes for Claude Code — none of which were necessary since Claude Code already reads the existing process files directly. Second, when Simon asked to "give it context," Claude misread this as needing site taxonomy or brand inventory, when Simon actually meant operational context for Claude Code on how to use the skill. The final resolution was clean: the `.skill` file is the only deliverable for claude.ai (which has no persistent filesystem), Claude Code needs no changes since the existing process files already work, and the single download is `tgg-copywriting.skill`. Simon's correction pattern throughout was to cut unnecessary complexity and consolidate to the minimum viable output.

## First user message

> help me build a skill - i will provide you the github repo of my claude code - not everything there is relevant, I want a copywriting skill that can assess my requirements and adjust. help me build a skill - i will provide you the github repo of my claude code - not everything there is relevant, I want a copywriting skill that can assess my requirements and adjust.

## Topics

[[topic/copy]], [[topic/deals]], [[topic/inlink]], [[topic/meta]], [[topic/plp]]

## Skills referenced

[[skill/tgg-copywriting]]
