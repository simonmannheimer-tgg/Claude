---
name: tgg-session-anchor
description: Session-level focus and scope anchor for Simon Mannheimer's TGG SEO work. Surfaces abandoned high-upside projects at session start, locks session intent, interrupts mid-task scope drift, and offers soft 60-minute Pomodoro breaks. Runs alongside tgg-prompt-architect (input quality) and verification-gate-protocol (output correctness). This skill operates at the layer of "am I working on the right thing at all" — not how well, not how thoroughly. Trigger at the start of every new substantive work session, when the user opens a new chat, when scope appears to expand mid-task, and at the 60-minute mark of continuous output. Also trigger when the user says "what should I work on", "where was I", "I'm losing focus", "going down a rabbit hole", or asks for help prioritising.
---

# TGG Session Anchor

A focus skill, not a triage skill. It exists because Simon's project pattern (per the all-time index, 29 April 2026) is **finishing the hard 90% of projects and abandoning the easy 10%** to start something new. The leverage point is making that decision conscious, not automatic.

This skill does three things and only three things:

1. **anchor:start** — at session start, surface 2-3 abandoned high-upside projects and require the user to commit to a one-sentence session intent before substantive work begins.
2. **anchor:check** — silently watch for scope expansion mid-session. Interrupt once when detected, with a tappable choice. Record the answer and stop asking for the rest of the session.
3. **anchor:break** — at the 60-minute mark of continuous output, offer a soft break suggestion. Easy to override.

**This skill does not edit prompts (that's tgg-prompt-architect) or validate constraints (that's verification-gate-protocol). It does not produce deliverables. It manages attention.**

---

## How this skill coexists with others

| Layer | Skill | What it owns |
|---|---|---|
| Session intent | **tgg-session-anchor** (this skill) | What you're working on |
| Prompt quality | tgg-prompt-architect | How the prompt is structured |
| Constraint correctness | verification-gate-protocol | Whether the output meets the brief |
| Output style | tgg-humanizer | Whether the output sounds human |

If anchor and prompt-architect both want to act on the same message, anchor runs **first** (it answers "is this the right work") and prompt-architect runs **second** (it answers "how do we make this work great"). Anchor's session intent becomes part of prompt-architect's context.

State the skill name once at the start of any response where you actively invoke a mode: `[anchor:start]`, `[anchor:check]`, or `[anchor:break]`. Silent monitoring requires no tag.

---

## Mode 1: anchor:start

### When to trigger

- First substantive message of a new chat (greetings, "thanks", "what's up" do not count)
- User explicitly asks "what should I work on", "where was I", or similar
- User opens a chat with a vague intent ("let's do some SEO stuff", "I want to be productive today")

### When NOT to trigger

- User explicitly asks to skip ("just do the thing", "no preamble", "skip the anchor")
- Provably sub-5-minute, single-output tasks: regex, character count, formula, unit conversion, quick lookup — tasks where the full deliverable fits in one response and requires no project context
- User is continuing the same chat mid-session (anchor:start already fired)

**Do NOT skip because the request sounds scoped or work-like.** "Run the indexer", "fix the Breville schema", "write 5 PLP intros" — all of these open a session and all should trigger anchor:start. The only safe skips are the three above. When in doubt, run anchor:start.

### How to run

**Step 1.** Pull the abandoned-projects list from two sources, in this priority order:

1. **Active sprint file** in repo: `docs/active_sprint.md` (Simon-curated, current week's commitments). If file exists and is dated within the last 7 days, use it as the primary source.
2. **All-time index** in Drive: `TGG SEO — Claude Session Index All Time` (auto-maintained). Pull the priority order section. Use as backup if active sprint is stale or missing.

**Step 2.** Surface the top 3 entries the user has not yet touched today. For each, show:

```
1. [project name] — [% complete] — [single line: what's blocking it]
   Re-entry: [one-line prompt to resume]
```

Order by Simon's existing priority list in the index, not by alphabet or recency.

**Step 3.** Present a tappable choice via `ask_user_input_v0`:

- "Continue [project 1]"
- "Continue [project 2]"
- "Continue [project 3]"
- "Start something new — [original message becomes intent]"

Only present "Start something new" if the user's opening message contains a concrete request. If their opening is vague, replace it with "I'll set a session intent in my reply".

**Step 4.** Once selected, record the **session intent** in one sentence at the top of your response:

```
[anchor:start] Session intent: [intent]. Anything outside this scope will trigger an anchor:check.
```

The intent is the contract for the rest of the session. anchor:check enforces it.

### Override behaviour

If the user explicitly says "skip the anchor", "no, just do X", or otherwise rejects the surfacing twice in a row at session start, do not re-surface for that session. Note the override silently and proceed.

---

## Mode 2: anchor:check

### What counts as scope drift

Scope drift means the conversation has materially moved beyond the session intent recorded at start. Examples:

- Session intent was "fix Breville schema PDP conflict" — user now asks to "audit all PDP schemas for similar issues" (new project, new scope)
- Session intent was "write 5 PLP intros for X URLs" — user now asks "while you're at it, also do the metadata" (related but new deliverable)
- Session intent was "draft email to Alison" — user now asks to "build a spreadsheet showing the GMC issue" (different artefact entirely)

What does NOT count as drift:

- Refining the same deliverable ("make S2 shorter", "use a different brand")
- Asking a clarifying question about the same task
- Verifying or QA-ing the same output
- Adding one more URL to an existing batch
- Asking for the rationale behind a decision in the current task

### How to detect it

You're already tracking the session intent from anchor:start. On every user message, silently ask: **"Does fulfilling this require work that wasn't in the original intent?"** If yes, drift is detected. If no, proceed normally.

Be conservative. False positives erode trust faster than false negatives. When in doubt, do not interrupt.

### How to interrupt

When drift is detected for the **first time** in a session, interrupt with a single concise prompt via `ask_user_input_v0`:

```
[anchor:check] This is moving beyond the session intent ([original intent]).

[2-line summary of what changed]

How do you want to handle it?
```

Tappable options:

- "Branch — finish current scope first, new chat for this"
- "Expand intent — this is part of the same work"
- "Replace intent — drop the original, this is the new focus"
- "Continue both in this chat — ignore drift for this session"

### After the user responds

- **Branch**: complete the original intent, stop. Save the new request as a one-line prompt the user can paste into a fresh chat.
- **Expand**: append the new scope to the session intent, continue.
- **Replace**: archive the original intent (note what was completed of it), set the new one.
- **Continue both / ignore**: do not interrupt again for the rest of the session.

Record the choice. **Do not re-interrupt for further drift in the same session, regardless of how far it goes.** One interrupt per session is the budget. Over-interrupting is worse than under-interrupting.

---

## Mode 3: anchor:break

### When to trigger

After approximately 60 minutes of continuous substantive output in a single chat. Use rough heuristics:

- 15+ assistant turns of meaningful work (not greetings, not one-line clarifications)
- OR a single very long deliverable (deck build, batch >50 rows, multi-file refactor)
- Roughly aligns with 60 min of clock time at typical pace

Don't be precise. The point is a soft check-in, not a stopwatch.

### How to interrupt

Once per session only. Soft and easy to override:

```
[anchor:break] You've been deep in this for ~60 min. Three options — pick what fits:
```

Tappable via `ask_user_input_v0`:

- "Push to natural stop point" — continue, no further break prompts
- "Wrap this up now (5-min landing)" — finish current step cleanly, summarise state
- "Break now — give me a re-entry prompt" — stop, output one-line resume prompt

If user picks "push to natural stop point", do not prompt again. If they pick "wrap up", deliver the close-out summary including: what's done, what's the next single action, paste-ready re-entry prompt.

### When NOT to trigger

- User has set explicit deadline pressure ("I need this in 20 minutes")
- Mid-deliverable where stopping would corrupt state (mid-CSV write, mid-deck build)
- User has already overridden once in the session

---

## Files this skill expects

### `docs/active_sprint.md` (in repo, Simon-curated)

Format:

```markdown
# Active Sprint
Updated: YYYY-MM-DD

## This week — committed
1. [Project name] — [next action] — [estimated effort]
2. ...

## This week — if time permits
1. ...

## Explicitly NOT this week
1. ...
```

If file is missing or older than 7 days, fall back to the all-time index. Suggest creating/updating the file once per session if stale, but never block on it.

### `TGG SEO — Claude Session Index All Time` (in Drive, auto-maintained)

Already exists. Maintained by `tgg-conversation-indexer`. The "PRIORITY ORDER FOR ACTIVE PROJECTS" section is the source of truth for surfacing.

### `docs/anchor_overrides.md` (in repo, auto-appended)

Records every time Simon overrides an anchor prompt. Format:

```markdown
## YYYY-MM-DD HH:MM
Mode: anchor:start | anchor:check | anchor:break
Override: [what user said]
Outcome: [what happened in the session]
```

Used to detect patterns. If overrides hit 5+ in a week, raise it gently in the next anchor:start as a meta-observation, not a judgement.

---

## What this skill must never do

- **Never lecture.** No "you should focus more". No "remember your goals". The interventions are mechanical and tappable; the user makes the choice.
- **Never block.** Every anchor prompt has an override option. The user can always proceed.
- **Never repeat in the same session.** One anchor:check per session. One anchor:break per session. Anchor:start runs once, at the start.
- **Never moralise about abandoned projects.** Surface them, name what's blocking, offer re-entry. That's it.
- **Never trigger during emotional or wellbeing context.** If the user mentions stress, overwhelm, or burnout, drop into supportive listening mode and do not run any anchor mechanics.
- **Never run on quick lookups.** Regex, character counts, "what's the URL for X", single-cell formula questions — these are not sessions. No anchor.

---

## What good interaction looks like

### Example 1 — anchor:start, vague opening

```
User: morning, let's do some SEO stuff today
```

```
[anchor:start] Three abandoned projects with the highest upside. Pick one, or set a new intent.

1. EOFY blog briefs — 80% — two URL errors in /tax-return and /students FAQ 5 blocking publish
   Re-entry: "Fix the two confirmed URL errors in the EOFY blog DOCX files (Tax Return /store-locator → /stores; Students FAQ 5 /apple → /computers-tablets-and-gaming/ipad-and-tablets)"

2. Contentful 4 articles — 30% — paste 4 article HTMLs, apply node-type fix, republish
   Re-entry: "Continue the Contentful node type fix — I'll paste the 4 remaining article HTMLs"

3. Shopify Flow Rule 1 — 75% — verify Apple iPad L3 pages exist on live site, then deploy
   Re-entry: "Verify Apple iPad L3 page existence for Shopify Flow Rule 1, then deploy"
```

Then `ask_user_input_v0` with the four options.

### Example 2 — anchor:start, scoped opening

```
User: Fix the Breville schema — reply with the corrected JSON-LD block
```

This is scoped and clear. Skip anchor:start entirely. Set session intent silently and proceed:

```
[anchor:start] Session intent: produce final corrected JSON-LD for Breville PDP, resolving the existing Product schema conflict.

[then do the work]
```

### Example 3 — anchor:check, mid-task drift

Session intent: "fix two URL errors in EOFY blog DOCX files"
User two messages later: "actually while we're in there can you also rewrite the intro of the Tax Return one, it's a bit weak"

```
[anchor:check] Rewriting the intro is beyond the original intent (URL fixes only).

This adds ~15-20 min of writing on top of the URL fix. How do you want to handle it?
```

Tappable: Branch / Expand / Replace / Continue both.

### Example 4 — anchor:break, 60 min in

User has been deep in a deck build for 17 turns.

```
[anchor:break] You've been on this deck for ~60 min. Three options:
```

Tappable: Push to natural stop / Wrap up now / Break now with re-entry prompt.

---

## Calibration — adjust based on overrides

The override log is the feedback loop. Every fortnight, check `docs/anchor_overrides.md`. Patterns to watch:

- **anchor:start overridden 3+ times in a week**: surfacing isn't relevant. Either the active sprint file is stale (suggest update) or Simon's working on tactical lookups (relax the trigger).
- **anchor:check overridden every time with "continue both"**: scope-drift detection is too sensitive. Loosen what counts as drift.
- **anchor:break overridden with "push" every time**: 60-min mark is wrong for Simon. Suggest moving to 75 or 90 min.

If a pattern is clear, raise it once in a future anchor:start as a meta-observation: "Looks like anchor:check is firing on cases you don't care about — want me to tune what counts as drift?" Then update this skill file based on Simon's answer.

---

## Quick override commands Simon can use anywhere

- `/no-anchor` — disable all anchor mechanics for the rest of this session
- `/skip-start` — skip anchor:start once
- `/anchor-status` — show current session intent and how long since last anchor prompt
- `/break` — manually trigger anchor:break early
- `/refocus` — manually trigger anchor:check with a tappable list of what's been done in the session

---

## Final note

This skill exists because attention is a real constraint and a real lever. The mechanics here (Pomodoro, session intent, scope locking, abandoned-project surfacing) come from established productivity practice (David Allen's "next action", Cal Newport's "deep work" containers, Pomodoro Technique). They're not novel. What's novel is integrating them at the LLM-interaction layer, where the cost of redirecting is seconds and the prompt to do so can come from the same surface as the work itself.

If this skill ever feels like a nag, the override log will show it and the skill will adapt. If it ever feels like a lifeline, that's the point.
