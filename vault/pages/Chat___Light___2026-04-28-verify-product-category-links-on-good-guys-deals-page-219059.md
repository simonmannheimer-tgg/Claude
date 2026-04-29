---
title: Verify product category links on Good Guys deals page
date: 2026-04-28
project: EOFY
status: completed
score: 4/5
uuid: 219059f1-601c-416c-9e7f-e976b5c07198
---

#chat/light #project/eofy #status/completed #topic/bfcm #topic/deals #topic/eofy #topic/inlink #topic/plp

# Verify product category links on Good Guys deals page

- **Date:** [[2026-04-28]]
- **Project:** [[Projects/EOFY]]
- **Status:** #status/completed (score 4/5: deliverable, named-tgg, 5+turns, project-keyword)
- **Messages:** 6
- **Chat URL:** https://claude.ai/chat/219059f1-601c-416c-9e7f-e976b5c07198
- **Medium view:** [[Chat/Medium/2026-04-28-verify-product-category-links-on-good-guys-deals-page-219059]]
- **Full transcript:** [[Chat/Full/2026-04-28-verify-product-category-links-on-good-guys-deals-page-219059]]

## Summary

**Conversation Overview**

The person is working on quality assurance for The Good Guys Australia website (thegoodguys.com.au), specifically checking a deals category slider module across multiple pages. The work involved two related tasks: first verifying that a specific internal navigation slider module on the TVs deals page contained links to 12 category pages (BBQs, coffee machines, dishwashers, dryers, fridges, headphones and soundbars, laptops, microwaves, phones and smart watches, TVs, vacuums and cleaning, and washing machines), and second checking whether that same slider module was live across all relevant deals pages.

Claude initially checked all links across the full page, which prompted the person to clarify scope — they wanted only the specific slider module checked, not the entire page. Claude identified that a `black-friday-tvs` link found earlier was located in the FAQ/body copy section (`_collectionPageFaq`), not in the slider module (`_sliderContainer`), resolving that discrepancy. For the second task, Claude fetched 14 deals pages programmatically (the 12 category pages plus `/deals` and `/deals/kitchen-appliances`, explicitly excluding Black Friday and Boxing Day pages) and confirmed all returned HTTP 200 and contained the `_sliderContainer` class, meaning the slider is live across all relevant pages.

The person demonstrated a precise, scope-conscious approach — correcting Claude when checks were too broad and clearly specifying exclusions (Black Friday, Boxing Day). The key technical marker used to detect the slider module was the CSS class `_sliderContainer`.

## First user message

> check that this page has all these linked? https://www.thegoodguys.com.au/deals/bbqshttps://www.thegoodguys.com.au/deals/coffee-machineshttps://www.thegoodguys.com.au/deals/dishwashershttps://www.thegoodguys.com.au/deals/dryershttps://www.thegoodguys.com.au/deals/fridgeshttps://www.thegoodguys.com.au/deals/headphones-and-soundbarshttps://www.thegoodguys.com.au/deals/laptopshttps://www.thegoodguys.

## Topics

[[topic/bfcm]], [[topic/deals]], [[topic/eofy]], [[topic/inlink]], [[topic/plp]]

## Skills referenced

none detected
