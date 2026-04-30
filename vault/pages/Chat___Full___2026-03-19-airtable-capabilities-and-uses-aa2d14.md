---
title: Airtable capabilities and uses (full)
parent: Chat/Light/2026-03-19-airtable-capabilities-and-uses-aa2d14
uuid: aa2d1486-f300-46c8-93e1-708adc5a4fec
---

#chat/full #project/airtable-plp-copy-tracker #status/completed

# Airtable capabilities and uses — Full Transcript

→ Light view: [[Chat/Light/2026-03-19-airtable-capabilities-and-uses-aa2d14]]
→ Medium view: [[Chat/Medium/2026-03-19-airtable-capabilities-and-uses-aa2d14]]

**Messages:** 10 | **Date:** 2026-03-19

---

### 1. **Human** — 2026-03-19T01:21

what can you do with airtable
what can you do with airtable

---

### 2. **Claude** — 2026-03-19T01:21

```
This block is not supported on your current device yet.
```

Here's what's available through the Airtable connection:

**Reading data**
- List all bases in your account
- List all tables and their field schemas within any base
- Query and filter records from any table (with sorting, filtering, field selection)
- Search for bases by name

**Writing data**
- Create new records in any table
- Update existing records
- Create new tables in a base
- Create new fields on an existing table
- Rename or update descriptions for tables and fields

**Practical use cases for your workflow:**

Given your SEO context, some concrete things this unlocks: building a keyword tracking or content audit database, logging PLP copy production status across hundreds of categories, managing a redirect mapping tracker, or maintaining a campaign/project registry. You could also use it to pipe Semrush data into an Airtable base and track it over time.

Want to take a look at what bases you currently have set up?
Here's what's available through the Airtable connection:

**Reading data**
- List all bases in your account
- List all tables and their field schemas within any base
- Query and filter records from any table (with sorting, filtering, field selection)
- Search for bases by name

**Writing data**
- Create new records in any table
- Update existing records
- Create new tables in a base
- Create new fields on an existing table
- Rename or update descriptions for tables and fields

**Practical use cases for your workflow:**

Given your SEO context, some concrete things this unlocks: building a keyword tracking or content audit database, logging PLP copy production status across hundreds of categories, managing a redirect mapping tracker, or maintaining a campaign/project registry. You could also use it to pipe Semrush data into an Airtable base and track it over time.

Want to take a look at what bases you currently have set up?

---

### 3. **Human** — 2026-03-19T01:32

Create a example table
Create a example table

---

### 4. **Claude** — 2026-03-19T01:32

First, let me find a base to create the table in.
```
This block is not supported on your current device yet.
```

No bases exist in your account yet, so there's nowhere to create a table. To proceed, I'd need to either:

1. **Create a new base first** — the current MCP connection doesn't include a `create_base` tool, so this would need to be done manually in Airtable.
2. **Use an existing base** — if you create a blank base in Airtable and share the base ID, I can build the table inside it straight away.

To create a base manually: log into [airtable.com](https://airtable.com), hit **Add a base**, give it a name (e.g. "SEO Workspace"), and then come back with the base ID from the URL (it looks like `appXXXXXXXXXXXXXX`). From there I can scaffold a table with fields, populate it with example records, and you'll have something live to work with.

Want to do that, or would a different approach suit better?
 First, let me find a base to create the table in.
No bases exist in your account yet, so there's nowhere to create a table. To proceed, I'd need to either:

1. **Create a new base first** — the current MCP connection doesn't include a `create_base` tool, so this would need to be done manually in Airtable.
2. **Use an existing base** — if you create a blank base in Airtable and share the base ID, I can build the table inside it straight away.

To create a base manually: log into [airtable.com](https://airtable.com), hit **Add a base**, give it a name (e.g. "SEO Workspace"), and then come back with the base ID from the URL (it looks like `appXXXXXXXXXXXXXX`). From there I can scaffold a table with fields, populate it with example records, and you'll have something live to work with.

Want to do that, or would a different approach suit better?

---

### 5. **Human** — 2026-03-19T01:37

[REDACTED-AIRTABLE-PAT]
[REDACTED-AIRTABLE-PAT]

---

### 6. **Claude** — 2026-03-19T01:37

That looks like an Airtable API key — I'd recommend not sharing that in chat. You should rotate it immediately at [airtable.com/create/tokens](https://airtable.com/create/tokens) to prevent unauthorised access to your account.

To connect Airtable properly, the integration is already authorised through your Claude.ai connector (which is how the tools above were working). You don't need to paste an API key here.

To get a base ID: open a base in Airtable, look at the URL, and copy the segment starting with `app` — it'll look like `appXXXXXXXXXXXXXX`. Share just that and I can create the example table from there.
 That looks like an Airtable API key — I'd recommend not sharing that in chat. You should rotate it immediately at [airtable.com/create/tokens](https://airtable.com/create/tokens) to prevent unauthorised access to your account.

To connect Airtable properly, the integration is already authorised through your Claude.ai connector (which is how the tools above were working). You don't need to paste an API key here.

To get a base ID: open a base in Airtable, look at the URL, and copy the segment starting with `app` — it'll look like `appXXXXXXXXXXXXXX`. Share just that and I can create the example table from there.

---

### 7. **Human** — 2026-03-19T01:42

https://airtable.com/appS4NfrOth5cVo7P/tblaIo1av7sgtwlzR/viwsaqcq2JrHmPGTR
https://airtable.com/appS4NfrOth5cVo7P/tblaIo1av7sgtwlzR/viwsaqcq2JrHmPGTR

---

### 8. **Claude** — 2026-03-19T01:42

Got it. Base ID is `appS4NfrOth5cVo7P`. Let me check what's already in there, then create an example table.
```
This block is not supported on your current device yet.
```

There's already a solid SEO base in there with three linked tables: Campaigns, Keywords, and Rankings. Rather than creating a generic example table, I can add something more useful alongside these. A few options that would complement what's already there:
```
This block is not supported on your current device yet.
```


 Got it. Base ID is `appS4NfrOth5cVo7P`. Let me check what's already in there, then create an example table.
There's already a solid SEO base in there with three linked tables: Campaigns, Keywords, and Rankings. Rather than creating a generic example table, I can add something more useful alongside these. A few options that would complement what's already there:

---

### 9. **Human** — 2026-03-19T01:45

Q: What example table would you like added to the base?
A: PLP Copy Tracker (URL, status, intro copy, metadata)
Q: What example table would you like added to the base?
A: PLP Copy Tracker (URL, status, intro copy, metadata)

---

### 10. **Claude** — 2026-03-19T01:46

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Table created. Now populating it with example records across a few realistic TGG categories.
```
This block is not supported on your current device yet.
```

Done. The **PLP Copy Tracker** table is live in your base with 10 fields and 5 example rows:

| Page | Status | Notes |
|---|---|---|
| Televisions | Live | 196 char intro, meta populated |
| Washing Machines | QA | Intro slightly under 230 floor, flagged |
| Robot Vacuums | In Progress | Intro blank, AI visibility gap noted |
| Laptops | Not Started | Blank, flagged as high priority |
| Air Conditioners | Written | 212 chars, needs expansion before QA |

Fields included: Page URL, Category, Copy Status (colour-coded select), PLP Intro Copy, Intro Char Count, Meta Title, Meta Description, Meta Title Chars, Meta Desc Chars, and Notes.

You can view it directly at [airtable.com/appS4NfrOth5cVo7P](https://airtable.com/appS4NfrOth5cVo7P). From here it would be straightforward to bulk-import your full category list, use filtered views by status, or pipe copy output from Claude Code directly into rows via the API.
Table created. Now populating it with example records across a few realistic TGG categories.
Done. The **PLP Copy Tracker** table is live in your base with 10 fields and 5 example rows:

| Page | Status | Notes |
|---|---|---|
| Televisions | Live | 196 char intro, meta populated |
| Washing Machines | QA | Intro slightly under 230 floor, flagged |
| Robot Vacuums | In Progress | Intro blank, AI visibility gap noted |
| Laptops | Not Started | Blank, flagged as high priority |
| Air Conditioners | Written | 212 chars, needs expansion before QA |

Fields included: Page URL, Category, Copy Status (colour-coded select), PLP Intro Copy, Intro Char Count, Meta Title, Meta Description, Meta Title Chars, Meta Desc Chars, and Notes.

You can view it directly at [airtable.com/appS4NfrOth5cVo7P](https://airtable.com/appS4NfrOth5cVo7P). From here it would be straightforward to bulk-import your full category list, use filtered views by status, or pipe copy output from Claude Code directly into rows via the API.
