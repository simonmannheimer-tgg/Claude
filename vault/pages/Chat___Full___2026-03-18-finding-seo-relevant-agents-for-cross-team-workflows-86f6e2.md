---
title: Finding SEO-relevant agents for cross-team workflows (full)
parent: Chat/Light/2026-03-18-finding-seo-relevant-agents-for-cross-team-workflows-86f6e2
uuid: 86f6e284-5363-4889-9da7-934bf734987e
---

#chat/full #project/semrush-migration #status/completed

# Finding SEO-relevant agents for cross-team workflows — Full Transcript

→ Light view: [[Chat/Light/2026-03-18-finding-seo-relevant-agents-for-cross-team-workflows-86f6e2]]
→ Medium view: [[Chat/Medium/2026-03-18-finding-seo-relevant-agents-for-cross-team-workflows-86f6e2]]

**Messages:** 28 | **Date:** 2026-03-18

---

### 1. **Human** — 2026-03-18T03:54

https://subagents.app/categories < identify all agents relevant to my work or potential work as an inhouse seo working cross team etc. including repo management for my claude code, template generation for inhouse templates, dev methodologies for best practices etc.
https://subagents.app/categories < identify all agents relevant to my work or potential work as an inhouse seo working cross team etc. including repo management for my claude code, template generation for inhouse templates, dev methodologies for best practices etc.

---

### 2. **Claude** — 2026-03-18T03:54

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


```
This block is not supported on your current device yet.
```

The site blocks direct fetching, but I've pulled enough from search results to give you a thorough picture. Here's a curated breakdown of every agent category from subagents.app plus the wider ecosystem that's relevant to your work.

---

## Agents relevant to your work — by use case

### Core SEO and digital marketing

The `seo-expert`, `seo-strategist`, and `geo-strategist` agents cover comprehensive SEO strategy, technical audits, Core Web Vitals, and Generative Engine Optimisation for AI search visibility. The geo-strategist is directly relevant to your AEO/AIO work at TGG. There's also a `content-strategist` and `content-editor` for editorial quality assurance, content optimisation, and style guides — useful for your PLP and FAQ production pipelines.

### Repo management for Claude Code

Subagents.app has a dedicated **GitHub Workflow** category covering GitHub workflow automation and repository management. This maps directly to managing your `.claude/agents/` directory and Claude.md config. The built-in `Explore` agent is a fast, read-only agent optimised for searching and analysing codebases, which is useful for navigating your process files (01-09) without polluting the main context.

### Template generation

There's a dedicated **Code Generation** category on subagents.app for code generation, templates, and boilerplate creators. For your SEO process templates specifically, the `copywriter-specialist` and `content-editor` agents from the marketing cluster are worth adapting.

### Dev methodologies and best practices

Subagents.app has a **Development Process** category covering development process methodologies and frameworks. In the broader ecosystem, the `wshobson/agents` repo includes an SDD (spec-driven development) workflow that enforces a structured requirements → design → tasks pipeline, plus a TDD workflow with verification checkpoints.

### Documentation

There's a **Documentation** category on subagents.app for documentation creation, maintenance, and automation. Given your 9 process files and Claude.md memory system, a documentation agent that reads your `.claude/` directory and keeps process files current would have real value.

### Data processing and Python automation

Subagents.app includes a **Data Science** category for data processing, analysis, and machine learning development. Given your active work on `semrush_csv_merger.py` and the keyword batch exporter, a dedicated Python/data agent with `Bash`, `Read`, `Write` tools would handle these without context bleed into your main sessions.

### Cross-team and product work

For working cross-functionally with dev teams at TGG:

- A `feedback-synthesizer` agent (product category) and `sprint-prioritizer` are useful for translating SEO recommendations into dev-ready briefs.
- The `content-strategist` and `copywriter-specialist` agents cover persuasive copywriting, conversion psychology, and sales messaging — relevant when briefing merch or CRO teams.
- The `geo-strategist` is specifically scoped to GEO for AI search visibility, which aligns with your AI Visibility and Polling Framework.

### Quality assurance and code review

The **Testing & QA** category has three agents covering automated testing, quality assurance, and validation. For your scripts specifically, the `NeoLabHQ/code-review` skill deploys specialist subagents including a bug-hunter, security-auditor, and code-quality-reviewer in parallel — useful for validating Python scripts before sending processed files to external parties like the Semrush migration team.

### SEO and content agent skills (beyond subagents.app)

Sanity has published an official `seo-aeo-best-practices` skill covering SEO and answer engine optimisation patterns for content sites — directly applicable to your AEO framework. There's also a `firecrawl` plugin for web scraping and search that could replace or augment your Playwright scrapers.

---

## Priority shortlist for your setup

| Agent/Skill | Where to get it | Why relevant |
|---|---|---|
| `seo-strategist` + `geo-strategist` | rshah515/claude-code-subagents | AEO, AI visibility, technical audits |
| `content-editor` + `copywriter-specialist` | rshah515/claude-code-subagents | PLP/FAQ production, brand voice |
| GitHub Workflow agent | subagents.app | `.claude/` repo management |
| Code Generation / Templates | subagents.app | SEO process file templating |
| Development Process agent | subagents.app | Best practices for Python scripts |
| Documentation agent | subagents.app / GitHub | Keeping process files 01-09 current |
| `seo-aeo-best-practices` skill | VoltAgent/awesome-agent-skills (Sanity) | AEO patterns for content sites |
| Data Science agent | subagents.app | CSV processing, batch keyword work |

The most actionable starting point: grab the `geo-strategist` and `seo-strategist` MDs from rshah515's repo, adapt them to TGG's context (including your PLP rules and brand voice constraints), and drop them into `~/.claude/agents/` for global availability across projects.
The site blocks direct fetching, but I've pulled enough from search results to give you a thorough picture. Here's a curated breakdown of every agent category from subagents.app plus the wider ecosystem that's relevant to your work.

---

## Agents relevant to your work — by use case

### Core SEO and digital marketing

The `seo-expert`, `seo-strategist`, and `geo-strategist` agents cover comprehensive SEO strategy, technical audits, Core Web Vitals, and Generative Engine Optimisation for AI search visibility. The geo-strategist is directly relevant to your AEO/AIO work at TGG. There's also a `content-strategist` and `content-editor` for editorial quality assurance, content optimisation, and style guides — useful for your PLP and FAQ production pipelines.

### Repo management for Claude Code

Subagents.app has a dedicated **GitHub Workflow** category covering GitHub workflow automation and repository management. This maps directly to managing your `.claude/agents/` directory and Claude.md config. The built-in `Explore` agent is a fast, read-only agent optimised for searching and analysing codebases, which is useful for navigating your process files (01-09) without polluting the main context.

### Template generation

There's a dedicated **Code Generation** category on subagents.app for code generation, templates, and boilerplate creators. For your SEO process templates specifically, the `copywriter-specialist` and `content-editor` agents from the marketing cluster are worth adapting.

### Dev methodologies and best practices

Subagents.app has a **Development Process** category covering development process methodologies and frameworks. In the broader ecosystem, the `wshobson/agents` repo includes an SDD (spec-driven development) workflow that enforces a structured requirements → design → tasks pipeline, plus a TDD workflow with verification checkpoints.

### Documentation

There's a **Documentation** category on subagents.app for documentation creation, maintenance, and automation. Given your 9 process files and Claude.md memory system, a documentation agent that reads your `.claude/` directory and keeps process files current would have real value.

### Data processing and Python automation

Subagents.app includes a **Data Science** category for data processing, analysis, and machine learning development. Given your active work on `semrush_csv_merger.py` and the keyword batch exporter, a dedicated Python/data agent with `Bash`, `Read`, `Write` tools would handle these without context bleed into your main sessions.

### Cross-team and product work

For working cross-functionally with dev teams at TGG:

- A `feedback-synthesizer` agent (product category) and `sprint-prioritizer` are useful for translating SEO recommendations into dev-ready briefs.
- The `content-strategist` and `copywriter-specialist` agents cover persuasive copywriting, conversion psychology, and sales messaging — relevant when briefing merch or CRO teams.
- The `geo-strategist` is specifically scoped to GEO for AI search visibility, which aligns with your AI Visibility and Polling Framework.

### Quality assurance and code review

The **Testing & QA** category has three agents covering automated testing, quality assurance, and validation. For your scripts specifically, the `NeoLabHQ/code-review` skill deploys specialist subagents including a bug-hunter, security-auditor, and code-quality-reviewer in parallel — useful for validating Python scripts before sending processed files to external parties like the Semrush migration team.

### SEO and content agent skills (beyond subagents.app)

Sanity has published an official `seo-aeo-best-practices` skill covering SEO and answer engine optimisation patterns for content sites — directly applicable to your AEO framework. There's also a `firecrawl` plugin for web scraping and search that could replace or augment your Playwright scrapers.

---

## Priority shortlist for your setup

| Agent/Skill | Where to get it | Why relevant |
|---|---|---|
| `seo-strategist` + `geo-strategist` | rshah515/claude-code-subagents | AEO, AI visibility, technical audits |
| `content-editor` + `copywriter-specialist` | rshah515/claude-code-subagents | PLP/FAQ production, brand voice |
| GitHub Workflow agent | subagents.app | `.claude/` repo management |
| Code Generation / Templates | subagents.app | SEO process file templating |
| Development Process agent | subagents.app | Best practices for Python scripts |
| Documentation agent | subagents.app / GitHub | Keeping process files 01-09 current |
| `seo-aeo-best-practices` skill | VoltAgent/awesome-agent-skills (Sanity) | AEO patterns for content sites |
| Data Science agent | subagents.app | CSV processing, batch keyword work |

The most actionable starting point: grab the `geo-strategist` and `seo-strategist` MDs from rshah515's repo, adapt them to TGG's context (including your PLP rules and brand voice constraints), and drop them into `~/.claude/agents/` for global availability across projects.

---

### 3. **Human** — 2026-03-18T03:55

tell me which ones you want
tell me which ones you want

---

### 4. **Claude** — 2026-03-18T03:55

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good, I have the full list now. Here's my honest pick for your setup specifically:

---

**Yes — install these**

**Documentation** (1 agent). Your 9 process files and Claude.md are the closest thing to institutional knowledge you have in Claude Code. A documentation agent that can read and update them on instruction is immediately useful — especially as your process rules evolve mid-project.

**GitHub Integration** (1 agent). You're managing a non-trivial `.claude/` repo with agents, process files, commands, and config. An agent scoped to repo hygiene, commit discipline, and file organisation removes overhead you're currently doing manually.

**Templates & Generators** (1 agent). With PLP intros, metadata, FAQ structures, and EAV descriptions all having strict char limits and formatting rules, a template agent trained on your constraints could batch-generate scaffolds faster than rebuilding them each session.

**Development Methodologies** (1 agent). Best-practice enforcement for your Python scripts (`semrush_csv_merger.py`, the keyword batcher, the Chrome Extension). Useful when working cross-team with TGG devs — gives you a structured brief format for dev handoffs.

**Marketing & Growth** (5 agents). This is the highest-value category for your day job. Five agents covering content strategy, automation, and growth optimisation — worth auditing individually to identify which ones map to AEO, PLP production, and campaign copy.

---

**Situational — worth inspecting but not immediately critical**

**Analysis & Review** (1 agent). Could be useful for GSC/GA4 data interpretation or auditing category page performance, but likely overlaps with what you already do with Semrush MCP.

**Product Management** (1 agent). Potentially useful for structuring cross-team briefs and roadmap inputs — depends on how formal those handoffs need to be at TGG.

**UI/UX Design** (3 agents). Marginal for an in-house SEO role unless you're producing mockups for internal decks (which you have been doing with the PPTX work).

---

**Skip**

Core Development, Testing & QA, Web Development, DevOps & Infrastructure, Data & Machine Learning, Swarm Coordination, Consensus Protocols, Performance Optimization — all of these are dev-team tools. They're not meaningless, but none map to anything in your current workflow and they'd just add noise to your agents directory.

---

The four I'd prioritise installing today: **Documentation**, **GitHub Integration**, **Templates & Generators**, **Development Methodologies** — all low agent counts (1 each), fast to review and adapt, and directly applicable to how you already use Claude Code.
Good, I have the full list now. Here's my honest pick for your setup specifically:

---

**Yes — install these**

**Documentation** (1 agent). Your 9 process files and Claude.md are the closest thing to institutional knowledge you have in Claude Code. A documentation agent that can read and update them on instruction is immediately useful — especially as your process rules evolve mid-project.

**GitHub Integration** (1 agent). You're managing a non-trivial `.claude/` repo with agents, process files, commands, and config. An agent scoped to repo hygiene, commit discipline, and file organisation removes overhead you're currently doing manually.

**Templates & Generators** (1 agent). With PLP intros, metadata, FAQ structures, and EAV descriptions all having strict char limits and formatting rules, a template agent trained on your constraints could batch-generate scaffolds faster than rebuilding them each session.

**Development Methodologies** (1 agent). Best-practice enforcement for your Python scripts (`semrush_csv_merger.py`, the keyword batcher, the Chrome Extension). Useful when working cross-team with TGG devs — gives you a structured brief format for dev handoffs.

**Marketing & Growth** (5 agents). This is the highest-value category for your day job. Five agents covering content strategy, automation, and growth optimisation — worth auditing individually to identify which ones map to AEO, PLP production, and campaign copy.

---

**Situational — worth inspecting but not immediately critical**

**Analysis & Review** (1 agent). Could be useful for GSC/GA4 data interpretation or auditing category page performance, but likely overlaps with what you already do with Semrush MCP.

**Product Management** (1 agent). Potentially useful for structuring cross-team briefs and roadmap inputs — depends on how formal those handoffs need to be at TGG.

**UI/UX Design** (3 agents). Marginal for an in-house SEO role unless you're producing mockups for internal decks (which you have been doing with the PPTX work).

---

**Skip**

Core Development, Testing & QA, Web Development, DevOps & Infrastructure, Data & Machine Learning, Swarm Coordination, Consensus Protocols, Performance Optimization — all of these are dev-team tools. They're not meaningless, but none map to anything in your current workflow and they'd just add noise to your agents directory.

---

The four I'd prioritise installing today: **Documentation**, **GitHub Integration**, **Templates & Generators**, **Development Methodologies** — all low agent counts (1 each), fast to review and adapt, and directly applicable to how you already use Claude Code.

---

### 5. **Human** — 2026-03-18T03:57



---

### 6. **Claude** — 2026-03-18T03:57

Now I have the full picture. Here's my honest take on each one you've shared:

---

**Definite yes — adapt and install**

**SEO Optimization Specialist** (`seo-specialist`). Highest-value agent in this set for your work. It covers technical SEO, on-page, keyword research, schema, Core Web Vitals, and structured data. The system prompt is solid and the YAML config is clean. Needs TGG-specific adaptation — the robots.txt and sitemap examples are generic, and the content structure section would benefit from your PLP rules baked in directly.

**Content Marketing Strategist** (`content-strategist`). Useful for PLP, FAQ, and campaign copy workflows. The audience analysis framework and content calendar scaffold are directly applicable. The SEO integration is lightweight but present. Worth installing with your char limits and brand voice constraints added to the system prompt.

**Base Template Generator** (`base-template-generator`). The one I'd install most quickly. It's simple, clean, well-scoped, and immediately applicable to your SEO process file templates. The system prompt already follows SPARC methodology, which aligns with how your process files are structured. Low adaptation effort, high practical return.

**GitHub PR Manager** (`pr-manager`). Overpowered for your current Claude Code repo management needs — it's built around a full swarm/multi-agent stack with `claude-flow` MCP tools you don't have. But the core PR lifecycle logic and hook structure are worth borrowing. Strip the swarm coordination layer, keep the branch management and commit discipline patterns.

---

**Conditional yes — useful with significant trimming**

**Marketing Analytics Specialist** (`marketing-analyst`). The attribution modeling and campaign performance frameworks are genuinely useful for GSC/GA4 analysis and building the case for SEO decisions internally. However, the agent is written for a full martech stack with GA4 pixels, Segment, Mixpanel, etc. Adapt it to focus purely on organic search performance reporting and it becomes a solid companion for the BFCM-style decks.

**SPARC Methodology Coordinator** (`sparc-coord`). Useful conceptually for structuring your Python scripts and SEO process workflows, but the YAML config relies on memory tools (`memory_store`, `memory_search`) that may not be available in your setup. The phase framework itself is worth adding to your Claude.md as a working pattern rather than installing as a standalone agent.

---

**Skip**

**Revenue Optimization Specialist** — SaaS pricing and LTV modelling. Nothing here maps to in-house retail SEO.

**Growth Engineering Specialist** — Referral engines, A/B testing infrastructure, push notification optimisation. Product/engineering territory, not yours.

**Machine Learning Developer** — Model training pipelines. Irrelevant to your current stack.

**Code Quality Analyzer** — Useful for reviewing your Python scripts, but the scope (JS/TS/Java codebases) is heavily dev-team oriented. The built-in Explore subagent in Claude Code handles most of what you'd actually need here.

**API Documentation Expert** — Not applicable.

---

**Install order if you do this today:** Base Template Generator first (zero adaptation needed, immediate use), then SEO Optimization Specialist (adapt with your PLP/char limit rules), then Content Marketing Strategist (add brand voice constraints). Leave PR Manager and Marketing Analytics for a second pass.
 Now I have the full picture. Here's my honest take on each one you've shared:

---

**Definite yes — adapt and install**

**SEO Optimization Specialist** (`seo-specialist`). Highest-value agent in this set for your work. It covers technical SEO, on-page, keyword research, schema, Core Web Vitals, and structured data. The system prompt is solid and the YAML config is clean. Needs TGG-specific adaptation — the robots.txt and sitemap examples are generic, and the content structure section would benefit from your PLP rules baked in directly.

**Content Marketing Strategist** (`content-strategist`). Useful for PLP, FAQ, and campaign copy workflows. The audience analysis framework and content calendar scaffold are directly applicable. The SEO integration is lightweight but present. Worth installing with your char limits and brand voice constraints added to the system prompt.

**Base Template Generator** (`base-template-generator`). The one I'd install most quickly. It's simple, clean, well-scoped, and immediately applicable to your SEO process file templates. The system prompt already follows SPARC methodology, which aligns with how your process files are structured. Low adaptation effort, high practical return.

**GitHub PR Manager** (`pr-manager`). Overpowered for your current Claude Code repo management needs — it's built around a full swarm/multi-agent stack with `claude-flow` MCP tools you don't have. But the core PR lifecycle logic and hook structure are worth borrowing. Strip the swarm coordination layer, keep the branch management and commit discipline patterns.

---

**Conditional yes — useful with significant trimming**

**Marketing Analytics Specialist** (`marketing-analyst`). The attribution modeling and campaign performance frameworks are genuinely useful for GSC/GA4 analysis and building the case for SEO decisions internally. However, the agent is written for a full martech stack with GA4 pixels, Segment, Mixpanel, etc. Adapt it to focus purely on organic search performance reporting and it becomes a solid companion for the BFCM-style decks.

**SPARC Methodology Coordinator** (`sparc-coord`). Useful conceptually for structuring your Python scripts and SEO process workflows, but the YAML config relies on memory tools (`memory_store`, `memory_search`) that may not be available in your setup. The phase framework itself is worth adding to your Claude.md as a working pattern rather than installing as a standalone agent.

---

**Skip**

**Revenue Optimization Specialist** — SaaS pricing and LTV modelling. Nothing here maps to in-house retail SEO.

**Growth Engineering Specialist** — Referral engines, A/B testing infrastructure, push notification optimisation. Product/engineering territory, not yours.

**Machine Learning Developer** — Model training pipelines. Irrelevant to your current stack.

**Code Quality Analyzer** — Useful for reviewing your Python scripts, but the scope (JS/TS/Java codebases) is heavily dev-team oriented. The built-in Explore subagent in Claude Code handles most of what you'd actually need here.

**API Documentation Expert** — Not applicable.

---

**Install order if you do this today:** Base Template Generator first (zero adaptation needed, immediate use), then SEO Optimization Specialist (adapt with your PLP/char limit rules), then Content Marketing Strategist (add brand voice constraints). Leave PR Manager and Marketing Analytics for a second pass.

---

### 7. **Human** — 2026-03-18T03:58

create skills for each, as well as a hadnover doc for claude code
create skills for each, as well as a hadnover doc for claude code

---

### 8. **Claude** — 2026-03-18T04:04

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good. Now I understand the format. Let me build all five skill files plus the handover doc.
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

Now the handover doc:
```
This block is not supported on your current device yet.
```

Now create the corresponding subagent `.md` files:
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


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

11 files across three directories. Here's what was built and what to do with it.

---

**File structure delivered:**

```
HANDOVER.md                          ← start here
skills/
  seo-specialist/SKILL.md
  content-strategist/SKILL.md
  base-template-generator/SKILL.md
  pr-manager/SKILL.md
  marketing-analyst/SKILL.md
agents/
  seo-specialist.md
  content-strategist.md
  base-template-generator.md
  pr-manager.md
  marketing-analyst.md
```

**Installation — two commands:**

```bash
cp -r skills/* ~/.claude/skills/
cp -r agents/* ~/.claude/agents/
```

Then run `/agents` in Claude Code to reload.

---

**What's baked into each skill that wasn't in the source agents:**

`seo-specialist` — PLP char limits (230–260), S1 action verb rule, "The Good Guys" in S2 only, brand PLP banned words, em dash replacement rule, TGG schema templates, AEO priority order (category pages first, vacuums flagged), JB Hi-Fi competitor context.

`content-strategist` — Production checklist (char count + em dash check before every delivery), AEO copy framework (definitional opening, interleaved question headings, comparison framing), BFCM URL strategy risk flagged for seasonal content.

`base-template-generator` — TGG process file format (01–09 structure), Python script starter matching your CSV processing pattern (argparse, UTF-8-sig, ThreadPoolExecutor-ready), copy brief and Semrush report templates.

`pr-manager` — Entire swarm/claude-flow layer stripped. Pure git + gh CLI. Commit message convention, PR template, CLAUDE.md pruning protocol (archive at 200 lines), YAML validation patterns for agent frontmatter.

`marketing-analyst` — Scope narrowed to organic only (no paid/social). BFCM 2025 baselines documented (sessions -23.5%, non-brand clicks -41.2%). Semrush MCP invocation pattern with `database: 'au'`. Deck output conventions (insight-led, `#002060` headers, colour-coded YoY cells).

---

**One open item flagged in the handover:** the EAV vs PLP field question (250–265 vs 230–260 chars) is noted in both the `seo-specialist` and `content-strategist` skills as unresolved. Once you confirm whether these are the same CMS field, update both files and that ambiguity is closed.
 
Good. Now I understand the format. Let me build all five skill files plus the handover doc.
Now the handover doc:
Now create the corresponding subagent `.md` files:
11 files across three directories. Here's what was built and what to do with it.

---

**File structure delivered:**

```
HANDOVER.md                          ← start here
skills/
  seo-specialist/SKILL.md
  content-strategist/SKILL.md
  base-template-generator/SKILL.md
  pr-manager/SKILL.md
  marketing-analyst/SKILL.md
agents/
  seo-specialist.md
  content-strategist.md
  base-template-generator.md
  pr-manager.md
  marketing-analyst.md
```

**Installation — two commands:**

```bash
cp -r skills/* ~/.claude/skills/
cp -r agents/* ~/.claude/agents/
```

Then run `/agents` in Claude Code to reload.

---

**What's baked into each skill that wasn't in the source agents:**

`seo-specialist` — PLP char limits (230–260), S1 action verb rule, "The Good Guys" in S2 only, brand PLP banned words, em dash replacement rule, TGG schema templates, AEO priority order (category pages first, vacuums flagged), JB Hi-Fi competitor context.

`content-strategist` — Production checklist (char count + em dash check before every delivery), AEO copy framework (definitional opening, interleaved question headings, comparison framing), BFCM URL strategy risk flagged for seasonal content.

`base-template-generator` — TGG process file format (01–09 structure), Python script starter matching your CSV processing pattern (argparse, UTF-8-sig, ThreadPoolExecutor-ready), copy brief and Semrush report templates.

`pr-manager` — Entire swarm/claude-flow layer stripped. Pure git + gh CLI. Commit message convention, PR template, CLAUDE.md pruning protocol (archive at 200 lines), YAML validation patterns for agent frontmatter.

`marketing-analyst` — Scope narrowed to organic only (no paid/social). BFCM 2025 baselines documented (sessions -23.5%, non-brand clicks -41.2%). Semrush MCP invocation pattern with `database: 'au'`. Deck output conventions (insight-led, `#002060` headers, colour-coded YoY cells).

---

**One open item flagged in the handover:** the EAV vs PLP field question (250–265 vs 230–260 chars) is noted in both the `seo-specialist` and `content-strategist` skills as unresolved. Once you confirm whether these are the same CMS field, update both files and that ambiguity is closed.

---

### 9. **Human** — 2026-03-18T04:06

i need help - what goes into claude.ai skills (and how?) what goes to claude code (and how)

* how do i use regular vlaude vs claude code?
i need help - what goes into claude.ai skills (and how?) what goes to claude code (and how)

* how do i use regular vlaude vs claude code?

---

### 10. **Claude** — 2026-03-18T04:07

Good question — the terminology overlaps in confusing ways. Let me map it out clearly.

---

## Two completely separate systems

"Skills" in **Claude.ai** and "skills" in **Claude Code** are different things with different purposes, different file formats, and different installation methods. They don't talk to each other.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's how each system actually works.

---

## Claude.ai — what goes here and how

This is the browser/app interface you're using right now. It's conversational. Nothing here touches your filesystem.

**What lives here:**

**Projects + system prompts.** In Claude.ai, you can create a Project (sidebar) and give it a system prompt — persistent instructions that apply to every conversation in that project. This is where you'd put TGG brand rules, your tone preferences, and standing instructions that should apply to all casual work (research, deck drafts, quick copy checks) without needing to paste context each time.

**Memory.** Claude.ai builds and stores facts about you across sessions — you can view and edit these by going to Settings > Memory. These are the `userMemories` entries that inform how I respond to you now. Useful for personal preferences, job context, and standing rules. You manage these through conversation ("remember that...") or the Settings panel directly.

**Style settings.** Settings > Your preferences lets you set tone, response length, and formatting preferences globally.

**MCP connectors.** Settings > Integrations — this is where your Semrush MCP connection lives. Available across all Claude.ai conversations.

**Artefacts.** Files created inline in chat (PPTX, DOCX, code, etc.) using the computer-use tools you've been using in this session.

**How to install things here:** You don't install files. You configure through the UI — Projects for system prompts, Settings for memory/preferences/integrations.

---

## Claude Code — what goes here and how

This is the terminal CLI (`claude` command). It runs in your project directory and has access to your filesystem, bash, and git. It's not conversational in the same way — it's task execution inside a repo context.

**What lives here:**

**CLAUDE.md** — the equivalent of a system prompt, but as a file. Lives in the repo root. Claude Code reads it at session start. This is where your process rules, active project context, and behavioural instructions live. You edit it like any markdown file.

**Subagents** (`~/.claude/agents/` or `.claude/agents/`) — the `.md` files we just created. YAML frontmatter defines the agent name, description, tools, and colour. The body is the system prompt. Claude Code reads the `description` field to decide when to automatically delegate to an agent. You install them by dropping the `.md` file in the right folder and running `/agents` to reload.

**Skills** (`~/.claude/skills/[name]/SKILL.md`) — instruction files that Claude Code reads before executing a relevant task. The agent's system prompt says "read the SKILL.md before beginning" — that's how they connect. You install them by creating the directory and file at the right path.

**Slash commands** (`.claude/commands/`) — shortcut prompts you invoke with `/command-name`. Each is a `.md` file containing a prompt template. Good for repetitive tasks like `/plp-review` or `/audit-category`.

**Process files** — any markdown files in your repo that agents read as reference. Your 01–09 files are these.

**How to install things here:** Copy files to the right paths, then run `/agents` or restart the session.

---

## The key difference in practice

Think of it this way:

**Claude.ai** is where you go for ad-hoc work — research, writing, deck building, quick analysis, anything that doesn't need to touch files or run scripts. Your MCP tools (Semrush, web search) are available here. Context is conversational and session-based.

**Claude Code** is where you go for systematic, repeatable, file-touching work — running your PLP production process, executing the CSV merger scripts, committing agent updates, running the keyword batch exporter. It reads your CLAUDE.md for standing context, uses your subagents for specialised tasks, and can run bash directly.

**The skills and agents we just built live in Claude Code.** They don't do anything in Claude.ai — the two systems are completely separate. The `seo-specialist` subagent won't activate in this conversation; it activates when you invoke it in a Claude Code terminal session.

---

## Installation — the exact commands

```bash
# 1. Create the skills directories
mkdir -p ~/.claude/skills/seo-specialist
mkdir -p ~/.claude/skills/content-strategist
mkdir -p ~/.claude/skills/base-template-generator
mkdir -p ~/.claude/skills/pr-manager
mkdir -p ~/.claude/skills/marketing-analyst

# 2. Copy skill files (adjust path to where you saved the outputs)
cp skills/seo-specialist/SKILL.md ~/.claude/skills/seo-specialist/
cp skills/content-strategist/SKILL.md ~/.claude/skills/content-strategist/
cp skills/base-template-generator/SKILL.md ~/.claude/skills/base-template-generator/
cp skills/pr-manager/SKILL.md ~/.claude/skills/pr-manager/
cp skills/marketing-analyst/SKILL.md ~/.claude/skills/marketing-analyst/

# 3. Copy agent configs
cp agents/seo-specialist.md ~/.claude/agents/
cp agents/content-strategist.md ~/.claude/agents/
cp agents/base-template-generator.md ~/.claude/agents/
cp agents/pr-manager.md ~/.claude/agents/
cp agents/marketing-analyst.md ~/.claude/agents/

# 4. Reload in Claude Code
# Open a Claude Code session and run:
/agents
```

After that, in a Claude Code session you can say "audit the TVs PLP" and the `seo-specialist` agent will pick it up automatically — or you can explicitly call `/agent seo-specialist` to invoke it directly.

---

## When to use which

| Task | Where |
|------|--------|
| Quick copy check / draft | Claude.ai |
| Research + Semrush pull | Claude.ai (MCP available here) |
| Building a deck | Claude.ai (artefacts) |
| PLP production at scale | Claude Code (process files + agents) |
| Running Python scripts | Claude Code (bash access) |
| Updating CLAUDE.md / agents | Claude Code |
| GSC data analysis | Either — depends on whether you're pasting data or processing files |
 Good question — the terminology overlaps in confusing ways. Let me map it out clearly.

---

## Two completely separate systems

"Skills" in **Claude.ai** and "skills" in **Claude Code** are different things with different purposes, different file formats, and different installation methods. They don't talk to each other.
Here's how each system actually works.

---

## Claude.ai — what goes here and how

This is the browser/app interface you're using right now. It's conversational. Nothing here touches your filesystem.

**What lives here:**

**Projects + system prompts.** In Claude.ai, you can create a Project (sidebar) and give it a system prompt — persistent instructions that apply to every conversation in that project. This is where you'd put TGG brand rules, your tone preferences, and standing instructions that should apply to all casual work (research, deck drafts, quick copy checks) without needing to paste context each time.

**Memory.** Claude.ai builds and stores facts about you across sessions — you can view and edit these by going to Settings > Memory. These are the `userMemories` entries that inform how I respond to you now. Useful for personal preferences, job context, and standing rules. You manage these through conversation ("remember that...") or the Settings panel directly.

**Style settings.** Settings > Your preferences lets you set tone, response length, and formatting preferences globally.

**MCP connectors.** Settings > Integrations — this is where your Semrush MCP connection lives. Available across all Claude.ai conversations.

**Artefacts.** Files created inline in chat (PPTX, DOCX, code, etc.) using the computer-use tools you've been using in this session.

**How to install things here:** You don't install files. You configure through the UI — Projects for system prompts, Settings for memory/preferences/integrations.

---

## Claude Code — what goes here and how

This is the terminal CLI (`claude` command). It runs in your project directory and has access to your filesystem, bash, and git. It's not conversational in the same way — it's task execution inside a repo context.

**What lives here:**

**CLAUDE.md** — the equivalent of a system prompt, but as a file. Lives in the repo root. Claude Code reads it at session start. This is where your process rules, active project context, and behavioural instructions live. You edit it like any markdown file.

**Subagents** (`~/.claude/agents/` or `.claude/agents/`) — the `.md` files we just created. YAML frontmatter defines the agent name, description, tools, and colour. The body is the system prompt. Claude Code reads the `description` field to decide when to automatically delegate to an agent. You install them by dropping the `.md` file in the right folder and running `/agents` to reload.

**Skills** (`~/.claude/skills/[name]/SKILL.md`) — instruction files that Claude Code reads before executing a relevant task. The agent's system prompt says "read the SKILL.md before beginning" — that's how they connect. You install them by creating the directory and file at the right path.

**Slash commands** (`.claude/commands/`) — shortcut prompts you invoke with `/command-name`. Each is a `.md` file containing a prompt template. Good for repetitive tasks like `/plp-review` or `/audit-category`.

**Process files** — any markdown files in your repo that agents read as reference. Your 01–09 files are these.

**How to install things here:** Copy files to the right paths, then run `/agents` or restart the session.

---

## The key difference in practice

Think of it this way:

**Claude.ai** is where you go for ad-hoc work — research, writing, deck building, quick analysis, anything that doesn't need to touch files or run scripts. Your MCP tools (Semrush, web search) are available here. Context is conversational and session-based.

**Claude Code** is where you go for systematic, repeatable, file-touching work — running your PLP production process, executing the CSV merger scripts, committing agent updates, running the keyword batch exporter. It reads your CLAUDE.md for standing context, uses your subagents for specialised tasks, and can run bash directly.

**The skills and agents we just built live in Claude Code.** They don't do anything in Claude.ai — the two systems are completely separate. The `seo-specialist` subagent won't activate in this conversation; it activates when you invoke it in a Claude Code terminal session.

---

## Installation — the exact commands

```bash
# 1. Create the skills directories
mkdir -p ~/.claude/skills/seo-specialist
mkdir -p ~/.claude/skills/content-strategist
mkdir -p ~/.claude/skills/base-template-generator
mkdir -p ~/.claude/skills/pr-manager
mkdir -p ~/.claude/skills/marketing-analyst

# 2. Copy skill files (adjust path to where you saved the outputs)
cp skills/seo-specialist/SKILL.md ~/.claude/skills/seo-specialist/
cp skills/content-strategist/SKILL.md ~/.claude/skills/content-strategist/
cp skills/base-template-generator/SKILL.md ~/.claude/skills/base-template-generator/
cp skills/pr-manager/SKILL.md ~/.claude/skills/pr-manager/
cp skills/marketing-analyst/SKILL.md ~/.claude/skills/marketing-analyst/

# 3. Copy agent configs
cp agents/seo-specialist.md ~/.claude/agents/
cp agents/content-strategist.md ~/.claude/agents/
cp agents/base-template-generator.md ~/.claude/agents/
cp agents/pr-manager.md ~/.claude/agents/
cp agents/marketing-analyst.md ~/.claude/agents/

# 4. Reload in Claude Code
# Open a Claude Code session and run:
/agents
```

After that, in a Claude Code session you can say "audit the TVs PLP" and the `seo-specialist` agent will pick it up automatically — or you can explicitly call `/agent seo-specialist` to invoke it directly.

---

## When to use which

| Task | Where |
|------|--------|
| Quick copy check / draft | Claude.ai |
| Research + Semrush pull | Claude.ai (MCP available here) |
| Building a deck | Claude.ai (artefacts) |
| PLP production at scale | Claude Code (process files + agents) |
| Running Python scripts | Claude Code (bash access) |
| Updating CLAUDE.md / agents | Claude Code |
| GSC data analysis | Either — depends on whether you're pasting data or processing files |

---

### 11. **Human** — 2026-03-18T04:15

what files do i upload where?
what files do i upload where?

---

### 12. **Claude** — 2026-03-18T04:15

Good question — let me be direct about this.

**There is no "uploading" for Claude Code skills or agents.** The files we created need to be on your Mac filesystem, not uploaded anywhere. Here's the full picture:
```
This block is not supported on your current device yet.
```

---

## The concrete steps

**Step 1 — Download the files from this chat**

The 11 files presented at the end of the previous response are downloadable. Save them somewhere on your Mac (e.g. `~/Downloads/claude-skills/`).

**Step 2 — Open Terminal and run these commands**

```bash
# Create the directories
mkdir -p ~/.claude/agents
mkdir -p ~/.claude/skills/seo-specialist
mkdir -p ~/.claude/skills/content-strategist
mkdir -p ~/.claude/skills/base-template-generator
mkdir -p ~/.claude/skills/pr-manager
mkdir -p ~/.claude/skills/marketing-analyst

# Copy agents (adjust the source path to wherever you saved them)
cp ~/Downloads/claude-skills/agents/*.md ~/.claude/agents/

# Copy skills
cp ~/Downloads/claude-skills/skills/seo-specialist/SKILL.md ~/.claude/skills/seo-specialist/
cp ~/Downloads/claude-skills/skills/content-strategist/SKILL.md ~/.claude/skills/content-strategist/
cp ~/Downloads/claude-skills/skills/base-template-generator/SKILL.md ~/.claude/skills/base-template-generator/
cp ~/Downloads/claude-skills/skills/pr-manager/SKILL.md ~/.claude/skills/pr-manager/
cp ~/Downloads/claude-skills/skills/marketing-analyst/SKILL.md ~/.claude/skills/marketing-analyst/
```

**Step 3 — Reload in Claude Code**

Open a Claude Code session (run `claude` in Terminal) and type `/agents` to confirm they've loaded.

---

**For Claude.ai — nothing to install.** The skills and agents don't come here. The only things you configure in Claude.ai are:

- **Projects** — create one, paste your TGG rules as plain text in the system prompt field
- **Memory** — Settings > Memory, or just tell me "remember that…" in conversation
- **Integrations** — Settings > Integrations (your Semrush MCP is already there)

The `HANDOVER.md` is just a reference document — keep it wherever makes sense to you (Desktop, Notion, your repo). It doesn't need to go anywhere specific to function.
 Good question — let me be direct about this.

**There is no "uploading" for Claude Code skills or agents.** The files we created need to be on your Mac filesystem, not uploaded anywhere. Here's the full picture:
---

## The concrete steps

**Step 1 — Download the files from this chat**

The 11 files presented at the end of the previous response are downloadable. Save them somewhere on your Mac (e.g. `~/Downloads/claude-skills/`).

**Step 2 — Open Terminal and run these commands**

```bash
# Create the directories
mkdir -p ~/.claude/agents
mkdir -p ~/.claude/skills/seo-specialist
mkdir -p ~/.claude/skills/content-strategist
mkdir -p ~/.claude/skills/base-template-generator
mkdir -p ~/.claude/skills/pr-manager
mkdir -p ~/.claude/skills/marketing-analyst

# Copy agents (adjust the source path to wherever you saved them)
cp ~/Downloads/claude-skills/agents/*.md ~/.claude/agents/

# Copy skills
cp ~/Downloads/claude-skills/skills/seo-specialist/SKILL.md ~/.claude/skills/seo-specialist/
cp ~/Downloads/claude-skills/skills/content-strategist/SKILL.md ~/.claude/skills/content-strategist/
cp ~/Downloads/claude-skills/skills/base-template-generator/SKILL.md ~/.claude/skills/base-template-generator/
cp ~/Downloads/claude-skills/skills/pr-manager/SKILL.md ~/.claude/skills/pr-manager/
cp ~/Downloads/claude-skills/skills/marketing-analyst/SKILL.md ~/.claude/skills/marketing-analyst/
```

**Step 3 — Reload in Claude Code**

Open a Claude Code session (run `claude` in Terminal) and type `/agents` to confirm they've loaded.

---

**For Claude.ai — nothing to install.** The skills and agents don't come here. The only things you configure in Claude.ai are:

- **Projects** — create one, paste your TGG rules as plain text in the system prompt field
- **Memory** — Settings > Memory, or just tell me "remember that…" in conversation
- **Integrations** — Settings > Integrations (your Semrush MCP is already there)

The `HANDOVER.md` is just a reference document — keep it wherever makes sense to you (Desktop, Notion, your repo). It doesn't need to go anywhere specific to function.

---

### 13. **Human** — 2026-03-18T06:09

give me first the claude skills for claude.ai as download files that carry the full context
give me first the claude skills for claude.ai as download files that carry the full context

---

### 14. **Claude** — 2026-03-18T06:15

Good call — Claude.ai skills (used in Projects system prompts) are fundamentally different from Claude Code SKILL.md files. These need to be self-contained, conversational instruction sets that carry all TGG context without relying on any external files being read.
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

Good. Now I understand the format clearly. Claude.ai skills are self-contained instruction documents — no file references, no external paths. Everything must be inline. Let me build all five.
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

Now verify and move to outputs:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Five files. Here's what's in each and exactly how to install them.

---

## What's in these files

These are **Claude.ai Project skills** — self-contained instruction documents that carry all TGG context inline. No external file references, no paths to read. Everything Claude needs is inside the file.

| File | What it does |
|------|-------------|
| `01-tgg-seo-specialist.md` | Technical audits, PLP copy, schema, AEO, keyword research, internal linking. Full TGG rules + BFCM competitor context. |
| `02-tgg-content-strategist.md` | Copy production — PLP intros, FAQ sections, metadata, campaign briefs. Full brand voice + char limits + production checklist. |
| `03-tgg-template-generator.md` | Generates copy briefs, audit scopes, campaign plans, dev requests, stakeholder updates. Realistic TGG placeholder content. |
| `04-tgg-marketing-analyst.md` | GSC/GA4/Semrush analysis, YoY reports, traffic concentration risk, deck-ready output. BFCM 2025 baselines baked in. |
| `05-tgg-repo-manager.md` | Commit messages, PR descriptions, CLAUDE.md entries, process file format, subagent YAML validation. |

---

## How to install in Claude.ai

**Option A — One Project with all five skills (recommended)**

1. Go to **claude.ai → Projects → New Project**
2. Name it something like "TGG SEO"
3. Open **Project Settings** (gear icon or "Set instructions")
4. In the **Custom Instructions** field, paste the content of each skill file you want active — one after another, with a heading separator between them
5. Save

The custom instructions field is essentially a system prompt. All five files together total about 47KB of text — well within limits.

**Option B — Separate Projects per skill**

Create five Projects, one per skill. Useful if you want to keep, say, analytics work completely separate from copy production. More overhead to manage but cleaner context per session.

**Option C — Upload as knowledge files**

Some Project configurations support file uploads as knowledge. If that option is available in your account, you can upload each `.md` file directly to the Project's knowledge base rather than pasting into instructions.

---

## Key difference from the Claude Code skills

The Claude Code `SKILL.md` files are read by a subagent at runtime from the filesystem. These Claude.ai files are pasted into a Project's system prompt — they're always present in context, not read on demand. That's why they're written differently: more conversational framing, explicit "who you are working with" sections, and full inline content with no file references.
 Good call — Claude.ai skills (used in Projects system prompts) are fundamentally different from Claude Code SKILL.md files. These need to be self-contained, conversational instruction sets that carry all TGG context without relying on any external files being read.
Good. Now I understand the format clearly. Claude.ai skills are self-contained instruction documents — no file references, no external paths. Everything must be inline. Let me build all five.
Now verify and move to outputs:
Five files. Here's what's in each and exactly how to install them.

---

## What's in these files

These are **Claude.ai Project skills** — self-contained instruction documents that carry all TGG context inline. No external file references, no paths to read. Everything Claude needs is inside the file.

| File | What it does |
|------|-------------|
| `01-tgg-seo-specialist.md` | Technical audits, PLP copy, schema, AEO, keyword research, internal linking. Full TGG rules + BFCM competitor context. |
| `02-tgg-content-strategist.md` | Copy production — PLP intros, FAQ sections, metadata, campaign briefs. Full brand voice + char limits + production checklist. |
| `03-tgg-template-generator.md` | Generates copy briefs, audit scopes, campaign plans, dev requests, stakeholder updates. Realistic TGG placeholder content. |
| `04-tgg-marketing-analyst.md` | GSC/GA4/Semrush analysis, YoY reports, traffic concentration risk, deck-ready output. BFCM 2025 baselines baked in. |
| `05-tgg-repo-manager.md` | Commit messages, PR descriptions, CLAUDE.md entries, process file format, subagent YAML validation. |

---

## How to install in Claude.ai

**Option A — One Project with all five skills (recommended)**

1. Go to **claude.ai → Projects → New Project**
2. Name it something like "TGG SEO"
3. Open **Project Settings** (gear icon or "Set instructions")
4. In the **Custom Instructions** field, paste the content of each skill file you want active — one after another, with a heading separator between them
5. Save

The custom instructions field is essentially a system prompt. All five files together total about 47KB of text — well within limits.

**Option B — Separate Projects per skill**

Create five Projects, one per skill. Useful if you want to keep, say, analytics work completely separate from copy production. More overhead to manage but cleaner context per session.

**Option C — Upload as knowledge files**

Some Project configurations support file uploads as knowledge. If that option is available in your account, you can upload each `.md` file directly to the Project's knowledge base rather than pasting into instructions.

---

## Key difference from the Claude Code skills

The Claude Code `SKILL.md` files are read by a subagent at runtime from the filesystem. These Claude.ai files are pasted into a Project's system prompt — they're always present in context, not read on demand. That's why they're written differently: more conversational framing, explicit "who you are working with" sections, and full inline content with no file references.

---

### 15. **Human** — 2026-03-18T06:18

or do you create 1 skill file per?
or do you create 1 skill file per?

---

### 16. **Claude** — 2026-03-18T06:18

Yes — one skill file per Project is the right model. Here's why, and how it changes the setup.

---

## The problem with all-five-in-one

When you paste all five skills into one Project's instructions, Claude has to hold all that context simultaneously and decide which role applies to each request. It works, but it's cognitively noisy — you're asking a copywriting task and the analytics framework is sitting there in context doing nothing except consuming tokens and occasionally muddying the output.

**One skill per Project gives you:**
- Cleaner, more focused responses — Claude is fully in one mode
- No ambiguity about which rules apply
- Easier to update a single skill without worrying about interactions
- Faster to load (smaller context per session)

---

## The five Projects you'd create

| Project name | Skill file to paste | When you open it |
|---|---|---|
| **TGG — SEO** | `01-tgg-seo-specialist.md` | Audits, schema, keyword research, technical work |
| **TGG — Copy** | `02-tgg-content-strategist.md` | PLP intros, FAQs, metadata, campaign copy |
| **TGG — Templates** | `03-tgg-template-generator.md` | Briefs, campaign plans, dev requests, stakeholder updates |
| **TGG — Analytics** | `04-tgg-marketing-analyst.md` | GSC/GA4 reports, Semrush analysis, deck data |
| **TGG — Repo** | `05-tgg-repo-manager.md` | Commit messages, CLAUDE.md entries, process file docs |

---

## How to set each one up

1. **claude.ai → Projects → New Project**
2. Give it the name from the table above
3. Click the **pencil / instructions** icon to open custom instructions
4. Open the `.md` file you downloaded, select all, copy
5. Paste into the instructions field — the YAML frontmatter (`---` block at the top) can be included or stripped, Claude ignores it either way
6. Save

Repeat five times. Each Project then has exactly one skill loaded and behaves as that specialist for every conversation inside it.

---

## One exception worth considering

**TGG — SEO** and **TGG — Copy** overlap heavily in practice — you often need both the content rules and the technical SEO context in the same session (writing a PLP intro while also thinking about schema and heading structure). If you find yourself constantly switching between the two, merge those two files into one "TGG — SEO + Copy" Project. The other three (Templates, Analytics, Repo) are distinct enough to stay separate.
 Yes — one skill file per Project is the right model. Here's why, and how it changes the setup.

---

## The problem with all-five-in-one

When you paste all five skills into one Project's instructions, Claude has to hold all that context simultaneously and decide which role applies to each request. It works, but it's cognitively noisy — you're asking a copywriting task and the analytics framework is sitting there in context doing nothing except consuming tokens and occasionally muddying the output.

**One skill per Project gives you:**
- Cleaner, more focused responses — Claude is fully in one mode
- No ambiguity about which rules apply
- Easier to update a single skill without worrying about interactions
- Faster to load (smaller context per session)

---

## The five Projects you'd create

| Project name | Skill file to paste | When you open it |
|---|---|---|
| **TGG — SEO** | `01-tgg-seo-specialist.md` | Audits, schema, keyword research, technical work |
| **TGG — Copy** | `02-tgg-content-strategist.md` | PLP intros, FAQs, metadata, campaign copy |
| **TGG — Templates** | `03-tgg-template-generator.md` | Briefs, campaign plans, dev requests, stakeholder updates |
| **TGG — Analytics** | `04-tgg-marketing-analyst.md` | GSC/GA4 reports, Semrush analysis, deck data |
| **TGG — Repo** | `05-tgg-repo-manager.md` | Commit messages, CLAUDE.md entries, process file docs |

---

## How to set each one up

1. **claude.ai → Projects → New Project**
2. Give it the name from the table above
3. Click the **pencil / instructions** icon to open custom instructions
4. Open the `.md` file you downloaded, select all, copy
5. Paste into the instructions field — the YAML frontmatter (`---` block at the top) can be included or stripped, Claude ignores it either way
6. Save

Repeat five times. Each Project then has exactly one skill loaded and behaves as that specialist for every conversation inside it.

---

## One exception worth considering

**TGG — SEO** and **TGG — Copy** overlap heavily in practice — you often need both the content rules and the technical SEO context in the same session (writing a PLP intro while also thinking about schema and heading structure). If you find yourself constantly switching between the two, merge those two files into one "TGG — SEO + Copy" Project. The other three (Templates, Analytics, Repo) are distinct enough to stay separate.

---

### 17. **Human** — 2026-03-18T06:19

5 separate skills? as files?
5 separate skills? as files?

---

### 18. **Claude** — 2026-03-18T06:19

Yes. Five separate files, one per Project.

You already have them — the five `.md` files from the previous download. Each one goes into its own Project as the custom instructions. That's it.

```
01-tgg-seo-specialist.md      → Project: TGG — SEO
02-tgg-content-strategist.md  → Project: TGG — Copy  
03-tgg-template-generator.md  → Project: TGG — Templates
04-tgg-marketing-analyst.md   → Project: TGG — Analytics
05-tgg-repo-manager.md        → Project: TGG — Repo
```

Open the file, select all, paste into the Project's custom instructions. Done.
 Yes. Five separate files, one per Project.

You already have them — the five `.md` files from the previous download. Each one goes into its own Project as the custom instructions. That's it.

```
01-tgg-seo-specialist.md      → Project: TGG — SEO
02-tgg-content-strategist.md  → Project: TGG — Copy  
03-tgg-template-generator.md  → Project: TGG — Templates
04-tgg-marketing-analyst.md   → Project: TGG — Analytics
05-tgg-repo-manager.md        → Project: TGG — Repo
```

Open the file, select all, paste into the Project's custom instructions. Done.

---

### 19. **Human** — 2026-03-18T06:19

not proojects - skills
not proojects - skills

---

### 20. **Claude** — 2026-03-18T06:20

You're right — Skills is a specific Claude.ai feature, separate from Projects.
```
This block is not supported on your current device yet.
```

Good. Now I have the full picture. The answer is: you upload a ZIP file via **Settings > Customize > Skills** in Claude.ai. The ZIP must contain the skill folder itself at the root — not just the contents.

The format is simple: a folder with a `SKILL.md` file containing YAML frontmatter and instructions.

So the five files we already built are **exactly the right format** — they just need to be packaged correctly as ZIPs. Let me do that now.
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

Five ZIPs, correctly structured. Here's how to install them.

---

## How to install

**Settings → Customize → Skills → Upload skill**

Do that five times, once per ZIP. Each skill then appears in your Skills list and can be toggled on or off per conversation.

All your skills are listed in Customize > Skills. Toggle any skill on or off using the switch next to it — disabled skills won't be available to Claude.

---

## One important thing to know

Custom Skills do not sync across surfaces — meaning these live in Claude.ai only, separate from your Claude Code skills. They're the same five skill documents, packaged differently for each environment.

Also worth knowing: Skills give Claude access to execute code, so stick to trusted sources — these are your own files so that's not a concern here, but it explains why the feature requires code execution to be enabled in Settings → Capabilities.
 You're right — Skills is a specific Claude.ai feature, separate from Projects.
Good. Now I have the full picture. The answer is: you upload a ZIP file via **Settings > Customize > Skills** in Claude.ai. The ZIP must contain the skill folder itself at the root — not just the contents.

The format is simple: a folder with a `SKILL.md` file containing YAML frontmatter and instructions.

So the five files we already built are **exactly the right format** — they just need to be packaged correctly as ZIPs. Let me do that now.
Five ZIPs, correctly structured. Here's how to install them.

---

## How to install

**Settings → Customize → Skills → Upload skill**

Do that five times, once per ZIP. Each skill then appears in your Skills list and can be toggled on or off per conversation.

All your skills are listed in Customize > Skills. Toggle any skill on or off using the switch next to it — disabled skills won't be available to Claude.

---

## One important thing to know

Custom Skills do not sync across surfaces — meaning these live in Claude.ai only, separate from your Claude Code skills. They're the same five skill documents, packaged differently for each environment.

Also worth knowing: Skills give Claude access to execute code, so stick to trusted sources — these are your own files so that's not a concern here, but it explains why the feature requires code execution to be enabled in Settings → Capabilities.

---

### 21. **Human** — 2026-03-18T06:22

malformed YAML frontmatter in SKILL.md for seo specialist
malformed YAML frontmatter in SKILL.md for seo specialist

---

### 22. **Claude** — 2026-03-18T06:23

Let me check it.
```
This block is not supported on your current device yet.
```

The colon in the description value is the problem — YAML interprets `thegoodguys.com.au). Use for any SEO task:` as a nested key. Needs quoting.
```
This block is not supported on your current device yet.
```

While I'm here, let me check the other four for the same issue — any description with a colon needs quoting too.
```
This block is not supported on your current device yet.
```

All four others are clean — no colons in their description values. Only `01` had the issue. Now repackage just that one:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Fixed. The cause was an unquoted colon mid-value in the `description` field — YAML treats anything after a colon as a new key unless the whole value is quoted. The fix was wrapping the description in double quotes. The other four were clean, so only this one ZIP needed replacing.
 Let me check it.
The colon in the description value is the problem — YAML interprets `thegoodguys.com.au). Use for any SEO task:` as a nested key. Needs quoting.
While I'm here, let me check the other four for the same issue — any description with a colon needs quoting too.
All four others are clean — no colons in their description values. Only `01` had the issue. Now repackage just that one:
Fixed. The cause was an unquoted colon mid-value in the `description` field — YAML treats anything after a colon as a new key unless the whole value is quoted. The fix was wrapping the description in double quotes. The other four were clean, so only this one ZIP needed replacing.

---

### 23. **Human** — 2026-03-18T06:24

skills are all live - check them and give me ideas how to use them or how you will auto use them when needed
skills are all live - check them and give me ideas how to use them or how you will auto use them when needed

---

### 24. **Claude** — 2026-03-18T06:25

Let me fetch the actual skills documentation to understand exactly how auto-triggering works before giving you ideas.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good. Now I have the full picture on how triggering actually works. Let me give you a straight answer.

---

## How auto-triggering works

Skills work through progressive disclosure — Claude determines which skills are relevant and loads the information it needs to complete the task, helping to prevent context window overload. When you ask Claude to complete a task, it reviews available skills, loads relevant ones, and applies their instructions.

The trigger is the **description field** in each skill's YAML frontmatter. That's the only thing Claude reads to decide whether to load a skill. It doesn't read the full skill contents until it decides to use it.

So for your five skills, here's exactly what will trigger each one automatically, and what you can also say explicitly to force it:

---

## Skill-by-skill: auto triggers and explicit prompts

### tgg-seo-specialist
**Auto-triggers on:** anything containing "SEO", "audit", "PLP", "schema", "AEO", "GEO", "internal linking", "keyword research", "metadata", "category page", "technical SEO", "robots.txt", "sitemap", "canonical", "structured data", "featured snippet"

**Example prompts that will auto-load it:**
- "Audit the robot vacuums PLP"
- "Write PLP intro for OLED TVs"
- "Generate FAQPage schema for air conditioners"
- "What keywords should we target for coffee machines?"
- "Check the heading structure on this page [paste URL or HTML]"
- "Is this page AEO-ready?"

**Explicit invoke:** "Use my TGG SEO skill to..."

---

### tgg-content-strategist
**Auto-triggers on:** "copy", "write", "draft", "PLP intro", "FAQ section", "meta description", "campaign brief", "content calendar", "brand voice", "category copy", "EAV"

**Example prompts that will auto-load it:**
- "Write the PLP intro for robot vacuums"
- "Draft FAQ questions for the washing machines category"
- "Give me meta title and description for /televisions/oled-tvs"
- "Create a content brief for Mother's Day"
- "Is this copy on-brand?" [paste copy]

**Note:** This skill and the SEO specialist overlap heavily. If you're doing both copy and technical work in one session, Claude may load both. That's fine — they're complementary.

**Explicit invoke:** "Use my TGG content strategy skill to..."

---

### tgg-template-generator
**Auto-triggers on:** "template", "brief", "scaffold", "structure", "plan", "report format", "stakeholder update", "dev request", "campaign plan"

**Example prompts that will auto-load it:**
- "Give me a copy brief template for the BFCM campaign"
- "Create an SEO audit scope for the TVs category"
- "I need a dev brief for implementing FAQPage schema"
- "Scaffold a stakeholder update for this month's organic performance"
- "Give me a campaign planning template for Mother's Day"

**Explicit invoke:** "Use my TGG template skill to..."

---

### tgg-marketing-analyst
**Auto-triggers on:** "GSC", "GA4", "Semrush", "performance", "traffic", "YoY", "MoM", "non-brand", "organic clicks", "impressions", "CTR", "ranking", "concentration risk", "BFCM", "analytics"

**Example prompts that will auto-load it:**
- "Analyse this GSC export" [paste data]
- "Why did non-brand clicks drop in November?"
- "Build a YoY performance summary for the TVs category"
- "Identify concentration risk in these rankings" [paste keywords]
- "What's the root cause of the BFCM traffic drop?"

**Explicit invoke:** "Use my TGG analytics skill to..."

---

### tgg-repo-manager
**Auto-triggers on:** "commit", "PR", "CLAUDE.md", "process file", "agent", "repo", "subagent", "YAML", "frontmatter", ".claude/"

**Example prompts that will auto-load it:**
- "Write a commit message for adding the seo-specialist agent"
- "Create a PR description for the process file updates"
- "Add a CLAUDE.md entry for the BFCM project"
- "Validate the YAML in this agent config" [paste config]
- "I need to update process file 07"

**Explicit invoke:** "Use my TGG repo skill to..."

---

## One honest caveat

If Claude isn't using a skill, verify it's toggled on, check that the skill's description field clearly explains when it should be used, and try being more explicit in your request — for example, "Use my brand guidelines skill to create a presentation."

Auto-triggering is reliable for clear task types but not guaranteed for every request. If you're doing something where the skill matters — especially copy production where the char limits are non-negotiable — it's worth adding "using my TGG copy skill" the first time in a session until you get a feel for when it fires automatically.

Skills are task-specific and only load when relevant, making them better for specialised workflows than custom instructions, which apply broadly to all conversations. The practical implication: if you want TGG rules applied to *every* conversation without thinking about it, put the core constraints (char limits, em dash rule, "The Good Guys" in S2) in your custom instructions as a fallback. The skills then layer on top with the full detail when triggered.
 Let me fetch the actual skills documentation to understand exactly how auto-triggering works before giving you ideas.
Good. Now I have the full picture on how triggering actually works. Let me give you a straight answer.

---

## How auto-triggering works

Skills work through progressive disclosure — Claude determines which skills are relevant and loads the information it needs to complete the task, helping to prevent context window overload. When you ask Claude to complete a task, it reviews available skills, loads relevant ones, and applies their instructions.

The trigger is the **description field** in each skill's YAML frontmatter. That's the only thing Claude reads to decide whether to load a skill. It doesn't read the full skill contents until it decides to use it.

So for your five skills, here's exactly what will trigger each one automatically, and what you can also say explicitly to force it:

---

## Skill-by-skill: auto triggers and explicit prompts

### tgg-seo-specialist
**Auto-triggers on:** anything containing "SEO", "audit", "PLP", "schema", "AEO", "GEO", "internal linking", "keyword research", "metadata", "category page", "technical SEO", "robots.txt", "sitemap", "canonical", "structured data", "featured snippet"

**Example prompts that will auto-load it:**
- "Audit the robot vacuums PLP"
- "Write PLP intro for OLED TVs"
- "Generate FAQPage schema for air conditioners"
- "What keywords should we target for coffee machines?"
- "Check the heading structure on this page [paste URL or HTML]"
- "Is this page AEO-ready?"

**Explicit invoke:** "Use my TGG SEO skill to..."

---

### tgg-content-strategist
**Auto-triggers on:** "copy", "write", "draft", "PLP intro", "FAQ section", "meta description", "campaign brief", "content calendar", "brand voice", "category copy", "EAV"

**Example prompts that will auto-load it:**
- "Write the PLP intro for robot vacuums"
- "Draft FAQ questions for the washing machines category"
- "Give me meta title and description for /televisions/oled-tvs"
- "Create a content brief for Mother's Day"
- "Is this copy on-brand?" [paste copy]

**Note:** This skill and the SEO specialist overlap heavily. If you're doing both copy and technical work in one session, Claude may load both. That's fine — they're complementary.

**Explicit invoke:** "Use my TGG content strategy skill to..."

---

### tgg-template-generator
**Auto-triggers on:** "template", "brief", "scaffold", "structure", "plan", "report format", "stakeholder update", "dev request", "campaign plan"

**Example prompts that will auto-load it:**
- "Give me a copy brief template for the BFCM campaign"
- "Create an SEO audit scope for the TVs category"
- "I need a dev brief for implementing FAQPage schema"
- "Scaffold a stakeholder update for this month's organic performance"
- "Give me a campaign planning template for Mother's Day"

**Explicit invoke:** "Use my TGG template skill to..."

---

### tgg-marketing-analyst
**Auto-triggers on:** "GSC", "GA4", "Semrush", "performance", "traffic", "YoY", "MoM", "non-brand", "organic clicks", "impressions", "CTR", "ranking", "concentration risk", "BFCM", "analytics"

**Example prompts that will auto-load it:**
- "Analyse this GSC export" [paste data]
- "Why did non-brand clicks drop in November?"
- "Build a YoY performance summary for the TVs category"
- "Identify concentration risk in these rankings" [paste keywords]
- "What's the root cause of the BFCM traffic drop?"

**Explicit invoke:** "Use my TGG analytics skill to..."

---

### tgg-repo-manager
**Auto-triggers on:** "commit", "PR", "CLAUDE.md", "process file", "agent", "repo", "subagent", "YAML", "frontmatter", ".claude/"

**Example prompts that will auto-load it:**
- "Write a commit message for adding the seo-specialist agent"
- "Create a PR description for the process file updates"
- "Add a CLAUDE.md entry for the BFCM project"
- "Validate the YAML in this agent config" [paste config]
- "I need to update process file 07"

**Explicit invoke:** "Use my TGG repo skill to..."

---

## One honest caveat

If Claude isn't using a skill, verify it's toggled on, check that the skill's description field clearly explains when it should be used, and try being more explicit in your request — for example, "Use my brand guidelines skill to create a presentation."

Auto-triggering is reliable for clear task types but not guaranteed for every request. If you're doing something where the skill matters — especially copy production where the char limits are non-negotiable — it's worth adding "using my TGG copy skill" the first time in a session until you get a feel for when it fires automatically.

Skills are task-specific and only load when relevant, making them better for specialised workflows than custom instructions, which apply broadly to all conversations. The practical implication: if you want TGG rules applied to *every* conversation without thinking about it, put the core constraints (char limits, em dash rule, "The Good Guys" in S2) in your custom instructions as a fallback. The skills then layer on top with the full detail when triggered.

---

### 25. **Human** — 2026-03-18T06:30

memorise to state when using a skill, and also let me know hwo to maintain teh skills if things change
memorise to state when using a skill, and also let me know hwo to maintain teh skills if things change

---

### 26. **Claude** — 2026-03-18T06:30

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

At 30 entries I'm at the limit. I need to consolidate before adding. Let me tighten a few entries to free a slot.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Saved. Now on skill maintenance:

---

## How to maintain the skills when things change

### The update workflow

**Step 1 — Edit the source `.md` file** on your Mac. The files from earlier are your source of truth:

```
01-tgg-seo-specialist.md
02-tgg-content-strategist.md
03-tgg-template-generator.md
04-tgg-marketing-analyst.md
05-tgg-repo-manager.md
```

Keep these somewhere permanent — a folder in your repo, iCloud, or Notion export. Treat them as the master copies.

**Step 2 — Repackage as a ZIP.** The structure must be correct (folder at root, not bare file):

```bash
# Example for the SEO skill
mkdir -p tgg-seo-specialist
cp 01-tgg-seo-specialist.md tgg-seo-specialist/SKILL.md
zip -r tgg-seo-specialist.zip tgg-seo-specialist/
```

**Step 3 — Re-upload in Claude.ai.** Go to Customize > Skills, delete the old version, upload the new ZIP.

---

### What triggers an update

| Change | Which skill | What to update |
|--------|------------|----------------|
| PLP char limits change | seo-specialist, content-strategist | Update the limit in both |
| EAV field confirmed same/different as PLP | seo-specialist, content-strategist | Resolve the open question, remove the caveat |
| New banned words for brand PLPs | seo-specialist, content-strategist | Add to the banned words list |
| BFCM strategy changes (e.g. dedicated URLs reinstated) | seo-specialist, marketing-analyst | Update competitor context and BFCM baselines |
| New seasonal campaign pattern | content-strategist, template-generator | Add to seasonal calendar section |
| GSC/GA4 new baseline metrics | marketing-analyst | Update the known performance context section |
| New process file added (10+) | template-generator, repo-manager | Add the new file number and scope |
| Commit conventions change | repo-manager | Update the commit format section |
| New subagent added to .claude/ | repo-manager | Add to the directory structure reference |

---

### The YAML frontmatter trap

Every time you edit and re-save, double-check the description field. If it contains a colon (which yours did), it must be quoted:

```yaml
# Will break
description: Use for: SEO tasks

# Correct
description: "Use for: SEO tasks"
```

Run a quick sanity check before re-zipping:

```bash
# Verify YAML parses cleanly (requires python3)
python3 -c "
import yaml, sys
with open('tgg-seo-specialist/SKILL.md') as f:
    content = f.read()
front = content.split('---')[1]
yaml.safe_load(front)
print('YAML OK')
"
```

---

### Lightweight alternative: ask Claude to update it

If you don't want to edit the file manually, paste the relevant section into a chat and say "update the PLP char limit in my content-strategist skill from X to Y, then give me the updated file to download." I'll make the change, you download it, repackage, re-upload. Takes two minutes.
 
At 30 entries I'm at the limit. I need to consolidate before adding. Let me tighten a few entries to free a slot.
Saved. Now on skill maintenance:

---

## How to maintain the skills when things change

### The update workflow

**Step 1 — Edit the source `.md` file** on your Mac. The files from earlier are your source of truth:

```
01-tgg-seo-specialist.md
02-tgg-content-strategist.md
03-tgg-template-generator.md
04-tgg-marketing-analyst.md
05-tgg-repo-manager.md
```

Keep these somewhere permanent — a folder in your repo, iCloud, or Notion export. Treat them as the master copies.

**Step 2 — Repackage as a ZIP.** The structure must be correct (folder at root, not bare file):

```bash
# Example for the SEO skill
mkdir -p tgg-seo-specialist
cp 01-tgg-seo-specialist.md tgg-seo-specialist/SKILL.md
zip -r tgg-seo-specialist.zip tgg-seo-specialist/
```

**Step 3 — Re-upload in Claude.ai.** Go to Customize > Skills, delete the old version, upload the new ZIP.

---

### What triggers an update

| Change | Which skill | What to update |
|--------|------------|----------------|
| PLP char limits change | seo-specialist, content-strategist | Update the limit in both |
| EAV field confirmed same/different as PLP | seo-specialist, content-strategist | Resolve the open question, remove the caveat |
| New banned words for brand PLPs | seo-specialist, content-strategist | Add to the banned words list |
| BFCM strategy changes (e.g. dedicated URLs reinstated) | seo-specialist, marketing-analyst | Update competitor context and BFCM baselines |
| New seasonal campaign pattern | content-strategist, template-generator | Add to seasonal calendar section |
| GSC/GA4 new baseline metrics | marketing-analyst | Update the known performance context section |
| New process file added (10+) | template-generator, repo-manager | Add the new file number and scope |
| Commit conventions change | repo-manager | Update the commit format section |
| New subagent added to .claude/ | repo-manager | Add to the directory structure reference |

---

### The YAML frontmatter trap

Every time you edit and re-save, double-check the description field. If it contains a colon (which yours did), it must be quoted:

```yaml
# Will break
description: Use for: SEO tasks

# Correct
description: "Use for: SEO tasks"
```

Run a quick sanity check before re-zipping:

```bash
# Verify YAML parses cleanly (requires python3)
python3 -c "
import yaml, sys
with open('tgg-seo-specialist/SKILL.md') as f:
    content = f.read()
front = content.split('---')[1]
yaml.safe_load(front)
print('YAML OK')
"
```

---

### Lightweight alternative: ask Claude to update it

If you don't want to edit the file manually, paste the relevant section into a chat and say "update the PLP char limit in my content-strategist skill from X to Y, then give me the updated file to download." I'll make the change, you download it, repackage, re-upload. Takes two minutes.

---

### 27. **Human** — 2026-03-18T06:33

memorise this and update or ask for permission to update whenever you need
memorise this and update or ask for permission to update whenever you need

---

### 28. **Claude** — 2026-03-18T06:33

The instruction is already saved as memory #30. But you want it strengthened — currently it just says "state which skill was used." You want me to also update skills proactively or ask permission when something changes.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done. Here's exactly how it will work in practice:

**Clear, unambiguous change** — e.g. "the PLP char limit is now 225–255" — I'll update the relevant skill files immediately and offer the new ZIPs to download without asking first.

**Ambiguous or potentially permanent change** — e.g. we work through a one-off exception to a rule, or you mention something that might be a project-specific constraint rather than a global rule change — I'll flag it and ask whether it should be baked into the skill permanently before touching anything.
 The instruction is already saved as memory #30. But you want it strengthened — currently it just says "state which skill was used." You want me to also update skills proactively or ask permission when something changes.
Done. Here's exactly how it will work in practice:

**Clear, unambiguous change** — e.g. "the PLP char limit is now 225–255" — I'll update the relevant skill files immediately and offer the new ZIPs to download without asking first.

**Ambiguous or potentially permanent change** — e.g. we work through a one-off exception to a rule, or you mention something that might be a project-specific constraint rather than a global rule change — I'll flag it and ask whether it should be baked into the skill permanently before touching anything.
