---
title: Editing tgg-copywriting skill with skill-creator
date: 2026-03-19
project: main
status: completed
score: 4/5
uuid: 99986fbb-2079-49c5-ae7b-17847d965610
---

#chat/light #project/main #status/completed #topic/copy #topic/plp #skill/tgg-copywriting

# Editing tgg-copywriting skill with skill-creator

- **Date:** [[2026-03-19]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, project-keyword, lasting-effect)
- **Messages:** 2
- **Chat URL:** https://claude.ai/chat/99986fbb-2079-49c5-ae7b-17847d965610
- **Medium view:** [[Chat/Medium/2026-03-19-editing-tgg-copywriting-skill-with-skill-creator-99986f]]
- **Full transcript:** [[Chat/Full/2026-03-19-editing-tgg-copywriting-skill-with-skill-creator-99986f]]

## Summary

**Conversation Overview**

The person asked Claude to edit the "tgg-copywriting" skill using the skill-creator tool. This is a professional copywriting skill for The Good Guys (thegoodguys.com.au), an Australian electronics and appliances retailer. The task involved replacing two reference files within the skill package with updated content, then repackaging the skill as a `.skill` file for download.

The two files updated were `references/00-tov.md` (Tone of Voice and Language Reference) and `references/01-plp-intros.md` (PLP Intro Copy process guide). Key changes included: adding an explicit two-category framework distinguishing hard bans from overuse warnings in the TOV file; refining the "save/saving" rule with a critical distinction around price-framing context; adding energy claims, Price Beat, and Click & Collect guidance; updating the PLP intro character count range from 230–260 to 220–250 characters (with 225–235 as the preferred lower-end target); and adding a new section explaining the SEO and AI citability rationale for the two-sentence copy format. The SKILL.md description was also updated to reflect the new character range.

**Tool Knowledge**

The skill-creator packaging workflow requires reading source files from `/mnt/skills/user/` (read-only), copying to `/tmp/` for editing, then running the packager. The correct invocation pattern for `package_skill.py` is `cd /mnt/skills/examples/skill-creator && python -m scripts.package_skill /tmp/[skill-folder] /tmp`, which outputs a `.skill` file to `/tmp/`. The final step is copying the output to `/mnt/user-data/outputs/` for delivery via `present_files`. Running the script from a different working directory or passing `--output` as a flag did not work; the second positional argument as the output directory is the correct syntax.

## First user message

> Help me edit the "tgg-copywriting" skill using skill-creator: Help me edit the "tgg-copywriting" skill using skill-creator:

## Topics

[[topic/copy]], [[topic/plp]]

## Skills referenced

[[skill/tgg-copywriting]]
