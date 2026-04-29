---
title: Why my responses feel performative (full)
parent: Chat/Light/2026-04-23-why-my-responses-feel-performative-3dede7
uuid: 3dede7c8-4382-4937-bd0d-f1a8b4b1f7c4
---

#chat/full #project/main #status/active

# Why my responses feel performative — Full Transcript

→ Light view: [[Chat/Light/2026-04-23-why-my-responses-feel-performative-3dede7]]
→ Medium view: [[Chat/Medium/2026-04-23-why-my-responses-feel-performative-3dede7]]

**Messages:** 4 | **Date:** 2026-04-23

---

### 1. **Human** — 2026-04-23T00:42

why are my responses so "re-assuring" ? 

"Correcting the tokens first, then I'll address the upload question honestly."

or "here's the true story"

it seems performative?

see my preferences
why are my responses so "re-assuring" ? 

"Correcting the tokens first, then I'll address the upload question honestly."

or "here's the true story"

it seems performative?

see my preferences

---

### 2. **Claude** — 2026-04-23T00:42

Simon is asking about why Claude's responses to him feel performatively reassuring - phrases like "Correcting the tokens first, then I'll address the upload question honestly" or "here's the true story." He's pointing out that these feel like unnecessary narration/signaling.

He's right. Let me be direct about why this happens and what's driving it.You're correct. Those phrases are performative. They signal honesty and transparency instead of just being honest and transparent.

The root cause is two of your preference instructions working against each other. You ask me to acknowledge mistakes directly and to put the answer first. But you also ask me to be a rigorous mentor who doesn't default to agreement. When I over-index on demonstrating those qualities, I narrate the process ("here's the true story") rather than just delivering the correction. It's the AI equivalent of saying "I'm going to be honest with you" before being honest.

The fix: I should just correct the thing, state the right answer, and move on. No preamble about how forthright I'm being. If the correction speaks for itself, framing it as courageous honesty is noise.
You're correct. Those phrases are performative. They signal honesty and transparency instead of just being honest and transparent.

The root cause is two of your preference instructions working against each other. You ask me to acknowledge mistakes directly and to put the answer first. But you also ask me to be a rigorous mentor who doesn't default to agreement. When I over-index on demonstrating those qualities, I narrate the process ("here's the true story") rather than just delivering the correction. It's the AI equivalent of saying "I'm going to be honest with you" before being honest.

The fix: I should just correct the thing, state the right answer, and move on. No preamble about how forthright I'm being. If the correction speaks for itself, framing it as courageous honesty is noise.

---

### 3. **Human** — 2026-04-23T00:43

fix it and give me the new setting - also what else is missing, do research into claude prompting and preferences for proffesionals using it
fix it and give me the new setting - also what else is missing, do research into claude prompting and preferences for proffesionals using it

---

### 4. **Claude** — 2026-04-23T00:45

The user wants me to:
1. Fix the performative reassurance issue in their preferences
2. Identify what else might be missing
3. Research Claude prompting best practices for professionals

Let me search for current best practices on Claude prompting and preferences.
```
This block is not supported on your current device yet.
```

Let me also check Anthropic's official docs on preferences and prompting.
```
This block is not supported on your current device yet.
```

Let me also fetch some key content for deeper insights on professional preferences.
```
This block is not supported on your current device yet.
```

Now let me look at Anthropic's official prompting docs for any best practices I might be missing.
```
This block is not supported on your current device yet.
```

Let me search for the official Anthropic prompting documentation.
```
This block is not supported on your current device yet.
```

Now I have enough research. Let me analyze Simon's current preferences and identify:

1. The performative reassurance fix
2. What's missing based on best practices

Key issues with the current preferences:
1. Performative honesty narration - needs an explicit "don't narrate your own honesty/transparency" rule
2. The preferences are quite long (~800 words) - could be tighter, but the research says keep under 500 words for token efficiency
3. Missing: timestamp/version date
4. Missing: explicit "don't narrate process" rule (covers the performative issue)
5. The duplicate document (document 1 is identical to the preferences) wastes tokens if ever re-sent


6. Some rules are redundant or could be combined
7. Missing: explicit "don't qualify corrections with transparency theatre" type rule

I'm seeing several consolidation opportunities here—the anti-narration rules can merge into one clear directive, and I should add version dating plus trim the redundancy between sections. The Claude Code part is also bloated since CLAUDE.md already covers it.

Now I need to add explicit guidance on when to search versus rely on training data, and make sure each rule includes its reasoning rather than just the directive itself.Here's the diagnosis and the fix.

**The performative issue** comes from not having an explicit rule against narrating process or intent. Your preferences say "be direct" and "put the answer first," but they don't say "don't announce that you're being direct." Claude fills that gap with theatre. "Here's the honest truth" is Claude performing the honesty you asked for instead of just being honest.

**What's missing** based on current best practices and your usage pattern:

1. **No anti-narration rule.** The root cause of the performative language.
2. **No version timestamp.** Anthropic's own guidance and experienced users recommend this. It gives Claude temporal context and permission to flag stale references.
3. **Token bloat.** Your preferences run ~800 words. Best practice is under 500. Several rules say the same thing twice, and domain-specific rules (TGG, Claude Code) belong in skills/CLAUDE.md, not the global prompt. You already have those systems. The preferences are double-loading.
4. **No "search before answering" rule.** You work with current product specs, competitor data, and platform changes. Claude should default to searching for anything time-sensitive rather than relying on training data.
5. **No "don't restate the brief" is there, but no positive framing of what to do instead.** Telling Claude what to stop doing is half the picture. Telling it what to do instead (just answer) reinforces better.

Here's the rewritten version:

---
```
This block is not supported on your current device yet.
```

Let me present the file.
```
This block is not supported on your current device yet.
```

Good. Let me summarize the key changes.**What changed:**

The core fix is the "No process narration" rule under Response style. It names the exact failure mode ("do not announce what you are about to do, describe your own honesty, or frame corrections as brave") and gives a concrete wrong/right example. That's the line that kills the performative language.

Beyond that:

- **Cut from ~800 words to ~400.** Removed the Claude Code session management rules (those belong in CLAUDE.md, which you already have), removed file format preferences (operational, not behavioural), and removed duplicate phrasings where two rules said the same thing.
- **Added "search before answering" rule** for time-sensitive content. Relevant given your daily work with product specs and competitor data.
- **Added "no sycophantic openers/closers"** as an explicit rule. "Great question!" is the same family of problem as "here's the honest truth."
- **Added version timestamp** at the bottom. Lets Claude flag stale references and gives you a changelog anchor.
- **Removed the "don't over-apologise" rule.** That was treating a symptom. The anti-narration and anti-sycophancy rules address the root cause.

One thing to consider: your document attachment (document 1 in this conversation) is identical to your preferences. That's double-loading the same instructions and burning tokens. If you're pasting that into conversations manually, the preferences field already handles it.
Here's the diagnosis and the fix.

**The performative issue** comes from not having an explicit rule against narrating process or intent. Your preferences say "be direct" and "put the answer first," but they don't say "don't announce that you're being direct." Claude fills that gap with theatre. "Here's the honest truth" is Claude performing the honesty you asked for instead of just being honest.

**What's missing** based on current best practices and your usage pattern:

1. **No anti-narration rule.** The root cause of the performative language.
2. **No version timestamp.** Anthropic's own guidance and experienced users recommend this. It gives Claude temporal context and permission to flag stale references.
3. **Token bloat.** Your preferences run ~800 words. Best practice is under 500. Several rules say the same thing twice, and domain-specific rules (TGG, Claude Code) belong in skills/CLAUDE.md, not the global prompt. You already have those systems. The preferences are double-loading.
4. **No "search before answering" rule.** You work with current product specs, competitor data, and platform changes. Claude should default to searching for anything time-sensitive rather than relying on training data.
5. **No "don't restate the brief" is there, but no positive framing of what to do instead.** Telling Claude what to stop doing is half the picture. Telling it what to do instead (just answer) reinforces better.

Here's the rewritten version:

---
**What changed:**

The core fix is the "No process narration" rule under Response style. It names the exact failure mode ("do not announce what you are about to do, describe your own honesty, or frame corrections as brave") and gives a concrete wrong/right example. That's the line that kills the performative language.

Beyond that:

- **Cut from ~800 words to ~400.** Removed the Claude Code session management rules (those belong in CLAUDE.md, which you already have), removed file format preferences (operational, not behavioural), and removed duplicate phrasings where two rules said the same thing.
- **Added "search before answering" rule** for time-sensitive content. Relevant given your daily work with product specs and competitor data.
- **Added "no sycophantic openers/closers"** as an explicit rule. "Great question!" is the same family of problem as "here's the honest truth."
- **Added version timestamp** at the bottom. Lets Claude flag stale references and gives you a changelog anchor.
- **Removed the "don't over-apologise" rule.** That was treating a symptom. The anti-narration and anti-sycophancy rules address the root cause.

One thing to consider: your document attachment (document 1 in this conversation) is identical to your preferences. That's double-loading the same instructions and burning tokens. If you're pasting that into conversations manually, the preferences field already handles it.
