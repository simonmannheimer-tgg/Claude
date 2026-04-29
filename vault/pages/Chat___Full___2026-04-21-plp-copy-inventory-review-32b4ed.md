---
title: PLP copy inventory review (full)
parent: Chat/Light/2026-04-21-plp-copy-inventory-review-32b4ed
uuid: 32b4ed02-6508-4c20-9d1c-b858233587b4
---

#chat/full #project/main #status/tactical

# PLP copy inventory review — Full Transcript

→ Light view: [[Chat/Light/2026-04-21-plp-copy-inventory-review-32b4ed]]
→ Medium view: [[Chat/Medium/2026-04-21-plp-copy-inventory-review-32b4ed]]

**Messages:** 4 | **Date:** 2026-04-21

---

### 1. **Human** — 2026-04-21T04:28

can you do inventory of all our converstaions around PLP copy - skills, rules, files
can you do inventory of all our converstaions around PLP copy - skills, rules, files

---

### 2. **Claude** — 2026-04-21T04:29

Simon wants an inventory of all conversations around PLP copy - skills, rules, files. Let me search past conversations.
```
This block is not supported on your current device yet.
```

Good results. Let me search for more specific conversations around PLP copy rules, audits, and files.
```
This block is not supported on your current device yet.
```

Good. Now let me search for more conversations around PLP copy auditor, batch production, and the skill building session.
```
This block is not supported on your current device yet.
```

I have enough to build a comprehensive inventory. Let me also check for any conversations specifically around batch PLP production or the auditor script.Here's the full inventory across skills, rules, files, and production conversations.

---

## Skill: `tgg-copywriting`

**Location:** `/mnt/skills/user/tgg-copywriting/`

**Reference files inside the skill:**

| File | Covers |
|---|---|
| `SKILL.md` | Routing table, 5-step workflow, content type identification |
| `references/00-tov.md` | Hard bans, overuse warnings, Australian English, Price Beat/C&C rules |
| `references/01-plp-intros.md` | Char limits, structure rules, QA checklist, batch output format |
| `references/02-metadata.md` | Meta title (≤60 chars), meta description (140–155 chars), placement rules |
| `references/03-inlink-migration.md` | HTML rewrites, top-to-bottom copy, Slate/CSS formatting |
| `references/05-faq-category-copy.md` | FAQ generation, brand+category copy, extended intros |
| `references/08-eav-descriptions.md` | EAV mapping (research-led, not standard copywriting) |

**Rule change history worth knowing:**
- Char range moved from 230–260 → **220–250**, ideal 225–235. Updated in both `01-plp-intros.md` and `SKILL.md` description. Done in the skill-creator session (March 19).
- Open unresolved question: whether EAV descriptions (250–265 chars) and PLP intros (220–250 chars) serve the same CMS field or different fields.

---

## Tooling Built Around PLP Copy

| Artefact | Purpose | Origin |
|---|---|---|
| `tgg_plp_auditor.py` | Scrapes live PLP intros, checks char count, sentence count, TGG mention, banned openers | March 27 session |
| `tgg-copywriting.skill` (ZIP) | Packaged skill for upload/install | March 19 skill-creator session |

---

## Production Conversations

| Chat | What was produced |
|---|---|
| [March 18](https://claude.ai/chat/63f3c699-be20-4241-9b4e-ec7a94d34c97) | Built `tgg-copywriting` skill from GitHub process files |
| [March 19](https://claude.ai/chat/99986fbb-2079-49c5-ae7b-17847d965610) | Updated char range to 220–250 via skill-creator, repackaged |
| [March 25](https://claude.ai/chat/9a215b0b-7b78-4ab4-acfc-9f4ea69ab146) | Samsung and Hisense 2026 Latest TVs PLP intro + metadata |
| [March 27](https://claude.ai/chat/fe21d9bb-451e-438e-a2ff-ef8d48139457) | Built `tgg_plp_auditor.py` |
| [April 10](https://claude.ai/chat/ebe80843-1d40-42f2-ab24-f76562aeddad) | Google Pixel 10a copy + metadata for `/google/phones-and-wearables/mobile-phones` |
| [April 16](https://claude.ai/chat/254fb60a-e13e-4edb-b7d8-004a9f816965) | Portable monitors PLP intro + metadata (entity fabrication incident documented) |

---

**One flag:** The portable monitors session surfaced a live skill compliance failure. The rule "entities match the page" in `01-plp-intros.md` was violated by fabricating brands. Worth confirming the skill now has a stronger pre-write page-fetch step enforcing that check.
 
Here's the full inventory across skills, rules, files, and production conversations.

---

## Skill: `tgg-copywriting`

**Location:** `/mnt/skills/user/tgg-copywriting/`

**Reference files inside the skill:**

| File | Covers |
|---|---|
| `SKILL.md` | Routing table, 5-step workflow, content type identification |
| `references/00-tov.md` | Hard bans, overuse warnings, Australian English, Price Beat/C&C rules |
| `references/01-plp-intros.md` | Char limits, structure rules, QA checklist, batch output format |
| `references/02-metadata.md` | Meta title (≤60 chars), meta description (140–155 chars), placement rules |
| `references/03-inlink-migration.md` | HTML rewrites, top-to-bottom copy, Slate/CSS formatting |
| `references/05-faq-category-copy.md` | FAQ generation, brand+category copy, extended intros |
| `references/08-eav-descriptions.md` | EAV mapping (research-led, not standard copywriting) |

**Rule change history worth knowing:**
- Char range moved from 230–260 → **220–250**, ideal 225–235. Updated in both `01-plp-intros.md` and `SKILL.md` description. Done in the skill-creator session (March 19).
- Open unresolved question: whether EAV descriptions (250–265 chars) and PLP intros (220–250 chars) serve the same CMS field or different fields.

---

## Tooling Built Around PLP Copy

| Artefact | Purpose | Origin |
|---|---|---|
| `tgg_plp_auditor.py` | Scrapes live PLP intros, checks char count, sentence count, TGG mention, banned openers | March 27 session |
| `tgg-copywriting.skill` (ZIP) | Packaged skill for upload/install | March 19 skill-creator session |

---

## Production Conversations

| Chat | What was produced |
|---|---|
| [March 18](https://claude.ai/chat/63f3c699-be20-4241-9b4e-ec7a94d34c97) | Built `tgg-copywriting` skill from GitHub process files |
| [March 19](https://claude.ai/chat/99986fbb-2079-49c5-ae7b-17847d965610) | Updated char range to 220–250 via skill-creator, repackaged |
| [March 25](https://claude.ai/chat/9a215b0b-7b78-4ab4-acfc-9f4ea69ab146) | Samsung and Hisense 2026 Latest TVs PLP intro + metadata |
| [March 27](https://claude.ai/chat/fe21d9bb-451e-438e-a2ff-ef8d48139457) | Built `tgg_plp_auditor.py` |
| [April 10](https://claude.ai/chat/ebe80843-1d40-42f2-ab24-f76562aeddad) | Google Pixel 10a copy + metadata for `/google/phones-and-wearables/mobile-phones` |
| [April 16](https://claude.ai/chat/254fb60a-e13e-4edb-b7d8-004a9f816965) | Portable monitors PLP intro + metadata (entity fabrication incident documented) |

---

**One flag:** The portable monitors session surfaced a live skill compliance failure. The rule "entities match the page" in `01-plp-intros.md` was violated by fabricating brands. Worth confirming the skill now has a stronger pre-write page-fetch step enforcing that check.

---

### 3. **Human** — 2026-04-21T04:30

create a zip of all this together that i can share to an ai agent as the project needs a re-set in terms of progress and next steps.

Audit assumptions against known and emerging copywriting for AI methods, noting entitites, semantics, koray's semantic seo frameworks and how Top copy is good for AI and seo
create a zip of all this together that i can share to an ai agent as the project needs a re-set in terms of progress and next steps.

Audit assumptions against known and emerging copywriting for AI methods, noting entitites, semantics, koray's semantic seo frameworks and how Top copy is good for AI and seo

---

### 4. **Claude** — 2026-04-21T04:33

Simon wants me to:
1. Read the actual skill files to understand current rules
2. Create a comprehensive ZIP that an AI agent can use as a project reset
3. Audit the current assumptions against modern AI copywriting methods (entities, semantics, Koray's semantic SEO framework, top copy for AI/SEO)

Let me read the skill files first, then create the ZIP.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now I have all the reference files. Let me now create a comprehensive ZIP with:

1. All existing skill reference files (copied)
2. A new `PROJECT_RESET.md` with:
   - Project context and current state
   - Progress summary
   - Next steps
   - Audit of current assumptions vs AI/SEO best practices including Koray's semantic SEO frameworks, entity SEO, top copy for AI
3. An audit doc comparing current rules against emerging best practices

Let me think about the audit section first:

**Koray Tuğrul's Semantic SEO framework** - key concepts:


- Topical authority built through exhaustive semantic coverage of all sub-topics and attributes
- Contextual vectors that define the meaning field around a topic
- Entity-attribute-relationship modeling to capture how concepts connect
- Structured topical maps showing content hierarchy
- Micro-semantic intent at each content node
- Passage ranking capabilities that let Google rank individual sections
- Semantic distance measuring how closely related concepts sit in embedding space
- Source entity identification for the main topic
- Contextual coverage ensuring all semantically related aspects are addressed
- Knowledge Graph alignment to match Google's entity understanding

Now I'm thinking about how entities themselves drive relevance—named entities let search engines and AI match content at the concept level rather than just keywords, and when related entities appear together they reinforce topic relevance. Using full entity names instead of pronouns helps with disambiguation, and entity prominence and density both matter for how search systems evaluate content. For AI systems specifically, they favor definite statements over hedged language, high entity density, structured information that directly answers queries, strong source signals, and factual content broken into quotable passages. The current approach already handles entity naming well for brands and products.

But there are two meaningful gaps: the intro doesn't consider topical authority or semantic coverage—it exists as an isolated unit without ensuring its entities represent the highest-salience ones for the broader topic the page needs to cover. And there's no explicit framing of the source entity itself, the core "what is this page fundamentally about" question, even though the rules do emphasize brand and tech entities upfront.

The framework also doesn't model how entities relate to each other—just listing them independently misses the semantic value of entities that co-occur with proper relationships. For AI systems reading the intro as a citable passage, there's another layer: they need factual completeness, declarative sentence structure with clear subject-verb-object patterns, and attribute-value pairs stated explicitly rather than implied. And the current rules don't distinguish between entity salience and sheer entity volume—more entities aren't always better if they're not the right ones.

There's also a process gap: EAV mapping is positioned as optional research, but writers skip it and go straight to drafting, so if entity selection depends on EAV output, it can't stay optional. Finally, the 5C extended intro structure covers overview, options, benefits, and guidance, but it's not anchored to Koray's principle of covering all relevant semantic sub-topics for the category—the 5-entity requirement feels arbitrary without that grounding.

The intro's position as the only editable free-text block above the product grid is actually a critical SEO/AEO signal that sets the semantic frame for the entire page, especially since Google's crawler and AI systems prioritize above-fold content and use it to establish context for everything downstream. And while the 5C structure does impose discipline, it's not connected to structured data markup, which would reinforce those signals further.

The FAQ section also needs tighter alignment—each question should match Google's featured snippet patterns, each answer should stand alone as a citable unit, and the FAQ entities should map directly to the intro entities to form a cohesive topical coverage rather than scattered answers.

I'm going to document the full project context and production history in one file, then create a separate audit that maps out the gaps between the current approach and what modern AI/semantic systems actually reward.Now I have everything I need. Let me build the ZIP.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

28KB ZIP. Here is what is inside and what the audit found.

---

**Package structure:**

```
PROJECT_RESET.md        ← Full context: retailer, system purpose, production history, open issues, next steps
AUDIT_AI_SEO.md         ← Gaps analysis against semantic SEO / AI copywriting methods
skill-reference/
  SKILL.md              ← Routing, workflow, page types
  00-tov.md             ← Hard bans, overuse warnings, Australian English
  01-plp-intros.md      ← PLP intro rules (canonical version)
  02-metadata.md        ← Meta title + description rules
  05-faq-category-copy.md
  08-eav-descriptions.md
```

---

**Audit findings in order of impact:**

**Strong already.** Entity density discipline, definite language, Type B/C specificity rules, and the tight 220–250 char constraint are all well-aligned with how search engines and AI systems weight content. These are ahead of standard ecommerce practice.

**Gap 1 — No source entity salience framework.** The rules say "name a specific tech or format" but do not require the entities chosen to be the highest co-occurrence ones for the category. Two intros can both comply with the current rules while one is semantically dominant and the other is peripheral.

**Gap 2 — Entity listing vs entity co-occurrence.** Naming Samsung, Bespoke, and French door as a list is weaker than expressing them in syntactic relationship. AI passage extraction favours relational claims over entity enumerations.

**Gap 3 — Passage citability is not explicit.** S1 should be independently interpretable and answer an implied question. The current checklist does not test for this.

**Gap 4 — EAV is advisory, not enforced.** Process 08 exists and is correctly designed. It is systematically skipped. Making it mandatory before 01 and 05 for new or stale categories closes both the entity fabrication risk and the salience gap.

**Gap 5 — FAQ archetypes missing.** Definitional, comparison, how-to, and criteria questions need structurally different answers. One 1–3 sentence template misses all four.

**Gap 6 — 5C extended intro is a fixed template, not a semantic coverage check.** The 5-paragraph structure does not adapt to the actual sub-topic map of a category.

**Gap 7 — The intro's role as a page-level contextual frame is underused.** The intro entities set the semantic frame for how the entire page is indexed and cited. The entity selection principle should reflect the full product range semantics, not just the most prominent products.
 
Now I have everything I need. Let me build the ZIP.
28KB ZIP. Here is what is inside and what the audit found.

---

**Package structure:**

```
PROJECT_RESET.md        ← Full context: retailer, system purpose, production history, open issues, next steps
AUDIT_AI_SEO.md         ← Gaps analysis against semantic SEO / AI copywriting methods
skill-reference/
  SKILL.md              ← Routing, workflow, page types
  00-tov.md             ← Hard bans, overuse warnings, Australian English
  01-plp-intros.md      ← PLP intro rules (canonical version)
  02-metadata.md        ← Meta title + description rules
  05-faq-category-copy.md
  08-eav-descriptions.md
```

---

**Audit findings in order of impact:**

**Strong already.** Entity density discipline, definite language, Type B/C specificity rules, and the tight 220–250 char constraint are all well-aligned with how search engines and AI systems weight content. These are ahead of standard ecommerce practice.

**Gap 1 — No source entity salience framework.** The rules say "name a specific tech or format" but do not require the entities chosen to be the highest co-occurrence ones for the category. Two intros can both comply with the current rules while one is semantically dominant and the other is peripheral.

**Gap 2 — Entity listing vs entity co-occurrence.** Naming Samsung, Bespoke, and French door as a list is weaker than expressing them in syntactic relationship. AI passage extraction favours relational claims over entity enumerations.

**Gap 3 — Passage citability is not explicit.** S1 should be independently interpretable and answer an implied question. The current checklist does not test for this.

**Gap 4 — EAV is advisory, not enforced.** Process 08 exists and is correctly designed. It is systematically skipped. Making it mandatory before 01 and 05 for new or stale categories closes both the entity fabrication risk and the salience gap.

**Gap 5 — FAQ archetypes missing.** Definitional, comparison, how-to, and criteria questions need structurally different answers. One 1–3 sentence template misses all four.

**Gap 6 — 5C extended intro is a fixed template, not a semantic coverage check.** The 5-paragraph structure does not adapt to the actual sub-topic map of a category.

**Gap 7 — The intro's role as a page-level contextual frame is underused.** The intro entities set the semantic frame for how the entire page is indexed and cited. The entity selection principle should reflect the full product range semantics, not just the most prominent products.
