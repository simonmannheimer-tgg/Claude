---
title: YouTube optimization agent development
date: 2026-04-07
project: main
status: completed
score: 5/5
uuid: 45b4034a-0749-4a0e-878f-b3f06ece5a39
---

#chat/light #project/main #status/completed #topic/aeo #topic/blog #topic/gsc #topic/inlink #topic/keyword #topic/pdp #topic/plp #topic/profound #topic/regex #topic/schema #topic/sitemap #topic/youtube

# YouTube optimization agent development

- **Date:** [[2026-04-07]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 141
- **Chat URL:** https://claude.ai/chat/45b4034a-0749-4a0e-878f-b3f06ece5a39
- **Medium view:** [[Chat/Medium/2026-04-07-youtube-optimization-agent-development-45b403]]
- **Full transcript:** [[Chat/Full/2026-04-07-youtube-optimization-agent-development-45b403]]

## Summary

**Conversation overview**

This was an extended iterative build session for a YouTube Metadata Optimizer agent built in Profound AI for The Good Guys (thegoodguys.com.au), an Australian electronics and appliance retailer. The person works on the SEO/eCommerce team and is building tooling to generate AEO-optimised YouTube metadata (titles, descriptions, tags, hashtags, chapters, internal links, transcripts) ready to paste into YouTube Studio. The session picked up from a prior compacted conversation and continued debugging, refining, and extending the agent through approximately versions 11 through 25 (single-video) and sheet versions 1 through 8.

The core work involved diagnosing why the agent was producing broken outputs — specifically: timestamps all showing 0:00 (SerpAPI transcript connector strips timing data), sitemap nodes returning URL strings instead of content (firecrawl:map doesn't fetch XML, firecrawl:scrape does), fabricated URLs, duplicate URLs, and missing product type coverage in category links. Multiple approaches to solving the timestamp problem were explored and abandoned: scraping youtube-transcript.io (requires login, blocked), scraping the YouTube page directly (JS-rendered, blocked), a Python Code node using youtube_transcript_api (pip install not supported in Profound), and a Call API node to SerpAPI (SerpAPI is built into Profound, no direct API key available). The final solution was adding a manual "Timed Transcript (paste from YouTube)" long-text input to the Start node, which the user pastes from YouTube's Show Transcript panel. This proved the simplest and most reliable approach. The agent was also significantly streamlined — removing the SerpAPI transcript node, duplicate Google Search nodes, failed code nodes, and a Scorecard node — reducing to 12 nodes and 2 LLM calls (GPT-4o mini for keyword inference, GPT-5 mini for metadata generation).

A second agent was built for batch processing: a sheet-powered version that reads from a Profound Sheet (imported from a CSV with columns Video Title, Video URL, Transcript), uses a JavaScript Code node to find the first unprocessed row, runs the full pipeline on that row's data, creates a Google Doc with the output, and writes the doc link back to the sheet. The "first row keeps repeating" bug was diagnosed — the Code node was checking the `Optimised Metadata Package` column which Profound writes to unpredictably, so it was updated to check Profound's own status column (`YouTube Metadata Optimizer V2 (Sheet)`) which reliably shows `completed` for processed rows. Key prompt fixes applied to both agents included: hard enforcement of no em dashes (naming the Unicode characters explicitly), fixing duplicate "The Good Guys" in titles, updating title character limit from 70 to 100 characters with front-loading guidance for mobile truncation, adding a short-video chapter warning (`[VIDEO MAY BE TOO SHORT FOR CHAPTERS]` for videos under 60 seconds), adding a product/topic summary paragraph for AEO citation, video type awareness (unboxing vs review vs comparison vs how-to), and adding the YouTube Video URL as the first line of every output document.

**Tool knowledge**

For Profound AI agent JSON architecture, several non-obvious patterns were confirmed through this session. The `firecrawl:scrape` connector works for XML sitemaps with `formats: "markdown"` and `only_main_content: false`; `firecrawl:map` does not fetch content and only returns the URL string. All variable IDs must be in strict UUID format (36 characters, 4 hyphens) — shorthand IDs like `pr-video-url-0001` cause Profound's parser to fail with "Unexpected token" errors. Any variable referenced via `{{variable-id}}` in a prompt must also appear in that node's `input_variables` array or Profound throws a template validation error on import. The Start node requires `"selected": true` and at least one output variable or Profound will not allow saving or running the agent. Transitive edges (a direct connection where an alternative path already exists between two nodes) cause an "execution ambiguity" import error and must be removed. Edge IDs must follow the format `xy-edge__[sourceNodeId]output-[targetNodeId]`. For the sheet version, Profound's own run status column (named after the agent) is the most reliable way to detect processed rows — the `Optimised Metadata Package` output column is written to rows unpredictably and cannot be used for row

## First user message

> I want to add on to this agent, creating a best practice youtube optimisation agent; I want to add on to this agent, creating a best practice youtube optimisation agent;

## Topics

[[topic/aeo]], [[topic/blog]], [[topic/gsc]], [[topic/inlink]], [[topic/keyword]], [[topic/pdp]], [[topic/plp]], [[topic/profound]], [[topic/regex]], [[topic/schema]], [[topic/sitemap]], [[topic/youtube]]

## Skills referenced

none detected
