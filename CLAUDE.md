# CLAUDE.md

This file provides guidance to AI assistants (Claude and others) working in this repository.

---

## Repository Overview

This repository is currently in its initialization phase. No source files, framework, or project structure have been committed yet. This CLAUDE.md serves as a foundational guide for AI-assisted development as the project grows.

---

## Git Workflow

### Branch Naming

- Feature branches for Claude sessions must follow the pattern:
  `claude/<feature-name>-<session-id>`
  Example: `claude/claude-md-mm42r61l51dt1g1s-EyZO6`
- Never push directly to `main` or `master` without explicit permission.

### Commits

- Write clear, descriptive commit messages in the imperative mood:
  - Good: `Add user authentication module`
  - Bad: `stuff` or `WIP`
- Sign commits using SSH (already configured via `.git/config`).
- Commit only related changes together — keep commits focused.

### Pushing

Always push with the upstream tracking flag:

```bash
git push -u origin <branch-name>
```

If push fails due to network errors, retry with exponential backoff:
- Wait 2s, retry
- Wait 4s, retry
- Wait 8s, retry
- Wait 16s, retry (final attempt)

### Fetching / Pulling

Prefer fetching specific branches:

```bash
git fetch origin <branch-name>
git pull origin <branch-name>
```

Apply the same exponential backoff retry strategy on network failures.

---

## AI Assistant Guidelines

### General Principles

1. **Read before modifying** — always read existing files before editing them to understand current state and conventions.
2. **Minimize scope** — only make changes directly requested or clearly necessary. Do not refactor surrounding code, add extra comments, or introduce new abstractions unless asked.
3. **No over-engineering** — avoid feature flags, backwards-compatibility shims, or premature abstractions. Write the minimum code needed for the current task.
4. **Avoid security vulnerabilities** — never introduce SQL injection, XSS, command injection, or other OWASP top-10 issues.
5. **Prefer editing over creating** — modify existing files rather than creating new ones when possible.

### What NOT to Do

- Do not add docstrings, type annotations, or comments to code you didn't change.
- Do not add error handling for scenarios that cannot happen.
- Do not create helper utilities for one-off operations.
- Do not design for hypothetical future requirements.
- Do not add backwards-compatibility code when you can just change the thing directly.

### Confirming Risky Actions

Always confirm with the user before:
- Deleting files or branches
- Force-pushing (`git push --force`)
- Running destructive resets (`git reset --hard`)
- Modifying CI/CD pipelines
- Pushing to branches other than the designated feature branch

---

## Project Setup (To Be Updated)

Once project files are added, this section should be updated with:

- **Language / Runtime**: e.g., Python 3.12, Node.js 20, Rust 1.x
- **Package manager**: e.g., pip/uv, npm/pnpm, cargo
- **Install dependencies**: e.g., `npm install` or `pip install -e .`
- **Run development server**: e.g., `npm run dev`
- **Run tests**: e.g., `pytest` or `npm test`
- **Lint / format**: e.g., `ruff check .` or `eslint .`
- **Build**: e.g., `npm run build`

---

## Testing (To Be Updated)

Once a testing framework is established, document:

- Test directory location
- How to run the full test suite
- How to run a single test
- Any required environment variables or test fixtures

---

## Code Conventions (To Be Updated)

Once source code exists, document observed conventions:

- Naming conventions (snake_case, camelCase, etc.)
- File/module organization patterns
- Error handling patterns
- Logging approach
- Environment configuration method (dotenv, config files, etc.)

---

## Remote

- **Origin**: `http://local_proxy@127.0.0.1:38487/git/simonmannheimer-tgg/Claude`
- **Proxy**: Local proxy server on `127.0.0.1:38487`

---

*This CLAUDE.md will be updated as the project structure and conventions evolve.*
