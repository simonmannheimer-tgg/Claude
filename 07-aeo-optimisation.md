# Process 07: AEO (Answer Engine Optimisation)

> **Version:** 1.0 — Extracted from Master Prompt Tasks 13–14  
> **Last updated:** 2026-02-27

## Purpose

Review content and generate actionable recommendations to improve performance in AI-generated answers (ChatGPT, Google AI Overviews, Perplexity).

---

## Task 7A: AEO Improvement Suggestions

**Input:** Article URL or content  
**Output:** 5–10 numbered suggestions

**Focus areas:**
- Making answers more direct and extractable
- Improving clarity, structure, and factual grounding
- Adding or refining definitions, lists, and concise explanations
- Strengthening signals that help AI systems confidently cite this content

**Output:** Numbered list only. No explanations, introductions, or summaries.

```
1. [Specific actionable suggestion]
2. [Specific actionable suggestion]
...
```

---

## Task 7B: Finalise AEO Suggestions

**Input:** AEO scorecard + previous suggestions + article URL  
**Output:** Refined list of 5–10 high-impact suggestions

**Requirements:**
- Contextualise every suggestion to the specific article
- Remove duplicates and overlapping ideas
- Eliminate overly general or low-impact suggestions
- **Exclude non-semantic/technical recommendations** (schema markup, metadata, page speed, internal linking — those belong in other processes)
- Focus only on semantic, content-level improvements that improve clarity, answerability, and AI citability

**Output:** Numbered list only, 5–10 items, no additional text.

---

## Standard Workflow

```
04C (Summarise Article)
  → 04D (Core Keyword)
    → 06A (Link Opportunities)
      → 7A (AEO Suggestions)
        → 7B (Finalise Suggestions)
```

---

## What Makes Content AI-Citable

These principles inform the suggestions:

- **Direct answers** in the first 1–2 sentences of a section
- **Structured data** — clear headings, consistent formatting
- **Specific claims** with attributable facts (numbers, brand names, specs)
- **FAQ format** for common questions — AI engines extract Q&A pairs easily
- **Entity-rich language** — named brands, technologies, specifications
- **Concise definitions** before detailed explanations
- **Comparison tables** rather than buried prose comparisons
