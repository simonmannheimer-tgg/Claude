# Agentic SEO (AEO Auditor) — Setup

**What it does:** Audits any website or local build directory for AI agent discoverability — checks `robots.txt`, `llms.txt`, `AGENTS.md/CLAUDE.md`, heading hierarchy, token budgets per page, capability signalling files (`skill.md`), and copy-to-clipboard/raw-view UX. Scores 0–100 and outputs a grade (A–F).

**Best for:** Auditing TGG category pages or buying guides for AEO readiness; scoring a site before publishing an `llms.txt`; CI gating a documentation build; checking competitors' agent-readiness.

**Status:** Active. Repo cloned and deps installed. Node 22 confirmed.

**Binary:** `node /home/user/Claude/.claude/optional/agentic-seo/repo/bin/aeo.js` (the CLI entry is `aeo.js`, not `agentic-seo.js`).

---

## What it audits (100-point scale)

| Category | Points | Checks |
|----------|--------|--------|
| Discovery | 25 | `robots.txt` agent rules, `llms.txt`, `AGENTS.md` / `CLAUDE.md` |
| Content Structure | 25 | Heading hierarchy, semantic HTML, Markdown availability |
| Token Economics | 25 | Per-page token counts, AI-friendly metadata |
| Capability Signalling | 15 | `skill.md`, agent permission declarations |
| UX Bridge | 10 | Copy-to-clipboard, raw view links |

---

## Repo

Source: `https://github.com/addyosmani/agentic-seo`
Cloned to: `.claude/optional/agentic-seo/repo/`
Language: JavaScript (MIT licence, no API keys needed)

---

## Activate

### Already done — active as of 2026-05-01

Node 22 confirmed, repo cloned to `repo/`, `npm install` complete.

### Run an audit

```bash
# alias for convenience (add to shell profile if desired)
alias aeo="node /home/user/Claude/.claude/optional/agentic-seo/repo/bin/aeo.js"

# Audit a live URL
node /home/user/Claude/.claude/optional/agentic-seo/repo/bin/aeo.js --url https://www.thegoodguys.com.au

# Verbose
node /home/user/Claude/.claude/optional/agentic-seo/repo/bin/aeo.js --verbose --url https://www.thegoodguys.com.au

# JSON output
node /home/user/Claude/.claude/optional/agentic-seo/repo/bin/aeo.js --json --url https://www.thegoodguys.com.au > aeo-report.json

# CI mode with score threshold
node /home/user/Claude/.claude/optional/agentic-seo/repo/bin/aeo.js --json --threshold 60 ./build

# Specific checks only
node /home/user/Claude/.claude/optional/agentic-seo/repo/bin/aeo.js --checks robots-txt,llms-txt,token-budget --url https://www.thegoodguys.com.au
```

---

## Configuration (.aeorc.json)

Place at project root or add an `"aeo"` key in `package.json`:

```json
{
  "outputDir": "_site",
  "checks": {
    "token-budget": { "maxTokensPerPage": 25000 },
    "robots-txt": { "requiredAgents": ["ClaudeBot", "GPTBot"] }
  },
  "ignore": ["**/node_modules/**", "**/vendor/**"],
  "threshold": 60
}
```

---

## Programmatic API

```javascript
import { audit, auditWithServer } from 'agentic-seo';

const report = await audit('./my-site');
console.log(report.grade);          // 'B'
console.log(report.percentage);     // 78
console.log(report.findings.errors);

// With local server (enables HTTP-based checks)
const serverReport = await auditWithServer('./build');
```

---

## CLI flags reference

| Flag | Description |
|------|-------------|
| `--url, -u` | Audit a live URL |
| `--serve, -s` | Launch local server; run HTTP-based checks |
| `--json` | Output JSON |
| `--verbose, -v` | Show all findings including informational |
| `--threshold, -t` | Minimum score; exit 1 if below |
| `--checks` | Comma-separated list of specific checkers |
| `--output-dir` | Manually specify build directory |

---

## What you can ask once activated

- "Run an AEO audit on thegoodguys.com.au and score it"
- "Check if our buying guides have llms.txt and token-budget issues"
- "Audit the local build of the TVs category page for agent discoverability"
- "Run agentic-seo in CI mode with a threshold of 70 on this build"
- "Compare TGG's AEO score against jbhifi.com.au"

---

## Security: CLEAN
- MIT licence
- No API keys, no credentials, no network write access
- Reads local files and makes outbound GET requests to target URLs only
- Reviewed April 2026
