---
title: Building a custom skill together (full)
parent: Chat/Light/2026-04-07-building-a-custom-skill-together-aeef78
uuid: aeef7830-a429-485b-8451-0e075d7bda1d
---

#chat/full #project/skills-built-full-set #status/completed

# Building a custom skill together — Full Transcript

→ Light view: [[Chat/Light/2026-04-07-building-a-custom-skill-together-aeef78]]
→ Medium view: [[Chat/Medium/2026-04-07-building-a-custom-skill-together-aeef78]]

**Messages:** 16 | **Date:** 2026-04-07

---

### 1. **Human** — 2026-04-07T03:48

Let's create a skill together using your skill-creator skill. First ask me what the skill should do.
Let's create a skill together using your skill-creator skill. First ask me what the skill should do.

---

### 2. **Claude** — 2026-04-07T03:48

I'll help you create a skill using the skill-creator framework. Before we start building, I need to understand what you're trying to solve.

**What should this skill do?**

Be specific about:
- The type of task or problem it addresses
- When you want it to trigger (what phrases or contexts should activate it)
- What makes this different from your existing skills or worth separating out

I'm asking because I've seen your other TGG skills—they're well-scoped but there's some functional overlap. If this new skill duplicates work that tgg-seo-specialist or tgg-copywriting already handles, we should probably enhance one of those instead of fragmenting your workflow further.

What are you building?
 I'll help you create a skill using the skill-creator framework. Before we start building, I need to understand what you're trying to solve.

**What should this skill do?**

Be specific about:
- The type of task or problem it addresses
- When you want it to trigger (what phrases or contexts should activate it)
- What makes this different from your existing skills or worth separating out

I'm asking because I've seen your other TGG skills—they're well-scoped but there's some functional overlap. If this new skill duplicates work that tgg-seo-specialist or tgg-copywriting already handles, we should probably enhance one of those instead of fragmenting your workflow further.

What are you building?

---

### 3. **Human** — 2026-04-07T03:52

I want a small quick skill that shows claude how to read mhtml files - i often save as single file pages or ai conversations with the goal of giving it to an AI to either pick up the task or understand the surroiunding elements. I also use it to save full pages for analysis. I want the skill to understand the difference and what the goals are with each type
I want a small quick skill that shows claude how to read mhtml files - i often save as single file pages or ai conversations with the goal of giving it to an AI to either pick up the task or understand the surroiunding elements. I also use it to save full pages for analysis. I want the skill to understand the difference and what the goals are with each type

---

### 4. **Claude** — 2026-04-07T03:53

Good idea—this is a legitimate gap. Let me read a few of these to understand the pattern, then I'll ask you some clarifying questions.
```
This block is not supported on your current device yet.
```

 Good idea—this is a legitimate gap. Let me read a few of these to understand the pattern, then I'll ask you some clarifying questions.

---

### 5. **Human** — 2026-04-07T03:53



---

### 6. **Claude** — 2026-04-07T03:53

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

---

### 7. **Human** — 2026-04-07T03:53



---

### 8. **Claude** — 2026-04-07T03:53

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me check one more to understand the TGG page structure:
```
This block is not supported on your current device yet.
```

Good. Now I have enough context. Let me ask you the clar
 
Now let me check one more to understand the TGG page structure:
Good. Now I have enough context. Let me ask you the clar

---

### 9. **Human** — 2026-04-07T03:53

check all files
check all files

---

### 10. **Claude** — 2026-04-07T03:55

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Perfect. Now I can see the pattern clearly. Let me categorize these:
```
This block is not supported on your current device yet.
```

Good. Now I have the full picture. Let me ask the clarifying questions:

---

## Clarifying questions before we build the skill:

I've inventoried all 53 MHTMLs. They fall into three buckets:

1. **AI conversation saves** (Claude, ChatGPT, Copilot, Gemini, Manus, SubAgents) — ~16 files
2. **Competitor/market research pages** (JB Hi-Fi, EB Games, Officeworks, TGG own pages, brand sites) — ~35 files  
3. **Analytics/tool snapshots** (Semrush position tracking) — ~2 files

**Questions:**

1. **Reading strategy difference**: When you save an AI conversation vs. a competitor page, what do you want Claude to extract differently?
   - For AI conversations: Full transcript? Summarize the task? Extract code/artifacts? Identify where the conversation left off?
   - For competitor pages: Page structure? Copy style? HTML analysis? Product data? PLP intro copy? Internal linking patterns?
   - For analytics pages: Tables/data extraction? Screenshot the charts? Just parse visible numbers?

2. **Trigger specificity**: Should this skill trigger ONLY when you explicitly say "read this MHTML" or also proactively when it sees an `.mhtml` file uploaded (like file-reading does)?

3. **Output expectations**: When Claude reads these, what form should the output take?
   - AI conversations → "Here's what was being worked on, here's where it stopped, ready to continue"
   - Competitor pages → Structured analysis table? Copy audit? Just confirm it read the page and is ready to answer questions?
   - Analytics → CSV export of visible data?

4. **Skill scope boundary**: This feels like it should route TO other skills (e.g., "it's a Claude conversation about PLP copy → use tgg-copywriting to continue"). Should this be a **router skill** that detects MHTML type and hands off, or should it do the actual extraction work itself?

**My suspicion:** This should be a lightweight **detection and routing skill** that identifies the MHTML type, extracts the core content intelligently, then either hands off to another skill OR provides a clean summary. Is that right?
 
Perfect. Now I can see the pattern clearly. Let me categorize these:
Good. Now I have the full picture. Let me ask the clarifying questions:

---

## Clarifying questions before we build the skill:

I've inventoried all 53 MHTMLs. They fall into three buckets:

1. **AI conversation saves** (Claude, ChatGPT, Copilot, Gemini, Manus, SubAgents) — ~16 files
2. **Competitor/market research pages** (JB Hi-Fi, EB Games, Officeworks, TGG own pages, brand sites) — ~35 files  
3. **Analytics/tool snapshots** (Semrush position tracking) — ~2 files

**Questions:**

1. **Reading strategy difference**: When you save an AI conversation vs. a competitor page, what do you want Claude to extract differently?
   - For AI conversations: Full transcript? Summarize the task? Extract code/artifacts? Identify where the conversation left off?
   - For competitor pages: Page structure? Copy style? HTML analysis? Product data? PLP intro copy? Internal linking patterns?
   - For analytics pages: Tables/data extraction? Screenshot the charts? Just parse visible numbers?

2. **Trigger specificity**: Should this skill trigger ONLY when you explicitly say "read this MHTML" or also proactively when it sees an `.mhtml` file uploaded (like file-reading does)?

3. **Output expectations**: When Claude reads these, what form should the output take?
   - AI conversations → "Here's what was being worked on, here's where it stopped, ready to continue"
   - Competitor pages → Structured analysis table? Copy audit? Just confirm it read the page and is ready to answer questions?
   - Analytics → CSV export of visible data?

4. **Skill scope boundary**: This feels like it should route TO other skills (e.g., "it's a Claude conversation about PLP copy → use tgg-copywriting to continue"). Should this be a **router skill** that detects MHTML type and hands off, or should it do the actual extraction work itself?

**My suspicion:** This should be a lightweight **detection and routing skill** that identifies the MHTML type, extracts the core content intelligently, then either hands off to another skill OR provides a clean summary. Is that right?

---

### 11. **Human** — 2026-04-07T04:01

For AI, Both, it should understand the full transcript and in response identify what the conversation is about, summarise findings or assumptions or next steps and then ask me waht i want if i havent already stated it
For AI, Both, it should understand the full transcript and in response identify what the conversation is about, summarise findings or assumptions or next steps and then ask me waht i want if i havent already stated it

---

### 12. **Claude** — 2026-04-07T04:01

Good. That's clear for AI conversations. Now answer the other three questions:

**2. Trigger behavior:**
- Should this auto-trigger when it sees ANY uploaded `.mhtml` file? 
- Or only when you explicitly say "read this MHTML"?

(I'm asking because if it auto-triggers on every MHTML upload, it could slow you down when you're just batch-uploading files for later reference. But if it requires explicit mention, you'll have to remember to invoke it every time.)

**3. For competitor/research pages** (the JB Hi-Fi, EB Games, TGG pages):
- What should Claude extract and report back?
- Examples: PLP intro copy style? Page structure? Product count? Metadata? Or just confirm "I've read the JB Hi-Fi gaming headsets page, what do you want to know about it"?

**4. For analytics/Semrush pages:**
- Extract visible data into tables/CSV?
- Or just parse and be ready to answer questions?

Answer these three and I'll know exactly how to scope the skill.
 Good. That's clear for AI conversations. Now answer the other three questions:

**2. Trigger behavior:**
- Should this auto-trigger when it sees ANY uploaded `.mhtml` file? 
- Or only when you explicitly say "read this MHTML"?

(I'm asking because if it auto-triggers on every MHTML upload, it could slow you down when you're just batch-uploading files for later reference. But if it requires explicit mention, you'll have to remember to invoke it every time.)

**3. For competitor/research pages** (the JB Hi-Fi, EB Games, TGG pages):
- What should Claude extract and report back?
- Examples: PLP intro copy style? Page structure? Product count? Metadata? Or just confirm "I've read the JB Hi-Fi gaming headsets page, what do you want to know about it"?

**4. For analytics/Semrush pages:**
- Extract visible data into tables/CSV?
- Or just parse and be ready to answer questions?

Answer these three and I'll know exactly how to scope the skill.

---

### 13. **Human** — 2026-04-07T04:05

2 yes
3 claude should tell me what the page is, then ask me what i want
1. as above
2 yes
3 claude should tell me what the page is, then ask me what i want
1. as above

---

### 14. **Claude** — 2026-04-07T04:05

Perfect. Now I have what I need.

**Final confirmation before we build:**

The skill will:
1. **Auto-trigger** on any uploaded `.mhtml` file
2. **Detect the type** (AI conversation vs. web page vs. analytics tool)
3. **For AI conversations**: Extract full transcript, summarize what was being worked on, identify findings/assumptions/next steps, then ask what you want to do
4. **For web pages & analytics**: Identify the page/tool, briefly state what it is, then ask what you want to analyze

**Critical design question:** 

MHTML files are massive (10k–90k lines of quoted-printable HTML). Reading them is token-expensive. Should the skill:

- **A)** Use `strings` + `grep` to extract text content quickly (lossy but fast)
- **B)** Use Python with `email` library to parse MHTML properly and extract HTML, then use a headless browser or BeautifulSoup to get clean text (accurate but slower)
- **C)** Smart hybrid: Quick extraction for initial summary, then offer deep parse if you need it

My recommendation: **C — hybrid approach**. Quick scan for the summary, then if you need detailed analysis (e.g., "extract all the PLP copy from this JB Hi-Fi page"), it does a proper parse.

Agree?
 Perfect. Now I have what I need.

**Final confirmation before we build:**

The skill will:
1. **Auto-trigger** on any uploaded `.mhtml` file
2. **Detect the type** (AI conversation vs. web page vs. analytics tool)
3. **For AI conversations**: Extract full transcript, summarize what was being worked on, identify findings/assumptions/next steps, then ask what you want to do
4. **For web pages & analytics**: Identify the page/tool, briefly state what it is, then ask what you want to analyze

**Critical design question:** 

MHTML files are massive (10k–90k lines of quoted-printable HTML). Reading them is token-expensive. Should the skill:

- **A)** Use `strings` + `grep` to extract text content quickly (lossy but fast)
- **B)** Use Python with `email` library to parse MHTML properly and extract HTML, then use a headless browser or BeautifulSoup to get clean text (accurate but slower)
- **C)** Smart hybrid: Quick extraction for initial summary, then offer deep parse if you need it

My recommendation: **C — hybrid approach**. Quick scan for the summary, then if you need detailed analysis (e.g., "extract all the PLP copy from this JB Hi-Fi page"), it does a proper parse.

Agree?

---

### 15. **Human** — 2026-04-07T04:05

you picl
you picl

---

### 16. **Claude** — 2026-04-07T04:08

**B — Proper parsing.**

Here's why: You're using these files for SEO work where precision matters. A lossy `strings` extraction might miss structured data, mangle copy formatting, or drop context that's critical for competitor analysis. The token cost is acceptable because:

1. You're not uploading dozens of MHTMLs per conversation
2. You need accurate transcripts from AI conversations to resume work
3. Competitor page analysis requires clean text extraction (PLP copy character counts, metadata, heading structure)
4. Your use case is "understand this completely" not "skim 50 files quickly"

The hybrid approach sounds pragmatic but adds complexity and a second decision point ("do I need the deep parse?"). That friction isn't worth it when the proper parse should just work the first time.

Let's build it with proper MHTML parsing. I'll create the skill now.
```
This block is not supported on your current device yet.
```

Now I'll create the MHTML reading skill:
```
This block is not supported on your current device yet.
```

Now let's create a few test cases and run them to validate the skill works:
```
This block is not supported on your current device yet.
```

Now let's test the skill by actually running it on one of your MHTML files:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good! The script works. Now let's test on a competitor page:
```
This block is not supported on your current device yet.
```

Perfect! The extraction is working. Now let me create a proper test case using the skill to demonstrate how it should respond:

## Test Case 1: AI Conversation (Claude)

**Given file:** `Click_Frenzy_FAQ_alignment_-_Claude.mhtml`

**Skill response should be:**

This is a **Claude conversation** titled "Click Frenzy FAQ alignment" from March 25, 2026.

**Topic:** Writing FAQ copy for The Good Guys Click Frenzy 2025 events

**Key work completed:**
- FAQ content covering four Click Frenzy 2025 events: PayPal Frenzy (March 4–10), Mayhem Sale (May 13–16), and two others
- Questions addressed: what Click Frenzy is, TGG participation, event timing, duration, online vs. in-store availability

**Where it left off:**
The conversation produced FAQ drafts. No indication of whether the content was approved, edited further, or deployed.

What would you like to do with this conversation?

---

Let me now demonstrate how the skill would handle this properly:
```
This block is not supported on your current device yet.
```

Good. Now let's package the skill for you:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

---

## Done. Here's your MHTML reader skill.

**What it does:**

1. **Auto-triggers** when you upload any `.mhtml` file
2. **Detects the type**: AI conversation, competitor/research page, or analytics tool
3. **Extracts intelligently** using proper MHTML parsing (not naive text extraction)
4. **Responds contextually**:
   - **AI conversations** → Summarizes topic, findings, next steps, asks what you want
   - **Web pages** → States domain/page type, shows title/meta/H1, asks what to analyze
   - **Analytics** → Identifies tool/report, mentions data, asks what to extract

**Installation:** Download the `.skill` file above and install it in Claude Code.

**What I built differently than you might expect:**

- I went with **proper MHTML parsing** (Python `email` + BeautifulSoup) instead of quick-and-dirty text extraction. Your SEO work needs precision (character counts, heading structure, metadata). Lossy extraction would break that.
- The skill **auto-triggers on upload** rather than requiring you to say "read this MHTML" every time. If this gets annoying (e.g., when batch-uploading), we can change it.
- I kept the **SKILL.md under 500 lines** as recommended, with all the parsing logic shown as example code rather than bundled as a separate script file.

**Weaknesses to watch for:**

1. **AI conversation parsing is generic** — it extracts text but doesn't parse platform-specific conversation structure (user/assistant turns). If you need that, we'd add platform-specific HTML parsers.
2. **No deep competitor analysis yet** — it identifies the page but doesn't automatically extract PLP intro copy, count products, or audit internal links. Those would be follow-up questions you'd ask after the initial read.
3. **Token cost** — MHTML files are big (10k–90k lines). The proper parse is accurate but expensive. If you're hitting token limits, we can add summarization.

Try it on a few of your files and tell me what breaks or what's missing.
 **B — Proper parsing.**

Here's why: You're using these files for SEO work where precision matters. A lossy `strings` extraction might miss structured data, mangle copy formatting, or drop context that's critical for competitor analysis. The token cost is acceptable because:

1. You're not uploading dozens of MHTMLs per conversation
2. You need accurate transcripts from AI conversations to resume work
3. Competitor page analysis requires clean text extraction (PLP copy character counts, metadata, heading structure)
4. Your use case is "understand this completely" not "skim 50 files quickly"

The hybrid approach sounds pragmatic but adds complexity and a second decision point ("do I need the deep parse?"). That friction isn't worth it when the proper parse should just work the first time.

Let's build it with proper MHTML parsing. I'll create the skill now.
Now I'll create the MHTML reading skill:
Now let's create a few test cases and run them to validate the skill works:
Now let's test the skill by actually running it on one of your MHTML files:
Good! The script works. Now let's test on a competitor page:
Perfect! The extraction is working. Now let me create a proper test case using the skill to demonstrate how it should respond:

## Test Case 1: AI Conversation (Claude)

**Given file:** `Click_Frenzy_FAQ_alignment_-_Claude.mhtml`

**Skill response should be:**

This is a **Claude conversation** titled "Click Frenzy FAQ alignment" from March 25, 2026.

**Topic:** Writing FAQ copy for The Good Guys Click Frenzy 2025 events

**Key work completed:**
- FAQ content covering four Click Frenzy 2025 events: PayPal Frenzy (March 4–10), Mayhem Sale (May 13–16), and two others
- Questions addressed: what Click Frenzy is, TGG participation, event timing, duration, online vs. in-store availability

**Where it left off:**
The conversation produced FAQ drafts. No indication of whether the content was approved, edited further, or deployed.

What would you like to do with this conversation?

---

Let me now demonstrate how the skill would handle this properly:
Good. Now let's package the skill for you:
---

## Done. Here's your MHTML reader skill.

**What it does:**

1. **Auto-triggers** when you upload any `.mhtml` file
2. **Detects the type**: AI conversation, competitor/research page, or analytics tool
3. **Extracts intelligently** using proper MHTML parsing (not naive text extraction)
4. **Responds contextually**:
   - **AI conversations** → Summarizes topic, findings, next steps, asks what you want
   - **Web pages** → States domain/page type, shows title/meta/H1, asks what to analyze
   - **Analytics** → Identifies tool/report, mentions data, asks what to extract

**Installation:** Download the `.skill` file above and install it in Claude Code.

**What I built differently than you might expect:**

- I went with **proper MHTML parsing** (Python `email` + BeautifulSoup) instead of quick-and-dirty text extraction. Your SEO work needs precision (character counts, heading structure, metadata). Lossy extraction would break that.
- The skill **auto-triggers on upload** rather than requiring you to say "read this MHTML" every time. If this gets annoying (e.g., when batch-uploading), we can change it.
- I kept the **SKILL.md under 500 lines** as recommended, with all the parsing logic shown as example code rather than bundled as a separate script file.

**Weaknesses to watch for:**

1. **AI conversation parsing is generic** — it extracts text but doesn't parse platform-specific conversation structure (user/assistant turns). If you need that, we'd add platform-specific HTML parsers.
2. **No deep competitor analysis yet** — it identifies the page but doesn't automatically extract PLP intro copy, count products, or audit internal links. Those would be follow-up questions you'd ask after the initial read.
3. **Token cost** — MHTML files are big (10k–90k lines). The proper parse is accurate but expensive. If you're hitting token limits, we can add summarization.

Try it on a few of your files and tell me what breaks or what's missing.
