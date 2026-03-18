# Prompt: Keyword Research

Use this prompt in an issue comment (`@claude ...`) or as a workflow dispatch input.

---

## Full cluster research

```
@claude Use the seo-keyword-researcher agent to research keywords for "[TOPIC]".
I want:
- Primary keyword (highest volume we can realistically rank for)
- 10 supporting long-tail keywords grouped by intent (informational / commercial / transactional)
- 5 quick-win keywords (KD < 40, volume > 200)
- Database: uk
Save results to seo/outputs/ and summarise here.
```

---

## Competitor keyword gap

```
@claude Use the seo-keyword-researcher and seo-competitor-analyst agents to find keyword gaps between [OUR-DOMAIN] and [COMPETITOR-DOMAIN].
Focus on:
- Keywords competitor ranks in top 10 that we don't appear for at all
- Informational keywords with volume > 500
- Filter to uk database
Give me the top 20 opportunities with volume, KD, and recommended page type.
```

---

## SERP feature research

```
@claude Research the SERP landscape for "[KEYWORD]" using the seo-keyword-researcher agent.
Tell me:
- Current SERP features (featured snippet, PAA, local pack, etc.)
- Top 5 ranking domains and their content types
- Is there a featured snippet opportunity?
- Recommended content format to target
```
