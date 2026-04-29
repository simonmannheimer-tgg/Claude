---
title: EOFY blog content table for monday.com
date: 2026-04-27
project: EOFY
status: active
score: 3/5
uuid: ad41ad1f-a193-48a8-813f-47ae2c54829f
---

#chat/light #project/eofy #status/active #topic/blog #topic/eofy #topic/monday

# EOFY blog content table for monday.com

- **Date:** [[2026-04-27]]
- **Project:** [[Projects/EOFY]]
- **Status:** #status/active (score 3/5: named-tgg, 5+turns, project-keyword)
- **Messages:** 12
- **Chat URL:** https://claude.ai/chat/ad41ad1f-a193-48a8-813f-47ae2c54829f
- **Medium view:** [[Chat/Medium/2026-04-27-eofy-blog-content-table-for-mondaycom-ad41ad]]
- **Full transcript:** [[Chat/Full/2026-04-27-eofy-blog-content-table-for-mondaycom-ad41ad]]

## Summary

**Conversation Overview**

The person works with The Good Guys (TGG) and needed help formatting a reference table of existing EOFY blog content for pasting into a Monday.com update. The task involved organizing six blog posts, each with a live URL and a corresponding Google Doc link, into a clean table format.

The conversation involved several iterations to resolve formatting issues. The initial table used "Open Doc" as anchor text for Google Doc links, which the person rejected — they wanted the full document titles (e.g., "TGG | Existing EOFY Blogs | EOFY Deals") used as anchor text. This caused the markdown table to break because pipe characters in the anchor text conflicted with markdown table syntax. After the person flagged the table as broken and shared a screenshot, Claude identified the pipe character conflict and resolved it by escaping pipes with backslashes (`\|`) within the link text, producing a functional markdown table with full-title anchor text preserved.

The person communicates tersely and expects Claude to diagnose and fix problems with minimal back-and-forth. When something breaks, they expect a solution rather than multiple options where avoidable. The correction to note for future similar tasks: markdown tables in Monday.com updates break when link anchor text contains pipe characters — these must be escaped with `\|`.

## First user message

> can i get this as a nice table to paste into [monday.com](http://monday.com) update?  https://www.thegoodguys.com.au/whats-new/eofy-dealsTGG[ | Existing EOFY Blogs | EOFY Deals](https://docs.google.com/document/d/1O0gvGcZyFXwNXRs8srfLbJGEzu0qXXop7Kz26flspto/edit?tab=t.0)https://www.thegoodguys.com.au/whats-new/best-tech-buys-for-eofy[TGG | Existing EOFY Blogs | Best Tech Buys for EOFY](https://doc

## Topics

[[topic/blog]], [[topic/eofy]], [[topic/monday]]

## Skills referenced

none detected
