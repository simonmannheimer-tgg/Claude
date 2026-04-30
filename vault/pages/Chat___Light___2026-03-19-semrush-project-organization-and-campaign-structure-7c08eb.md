---
title: Semrush project organization and campaign structure
date: 2026-03-19
project: SEMRUSH MIGRATION
status: completed
score: 5/5
uuid: 7c08eb3d-3034-4232-b3d7-402acaa0a020
---

#chat/light #project/semrush-migration #status/completed #topic/bfcm #topic/blog #topic/keyword #topic/regex #topic/semrush #topic/sitemap

# Semrush project organization and campaign structure

- **Date:** [[2026-03-19]]
- **Project:** [[Projects/SEMRUSH MIGRATION]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 38
- **Chat URL:** https://claude.ai/chat/7c08eb3d-3034-4232-b3d7-402acaa0a020
- **Medium view:** [[Chat/Medium/2026-03-19-semrush-project-organization-and-campaign-structure-7c08eb]]
- **Full transcript:** [[Chat/Full/2026-03-19-semrush-project-organization-and-campaign-structure-7c08eb]]

## Summary

**Conversation Overview**

Simon Mannheimer (SEO Lead, The Good Guys / thegoodguys.com.au) is working on consolidating approximately 25 separate Semrush Position Tracking projects into a single unified project using tags. The conversation continued from a prior session where the core approach was established: export Extended CSV files from each campaign, merge them into Semrush's migration template format, and send to Semrush support (Jelena, jodi.kawi@semrush.com, cc: alisonchen@thegoodguys.com.au) for import.

The session focused on three deliverables. First, rebuilding the CSV merger script after discovering the actual Semrush Extended export format is far more complex than the migration template (6-line metadata headers, date triplets per domain, competitor columns to strip). The final merger script produces two separate files — `thegoodguys_migration_desktop.csv` and `thegoodguys_migration_mobile.csv` — matching the Semrush migration template format exactly: `Keyword, Location, Device, Labels, URL, dd/mm/yyyy...`. Key decisions: tags combine the existing pipe-separated Semrush tags plus the project name as an additional tag on every keyword; device mapping was verified against MHTML source rather than inferred from campaign IDs; the Black Friday campaign (`6675175_3716727`) is excluded as it tracks JB Hi-Fi as the primary domain with no TGG position data; date range spans the full history with no artificial cap. Simon corrected Claude's initial output when tags were missing or incorrect, and specified that mobile and desktop must be split into separate files.

Second, a detailed automation brief was written for a Claude Chrome Extension browser agent, covering the complete 41-campaign inventory with campaign IDs, folder IDs, device mappings, project names, step-by-step Semrush UI navigation (date picker → All time → Apply → Export → Extended → CSV), source and target CSV format specifications, deduplication rules, and a validation checklist. Third, a Chrome Extension (v4) was built and packaged. Key changes from the prior v3: date range is set via UI interaction (clicking "All time" in the date picker) rather than hardcoded URL parameters; tabs are never closed after export; the campaign list was corrected to 41 campaigns (19 Desktop, 22 Mobile) after Simon flagged the count was wrong — Godfreys and Site Audit campaigns are excluded. The popup pulls the total dynamically from `CAMPAIGNS.length` in the background script rather than hardcoding it, which was the root cause of the "38 campaigns queued" discrepancy Simon flagged.

**Tool Knowledge**

Claude used bash and Python tools extensively to parse MHTML files from Semrush. The MHTML files required quoted-printable decoding before parsing: `content = re.sub(r'=\n', '', content)` followed by `re.sub(r'=3D', '=', content)`. Campaign IDs and folder IDs were extracted from `tracking/landscape/{projectId}_{campaignId}.html` URL patterns within the MHTML. Device type (Desktop/Mobile) was determined by finding the nearest preceding `aria-label="Desktop"` or `aria-label="Mobile"` element before each campaign link — proximity-based detection worked reliably when searching backwards from each campaign's first occurrence. Folder IDs (`fid=XXXXXX`) were extracted from nearby URL context within 500 characters of each campaign ID occurrence. Single-ID campaign files (no underscore, e.g. `6187781`) are always Desktop — they are original campaigns predating the November 2025 mobile additions. Mobile campaign IDs follow the pattern `_37XXXXX`, `_36XXXXX`, `_39XXXXX`, or `_40XXXXX` as the second segment. The actual Semrush Extended CSV export has 6 metadata lines before the data header; the header line starts with `Keyword,` and TGG position columns match the regex `.*thegoodguys\.com\.au.*?_(\d{8})$` excluding `_type`, `_landing`, and `_difference` suffixes.

## First user message

> _(no user message)_

## Topics

[[topic/bfcm]], [[topic/blog]], [[topic/keyword]], [[topic/regex]], [[topic/semrush]], [[topic/sitemap]]

## Skills referenced

none detected
