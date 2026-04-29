---
name: tgg-conversation-indexer
description: Weekly conversation indexer for Simon Mannheimer's TGG SEO work. Scans recent Claude conversations, scores them for significance, appends significant ones to the master index file, and writes abandoned high-upside projects to a todo markdown file. Trigger when asked to "update conversation index", "run indexer", "check abandoned projects", or "what have I left unfinished". Also trigger on any scheduled indexer run prompt. This skill must be used for any task involving conversation history indexing, project abandonment detection, or todo generation from past chats.
---

# TGG Conversation Indexer

Scans recent conversations, scores significance, updates the master index, and flags abandoned projects with upside to a todo file.

---

## Trigger prompt (for scheduled use)

> Run tgg-conversation-indexer. Scan conversations since last run, score significance, append to index, flag abandoned projects with upside, update todo.

---

## Drive file names (fixed — do not change between runs)

| Purpose | File name in Drive |
|---|---|
| All-time master index | `TGG SEO — Claude Session Index All Time` |
| Monthly index (current month) | `TGG SEO — Claude Session Index [Month YYYY]` |
| Abandoned projects todo | `TGG SEO — Abandoned Projects Todo` |
| Last run timestamp | `TGG SEO — Indexer Last Run` |

All three files live in Google Drive root. Search by exact name each run using `search_files`.

---

## Step 1 — Establish last run date

Search Drive for `TGG SEO — Indexer Last Run` using `search_files`. If found, read its contents with `read_file_contents` to get the ISO datetime. If not found, default to 7 days ago.

All conversations with `updated_at` after this datetime are candidates.

---

## Step 2 — Fetch candidate conversations

Call `recent_chats` with `n=20` and paginate with `before` if needed until you reach the last run date. Collect all conversations with `updated_at` after last run date.

---

## Step 3 — Score each conversation for significance

Score each conversation on the following criteria. Each criterion = 1 point.

| Criterion | Signal |
|---|---|
| Named deliverable | File produced: XLSX, DOCX, PPTX, CSV, script, regex, copy block |
| Named TGG project or workstream | References a known ongoing project by name |
| 5+ turns | Conversation has substantial back-and-forth |
| Project keyword present | schema, feed, blog, EOFY, GMC, 404, Contentful, Shopify, Screaming Frog, Semrush, Profound, Airtable, AEO, inlink, PLP, PDP, redirect, sitemap, crawl, meta, copy, keyword, GSC, GA4, Merchant Center |
| Lasting effect | Produced a skill update, process change, permanent rule, or decision that carries forward |

**Thresholds:**
- Score 0–1 → Closed/Tactical. Add to index Closed section only, no todo entry.
- Score 2–3 → Completed Deliverable or Active Project. Classify based on whether outcome was reached.
- Score 4–5 → Active Project or major Completed Deliverable.

---

## Step 4 — Classify each significant conversation

For each conversation scoring 2+:

**If outcome was clearly reached** (file delivered, decision made, task closed) → Completed Deliverable.

**If work is in-flight or ended mid-task** → Active Project. Estimate % complete based on what was done vs what was described as needed.

**Abandonment flag:** An Active Project is flagged as Abandoned With Upside if ALL of the following are true:
- Already exists in the index as Active (i.e., was indexed in a prior run)
- Last `updated_at` is 14+ days ago
- Has a named deliverable in-flight OR an open decision/Jira/implementation pending
- Upside signal: the project has commercial impact, ranking impact, or reduces a known risk (404s, schema gaps, feed errors, AIO visibility)

---

## Step 5 — Update the master index file in Drive

Search Drive for `TGG SEO — Claude Session Index [current Month YYYY]` (e.g. `TGG SEO — Claude Session Index May 2026`).

**If the file exists:** Read its contents with `read_file_contents`. Append new entries to the relevant sections. Overwrite the file using `create_file` with the full updated content.

**If the file does not exist (new month):** Search for the prior month's index. Read it. Extract all Active Projects. Create a new file named `TGG SEO — Claude Session Index [Month YYYY]` containing:
- All carried-forward Active Projects (unchanged)
- Empty Completed Deliverables section
- Empty Closed/Tactical section
- Updated counts table

Then append this run's new entries.

**In all cases:**
- Append new Completed Deliverables to the Completed section
- Append new Active Projects to the Active section with % complete and Still Needed list
- Move any existing Active Projects that are now complete to Completed
- Update the counts table at the bottom
- Do NOT re-index conversations already present — match on chat URL to deduplicate

---

## Step 6 — Write abandoned projects to todo in Drive

Search Drive for `TGG SEO — Abandoned Projects Todo`.

**If found:** Read contents. Append only newly flagged projects not already listed (match on project name). Overwrite file with updated content using `create_file`.

**If not found:** Create the file with a header and the new entries.

Each todo entry format:

```
### [Project Name]
**Last active:** YYYY-MM-DD
**Chat:** https://claude.ai/chat/[uuid]
**What was in-flight:** [1–2 sentences]
**Why it has upside:** [1 sentence — commercial, ranking, or risk signal]
**Re-entry prompt:** "[Paste this to continue the project]"

---
```

---

## Step 7 — Update last run timestamp in Drive

Search Drive for `TGG SEO — Indexer Last Run`. Overwrite (or create) it with the current ISO datetime as its entire content. This is the anchor for the next run.

---

## Output summary (print to chat)

After each run, print:

```
Indexer run complete — [DATE]
Conversations scanned: N
New significant conversations: N
  — Completed deliverables added: N
  — Active projects added: N
Abandoned with upside flagged: N (added to TGG SEO — Abandoned Projects Todo in Drive)
Index file updated: TGG SEO — Claude Session Index [Month YYYY]
```

---

## Notes

- File names are fixed and exact — always search by the full name string above. Do not vary capitalisation or punctuation.
- If `create_file` overwrites an existing file, pass the full updated content — not just the new section. Partial writes will corrupt the file.
- If a conversation's summary is truncated, use `conversation_search` with a distinctive keyword to get fuller context before scoring.
- Significance scoring is pass/fail per criterion — no partial points.
- When in doubt on classification, default to Active rather than Completed.
- Month rollover happens automatically when the current month's index file does not exist yet. Always carry forward all Active projects — never drop them.
- **Project conversations are invisible to `recent_chats`.** Conversations inside Claude Projects (EOFY, Monthly SEO Update, Blog inventory, testing pdpd, Compass OS, etc.) do not appear in `recent_chats` results. If Simon uploads a `skills_reference.zip` alongside a run, scan the `example_conversations.md` files in each skill folder for UUIDs and titles not already in the index and add them. This is the only way to capture Project-based work.
- The all-time master index is named `TGG SEO — Claude Session Index All Time` in Drive. Monthly indexes are named `TGG SEO — Claude Session Index [Month YYYY]`. The all-time index is seeded manually; monthly indexes are auto-maintained by this skill.
