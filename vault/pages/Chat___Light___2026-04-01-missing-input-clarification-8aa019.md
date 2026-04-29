---
title: Missing input clarification
date: 2026-04-01
project: main
status: completed
score: 2/5
uuid: 8aa01934-78e4-4f55-a2de-f66301ffd452
---

#chat/light #project/main #status/completed #topic/blog #topic/profound

# Missing input clarification

- **Date:** [[2026-04-01]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 2/5: deliverable, project-keyword)
- **Messages:** 2
- **Chat URL:** https://claude.ai/chat/8aa01934-78e4-4f55-a2de-f66301ffd452
- **Medium view:** [[Chat/Medium/2026-04-01-missing-input-clarification-8aa019]]
- **Full transcript:** [[Chat/Full/2026-04-01-missing-input-clarification-8aa019]]

## Summary

**Conversation Overview**

The conversation was very brief and focused on a technical question about workflow architecture in Profound, an AI agent-building platform. The person asked a pointed question about whether a specific template — a Parallel Deep Research workflow — had any starting inputs connected to its research node. Claude confirmed the issue and provided a detailed technical explanation of how input variables should be wired between nodes in Profound's JSON-based architecture.

Claude explained that the Parallel Deep Research node requires an `input_variables` array referencing the Start node's output variables (such as Article Topic, Your Brand Name, and Additional Instructions), and that the prompt within the node must reference matching variable IDs. Claude provided an example JSON structure illustrating the correct configuration and outlined three validation checks for building or debugging Profound agents: confirming that variables referenced in prompts are declared in `input_variables`, verifying each variable has a `node_id` pointing to its source node, and ensuring variable IDs are consistent between prompt references and declarations. Claude noted that mismatches in this structure cause import failures in Profound.

The conversation ended with Claude offering to help design a workflow or debug a specific agent structure, but no follow-up response was provided by the person.

## First user message

> It has no starting input? It has no starting input?

## Topics

[[topic/blog]], [[topic/profound]]

## Skills referenced

none detected
