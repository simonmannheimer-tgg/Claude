---
title: Making responses more concise and efficient (full)
parent: Chat/Light/2026-04-20-making-responses-more-concise-and-efficient-71a44f
uuid: 71a44f4e-50bf-46a2-b945-0cd52dc8d6a6
---

#chat/full #project/main #status/completed

# Making responses more concise and efficient — Full Transcript

→ Light view: [[Chat/Light/2026-04-20-making-responses-more-concise-and-efficient-71a44f]]
→ Medium view: [[Chat/Medium/2026-04-20-making-responses-more-concise-and-efficient-71a44f]]

**Messages:** 10 | **Date:** 2026-04-20

---

### 1. **Human** — 2026-04-20T03:56

this is my personal preferences:

i feel like claude will create very long, wordy, hard to grasp responses, that i frankly end up not reading - it's a waste of tokens, time, and its innefficient - we need to figure out a way together too ensure responses are consise, helpful, and not wasteful.
this is my personal preferences:

i feel like claude will create very long, wordy, hard to grasp responses, that i frankly end up not reading - it's a waste of tokens, time, and its innefficient - we need to figure out a way together too ensure responses are consise, helpful, and not wasteful.

---

### 2. **Claude** — 2026-04-20T03:57

Simon wants to fix verbosity. He's asking me to help him solve this collaboratively. Let me be direct and practical rather than giving a long response about how to give short responses (that would be ironic).

The core problem: Claude defaults to comprehensiveness because it's trained to be thorough. Without explicit constraints, it pads.

What actually works:
1. A hard token/line budget in the system prompt
2. Format defaults that discourage lists and headers (which inflate length)
3. A "answer first, rationale optional" rule
4. Flagging when a response genuinely needs length vs. padding

His preferences already have some of this but it's not tight enough. 

The instructions themselves are getting too long and diluting the core message. I should give him a short, direct response with concrete options he can actually implement.The root cause: your preferences file is detailed and well-intentioned, but Claude still defaults to comprehensiveness because there's no hard ceiling. "Concise" is subjective. "Max 150 words unless the task requires more" is not.

Three options, pick one or combine:

**A. Add a hard default word budget.** Something like: "Default response cap: 120 words. Exceed only when the task explicitly requires more (code, batch output, structured deliverables). No exceptions for explanation, rationale, or caveats." This forces triage before writing.

**B. Ban structural padding triggers.** Lists, headers, and bold text inflate perceived length and encourage Claude to fill sections. You already prefer prose. Strengthen it: "No headers, no bullet points, no bold in conversational responses. Prose only, one paragraph max unless the task is a deliverable."

**C. Add a self-check rule.** "Before responding, ask: could this be half the length without losing the answer? If yes, cut it."

My recommendation: A plus B. The word cap creates a hard constraint. The formatting ban removes the structural temptation to pad. C is soft and Claude will rationalise around it.

Want me to rewrite your preferences block with these baked in?
 
The root cause: your preferences file is detailed and well-intentioned, but Claude still defaults to comprehensiveness because there's no hard ceiling. "Concise" is subjective. "Max 150 words unless the task requires more" is not.

Three options, pick one or combine:

**A. Add a hard default word budget.** Something like: "Default response cap: 120 words. Exceed only when the task explicitly requires more (code, batch output, structured deliverables). No exceptions for explanation, rationale, or caveats." This forces triage before writing.

**B. Ban structural padding triggers.** Lists, headers, and bold text inflate perceived length and encourage Claude to fill sections. You already prefer prose. Strengthen it: "No headers, no bullet points, no bold in conversational responses. Prose only, one paragraph max unless the task is a deliverable."

**C. Add a self-check rule.** "Before responding, ask: could this be half the length without losing the answer? If yes, cut it."

My recommendation: A plus B. The word cap creates a hard constraint. The formatting ban removes the structural temptation to pad. C is soft and Claude will rationalise around it.

Want me to rewrite your preferences block with these baked in?

---

### 3. **Human** — 2026-04-20T04:12

A+ C, i like visuals like B they help break data down.

The goal is to be able to give me an answer without waffling on
A+ C, i like visuals like B they help break data down.

The goal is to be able to give me an answer without waffling on

---

### 4. **Claude** — 2026-04-20T04:12

Simon wants A + C, keeping visuals/formatting (B stays as-is). Let me update his preferences with a hard word cap and a self-check rule. He wants me to rewrite the preferences block.

Let me draft the additions:

1. Hard default word budget: ~120 words for conversational responses, exceed only for deliverables
2. Self-check: before responding, could this be half the length? If yes, cut it.

I should just tell him what I'm adding and offer to rewrite, or just show the additions. He said "want me to rewrite your preferences block" - he said A+C so yes, let me do it concisely.


I'll show him the two new rules cleanly rather than rewriting the entire block—that's more direct and efficient.Two rules to add to your preferences block:

> **Response length:** Default cap is 120 words for conversational responses. Exceed only for code, batch output, or structured deliverables. No rationale padding, no caveats unless they change the decision.

> **Self-check before every response:** Can this be half the length without losing the answer? If yes, cut it before sending.

Want me to drop these into your full preferences file and return the updated block?
 
Two rules to add to your preferences block:

> **Response length:** Default cap is 120 words for conversational responses. Exceed only for code, batch output, or structured deliverables. No rationale padding, no caveats unless they change the decision.

> **Self-check before every response:** Can this be half the length without losing the answer? If yes, cut it before sending.

Want me to drop these into your full preferences file and return the updated block?

---

### 5. **Human** — 2026-04-20T04:13

yes
yes

---

### 6. **Claude** — 2026-04-20T04:14

The user wants me to update their preferences file with the two new rules. Let me read the current preferences from the document provided, add the two rules, and return the updated block.

The current preferences are in the uploaded document (document index 1). Let me work with that content and add the two rules.

I'll add them as a new section or integrate them naturally. Let me write the updated block concisely.
```
This block is not supported on your current device yet.
```

Done. Present the file.
```
This block is not supported on your current device yet.
```

Two rules added, formatting preference updated to explicitly allow visuals when they earn their place. Paste this into Settings > Profile to activate.
 
Two rules added, formatting preference updated to explicitly allow visuals when they earn their place. Paste this into Settings > Profile to activate.

---

### 7. **Human** — 2026-04-20T06:06

how can i add in a rule that we never talk like this:

We are not setting goals for them; we are asking them to bring the goals alongside their proposed work.

its noot just x, its y, < this is a typical AI give-away and alongside emdashes its badddd
how can i add in a rule that we never talk like this:

We are not setting goals for them; we are asking them to bring the goals alongside their proposed work.

its noot just x, its y, < this is a typical AI give-away and alongside emdashes its badddd

---

### 8. **Claude** — 2026-04-20T06:06

Simon wants to ban a specific rhetorical pattern: the "not X, but Y" correction structure (e.g., "We are not setting goals for them; we are asking them to bring the goals alongside their proposed work."). This is a classic AI-sounding clarification pattern.Add this to your formatting rules:

> **No corrective reframing.** Never write "not X, but Y" or "it's not just X, it's Y" constructions. State the point directly without contrasting it against a straw version of itself.
 
Add this to your formatting rules:

> **No corrective reframing.** Never write "not X, but Y" or "it's not just X, it's Y" constructions. State the point directly without contrasting it against a straw version of itself.

---

### 9. **Human** — 2026-04-20T06:07

full new format
full new format

---

### 10. **Claude** — 2026-04-20T06:07

The user wants the full updated preferences file with this new rule added.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done. Rule added under formatting.
 
Done. Rule added under formatting.
