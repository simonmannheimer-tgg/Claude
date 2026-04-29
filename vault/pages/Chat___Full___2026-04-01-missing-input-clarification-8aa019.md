---
title: Missing input clarification (full)
parent: Chat/Light/2026-04-01-missing-input-clarification-8aa019
uuid: 8aa01934-78e4-4f55-a2de-f66301ffd452
---

#chat/full #project/main #status/completed

# Missing input clarification — Full Transcript

→ Light view: [[Chat/Light/2026-04-01-missing-input-clarification-8aa019]]
→ Medium view: [[Chat/Medium/2026-04-01-missing-input-clarification-8aa019]]

**Messages:** 2 | **Date:** 2026-04-01

---

### 1. **Human** — 2026-04-01T21:45

It has no starting input?
It has no starting input?

---

### 2. **Claude** — 2026-04-01T21:45

You're absolutely right to flag that — **the Parallel Deep Research template has no Start node inputs connected to the research node**. Looking at the structure:

```
Flow: Start → Parallel Deep Research → End
Inputs: Article Topic, Your Brand Name (e.g. Profound), Additional Instructions
```

But then the research prompt references `[Article Topic]` and `[Your Brand Name]` — which means **those input variables need to be passed into the Parallel Deep Research node**, but the template description doesn't show how they're connected.

---

## What's likely happening (based on Profound's architecture):

In the actual JSON, the **Parallel Deep Research node** would have an `input_variables` array that references the Start node's output variables:

```json
{
  "id": "research-node-id",
  "type": "parallel_deep_research",
  "data": {
    "label": "Parallel Deep Research",
    "output_label": "Parallel Deep Research Output",
    "input_variables": [
      {
        "id": "article-topic-var-id",
        "name": "Article Topic",
        "node_id": "start-node-id"
      },
      {
        "id": "brand-name-var-id", 
        "name": "Your Brand Name",
        "node_id": "start-node-id"
      },
      {
        "id": "additional-instructions-var-id",
        "name": "Additional Instructions", 
        "node_id": "start-node-id"
      }
    ],
    "model_parameters": {
      "research_prompt": "Conduct a comprehensive analysis about {{article-topic-var-id}} for {{brand-name-var-id}}...",
      "output_format": "text"
    }
  }
}
```

---

## The missing piece in the template doc:

The template description **should have specified**:

**Node 1 — Parallel Deep Research**
- Type: Parallel Deep Research
- **Input Variables**: Article Topic, Your Brand Name, Additional Instructions (all from Start node)
- Research Prompt: `Conduct a comprehensive analysis about {{Article Topic}} for {{Your Brand Name}}...`
- Output Format: Text
- Output Label: Parallel Deep Research Output

---

## For your workflow design work:

When you're **building or debugging Profound agents**, always check:

1. **Does the node reference variables in its prompt?** → Those variables must be in `input_variables`
2. **Where do those variables come from?** → Each must have a `node_id` pointing to the source node
3. **Are the variable IDs consistent?** → The `{{variable-id}}` in the prompt must match the `id` in `input_variables`

This is exactly the kind of validation error that causes **import failures** — Profound will reject JSON where a prompt references `{{article_topic}}` but that variable isn't declared in the node's inputs.

---

Would you like me to help you design a workflow, or do you have a specific agent structure you want to build/debug?
 You're absolutely right to flag that — **the Parallel Deep Research template has no Start node inputs connected to the research node**. Looking at the structure:

```
Flow: Start → Parallel Deep Research → End
Inputs: Article Topic, Your Brand Name (e.g. Profound), Additional Instructions
```

But then the research prompt references `[Article Topic]` and `[Your Brand Name]` — which means **those input variables need to be passed into the Parallel Deep Research node**, but the template description doesn't show how they're connected.

---

## What's likely happening (based on Profound's architecture):

In the actual JSON, the **Parallel Deep Research node** would have an `input_variables` array that references the Start node's output variables:

```json
{
  "id": "research-node-id",
  "type": "parallel_deep_research",
  "data": {
    "label": "Parallel Deep Research",
    "output_label": "Parallel Deep Research Output",
    "input_variables": [
      {
        "id": "article-topic-var-id",
        "name": "Article Topic",
        "node_id": "start-node-id"
      },
      {
        "id": "brand-name-var-id", 
        "name": "Your Brand Name",
        "node_id": "start-node-id"
      },
      {
        "id": "additional-instructions-var-id",
        "name": "Additional Instructions", 
        "node_id": "start-node-id"
      }
    ],
    "model_parameters": {
      "research_prompt": "Conduct a comprehensive analysis about {{article-topic-var-id}} for {{brand-name-var-id}}...",
      "output_format": "text"
    }
  }
}
```

---

## The missing piece in the template doc:

The template description **should have specified**:

**Node 1 — Parallel Deep Research**
- Type: Parallel Deep Research
- **Input Variables**: Article Topic, Your Brand Name, Additional Instructions (all from Start node)
- Research Prompt: `Conduct a comprehensive analysis about {{Article Topic}} for {{Your Brand Name}}...`
- Output Format: Text
- Output Label: Parallel Deep Research Output

---

## For your workflow design work:

When you're **building or debugging Profound agents**, always check:

1. **Does the node reference variables in its prompt?** → Those variables must be in `input_variables`
2. **Where do those variables come from?** → Each must have a `node_id` pointing to the source node
3. **Are the variable IDs consistent?** → The `{{variable-id}}` in the prompt must match the `id` in `input_variables`

This is exactly the kind of validation error that causes **import failures** — Profound will reject JSON where a prompt references `{{article_topic}}` but that variable isn't declared in the node's inputs.

---

Would you like me to help you design a workflow, or do you have a specific agent structure you want to build/debug?
