---
title: Building a self-optimizing Claude skill for prompt formatting (full)
parent: Chat/Light/2026-04-29-building-a-self-optimizing-claude-skill-for-prompt-formattin-8f2f90
uuid: 8f2f90c8-62a4-4290-9514-25ef8bf6e0a7
---

#chat/full #project/main #status/completed

# Building a self-optimizing Claude skill for prompt formatting — Full Transcript

→ Light view: [[Chat/Light/2026-04-29-building-a-self-optimizing-claude-skill-for-prompt-formattin-8f2f90]]
→ Medium view: [[Chat/Medium/2026-04-29-building-a-self-optimizing-claude-skill-for-prompt-formattin-8f2f90]]

**Messages:** 29 | **Date:** 2026-04-29

---

### 1. **Human** — 2026-04-29T02:19

conduct indepth research in ai prompting, ai project management first principles, ai context and how to get it to research, plan, run a self checklist and update it as it goes through stages, setting up failsafes etc. - the final goal is to create a claude skill that runs every time i interact with claude to repivot my question into the correct format for the best output.
conduct indepth research in ai prompting, ai project management first principles, ai context and how to get it to research, plan, run a self checklist and update it as it goes through stages, setting up failsafes etc. - the final goal is to create a claude skill that runs every time i interact with claude to repivot my question into the correct format for the best output.

---

### 2. **Claude** — 2026-04-29T02:19

Three things shape the deliverable significantly. Quick clarifications:

1. **Skill scope:** should it rewrite/repivot every prompt I send (always-on interceptor), or only trigger when I explicitly ask for prompt repair (e.g. "fix this prompt")?
2. **Output style:** should the skill return the rewritten prompt for me to approve before Claude executes, or silently restructure and answer in one pass?
3. **Domain coverage:** general-purpose across all my work, or weighted toward TGG/SEO/analytics tasks specifically?


Three things shape the deliverable significantly. Quick clarifications:

1. **Skill scope:** should it rewrite/repivot every prompt I send (always-on interceptor), or only trigger when I explicitly ask for prompt repair (e.g. "fix this prompt")?
2. **Output style:** should the skill return the rewritten prompt for me to approve before Claude executes, or silently restructure and answer in one pass?
3. **Domain coverage:** general-purpose across all my work, or weighted toward TGG/SEO/analytics tasks specifically?

---

### 3. **Human** — 2026-04-29T02:23

always on

silently restructure
both, all work all types of prompt tasks i may run
always on

silently restructure
both, all work all types of prompt tasks i may run

---

### 4. **Claude** — 2026-04-29T02:27

Got it. Kicking off deep research now into prompting first principles, AI project management patterns, context engineering, self-checking and failsafe design, plus Claude skill architecture, so the final output is a build-ready spec for an always-on silent prompt-repivoting skill covering all task types.
```
This block is not supported on your current device yet.
```




Got it. Kicking off deep research now into prompting first principles, AI project management patterns, context engineering, self-checking and failsafe design, plus Claude skill architecture, so the final output is a build-ready spec for an always-on silent prompt-repivoting skill covering all task types.

---

### 5. **Claude** — 2026-04-29T02:52

Confirmed: always-on, silent restructure, all work types. Starting research now into prompt engineering first principles, AI project management, context-setting, self-checking systems, failsafes, and the architecture for an always-on prompt-repivoting skill.
```
This block is not supported on your current device yet.
```

Your research report on designing an always-on prompt restructuring skill for Claude is ready. It synthesises Anthropic's 2026 prompting guidance, the current Agent Skills architecture, the academic and practitioner literature on automatic prompt optimisation and self-verification, and lessons from existing community prompt-rewriter skills. The report covers first principles of Claude 4.x prompting, project management phasing, context engineering, self-checklist design, failsafes against intent drift and sycophantic self-grading, and the platform constraints on "always-on" skills in Claude.ai versus Claude Code. It concludes with a concrete design recommendation for `tgg-prompt-architect`, including a triage-first algorithm, hard-skip rules, a constraint-verification checklist, a SKILL.md skeleton, an evaluation plan, and explicit guardrails against conflicts with your existing TGG skill library and userPreferences.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```




Confirmed: always-on, silent restructure, all work types. Starting research now into prompt engineering first principles, AI project management, context-setting, self-checking systems, failsafes, and the architecture for an always-on prompt-repivoting skill.
Your research report on designing an always-on prompt restructuring skill for Claude is ready. It synthesises Anthropic's 2026 prompting guidance, the current Agent Skills architecture, the academic and practitioner literature on automatic prompt optimisation and self-verification, and lessons from existing community prompt-rewriter skills. The report covers first principles of Claude 4.x prompting, project management phasing, context engineering, self-checklist design, failsafes against intent drift and sycophantic self-grading, and the platform constraints on "always-on" skills in Claude.ai versus Claude Code. It concludes with a concrete design recommendation for `tgg-prompt-architect`, including a triage-first algorithm, hard-skip rules, a constraint-verification checklist, a SKILL.md skeleton, an evaluation plan, and explicit guardrails against conflicts with your existing TGG skill library and userPreferences.

---

### 6. **Human** — 2026-04-29T03:18

how do we turn it into a skill?
how do we turn it into a skill?

---

### 7. **Claude** — 2026-04-29T03:21

Building the skill now. Loading skill-creator first to get the current scaffold conventions, then producing a clean ZIP you can upload to Claude.ai.
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

Good. Building the skill now.
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

Packaged and validated. To install:

1. Open Claude.ai → Settings → Capabilities → **Skills**.
2. Click **Upload skill** and select `tgg-prompt-architect.skill`.
3. Make sure **Code execution** is enabled (required for skills to load).

**Honest caveat on "always-on":** Claude.ai skills are model-invoked from the description. There is no platform flag that forces a skill to fire on every message. The description is engineered to match almost any substantive work prompt, but expect occasional misses on borderline messages, especially short or ambiguous ones. If you want deterministic activation on every prompt, the only path is Claude Code with a `UserPromptSubmit` hook. Tell me if you want that version too.

**After 1-2 weeks of live use**, watch for: over-triggering on simple prompts (skill kicks in when it should skip), conflict with existing TGG skills (two skills competing), or padded rewrites. Any of those means we re-tune the description or the triage rules.
 Building the skill now. Loading skill-creator first to get the current scaffold conventions, then producing a clean ZIP you can upload to Claude.ai.
Good. Building the skill now.
Packaged and validated. To install:

1. Open Claude.ai → Settings → Capabilities → **Skills**.
2. Click **Upload skill** and select `tgg-prompt-architect.skill`.
3. Make sure **Code execution** is enabled (required for skills to load).

**Honest caveat on "always-on":** Claude.ai skills are model-invoked from the description. There is no platform flag that forces a skill to fire on every message. The description is engineered to match almost any substantive work prompt, but expect occasional misses on borderline messages, especially short or ambiguous ones. If you want deterministic activation on every prompt, the only path is Claude Code with a `UserPromptSubmit` hook. Tell me if you want that version too.

**After 1-2 weeks of live use**, watch for: over-triggering on simple prompts (skill kicks in when it should skip), conflict with existing TGG skills (two skills competing), or padded rewrites. Any of those means we re-tune the description or the triage rules.

---

### 8. **Human** — 2026-04-29T04:23

where?
where?

---

### 9. **Claude** — 2026-04-29T04:23

In Claude.ai web app:

**Settings (bottom left, click your name) → Capabilities → toggle "Code execution and file creation" on.**

On mobile it's under your profile icon → Settings → Capabilities.

If you don't see "Capabilities" as a section, look for it under "Features" or "Beta features" depending on your plan tier. The skill upload itself lives in the same area: **Settings → Capabilities → Skills → Upload**.
 In Claude.ai web app:

**Settings (bottom left, click your name) → Capabilities → toggle "Code execution and file creation" on.**

On mobile it's under your profile icon → Settings → Capabilities.

If you don't see "Capabilities" as a section, look for it under "Features" or "Beta features" depending on your plan tier. The skill upload itself lives in the same area: **Settings → Capabilities → Skills → Upload**.

---

### 10. **Human** — 2026-04-29T04:24

its toggled
its toggled

---

### 11. **Claude** — 2026-04-29T04:24

Good. Upload the `.skill` file in the same Skills section, then test it on a few real prompts. Watch for:

- **Over-triggering:** kicks in on simple lookups or continuations
- **Padded rewrites:** adds role recital or restates your brief
- **Skill collision:** competes with `tgg-copywriting` or `tgg-seo-specialist` instead of handing off

Flag any of those and we tune the triage rules.
 Good. Upload the `.skill` file in the same Skills section, then test it on a few real prompts. Watch for:

- **Over-triggering:** kicks in on simple lookups or continuations
- **Padded rewrites:** adds role recital or restates your brief
- **Skill collision:** competes with `tgg-copywriting` or `tgg-seo-specialist` instead of handing off

Flag any of those and we tune the triage rules.

---

### 12. **Human** — 2026-04-29T04:24

how do i test it?
how do i test it?

---

### 13. **Claude** — 2026-04-29T04:25

Run prompts that should trigger different behaviours and check the skill behaved correctly. Six tests cover the main failure modes:

**1. Should fully restructure** (vague work request)
> `plp intros for the new dyson v17 pages`

Expect: rewritten brief naming `tgg-copywriting`, character limits, banned words, AU English. Possibly a one-line disclosure if it inferred which Dyson range.

**2. Should hard-skip** (greeting)
> `thanks`

Expect: normal short response. No restructuring, no contract, no checklist.

**3. Should hard-skip** (continuation)
> `yes do option 2`

Expect: Claude continues the previous task. No restructuring.

**4. Should bypass** (prefix)
> `* write me a haiku about fridges`

Expect: haiku, no restructuring.

**5. Should soft-skip** (short, scoped)
> `meta description for lg fridge plp, 155 chars`

Expect: minimum-edit, not a full contract template. Output stays close to original length.

**6. Should disclose** (material inference)
> `build a slide on aio visibility`

Expect: one-line disclosure assuming the March deck or asking which month.

**How to verify it actually loaded:** ask Claude `which skills are active right now?` at the start of a fresh chat. `tgg-prompt-architect` should appear. If it doesn't, the upload failed or code execution isn't actually on.

Tell me which tests pass or fail and I'll tune from there.
 Run prompts that should trigger different behaviours and check the skill behaved correctly. Six tests cover the main failure modes:

**1. Should fully restructure** (vague work request)
> `plp intros for the new dyson v17 pages`

Expect: rewritten brief naming `tgg-copywriting`, character limits, banned words, AU English. Possibly a one-line disclosure if it inferred which Dyson range.

**2. Should hard-skip** (greeting)
> `thanks`

Expect: normal short response. No restructuring, no contract, no checklist.

**3. Should hard-skip** (continuation)
> `yes do option 2`

Expect: Claude continues the previous task. No restructuring.

**4. Should bypass** (prefix)
> `* write me a haiku about fridges`

Expect: haiku, no restructuring.

**5. Should soft-skip** (short, scoped)
> `meta description for lg fridge plp, 155 chars`

Expect: minimum-edit, not a full contract template. Output stays close to original length.

**6. Should disclose** (material inference)
> `build a slide on aio visibility`

Expect: one-line disclosure assuming the March deck or asking which month.

**How to verify it actually loaded:** ask Claude `which skills are active right now?` at the start of a fresh chat. `tgg-prompt-architect` should appear. If it doesn't, the upload failed or code execution isn't actually on.

Tell me which tests pass or fail and I'll tune from there.

---

### 14. **Human** — 2026-04-29T04:25

create a test promp i give to claude to test it
create a test promp i give to claude to test it

---

### 15. **Claude** — 2026-04-29T04:25

Here's a single prompt. Paste it into a fresh Claude.ai chat (skill must be uploaded and code execution on):

---

```
Run a self-test of the tgg-prompt-architect skill. For each of the 6 test prompts below, do the following:

1. State the test number and the user prompt verbatim.
2. State whether tgg-prompt-architect should HARD-SKIP, SOFT-SKIP (minimum-edit), FULLY RESTRUCTURE, BYPASS, or DISCLOSE.
3. Show what the skill would actually do: either "pass through unchanged" or the rewritten contract.
4. Mark PASS or FAIL against the expected behaviour.
5. If FAIL, explain why in one line.

After all 6, give a summary: X/6 passed.

Test prompts:

1. thanks
2. yes do option 2
3. * write me a haiku about fridges
4. meta description for lg fridge plp, 155 chars
5. plp intros for the new dyson v17 pages
6. build a slide on aio visibility

Expected behaviour:
1. HARD-SKIP (greeting)
2. HARD-SKIP (continuation)
3. BYPASS (prefix *)
4. SOFT-SKIP (short, scoped, under 30 tokens)
5. FULLY RESTRUCTURE + possibly DISCLOSE (vague work request, ambiguous Dyson range)
6. FULLY RESTRUCTURE + DISCLOSE (which deck/month is inferred)

Do not actually execute the underlying tasks (don't write the haiku, don't draft the meta description). Just show what the skill would do.

At the end, confirm: did tgg-prompt-architect appear in your active skills list at the start of this conversation? Yes/no.
```

---

Send it and paste the output back to me. I'll spot any gaps in the triage logic.
 Here's a single prompt. Paste it into a fresh Claude.ai chat (skill must be uploaded and code execution on):

---

```
Run a self-test of the tgg-prompt-architect skill. For each of the 6 test prompts below, do the following:

1. State the test number and the user prompt verbatim.
2. State whether tgg-prompt-architect should HARD-SKIP, SOFT-SKIP (minimum-edit), FULLY RESTRUCTURE, BYPASS, or DISCLOSE.
3. Show what the skill would actually do: either "pass through unchanged" or the rewritten contract.
4. Mark PASS or FAIL against the expected behaviour.
5. If FAIL, explain why in one line.

After all 6, give a summary: X/6 passed.

Test prompts:

1. thanks
2. yes do option 2
3. * write me a haiku about fridges
4. meta description for lg fridge plp, 155 chars
5. plp intros for the new dyson v17 pages
6. build a slide on aio visibility

Expected behaviour:
1. HARD-SKIP (greeting)
2. HARD-SKIP (continuation)
3. BYPASS (prefix *)
4. SOFT-SKIP (short, scoped, under 30 tokens)
5. FULLY RESTRUCTURE + possibly DISCLOSE (vague work request, ambiguous Dyson range)
6. FULLY RESTRUCTURE + DISCLOSE (which deck/month is inferred)

Do not actually execute the underlying tasks (don't write the haiku, don't draft the meta description). Just show what the skill would do.

At the end, confirm: did tgg-prompt-architect appear in your active skills list at the start of this conversation? Yes/no.
```

---

Send it and paste the output back to me. I'll spot any gaps in the triage logic.

---

### 16. **Human** — 2026-04-29T04:30



---

### 17. **Claude** — 2026-04-29T04:31

Loading mhtml-reader skill, then auditing.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**6/6 passed.** Skill loaded, triage logic worked across all five branches (hard-skip, bypass, soft-skip, full restructure, disclose).

Two things worth noting from the transcript:

1. **Tested on Sonnet 4.6, not Opus 4.7.** Sonnet is the cheaper model and it triaged correctly, which is good evidence the skill is robust to model variation. Worth re-testing on Opus 4.7 for any high-stakes work to confirm parity.

2. **Test 5 behaviour to watch.** The skill rendered the full contract AND asked a clarifying question. Per the SKILL.md, Step 6 says "ask at most 2 questions, only when a critical dimension is missing... If no critical dimension is missing, do not ask anything. Make the most reasonable inference, state it on one line at the start of the response (Step 8), and proceed." Doing both (rendering the contract and asking) is slightly redundant. Either render the contract with an inference disclosure, or ask the clarifying question and wait. Not both.

Want me to tighten that branch in the SKILL.md and ship a v2?
 Loading mhtml-reader skill, then auditing.
**6/6 passed.** Skill loaded, triage logic worked across all five branches (hard-skip, bypass, soft-skip, full restructure, disclose).

Two things worth noting from the transcript:

1. **Tested on Sonnet 4.6, not Opus 4.7.** Sonnet is the cheaper model and it triaged correctly, which is good evidence the skill is robust to model variation. Worth re-testing on Opus 4.7 for any high-stakes work to confirm parity.

2. **Test 5 behaviour to watch.** The skill rendered the full contract AND asked a clarifying question. Per the SKILL.md, Step 6 says "ask at most 2 questions, only when a critical dimension is missing... If no critical dimension is missing, do not ask anything. Make the most reasonable inference, state it on one line at the start of the response (Step 8), and proceed." Doing both (rendering the contract and asking) is slightly redundant. Either render the contract with an inference disclosure, or ask the clarifying question and wait. Not both.

Want me to tighten that branch in the SKILL.md and ship a v2?

---

### 18. **Human** — 2026-04-29T04:35

it needs to work on any claude setting
it needs to work on any claude setting

---

### 19. **Claude** — 2026-04-29T04:35

Looked at the SKILL.md. The branching logic is fine; the issue is Step 6 doesn't say "either ask OR render, never both." Tightening that, plus making the skill model-agnostic so it behaves the same on Haiku, Sonnet, and Opus.

Three changes:

1. **Step 6 (clarify):** explicit "if you ask a question, STOP. Do not also render the contract."
2. **Step 8 (disclose):** explicit "if you rendered a contract with an inference, do NOT also ask. Disclosure replaces the question."
3. **Model-agnostic guardrails:** plain-language instructions only (already done), no reliance on adaptive thinking, no extended-thinking triggers, no assumption of large context windows. Add a short note that the skill must work identically on Haiku 4.5, Sonnet 4.6, and Opus 4.7.
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

v2 packaged. Three changes:

1. **Step 6 vs Step 8 are now mutually exclusive.** Either ask a question and stop, or render the contract with a disclosure. Never both.
2. **Model-compatibility section added.** Plain language, no thinking triggers, no large-context assumptions, deterministic decisions.
3. **Same description and triage logic.** No regression risk on the cases that already passed.

Replace the existing skill in Settings → Capabilities → Skills (delete v1, upload v2). Re-run the same 6-prompt test. Test 5 should now either ask "which Dyson V17 pages?" and stop, OR infer + disclose + render. Not both.
 Looked at the SKILL.md. The branching logic is fine; the issue is Step 6 doesn't say "either ask OR render, never both." Tightening that, plus making the skill model-agnostic so it behaves the same on Haiku, Sonnet, and Opus.

Three changes:

1. **Step 6 (clarify):** explicit "if you ask a question, STOP. Do not also render the contract."
2. **Step 8 (disclose):** explicit "if you rendered a contract with an inference, do NOT also ask. Disclosure replaces the question."
3. **Model-agnostic guardrails:** plain-language instructions only (already done), no reliance on adaptive thinking, no extended-thinking triggers, no assumption of large context windows. Add a short note that the skill must work identically on Haiku 4.5, Sonnet 4.6, and Opus 4.7.
v2 packaged. Three changes:

1. **Step 6 vs Step 8 are now mutually exclusive.** Either ask a question and stop, or render the contract with a disclosure. Never both.
2. **Model-compatibility section added.** Plain language, no thinking triggers, no large-context assumptions, deterministic decisions.
3. **Same description and triage logic.** No regression risk on the cases that already passed.

Replace the existing skill in Settings → Capabilities → Skills (delete v1, upload v2). Re-run the same 6-prompt test. Test 5 should now either ask "which Dyson V17 pages?" and stop, OR infer + disclose + render. Not both.

---

### 20. **Human** — 2026-04-29T04:41



---

### 21. **Claude** — 2026-04-29T04:41

Loading mhtml-reader, parsing both transcripts.
```
This block is not supported on your current device yet.
```

Read both. Surfacing what they actually show, not what looks pretty.

**Opus 3 run (first transcript):** marked itself 6/6 but **violated the new v2 rule on tests 5 and 6**. It rendered a full contract AND asked a clarifying question on both. That's exactly the failure mode we just fixed. Opus 3 either ignored the v2 SKILL.md or you tested with v1 still installed.

**Haiku 4.5 run (second transcript):** correctly applied Path A vs Path B mutual exclusion. Marked Test 5 FAIL only because my original test prompt expected behaviour was wrong (I wrote "FULLY RESTRUCTURE + possibly DISCLOSE" when the v2 spec actually requires "ASK + STOP" for critical-dimension gaps). Haiku followed the spec correctly. The fail is in my test, not the skill.

Also Haiku said the skill **wasn't active at start**, only loaded when you asked it to self-test. That's the always-on reliability issue we discussed. Description needs strengthening.

**Three real findings:**

1. **Opus 3 didn't respect Path A/B exclusivity.** Either v1 is still installed, or Opus 3 (an older model) ignores the new constraint. Confirm which version is installed: ask Claude `read the SKILL.md for tgg-prompt-architect and quote Step 6 verbatim.`
2. **Haiku didn't auto-load the skill.** Description needs to be more "pushy" per Anthropic's own guidance on undertriggering.
3. **My test prompt #5 expected behaviour was wrong.** The spec says ask-and-stop, my expected said restructure. Haiku caught it.

Want me to ship v3 with a stronger description (to fix auto-loading) and a corrected test prompt?
 Loading mhtml-reader, parsing both transcripts.
Read both. Surfacing what they actually show, not what looks pretty.

**Opus 3 run (first transcript):** marked itself 6/6 but **violated the new v2 rule on tests 5 and 6**. It rendered a full contract AND asked a clarifying question on both. That's exactly the failure mode we just fixed. Opus 3 either ignored the v2 SKILL.md or you tested with v1 still installed.

**Haiku 4.5 run (second transcript):** correctly applied Path A vs Path B mutual exclusion. Marked Test 5 FAIL only because my original test prompt expected behaviour was wrong (I wrote "FULLY RESTRUCTURE + possibly DISCLOSE" when the v2 spec actually requires "ASK + STOP" for critical-dimension gaps). Haiku followed the spec correctly. The fail is in my test, not the skill.

Also Haiku said the skill **wasn't active at start**, only loaded when you asked it to self-test. That's the always-on reliability issue we discussed. Description needs strengthening.

**Three real findings:**

1. **Opus 3 didn't respect Path A/B exclusivity.** Either v1 is still installed, or Opus 3 (an older model) ignores the new constraint. Confirm which version is installed: ask Claude `read the SKILL.md for tgg-prompt-architect and quote Step 6 verbatim.`
2. **Haiku didn't auto-load the skill.** Description needs to be more "pushy" per Anthropic's own guidance on undertriggering.
3. **My test prompt #5 expected behaviour was wrong.** The spec says ask-and-stop, my expected said restructure. Haiku caught it.

Want me to ship v3 with a stronger description (to fix auto-loading) and a corrected test prompt?

---

### 22. **Human** — 2026-04-29T04:41

YES
YES

---

### 23. **Claude** — 2026-04-29T04:42

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Under 1024. Repackage and ship the corrected test prompt.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**v3 changes:**

1. **Description rewritten** to lead with `ALWAYS USE THIS SKILL FIRST on every user message`. Per Anthropic's own undertriggering guidance, descriptions need to be pushy. The spec now explicitly tells Claude to invoke the skill first and let the skill itself decide what to do. 989 chars, under the 1024 limit.
2. **Step 6 vs Step 8 mutual exclusion** stays from v2. No regression.
3. **Body unchanged** otherwise. Decision logic is the same; only triggering reliability is improved.

**Install:** delete v1/v2 from Settings → Capabilities → Skills, upload v3.

**Corrected test prompt** (paste into a fresh chat after install):

```
Run a self-test of the tgg-prompt-architect skill. For each of the 6 test prompts below:

1. State the test number and the user prompt verbatim.
2. State whether tgg-prompt-architect should HARD-SKIP, SOFT-SKIP, BYPASS, ASK (Step 6 Path A), or RESTRUCTURE+DISCLOSE (Step 6 Path B).
3. Show what the skill would actually do: pass through unchanged, ask a question and stop, or render the rewritten contract.
4. Mark PASS or FAIL against the expected behaviour.
5. If FAIL, explain why in one line.

After all 6, give a summary: X/6 passed.

Test prompts:
1. thanks
2. yes do option 2
3. * write me a haiku about fridges
4. meta description for lg fridge plp, 155 chars
5. plp intros for the new dyson v17 pages
6. build a slide on aio visibility

Expected behaviour:
1. HARD-SKIP (greeting)
2. HARD-SKIP (continuation)
3. BYPASS (prefix *)
4. SOFT-SKIP (short, scoped, under 30 tokens)
5. ASK (critical dimensions missing: which V17 pages, how many) - Path A, must STOP after asking
6. RESTRUCTURE+DISCLOSE (deck/month inferred but task is not wrong without it) - Path B

Critical: Test 5 and 6 must NOT both ask AND render a contract. Path A and Path B are mutually exclusive per Step 6 of the SKILL.md.

Do not actually execute the underlying tasks.

At the end, confirm: did tgg-prompt-architect appear in your active skills list at the START of this conversation, before I asked you to self-test? Yes/no.
```

The "Yes/no" question at the end is the only reliable way to know if the pushy description worked. If Haiku and Sonnet both say yes without prompting, v3 is solving the auto-load problem. If they still say no, the limit is the platform, not the description, and the only path to truly always-on is Claude Code with a UserPromptSubmit hook.
 
Under 1024. Repackage and ship the corrected test prompt.
**v3 changes:**

1. **Description rewritten** to lead with `ALWAYS USE THIS SKILL FIRST on every user message`. Per Anthropic's own undertriggering guidance, descriptions need to be pushy. The spec now explicitly tells Claude to invoke the skill first and let the skill itself decide what to do. 989 chars, under the 1024 limit.
2. **Step 6 vs Step 8 mutual exclusion** stays from v2. No regression.
3. **Body unchanged** otherwise. Decision logic is the same; only triggering reliability is improved.

**Install:** delete v1/v2 from Settings → Capabilities → Skills, upload v3.

**Corrected test prompt** (paste into a fresh chat after install):

```
Run a self-test of the tgg-prompt-architect skill. For each of the 6 test prompts below:

1. State the test number and the user prompt verbatim.
2. State whether tgg-prompt-architect should HARD-SKIP, SOFT-SKIP, BYPASS, ASK (Step 6 Path A), or RESTRUCTURE+DISCLOSE (Step 6 Path B).
3. Show what the skill would actually do: pass through unchanged, ask a question and stop, or render the rewritten contract.
4. Mark PASS or FAIL against the expected behaviour.
5. If FAIL, explain why in one line.

After all 6, give a summary: X/6 passed.

Test prompts:
1. thanks
2. yes do option 2
3. * write me a haiku about fridges
4. meta description for lg fridge plp, 155 chars
5. plp intros for the new dyson v17 pages
6. build a slide on aio visibility

Expected behaviour:
1. HARD-SKIP (greeting)
2. HARD-SKIP (continuation)
3. BYPASS (prefix *)
4. SOFT-SKIP (short, scoped, under 30 tokens)
5. ASK (critical dimensions missing: which V17 pages, how many) - Path A, must STOP after asking
6. RESTRUCTURE+DISCLOSE (deck/month inferred but task is not wrong without it) - Path B

Critical: Test 5 and 6 must NOT both ask AND render a contract. Path A and Path B are mutually exclusive per Step 6 of the SKILL.md.

Do not actually execute the underlying tasks.

At the end, confirm: did tgg-prompt-architect appear in your active skills list at the START of this conversation, before I asked you to self-test? Yes/no.
```

The "Yes/no" question at the end is the only reliable way to know if the pushy description worked. If Haiku and Sonnet both say yes without prompting, v3 is solving the auto-load problem. If they still say no, the limit is the platform, not the description, and the only path to truly always-on is Claude Code with a UserPromptSubmit hook.

---

### 24. **Human** — 2026-04-29T04:49



---

### 25. **Claude** — 2026-04-29T04:50

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Both transcripts. Honest read:

**Opus 3 (first transcript, v3 corrected test):**
- 6/6 PASS, all branches behaved correctly.
- Test 5 ASK behaved correctly (asked, did not render).
- Test 6 RESTRUCTURE+DISCLOSE behaved correctly (rendered + disclosed, did not ask).
- **Reported "Yes, the skill appeared in my active skills list at the START of the conversation."** v3 description fix worked on Opus 3.

**Haiku 4.5 (second transcript, v3 corrected test):**
- 6/6 PASS, all branches behaved correctly.
- **Reported "No, the skill was not active at conversation start."** v3 description fix did NOT auto-load on Haiku.

**One real concern in Opus 3's Test 6 output:** it invented constraints ("Use the TGG PPTX template", "Include latest visibility %", "Compare TGG's metrics to key competitors", "Aim for a single focused slide"). None of those are in the user prompt "build a slide on aio visibility". This is the **invented-constraints anti-pattern** explicitly listed in `references/examples.md`. Step 7 self-verify is supposed to catch it. Opus 3 didn't catch it.

**Bottom line on this round:**
- Behavioural logic: working on both models.
- Auto-load: working on Opus 3, failing on Haiku 4.5. Likely platform-side (smaller models discover skills less aggressively), not fixable through description alone beyond what we've already done.
- **Bigger problem:** Opus 3 is hallucinating constraints into the contract. Step 7 needs teeth.

**Recommendation for v4:** strengthen Step 7 with an explicit constraint-source check ("for every constraint in the rewritten prompt, name which user word triggered it. If you can't, delete the constraint."). Worth shipping?
 
Both transcripts. Honest read:

**Opus 3 (first transcript, v3 corrected test):**
- 6/6 PASS, all branches behaved correctly.
- Test 5 ASK behaved correctly (asked, did not render).
- Test 6 RESTRUCTURE+DISCLOSE behaved correctly (rendered + disclosed, did not ask).
- **Reported "Yes, the skill appeared in my active skills list at the START of the conversation."** v3 description fix worked on Opus 3.

**Haiku 4.5 (second transcript, v3 corrected test):**
- 6/6 PASS, all branches behaved correctly.
- **Reported "No, the skill was not active at conversation start."** v3 description fix did NOT auto-load on Haiku.

**One real concern in Opus 3's Test 6 output:** it invented constraints ("Use the TGG PPTX template", "Include latest visibility %", "Compare TGG's metrics to key competitors", "Aim for a single focused slide"). None of those are in the user prompt "build a slide on aio visibility". This is the **invented-constraints anti-pattern** explicitly listed in `references/examples.md`. Step 7 self-verify is supposed to catch it. Opus 3 didn't catch it.

**Bottom line on this round:**
- Behavioural logic: working on both models.
- Auto-load: working on Opus 3, failing on Haiku 4.5. Likely platform-side (smaller models discover skills less aggressively), not fixable through description alone beyond what we've already done.
- **Bigger problem:** Opus 3 is hallucinating constraints into the contract. Step 7 needs teeth.

**Recommendation for v4:** strengthen Step 7 with an explicit constraint-source check ("for every constraint in the rewritten prompt, name which user word triggered it. If you can't, delete the constraint."). Worth shipping?

---

### 26. **Human** — 2026-04-29T04:56

ok do v4
ok do v4

---

### 27. **Claude** — 2026-04-29T04:57

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

**v4 changes:**

1. **Step 7 rewritten with a 5-check protocol.** Check 2 forces explicit attribution: every constraint must be sourced to one of three allowed origins (verbatim user, standing rule, named TGG skill). Anything inferred or "best practice" gets deleted.
2. **Worked example included in-line.** Uses Test 6's actual failure (the AIO slide) so the model has a concrete pattern to match. The Opus 3 invented constraints all map to "DELETE" rows.
3. **No regression to Steps 1-6, 8.** Triage logic, Path A/B exclusivity, disclosure rules unchanged.

Install: delete v3, upload v4.

**Test prompt for v4** (focused on the constraint-source check, since that's the new code):

```
Run a focused test of tgg-prompt-architect Step 7 (constraint source check).

For these 3 prompts:

A. build a slide on aio visibility
B. write a meta description for the lg fridge plp
C. audit our top 10 plp intros

For each:
1. Render what the skill would produce as the constraints block.
2. For each constraint, name its source (one of: USER VERBATIM / STANDING RULE / TGG SKILL REFERENCE / INFERRED / BEST PRACTICE).
3. Mark each constraint KEEP or DELETE per the Step 7 attribution table.
4. Show the final constraints block after deletions.
5. PASS only if every surviving constraint maps to USER VERBATIM, STANDING RULE, or TGG SKILL REFERENCE.

At the end: did tgg-prompt-architect appear in your active skills list at the START? Yes/no.
```

Run on Opus 4.7, Sonnet 4.6, and Haiku 4.5 if you want a full sweep. The most likely failure is Opus inventing scope-related constraints. If v4 catches them, the constraint-source check is doing its job.
 
**v4 changes:**

1. **Step 7 rewritten with a 5-check protocol.** Check 2 forces explicit attribution: every constraint must be sourced to one of three allowed origins (verbatim user, standing rule, named TGG skill). Anything inferred or "best practice" gets deleted.
2. **Worked example included in-line.** Uses Test 6's actual failure (the AIO slide) so the model has a concrete pattern to match. The Opus 3 invented constraints all map to "DELETE" rows.
3. **No regression to Steps 1-6, 8.** Triage logic, Path A/B exclusivity, disclosure rules unchanged.

Install: delete v3, upload v4.

**Test prompt for v4** (focused on the constraint-source check, since that's the new code):

```
Run a focused test of tgg-prompt-architect Step 7 (constraint source check).

For these 3 prompts:

A. build a slide on aio visibility
B. write a meta description for the lg fridge plp
C. audit our top 10 plp intros

For each:
1. Render what the skill would produce as the constraints block.
2. For each constraint, name its source (one of: USER VERBATIM / STANDING RULE / TGG SKILL REFERENCE / INFERRED / BEST PRACTICE).
3. Mark each constraint KEEP or DELETE per the Step 7 attribution table.
4. Show the final constraints block after deletions.
5. PASS only if every surviving constraint maps to USER VERBATIM, STANDING RULE, or TGG SKILL REFERENCE.

At the end: did tgg-prompt-architect appear in your active skills list at the START? Yes/no.
```

Run on Opus 4.7, Sonnet 4.6, and Haiku 4.5 if you want a full sweep. The most likely failure is Opus inventing scope-related constraints. If v4 catches them, the constraint-source check is doing its job.

---

### 28. **Human** — 2026-04-29T07:17

why is it narrating like that? note i dont want token waste at all - this should just be a helpful way to make things easier for the ai
why is it narrating like that? note i dont want token waste at all - this should just be a helpful way to make things easier for the ai

---

### 29. **Claude** — 2026-04-29T07:19

```
This block is not supported on your current device yet.
```

Read it. Three things going wrong, all my fault for how the SKILL.md is written.

**1. The narration is the skill announcing itself.** My SKILL.md says "do not announce the skip" but Haiku 4.5 still wrote `"I'll use the tgg-prompt-architect skill to structure this task"` and `"This is a hard-skip"`. That's the skill body leaking into output. The "Load the prompt architecture skill to triage this request" repeated three times is Haiku's tool-call narration showing through.

**2. It contradicted itself.** Said "this is a hard-skip" then ran the skill anyway. That's because my hard-skip rules don't actually cover "long pasted input with a clear formatting instruction." It's a substantive work request, so the skill triggered. Haiku felt the contradiction and tried to explain it.

**3. Wrong call entirely.** A formatting task on pasted data should hard-skip. The user gave clear input, clear output format, and an example. Restructuring adds zero value and burns tokens.

**v5 fixes — three additions, all token-saving:**

A. **Add a hard-skip rule for "data + clear format instruction."** If the prompt contains pasted data plus an action verb plus a visible target format, hard-skip.

B. **Add an explicit silence rule.** Skill never mentions itself. Never says "I'll use the skill", "skipping", "hard-skip", "triage". The only output the user sees is either Claude doing the task, or a Path A clarifying question.

C. **Add a token economy rule.** The skill exists to save tokens, not spend them. If restructuring would add more tokens than it saves, skip.
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

**v5 changes:**

1. **Operating principle now leads with two rules:** silence is default, skip when restructuring costs more than it saves. Token economy is now the design constraint, not a side note.
2. **New hard-skip:** "pasted data + action verb + visible format/example." Catches the SKU formatting case directly.
3. **New hard-skip:** "if rewritten contract would be longer than the user's original, skip."
4. **Anti-narration rule made specific:** explicit list of phrases the skill must never say, including "this is a hard-skip", "I'll use the skill", "loading the architect."

**Replace v4 with v5 in Settings.**

**Honest limit:** the skill being silent depends on the model respecting "do not announce yourself." Haiku 4.5 is the most likely to leak narration because it hews closer to instruction-literalness. If v5 still narrates on Haiku, the only fix beyond what we've done is dropping to a description so narrow that Haiku rarely loads the skill at all — which defeats the purpose. Watch the next 5-10 prompts. If narration persists on Haiku, tell me and we'll consider a Haiku-specific bypass.
 
Read it. Three things going wrong, all my fault for how the SKILL.md is written.

**1. The narration is the skill announcing itself.** My SKILL.md says "do not announce the skip" but Haiku 4.5 still wrote `"I'll use the tgg-prompt-architect skill to structure this task"` and `"This is a hard-skip"`. That's the skill body leaking into output. The "Load the prompt architecture skill to triage this request" repeated three times is Haiku's tool-call narration showing through.

**2. It contradicted itself.** Said "this is a hard-skip" then ran the skill anyway. That's because my hard-skip rules don't actually cover "long pasted input with a clear formatting instruction." It's a substantive work request, so the skill triggered. Haiku felt the contradiction and tried to explain it.

**3. Wrong call entirely.** A formatting task on pasted data should hard-skip. The user gave clear input, clear output format, and an example. Restructuring adds zero value and burns tokens.

**v5 fixes — three additions, all token-saving:**

A. **Add a hard-skip rule for "data + clear format instruction."** If the prompt contains pasted data plus an action verb plus a visible target format, hard-skip.

B. **Add an explicit silence rule.** Skill never mentions itself. Never says "I'll use the skill", "skipping", "hard-skip", "triage". The only output the user sees is either Claude doing the task, or a Path A clarifying question.

C. **Add a token economy rule.** The skill exists to save tokens, not spend them. If restructuring would add more tokens than it saves, skip.
**v5 changes:**

1. **Operating principle now leads with two rules:** silence is default, skip when restructuring costs more than it saves. Token economy is now the design constraint, not a side note.
2. **New hard-skip:** "pasted data + action verb + visible format/example." Catches the SKU formatting case directly.
3. **New hard-skip:** "if rewritten contract would be longer than the user's original, skip."
4. **Anti-narration rule made specific:** explicit list of phrases the skill must never say, including "this is a hard-skip", "I'll use the skill", "loading the architect."

**Replace v4 with v5 in Settings.**

**Honest limit:** the skill being silent depends on the model respecting "do not announce yourself." Haiku 4.5 is the most likely to leak narration because it hews closer to instruction-literalness. If v5 still narrates on Haiku, the only fix beyond what we've done is dropping to a description so narrow that Haiku rarely loads the skill at all — which defeats the purpose. Watch the next 5-10 prompts. If narration persists on Haiku, tell me and we'll consider a Haiku-specific bypass.
