# Vault & Sync Reference

---

## Conversation & Session Indexing

The Logseq vault under `vault/` is the long-memory layer. Every Claude conversation (web/desktop) and every Claude Code session that touches this repo is indexed as a tagged page, with a per-project MOC.

### Build script

```
python3 scripts/build_logseq_chat_index.py [export_dir] [vault_dir]
```

- `export_dir` — unzipped Anthropic conversation export (default `/tmp/chat-export`); contains `conversations.json` + `projects.json`
- `vault_dir` — Logseq vault root (default `vault/`)

### Outputs (written to `vault/pages/`)

| File pattern | Contents |
|---|---|
| `Chat___Light___<slug>.md` | Short summary, 1–2 paragraphs, 240-char excerpt |
| `Chat___Medium___<slug>.md` | User messages only, full text |
| `Chat___Full___<slug>.md` | Full transcript (human + assistant) |
| `Chat___Code___<slug>.md` | Claude Code session — commits + files touched |
| `Projects___<project>.md` | Per-project MOC listing every chat/session |
| `Projects___Claude-Code.md` | Master MOC of all Claude Code branches |
| `Conversations Master Index.md` | By-status / by-project / by-topic index |

### Tag taxonomy

Every page is tagged with: `#project/<slug>`, `#status/<active|completed|abandoned|tactical>`, `#topic/<keyword>`, `#skill/<seo|development|reporting|...>`. Project tags use a 40-char slug; MOC pages use the human-readable name as title.

### Every Claude Code branch is a project

Each `claude/<feature>-<id>` branch is treated as its own project in the vault. The indexer extracts `claude.ai/code/session_<id>` URLs from commit messages, groups commits by session, infers the owning branch, and writes one `Chat___Code___<slug>.md` per session and one `Projects___<branch>.md` MOC per branch.

### When to re-run

- When a fresh Anthropic conversation export is available
- After landing significant work on a Claude Code branch (before PR/merge)
- As part of the weekly `tgg-conversation-indexer` skill run

The script is idempotent — deletes all `Chat___*.md` and `Projects___*.md` before regenerating. Hand-written notes belong in `vault/journals/` or non-`Chat`/`Projects` pages.

---

## Chat ↔ Code Sync Pipeline

### Skills: Chat → Code

When a chat session creates or updates a skill, package it as a ZIP and upload to Google Drive root:

```
skill-name_YYYYMMDD-HHMM.zip
```

The ZIP must contain a `SKILL.md` at the root and a `metadata.json`:
```json
{
  "change": "Short description of what changed",
  "timestamp": "2026-05-01T14:30:00+00:00"
}
```

To pull pending skill ZIPs into the repo: run `skill-zip-sync` in a Claude Code session, or trigger `drive-skill-sync.yml` from GitHub Actions.

Processed ZIPs are logged to `.claude/skill-sync-cleanup.log` for manual Drive deletion (Drive delete not yet automated — activate Google Workspace MCP to enable).

### Conversations: Chat → Vault

1. Upload the export ZIP to Google Drive as `claude-export_YYYYMMDD.zip`
2. Run: `python3 scripts/drive_conversation_sync.py --from-file /path/to/export.zip`
3. Vault pages regenerate automatically; `vault-autocommit.yml` commits them nightly

Run the script without arguments for full usage instructions.
