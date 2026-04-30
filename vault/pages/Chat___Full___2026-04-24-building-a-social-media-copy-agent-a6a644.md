---
title: Building a social media copy agent (full)
parent: Chat/Light/2026-04-24-building-a-social-media-copy-agent-a6a644
uuid: a6a644c6-7668-4bb3-9e61-2031f60fad92
---

#chat/full #project/main #status/active

# Building a social media copy agent — Full Transcript

→ Light view: [[Chat/Light/2026-04-24-building-a-social-media-copy-agent-a6a644]]
→ Medium view: [[Chat/Medium/2026-04-24-building-a-social-media-copy-agent-a6a644]]

**Messages:** 6 | **Date:** 2026-04-24

---

### 1. **Human** — 2026-04-24T00:09

how would i build an agent to do social copy
how would i build an agent to do social copy

---

### 2. **Claude** — 2026-04-24T00:09

```
This block is not supported on your current device yet.
```

Here's how to build a social copy agent in Profound. The design depends on what you're feeding it, but here's the most practical version:

---

## Social Copy Agent — Recommended Design

**Use case:** Given a URL (article, product page, or campaign), generate platform-specific social copy.

**Flow:**

```
Start → Web Page Scrape → Extract Key Message (LLM) → Generate Social Copy (LLM) → End
```

**Inputs:**
- `Page URL` (string, required)
- `Brand Name` (string, required)
- `Platform` (string, optional — e.g. LinkedIn, Instagram, X)
- `Tone` (string, optional — e.g. informative, promotional, conversational)

---

**Node 1 — Web Page Scrape**
- URL: `{{page_url}}`
- Formats: markdown, only main content: true

**Node 2 — Extract Key Message (Prompt LLM)**
- Model: GPT-4o mini
- Prompt:
```
From the following page content, extract:
1. The core message or offer in one sentence
2. 3 key supporting points
3. Any specific product names, prices, or claims worth highlighting

Brand: {{brand_name}}
Content: {{scraped_content}}

Return as plain text, no formatting.
```

**Node 3 — Generate Social Copy (Prompt LLM)**
- Model: GPT-5 mini (or GPT-4o mini if credits are tight)
- Prompt:
```
Write social media copy for {{brand_name}} based on the following page content.

Core message: {{key_message}}
Platform: {{platform}} (if blank, generate for LinkedIn, Instagram, and X)
Tone: {{tone}} (if blank, default to informative and direct)

Requirements:
- LinkedIn: 100–150 words, no hashtags, professional but human
- Instagram: 80–100 words, 3–5 relevant hashtags, punchy opener
- X: Under 280 chars, include 1–2 hashtags

Output exactly this format:
## LinkedIn
[copy]

## Instagram
[copy]

## X
[copy]
```

---

## Variations worth considering

**If you want to pull from a YouTube video instead of a URL**, swap the scrape node for `YouTube Title & Description` + `YouTube Video Transcript` (see template #5). The key message LLM reads the transcript instead.

**If you're running this at batch scale** from a sheet (e.g. a list of product URLs), wrap it in the sheet-based pattern you've already built in v9. The write-back node saves the copy to a Google Doc and links it back to the sheet.

**If you need brand voice consistency**, add a `Use Brand Kit` node before the final LLM, or add your brand voice rules directly into the system prompt.

---

Want me to produce the full JSON for this, or do you want to start with a specific variant first?
Here's how to build a social copy agent in Profound. The design depends on what you're feeding it, but here's the most practical version:

---

## Social Copy Agent — Recommended Design

**Use case:** Given a URL (article, product page, or campaign), generate platform-specific social copy.

**Flow:**

```
Start → Web Page Scrape → Extract Key Message (LLM) → Generate Social Copy (LLM) → End
```

**Inputs:**
- `Page URL` (string, required)
- `Brand Name` (string, required)
- `Platform` (string, optional — e.g. LinkedIn, Instagram, X)
- `Tone` (string, optional — e.g. informative, promotional, conversational)

---

**Node 1 — Web Page Scrape**
- URL: `{{page_url}}`
- Formats: markdown, only main content: true

**Node 2 — Extract Key Message (Prompt LLM)**
- Model: GPT-4o mini
- Prompt:
```
From the following page content, extract:
1. The core message or offer in one sentence
2. 3 key supporting points
3. Any specific product names, prices, or claims worth highlighting

Brand: {{brand_name}}
Content: {{scraped_content}}

Return as plain text, no formatting.
```

**Node 3 — Generate Social Copy (Prompt LLM)**
- Model: GPT-5 mini (or GPT-4o mini if credits are tight)
- Prompt:
```
Write social media copy for {{brand_name}} based on the following page content.

Core message: {{key_message}}
Platform: {{platform}} (if blank, generate for LinkedIn, Instagram, and X)
Tone: {{tone}} (if blank, default to informative and direct)

Requirements:
- LinkedIn: 100–150 words, no hashtags, professional but human
- Instagram: 80–100 words, 3–5 relevant hashtags, punchy opener
- X: Under 280 chars, include 1–2 hashtags

Output exactly this format:
## LinkedIn
[copy]

## Instagram
[copy]

## X
[copy]
```

---

## Variations worth considering

**If you want to pull from a YouTube video instead of a URL**, swap the scrape node for `YouTube Title & Description` + `YouTube Video Transcript` (see template #5). The key message LLM reads the transcript instead.

**If you're running this at batch scale** from a sheet (e.g. a list of product URLs), wrap it in the sheet-based pattern you've already built in v9. The write-back node saves the copy to a Google Doc and links it back to the sheet.

**If you need brand voice consistency**, add a `Use Brand Kit` node before the final LLM, or add your brand voice rules directly into the system prompt.

---

Want me to produce the full JSON for this, or do you want to start with a specific variant first?

---

### 3. **Human** — 2026-04-24T00:10

generate a flow visual
generate a flow visual

---

### 4. **Claude** — 2026-04-24T00:10

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Click any node to ask a follow-up about it. The dashed line on the left shows the error path if the scrape returns nothing. The three output boxes at the bottom split by platform, then converge into a single End node carrying the full package.

Want me to add a sheet-based batch variant or a Brand Kit branch to this?
 
Click any node to ask a follow-up about it. The dashed line on the left shows the error path if the scrape returns nothing. The three output boxes at the bottom split by platform, then converge into a single End node carrying the full package.

Want me to add a sheet-based batch variant or a Brand Kit branch to this?

---

### 5. **Human** — 2026-04-24T00:12

How do I add a Google Docs write-back to this agent?
How do I add a Google Docs write-back to this agent?

---

### 6. **Claude** — 2026-04-24T00:12

```
This block is not supported on your current device yet.
```
