---
title: 2026 TV pages H1 naming strategy
date: 2026-03-18
project: main
status: completed
score: 5/5
uuid: f929c4cf-849a-4e00-b266-7e243f4999a2
---

#chat/light #project/main #status/completed #topic/404 #topic/bfcm #topic/blog #topic/copy #topic/inlink #topic/keyword #topic/meta #topic/plp #topic/redirect #topic/shopify

# 2026 TV pages H1 naming strategy

- **Date:** [[2026-03-18]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 46
- **Chat URL:** https://claude.ai/chat/f929c4cf-849a-4e00-b266-7e243f4999a2
- **Medium view:** [[Chat/Medium/2026-03-18-2026-tv-pages-h1-naming-strategy-f929c4]]
- **Full transcript:** [[Chat/Full/2026-03-18-2026-tv-pages-h1-naming-strategy-f929c4]]

## Summary

**Conversation Overview**

The person works in SEO/content for The Good Guys (thegoodguys.com.au), an Australian retail chain. The conversation centred on producing a full copy package for the 2026 LG TVs brand category page at `/lg/televisions/all-tvs/latest-tvs`, which was launching that day as part of a broader strategy to transition "Latest TVs" pages from 2025 to 2026 model year framing across multiple brand pages (LG, Samsung, TCL, Hisense, and possibly Sony). Simon Mannheimer and a team member referred to as OD were mentioned as stakeholders involved in the broader 2026 TV strategy.

Tasks completed included: H1 recommendation (settled on "2026 LG TVs"), title tag (finalised as "2026 LG TVs - New OLED, QNED & Mini LED TVs from LG"), meta description, PLP intro copy, top copy, five FAQs with internal links, and an AI-citable intro/considerations section linking to buying guides. Throughout the session the person corrected several rules: brand name ("The Good Guys") must never appear in title tags as the site appends it automatically; title tags must never exceed 60 characters; explicit prices must never be mentioned for legal reasons; "Explore/Discover/Shop" are not banned outright but should not be overused; and all URLs in copy must be hardcoded as absolute URLs (https://www.thegoodguys.com.au/...) rather than relative paths, as relative paths resolve incorrectly when copied from Claude. The person also flagged that Claude's URL status checker was using `-L` to follow redirects, masking 301s as 200s, which caused a bad link (`/lg/televisions/all-tvs/led-lcd-tvs`) to be included in copy before being caught and corrected.

The person's working style is direct and output-focused, preferring Claude to produce ready-to-use copy rather than explain reasoning at length. They pushed back on filler language in metadata, wanted more entities packed into titles, and required FAQ answers to be formatted as separate header-and-paragraph pairs. The final considerations section needed to match an AI-citable format with short declarative factual statements rather than advisory prose paragraphs, referencing existing TGG buying guide pages as the benchmark.

**Tool Knowledge**

URL status checks must be run without the `-L` flag to catch 301 redirects accurately; using `-L` follows the redirect chain and reports the final destination's 200 status, hiding the fact that the original URL is a redirect. The correct curl pattern is `curl -s -o /dev/null -w "%{http_code}" --max-time 10 "[url]"` without `-L`. To identify redirect destinations, use `curl -s -I --max-time 10 "[url]" | grep -i location`. Verified 200 LG TV URLs for this page include: `https://www.thegoodguys.com.au/lg/televisions/oled-tvs`, `/lg/televisions/all-tvs/4k-tvs`, `/lg/televisions/all-tvs/tvs-43-inch-and-below`, `/lg/televisions/all-tvs/tvs-45-inch-to-54-inch`, `/lg/televisions/all-tvs/tvs-55-inch-to-64-inch`, `/lg/televisions/all-tvs/tvs-65-inch-to-74-inch`, `/lg/televisions/all-tvs/tvs-75-inch-to-84-inch`, `/lg/televisions/all-tvs/tvs-85-inch-and-above`, `/lg/televisions/all-tvs/latest-tvs`, `/lg/televisions`, `/lg/audio/home-audio/sound-bars`, `/lg/computers-tablets-and-gaming/monitors/computer-monitors`, `/lg/audio`, and buying guides at `/buying-guide/what-is-oled` and `/buying-guide/television-buying-guide`. The URL `/lg/televisions/all-tvs/led-lcd-tvs` is a 301 and must not be used.

## First user message

> Pages: * Latest TVs - /televisions/all-tvs/latest-tvs (base page) * LG Latest TVs - /lg/televisions/all-tvs/latest-tvs (launching today) * TCL Latest TVs - /tcl/televisions/all-tvs/latest-tvs (coming TBA) * Hisense Latest TVs - /hisense/televisions/all-tvs/latest-tvs (coming TBA) * Sony Latest TVs - /sony/televisions/all-tvs/latest-tvs (50/50 we get these, TBA) * Samsung Latest TVs - /samsung/tele

## Topics

[[topic/404]], [[topic/bfcm]], [[topic/blog]], [[topic/copy]], [[topic/inlink]], [[topic/keyword]], [[topic/meta]], [[topic/plp]], [[topic/redirect]], [[topic/shopify]]

## Skills referenced

none detected
