---
title: Redirect best practices and product URL strategy (medium)
parent: Chat/Light/2026-04-29-redirect-best-practices-and-product-url-strategy-795a95
uuid: 795a9560-49c4-4ec1-8318-f88b68a153f5
---

#chat/medium #project/main #status/active

# Redirect best practices and product URL strategy — Key User Messages

→ Light view: [[Chat/Light/2026-04-29-redirect-best-practices-and-product-url-strategy-795a95]]
→ Full transcript: [[Chat/Full/2026-04-29-redirect-best-practices-and-product-url-strategy-795a95]]

**Total user messages:** 39

---

### Message 1 — 2026-04-29T00:03

I want to check these redirects against our established best practices - as well as:

Remove any paramater URLs

We tend to not redirect products 1:1 from e.g. "panasonic-1tb" to "panasonic-2tb" as our product churn is more likely to cause chains... the only exception is when the URL is malformed (e.g. -- should be -)

I tend to instead use the last breadcrumb of the most similar product, which can be found in the breadcrumb metafield (underscore's represent slashes)
I want to check these redirects against our established best practices - as well as:

Remove any paramater URLs

We tend to not redirect products 1:1 from e.g. "panasonic-1tb" to "panasonic-2tb" as our product churn is more likely to cause chains... the only exception is when the URL is malformed (e.g. -- should be -)

I tend to instead use the last breadcrumb of the most similar product, which can be found in the breadcrumb metafield (underscore's represent slashes)

### Message 2 — 2026-04-29T00:10

how come there is ?istCoompany ?? how come you changed the format it was shopify from the start and shouldve been kept, create simple separate audit that only shows changed urls (before after) and why
how come there is ?istCoompany ?? how come you changed the format it was shopify from the start and shouldve been kept, create simple separate audit that only shows changed urls (before after) and why

### Message 3 — 2026-04-29T00:11

where is the csv for shopify?
where is the csv for shopify?

### Message 4 — 2026-04-29T00:19

tell me aboout this:

292 CHANGE rows were skipped because the destination product wasn't in the export so no breadcrumb could be resolved.
tell me aboout this:

292 CHANGE rows were skipped because the destination product wasn't in the export so no breadcrumb could be resolved.

### Message 5 — 2026-04-29T00:20

cross checkagainst sitemap audit
cross checkagainst sitemap audit

### Message 6 — 2026-04-29T00:21

WTF is going on im confused
WTF is going on im confused

### Message 7 — 2026-04-29T00:37

Correct to remove paramaters, product to product too, if needing category use most similar (the one in the ooriginal csv)'s bradcrump, otherwise use sitemap audit for best match.
Correct to remove paramaters, product to product too, if needing category use most similar (the one in the ooriginal csv)'s bradcrump, otherwise use sitemap audit for best match.

### Message 8 — 2026-04-29T01:21

i need a breakdown of pages, there may be pages that dont have a active or not active breadcrumb url - in which case use the recommended product redirect in the first csv and get THAT one's breadcrumb and use it as a proxy - if that fails use sitemap audit
i need a breakdown of pages, there may be pages that dont have a active or not active breadcrumb url - in which case use the recommended product redirect in the first csv and get THAT one's breadcrumb and use it as a proxy - if that fails use sitemap audit

### Message 9 — 2026-04-29T01:46

not every - remember i said malformed urls like -- or --- are fine to send to the - version? only correct pdp urls going to another correct pdp url
not every - remember i said malformed urls like -- or --- are fine to send to the - version? only correct pdp urls going to another correct pdp url

### Message 10 — 2026-04-29T02:27

create an xlsx with the final shopify import (with all fixes) and oone tab for changes, then a workflow summary list (simple) that complemetns this discussion (attached)
create an xlsx with the final shopify import (with all fixes) and oone tab for changes, then a workflow summary list (simple) that complemetns this discussion (attached)

### Message 11 — 2026-04-29T02:49

bullets here pls
bullets here pls

### Message 12 — 2026-04-29T02:49

workflow
workflow

### Message 13 — 2026-04-29T02:50

no i want bullets here
no i want bullets here

### Message 14 — 2026-04-29T02:51

change to strip paramaters, check status, if still 404 keep, else remoove
change to strip paramaters, check status, if still 404 keep, else remoove

### Message 15 — 2026-04-29T02:51

yes, move into workfloow
yes, move into workfloow

### Message 16 — 2026-04-29T02:53

add in conditions we set up for iphone, ipad, macbook as FYI at the bottom (also ocheck if this is folloowed in the shopify import)
add in conditions we set up for iphone, ipad, macbook as FYI at the bottom (also ocheck if this is folloowed in the shopify import)

### Message 17 — 2026-04-29T02:55

remove installation services. also, say in the workflow he can run this sitemap audit if needing a recent source of live pages and their breadcrumbs: 

https://colab.research.google.com/drive/1eprOG4LH4f2begEWnSFyUp5uFqGBjj0e?usp=sharing
remove installation services. also, say in the workflow he can run this sitemap audit if needing a recent source of live pages and their breadcrumbs: 

https://colab.research.google.com/drive/1eprOG4LH4f2begEWnSFyUp5uFqGBjj0e?usp=sharing

### Message 18 — 2026-04-29T02:57

wheres my bullet list here as workflow?:
wheres my bullet list here as workflow?:

### Message 19 — 2026-04-29T02:58

i asked if it impacted the shopoify import and for you too give me bullets here with instructions around the collba
i asked if it impacted the shopoify import and for you too give me bullets here with instructions around the collba

### Message 20 — 2026-04-29T02:58

re-create the xlsx without workflow tab, instead show workflow here as a bullet / list / numbered flow i can share over slack - keep succinct
re-create the xlsx without workflow tab, instead show workflow here as a bullet / list / numbered flow i can share over slack - keep succinct

### Message 21 — 2026-04-29T03:46

1. why are some pages redirecting to home when they have better potential locations?
Redirect from	Redirect to
/gold-service-extras-terms-and-	/
/returns-and-refunds	/
/taveceshtoreces-tems-and-conditions	/
/promotional-terms-and-conditions	/
/contract-gold-service-extra-team	/


/best-christmas-movies-plus-best-televisions-for-watching	/
/internationalcallingpacks	/
/portal/page/portal/tggweb	/


we should only send administrative erroor type pages to homepage, rest there will be better options. 




1. why is the same page in there several times? all in "from" should be unique?
1. why are some pages redirecting to home when they have better potential locations?
Redirect from	Redirect to
/gold-service-extras-terms-and-	/
/returns-and-refunds	/
/taveceshtoreces-tems-and-conditions	/
/promotional-terms-and-conditions	/
/contract-gold-service-extra-team	/


/best-christmas-movies-plus-best-televisions-for-watching	/
/internationalcallingpacks	/
/portal/page/portal/tggweb	/


we should only send administrative erroor type pages to homepage, rest there will be better options. 




1. why is the same page in there several times? all in "from" should be unique?

### Message 22 — 2026-04-29T03:53

yes
yes

### Message 23 — 2026-04-29T03:53

have you checked the HTTP status of de-paramaterised pages
have you checked the HTTP status of de-paramaterised pages

### Message 24 — 2026-04-29T04:22

do it and produce the new sheet.
do it and produce the new sheet.

### Message 25 — 2026-04-29T06:52

some issues:
some issues:

### Message 26 — 2026-04-29T06:52

what about the 301s
what about the 301s

### Message 27 — 2026-04-29T06:55

replace all /phones-and-wearables/mobile-phone-accessories/phone-chargers-and-accessories with /phones-and-wearables/phone-accessories/phone-chargers-and-accessories

* if to = the first one disregard
replace all /phones-and-wearables/mobile-phone-accessories/phone-chargers-and-accessories with /phones-and-wearables/phone-accessories/phone-chargers-and-accessories

* if to = the first one disregard

### Message 28 — 2026-04-29T06:55



### Message 29 — 2026-04-29T06:56

what mismatches did you describe before?
1. Wrong category (token match failures)

* 


how did they happen?
what mismatches did you describe before?
1. Wrong category (token match failures)

* 


how did they happen?

### Message 30 — 2026-04-29T06:57

you may never guess a url, its from sitemap audit only if you fall back
you may never guess a url, its from sitemap audit only if you fall back

### Message 31 — 2026-04-29T06:57

no, you should use sitemap instead if no breadcrumb exists. but in the original tgg final didnt the recommended pdp be able to be matched to its breadcrumb?
no, you should use sitemap instead if no breadcrumb exists. but in the original tgg final didnt the recommended pdp be able to be matched to its breadcrumb?

### Message 32 — 2026-04-29T06:58

destination handle > previous matched url (seb) > sitemap audit > that matched urls breadcrumb with a summary for myself
destination handle > previous matched url (seb) > sitemap audit > that matched urls breadcrumb with a summary for myself

### Message 33 — 2026-04-29T06:59

why is this 2? Destination handle → sitemap Previous Breadcrumb URL
what doe sit mean?
why is this 2? Destination handle → sitemap Previous Breadcrumb URL
what doe sit mean?

### Message 34 — 2026-04-29T07:01

ok. map out the flow and run it
ok. map out the flow and run it

### Message 35 — 2026-04-29T07:03

now, write up a full breakdown of this proocess and methodology, the requirements, the data / exports needed - remoove all reference to seb and instead call that "nearest match from live pages" - it's the same thing (thjats what seb did) - break it down to a full process with flow and requirement and outcome - the final result should help me build a new 301 mapping skill, where the result is a inline (chat) table as well as a shopify import ready CSV.
now, write up a full breakdown of this proocess and methodology, the requirements, the data / exports needed - remoove all reference to seb and instead call that "nearest match from live pages" - it's the same thing (thjats what seb did) - break it down to a full process with flow and requirement and outcome - the final result should help me build a new 301 mapping skill, where the result is a inline (chat) table as well as a shopify import ready CSV.

### Message 36 — 2026-04-29T07:04

wait - in the manual how can you have: /instax-square-sq1-camera-chalk-white-87021
 did not resolve when it would EITHER be in the shopify export (use breadcrumb of nearest match) OR in the sitemap audit?
wait - in the manual how can you have: /instax-square-sq1-camera-chalk-white-87021
 did not resolve when it would EITHER be in the shopify export (use breadcrumb of nearest match) OR in the sitemap audit?

### Message 37 — 2026-04-29T07:17



### Message 38 — 2026-04-29T07:45

what did we say about /?
what did we say about /?

### Message 39 — 2026-04-29T07:47

there are massive issues in your formatting - what are you doing? create a list of safeguards, checklist items, guardrails for the 301 process- audit yourself against it, line by line
there are massive issues in your formatting - what are you doing? create a list of safeguards, checklist items, guardrails for the 301 process- audit yourself against it, line by line
