# TGG Skills Audit — 1 May 2026

20 user skills audited. Public and example skills excluded (Anthropic-maintained, not editable).

---

## 1. Dependency Map

| Skill | Depends on | Depended on by | Risk if renamed |
|---|---|---|---|
| docx-human-style | none | tgg-prompt-architect | LOW |
| mhtml-reader | none | tgg-prompt-architect | LOW |
| simon-voice | none | none | NONE |
| skill-zip-sync | none (consumes Drive ZIPs) | tgg-conversation-indexer (aside prompt) | MEDIUM (aside text refers to it) |
| tgg-301-mapper | none | none | NONE |
| tgg-chart-creator | none | tgg-prompt-architect | LOW |
| tgg-content-strategist | none | tgg-humanizer, tgg-prompt-architect | MEDIUM |
| tgg-contentful-linker | none | tgg-prompt-architect | LOW |
| **tgg-conversation-indexer** | **skill-zip-sync (file pattern), Drive files (5 hardcoded names), Active Sprint file** | tgg-prompt-architect, tgg-session-anchor | **HIGH** |
| tgg-copywriting | none | tgg-humanizer, tgg-prompt-architect, verification-gate-protocol | MEDIUM |
| tgg-humanizer | tgg-content-strategist, tgg-copywriting, tgg-seo-specialist (mentioned as cooperative) | tgg-prompt-architect | LOW |
| tgg-marketing-analyst | none | tgg-prompt-architect | LOW |
| tgg-monthly-seo-report | none | tgg-prompt-architect | LOW |
| tgg-pptx-style | none | tgg-prompt-architect | LOW |
| **tgg-prompt-architect** | **15 skills referenced by name** | none | **HIGH (it references everything; renames break here)** |
| tgg-repo-manager | none | tgg-prompt-architect | LOW |
| tgg-seo-specialist | none | tgg-humanizer, tgg-prompt-architect, verification-gate-protocol | MEDIUM |
| **tgg-session-anchor** | **tgg-conversation-indexer, Active Sprint file, all-time index file** | none | **HIGH** |
| tgg-template-generator | none | tgg-prompt-architect | LOW |
| verification-gate-protocol | tgg-copywriting, tgg-seo-specialist (mentioned cooperatively) | tgg-prompt-architect, tgg-session-anchor | MEDIUM |

**Critical insight:** Three skills carry significant rename risk because they reference other skills or files by name. Any rename to a skill referenced inside these will silently break the system:
- `tgg-prompt-architect` references 15 skill names
- `tgg-conversation-indexer` references 5 Drive filenames + skill-zip-sync's filename pattern
- `tgg-session-anchor` references the indexer and Drive files

---

## 2. Description Quality — Issues Found

Issues ranked by severity. "Hi-trigger" = description is too broad and likely fires when not wanted. "Lo-trigger" = description is too narrow and will miss valid triggers.

### Severity HIGH

#### tgg-content-strategist
**Issue:** Description overlaps almost entirely with tgg-copywriting (PLP intros, FAQ, category copy). Both fire on similar triggers, leading to ambiguity about which loads.
**Better description:** Should explicitly say "strategy and planning, not production. Use tgg-copywriting for actual copy delivery."
**Recommend rename?** No, but disambiguate scope.

#### tgg-seo-specialist
**Issue:** Description claims it covers "any SEO task" including PLP intros, metadata, FAQ. This is the same coverage as tgg-copywriting and tgg-content-strategist. Three skills competing for the same triggers.
**Better description:** "Use for technical SEO tasks: schema, AEO, internal linking, audits. For copy production use tgg-copywriting. For strategy use tgg-content-strategist."
**Recommend rename?** No, but tighten scope.

#### tgg-prompt-architect
**Issue:** Description says "ALWAYS USE THIS SKILL FIRST on every user message". This is the right intent but it's not actually firing on every message (today's session proves it). The description doesn't explain how it fires — it relies on me reading the instruction and remembering. Same failure mode as anchor:start.
**Better description:** Add concrete fire conditions. "This is a silent pre-processor. It fires on every message that is longer than 5 words OR contains a deliverable noun (write, build, draft, audit, analyse, generate, create)."
**Recommend rename?** No.

### Severity MEDIUM

#### tgg-conversation-indexer
**Issue:** Description doesn't mention that skill-zip-sync ZIP filename pattern is a hard dependency. If skill-zip-sync changes its naming convention, the indexer's auto-sync (Step 8) breaks silently.
**Fix:** Add to description: "Depends on skill-zip-sync filename pattern (skill-name_YYYYMMDD-HHMM.zip)."

#### tgg-session-anchor
**Issue:** Already fixed today (removed "scoped work request" exception). Description is accurate now.
**No action needed.**

#### tgg-template-generator
**Issue:** Description doesn't differentiate from tgg-copywriting briefs or tgg-content-strategist briefs. Three skills produce briefs.
**Fix:** Specify "use for blank-slate scaffolding when no existing artefact exists. Use tgg-copywriting for copy briefs. Use tgg-monthly-seo-report for monthly report briefs."

#### simon-voice
**Issue:** Description is good but doesn't say what NOT to use it for (technical writing, schema briefs, code comments). Risk of firing on internal documentation.
**Fix:** Add "Do not use for technical specs, code documentation, or briefs intended for AI consumption."

### Severity LOW

#### docx-human-style
**Issue:** Description is solid. Only minor: doesn't say it works alongside `docx` public skill (Anthropic's). Worth noting since both fire on .docx.
**Fix:** Add "Layers on top of the public docx skill — both should fire."

#### mhtml-reader
**Issue:** None. Description is precise.

#### skill-zip-sync
**Issue:** Description doesn't say where it runs (Claude Code only, not Claude.ai). Today's session showed user confusion about which side runs the sync.
**Fix:** Add to description: "Runs in Claude Code only. Claude.ai produces the ZIPs; Claude Code processes them."

#### tgg-301-mapper
**Issue:** None significant. Description is clear and scoped.

#### tgg-chart-creator
**Issue:** None significant.

#### tgg-contentful-linker
**Issue:** Description says "When in doubt, surface the link". Borderline hi-trigger but acceptable.

#### tgg-copywriting
**Issue:** None. Description is one of the strongest.

#### tgg-humanizer
**Issue:** Description is excellent. Lists exact triggers and exact patterns it fixes.

#### tgg-marketing-analyst
**Issue:** None.

#### tgg-monthly-seo-report
**Issue:** None.

#### tgg-pptx-style
**Issue:** None.

#### tgg-repo-manager
**Issue:** None.

#### verification-gate-protocol
**Issue:** Description doesn't say it's silent. Risk that Claude announces "loading verification gate" rather than running it invisibly. Today's chats suggest this is happening.
**Fix:** Add "Runs silently. Do not announce or label this skill in responses."

---

## 3. Issues That Are Not About Descriptions

These are real problems but not fixable by editing skill descriptions:

### A. tgg-prompt-architect doesn't actually fire reliably
Same failure mode as anchor:start before today's fix. The skill says "always run first" but I can skip it without consequence. There's no enforcement mechanism. The description fix above (concrete fire conditions) helps but isn't a full solution.

### B. Three copy/SEO skills overlap
tgg-copywriting, tgg-content-strategist, tgg-seo-specialist all claim PLP intros, FAQ, metadata. When you say "write 5 PLP intros", all three should fire by their descriptions. Recommend consolidating: tgg-copywriting for production, tgg-content-strategist for strategy/calendars, tgg-seo-specialist for technical SEO only.

### C. tgg-conversation-indexer Drive file dependencies are not documented in the skill description
Five Drive filenames are hardcoded inside the skill body but not surfaced in the description or anywhere outside the skill. If any get renamed in Drive, the indexer breaks and there's no obvious failure signal.

### D. The skill-zip-sync trigger prompt fix
Today's session caught the `example_conversations.md` bug. Already fixed in skill body. Worth a follow-up check that no other skill copies that exact phrase.

### E. No skill registry or index file
There's no single file listing all 20 skills, their dependencies, and their fire conditions. This audit becomes the source of truth, but it ages immediately. A `SKILLS_INDEX.md` in the repo would help, auto-generated by skill-zip-sync.

---

## 4. Naming Audit

All current skill names are consistent with `tgg-*` for TGG-specific and unprefixed for general-purpose. Three skills don't follow this convention:
- `simon-voice` — personal, not TGG-specific. Acceptable as-is.
- `verification-gate-protocol` — general-purpose. Acceptable.
- `docx-human-style` — general-purpose. Acceptable.
- `mhtml-reader` — general-purpose. Acceptable.
- `skill-zip-sync` — infrastructure. Acceptable.

**No renames recommended.** Renaming any TGG skill would require updating tgg-prompt-architect (15 references), tgg-session-anchor (4 references), tgg-humanizer (3 references), and verification-gate-protocol (2 references).

---

## 5. Priority-Ordered Fix List

If you want me to apply all of these:

| # | Skill | Fix | Risk | Time |
|---|---|---|---|---|
| 1 | tgg-prompt-architect | Add concrete fire conditions to description | LOW | 2 min |
| 2 | verification-gate-protocol | Add "Runs silently. Do not announce." | LOW | 1 min |
| 3 | tgg-content-strategist | Disambiguate from tgg-copywriting | LOW | 2 min |
| 4 | tgg-seo-specialist | Tighten scope to technical SEO | LOW | 2 min |
| 5 | tgg-template-generator | Differentiate from other brief-producing skills | LOW | 2 min |
| 6 | simon-voice | Add what NOT to use it for | LOW | 1 min |
| 7 | tgg-conversation-indexer | Note skill-zip-sync filename dependency | LOW | 1 min |
| 8 | skill-zip-sync | Note "runs in Claude Code only" | LOW | 1 min |
| 9 | docx-human-style | Note "layers on public docx skill" | LOW | 1 min |
| | | **Total** | | **~15 min** |

All of these are description-only edits. None change behaviour, none affect dependent skills.
