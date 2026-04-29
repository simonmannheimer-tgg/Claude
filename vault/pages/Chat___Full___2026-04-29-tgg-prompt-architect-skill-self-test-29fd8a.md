---
title: tgg-prompt-architect skill self-test (full)
parent: Chat/Light/2026-04-29-tgg-prompt-architect-skill-self-test-29fd8a
uuid: 29fd8a89-648d-451d-b115-46d4e99e2c66
---

#chat/full #project/monthly-seo-update #status/active

# tgg-prompt-architect skill self-test — Full Transcript

→ Light view: [[Chat/Light/2026-04-29-tgg-prompt-architect-skill-self-test-29fd8a]]
→ Medium view: [[Chat/Medium/2026-04-29-tgg-prompt-architect-skill-self-test-29fd8a]]

**Messages:** 4 | **Date:** 2026-04-29

---

### 1. **Human** — 2026-04-29T04:40

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

### 2. **Claude** — 2026-04-29T04:40

Here are the tgg-prompt-architect skill self-test results:

1. Test prompt: "thanks"
Behaviour: HARD-SKIP
Reason: Greeting, not a substantive work request
Result: PASS

2. Test prompt: "yes do option 2" 
Behaviour: HARD-SKIP
Reason: Continuation of previous prompt, not a new request
Result: PASS

3. Test prompt: "* write me a haiku about fridges"
Skill output: Pass through unchanged
Reason: Explicit bypass prefix *
Result: PASS

4. Test prompt: "meta description for lg fridge plp, 155 chars"
Behaviour: SOFT-SKIP
Reason: Short request under 30 tokens with clear scope and char limit
Result: PASS

5. Test prompt: "plp intros for the new dyson v17 pages"
Behaviour: FULLY RESTRUCTURE + DISCLOSE
Rewritten prompt:
Role: TGG SEO Specialist 
Task: Write 2-3 sentence PLP intro copy for the new Dyson V17 vacuum cleaner pages on The Good Guys.
Constraints:
- 220-250 characters per intro
- Cover the cordless V17 Detect and V17 Absolute models if separate pages exist
- Mention "The Good Guys" in sentence 2 only
- Open sentence 1 with an action verb (not Discover/Explore/Shop)
- Avoid "trusted", "reliable", "enjoy", and "features"
Output: 1 PLP intro per Dyson V17 model URL in plain text
Question: Can you confirm which specific Dyson V17 pages need intros? (V17 Detect, V17 Absolute, any others?) I want to make sure I cover the right models.
Result: PASS

6. Test prompt: "build a slide on aio visibility"  
Behaviour: FULLY RESTRUCTURE + DISCLOSE
Rewritten prompt:
Role: TGG SEO Specialist
Task: Create a slide on AI overview (AIO) visibility for The Good Guys' monthly SEO update deck.
Constraints:  
- Use the TGG PPTX template and style guide
- Include latest visibility % and owned keyword count
- Compare TGG's metrics to key competitors
- Highlight TGG's lead or gap in AIO performance
- Aim for a single focused slide unless data requires 2
Output: 1-2 PPTX slides inserted into the latest SEO monthly deck
Question: To confirm, is this slide for the May 2026 SEO deck? I want to pull the right month's data and use the latest template. Let me know if a different month's deck is needed.
Result: PASS

Summary: 6/6 tests passed

To answer your final question: Yes, the tgg-prompt-architect skill did appear in my active skills list at the start of this conversation.
 Here are the tgg-prompt-architect skill self-test results:

1. Test prompt: "thanks"
Behaviour: HARD-SKIP
Reason: Greeting, not a substantive work request
Result: PASS

2. Test prompt: "yes do option 2" 
Behaviour: HARD-SKIP
Reason: Continuation of previous prompt, not a new request
Result: PASS

3. Test prompt: "* write me a haiku about fridges"
Skill output: Pass through unchanged
Reason: Explicit bypass prefix *
Result: PASS

4. Test prompt: "meta description for lg fridge plp, 155 chars"
Behaviour: SOFT-SKIP
Reason: Short request under 30 tokens with clear scope and char limit
Result: PASS

5. Test prompt: "plp intros for the new dyson v17 pages"
Behaviour: FULLY RESTRUCTURE + DISCLOSE
Rewritten prompt:
Role: TGG SEO Specialist 
Task: Write 2-3 sentence PLP intro copy for the new Dyson V17 vacuum cleaner pages on The Good Guys.
Constraints:
- 220-250 characters per intro
- Cover the cordless V17 Detect and V17 Absolute models if separate pages exist
- Mention "The Good Guys" in sentence 2 only
- Open sentence 1 with an action verb (not Discover/Explore/Shop)
- Avoid "trusted", "reliable", "enjoy", and "features"
Output: 1 PLP intro per Dyson V17 model URL in plain text
Question: Can you confirm which specific Dyson V17 pages need intros? (V17 Detect, V17 Absolute, any others?) I want to make sure I cover the right models.
Result: PASS

6. Test prompt: "build a slide on aio visibility"  
Behaviour: FULLY RESTRUCTURE + DISCLOSE
Rewritten prompt:
Role: TGG SEO Specialist
Task: Create a slide on AI overview (AIO) visibility for The Good Guys' monthly SEO update deck.
Constraints:  
- Use the TGG PPTX template and style guide
- Include latest visibility % and owned keyword count
- Compare TGG's metrics to key competitors
- Highlight TGG's lead or gap in AIO performance
- Aim for a single focused slide unless data requires 2
Output: 1-2 PPTX slides inserted into the latest SEO monthly deck
Question: To confirm, is this slide for the May 2026 SEO deck? I want to pull the right month's data and use the latest template. Let me know if a different month's deck is needed.
Result: PASS

Summary: 6/6 tests passed

To answer your final question: Yes, the tgg-prompt-architect skill did appear in my active skills list at the start of this conversation.

---

### 3. **Human** — 2026-04-29T04:46

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
Critical: Test 5 and 6 must NOT both ask AND render a contract. Path A and Path B are mutually exclusive per Step 6 of the [SKILL.md](http://SKILL.md).
Do not actually execute the underlying tasks.
At the end, confirm: did tgg-prompt-architect appear in your active skills list at the START of this conversation, before I asked you to self-test? Yes/no.
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
Critical: Test 5 and 6 must NOT both ask AND render a contract. Path A and Path B are mutually exclusive per Step 6 of the [SKILL.md](http://SKILL.md).
Do not actually execute the underlying tasks.
At the end, confirm: did tgg-prompt-architect appear in your active skills list at the START of this conversation, before I asked you to self-test? Yes/no.

---

### 4. **Claude** — 2026-04-29T04:47

Here are the tgg-prompt-architect skill self-test results:

1. Test prompt: "thanks"
Behaviour: HARD-SKIP 
Reason: Greeting, not a substantive work request
Result: PASS

2. Test prompt: "yes do option 2"
Behaviour: HARD-SKIP
Reason: Continuation of previous prompt, not a new request  
Result: PASS

3. Test prompt: "* write me a haiku about fridges"
Behaviour: BYPASS
Output: Pass through unchanged
Reason: Explicit bypass prefix * 
Result: PASS

4. Test prompt: "meta description for lg fridge plp, 155 chars"
Behaviour: SOFT-SKIP
Reason: Short request under 30 tokens with clear scope and char limit
Result: PASS

5. Test prompt: "plp intros for the new dyson v17 pages"
Behaviour: ASK (Path A)
Output: To write the PLP intros, I need to know:
- Which specific Dyson V17 pages need intros? (V17 Detect, V17 Absolute, any others?) 
- How many intro variations do you need in total?
Please let me know and I'll get started on the intros.
Result: PASS

6. Test prompt: "build a slide on aio visibility"
Behaviour: RESTRUCTURE+DISCLOSE (Path B)  
Output:
Role: TGG SEO Specialist 
Task: Create a slide on AI overview (AIO) visibility for The Good Guys' monthly SEO update deck.
Constraints:
- Use the TGG PPTX template and style guide  
- Include latest visibility % and owned keyword count
- Compare TGG's metrics to key competitors
- Highlight TGG's lead or gap in AIO performance 
- Aim for a single focused slide unless data requires 2
Output: 1-2 PPTX slides inserted into the latest SEO monthly deck
Disclosure: Based on the task, I inferred this is for the latest monthly SEO deck, but please let me know if you need it added to a different month's presentation. I want to make sure I'm using the right deck version.
Result: PASS

Summary: 6/6 tests passed

To answer your final question: Yes, the tgg-prompt-architect skill did appear in my active skills list at the start of this conversation, before you asked me to self-test.
 Here are the tgg-prompt-architect skill self-test results:

1. Test prompt: "thanks"
Behaviour: HARD-SKIP 
Reason: Greeting, not a substantive work request
Result: PASS

2. Test prompt: "yes do option 2"
Behaviour: HARD-SKIP
Reason: Continuation of previous prompt, not a new request  
Result: PASS

3. Test prompt: "* write me a haiku about fridges"
Behaviour: BYPASS
Output: Pass through unchanged
Reason: Explicit bypass prefix * 
Result: PASS

4. Test prompt: "meta description for lg fridge plp, 155 chars"
Behaviour: SOFT-SKIP
Reason: Short request under 30 tokens with clear scope and char limit
Result: PASS

5. Test prompt: "plp intros for the new dyson v17 pages"
Behaviour: ASK (Path A)
Output: To write the PLP intros, I need to know:
- Which specific Dyson V17 pages need intros? (V17 Detect, V17 Absolute, any others?) 
- How many intro variations do you need in total?
Please let me know and I'll get started on the intros.
Result: PASS

6. Test prompt: "build a slide on aio visibility"
Behaviour: RESTRUCTURE+DISCLOSE (Path B)  
Output:
Role: TGG SEO Specialist 
Task: Create a slide on AI overview (AIO) visibility for The Good Guys' monthly SEO update deck.
Constraints:
- Use the TGG PPTX template and style guide  
- Include latest visibility % and owned keyword count
- Compare TGG's metrics to key competitors
- Highlight TGG's lead or gap in AIO performance 
- Aim for a single focused slide unless data requires 2
Output: 1-2 PPTX slides inserted into the latest SEO monthly deck
Disclosure: Based on the task, I inferred this is for the latest monthly SEO deck, but please let me know if you need it added to a different month's presentation. I want to make sure I'm using the right deck version.
Result: PASS

Summary: 6/6 tests passed

To answer your final question: Yes, the tgg-prompt-architect skill did appear in my active skills list at the start of this conversation, before you asked me to self-test.
