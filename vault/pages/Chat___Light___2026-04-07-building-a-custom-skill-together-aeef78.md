---
title: Building a custom skill together
date: 2026-04-07
project: main
status: completed
score: 5/5
uuid: aeef7830-a429-485b-8451-0e075d7bda1d
---

#chat/light #project/main #status/completed #topic/copy #topic/inlink #topic/plp #topic/schema #topic/semrush #skill/tgg-copywriting #skill/tgg-seo-specialist

# Building a custom skill together

- **Date:** [[2026-04-07]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 16
- **Chat URL:** https://claude.ai/chat/aeef7830-a429-485b-8451-0e075d7bda1d
- **Medium view:** [[Chat/Medium/2026-04-07-building-a-custom-skill-together-aeef78]]
- **Full transcript:** [[Chat/Full/2026-04-07-building-a-custom-skill-together-aeef78]]

## Summary

**Conversation overview**

The person works at The Good Guys (TGG) and asked Claude to collaboratively build a new skill using the skill-creator framework. The specific goal was to create an "mhtml-reader" skill that teaches Claude how to properly read and interpret MHTML files — single-file web page archives saved from browsers. The person explained they regularly save two main categories of MHTML files: AI conversation transcripts (from platforms like Claude, ChatGPT, Gemini, Microsoft Copilot, Manus, and SubAgents) saved for context handoff or task continuation, and web page snapshots (competitor pages, TGG's own site, analytics tools like Semrush) saved for analysis purposes.

Through a structured requirements-gathering process, the person clarified the desired behavior for each file type. For AI conversations, Claude should extract the full transcript, summarize what was being worked on, identify key findings, assumptions, and next steps, then ask what the person wants to do. For web pages and analytics snapshots, Claude should identify the page or tool, briefly describe what it is, and ask what the person wants to analyze. The person confirmed the skill should auto-trigger whenever any MHTML file is uploaded, without requiring an explicit invocation phrase. When asked to choose a parsing approach, the person deferred to Claude's judgment, and Claude selected proper MHTML parsing using Python's email library and BeautifulSoup over faster but lossy alternatives, reasoning that the person's SEO work requires precision in copy extraction, metadata, and heading structure.

Claude inventoried 53 uploaded MHTML files to inform the skill design, categorizing them into AI conversations (~16 files from various platforms), competitor and market research pages (~35 files including JB Hi-Fi, EB Games, Officeworks, brand sites, and TGG's own pages), and analytics snapshots (~2 Semrush files). The completed skill includes a SKILL.md with type detection logic, platform-specific response formats, a full Python parsing script, and test prompts. Claude noted known limitations: AI conversation parsing is currently generic rather than platform-specific for user/assistant turn structure, competitor page analysis is reactive rather than automatically structured, and large MHTML files carry token costs.

**Tool knowledge**

Claude used bash tools to inventory MHTML files efficiently using a loop over `*.mhtml` with `grep -m1` on the `Subject:` and `Snapshot-Content-Location:` headers — this pattern reliably extracts file type and source URL without parsing the full MHTML body. The `Snapshot-Content-Location` header is the authoritative field for determining file origin and should be checked before `Subject` for type detection. Python's `email.message_from_binary_file` with `policy=policy.default` is the correct approach for MHTML parsing; iterating `msg.walk()` and filtering for `part.get_content_type() == 'text/html'` reliably finds the main HTML part. BeautifulSoup with `html.parser` (not `lxml`) worked for extracting clean text after removing script, style, and noscript elements. The skill file was packaged using `zipfile.ZipFile` with `ZIP_DEFLATED` compression and saved with a `.skill` extension to `/mnt/user-data/outputs/`.

## First user message

> Let's create a skill together using your skill-creator skill. First ask me what the skill should do. Let's create a skill together using your skill-creator skill. First ask me what the skill should do.

## Topics

[[topic/copy]], [[topic/inlink]], [[topic/plp]], [[topic/schema]], [[topic/semrush]]

## Skills referenced

[[skill/tgg-copywriting]], [[skill/tgg-seo-specialist]]
