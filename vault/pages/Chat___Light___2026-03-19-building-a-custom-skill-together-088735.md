---
title: Building a custom skill together
date: 2026-03-19
project: main
status: completed
score: 5/5
uuid: 088735c4-4633-4f3a-8501-e70db18419cd
---

#chat/light #project/main #status/completed #topic/airtable #topic/bfcm #topic/copy #topic/keyword #topic/mcp #topic/plp #topic/semrush #topic/sitemap #skill/tgg-copywriting #skill/tgg-seo-specialist

# Building a custom skill together

- **Date:** [[2026-03-19]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 14
- **Chat URL:** https://claude.ai/chat/088735c4-4633-4f3a-8501-e70db18419cd
- **Medium view:** [[Chat/Medium/2026-03-19-building-a-custom-skill-together-088735]]
- **Full transcript:** [[Chat/Full/2026-03-19-building-a-custom-skill-together-088735]]

## Summary

**Conversation Overview**

Simon Mannheimer, who works in SEO for The Good Guys (thegoodguys.com.au), collaborated with Claude to build a new skill called `tgg-connector-router` using the skill-creator framework. The goal was to create a skill that understands all available connectors and tools in Simon's workflow and proactively identifies when any given task could be enhanced or unblocked by using them. Simon's available tools include Semrush MCP (always using the AU database), Airtable MCP (used for SEO records and a PLP Copy Tracker), Google Drive (for TGG performance decks and process docs), and the Claude Chrome Extension.

A key clarification Simon made mid-build shaped the entire skill design: the skill should not lock specific tasks to fixed tools, but instead act as an opportunity spotter — evaluating whatever task is underway and asking whether a connector would make it meaningfully better. Simon also clarified that the Claude Chrome Extension is valuable precisely because it circumvents MCP and API limitations by operating a real authenticated browser session directly, making it the escape hatch for anything connectors can't reach.

The final skill was written to run a silent enhancement check on every task, surface opportunities with a single lightweight inline question rather than interrupting workflow, and treat Chrome as the fallback for authenticated UI actions, JS-heavy pages, and bulk operations. TGG-specific context was baked in throughout, including competitors (JB Hi-Fi, Harvey Norman, Bing Lee), primary product categories, 41 active Semrush Position Tracking campaigns, and 9 Claude Code SEO process files numbered 01–09.

**Tool Knowledge**

For the Semrush MCP, `tool_search("semrush")` must be run before every call because parameter schemas vary by report type. The database parameter must always be set to `au` for TGG work. Key reports include `url_organic`, `url_rank`, `keyword_overview`, `domain_organic`, and `backlinks_overview`. The MCP cannot reach Semrush UI actions such as exports or campaign management — those require Claude in Chrome instead. For Airtable MCP, `tool_search("airtable")` is similarly required before calling. For Google Drive, `google_drive_search` is preferred for discovery followed by `google_drive_fetch` to read content; TGG documents commonly contain terms like "TGG", "BFCM", "Black Friday", "SEO", or "Organic" in their names, and process files follow a numbered 01–09 naming convention. For Claude in Chrome handoffs, the skill requires a numbered step-by-step brief including the starting URL, exact actions, what to capture or download, and where to return the result.

## First user message

> Let's create a skill together using your skill-creator skill. First ask me what the skill should do. Let's create a skill together using your skill-creator skill. First ask me what the skill should do.

## Topics

[[topic/airtable]], [[topic/bfcm]], [[topic/copy]], [[topic/keyword]], [[topic/mcp]], [[topic/plp]], [[topic/semrush]], [[topic/sitemap]]

## Skills referenced

[[skill/tgg-copywriting]], [[skill/tgg-seo-specialist]]
