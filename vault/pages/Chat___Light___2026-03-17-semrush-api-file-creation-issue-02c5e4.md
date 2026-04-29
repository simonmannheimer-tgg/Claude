---
title: Semrush API file creation issue
date: 2026-03-17
project: SEMRUSH MIGRATION
status: completed
score: 4/5
uuid: 02c5e45b-4b39-4182-b940-0d890957a889
---

#chat/light #project/semrush-migration #status/completed #topic/keyword #topic/mcp #topic/schema #topic/semrush

# Semrush API file creation issue

- **Date:** [[2026-03-17]]
- **Project:** [[Projects/SEMRUSH MIGRATION]]
- **Status:** #status/completed (score 4/5: deliverable, 5+turns, project-keyword, lasting-effect)
- **Messages:** 46
- **Chat URL:** https://claude.ai/chat/02c5e45b-4b39-4182-b940-0d890957a889
- **Medium view:** [[Chat/Medium/2026-03-17-semrush-api-file-creation-issue-02c5e4]]
- **Full transcript:** [[Chat/Full/2026-03-17-semrush-api-file-creation-issue-02c5e4]]

## Summary

**Conversation overview**

Simon Mannheimer (SEO Lead, The Good Guys / thegoodguys.com.au) is working on consolidating approximately 20 separate Semrush Position Tracking projects (organised by product category) into a single project using Tags. The core task is producing a combined CSV with full historical position data across all 41 campaigns (42 minus Godfreys, which was explicitly skipped) to send to Semrush's migration team (contact: jodi.kawi@semrush.com) so they can recreate the campaigns with history intact. The Semrush migration template requires columns for Keyword, Location, Device, Labels, URL, and date columns for every tracked week going back to campaign creation.

The conversation involved significant iteration. Claude initially built a keyword-only merged CSV without date columns, which Simon correctly identified as missing the entire point — Semrush needs full historical position data, not just current keywords. Claude also incorrectly used the Semrush MCP API when Simon had not asked for it, which Simon called out directly. The correct source files are the "Overview → All time → Extended" CSV exports from each campaign, which produce wide-format files with a position column per tracked date. Simon had already manually exported 41 of the 42 campaigns and uploaded them; these are confirmed to be the correct Extended format with date columns going back to March 2023 for desktop campaigns.

To automate the remaining exports and handle future re-runs, Claude built a Chrome Extension (v3) that opens each campaign overview page in a new tab with date range baked into the URL parameters (`date_begin=20230308&date_end=20260317`), waits for the page to settle, opens the export dropdown, selects the Extended radio button (`input[type="radio"][value="extended"]`), clicks the CSV menuitem (`[role="menuitem"]` with exact text "CSV"), then detects the download starting by intercepting `URL.createObjectURL` before signalling the background script to open the next campaign in a fresh tab and close the previous one. Simon flagged that an earlier version moved to the next campaign before the export completed, which drove the new-tab-per-campaign approach. The extension is delivered as a flat zip for loading unpacked via `chrome://extensions` in Developer mode.

**Tool knowledge**

The Semrush MCP server was used early in the conversation via `execute_report` with `report: "tracking_position_organic"` and parameters `campaign_id` and `url: "*.thegoodguys.com.au/*"` with `display_limit: 500`. Results were too large to hold in context and were written to `/mnt/user-data/tool_results/`. The MCP should not be used for this task — Simon's uploaded CSV exports are the authoritative source. When parsing Semrush's own overview export format, the header block contains metadata rows before the actual `Keyword,` header row; the data header must be detected by checking `row[0] == 'Keyword'` rather than assuming a fixed row number. Campaign IDs with a `_3XXXXXX` suffix pattern are mobile campaigns; those without (or with `_1XXXXXX`) are desktop. The full campaign map with all 42 IDs and their corresponding `fid` values is documented in the transcript at `/mnt/transcripts/2026-03-17-03-09-27-semrush-position-tracking-merge.txt`.

## First user message

> using semrush api - help me solve this issue and create the file. using semrush api - help me solve this issue and create the file.

## Topics

[[topic/keyword]], [[topic/mcp]], [[topic/schema]], [[topic/semrush]]

## Skills referenced

none detected
