---
title: Content planner alignment with overdose TGG
date: 2026-04-27
project: main
status: active
score: 5/5
uuid: 6a535d2a-4877-4fa5-9b4e-94c94d118268
---

#chat/light #project/main #status/active #topic/blog #topic/eofy #topic/mcp #topic/plp

# Content planner alignment with overdose TGG

- **Date:** [[2026-04-27]]
- **Project:** [[Projects/main]]
- **Status:** #status/active (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 22
- **Chat URL:** https://claude.ai/chat/6a535d2a-4877-4fa5-9b4e-94c94d118268
- **Medium view:** [[Chat/Medium/2026-04-27-content-planner-alignment-with-overdose-tgg-6a535d]]
- **Full transcript:** [[Chat/Full/2026-04-27-content-planner-alignment-with-overdose-tgg-6a535d]]

## Summary

**Conversation overview**

The person works in an SEO or digital content role and was managing two Google Sheets: an official SEO roadmap/tracker for The Good Guys (with a "Content Planner" tab) and a separate Overdose x TGG completed content briefs tracker ("Sheet1"). The core task was twofold: first, align the Content Planner tab with the OD completed briefs to date; second, build a mechanism to pull new blog entries added to the Content Planner into the OD sheet while keeping the OD sheet fully editable.

Claude analysed both sheets by reading uploaded Excel exports and identified specific mismatches: ten blog rows (#118–127) had "TBD" in the Content Planner but "November" in the OD file; the Dishwasher Buying Guide 2026 had conflicting months (January in CP vs November in OD); and the TV Buying Guide had a Content Type discrepancy (New in CP vs Optimisation in OD). The person confirmed January and Optimisation were correct, and Claude documented the three manual fixes needed across both sheets. For the sync mechanism, Claude recommended and built a Google Apps Script solution over IMPORTRANGE (read-only) or Power Query, as Apps Script allows the OD sheet to remain editable after import.

Several iterations of the Apps Script were required. Issues encountered and resolved included: hyperlinks in the "Content / Brief" column being dropped (fixed by using `getRichTextValues()` and `getRichTextValue()`), links rendering as Google Sheets smart chips rather than hyperlinks (fixed by writing `=HYPERLINK("url","text")` formulas instead of rich text), an off-by-one error in row index calculation causing hyperlink formulas to land in wrong cells (fixed by using `startRow + item.index`), formatting not copying from existing rows (fixed by using `copyTo` with `PASTE_FORMAT` before writing values), and a `SyntaxError: Identifier 'CP_ID' has already been declared` error caused by duplicate script content in the Apps Script editor (fixed by moving all constants inside the function and advising the person to clear the editor before repasting). The final script adds a blue separator row (`#1155CC`) before each sync batch, copies row formatting from the last existing data row, appends new Blog and Buyers Guide entries not already present in OD, and adds a "Sync Blogs" custom menu. Sheet IDs used: Content Planner `1NFReMzmaUNciQPyOAvsmtFxTGdIlDIsnHV71uA5JiSA` (tab: `Content Planner`), OD sheet `1cTQr-L4wnjC4ijDU0rjAdd_G9ONqui6Q6BL28PGs_4E` (tab: `Sheet1`).

## First user message

> i need you to take this content planner tab (on official) and ensure its aligned with the overdose tgg completed to date?  I then need ideas on how to pull in new blogs if added to the content planner one into the tgg x od one? but need to be able to allow the latter to be changed (so cant be just a streamed output) i need you to take this content planner tab (on official) and ensure its aligned w

## Topics

[[topic/blog]], [[topic/eofy]], [[topic/mcp]], [[topic/plp]]

## Skills referenced

none detected
