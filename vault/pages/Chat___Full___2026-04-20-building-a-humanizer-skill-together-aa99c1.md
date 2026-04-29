---
title: Building a humanizer skill together (full)
parent: Chat/Light/2026-04-20-building-a-humanizer-skill-together-aa99c1
uuid: aa99c12e-c1e0-4281-9b0f-e3390360e9cc
---

#chat/full #project/skills-built-full-set #status/completed

# Building a humanizer skill together — Full Transcript

→ Light view: [[Chat/Light/2026-04-20-building-a-humanizer-skill-together-aa99c1]]
→ Medium view: [[Chat/Medium/2026-04-20-building-a-humanizer-skill-together-aa99c1]]

**Messages:** 6 | **Date:** 2026-04-20

---

### 1. **Human** — 2026-04-20T05:46

i want us to make a skill together https://github.com/blader/humanizer
i want us to make a skill together https://github.com/blader/humanizer

---

### 2. **Claude** — 2026-04-20T05:47

Simon wants to build a skill together based on the humanizer GitHub repo. I can see the README.md and WARP.md in context, and there's also a SKILL.md uploaded. Let me read the SKILL.md to understand the full skill definition before we discuss building one together.
```
This block is not supported on your current device yet.
```

Now I have a full picture. Simon wants to build a skill together based on this humanizer repo. I should ask what kind of skill he wants to build. A few possibilities:
1. A TGG-specific variant of the humanizer (adapted for TGG's brand voice)
2. An entirely different new skill inspired by the structure/format of this one
3. A fork/adaptation of the humanizer skill for Claude.ai skills format (vs Claude Code skills format)

Let me read the uploaded AI_Humanizer__Content_Improvement_Prompt.docx too.

Actually, I should ask what he wants to make. "Make a skill together" could mean many things. 

Let me check the docx file first to understand what the humanizer prompt is actually about.
```
This block is not supported on your current device yet.
```

Now I have full context. Simon wants to build a skill together based on the humanizer repo. I need to understand what kind of skill he wants. A few possibilities:
1. A Claude.ai-compatible version of the humanizer skill (the existing SKILL.md is for Claude Code/OpenCode)
2. A TGG-adapted version of the humanizer for their specific content needs
3. Something else entirely that the humanizer inspired

Also, there's an uploaded `AI_Humanizer__Content_Improvement_Prompt.docx` I haven't read. Let me read it.

Actually, let me clarify what Simon wants first. 

I'm seeing some ambiguity here—he could want to port the humanizer to Claude.ai's skill format, build a TGG-specific variant, or create something entirely new using the humanizer as inspiration. The docx file he uploaded might clear this up, so let me check that first.Let me read that docx before asking anything, as it might clarify intent.
```
This block is not supported on your current device yet.
```

Now let me read the docx file to understand what's in it.
```
This block is not supported on your current device yet.
```

Now I have full context. Simon has already built a TGG-specific adaptation of the humanizer skill. The docx is called "AI_Humanizer__Content_Improvement_Prompt.docx" and it's a complete prompt adaptation of the humanizer for TGG ecommerce content.

So what does he want to do? He wants to make a skill together based on the humanizer repo. Given that he already has the TGG-adapted prompt in docx form, I think he wants to:
1. Turn this docx into a proper Claude.ai-compatible skill (SKILL.md format)


2. Or possibly build something new entirely

The docx is clearly a TGG-specific version of the humanizer, but I'm not entirely sure if he wants to package it as a Claude.ai skill in his tgg-* folder or if he's looking to create something different. I should clarify what he's aiming for before proceeding.Good context. You've already built a TGG-adapted version of the humanizer (the docx). Clear question before I start writing anything:

Is the goal to package your existing TGG ecommerce prompt from the docx into a proper `SKILL.md` for your Claude.ai skills folder, or are you looking to build a different skill that the humanizer inspires?
 
Let me read that docx before asking anything, as it might clarify intent.
Good context. You've already built a TGG-adapted version of the humanizer (the docx). Clear question before I start writing anything:

Is the goal to package your existing TGG ecommerce prompt from the docx into a proper `SKILL.md` for your Claude.ai skills folder, or are you looking to build a different skill that the humanizer inspires?

---

### 3. **Human** — 2026-04-20T05:53

im looking to use the existing skills, just removeing any issues and aligning more to tgg, to be used in conjunction with seo copywriter or any writing (such as report or response or email)
im looking to use the existing skills, just removeing any issues and aligning more to tgg, to be used in conjunction with seo copywriter or any writing (such as report or response or email)

---

### 4. **Claude** — 2026-04-20T05:58

So Simon wants to take the existing humanizer SKILL.md and adapt it for TGG use, removing issues and aligning it to TGG's context. It should work in conjunction with his existing TGG skills (like tgg-copywriting, tgg-content-strategist) and also for broader writing like reports, emails, and responses.

Let me think about what this means:
1. Start from the existing SKILL.md (v2.5.1, 29 patterns)
2. Adapt for TGG context (Australian English, retail/ecommerce, brand voice)


3. Keep it general enough for reports, emails, responses (not just copy)
4. Remove any issues with the existing skill

Looking at what needs to be trimmed or reworked: the voice calibration section adds length without much payoff, the "PERSONALITY AND SOUL" section is too editorial for TGG's ecommerce and business writing needs, and some patterns already overlap with Simon's existing global preferences. The three-stage output format (draft → audit → final) works well, but the full example is unnecessarily long. For TGG specifically, I need to reframe the brand voice around The Good Guys' tone and retail context rather than general humanization.

The skill should adapt for TGG's Australian, conversational, useful voice without being promotional, replace that personality section with guidance for multiple writing contexts, and reference the docx patterns where they're actually TGG-specific. I should keep the em dash and curly quote rules since they reinforce what's already in the global preferences, but I can flag the voice calibration feature as less critical now that the brand voice is already defined. The skill needs to complement the copywriting and SEO specialist skills without duplicating them.

For the structure, I'm keeping the 29 pattern framework as the core, but swapping out the personality section for TGG writing principles that cover ecommerce copy, business writing, and SEO content. I'll simplify or remove voice calibration, add TGG-specific banned words, keep the two-pass audit process, and update examples to fit the context. I also need to flag some conflicts: the first-person perspective instruction doesn't work for product listing page copy, "let some mess in" isn't right for professional writing, and those named example people should probably go since they're generic.

The skill should work as a post-processing filter that complements tgg-copywriting without duplicating its rules, while still being useful standalone for reports and emails. I'm going to move forward with building this—I'll call it `tgg-humanizer`, keep the 29 patterns as the foundation, replace the personality section with context-specific writing principles for TGG's three modes, and strip down or remove the voice calibration since TGG's voice is already defined.

Looking at what needs fixing in the current SKILL.md: the "PERSONALITY AND SOUL" section pushes advice like having opinions and letting mess in, which doesn't fit TGG's professional brand or formal documents. The voice calibration is redundant when the brand voice is established. And I should review pattern #13 on passive voice to make sure it aligns with TGG standards rather than general writing advice.

The example needs updating too—it's currently a tech blog post, but I should use something from TGG's ecommerce work instead. I also notice the draft invents fake people and citations, which models exactly the kind of behavior I want to avoid teaching. The allowed-tools in the frontmatter reference Claude Code tools, but Simon works in Claude.ai, so I should check whether those even belong there or if I should drop them entirely based on how his other TGG skills are structured.

Now I'm thinking through how this skill actually operates in practice. When paired with the copywriting skill, it should work as a post-edit filter to humanize the output. But used standalone on reports, it needs to catch AI patterns and clean them up. I'll keep all 29 patterns since they're solid, reorganize around TGG's actual writing principles rather than generic personality traits, strip out the voice calibration section to keep it lean, swap in an ecommerce example, add TGG-specific banned words where relevant, and note that the em dash rule is already a hard preference for Simon. I should also add a note about Australian English. Aiming to keep the whole thing under 500 lines.

For the principles section, I need to account for three distinct contexts: ecommerce copy that's utility-focused with specific product details and no fluff, business writing that's direct and evidence-backed without corporate padding, and customer-facing communications that feel conversational but professional while avoiding chatbot artifacts. Let me write out the SKILL.md cleanly now.

I'm also reconsidering whether to keep the em dash pattern since Simon's global preference already handles it, but I think it should stay—the skill needs to be self-contained and the pattern is still valid without creating conflicts. Now I'm writing the YAML structure that defines the humanizer skill, including its version, description of what it does across different content types, and how it integrates with other skills as a post-edit filter.

Writing the skill metadata and trigger conditions...

Organizing the content into sections with TGG writing principles and the 29 patterns, keeping examples concise...

Building out the pattern groups with before/after pairs and word lists for detection...

Laying out the two-pass process and output format guidelines...

Drafting the full example to show how all the patterns work together in practice... I'm pulling together the writing guidelines across different contexts—ecommerce product descriptions need utility and specifics, business writing demands metrics upfront without corporate jargon, and communications should address the reader's actual question. I'm noticing the current SKILL.md format shows a draft rewrite followed by explanation, but I should tighten that structure and integrate the 29 patterns I've already adapted for ecommerce into a more cohesive guide. I'm organizing the 29 AI-detection patterns into the SKILL.md file, using the TGG-focused examples from the existing document and adapting the remaining ones to fit that context while noting the same principles apply to reports and emails.
```
This block is not supported on your current device yet.
```

Now I have all 29 patterns. Let me build the TGG-adapted SKILL.md.

Key changes from original:
1. Name: tgg-humanizer
2. Replace PERSONALITY AND SOUL with TGG Writing Principles (3 contexts)
3. Remove voice calibration (TGG voice defined)
4. Use TGG-specific examples for relevant patterns (from the docx)
5. Add TGG banned words to pattern #7
6. Update pattern #4 to include TGG promotional words (from docx)
7. Update pattern #17 to note Australian title case convention


8. Keep the 2-pass process and use the full TGG example from the docx
9. Reinforce the em dash rule as a global preference across all content

I need to clean up the PERSONALITY section by removing "Have opinions", "Use 'I' when it fits", and "Let some mess in", plus remove the fabricated citations in the example. For pattern #26, I'm reconsidering the hyphenation approach—removing hyphens from standard compounds like "third-party" when used as modifiers would actually create issues, so I'll refine that guidance.

Pattern #13 on passive voice needs more nuance since passive construction is sometimes the right choice in copy. Now I'm drafting the SKILL.md file, aiming for around 400 lines, and breaking down the TGG Writing Principles across three distinct contexts: ecommerce copy prioritizes utility and specific details over vague praise, business writing leads with metrics and concrete numbers while avoiding corporate jargon, and I'm working through what the third context requires.

For communications—emails, stakeholder updates, responses—the focus shifts to answering what the reader actually needs, matching the tone to who you're writing to, and keeping each message to a single clear purpose. Now I'm adapting the key patterns to fit TGG's specific context, pulling in the promotional language they actually use like "vibrant," "nestled," and "groundbreaking," and I'll adjust the AI vocabulary and hyphenated word pair patterns to reflect retail writing conventions.

On the hyphenation front, I'm realizing the original advice was too broad—removing hyphens from "third-party" doesn't make sense. The real issue is specific pairs like "high-quality" and "data-driven" that get overused, while standard compounds like "real-time" and "long-term" should stay hyphenated. I'll narrow that pattern and add a clarifying note.

For Australian English, I'll add that to the intro section with the key spelling shifts: colour, recognise, organise, metre, centre, and -ise endings instead of -ize. Now I'm ready to write the file with concise examples throughout.Good. I have everything I need: the original SKILL.md (29 patterns), your TGG-adapted docx, and full context on how you use skills.

Issues I'll fix in the build:
- **PERSONALITY AND SOUL section** has "Use 'I' when it fits" and "Let some mess in." Wrong for brand copy, reports, and emails. Replacing with context-aware TGG writing principles (3 modes: copy, business writing, comms).
- **Voice calibration** removed (TGG voice is already defined across your skills).
- **Pattern #26** (hyphenated word pairs): original advice strips hyphens from standard compounds like "third-party" and "real-time." That's wrong. Narrowing to the ones that are genuinely AI-inflated.
- **Made-up citations** in the full example (Mira, fake study). Replacing with a TGG ecommerce example from your docx.
- **Pattern #13** (passive voice): adding a note that passive is acceptable in copy when the actor is irrelevant or the sentence reads more naturally.
- Adding TGG promotional word list and Australian English note.
```
This block is not supported on your current device yet.
```

Good. Now let me package it as a .skill file for Simon to download, and present it.Now let me package it and validate the line count before presenting.
```
This block is not supported on your current device yet.
```

The em dashes in the "Your Task" section (lines 29-33) are used as list separators in a format like "1. **Identify AI patterns** — Scan for...". These are instructional list items in the skill's body, not in output that would go to a user. However, since Simon's preference is to replace em dashes with a full stop for independent clauses or a comma for non-essential phrases, I should fix these.

The em dash in line 6 (frontmatter description) uses "—" to separate list items. That's a list separator, not really a clause separator. Still, I should fix for consistency.


Now I'm looking at line 125, which has an em dash in an example showing the "after" result of pattern 4. I'll change that to a full stop for consistency. I also notice the list items in lines 29-33 use em dashes as definition separators, which I should convert to colons to align with Simon's preferences about em dash usage. I've identified the em dash issues and need to trim about 20 lines to get under 500. I'll remove or condense the note after pattern 4, tighten some of the before examples, and streamline the process section to hit the target.
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

Let me check lines 388, 475, and 492:

- L249: "**Problem:** LLMs use em dashes (—) far more than humans." - This is a reference to the em dash character itself, not a use of em dash as punctuation. Fine.
- L388: "For reports and emails: end on the next step, open question, or specific recommendation —" - This uses em dash. I need to fix this.
- L475: "2. **Remaining AI tells** (brief bullets — skip if none)" - This uses em dash. I should fix this to use a comma or restructure.


- L492: "- Rhythm is still very even — four sentences of similar length and structure" - This is inside a quoted example block showing the "Remaining AI tells" output, so it's acceptable since it's demonstrating the skill's output rather than the skill's own writing.

Now I need to verify whether these lines are actually in example blocks or not. Let me look at the context around each one to determine if they're in code blocks or regular text.
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

Line 492 is inside the "Full Example" section showing example "Remaining AI tells" output. Let me check what exactly this is.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Both are in `>` quoted example blocks:
- Line 253: "Before" example showing incorrect em dash usage (correct, this should be there)
- Line 498: This is the "Final rewrite" example in the Full Example section. This should NOT have an em dash. Let me fix it.Line 498 is the "Final rewrite" in the full example. That shouldn't have an em dash.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The only remaining em dash is in line 253, which is inside the "Before" example block for pattern 14 (em dash overuse). That's correct - it's showing the bad example.

Now let me copy it to the outputs directory and present it.Only remaining em dash is in the "Before" example for pattern 14, which is correct. Now package and present.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

517 lines, all 29 patterns retained, no em dashes outside example blocks.

**What changed from the original:**

The PERSONALITY AND SOUL section is gone. In its place: three context-aware writing principles for ecommerce copy, business writing, and communications. The "Use 'I' when it fits" and "Let some mess in" instructions would have been actively harmful for brand copy and reports.

Voice calibration is removed. TGG voice is already defined across your other skills.

Pattern #4 uses TGG's specific promotional word list from your docx (transform, elevate, discover, curated, etc.) rather than the generic Wikipedia-sourced one.

Pattern #13 (passive voice) now notes that passive is acceptable when the actor is genuinely irrelevant, which matters for copy.

Pattern #26 (hyphenated word pairs) no longer strips hyphens from standard compounds like "third-party," "real-time," and "long-term." The original rule was wrong. It now only targets the genuinely AI-inflated pairs.

The full example uses the fridge PLP from your docx, not a tech blog post with invented citations.

**To install:** rename to `SKILL.md`, drop it in `~/.claude/skills/tgg-humanizer/`, and it will be available alongside your other TGG skills.
 
Good. I have everything I need: the original SKILL.md (29 patterns), your TGG-adapted docx, and full context on how you use skills.

Issues I'll fix in the build:
- **PERSONALITY AND SOUL section** has "Use 'I' when it fits" and "Let some mess in." Wrong for brand copy, reports, and emails. Replacing with context-aware TGG writing principles (3 modes: copy, business writing, comms).
- **Voice calibration** removed (TGG voice is already defined across your skills).
- **Pattern #26** (hyphenated word pairs): original advice strips hyphens from standard compounds like "third-party" and "real-time." That's wrong. Narrowing to the ones that are genuinely AI-inflated.
- **Made-up citations** in the full example (Mira, fake study). Replacing with a TGG ecommerce example from your docx.
- **Pattern #13** (passive voice): adding a note that passive is acceptable in copy when the actor is irrelevant or the sentence reads more naturally.
- Adding TGG promotional word list and Australian English note.
Now let me package it and validate the line count before presenting.
Line 498 is the "Final rewrite" in the full example. That shouldn't have an em dash.
Only remaining em dash is in the "Before" example for pattern 14, which is correct. Now package and present.
517 lines, all 29 patterns retained, no em dashes outside example blocks.

**What changed from the original:**

The PERSONALITY AND SOUL section is gone. In its place: three context-aware writing principles for ecommerce copy, business writing, and communications. The "Use 'I' when it fits" and "Let some mess in" instructions would have been actively harmful for brand copy and reports.

Voice calibration is removed. TGG voice is already defined across your other skills.

Pattern #4 uses TGG's specific promotional word list from your docx (transform, elevate, discover, curated, etc.) rather than the generic Wikipedia-sourced one.

Pattern #13 (passive voice) now notes that passive is acceptable when the actor is genuinely irrelevant, which matters for copy.

Pattern #26 (hyphenated word pairs) no longer strips hyphens from standard compounds like "third-party," "real-time," and "long-term." The original rule was wrong. It now only targets the genuinely AI-inflated pairs.

The full example uses the fridge PLP from your docx, not a tech blog post with invented citations.

**To install:** rename to `SKILL.md`, drop it in `~/.claude/skills/tgg-humanizer/`, and it will be available alongside your other TGG skills.

---

### 5. **Human** — 2026-04-20T06:05

can you just save it?
can you just save it?

---

### 6. **Claude** — 2026-04-20T06:05

Simon wants me to save the skill file to his skills directory. Let me do that.
```
This block is not supported on your current device yet.
```

Done. It's at `~/.claude/skills/tgg-humanizer/SKILL.md`.
 
Done. It's at `~/.claude/skills/tgg-humanizer/SKILL.md`.
