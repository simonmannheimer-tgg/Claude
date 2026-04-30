# Prompt: Competitor Analysis

---

## Full competitor overview

```
@claude Use the seo-competitor-analyst agent to analyse [COMPETITOR-DOMAIN].
I want:
- Organic traffic estimate and trend
- Top 10 keywords by traffic
- Backlink profile summary (referring domains, top anchors)
- 10 keyword gap opportunities vs [OUR-DOMAIN]
Database: uk. Save to seo/outputs/.
```

---

## Multi-competitor comparison

```
@claude Use the seo-competitor-analyst agent to compare these domains:
- Our domain: [OUR-DOMAIN]
- Competitors: [COMP1], [COMP2], [COMP3]

For each competitor I want:
- Estimated organic traffic
- Number of ranking keywords
- Domain authority / rating
- Top 3 content categories driving traffic

Then identify: where are all competitors ranking that we aren't?
Database: uk.
```

---

## Backlink opportunity research

```
@claude Use the seo-competitor-analyst agent to find backlink opportunities.
Analyse backlinks pointing to [COMPETITOR-DOMAIN] and identify:
- High-DR sites linking to them but not to us
- Resource pages or roundup articles we could pitch
- Any broken link opportunities
Focus on links with domain rating > 40.
```
