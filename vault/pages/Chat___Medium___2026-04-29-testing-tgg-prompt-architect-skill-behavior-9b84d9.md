---
title: Testing tgg-prompt-architect skill behavior (medium)
parent: Chat/Light/2026-04-29-testing-tgg-prompt-architect-skill-behavior-9b84d9
uuid: 9b84d9bc-75bc-4ae2-85d7-add55cfad4bc
---

#chat/medium #project/main #status/active

# Testing tgg-prompt-architect skill behavior — Key User Messages

→ Light view: [[Chat/Light/2026-04-29-testing-tgg-prompt-architect-skill-behavior-9b84d9]]
→ Full transcript: [[Chat/Full/2026-04-29-testing-tgg-prompt-architect-skill-behavior-9b84d9]]

**Total user messages:** 2

---

### Message 1 — 2026-04-29T04:40

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
2. State whether tgg-prompt-architect should HARD-SKIP, SOFT-SKIP (m

[truncated — see full transcript]

### Message 2 — 2026-04-29T04:46

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
Run a self-test of the tgg-prompt-architect skill. For each of the 6 test prompt

[truncated — see full transcript]
