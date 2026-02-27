# SEO Prompt Audit — The Good Guys

## Summary

10 process files created from 4 source documents. 5 original contradictions identified — all resolved. Philosophy: guardrails not templates; ban harmful patterns, don't prescribe "allowed" patterns.

---

## Process Inventory

| # | Process | File |
|---|---------|------|
| 00 | TOV & Language Reference | `00-tov-language-reference.md` |
| 01 | PLP Intro Copy (2-Sentence) | `01-plp-intro-copy.md` |
| 02 | Metadata Generation | `02-metadata-generation.md` |
| 03 | Inlink Migration (Top→Bottom) | `03-inlink-migration.md` |
| 04 | Content Analysis | `04-content-analysis.md` |
| 05 | FAQ & Category Copy | `05-faq-category-copy.md` |
| 06 | Internal Linking | `06-internal-linking.md` |
| 07 | AEO Optimisation | `07-aeo-optimisation.md` |
| 08 | EAV Mapping | `08-eav-mapping.md` |
| 09 | AI Visibility Polling | `09-ai-visibility-polling.md` |

---

## Contradictions — All Resolved

### 1. PLP Intro Character Range → RESOLVED
- SOP said 235–250. Standalone prompt said 230–260.
- **Resolution:** 230–260 is the range. ~250 is the sweet spot. Don't force or truncate unnaturally.

### 2. Sentence 1 "Allowed" Verbs → RESOLVED
- Standalone prompt had a prescriptive list of allowed openers.
- **Resolution:** Removed the allowed list entirely. Instead: don't open S1 with Discover/Explore/Shop (those suit S2 better), and vary openers across batches to avoid template patterns. No prescriptive "must use from this list."

### 3. "The Good Guys" Placement → RESOLVED
- SOP said "preferably S2." Standalone prompt said "S2 only."
- **Resolution:** Place naturally — doesn't have to be the last words of S2. Include exactly once. Vary placement across batches so it doesn't read like a formula.

### 4. Brand PLP Banned Words → RESOLVED
- SOP had no brand-specific bans. Standalone prompt banned: trusted, reliable, enjoy, features.
- **Resolution:** These are overuse bans on brand PLPs specifically (because they make brand copy feel generic). Fine in moderation on category PLPs. Documented in `00-tov-language-reference.md`.

### 5. EAV Description Length vs PLP Intro Length → RESOLVED
- EAV process was writing 250–265 character descriptions. PLP intros are 230–260 characters.
- **Resolution:** EAV is now a mapping/research process only — it produces entity lists, not descriptions. The descriptions are written by Process 01 (PLP intros) or Process 02 (metadata) using EAV as input.

---

## Key Design Decisions

### Guardrails, Not Templates
- No "allowed verb" lists — these steer writing into repetitive patterns
- Instead: hard bans (things that must never appear) and overuse warnings (things to use sparingly)
- Copy should vary in structure, opener, TGG placement, and angle across batches

### SEM Copy Guide Integration
- SEM Copy Guide rules now live in `00-tov-language-reference.md`
- Applies across ALL content-writing processes, not just PLP intros
- Key additions: sale→deal, save→pay less, no "exclusive" re: deals, energy claim restrictions, upgrade only for aspirational products, "across a range" not "across the range"

### EAV as Foundation
- EAV mapping (Process 08) is now a research step, not a writing step
- Produces entity/attribute/value lists that feed into other writing processes
- Run EAV first, then use the output to inform intros, FAQs, metadata, etc.

---

## Workflows (Process Chains)

**Workflow A — Category Page Optimisation:**
`08 (EAV)` → `04 (Core Query + Fanout)` → `06 (Hierarchy Validation + Link Status)` → `05 (Brand+Category FAQ)`

**Workflow B — Article AEO Audit:**
`04 (Summarise + Keyword)` → `06 (Link Opportunities)` → `07 (AEO Suggestions + Finalise)`

**Workflow C — Internal Linking:**
`06 (Find → Validate Hierarchy → Verify Status → Insert)`

**Workflow D — Full Category Page Build:**
`08 (EAV)` → `04 (Fanout)` → `01 (PLP Intro)` → `05 (FAQ Copy)` → `02 (Metadata)` → `06 (Internal Linking)`
