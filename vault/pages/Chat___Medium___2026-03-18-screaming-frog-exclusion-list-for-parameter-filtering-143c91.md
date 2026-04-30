---
title: Screaming Frog exclusion list for parameter filtering (medium)
parent: Chat/Light/2026-03-18-screaming-frog-exclusion-list-for-parameter-filtering-143c91
uuid: 143c91e7-b8d2-4bf0-b0ca-2cfe65198b41
---

#chat/medium #project/main #status/completed

# Screaming Frog exclusion list for parameter filtering — Key User Messages

→ Light view: [[Chat/Light/2026-03-18-screaming-frog-exclusion-list-for-parameter-filtering-143c91]]
→ Full transcript: [[Chat/Full/2026-03-18-screaming-frog-exclusion-list-for-parameter-filtering-143c91]]

**Total user messages:** 8

---

### Message 1 — 2026-03-18T09:33

i need a screamingfrog exclusion list that covers params in here, except any search ones like ?search/q=

this is my current list:

https://analytics.thegoodguys.com.au/.*
https://googleads.g.doubleclick.net/.*
https://obseu.yougreencolumn.com/.*
https://.*.snapchat.com/.*
https://pixel.tapad.com/.*
https://www.paypal.*
https://www.google.com/maps.*
.*maps.google.*
https://recs-1a.particularaudience.com/.*
https://truerewards.com.au/.*
https://use.typekit.net/.*
https://www.google-analytics.com/.*
https://www.googleadservices.com/.*
https://www.youtube.com/.*
https://cdn.shopify.com/.*.pdf.*
.*AjaxLogonForm.*
.*utm_.*=.*
.*ga_.*=.*
.*gclid=.*
.*fbclid=.*
.*cid=.*
.*scid=.*
.*ecid=.*
.*mcid=.*
.*?gStoreCode=.*
.*campaign=.*
.*ref=.*
.*referrer=.*
.*source=.*
.*session=.*
.*sid=.*
.*phpsessid=.*
.*sess=.*
.*id=.*
.*nid=.*
.*pid=.*
.*sku=.*
.*productId=.*
.*PayOnlineView.*
.*AjaxOrderItemDisplayView.*
.*pageno=.*
.*pagenum=.*
.*sort=.*
.*order=.*
.*filter=.*
.*store=.*
.*branch=.*
.*location=.*
.*track=.*
.*tracking=.*
.*trace=.*
.*commercial.thegoodguys.com.au.*
.*?_ga=.*
.*checkout.thegoodguys.com.au/web-pixels.*
.*web-pixel.*
.*wpm@.*
https://www.thegoodguys.com.au/payonline/verify?hash=.*
i need a screamingfrog exclusion list that covers params in here, except any search ones like ?search/q=

this is my current list:

https://analytics.thegoodguys.com.au/.*
https://googleads.g.doubleclick.net/.*
https://obseu.yougreencolumn.com/.*
https://.*.snapchat.com/.*
https://pixel.tap

[truncated — see full transcript]

### Message 2 — 2026-03-18T09:35

remove any refinementlist or ?cf
remove any refinementlist or ?cf

### Message 3 — 2026-03-18T09:35

deduplicate - e.g. .*cq_.*

keep simple
deduplicate - e.g. .*cq_.*

keep simple

### Message 4 — 2026-03-18T09:35

no comments, sort logically
no comments, sort logically

### Message 5 — 2026-03-18T09:37

whats [?&] and why did you add it?
whats [?&] and why did you add it?

### Message 6 — 2026-03-18T09:38

but .*ga=.* would do tht too
but .*ga=.* would do tht too

### Message 7 — 2026-03-18T09:38

like `.*id=.*` matching `/solid-state-drive/`. unless theres a = in the url after id no?
like `.*id=.*` matching `/solid-state-drive/`. unless theres a = in the url after id no?

### Message 8 — 2026-03-18T09:39

yeah keep it simple stupid
yeah keep it simple stupid
