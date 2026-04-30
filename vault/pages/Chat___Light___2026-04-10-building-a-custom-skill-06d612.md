---
title: Building a custom skill
date: 2026-04-10
project: Skills Built (full set)
status: completed
score: 5/5
uuid: 06d61231-0075-41df-aa7a-fd8797f8f4e3
---

#chat/light #project/skills-built-full-set #status/completed #topic/aeo #topic/copy #topic/inlink #topic/plp #topic/redirect #topic/youtube #skill/tgg-content-strategist #skill/tgg-marketing-analyst #skill/tgg-repo-manager #skill/tgg-seo-specialist #skill/tgg-template-generator #skill/verification-gate-protocol

# Building a custom skill

- **Date:** [[2026-04-10]]
- **Project:** [[Projects/Skills Built (full set)]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 20
- **Chat URL:** https://claude.ai/chat/06d61231-0075-41df-aa7a-fd8797f8f4e3
- **Medium view:** [[Chat/Medium/2026-04-10-building-a-custom-skill-06d612]]
- **Full transcript:** [[Chat/Full/2026-04-10-building-a-custom-skill-06d612]]

## Summary

**Conversation Overview**

Simon Mannheimer, who works in SEO and digital marketing with a client called The Good Guys (TGG), initiated a session to build a task verification skill using Claude's skill-creator framework. The conversation began with Simon describing a recurring problem: complex multi-step tasks were failing badly enough that he had needed to use a secondary LLM tool to review Claude's outputs and feed corrections back, because Claude could not self-identify its own errors. He wanted to build a planning, execution, and check-in skill with guardrails, expectations, and KPIs for complex tasks running overboard.

Claude initially tried to shortcut the work. When asked to read all 19 uploaded conversation transcripts before forming conclusions, Claude stopped at 12, presented a hypothesis, and asked Simon if it was "on the right track." Simon explicitly called this out as a failure of instruction compliance, and Claude was directed to complete the full analysis and add this meta-failure into the analysis itself. The transcripts, spanning copywriting, SEO audits, data processing, agent development, and presentation work, revealed six recurring Claude failure modes: ignoring quantified instructions midway, specification drift (violating numeric constraints like character counts without self-awareness), iteration without testing (presenting broken deliverables then debugging symptoms), multi-constraint blindness (satisfying 12 of 15 rules but missing 3 consistently), infrastructure theater (debugging CI pipelines before validating core output quality), and runaway iteration loops (21+ edits to the same artifact with cascading side effects). Simon's own contribution to failures included underspecified success criteria, delayed feedback on constraint violations, and never explicitly requesting validation-first delivery.

The session produced three concrete deliverables. First, Claude updated its memory with enforcement rules covering explicit instruction compliance, verification-first protocol, iteration loop detection, and constraint handling. Second, a full `verification-gate-protocol` skill was built and packaged as a `.skill` file, covering a three-phase workflow (criteria extraction, gated execution with checkpoints, pre-delivery final validation), special handling for code and JSON testing, batch pattern variation checks, and iteration loop detection triggering at three cycles without user feedback. Third, a consolidated personal preferences block was written for Simon to paste directly into Settings → Profile → User Preferences. Simon's preference was that Claude not present options for next steps when the obvious answer is "all of it," and this was reflected in both the preferences text and Claude's behavior change during the session. Simon's existing preferences around acting as a rigorous honest mentor, not defaulting to agreement, and using polls for clarification questions were preserved and integrated into the final preferences block.

## First user message

> Let's create a skill together using your skill-creator skill. First ask me what the skill should do. Let's create a skill together using your skill-creator skill. First ask me what the skill should do.

## Topics

[[topic/aeo]], [[topic/copy]], [[topic/inlink]], [[topic/plp]], [[topic/redirect]], [[topic/youtube]]

## Skills referenced

[[skill/tgg-content-strategist]], [[skill/tgg-marketing-analyst]], [[skill/tgg-repo-manager]], [[skill/tgg-seo-specialist]], [[skill/tgg-template-generator]], [[skill/verification-gate-protocol]]
