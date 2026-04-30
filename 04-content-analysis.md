# Process 04: Content Analysis

> **Version:** 1.0 — Extracted from Master Prompt Tasks 1–5  
> **Last updated:** 2026-02-27

## Purpose

Analyse web content to extract core queries, related search patterns, summaries, keywords, and entities. These outputs feed into other processes (FAQ copy, internal linking, AEO optimisation).

---

## Task 4A: Determine Core Search Query

**Input:** Full text of a webpage or article  
**Output:** Single plain-text search query

**Rules:**
- One query only — the most likely search that would surface this page
- Natural, concise, real-world phrasing
- Everyday language unless topic requires technical terms
- No explanation, no quotation marks, no multiple options

**Example:** Article titled "How to Clean White Sneakers Without Damaging Them" → `how to clean white sneakers`

---

## Task 4B: Query Fanout Estimator

**Input:** A primary user search query  
**Output:** 5–10 related queries

**Rules:**
- Consider the user journey: before, during, and after the primary search
- Include intent angles: how, what, why, best, vs, comparison
- Natural conversational phrasing
- Do not repeat the original query

**Output Format:**
```
Prompt: [original query]

Fanout Queries: [comma-separated list]
```

No numbering, no commentary. End immediately after the final query.

---

## Task 4C: Summarise Article

**Input:** URL or raw article content  
**Output:** Single paragraph, 3–5 sentences

**Rules:**
- If URL: extract main body content only (ignore nav, ads, sidebars, boilerplate)
- Mention core subjects, subtopics, and distinct concepts
- Focus on specificity — this summary will be used for internal linking opportunities
- No commentary or preamble

---

## Task 4D: Determine Core Keyword

**Input:** Article summary + brand domain  
**Output:** Single keyword/keyphrase (1–5 words)

**Consider:**
- Core topic of the summary
- Search intent to find this content
- Relevance to the brand's domain and niche
- What drives the most valuable organic traffic

**Output only the keyword. Nothing else.**

---

## Task 4E: Entity Extraction

**Input:** Article or page content  
**Output:** Entities list + subject-verb-object triplets

**Entity Types:**
- Brand names
- Model numbers/names
- Technologies/features
- Specifications (capacity, size, power)
- Benefits/claims

**Output Format:**
```
ENTITIES:
- [Entity 1]
- [Entity 2]
...

TRIPLETS:
1. [Subject] → [Verb] → [Object]
2. [Subject] → [Verb] → [Object]
...
```

Minimum: 10–15 entities, 5–10 triplets.

---

## Chaining

These tasks feed into other processes:

| This task | Feeds into |
|-----------|-----------|
| 4A (Core Query) | 4B (Fanout), 05 (FAQ generation) |
| 4B (Fanout) | 05 (FAQ/category copy), 01 (PLP intros) |
| 4C (Summarise) | 4D (Keyword), 06 (Link opportunities) |
| 4D (Keyword) | 06 (Link opportunities), 07 (AEO) |
| 4E (Entities) | 05 (FAQ copy), 08 (EAV mapping) |
