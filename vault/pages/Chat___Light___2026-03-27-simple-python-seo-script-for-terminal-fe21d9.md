---
title: Simple Python SEO script for terminal
date: 2026-03-27
project: PLP Copy Auditor Script
status: completed
score: 4/5
uuid: fe21d9bb-451e-438e-a2ff-ef8d48139457
---

#chat/light #project/plp-copy-auditor-script #status/completed #topic/contentful #topic/crawl #topic/keyword #topic/plp

# Simple Python SEO script for terminal

- **Date:** [[2026-03-27]]
- **Project:** [[Projects/PLP Copy Auditor Script]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, 5+turns, project-keyword)
- **Messages:** 20
- **Chat URL:** https://claude.ai/chat/fe21d9bb-451e-438e-a2ff-ef8d48139457
- **Medium view:** [[Chat/Medium/2026-03-27-simple-python-seo-script-for-terminal-fe21d9]]
- **Full transcript:** [[Chat/Full/2026-03-27-simple-python-seo-script-for-terminal-fe21d9]]

## Summary

**Conversation overview**

The person works at The Good Guys (thegoodguys.com.au), which operates under JB HI-FI Group Pty Ltd, and is involved in SEO and copywriting quality assurance work. The conversation centred on building a Python script to audit PLP (Product Listing Page) intro copy against The Good Guys' copywriting rules. The rules enforced by the script include: character count of 220–250 (ideal 225–235), exactly two sentences, one mention of "The Good Guys," no banned S1 openers (Discover, Explore, Shop), banned words on brand pages (trusted, reliable, enjoy, features), hard-banned words site-wide (sale, discount), and S2 must be shorter than S1.

The person provided the actual HTML markup from a live TGG PLP page, identifying that CSS class names use hashed suffixes (e.g. `_richText_1j2n6_11`) that change per page, and confirmed that using `data-testid` attributes (`contentful-richtext`, `readmore-content`) is the reliable selector approach. The script was iteratively refined: first built with a file-based URL input, then simplified to a hardcoded `URLS` list inside the `.py` file at the person's request. The person then provided 20 specific TGG category URLs to populate that list. A PowerShell parse error occurred when the person attempted to run the `.py` file directly in the terminal rather than passing it to Python — this was resolved by clarifying the correct `python tgg_plp_auditor.py` syntax. The person confirmed they are on Windows using PowerShell. They do not need Git; they want the script saved locally at `C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\Other\Python and VSCode`, and the correct `cd` command with quoted path was provided.

The person prefers simplicity — they explicitly asked to move away from file-based input toward editing URLs directly in the script. The final script requires `requests` and `beautifulsoup4`, runs with `python tgg_plp_auditor.py` or `python tgg_plp_auditor.py --output report.csv`, and classifies pages as Type A/B/C/D based on URL structure to apply the correct rule set.

## First user message

> write me a simple python script for SEO i can run in terminal write me a simple python script for SEO i can run in terminal

## Topics

[[topic/contentful]], [[topic/crawl]], [[topic/keyword]], [[topic/plp]]

## Skills referenced

none detected
