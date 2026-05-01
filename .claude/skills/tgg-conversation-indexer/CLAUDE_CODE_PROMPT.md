# Claude Code Prompt — Skills Export + GitHub Sync

## Purpose
Generate a fresh `skills_reference.zip` from local skills, upload it to the GitHub repo at the path the conversation indexer expects, and update the export timestamp file. Run this every 7 days, or whenever the indexer's "skills export is due" aside fires.

---

## Paste this entire block into Claude Code

```
Run the skills export sync. Steps:

1. Zip every skill folder under /mnt/skills/user/ into a single skills_reference.zip in /tmp/. Each skill's folder must include its SKILL.md and example_conversations.md if present. Do not include nested zips, .DS_Store, or __pycache__.

2. Verify the zip:
   - Lists every skill folder name in /mnt/skills/user/
   - Each folder contains SKILL.md
   - Total uncompressed size under 50MB
   Print the file list and total count.

3. Use the GitHub MCP to upload the zip to:
   Repo:   simonmannheimer-tgg/Claude
   Branch: main
   Path:   .claude/skills/tgg-conversation-indexer/skills_reference.zip
   Commit: "chore: refresh skills_reference.zip — [today's ISO date]"

   If the file already exists at that path, overwrite it (use the existing file SHA).

4. Update the Drive file 'TGG SEO — Skills Export Last Date' with today's ISO date (YYYY-MM-DD). If the file doesn't exist, create it. Use the Google Drive MCP.

5. Print a final summary:
   - Skills exported: N
   - Zip size: X KB
   - GitHub commit URL
   - Drive file updated: YES/NO
   - Next step: "Open a fresh Claude.ai chat. Attach the zip. Paste the indexer trigger prompt."

Stop on any failure. Do not continue past a failed step.
```

---

## After Claude Code finishes

1. Download `skills_reference.zip` from the GitHub commit URL (or the local /tmp path if Claude Code surfaces it).
2. Open a fresh Claude.ai chat.
3. Attach the zip.
4. Paste this trigger prompt:

```
Run tgg-conversation-indexer. Scan conversations since last run, score significance, append to index, flag abandoned projects with upside, update todo, check if skills export is due. Use the attached skills_reference.zip to capture Claude Projects conversations.
```

The indexer will then process both main-chat conversations (via `recent_chats`) and Claude Projects conversations (via the zip's `example_conversations.md` files), update the master index, write abandoned projects to the todo file, and update the last-run timestamp.

---

## Why two steps

Claude Code can read `/mnt/skills/user/` (where your skills live locally) and commit to GitHub. Claude.ai cannot do either, but it can run the indexer's scoring and Drive write logic. Splitting the work keeps each tool on what it can actually do.
