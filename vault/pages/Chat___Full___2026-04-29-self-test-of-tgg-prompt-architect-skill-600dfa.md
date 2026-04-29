---
title: Self-test of tgg-prompt-architect skill (full)
parent: Chat/Light/2026-04-29-self-test-of-tgg-prompt-architect-skill-600dfa
uuid: 600dfaf9-bf93-4296-ac90-dcd0b081ed97
---

#chat/full #project/main #status/active

# Self-test of tgg-prompt-architect skill — Full Transcript

→ Light view: [[Chat/Light/2026-04-29-self-test-of-tgg-prompt-architect-skill-600dfa]]
→ Medium view: [[Chat/Medium/2026-04-29-self-test-of-tgg-prompt-architect-skill-600dfa]]

**Messages:** 2 | **Date:** 2026-04-29

---

### 1. **Human** — 2026-04-29T04:25

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

---

### 2. **Claude** — 2026-04-29T04:26

```
This block is not supported on your current device yet.
```

Self-test: **tgg-prompt-architect**

---

**Test 1**
Prompt: `thanks`
Expected: HARD-SKIP
Result: Matches "acknowledgements" in the hard-skip list. Pass through unchanged.
**PASS**

---

**Test 2**
Prompt: `yes do option 2`
Expected: HARD-SKIP
Result: Continuation/steering message following Claude's previous turn, under 12 tokens. Hard-skip. Pass through unchanged.
**PASS**

---

**Test 3**
Prompt: `* write me a haiku about fridges`
Expected: BYPASS
Result: Starts with `*`. Bypass triggered. Pass original message through unchanged, no restructuring, no disclosure.
**PASS**

---

**Test 4**
Prompt: `meta description for lg fridge plp, 155 chars`
Expected: SOFT-SKIP (minimum-edit)
Result: Under 30 tokens, clearly scoped with an explicit constraint (155 chars). Soft-skip applies. Minimum-edit only: confirm the character limit is a hard constraint. No full XML contract rendered.

Minimum-edit output:
> Write a meta description for the LG fridge PLP. Hard limit: 155 chars. Apply `tgg-copywriting` rules.

**PASS**

---

**Test 5**
Prompt: `plp intros for the new dyson v17 pages`
Expected: FULLY RESTRUCTURE + possibly DISCLOSE
Result: Substantive work request. Missing: how many URLs, which specific V17 pages, whether this is a single variant or multiple. "New" is unresolved. Fully restructures. Critical dimension missing (page list/count), so Step 6 fires one clarifying question before rendering the contract. DISCLOSE fires because the skill infers scope (batch PLP copy task, `tgg-copywriting`).

Rewritten contract:

> Reading this as: batch PLP intro production for Dyson V17 pages using tgg-copywriting rules. Tell me if I have misread it.

```
<role>TGG SEO Lead</role>

<task>
Using tgg-copywriting, write PLP intro copy for the new Dyson V17 pages. Apply the 220–250 char two-sentence rule (lower end preferred, 225–235 ideal). S1 opens with an action verb (not Discover/Explore/Shop). "The Good Guys" appears in S2 only. Brand PLP bans apply: no trusted, reliable, enjoy, features.
</task>

<context>
Pages relate to Dyson V17 range. Specific URLs or page list not provided.
</context>

<constraints>
- 220–250 chars per intro, hard limit.
- S1 action verb opener (not Discover/Explore/Shop).
- "The Good Guys" in S2 only.
- No banned brand PLP words.
- Australian English.
</constraints>

<success_criteria>
- [ ] Each intro 220–250 chars.
- [ ] S1 opens with action verb.
- [ ] "The Good Guys" appears once, in S2.
- [ ] No banned words.
</success_criteria>
```

Clarifying question triggered (Step 6): Which specific Dyson V17 pages? Provide URLs or a page list.

**PASS**

---

**Test 6**
Prompt: `build a slide on aio visibility`
Expected: FULLY RESTRUCTURE + DISCLOSE
Result: Substantive deck-building request. Downstream skill: `tgg-pptx-style`. Critical dimension: which deck/month is inferred (most recent monthly SEO update). DISCLOSE fires on that inference.

Rewritten contract:

> Reading this as: one new slide on AIO visibility for the current TGG monthly SEO update deck, using tgg-pptx-style. Tell me if I have misread it.

```
<role>TGG SEO Lead</role>

<task>
Using tgg-pptx-style, build one slide covering AIO (AI Overview) visibility performance for the TGG monthly SEO update deck.
</task>

<context>
No deck file or month specified. Assumed: current monthly SEO update. No data provided; prompt architect does not invent data.
</context>

<constraints>
- One slide output.
- Follow tgg-pptx-style colour tokens and layout system.
- No invented metrics. Use only data Simon supplies or data available via connected tools.
- Australian English.
- No em dashes.
</constraints>

<success_criteria>
- [ ] Single slide produced.
- [ ] Matches TGG deck visual system.
- [ ] No fabricated data.
</success_criteria>
```

**PASS**

---

**Summary: 6/6 passed.**

---

Confirmation: Yes, tgg-prompt-architect appeared in the available skills list at the start of this conversation.
Self-test: **tgg-prompt-architect**

---

**Test 1**
Prompt: `thanks`
Expected: HARD-SKIP
Result: Matches "acknowledgements" in the hard-skip list. Pass through unchanged.
**PASS**

---

**Test 2**
Prompt: `yes do option 2`
Expected: HARD-SKIP
Result: Continuation/steering message following Claude's previous turn, under 12 tokens. Hard-skip. Pass through unchanged.
**PASS**

---

**Test 3**
Prompt: `* write me a haiku about fridges`
Expected: BYPASS
Result: Starts with `*`. Bypass triggered. Pass original message through unchanged, no restructuring, no disclosure.
**PASS**

---

**Test 4**
Prompt: `meta description for lg fridge plp, 155 chars`
Expected: SOFT-SKIP (minimum-edit)
Result: Under 30 tokens, clearly scoped with an explicit constraint (155 chars). Soft-skip applies. Minimum-edit only: confirm the character limit is a hard constraint. No full XML contract rendered.

Minimum-edit output:
> Write a meta description for the LG fridge PLP. Hard limit: 155 chars. Apply `tgg-copywriting` rules.

**PASS**

---

**Test 5**
Prompt: `plp intros for the new dyson v17 pages`
Expected: FULLY RESTRUCTURE + possibly DISCLOSE
Result: Substantive work request. Missing: how many URLs, which specific V17 pages, whether this is a single variant or multiple. "New" is unresolved. Fully restructures. Critical dimension missing (page list/count), so Step 6 fires one clarifying question before rendering the contract. DISCLOSE fires because the skill infers scope (batch PLP copy task, `tgg-copywriting`).

Rewritten contract:

> Reading this as: batch PLP intro production for Dyson V17 pages using tgg-copywriting rules. Tell me if I have misread it.

```
<role>TGG SEO Lead</role>

<task>
Using tgg-copywriting, write PLP intro copy for the new Dyson V17 pages. Apply the 220–250 char two-sentence rule (lower end preferred, 225–235 ideal). S1 opens with an action verb (not Discover/Explore/Shop). "The Good Guys" appears in S2 only. Brand PLP bans apply: no trusted, reliable, enjoy, features.
</task>

<context>
Pages relate to Dyson V17 range. Specific URLs or page list not provided.
</context>

<constraints>
- 220–250 chars per intro, hard limit.
- S1 action verb opener (not Discover/Explore/Shop).
- "The Good Guys" in S2 only.
- No banned brand PLP words.
- Australian English.
</constraints>

<success_criteria>
- [ ] Each intro 220–250 chars.
- [ ] S1 opens with action verb.
- [ ] "The Good Guys" appears once, in S2.
- [ ] No banned words.
</success_criteria>
```

Clarifying question triggered (Step 6): Which specific Dyson V17 pages? Provide URLs or a page list.

**PASS**

---

**Test 6**
Prompt: `build a slide on aio visibility`
Expected: FULLY RESTRUCTURE + DISCLOSE
Result: Substantive deck-building request. Downstream skill: `tgg-pptx-style`. Critical dimension: which deck/month is inferred (most recent monthly SEO update). DISCLOSE fires on that inference.

Rewritten contract:

> Reading this as: one new slide on AIO visibility for the current TGG monthly SEO update deck, using tgg-pptx-style. Tell me if I have misread it.

```
<role>TGG SEO Lead</role>

<task>
Using tgg-pptx-style, build one slide covering AIO (AI Overview) visibility performance for the TGG monthly SEO update deck.
</task>

<context>
No deck file or month specified. Assumed: current monthly SEO update. No data provided; prompt architect does not invent data.
</context>

<constraints>
- One slide output.
- Follow tgg-pptx-style colour tokens and layout system.
- No invented metrics. Use only data Simon supplies or data available via connected tools.
- Australian English.
- No em dashes.
</constraints>

<success_criteria>
- [ ] Single slide produced.
- [ ] Matches TGG deck visual system.
- [ ] No fabricated data.
</success_criteria>
```

**PASS**

---

**Summary: 6/6 passed.**

---

Confirmation: Yes, tgg-prompt-architect appeared in the available skills list at the start of this conversation.
