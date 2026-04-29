---
title: Building a custom skill together (full)
parent: Chat/Light/2026-03-19-building-a-custom-skill-together-088735
uuid: 088735c4-4633-4f3a-8501-e70db18419cd
---

#chat/full #project/main #status/completed

# Building a custom skill together — Full Transcript

→ Light view: [[Chat/Light/2026-03-19-building-a-custom-skill-together-088735]]
→ Medium view: [[Chat/Medium/2026-03-19-building-a-custom-skill-together-088735]]

**Messages:** 14 | **Date:** 2026-03-19

---

### 1. **Human** — 2026-03-19T01:55

Let's create a skill together using your skill-creator skill. First ask me what the skill should do.
Let's create a skill together using your skill-creator skill. First ask me what the skill should do.

---

### 2. **Claude** — 2026-03-19T01:55

```
This block is not supported on your current device yet.
```

Skill Creator loaded. What should this skill do? Describe the task, workflow, or type of output you want it to handle, and we'll shape it from there.
Skill Creator loaded. What should this skill do? Describe the task, workflow, or type of output you want it to handle, and we'll shape it from there.

---

### 3. **Human** — 2026-03-19T01:57

I want a skill that knows how to leverage all my connectors + chrome extension to do tasks, and when a task seems like it could benefit from a connector or chrome workflow
I want a skill that knows how to leverage all my connectors + chrome extension to do tasks, and when a task seems like it could benefit from a connector or chrome workflow

---

### 4. **Claude** — 2026-03-19T01:57

Great starting point. A few questions to nail down the scope before drafting anything:
```
This block is not supported on your current device yet.
```

What should this skill do, and when should it kick in? Answer whatever you can and we'll go from there.
 Great starting point. A few questions to nail down the scope before drafting anything:
What should this skill do, and when should it kick in? Answer whatever you can and we'll go from there.

---

### 5. **Human** — 2026-03-19T02:00

Q: Which connectors do you want the skill to know about? (Select all that apply)
A: all

Q: What kinds of tasks should trigger this skill? (Select all that apply)
A: all

Q: How opinionated should the skill be?
A: Proactively suggest the right tool
Q: Which connectors do you want the skill to know about? (Select all that apply)
A: all

Q: What kinds of tasks should trigger this skill? (Select all that apply)
A: all

Q: How opinionated should the skill be?
A: Proactively suggest the right tool

---

### 6. **Claude** — 2026-03-19T02:01

Good. A couple more things before I draft:
```
This block is not supported on your current device yet.
```


 Good. A couple more things before I draft:

---

### 7. **Human** — 2026-03-19T02:03

Q: What does your Chrome Extension actually do?
A: its claude chrome extension, it can take over

Q: Should the skill know TGG-specific context (e.g. that Semrush = AU database, Airtable = SEO records)?
A: Yes — bake in TGG context
Q: What does your Chrome Extension actually do?
A: its claude chrome extension, it can take over

Q: Should the skill know TGG-specific context (e.g. that Semrush = AU database, Airtable = SEO records)?
A: Yes — bake in TGG context

---

### 8. **Claude** — 2026-03-19T02:03

Got it. So the Chrome Extension is Claude in Chrome, meaning it can browse, interact with pages, and execute browser-based workflows directly. That's a meaningful capability to route tasks toward.

One last question before drafting:
```
This block is not supported on your current device yet.
```


 Got it. So the Chrome Extension is Claude in Chrome, meaning it can browse, interact with pages, and execute browser-based workflows directly. That's a meaningful capability to route tasks toward.

One last question before drafting:

---

### 9. **Human** — 2026-03-19T02:06

Q: Which of these are realistic tasks you'd want this skill to help route correctly? (Select all that apply)
A: anything i mightr need, all of those and more - use claudes skillsets where it aligns "like scrape live page" and only patch gaps with the connectors
Q: Which of these are realistic tasks you'd want this skill to help route correctly? (Select all that apply)
A: anything i mightr need, all of those and more - use claudes skillsets where it aligns "like scrape live page" and only patch gaps with the connectors

---

### 10. **Claude** — 2026-03-19T02:07

Perfect. Clear mental model: Claude's native capabilities (web fetch, search, code execution) are the first resort. Connectors and Chrome fill the gaps where Claude can't reach directly. The skill's job is to know which tool closes which gap, and proactively say so.

Drafting now.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Draft is done. Here's what it covers:

**Core logic.** A four-step routing decision tree: native first, then Semrush MCP, then Airtable/Drive, then Chrome. Hybrid tasks get a stated plan before execution.

**Per-connector docs.** Each tool has a "when to use", TGG-specific notes, and gotchas (e.g. always `database: 'au'` for Semrush, always `tool_search` before calling MCP tools since parameter schemas vary).

**Chrome handoff protocol.** Rather than just saying "use Chrome," the skill requires a numbered step-by-step brief with starting URL, actions, and expected output. That's what makes Chrome delegation actually work.

**Routing table.** Ten concrete examples mapping task types to tools, so the skill can pattern-match quickly.

**TGG context baked in.** Competitors, categories, campaign count, active infrastructure.

Before I package this, want to do a quick sanity check? Give me one or two real tasks you'd actually throw at this, and I'll run through them using the skill to see if the routing feels right.
 Perfect. Clear mental model: Claude's native capabilities (web fetch, search, code execution) are the first resort. Connectors and Chrome fill the gaps where Claude can't reach directly. The skill's job is to know which tool closes which gap, and proactively say so.

Drafting now.
Draft is done. Here's what it covers:

**Core logic.** A four-step routing decision tree: native first, then Semrush MCP, then Airtable/Drive, then Chrome. Hybrid tasks get a stated plan before execution.

**Per-connector docs.** Each tool has a "when to use", TGG-specific notes, and gotchas (e.g. always `database: 'au'` for Semrush, always `tool_search` before calling MCP tools since parameter schemas vary).

**Chrome handoff protocol.** Rather than just saying "use Chrome," the skill requires a numbered step-by-step brief with starting URL, actions, and expected output. That's what makes Chrome delegation actually work.

**Routing table.** Ten concrete examples mapping task types to tools, so the skill can pattern-match quickly.

**TGG context baked in.** Competitors, categories, campaign count, active infrastructure.

Before I package this, want to do a quick sanity check? Give me one or two real tasks you'd actually throw at this, and I'll run through them using the skill to see if the routing feels right.

---

### 11. **Human** — 2026-03-19T02:20

based on our history together, what tools and tasks do i frequent
based on our history together, what tools and tasks do i frequent

---

### 12. **Claude** — 2026-03-19T02:20

```
This block is not supported on your current device yet.
```

Here's the pattern from the last 20 conversations:

**Native Claude (daily use)**
`web_fetch` is your most-reached tool. Live page audits, competitor sitemap checks, page content reviews, and URL validation all go through it. `bash_tool` runs close behind for Python scripts, CSV processing, and curl-based URL checks.

**Semrush MCP (regular)**
Primarily for keyword research to inform copy rewrites (Easter sale, LG TVs, PLP batches), and domain/URL-level organic data pulls. Always AU database. You tend to use it in conjunction with a copy task rather than as a standalone research session.

**Google Drive (occasional)**
Referenced in workflow but not heavily used in recent chats. More relevant to the BFCM deck and process doc work than day-to-day tasks.

**Airtable (recent, exploratory)**
Just set up a PLP Copy Tracker table. Still early. The potential is clearly there for copy status tracking and keyword list management.

**Claude in Chrome (indirect)**
Your Semrush CSV export automation (the `semrush_csv_merger.py` / 41-campaign consolidation) is the clearest Chrome-appropriate workflow. You haven't been explicitly routing to it in chat because that work runs in Claude Code, but it's the right fit for any Semrush UI action the MCP can't reach.

**Skills (constant)**
`tgg-copywriting`, `tgg-seo-specialist`, and `skill-creator` are your most-loaded skills. Most sessions start by loading one or more of these.

---

This gives me a solid basis to add a few things to the skill draft. Want me to update it with this routing frequency context, plus add a note that the Chrome extension is the correct path for the Semrush 41-campaign export workflow specifically?
Here's the pattern from the last 20 conversations:

**Native Claude (daily use)**
`web_fetch` is your most-reached tool. Live page audits, competitor sitemap checks, page content reviews, and URL validation all go through it. `bash_tool` runs close behind for Python scripts, CSV processing, and curl-based URL checks.

**Semrush MCP (regular)**
Primarily for keyword research to inform copy rewrites (Easter sale, LG TVs, PLP batches), and domain/URL-level organic data pulls. Always AU database. You tend to use it in conjunction with a copy task rather than as a standalone research session.

**Google Drive (occasional)**
Referenced in workflow but not heavily used in recent chats. More relevant to the BFCM deck and process doc work than day-to-day tasks.

**Airtable (recent, exploratory)**
Just set up a PLP Copy Tracker table. Still early. The potential is clearly there for copy status tracking and keyword list management.

**Claude in Chrome (indirect)**
Your Semrush CSV export automation (the `semrush_csv_merger.py` / 41-campaign consolidation) is the clearest Chrome-appropriate workflow. You haven't been explicitly routing to it in chat because that work runs in Claude Code, but it's the right fit for any Semrush UI action the MCP can't reach.

**Skills (constant)**
`tgg-copywriting`, `tgg-seo-specialist`, and `skill-creator` are your most-loaded skills. Most sessions start by loading one or more of these.

---

This gives me a solid basis to add a few things to the skill draft. Want me to update it with this routing frequency context, plus add a note that the Chrome extension is the correct path for the Semrush 41-campaign export workflow specifically?

---

### 13. **Human** — 2026-03-19T02:21

you arent to lock specific tasks you are to see if any of them can be enhanced with skills and connectors- the chrome extension is helpful as it circumvents mcps and apis
you arent to lock specific tasks you are to see if any of them can be enhanced with skills and connectors- the chrome extension is helpful as it circumvents mcps and apis

---

### 14. **Claude** — 2026-03-19T02:23

Good clarification. The skill's job isn't to map known tasks to fixed tools. it's to look at whatever's in front of it and ask "could a connector or Chrome make this better or possible?" Chrome in particular is the escape hatch when MCP/API can't reach something.

Let me revise the draft to reflect that framing.
```
This block is not supported on your current device yet.
```

The key shift in this version:

The skill no longer maps tasks to tools. It runs a silent enhancement check on whatever's already happening and asks whether a connector would make the output meaningfully better. Chrome is framed correctly. it's the escape hatch for anything MCP or API can't touch, because it operates a real authenticated browser directly.

The surfacing language is deliberately lightweight. One inline question, not an interruption. "Semrush MCP could add keyword volume here — worth pulling?" That's it.

Want to package this now, or run a couple of real tasks through it first to test how the enhancement check fires in practice?
 Good clarification. The skill's job isn't to map known tasks to fixed tools. it's to look at whatever's in front of it and ask "could a connector or Chrome make this better or possible?" Chrome in particular is the escape hatch when MCP/API can't reach something.

Let me revise the draft to reflect that framing.
The key shift in this version:

The skill no longer maps tasks to tools. It runs a silent enhancement check on whatever's already happening and asks whether a connector would make the output meaningfully better. Chrome is framed correctly. it's the escape hatch for anything MCP or API can't touch, because it operates a real authenticated browser directly.

The surfacing language is deliberately lightweight. One inline question, not an interruption. "Semrush MCP could add keyword volume here — worth pulling?" That's it.

Want to package this now, or run a couple of real tasks through it first to test how the enhancement check fires in practice?
