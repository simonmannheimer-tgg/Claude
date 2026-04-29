# Logseq vault

This folder is the Logseq graph for Simon's PKM workflow.

## First-time setup

1. Open https://logseq.com/ in Chrome or Edge.
2. "Add new graph" → pick this `vault/` folder when prompted (File System Access API).
3. Logseq will create `journals/`, `pages/`, `assets/`, and `logseq/` subfolders.

## Sync

Plain git. Commit and push from here like any other folder. The `vault-autocommit.yml` workflow snapshots changes nightly so nothing is lost.

## Claude integration

The `vault` filesystem MCP is declared in `.claude/settings.json`, scoped to this folder. Claude can read/write daily notes, search backlinks, and run weekly reviews directly on the markdown files.

## Suggested prompts

- `Create today's daily note in vault/journals/ using the standard template`
- `Read my last 7 daily notes and write a weekly review under vault/pages/Weekly Reviews`
- `Read vault/pages/Goals.md and check this week's daily notes against it`
- `Scaffold a new project page in vault/pages/Projects/<name>.md`
