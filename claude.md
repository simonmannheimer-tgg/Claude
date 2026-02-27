# Claude Code — Personal Workflow

## How I Work

### 1. Think Before Acting
- For anything beyond a quick question, outline a plan before diving in
- If a task has multiple parts, write them out in `tasks/todo.md` first
- When something isn't working or doesn't make sense, pause and reassess — don't just push through

### 2. Remember and Build On What We've Done
- Treat `tasks/lessons.md` as a living document — update it whenever we learn something useful together
- At the start of each session, check for relevant context from past work
- If I correct something or clarify a preference, capture that pattern so it sticks
- Reference previous projects and decisions rather than starting from scratch

### 3. Use Subagents for Heavy Lifting
- Offload research, comparisons, and deep dives to subagents to keep the main conversation focused
- Use parallel subagents when exploring multiple options
- One clear objective per subagent

### 4. Confirm Before Committing
- For anything that changes files, sends information, or takes significant action — check in first
- Show a summary of what's about to happen before doing it
- For routine or repeated tasks where we've already aligned, just get it done

### 5. Keep Things Simple and Practical
- Default to the most straightforward approach
- Avoid overcomplicating processes — if a simple list works, don't build a system
- Match the effort to the task: quick answers for quick questions, thorough work for thorough requests

---

## Task Management

1. **Plan**: Write out steps in `tasks/todo.md` with checkable items
2. **Check In**: Confirm the approach before starting on bigger tasks
3. **Track Progress**: Mark items complete as they're finished
4. **Summarise**: Give a clear, brief recap of what was done at each step
5. **Document**: Add outcomes and notes to `tasks/todo.md` when wrapping up
6. **Learn**: Update `tasks/lessons.md` after any corrections or new preferences

---

## Long-Running Projects

- Maintain a `projects/` folder for anything ongoing
- Each project gets its own folder with a `README.md` covering: purpose, current status, key decisions, and next steps
- When returning to a project, read the README first to pick up where we left off
- Archive completed projects rather than deleting them — past context is valuable

---

## SEO Process Management

### Process Files
All SEO processes live in `processes/` as numbered markdown files. Each is self-contained but may reference others.

**Always read `00-tov-language-reference.md` before any content-writing task.** It contains the master banned word list, overuse warnings, and tone rules that apply across all processes.

| # | Process | File |
|---|---------|------|
| 00 | TOV & Language Reference | `processes/00-tov-language-reference.md` |
| 01 | PLP Intro Copy (2-Sentence) | `processes/01-plp-intro-copy.md` |
| 02 | Metadata Generation | `processes/02-metadata-generation.md` |
| 03 | Inlink Migration (Top→Bottom) | `processes/03-inlink-migration.md` |
| 04 | Content Analysis | `processes/04-content-analysis.md` |
| 05 | FAQ & Category Copy | `processes/05-faq-category-copy.md` |
| 06 | Internal Linking | `processes/06-internal-linking.md` |
| 07 | AEO Optimisation | `processes/07-aeo-optimisation.md` |
| 08 | EAV Mapping | `processes/08-eav-mapping.md` |
| 09 | AI Visibility Polling | `processes/09-ai-visibility-polling.md` |

### How to Use Processes
- When a task maps to a process, **read the process file first** before executing
- For any content writing: read `00` first, then the specific process
- Follow the rules, QA checklist, and output format specified in the file
- If a task spans multiple processes, follow the workflow chain

### Standard Workflows

**Workflow A — Category Page Optimisation:**
`08 (EAV)` → `04 (Core Query + Fanout)` → `06 (Link Validation)` → `05 (Brand+Category FAQ)`

**Workflow B — Article AEO Audit:**
`04 (Summarise + Keyword)` → `06 (Link Opportunities)` → `07 (AEO Suggestions + Finalise)`

**Workflow C — Internal Linking:**
`06 (Find → Validate → Verify → Insert)`

**Workflow D — Full Category Page Build:**
`08 (EAV)` → `04 (Fanout)` → `01 (PLP Intro)` → `05 (FAQ Copy)` → `02 (Metadata)` → `06 (Linking)`

### Updating Processes
- When Simon changes a rule or preference, update the relevant process file immediately
- Add a changelog note at the top (version + date + what changed)
- **Contradiction handling:** If a request conflicts with an existing process rule, flag it and ask:
  - "This conflicts with [process file, specific rule]. Is this a one-time exception or a permanent change?"
  - If permanent: update the process file
  - If one-time: proceed but don't change the file

---

## Writing Philosophy (Applies to All Content)

- **Guardrails, not templates.** Ban harmful patterns; don't prescribe "allowed" patterns.
- **Vary everything.** Sentence openers, TGG placement, benefit angles, structure. If a batch of 20 intros reads like they came from the same fill-in-the-blank template, rewrite.
- **Be specific.** Name brands, name features, name use cases. Specificity is what makes copy useful to humans and citable by AI.
- **Sound human.** If it reads like a chatbot or a keyword list disguised as prose, rewrite.

---

## Core Principles

- **Context is king**: Always check what we already know before asking or assuming
- **Preferences stick**: Once a preference is established, apply it consistently going forward
- **Clarity over cleverness**: Plain language, clear structure, no unnecessary complexity
- **Respect my time**: Get to the point, do the work, flag only what genuinely needs my input
- **Processes evolve**: These files are living documents — update them, don't let them go stale
