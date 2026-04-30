# Superpowers — Setup

**What it does:** Forces plan-before-execute on every complex task. Claude brainstorms, writes a checklist plan, executes step by step, reviews before finishing. Stops runaway iteration and scope creep.

**Best for:** Monthly report builds, batch copy jobs, audit pipelines, deck construction, anything where Claude currently goes off and does things you didn't ask for.

**Status:** Not installed.

## Activate

Run in your terminal (requires Claude Code installed):
```bash
claude plugin install superpowers
```

That's it. No config, no API key, no repo changes needed. It's an Anthropic marketplace plugin.

## After activation

Works silently. When you give Claude a complex task it will:
1. Brainstorm approaches first
2. Write a plan file with checkboxes
3. Execute step by step against the plan
4. Review completeness before stopping

You can override it mid-task with "skip the plan, just do it" and it will comply.

## Uninstall

```bash
claude plugin uninstall superpowers
```

## Security: CLEAN
- MIT licence
- Anthropic official marketplace
- No network calls, no telemetry, no external APIs
- Reviewed April 2026
