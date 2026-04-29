---
title: Productivity tools
date: 2026-04-28
project: main
status: active
score: 4/5
uuid: 04274f10-1bab-4e26-a0cf-17054536d1c3
---

#chat/light #project/main #status/active #topic/404 #topic/blog #topic/copy #topic/crawl #topic/ga4 #topic/gsc #topic/inlink #topic/keyword #topic/pdp #topic/plp #topic/redirect #topic/schema #topic/screaming-frog #topic/semrush

# Productivity tools

- **Date:** [[2026-04-28]]
- **Project:** [[Projects/main]]
- **Status:** #status/active (score 4/5: deliverable, 5+turns, project-keyword, lasting-effect)
- **Messages:** 40
- **Chat URL:** https://claude.ai/chat/04274f10-1bab-4e26-a0cf-17054536d1c3
- **Medium view:** [[Chat/Medium/2026-04-28-productivity-tools-04274f]]
- **Full transcript:** [[Chat/Full/2026-04-28-productivity-tools-04274f]]

## Summary

**Conversation overview**

The person is an SEO and digital strategy professional who self-identifies as having ADHD, working in a high-pressure, unstructured field where success metrics are often delayed or invisible. They engaged Claude in an extended product design and development session to build a sophisticated AI-powered productivity tool called "Compass" — described throughout as a "second brain" and "executive function prosthetic" tailored specifically to how their brain works, including difficulties with task initiation, hyperfocus on the wrong things, and the challenge of gauging ROI on ambiguous work like SEO.

The session progressed through multiple phases: initial requirements gathering (task tracker with AI chat, persistent storage, drag-to-reorder, tags, priorities), deep research into ADHD-specific productivity design and top tools (Obsidian, NotebookLM, Linear, Things 3, Motion, Reclaim, Goblin.tools, Mem.ai, Granola, Tana, Reflect, Capacities), and then iterative React artifact development across approximately eight major rebuilds. The person provided a real brain dump mid-session — a long, rambling list of actual SEO work tasks including blog intros, PLP copy reviews, 404 redirects, schema/feed alignment, SEMrush issues, and AI copywriting planning — which exposed a critical JSON parsing bug (Claude was wrapping responses in markdown fences, breaking `JSON.parse`). The person also flagged that tasks were not being added to the UI despite the AI responding, which led to a robust multi-strategy JSON extraction function. Throughout, the person pushed back on code quality (ultra-minified code causing transpiler errors like "can't find variable: returnReact"), design quality ("sad and uninspired," "boring," "vibecoded"), and requested that code be written as a real developer would — with proper formatting, descriptive variable names, explicit returns, and readable structure.

The final version of Compass includes: AI chat with brain dump → structured task extraction, voice input via Web Speech API, a Today panel with overwhelm mode (one-thing-at-a-time), a context panel that slides in when selecting a task (showing related notes by keyword overlap, linked notes, all subtasks as a checklist with step-promotion to tasks, and quick actions), smart body doubling with drift-aware check-ins every 25 minutes that reference the declared task by name, a Notes panel with markdown rendering, wikilink syntax (`[[Title]]`), and live task chips that can be completed from within a note, a Weekly Review panel where Claude generates a narrative summary, auto-created daily notes on load, a command palette (Cmd+K) with full-text search, particle burst animations on task completion, and persistent storage. The final design direction was Arc browser-inspired: warm cream main area, deep plum sidebar with violet-to-rose gradient active states, warm priority/tag badges with borders, and a gradient send/action button system. Key colleagues mentioned include James from OD (blog intro format decisions), Pete (schema/feed retainer work), and the content team (needing CMS field guidance).

## First user message

> Productivity tools Productivity tools

## Topics

[[topic/404]], [[topic/blog]], [[topic/copy]], [[topic/crawl]], [[topic/ga4]], [[topic/gsc]], [[topic/inlink]], [[topic/keyword]], [[topic/pdp]], [[topic/plp]], [[topic/redirect]], [[topic/schema]], [[topic/screaming-frog]], [[topic/semrush]]

## Skills referenced

none detected
