---
name: skill-zip-sync
description: Syncs skill ZIPs from Google Drive to the GitHub repo. Runs in Claude Code only. Claude.ai produces and uploads the timestamped ZIPs; Claude Code processes them. Finds timestamped skill ZIPs (format: skill-name_YYYYMMDD-HHMM.zip), picks the latest per skill, extracts to .claude/skills/, commits with metadata, pushes to GitHub, then deletes all processed ZIPs from Drive. Run on a routine schedule or manually.
---

# skill-zip-sync

Pulls the latest skill ZIPs from Google Drive into the repo, commits them, and cleans up Drive.

---

## Step 1 — List skill ZIPs in Drive

Search Drive root for all `.zip` files matching the pattern `[skill-name]_[YYYYMMDD-HHMM].zip`.

- `skill-name`: lowercase letters, numbers, hyphens only
- `timestamp`: exactly `YYYYMMDD-HHMM` format

Return `{name, fileId, modifiedTime}` for each match. Ignore any ZIPs that don't match this pattern.

---

## Step 2 — Group by skill, select latest

1. Parse each filename: split on the last `_` to get `skill-name` and `timestamp`
2. Group all ZIPs by `skill-name`
3. Sort each group by `timestamp` descending
4. Select the newest ZIP per skill to process
5. All others in the group are stale — collect their `fileId` values for deletion in Step 5

Check `.claude/skills/[skill-name]/.last_sync` in the repo. If the latest ZIP timestamp is not newer than `.last_sync`, skip that skill entirely (already current).

---

## Step 3 — Download and extract

For each skill selected in Step 2:

1. Download the ZIP using `fileId`
2. Save to `/tmp/[skill-name]_[timestamp].zip`
3. If `.claude/skills/[skill-name]/` exists, delete its contents but preserve `.last_sync`
4. Extract ZIP to `.claude/skills/[skill-name]/`
5. Read `metadata.json` from the extracted folder:
   - `change` — commit message body
   - `timestamp` — ISO datetime for `.last_sync`
6. Remove `metadata.json` from the extracted folder (sync-only, not part of the skill)

---

## Step 4 — Commit each skill

For each extracted skill:

1. Stage: `git add .claude/skills/[skill-name]/`
2. Commit:
   ```
   feat: Update [skill-name] skill

   [change from metadata.json]

   Synced from Claude.ai via Drive
   Timestamp: [timestamp]
   ```
3. Write the ZIP timestamp to `.claude/skills/[skill-name]/.last_sync`
4. Stage and amend: `git add .claude/skills/[skill-name]/.last_sync && git commit --amend --no-edit`

---

## Step 5 — Delete all processed ZIPs from Drive

For every ZIP found in Step 1 (latest and stale), delete from Drive using the Drive MCP delete tool.

This includes the ZIP just processed and any older stale ZIPs for the same skill. Drive should be empty of skill ZIPs after a successful run.

If extraction or commit failed for a skill in Step 3-4, do NOT delete that skill's ZIPs. Leave them for retry on next run.

---

## Step 6 — Push to GitHub

```
git push origin main
```

If push fails due to conflict, pull with rebase then push again.

---

## Output summary

```
skill-zip-sync complete — [DATE]
Skills checked: N
Skills updated: N
  — [skill-name]: [change description]
Skills already current: N
ZIPs deleted from Drive: N
Pushed to GitHub: YES / NO
```

---

## Notes

- Only ZIPs matching `[skill-name]_[YYYYMMDD-HHMM].zip` are processed. All other ZIPs in Drive root are ignored.
- If two ZIPs have identical timestamps for the same skill, pick either and delete both after.
- If Drive delete is unavailable, log a warning and list fileIds needing manual cleanup.
