---
title: Airtable capabilities and uses
date: 2026-03-19
project: main
status: completed
score: 4/5
uuid: aa2d1486-f300-46c8-93e1-708adc5a4fec
---

#chat/light #project/main #status/completed #topic/airtable #topic/copy #topic/keyword #topic/mcp #topic/meta #topic/plp #topic/redirect #topic/semrush

# Airtable capabilities and uses

- **Date:** [[2026-03-19]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, 5+turns, project-keyword)
- **Messages:** 10
- **Chat URL:** https://claude.ai/chat/aa2d1486-f300-46c8-93e1-708adc5a4fec
- **Medium view:** [[Chat/Medium/2026-03-19-airtable-capabilities-and-uses-aa2d14]]
- **Full transcript:** [[Chat/Full/2026-03-19-airtable-capabilities-and-uses-aa2d14]]

## Summary

**Conversation Overview**

The person explored Claude's Airtable integration capabilities, starting with a general question about what actions are possible. Claude outlined available operations including reading bases, tables, and records, as well as writing data such as creating records, tables, and fields. The person works in an SEO context at The Good Guys (TGG), an Australian retailer, and the conversation referenced domain-specific work including PLP (product listing page) copy production, metadata, and category page management.

The person shared their Airtable base URL (https://airtable.com/appS4NfrOth5cVo7P), which revealed base ID `appS4NfrOth5cVo7P`. The existing base already contained three linked tables: Campaigns, Keywords, and Rankings. When asked what example table to create, the person selected a PLP Copy Tracker. Claude created the table with fields for Page URL, Category, Copy Status (colour-coded single select with five stages: Not Started, In Progress, Written, QA, Live), PLP Intro Copy, Intro Char Count, Meta Title, Meta Description, Meta Title Chars, Meta Desc Chars, and Notes. Five example records were populated using realistic TGG category pages (Televisions, Washing Machines, Robot Vacuums, Laptops, Air Conditioners) with copy, character counts, and production notes reflecting real SEO workflow considerations. The person also inadvertently shared what appeared to be an API key, and Claude flagged this and advised rotating it immediately.

**Tool Knowledge**

For Airtable operations, the base ID `appS4NfrOth5cVo7P` is the person's active SEO workspace. The existing table IDs encountered were `tblaIo1av7sgtwlzR` (from the URL) and the newly created PLP Copy Tracker landed at `tbl4E40UpT2J9inMY`. When creating records, field IDs rather than field names must be used in the records payload — the field IDs for the PLP Copy Tracker table were resolved from the `create_table` response and used directly in `create_records_for_table`. The `create_base` tool is not available in this MCP connection, so new bases must be created manually in Airtable before Claude can scaffold tables inside them.

## First user message

> what can you do with airtable what can you do with airtable

## Topics

[[topic/airtable]], [[topic/copy]], [[topic/keyword]], [[topic/mcp]], [[topic/meta]], [[topic/plp]], [[topic/redirect]], [[topic/semrush]]

## Skills referenced

none detected
