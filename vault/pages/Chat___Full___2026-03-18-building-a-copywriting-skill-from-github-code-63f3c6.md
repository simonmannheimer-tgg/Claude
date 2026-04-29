---
title: Building a copywriting skill from GitHub code (full)
parent: Chat/Light/2026-03-18-building-a-copywriting-skill-from-github-code-63f3c6
uuid: 63f3c699-be20-4241-9b4e-ec7a94d34c97
---

#chat/full #project/skills-built-full-set #status/completed

# Building a copywriting skill from GitHub code — Full Transcript

→ Light view: [[Chat/Light/2026-03-18-building-a-copywriting-skill-from-github-code-63f3c6]]
→ Medium view: [[Chat/Medium/2026-03-18-building-a-copywriting-skill-from-github-code-63f3c6]]

**Messages:** 18 | **Date:** 2026-03-18

---

### 1. **Human** — 2026-03-18T03:10

help me build a skill - i will provide you the github repo of my claude code - not everything there is relevant, I want a copywriting skill that can assess my requirements and adjust.
help me build a skill - i will provide you the github repo of my claude code - not everything there is relevant, I want a copywriting skill that can assess my requirements and adjust.

---

### 2. **Claude** — 2026-03-18T03:10

I'll start by reading the skill-creator skill to understand the best practices for building a new skill.
```
This block is not supported on your current device yet.
```

Let me also read the truncated section:
```
This block is not supported on your current device yet.
```

Good, I've got the full picture. Now let me look at the existing skills structure for reference:
```
This block is not supported on your current device yet.
```

Good. Now I have a solid understanding of the skill framework. Go ahead and share the GitHub repo URL for your Claude Code setup, Simon. I'll fetch it and pull out everything relevant to your copywriting workflows, then we can shape the skill together.

A few things I want to nail down as we go through your repo:

**What the skill should cover.** Based on what I already know about your work, I'm guessing this spans PLP intros, metadata (title/description), FAQ copy, category descriptions, and possibly EAV descriptions. But let me know if the scope is narrower or broader than that.

**How it should "assess and adjust."** I'm thinking the skill reads the relevant process file (01–09), identifies which content type is being requested, then applies the right constraints (char limits, banned words, structural rules) automatically. Is that the right mental model, or do you mean something different by "assess my requirements"?

Share the repo link and I'll dig in.


I'll start by reading the skill-creator skill to understand the best practices for building a new skill.
Let me also read the truncated section:
Good, I've got the full picture. Now let me look at the existing skills structure for reference:
Good. Now I have a solid understanding of the skill framework. Go ahead and share the GitHub repo URL for your Claude Code setup, Simon. I'll fetch it and pull out everything relevant to your copywriting workflows, then we can shape the skill together.

A few things I want to nail down as we go through your repo:

**What the skill should cover.** Based on what I already know about your work, I'm guessing this spans PLP intros, metadata (title/description), FAQ copy, category descriptions, and possibly EAV descriptions. But let me know if the scope is narrower or broader than that.

**How it should "assess and adjust."** I'm thinking the skill reads the relevant process file (01–09), identifies which content type is being requested, then applies the right constraints (char limits, banned words, structural rules) automatically. Is that the right mental model, or do you mean something different by "assess my requirements"?

Share the repo link and I'll dig in.

---

### 3. **Human** — 2026-03-18T03:11



---

### 4. **Claude** — 2026-03-18T03:11

I've now gone through the full repo. The relevant material for the copywriting skill is concentrated in files `00` through `09` (the SEO process files), `CLAUDE.md`/`claude.md` (workflow philosophy), and `PROMPT_AUDIT.md` (design decisions and contradiction resolutions). Everything else — GTMetrix, Context Mode, the shopping scraper — is infrastructure, not copywriting.

Here's my read on what this skill needs to do and a few questions before I draft it.

**What I'm seeing:** You have a mature, well-structured process system (00–09) that already works in Claude Code with the `ctx_read_file` → process file → execute pattern. The skill for claude.ai needs to package that same intelligence into something that triggers correctly and applies the right rules without the Claude Code scaffolding (no `ctx_read_file`, no `processes/` folder on disk).

**What I think the skill should do:**

1. **Detect content type from the request** — PLP intro, metadata, FAQ copy, brand+category FAQ, extended PLP intro, EAV mapping, inlink migration, or a combination.
2. **Load the right constraints automatically** — char/word limits, banned words, page type classification, structural rules, QA checklist.
3. **Apply TOV (00) as a base layer** across all content types — hard bans, overuse warnings, Australian English, phrasing principles.
4. **Handle batch variation** — when writing multiple pieces, enforce cross-piece diversity (openers, TGG placement, benefit angles).
5. **Self-QA against the checklist** before presenting output.

Before I write the draft, a few things to confirm:
```
This block is not supported on your current device yet.
```

These answers will shape whether I build a lean single-file skill or a modular system with bundled references. Take your pick and I'll draft it.
 I've now gone through the full repo. The relevant material for the copywriting skill is concentrated in files `00` through `09` (the SEO process files), `CLAUDE.md`/`claude.md` (workflow philosophy), and `PROMPT_AUDIT.md` (design decisions and contradiction resolutions). Everything else — GTMetrix, Context Mode, the shopping scraper — is infrastructure, not copywriting.

Here's my read on what this skill needs to do and a few questions before I draft it.

**What I'm seeing:** You have a mature, well-structured process system (00–09) that already works in Claude Code with the `ctx_read_file` → process file → execute pattern. The skill for claude.ai needs to package that same intelligence into something that triggers correctly and applies the right rules without the Claude Code scaffolding (no `ctx_read_file`, no `processes/` folder on disk).

**What I think the skill should do:**

1. **Detect content type from the request** — PLP intro, metadata, FAQ copy, brand+category FAQ, extended PLP intro, EAV mapping, inlink migration, or a combination.
2. **Load the right constraints automatically** — char/word limits, banned words, page type classification, structural rules, QA checklist.
3. **Apply TOV (00) as a base layer** across all content types — hard bans, overuse warnings, Australian English, phrasing principles.
4. **Handle batch variation** — when writing multiple pieces, enforce cross-piece diversity (openers, TGG placement, benefit angles).
5. **Self-QA against the checklist** before presenting output.

Before I write the draft, a few things to confirm:
These answers will shape whether I build a lean single-file skill or a modular system with bundled references. Take your pick and I'll draft it.

---

### 5. **Human** — 2026-03-18T03:12

Q: Which content types should this skill cover? (Select all that apply)
A: All writing processes (01, 02, 03, 05, 08)

Q: Should the skill include the full process rules inline (bigger file, self-contained), or reference separate bundled files (modular, mirrors your Claude Code setup)?
A: Modular (SKILL.md + references/ folder)

Q: Should the skill handle batch mode (e.g. 'write PLP intros for these 20 URLs') with cross-batch variation enforcement?
A: Yes, batch mode is critical
Q: Which content types should this skill cover? (Select all that apply)
A: All writing processes (01, 02, 03, 05, 08)

Q: Should the skill include the full process rules inline (bigger file, self-contained), or reference separate bundled files (modular, mirrors your Claude Code setup)?
A: Modular (SKILL.md + references/ folder)

Q: Should the skill handle batch mode (e.g. 'write PLP intros for these 20 URLs') with cross-batch variation enforcement?
A: Yes, batch mode is critical

---

### 6. **Claude** — 2026-03-18T03:17

Good. All writing processes, modular structure, batch mode critical. Let me build this out.

I'll create the full skill directory with SKILL.md as the router/orchestrator and individual reference files for each process. Let me start by reading the frontend-design skill and an existing modular skill for structural patterns.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good pattern. Now let me build the full skill. I'll create the directory structure, SKILL.md as the orchestrator, and individual reference files for each process.
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

Now let me verify the full structure and package it:
```
This block is not supported on your current device yet.
```

Good structure. Let me also check line counts to make sure SKILL.md stays under the 500-line guidance:
```
This block is not supported on your current device yet.
```

SKILL.md at 134 lines, well within limits. Now let me package it and run a quick sanity test by executing the skill myself on a sample prompt.
```
This block is not supported on your current device yet.
```

Now let me do a quick self-test: I'll follow the skill's own instructions to write a PLP intro, verifying the routing and QA flow works.
```
This block is not supported on your current device yet.
```

Good. Let me now verify the skill works end-to-end by simulating a test case — I'll write 3 PLP intros following the skill's own workflow.

**Test prompt:** "Write PLP intros for: /televisions, /samsung/fridges, /deals/black-friday-vacuums"

Step 1 — Content type: PLP Intro → load `01-plp-intros.md`
Step 3 — Page types: /televisions = Type A, /samsung/fridges = Type C, /deals/black-friday-vacuums = Type D

Let me write and QA:
```
This block is not supported on your current device yet.
```

The self-QA correctly caught the char-count shortfalls and the TGG placement repetition. The routing logic works. Let me now package the final skill file.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Description is 30 chars over the 1024 limit. Let me tighten it:
```
This block is not supported on your current device yet.
```




Good. All writing processes, modular structure, batch mode critical. Let me build this out.

I'll create the full skill directory with SKILL.md as the router/orchestrator and individual reference files for each process. Let me start by reading the frontend-design skill and an existing modular skill for structural patterns.
Good pattern. Now let me build the full skill. I'll create the directory structure, SKILL.md as the orchestrator, and individual reference files for each process.
Now let me verify the full structure and package it:
Good structure. Let me also check line counts to make sure SKILL.md stays under the 500-line guidance:
SKILL.md at 134 lines, well within limits. Now let me package it and run a quick sanity test by executing the skill myself on a sample prompt.
Now let me do a quick self-test: I'll follow the skill's own instructions to write a PLP intro, verifying the routing and QA flow works.
Good. Let me now verify the skill works end-to-end by simulating a test case — I'll write 3 PLP intros following the skill's own workflow.

**Test prompt:** "Write PLP intros for: /televisions, /samsung/fridges, /deals/black-friday-vacuums"

Step 1 — Content type: PLP Intro → load `01-plp-intros.md`
Step 3 — Page types: /televisions = Type A, /samsung/fridges = Type C, /deals/black-friday-vacuums = Type D

Let me write and QA:
The self-QA correctly caught the char-count shortfalls and the TGG placement repetition. The routing logic works. Let me now package the final skill file.
Description is 30 chars over the 1024 limit. Let me tighten it:

---

### 7. **Human** — 2026-03-18T03:39

Continue
Continue

---

### 8. **Claude** — 2026-03-18T03:39

```
This block is not supported on your current device yet.
```

Read-only filesystem. Let me copy the skill and package from a writable location:
```
This block is not supported on your current device yet.
```

Packaged successfully. Let me copy everything to outputs:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's what you've got:

**`tgg-copywriting.skill`** — the installable package. Drop it into Claude Code or Claude.ai.

**Structure:**

- **SKILL.md** (134 lines) — the orchestrator. Routes requests to the right content type, enforces the 6-step workflow (identify → load references → classify page → write → batch-check → self-QA), and handles batch variation enforcement.
- **references/00-tov.md** — hard bans, overuse warnings, Australian English, phrasing principles. Loaded as a base layer for every task.
- **references/01-plp-intros.md** — 2-sentence PLP intros (230–260 chars), page type rules, sentence structure, batch output table format.
- **references/02-metadata.md** — meta titles (≤60 chars) and descriptions (140–155 chars), CTA rules, prohibited words, CSV batch format.
- **references/03-inlink-migration.md** — top-to-bottom HTML rewrites with Slate/CSS class preservation and link integrity rules.
- **references/05-faq-category-copy.md** — FAQ generation (5A), brand+category FAQ 150–250 words (5B), extended PLP intro 230–260 words (5C).
- **references/08-eav-descriptions.md** — entity-attribute-value category research.

**Self-test results:** I ran the skill against a 3-URL PLP intro batch. The QA step correctly caught two pieces under 230 chars and flagged all three ending with identical TGG placement. The routing, reference loading, and cross-batch variation check all function as intended.

**What to try first:** Give it a real batch of 5–10 PLP URLs and see if the variation enforcement catches patterns you'd normally have to flag manually. That's where the batch logic earns its keep.
Read-only filesystem. Let me copy the skill and package from a writable location:
Packaged successfully. Let me copy everything to outputs:
Here's what you've got:

**`tgg-copywriting.skill`** — the installable package. Drop it into Claude Code or Claude.ai.

**Structure:**

- **SKILL.md** (134 lines) — the orchestrator. Routes requests to the right content type, enforces the 6-step workflow (identify → load references → classify page → write → batch-check → self-QA), and handles batch variation enforcement.
- **references/00-tov.md** — hard bans, overuse warnings, Australian English, phrasing principles. Loaded as a base layer for every task.
- **references/01-plp-intros.md** — 2-sentence PLP intros (230–260 chars), page type rules, sentence structure, batch output table format.
- **references/02-metadata.md** — meta titles (≤60 chars) and descriptions (140–155 chars), CTA rules, prohibited words, CSV batch format.
- **references/03-inlink-migration.md** — top-to-bottom HTML rewrites with Slate/CSS class preservation and link integrity rules.
- **references/05-faq-category-copy.md** — FAQ generation (5A), brand+category FAQ 150–250 words (5B), extended PLP intro 230–260 words (5C).
- **references/08-eav-descriptions.md** — entity-attribute-value category research.

**Self-test results:** I ran the skill against a 3-URL PLP intro batch. The QA step correctly caught two pieces under 230 chars and flagged all three ending with identical TGG placement. The routing, reference loading, and cross-batch variation check all function as intended.

**What to try first:** Give it a real batch of 5–10 PLP URLs and see if the variation enforcement catches patterns you'd normally have to flag manually. That's where the batch logic earns its keep.

---

### 9. **Human** — 2026-03-18T03:52

I want you to host it fully in your skill repo so it is online and always 'updatable' by yourself if i change things.
I want you to host it fully in your skill repo so it is online and always 'updatable' by yourself if i change things.

---

### 10. **Claude** — 2026-03-18T03:53

Good call. Let me check what skill locations are writable in this environment:
```
This block is not supported on your current device yet.
```

All skill directories here are read-only. This environment (claude.ai) doesn't have a writable skill folder I can persist to. The skill files reset between sessions.

To host this where it's always online and I can update it myself when you change rules, the right move is to put it in your existing GitHub repo. That way:

1. The files live at a permanent URL I can always fetch.
2. You can review changes via PR/diff before they go live.
3. When you tell me "update the PLP intro char limit to 240–270" in any future session, I can fetch the current version, make the edit, and give you the updated file to push. Or if you're in Claude Code, I can push it directly.

Let me structure it to slot into your existing repo layout:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me also update the SKILL.md reference paths to be repo-relative, and add the skill to CLAUDE.md so Claude Code knows about it:
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

Here's the plan for getting this live in your repo:

**What to do in Claude Code:**

1. Create `skills/tgg-copywriting/` in your repo root (alongside `context_mode/`, `.github/`, etc.)
2. Drop all 7 files into the structure:
   ```
   skills/tgg-copywriting/
   ├── SKILL.md
   └── references/
       ├── 00-tov.md
       ├── 01-plp-intros.md
       ├── 02-metadata.md
       ├── 03-inlink-migration.md
       ├── 05-faq-category-copy.md
       └── 08-eav-descriptions.md
   ```
3. Add the `CLAUDE_MD_ADDITIONS.md` content into your existing `CLAUDE.md` and `claude.md` files. This tells Claude Code to use the skill directory as the canonical copywriting reference.
4. Commit and push.

**How updates work going forward:** When you tell me (in any session, Claude Code or claude.ai) something like "banned word list changed, add 'unbeatable' to the bans", I'll produce the exact edit to the specific reference file. In Claude Code I can push it directly. In claude.ai I'll give you the diff.

**The `.skill` package file** is still available for standalone use, but the repo copy is what stays canonical and version-controlled.
 

Good call. Let me check what skill locations are writable in this environment:
All skill directories here are read-only. This environment (claude.ai) doesn't have a writable skill folder I can persist to. The skill files reset between sessions.

To host this where it's always online and I can update it myself when you change rules, the right move is to put it in your existing GitHub repo. That way:

1. The files live at a permanent URL I can always fetch.
2. You can review changes via PR/diff before they go live.
3. When you tell me "update the PLP intro char limit to 240–270" in any future session, I can fetch the current version, make the edit, and give you the updated file to push. Or if you're in Claude Code, I can push it directly.

Let me structure it to slot into your existing repo layout:
Now let me also update the SKILL.md reference paths to be repo-relative, and add the skill to CLAUDE.md so Claude Code knows about it:
Here's the plan for getting this live in your repo:

**What to do in Claude Code:**

1. Create `skills/tgg-copywriting/` in your repo root (alongside `context_mode/`, `.github/`, etc.)
2. Drop all 7 files into the structure:
   ```
   skills/tgg-copywriting/
   ├── SKILL.md
   └── references/
       ├── 00-tov.md
       ├── 01-plp-intros.md
       ├── 02-metadata.md
       ├── 03-inlink-migration.md
       ├── 05-faq-category-copy.md
       └── 08-eav-descriptions.md
   ```
3. Add the `CLAUDE_MD_ADDITIONS.md` content into your existing `CLAUDE.md` and `claude.md` files. This tells Claude Code to use the skill directory as the canonical copywriting reference.
4. Commit and push.

**How updates work going forward:** When you tell me (in any session, Claude Code or claude.ai) something like "banned word list changed, add 'unbeatable' to the bans", I'll produce the exact edit to the specific reference file. In Claude Code I can push it directly. In claude.ai I'll give you the diff.

**The `.skill` package file** is still available for standalone use, but the repo copy is what stays canonical and version-controlled.

---

### 11. **Human** — 2026-03-18T04:03

give it context.
give it context.

---

### 12. **Claude** — 2026-03-18T04:03

You mean the skill needs to understand what TGG's site actually looks like, what categories exist, what brands sit where, what the URL structure is, and what real copy looks like on the ground. Right now it knows the rules but has no grounding in the actual site.

Let me think about what context layers would be most useful:
```
This block is not supported on your current device yet.
```

This will determine whether I build a static reference doc, a live-fetching context layer, or both.
 

You mean the skill needs to understand what TGG's site actually looks like, what categories exist, what brands sit where, what the URL structure is, and what real copy looks like on the ground. Right now it knows the rules but has no grounding in the actual site.

Let me think about what context layers would be most useful:
This will determine whether I build a static reference doc, a live-fetching context layer, or both.

---

### 13. **Human** — 2026-03-18T04:06

Q: Which context layers should the skill have access to? (Select all that apply)
A: I meant you need to give some context to claude coode on all this and what to do with it

Q: Do you have existing material to feed in, or should I pull context from thegoodguys.com.au directly?
A: [No preference]
Q: Which context layers should the skill have access to? (Select all that apply)
A: I meant you need to give some context to claude coode on all this and what to do with it

Q: Do you have existing material to feed in, or should I pull context from thegoodguys.com.au directly?
A: [No preference]

---

### 14. **Claude** — 2026-03-18T04:08

Got it. You want a proper README/integration guide so that Claude Code knows what this skill is, how the pieces fit together, where it lives, and how to use it in practice. Not site context, but operational context for the AI working with it.

Let me build that directly into the skill and rewrite the CLAUDE.md additions to be comprehensive.
```
This block is not supported on your current device yet.
```

Now let me rewrite the CLAUDE.md additions to be a proper integration block, not just a stub:
```
This block is not supported on your current device yet.
```

Now let me copy the final set to outputs:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's what's ready to drop into your repo:

**`skills/tgg-copywriting/README.md`** — the operational context file. This is what Claude Code reads to understand the full picture: what the skill is, why it exists, how every piece connects, common task mappings with exact file paths, the relationship between skill references and root process files, how to update rules, what the skill does NOT cover, and a "key constraints to remember" section covering the gotchas that trip up most often (chars vs words, banned words on brand PLPs, "across the range" legal risk, etc).

**`skills/tgg-copywriting/CLAUDE_MD_INTEGRATION.md`** — the exact blocks to merge into your `CLAUDE.md` and `claude.md`. Covers when to use the skill, how to use it, the "don't fall back to root process files" instruction, the canonical source mapping table (root file → skill reference), how workflows A–D interact with the skill vs direct process files, and the `.claude/settings.json` registration snippet.

**To get this live:** In your next Claude Code session, create `skills/tgg-copywriting/`, drop the full directory in, merge the integration blocks into your CLAUDE.md files, update `.claude/settings.json`, commit and push. From that point on, any Claude Code session that reads your CLAUDE.md will know exactly what to do with copywriting tasks.
 

Got it. You want a proper README/integration guide so that Claude Code knows what this skill is, how the pieces fit together, where it lives, and how to use it in practice. Not site context, but operational context for the AI working with it.

Let me build that directly into the skill and rewrite the CLAUDE.md additions to be comprehensive.
Now let me rewrite the CLAUDE.md additions to be a proper integration block, not just a stub:
Now let me copy the final set to outputs:
Here's what's ready to drop into your repo:

**`skills/tgg-copywriting/README.md`** — the operational context file. This is what Claude Code reads to understand the full picture: what the skill is, why it exists, how every piece connects, common task mappings with exact file paths, the relationship between skill references and root process files, how to update rules, what the skill does NOT cover, and a "key constraints to remember" section covering the gotchas that trip up most often (chars vs words, banned words on brand PLPs, "across the range" legal risk, etc).

**`skills/tgg-copywriting/CLAUDE_MD_INTEGRATION.md`** — the exact blocks to merge into your `CLAUDE.md` and `claude.md`. Covers when to use the skill, how to use it, the "don't fall back to root process files" instruction, the canonical source mapping table (root file → skill reference), how workflows A–D interact with the skill vs direct process files, and the `.claude/settings.json` registration snippet.

**To get this live:** In your next Claude Code session, create `skills/tgg-copywriting/`, drop the full directory in, merge the integration blocks into your CLAUDE.md files, update `.claude/settings.json`, commit and push. From that point on, any Claude Code session that reads your CLAUDE.md will know exactly what to do with copywriting tasks.

---

### 15. **Human** — 2026-03-18T05:51

okay im confused, what skills go into claude skills and what do i give to claude code - and why? separate it all
okay im confused, what skills go into claude skills and what do i give to claude code - and why? separate it all

---

### 16. **Claude** — 2026-03-18T05:52

Fair question. Let me lay this out clearly.

**Two different systems, two different purposes:**

**Claude.ai Skills** (this chat interface, where we are now) — you install a `.skill` file, and it becomes available as a tool that claude.ai can trigger automatically when you ask relevant questions. It works through the `available_skills` list in the system prompt. The skill needs to be self-contained because claude.ai has no persistent filesystem between sessions.

**Claude Code** (your terminal setup with CLAUDE.md, context mode, git) — there are no "skills" in the same sense. Claude Code reads your `CLAUDE.md` at session start, follows the instructions there, and reads files from disk when told to. Your existing process files (00–09) already work this way. Adding a `skills/` folder is just a reorganisation of files Claude Code reads from disk.

The problem is: **your process files already work in Claude Code.** The gap is claude.ai, where you don't have those files on disk.

So here's the clean separation:
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

Here's the clean split:

**For claude.ai** → Install `tgg-copywriting.skill`. That's the only deliverable. It bundles your copywriting rules into something this interface can use, since it can't read your repo.

**For Claude Code** → Change nothing. Your process files already work. The only optional addition is a 4-line note in CLAUDE.md flagging that a claude.ai skill exists and needs rebuilding when process files change.

**When rules change** → Update the process file in your repo (Claude Code is immediately current). Then tell me in claude.ai and I'll rebuild the `.skill` file.

The previous deliverables with the `skills/` directory, README, integration guide, and settings.json changes were unnecessary complexity. Your Claude Code setup was already correct.
 

Fair question. Let me lay this out clearly.

**Two different systems, two different purposes:**

**Claude.ai Skills** (this chat interface, where we are now) — you install a `.skill` file, and it becomes available as a tool that claude.ai can trigger automatically when you ask relevant questions. It works through the `available_skills` list in the system prompt. The skill needs to be self-contained because claude.ai has no persistent filesystem between sessions.

**Claude Code** (your terminal setup with CLAUDE.md, context mode, git) — there are no "skills" in the same sense. Claude Code reads your `CLAUDE.md` at session start, follows the instructions there, and reads files from disk when told to. Your existing process files (00–09) already work this way. Adding a `skills/` folder is just a reorganisation of files Claude Code reads from disk.

The problem is: **your process files already work in Claude Code.** The gap is claude.ai, where you don't have those files on disk.

So here's the clean separation:
Here's the clean split:

**For claude.ai** → Install `tgg-copywriting.skill`. That's the only deliverable. It bundles your copywriting rules into something this interface can use, since it can't read your repo.

**For Claude Code** → Change nothing. Your process files already work. The only optional addition is a 4-line note in CLAUDE.md flagging that a claude.ai skill exists and needs rebuilding when process files change.

**When rules change** → Update the process file in your repo (Claude Code is immediately current). Then tell me in claude.ai and I'll rebuild the `.skill` file.

The previous deliverables with the `skills/` directory, README, integration guide, and settings.json changes were unnecessary complexity. Your Claude Code setup was already correct.

---

### 17. **Human** — 2026-03-18T06:07

why 3 download files if i just need 1?
why 3 download files if i just need 1?

---

### 18. **Claude** — 2026-03-18T06:07

You're right. Here's the one file.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Install this in claude.ai. Your Claude Code setup needs no changes.
 

You're right. Here's the one file.
Install this in claude.ai. Your Claude Code setup needs no changes.
