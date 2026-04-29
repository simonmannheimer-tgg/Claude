---
title: AI blog intro audit and expert attribution review
date: 2026-04-29
project: Blog EEAT / AIO Optimisation (792 Articles)
status: completed
score: 5/5
uuid: 11fa3047-9e68-4745-a0a0-b330ff2af6ae
---

#chat/light #project/blog-eeat-aio-optimisation-792-articles #status/completed #topic/aeo #topic/blog #topic/contentful #topic/copy #topic/eofy #topic/inlink #topic/keyword #topic/meta #topic/plp #topic/redirect #topic/regex #topic/schema #topic/shopify #skill/tgg-content-strategist #skill/tgg-contentful-linker #skill/tgg-copywriting #skill/tgg-seo-specialist

# AI blog intro audit and expert attribution review

- **Date:** [[2026-04-29]]
- **Project:** [[Projects/Blog EEAT / AIO Optimisation (792 Articles)]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 176
- **Chat URL:** https://claude.ai/chat/11fa3047-9e68-4745-a0a0-b330ff2af6ae
- **Medium view:** [[Chat/Medium/2026-04-29-ai-blog-intro-audit-and-expert-attribution-review-11fa30]]
- **Full transcript:** [[Chat/Full/2026-04-29-ai-blog-intro-audit-and-expert-attribution-review-11fa30]]

## Summary

**Conversation overview**

This conversation centered on a complex, multi-phase content remediation project for The Good Guys (TGG) blog platform, specifically focused on AI-generated intro summaries for 792 blog articles. The person was working to bring these summaries to production quality, with work spanning expert attribution fixes, paragraph improvements, and metadata alignment per EEAT/AIO optimization standards. The session began as a continuation of prior iteration work (Iterations 1-5 documented in uploaded files), with the person providing a compacted conversation summary and transcript reference as starting context.

The core remediation work involved fixing the final output file TGG_Blog_AI_Intros_FINAL_COMPLETE.xlsx, which required restoring missing expert bullets to specific rows, fixing a templated paragraph at Row 101 (Nespresso article), and adding verified credentials to all external expert attributions. A critical policy distinction ran throughout the work: the correct approach was a "retained-expert policy" (keep all source-supported experts whether TGG or external), not a "TGG National Category Managers only" policy that had incorrectly driven earlier iterations. Expert title research was conducted via web search and live blog page visits to find verified affiliations for all external experts, resulting in formats such as "John Wong (The Good Guys Buyer, Mobile Phones)," "Alice Zaslavsky (Cook, Author, and TV Presenter)," and "Matt Gaskell (Director, Devices & Services Partnerships ANZ, Google)." The person approved Alice Zaslavsky and Jake Dyson titles as reference points for the correct format, and flagged that generic titles like "Tech Expert" were insufficient without entity affiliation context.

Once the file work concluded, the conversation shifted to prompt improvement. The person provided the original Iteration 5 prompt (TGG_-_Blog_Intro_Prompt.docx) and asked Claude to identify what was wrong, what was fixed, and what remained. Key issues identified and corrected in the updated prompt included: paragraph length stated as words (35-70) when it should be characters (220-250), missing expert placement rule (expert bullet must always be last), missing parenthetical title format for expert credentials, missing attribution verb requirement (says, recommends, suggests, etc.), and missing multiple-expert priority hierarchy. Claude then ran duplication and edge case analysis on the updated prompt, finding two true duplications (H2 heading list appearing twice, attribution verb list repeated in validation checklist) and flagging five edge cases needing rules (expert names with parentheses, bullets exceeding 95 chars even when abbreviated, expert names without titles in source, past-tense attribution verbs, validation checklist gap). The person corrected a significant misunderstanding: Claude had created a "banned words" list (blocking Discover, Explore, Shop, The, This, For as first words), when the actual intent was only to avoid repetitive cookie-cutter phrases, not individual words. The person instructed that word-level bans should never be applied without asking first. A fixes checklist table with 10 items was produced, with 3 items still awaiting clarification from the person on banned words scope, The Good Guys S2 placement rule applicability to blogs vs PLP, and brand PLP word restrictions scope. The session ended with the person requesting all 792 blog URLs extracted, then a brief written for a separate AI to validate live summaries against requirements, before instructing Claude to disregard all messages from that day and return to PLP work.

## First user message

> These are AI introduction summaries we are working on bulk uploading to all our blogs for Ai visibility (AI SEO)  The outcome will be similar to this page: https://www.thegoodguys.com.au/whats-new/how-to-move-fridge  The attached 'all blog intro' content is to be reviewed by you, the tgg seo expert on account of our brand rules and best practices, any issues with the content - i will give you the 

## Topics

[[topic/aeo]], [[topic/blog]], [[topic/contentful]], [[topic/copy]], [[topic/eofy]], [[topic/inlink]], [[topic/keyword]], [[topic/meta]], [[topic/plp]], [[topic/redirect]], [[topic/regex]], [[topic/schema]], [[topic/shopify]]

## Skills referenced

[[skill/tgg-content-strategist]], [[skill/tgg-contentful-linker]], [[skill/tgg-copywriting]], [[skill/tgg-seo-specialist]]
