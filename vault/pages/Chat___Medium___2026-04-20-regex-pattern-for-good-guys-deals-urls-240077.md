---
title: Regex pattern for Good Guys deals URLs (medium)
parent: Chat/Light/2026-04-20-regex-pattern-for-good-guys-deals-urls-240077
uuid: 240077d3-c4b0-4428-980f-95b0011e68fd
---

#chat/medium #project/main #status/completed

# Regex pattern for Good Guys deals URLs — Key User Messages

→ Light view: [[Chat/Light/2026-04-20-regex-pattern-for-good-guys-deals-urls-240077]]
→ Full transcript: [[Chat/Full/2026-04-20-regex-pattern-for-good-guys-deals-urls-240077]]

**Total user messages:** 4

---

### Message 1 — 2026-04-20T04:52

i need a regex of this:
https://www.thegoodguys.com.au/deals/technology|https://www.thegoodguys.com.au/deals/smart-home|https://www.thegoodguys.com.au/deals/phone-and-smart-watches|https://www.thegoodguys.com.au/deals/coffee-machines|https://www.thegoodguys.com.au/deals/washing-machines|https://www.thegoodguys.com.au/deals/vacuums-and-cleaning|https://www.thegoodguys.com.au/deals/dishwashers|https://www.thegoodguys.com.au/deals/headphones-and-soundbars|https://www.thegoodguys.com.au/deals/laptops|https://www.thegoodguys.com.au/deals/cooking|https://www.thegoodguys.com.au/deals/dryers|https://www.thegoodguys.com.au/deals/kitchen-appliances|https://www.thegoodguys.com.au/deals/fridges|https://www.thegoodguys.com.au/deals/microwaves|https://www.thegoodguys.com.au/deals/kitchen|https://www.thegoodguys.com.au/deals/kitchenware-sinks-and-taps|https://www.thegoodguys.com.au/deals/fridge-and-laundry|https://www.thegoodguys.com.au/deals/health-fitness-beauty|https://www.thegoodguys.com.au/deals/tvs|https://www.thegoodguys.com.au/deals/bundle|https://www.thegoodguys.com.au/deals/heaters|https://www.thegoodguys.com.au/deals/bbqs|https://www.thegoodguys.com.au/deals/air-conditioners-and-fans|https://www.thegoodguys.com.au/deals
where the final (hub) is exact match only. 
I alsoo need each of these pages pre-mirgation equivalent (same deal on any hub)
as 1 regex. remove the category/product urls, and anything black friday or boxing day.
https://www.thegoodguys.com.au/buy/air-conditioner-a

[truncated — see full transcript]

### Message 2 — 2026-04-20T05:06

look at over-time perfoormance by page, show what pages are dooing well, what terms are doing well, and noot soo well, break down branded vs non branded ((?:^|\W)(?:(?:the|teh|te|th3|t3h|5he)?\s*[._-]?\s*(?:good|gud|god|goo|goog|gd)[\s._-]+(?:guy|giy|gys|guyz|guyy|giya|giyd|fuy|fuys|bguy)s?|(?:the|te|teh)?(?:good|god|gud|goo)guy(?:s{1,2}|a|d|e|y|z|ya|yd)?(?![a-z])|(?<![a-z0-9])tgg(?![a-z0-9]))(?:\W|$))

I want to understand monthly (with highligths on june (eofy) nov (black friday) and dec (boxing day) how various categories perform.
look at over-time perfoormance by page, show what pages are dooing well, what terms are doing well, and noot soo well, break down branded vs non branded ((?:^|\W)(?:(?:the|teh|te|th3|t3h|5he)?\s*[._-]?\s*(?:good|gud|god|goo|goog|gd)[\s._-]+(?:guy|giy|gys|guyz|guyy|giya|giyd|fuy|fuys|bguy)s?|(?:the|te|teh)?(?:good|god|gud|goo)guy(?:s{1,2}|a|d|e|y|z|ya|yd)?(?![a-z])|(?<![a-z0-9])tgg(?![a-z0-9]))(?:\W|$))

I want to understand monthly (with highligths on june (eofy) nov (black friday) and dec (boxing day) how various categories perform.

### Message 3 — 2026-04-20T05:13

Save this visual from earlier as an artifact: "tgg_deals_performance_dashboard"
Save this visual from earlier as an artifact: "tgg_deals_performance_dashboard"

### Message 4 — 2026-04-20T05:19

add in a way to filter by sale event, i want top queries to be all and searchable, i want avg. position and impressions to be used too, i want category breakdowns for things like TV went down with representation as to why. I want coloour legend on ctegoory trend for the dots, and change the dots to be different coloours, anything else that wouold improve?
add in a way to filter by sale event, i want top queries to be all and searchable, i want avg. position and impressions to be used too, i want category breakdowns for things like TV went down with representation as to why. I want coloour legend on ctegoory trend for the dots, and change the dots to be different coloours, anything else that wouold improve?
