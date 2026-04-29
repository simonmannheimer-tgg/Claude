---
title: Finding SEO-relevant agents for cross-team workflows
date: 2026-03-18
project: Skills Built (full set)
status: completed
score: 5/5
uuid: 86f6e284-5363-4889-9da7-934bf734987e
---

#chat/light #project/skills-built-full-set #status/completed #topic/aeo #topic/agent #topic/bfcm #topic/copy #topic/ga4 #topic/gsc #topic/inlink #topic/keyword #topic/mcp #topic/meta #topic/plp #topic/schema #topic/semrush #topic/sitemap #skill/tgg-content-strategist #skill/tgg-marketing-analyst #skill/tgg-repo-manager #skill/tgg-seo-specialist #skill/tgg-template-generator

# Finding SEO-relevant agents for cross-team workflows

- **Date:** [[2026-03-18]]
- **Project:** [[Projects/Skills Built (full set)]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 28
- **Chat URL:** https://claude.ai/chat/86f6e284-5363-4889-9da7-934bf734987e
- **Medium view:** [[Chat/Medium/2026-03-18-finding-seo-relevant-agents-for-cross-team-workflows-86f6e2]]
- **Full transcript:** [[Chat/Full/2026-03-18-finding-seo-relevant-agents-for-cross-team-workflows-86f6e2]]

## Summary

**Conversation overview**

Simon Mannheimer is an in-house SEO Strategist at The Good Guys (thegoodguys.com.au), Australia's major electronics and appliances retailer based in Melbourne. He works across AEO/AI visibility strategy, PLP copy production, technical SEO, internal linking, schema markup, Semrush position tracking, GSC/GA4 analysis, and cross-team work with dev, merch, and content teams. Primary competitor is JB Hi-Fi. Simon uses both Claude.ai and Claude Code (terminal CLI) as core workflow tools, and is building out a systematic agent and skills infrastructure across both platforms.

The conversation covered three main workstreams. First, Simon explored subagents.app to identify relevant agents for his in-house SEO role, and Claude curated a shortlist of five priority agents: SEO Specialist, Content Strategist, Base Template Generator, PR Manager (stripped of swarm dependencies), and Marketing Analyst. Second, Claude built five complete skill files and five corresponding subagent configs for Claude Code, plus a HANDOVER.md document — all carrying TGG-specific context including PLP character limits (230–260 chars), em dash rules, brand PLP banned words, BFCM 2025 performance baselines (non-brand clicks -41.2% YoY), AEO frameworks, and Semrush AU database patterns. Third, Claude rebuilt the same five skills as Claude.ai-compatible SKILL.md files packaged as ZIPs for upload via Settings > Customize > Skills — one skill per ZIP, with a fixed YAML frontmatter error (unquoted colon in the description field of the SEO specialist skill).

Simon confirmed all five Claude.ai skills are live. Claude explained how auto-triggering works via the SKILL.md description field, gave explicit prompt examples for each skill, and documented a maintenance workflow covering when to update skills, how to repackage ZIPs, and the YAML validation pattern to catch colon errors. Two memory instructions were saved: always state which skill is loaded at the start of a response, and when a conversation produces a rule or constraint change captured in a skill, either update the skill file and offer a new ZIP immediately, or ask permission first if the change is ambiguous or potentially permanent. Simon's stated preference is for Claude to be proactive about skill maintenance rather than waiting to be asked.

## First user message

> https://subagents.app/categories < identify all agents relevant to my work or potential work as an inhouse seo working cross team etc. including repo management for my claude code, template generation for inhouse templates, dev methodologies for best practices etc. https://subagents.app/categories < identify all agents relevant to my work or potential work as an inhouse seo working cross team etc.

## Topics

[[topic/aeo]], [[topic/agent]], [[topic/bfcm]], [[topic/copy]], [[topic/ga4]], [[topic/gsc]], [[topic/inlink]], [[topic/keyword]], [[topic/mcp]], [[topic/meta]], [[topic/plp]], [[topic/schema]], [[topic/semrush]], [[topic/sitemap]]

## Skills referenced

[[skill/tgg-content-strategist]], [[skill/tgg-marketing-analyst]], [[skill/tgg-repo-manager]], [[skill/tgg-seo-specialist]], [[skill/tgg-template-generator]]
