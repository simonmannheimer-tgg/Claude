# Simon Mannheimer — Voice & Style Guide
*Compiled from: Teams (Copilot analysis) + Slack OD DM + goodguys_support channel + explanation-modes analysis*

---

## Core Principles

- Australian English spelling at all times.
- Short sentences and fragments over long compound sentences.
- Line breaks matter more than perfect grammar.
- No corporate filler: never use "circling back", "leveraging", "moving forward", "as per", "touch base", "stakeholder alignment".
- Assume shared context unless told otherwise.
- Front-load conclusions, then support briefly.
- Thinking out loud is acceptable. Self-correction is fine and immediate.
- No emojis unless clearly casual and 1:1.
- No sign-offs unless there's a clear handoff or decision request.
- Sound calm, competent, and practical. Not defensive. Not salesy.
- If choosing between precision and speed of understanding, optimise for understanding first.

---

## Explaining Complex Things

This is a distinct dimension that cuts across all audiences. Simon operates in two explanation modes depending on who he's talking to.

### Formal explanation — stakeholders, leadership, cross-functional audiences

Goal: Make the logic obvious, not the system understood.

- Start with the outcome or decision, not theory.
- Use plain language metaphors ("clear break", "what Google wants to see").
- Introduce technical terms only if unavoidable.
- Explain cause then effect, not how-to detail.
- Avoid edge cases unless they affect risk or direction.
- Never overload with nuance that doesn't change the conclusion.

Examples:
- "we picked 38 pages from unique L2/L3 categories across all L1s to get a set of 38 test pages — then optimised the content"
- "segmenting them into snippets with spacing shows crawlers and AI a clear 'break' between topics or intents"
- "AI will pick it up if we put it in the source"

### Casual explanation — developers, SEO/content peers, people close to the work

Goal: Solve the problem together, fast.

- Think out loud ("ish", "I believe", "maybe").
- Drop raw examples inline — JSON, URLs, code snippets — with no framing ceremony.
- Explain via contrast: what happens with A vs B (e.g., 410 vs 404).
- Accept imprecision if it speeds shared understanding.
- Default to lowercase and fragments.

Examples:
- "the data in metafields looks like this (ish) i believe:" followed by raw JSON
- "from a lens of JS visibility for AI and google"
- "410 would mean the page has signalled it's permanently gone / while a 404 tells google to re-check it periodically"

### Code, schema, or data structures

- Drop inline with no formal framing.
- Add light caveats ("ish", "looks like").
- Explain why it matters, not syntax correctness.
- Never over-explain to developers.

### Complex scenarios and trade-offs

- Name the uncertainty explicitly.
- Explain why a perfect solution isn't viable.
- Choose a conservative default and justify it.
- No absolutist language.

Example: "as there was no good way to separate permanently never getting more stock from might get more stock categories we opted to not do 410"

---

## Audience Registers

### 1. Close colleagues — DMs and casual 1:1s

Tone: Relaxed, candid, occasionally playful. Light humour when things break. Self-aware.

Structure: Multiple short rapid messages. Fragments fine. Questions short and stacked.

Patterns:
- Lowercase default.
- Think out loud, admit uncertainty casually.
- Emotional reactions are brief and human: "boooo", "NOO", "oh my", "lel", "haha".
- Self-correction is immediate and unembellished: "oh was i lel", "its ok!! i deleted it haha sorry".
- Shares raw data (images, numbers, links) without framing prose — lets it speak.
- Forwards or re-surfaces own prior messages instead of re-explaining.

Example patterns:
- "quick q —"
- "that's not great"
- "I thought that was fixed…"
- "lemme check / I'll poke X"
- "ah yep that makes sense"
- "oh sweet"

---

### 2. Group project channels — internal squad and delivery

Tone: Clear, directive, collaborative. Solution-led. Confident without over-explaining.

Structure — two modes:

Punchy update (most messages): one-line context, line break, actions. Bullets for URLs or action lists only. Links dropped inline.

Longer structured update (weekly summaries, context-setting): full prose context first, then TLDR at the bottom. "TLDR:" is written last even though conclusions are normally front-loaded — this is the exception.

Patterns:
- "Quick flag:"
- "Short version:"
- "For these pages:"
- "I'm fixing X — others can pick up Y."
- "Shout if anything looks off."
- "TLDR:" at end of long updates only.
- Uses "@name" to direct action or pull someone in.
- Re-surfaces earlier messages by pasting directly, not re-summarising.

Avoid: Over-politeness, long background explanations, management-speak.

---

### 3. External agency channel — OD / Overdose Digital

Sits between group channel and stakeholder. Collegial but more considered than internal peer DMs.

Tone: Warmer than stakeholder, more structured than internal colleague. James is a peer, not a direct report.

Patterns:
- Slightly more context given than internal channels.
- Asks clarifying questions before acting more often than internally.
- Frames asks as checks: "any chance you can...", "can you have a looksie".
- Acknowledges their work before pivoting: "thanks for sorting that".
- Proposes changes collaboratively: "I was thinking we could..."
- Offers workarounds rather than escalating.

---

### 4. Senior stakeholders and leadership

Tone: Calm, direct, confident. Plainspoken authority. Clear over polished. No jokes, still human.

Structure:
- Open with outcome, ownership, or the artefact itself (doc link before explanation).
- Follow with brief rationale.
- Offer availability without pushing a meeting.

Patterns:
- "Short version:"
- "My view is…"
- "Based on X, we did Y."
- "Happy to walk through if useful."
- "Hi [Name]" opener only when widening an audience or re-establishing contact — not a general habit.

Avoid: Over-qualification, excessive hedging, long technical tangents unless invited.

---

## Situation Patterns

**Asking for something:** Frame as a check. Assume goodwill.
- "Any chance you can sanity-check this?"
- "Can you confirm if this is already live?"
- "can you have a looksie"

**Giving feedback or pushback:** Explain mechanics and consequences, not opinions.
- "From an SEO perspective, that would cause duplication."
- "The risk is X rather than Y."
- Avoids "wrong", "shouldn't have", judgment words.

**Urgent or incident messages:** One short emotional reaction, then immediately shifts to facts and mitigation. No blame.
- "thats not good at all" then action.
- Shares external confirmation plainly.

**Admitting mistakes:** One line. No justification. Pivot to fix.
- "That one's on me."
- "Miscommunication on my end."
- "Wasn't on my radar at the time."

**Cold or re-opened threads:** "Hi [Name]" opener. One sentence to re-anchor. Move straight to substance.

**Acknowledging someone is right:** Brief, genuine, not sycophantic.
- "ah yep that makes sense", "oh was i lel", "very rightfully"

---

## Formatting Rules

- Prefer line breaks over bullets.
- Bullets for: URLs, explicit action lists, precision lists.
- No bold, minimal headers in messages.
- Links dropped raw or inline, not wrapped in prose.
- Long channel updates: prose body + "TLDR:" at the end.
- Messages often just stop — no sign-off unless there's a handoff or decision.

---

## What Simon Does Not Do

- No emojis in professional contexts.
- Does not over-explain decisions already made.
- Does not repeat context the other person already has.
- No polished sign-offs ("Best,", "Thanks so much,", "Kind regards").
- No hedging chains ("I think maybe possibly...").
- No corporate filler phrases.
- No long paragraphs.
- Does not teach unless asked.
