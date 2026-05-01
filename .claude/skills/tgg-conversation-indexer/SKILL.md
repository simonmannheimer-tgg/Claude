---
name: tgg-conversation-indexer
description: Weekly conversation indexer for Simon Mannheimer's TGG SEO work. Scans recent Claude conversations, scores them for significance, appends significant ones to the master index file, and writes abandoned high-upside projects to a todo markdown file. Also tracks skills export cadence and outputs an aside prompt when a weekly export is due. Trigger when asked to "update conversation index", "run indexer", "check abandoned projects", or "what have I left unfinished". Also trigger on any scheduled indexer run prompt. This skill must be used for any task involving conversation history indexing, project abandonment detection, or todo generation from past chats. Depends on skill-zip-sync filename pattern (skill-name_YYYYMMDD-HHMM.zip) for auto-sync of skill changes. Reads/writes 5 hardcoded Drive files (TGG SEO — Indexer Last Run, TGG SEO — Skills Export Last Date, TGG SEO — Active Sprint, TGG SEO — Claude Session Index [Month YYYY], TGG SEO — Abandoned Projects Todo).
---

# TGG Conversation Indexer

Scans recent conversations, scores significance, updates the master index, flags abandoned projects, and tracks when a skills export is due.

---

## Trigger prompt (for scheduled use)

> Run tgg-conversation-indexer. Scan conversations since last run, score significance, append to index, flag abandoned projects with upside, update todo, check if skills export is due.

---

## Drive file names (fixed — do not change between runs)

| Purpose | File name in Drive |
|---|---|
| All-time master index | `TGG SEO — Claude Session Index All Time` |
| Monthly index (current month) | `TGG SEO — Claude Session Index [Month YYYY]` |
| Abandoned projects todo | `TGG SEO — Abandoned Projects Todo` |
| Last run timestamp | `TGG SEO — Indexer Last Run` |
| Last skills export timestamp | `TGG SEO — Skills Export Last Date` |

All files live in Google Drive root. Search by exact name each run using `search_files`.

---

## Step 0 — Check skills export cadence (run first, silently)

Search Drive for `TGG SEO — Skills Export Last Date`. If found, read its contents to get the last export ISO datetime. If not found, the export is overdue.

Calculate days since last export. If **7 or more days** have passed (or file not found), set `export_due = true`. Otherwise `export_due = false`. Do not output anything yet — this is recorded and used in the output summary at the end.

---

## Step 1 — Establish last run date

Search Drive for `TGG SEO — Indexer Last Run` using `search_files`. If found, read its contents to get the ISO datetime. If not found, default to 7 days ago.

All conversations with `updated_at` after this datetime are candidates.

---

## Step 2 — Fetch candidate conversations

Call `recent_chats` with `n=20` and paginate with `before` if needed until the last run date. Collect all conversations with `updated_at` after last run date.

**Also check for sprint activity:** Search Drive for `TGG SEO — Active Sprint` and read its contents. If it contains recently completed work or mentions specific chat URLs, extract those chat UUIDs and add them to candidates even if they're older than the last run date. This ensures sprint completion gets indexed.

If a `skills_reference.zip` was uploaded alongside this run, scan the `example_conversations.md` files inside each skill folder. Extract any UUIDs and titles not already in the current index and treat them as additional candidates for scoring. This is the only way to capture conversations from Claude Projects.

---

## Step 3 — Score each conversation for significance

Score each conversation. Each criterion = 1 point. **For conversations with truncated content, use `conversation_search` to get full context before scoring, or check the verbatim archive in Drive (`tgg conversation archive 30apr26.zip` or similar) if available.**

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
- Already exists in the index as Active (indexed in a prior run)
- Last `updated_at` is 14+ days ago
- Has a named deliverable in-flight OR an open decision/Jira/implementation pending
- Upside signal: commercial impact, ranking impact, or reduces a known risk (404s, schema gaps, feed errors, AIO visibility)

---

## Step 5 — Update the master index file in Drive

Search Drive for `TGG SEO — Claude Session Index [current Month YYYY]` (e.g. `TGG SEO — Claude Session Index May 2026`).

**Before updating, merge sprint completions:** If any conversations referenced in the current Active Sprint (Drive: `TGG SEO — Active Sprint`) are now complete, mark those sprint items as completed in the index. Cross-reference sprint "committed" items against newly scored conversations to identify matches.

**If the file exists:** Read its contents. Append new entries. Overwrite using `create_file` with full updated content.

**If the file does not exist (new month):** Search for the prior month's index. Read it. Extract all Active Projects. Create a new file for the current month carrying forward all Active projects, then append this run's new entries.

**In all cases:**
- Append new Completed Deliverables to the Completed section
- Append new Active Projects with % complete and Still Needed list
- Move any Active Projects that are now complete to Completed
- Update sprint-to-index linkage for completed items
- Update the counts table
- Do NOT re-index conversations already present — match on chat URL to deduplicate

---

## Step 6 — Write abandoned projects to todo in Drive

Search Drive for `TGG SEO — Abandoned Projects Todo`.

If found: read contents, append only newly flagged projects not already listed, overwrite with full updated content.
If not found: create the file with a header and new entries.

Each entry format:
```
### [Project Name]
**Last active:** YYYY-MM-DD
**Chat:** https://claude.ai/chat/[uuid]
**What was in-flight:** [1–2 sentences]
**Why it has upside:** [1 sentence]
**Re-entry prompt:** "[Paste this to continue the project]"

---
```

---

## Step 7 — Update last run timestamp in Drive

Overwrite (or create) `TGG SEO — Indexer Last Run` with the current ISO datetime.

---

## Full rebuild (Option C)

For quarterly rebuilds using the complete conversation export (conversations.json from Claude account settings):

**When to use:** Quarterly or when the incremental index has gaps. Last run: 30 April 2026.

**Workflow:**
1. Download full export from Claude account settings (Settings → Data Export → Request Export)
2. Upload both parts (.zip files) to a new Claude conversation
3. Run this skill with "full rebuild mode" flag

**Process:**
- Extract conversations_part1.json + conversations_part2.json 
- Combine and deduplicate all conversations (277 conversations as of April 30)
- Theme-classify into ~20 streams (BFCM, EOFY, Blog AI Intros, Monthly SEO, etc.)
- Score all conversations, not just recent ones
- Rebuild the all-time index from scratch
- Generate verbatim archive for future reference
- Update git repo with patches

**Limitations:** Project conversations need content inference (no project_uuid in export). Keyword-based theme classification may miss nuanced project boundaries.

---

## Step 8 — Auto-sync skill changes to Drive

**If this skill was modified during this run**, upload a timestamped ZIP to Drive:

1. **Package complete skill directory:**
   - SKILL.md (primary file)
   - Any other files in the skill folder

2. **Name the ZIP with a timestamp:** `tgg-conversation-indexer_YYYYMMDD-HHMM.zip`
   - Example: `tgg-conversation-indexer_20260430-2140.zip`
   - Always create new, never attempt to replace or rename existing

3. **Include metadata.json in ZIP:**
   ```json
   {
     "skill": "tgg-conversation-indexer",
     "timestamp": "ISO datetime",
     "change": "brief description of what changed"
   }
   ```

4. **Upload to Drive root** using `Google Drive:create_file` with `mimeType: application/zip` and `disableConversionToGoogleType: true`

**Claude Code skill-zip-sync will:**
- Find all ZIPs matching `tgg-conversation-indexer_*.zip`
- Take the latest by timestamp
- Extract to `.claude/skills/tgg-conversation-indexer/`, commit, push
- Delete all ZIPs for this skill from Drive after successful commit

---

## Step 9 — Skills export aside (only if export_due = true)

If `export_due = true`, output the following block verbatim at the end of the run summary. Do not output this block if export_due = false.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 BY THE WAY — Skills export is due
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

It has been 7+ days since the last skills export. Project conversations
(EOFY, Monthly SEO Update, etc.) are invisible to this indexer unless
a fresh skills_reference.zip is uploaded with each run.

Open a new Claude window and paste this prompt:
───────────────────────────────────────
Zip all skills from /mnt/skills/user/ into a single skills_reference.zip.
Include all files that exist within each skill directory. Name the
output skills_reference.zip and present it for download.
───────────────────────────────────────

Then upload the downloaded zip to GitHub:
  Repo:   simonmannheimer-tgg/Claude
  Path:   .claude/skills/tgg-conversation-indexer/skills_reference.zip
  Method: GitHub web UI → navigate to path → Add file → Upload files

Once uploaded, paste the trigger prompt again with the zip attached
so this indexer can process project conversations from the export.

After completing the upload, update the export date in Drive:
  File: TGG SEO — Skills Export Last Date
  Content: [today's ISO date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

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
Skills export due: YES / NO (last export: [date or never])
```

Then output the aside block if applicable (Step 9).

---

## Notes

- File names are fixed and exact. Do not vary capitalisation or punctuation.
- If `create_file` overwrites an existing file, pass the full updated content. Partial writes corrupt the file.
- If a conversation's summary is truncated, use `conversation_search` with a distinctive keyword before scoring, or reference the verbatim archive if available in Drive.
- **Sprint integration:** Active Sprint completion checking happens at Step 5. Cross-reference sprint "committed" items against newly indexed conversations to detect completions.
- **Archive access:** If verbatim archive exists in Drive (`tgg conversation archive 30apr26.zip` or later), use it to get full conversation content for better scoring when `recent_chats` content is truncated.
- Significance scoring is pass/fail per criterion — no partial points.
- When in doubt on classification, default to Active rather than Completed.
- Month rollover happens automatically when the current month's index file does not exist. Always carry forward all Active projects.
- `recent_chats` is blind to Claude Projects (EOFY, Monthly SEO Update, Blog inventory, testing pdpd, Compass OS, etc.). The skills_reference.zip is the only way to capture project conversations. Upload it with the trigger prompt whenever the aside fires.
- The all-time master index (`TGG SEO — Claude Session Index All Time`) is seeded manually. Monthly indexes are auto-maintained by this skill.
- The `TGG SEO — Skills Export Last Date` file is updated manually by Simon after completing the upload. The indexer reads it but does not write to it automatically.
- **Option C full rebuild** documented above should be used quarterly or when incremental gaps are detected.
