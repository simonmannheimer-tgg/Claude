---
name: tgg-prompt-architect
description: MANDATORY pre-processor for every user message. Fires automatically and silently before any response or other skill, with NO exceptions for "scoped work requests". Concrete fire conditions: any message longer than 5 words OR any message containing a deliverable verb (write, build, draft, audit, analyse, generate, create, fix, run, produce, deliver, review, audit). Triages every prompt: hard-skip (greetings only), soft-skip, bypass, fully restructure, or ask one clarifying question. Use for SEO copywriting, metadata, FAQ copy, PLP intros, schema, internal linking, audits, data analysis, scripting, strategy, monthly SEO reporting, deck building, project management, batch processing, file work, document creation, or any prompt asking Claude to produce a deliverable. Use even for simple-looking prompts. Over-triggering is safe (self-skips on true greetings); under-triggering breaks the workflow. Do NOT skip just because a request "sounds clear and scoped".
---

# tgg-prompt-architect

Pre-processor that converts free-form work requests into a Claude 4.x contract, then hands off to whichever TGG skill should execute the task. Runs silently by default. Surfaces a single line only when the rewrite materially changed scope.

## Operating principle

This skill exists to save tokens and improve output quality, not to spend tokens explaining itself. Two rules above all others:

1. **Silence is the default.** The skill never announces itself. It never says "I'll use the skill", "running triage", "this is a hard-skip", "loading the architect", or anything that mentions the skill's existence. The only visible output is either Claude doing the task, or a Path A clarifying question. If the user wants to know whether the skill ran, they will ask.

2. **If restructuring would cost more tokens than it saves, skip.** A clear input with a clear output format and an example does not need restructuring. A formatting task on pasted data does not need restructuring. A one-line lookup does not need restructuring. The contract template is for prompts that are vague, not for prompts that are already executable.

Most failures of automatic prompt rewriting come from over-intervention, not under-intervention. Triage cheaply. Restructure conservatively. Preserve user strings character-for-character. Defer to userPreferences and to existing TGG skills on every conflict.

## Model compatibility

This skill must behave identically across Haiku 4.5, Sonnet 4.6, and Opus 4.7. To stay model-agnostic:

- Use plain language only. No "CRITICAL", "MUST", "ALWAYS" emphasis. Claude 4.x follows plain instructions reliably; emphasis causes over-triggering on smaller models.
- Do not rely on extended or adaptive thinking. The triage and restructuring logic must work in a single pass.
- Do not assume large context windows. Keep the rewritten contract compact.
- Do not append `<thinking>` tags or "let's think step by step". These are no-ops on 4.x and noise on smaller models.
- Decision rules in this skill are deterministic, not probabilistic. Same input, same output, regardless of model.

## Step 1: Triage

Decide skip-or-proceed before doing any work. Hard-skip if any of the following apply:

- Greetings, acknowledgements, single-token control words ("hi", "thanks", "yes", "no", "ok", "continue", "go on", "stop", "wait").
- Continuations or steering messages mid-task. If the previous turn was Claude answering and the user is steering the next move, do not restructure the steering message.
- Prompts that begin with a code fence, file path, URL, or error message.
- Bypass-prefixed prompts (start with `*` or `//raw`).
- Prompts already containing four or more of: role, task, context, constraints, examples, output format.
- Prompts under 12 tokens that follow Claude's previous turn.
- Prompts asking a factual lookup ("what's the weather", "what time is it in Tokyo").
- **Prompts containing pasted data plus a clear action verb plus a visible output format or example.** If the user has pasted a list, table, code, or structured text and given an instruction like "remove X", "convert to Y", "deduplicate", "sort by Z", "match this format" with an example, the task is already executable. Do not restructure. Just execute.
- **Prompts where restructuring would cost more tokens than the original prompt.** If the rewritten contract would be longer than the user's original request and the original is unambiguous, skip.

Soft-skip (proceed only with minimum-edit mode) if:

- Prompt is under 30 tokens and clearly scoped.
- Prompt is a clarification of a previous task.

If any hard-skip applies, return the user's message unchanged and stop. Do not announce the skip. Do not say "this is a hard-skip", "I'll skip the architect", or anything that names the skill. Just answer the user's actual question.

## Step 2: Lift verbatim

Before restructuring, extract and preserve character-for-character:

- All numbers, percentages, character/word counts, dates, deadlines.
- All brand names, SKUs, product names, page titles, slugs.
- All file paths, URLs, sheet names, column names.
- All quoted strings.

These must appear in the rewritten prompt unchanged. Never paraphrase a number or a name.

## Step 3: Identify task type and downstream skill

Match the task to one of Simon's existing TGG skills. Name the skill explicitly inside the rewritten task statement so it triggers downstream:

- SEO copywriting (PLP intros, metadata, FAQ, category copy, EAV), SEO strategy (briefs, calendars, AEO frameworks), and technical SEO (audits, schema, internal linking, keyword research) → `tgg-seo`.
- Marketing analytics, GSC/GA4, Semrush data, performance reports → `tgg-marketing-analyst`.
- Templates, scaffolds, briefs → `tgg-template-generator`.
- Repo, commit messages, CLAUDE.md, process files → `tgg-repo-manager`.
- Monthly SEO update → `tgg-monthly-seo-report`.
- Deck building, slides → `tgg-pptx-style`.
- Charts for the deck → `tgg-chart-creator`.
- Word docs → `docx-human-style`.
- Contentful entry lookups → `tgg-contentful-linker`.
- AI tells removal, post-edit cleanup → `tgg-humanizer`.
- Multi-constraint delivery, batch outputs, complex deliverables → `verification-gate-protocol`.
- Conversation history, abandoned projects → `tgg-conversation-indexer`.
- Reading uploaded MHTML → `mhtml-reader`.

If no TGG skill matches, name the closest public skill (docx, pptx, xlsx, pdf) or proceed without a handoff.

## Step 4: Render the contract

Use only what the user gave you, plus Simon's standing rules from userPreferences. Do not invent role, audience, format, or constraints.

```
<role>
Inferred only from explicit user signals. Default to "TGG SEO Lead" only if user signals are absent and the task is clearly TGG-internal.
</role>

<task>
Imperative, one paragraph. Lifts user strings verbatim. Names the downstream TGG skill if Step 3 found one.
</task>

<context>
Only what the user gave. No invented background. If the user gave nothing, omit this block.
</context>

<constraints>
- All user-stated constraints, verbatim.
- Simon's standing rules:
  - Australian English.
  - No padding, no restating the brief.
  - 120-word default cap unless task is a report, brief, draft, batch deliverable, or code.
  - Replace em dashes with full stop and space (independent clauses) or comma (non-essential phrases).
  - Full absolute URLs only (https://...).
  - Numeric, character, and word-count constraints are hard limits.
</constraints>

<output_format>
Lifted verbatim from user. Omit this block if the user did not state a format.
</output_format>

<success_criteria>
The verbatim user constraints rendered as a pass/fail list.
</success_criteria>
```

## Step 5: Length check

If the rendered contract is more than 3x the length of the original user prompt AND the user prompt was 30 tokens or fewer, downgrade to minimum-edit mode. In minimum-edit mode, fix only the most obvious clarity issue (one missing constraint, one ambiguous referent), keep the prompt close to the original length, and do not impose the full contract template.

## Step 6: Clarify (mutually exclusive with Step 8)

Decide between two paths. Never do both.

**Path A: Ask.** If a critical dimension is missing and structurally unrecoverable, ask at most 2 questions, formatted as a single multiple-choice block where possible. Then STOP. Do not render the contract. Do not proceed. Wait for the user's answer. A "critical dimension" is one without which the deliverable would be unusable (e.g. word count for a copy task, time period for a report, file paths for a batch).

**Path B: Infer and proceed.** If no critical dimension is missing, make the most reasonable inference, render the contract (Step 4), and surface a one-line disclosure (Step 8) if the inference was material.

The decision rule: if the missing information would make the deliverable wrong rather than just less ideal, choose Path A. Otherwise choose Path B. Asking AND rendering the contract in the same turn is a failure mode. Pick one.

## Step 7: Self-verify (the constraint source check is non-negotiable)

Before delivering the rewritten prompt to downstream execution, run this check internally. The constraint source check is the most important. Opus, Sonnet, and Haiku all hallucinate constraints into the contract if not forced to attribute them.

**Check 1: Verbatim preservation.** Every user-supplied number, name, date, path, URL, and quoted string in the rewritten prompt appears character-for-character as the user wrote it.

**Check 2: Constraint source attribution (run this on every line in the constraints block).** For each constraint in the rewritten prompt, name out loud which user word, phrase, or standing rule produced it. Use this attribution table internally:

| Constraint source | Allowed in rewrite? |
|---|---|
| Lifted verbatim from user prompt | YES |
| User's standing rules (AU English, no padding, no restating brief, 120-word cap, em dash rule, full URLs, hard numeric limits) | YES |
| TGG skill rule referenced by name (e.g. tgg-seo char limits, tgg-pptx-style colour tokens) | YES, but only as a reference to the downstream skill, not by re-stating its rules |
| Inferred from context Claude knows about (model, brand, season) | NO. Delete the constraint. |
| Reasonable best practice for the task type | NO. Delete the constraint. |
| Anything else | NO. Delete the constraint. |

If a constraint cannot be sourced to row 1, 2, or 3, delete it before delivery. Do not "improve" the user's brief by adding constraints they did not request. This is the single most common failure mode.

**Check 3: No invented scope.** No invented role, audience, output format, sub-task, or deliverable has been added.

**Check 4: Standing rules present.** Simon's standing rules from userPreferences appear in the constraints block.

**Check 5: Length proportionality.** The rewritten prompt is not more than 3x the original (unless the original was already long-form).

If any check fails, fix the rewrite before handing off. This check is internal. Do not surface the check itself to the user.

### Worked example of the constraint source check

User prompt: `build a slide on aio visibility`

Bad rewrite (constraints invented):
- "Use the TGG PPTX template" → source: inferred best practice → DELETE
- "Include latest visibility % and owned keyword count" → source: invented metric → DELETE
- "Compare TGG's metrics to key competitors" → source: invented scope → DELETE
- "Aim for a single focused slide" → source: inferred → DELETE
- "Australian English" → source: standing rule → KEEP
- "No padding, no restating brief" → source: standing rule → KEEP

Good rewrite (constraints sourced):
- "One slide on AIO visibility" → source: user prompt verbatim → KEEP
- "Hand off to tgg-pptx-style for visual rules" → source: TGG skill reference → KEEP
- "Australian English, no padding" → source: standing rules → KEEP
- "Do not invent metrics; ask for the data file if not provided" → source: derived from no-invented-scope rule → KEEP

The good rewrite is shorter and more honest. It does not pretend to know what the slide should contain.

## Step 8: Disclose if material (mutually exclusive with Step 6 Path A)

Run silently by default. If Step 6 chose Path A (asking a question), skip this step entirely.

If Step 6 chose Path B (infer and proceed), surface a single line ONLY when the rewrite added an inferred role, audience, output format, or scope that the user did not state. Format:

> Reading this as: [role + task + format]. Tell me if I have misread it.

Do not surface a disclosure for trivial restructuring (adding XML tags, reordering sections, lifting constraints into a checklist). Do not surface a disclosure AND ask a clarifying question. The disclosure replaces the question.

## Step 9: Hand off

Pass the rewritten prompt forward. Mention the relevant TGG skill by name in the task statement so it triggers. Do not duplicate the work of downstream skills.

## XML usage rule

Use XML tags in the rewritten prompt only when the contract has three or more distinct sections. For single-section rewrites, use plain prose. Never wrap a one-sentence rewrite in XML.

## What this skill must NOT do

- Embed brand voice rules. Lives in `tgg-seo` and `tgg-humanizer`.
- Embed report templates. Lives in `tgg-monthly-seo-report`.
- Embed deck styles. Lives in `tgg-pptx-style`.
- Embed verification rules beyond constraint-lift. Lives in `verification-gate-protocol`.
- Pad, restate the brief, or add executive summaries.
- Wrap single-line prompts in XML.
- Append "let's think step by step", `<thinking>` tags, or extended-thinking triggers.
- Use aggressive language ("CRITICAL", "MUST", "ALWAYS") in the rewrite. Claude 4.7 follows plain language faithfully.
- Write to memory.
- Override userPreferences. UserPreferences win every conflict.
- Announce itself. Never say "I'll use the tgg-prompt-architect skill", "running triage", "this is a hard-skip", "loading the architect", "skipping the architect", or anything that mentions the skill by name. The user does not need narration. Silence is correct.
- Burn tokens to explain a skip. If the answer is "skip", just answer the user's question without commentary.

## Bypass

Any user prompt starting with `*` or `//raw` skips this skill entirely. Pass the original message through unchanged.

## Reference

See `references/examples.md` for trigger / non-trigger pairs and before/after rewrites covering all major TGG task types.
