# Claude Code change summary — 2 May 2026

**Branch:** claude/audit-agent-workflows-SVd8h
**Commits:** 758cb2d, 64498bd

## What changed in Claude Code

The three deprecated SEO skills (tgg-content-strategist, tgg-copywriting, tgg-seo-specialist) were already merged into a single tgg-seo skill in Claude Code on 2026-05-01. However, the CE pipeline stage files still referenced the old names. That has now been fixed across 15 files.

tgg-ce-brief, tgg-ce-outline, tgg-ce-draft, tgg-ce-qa, tgg-ce-competitor-extract, tgg-ce-finalise, and tgg-ce-batch all had calls to the three deprecated skill names. These have been replaced with tgg-seo (strategy mode), tgg-seo (production mode), or tgg-seo (technical mode) as appropriate.

The tgg-content-pipeline orchestrator had the same stale references throughout and has been updated in the same way.

Five reference files were also updated: stage-contracts.md, delegation-map.md, voice-references.md, australian-retail-language.md, and examples.md.

docs/content-engineering-charter.md had the system map and delegation table updated to match.

The tgg-seo-specialist directory was deleted. It contained only a .last_sync file and no SKILL.md, so it was a stub left over from the merge.

No changes were made to tgg-seo itself or to any other skill.

## What you need to check in Claude.ai

The three deprecated skills (tgg-content-strategist, tgg-copywriting, tgg-seo-specialist) still exist in Claude.ai. They have not been deleted there. The Claude Code changes do not affect them.

The one skill to check is tgg-content-engineer, which is the Claude.ai equivalent of tgg-content-pipeline. If it delegates to the deprecated skill names, it will continue to work for now because those skills still exist in Claude.ai. But if the plan is to eventually remove them from Claude.ai too, tgg-content-engineer will need the same updates: replace tgg-content-strategist with tgg-seo (strategy mode), tgg-copywriting with tgg-seo (production mode), and tgg-seo-specialist with tgg-seo (technical mode).

No other Claude.ai skills are expected to be affected.
