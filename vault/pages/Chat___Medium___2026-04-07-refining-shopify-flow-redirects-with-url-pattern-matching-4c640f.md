---
title: Refining Shopify flow redirects with URL pattern matching (medium)
parent: Chat/Light/2026-04-07-refining-shopify-flow-redirects-with-url-pattern-matching-4c640f
uuid: 4c640f7a-8395-4200-ba4a-a38476d6c48e
---

#chat/medium #project/main #status/abandoned

# Refining Shopify flow redirects with URL pattern matching — Key User Messages

→ Light view: [[Chat/Light/2026-04-07-refining-shopify-flow-redirects-with-url-pattern-matching-4c640f]]
→ Full transcript: [[Chat/Full/2026-04-07-refining-shopify-flow-redirects-with-url-pattern-matching-4c640f]]

**Total user messages:** 16

---

### Message 1 — 2026-03-31T06:01

I have this flow in shopify flow:

it currently auto redirects based on breadcrumb, however sometimes it is limited (breadcrumbs less detailed than actual opportunity to redirect)

for example, an ipad air product redirects to ipad, not ipad air.

I will attach our list of redirects, and youll be able to see the ipad air, pro etc. and macbook pages (and any others you can see) that have been re-done for more indepth redirection - can we rewrite the flow to "if url contains xxx" it gets a specific treatment that is more detailed? same for home installation and the extended warranty urls ive done.
I have this flow in shopify flow:

it currently auto redirects based on breadcrumb, however sometimes it is limited (breadcrumbs less detailed than actual opportunity to redirect)

for example, an ipad air product redirects to ipad, not ipad air.

I will attach our list of redirects, and youll be able to see the ipad air, pro etc. and macbook pages (and any others you can see) that have been re-done for more indepth redirection - can we rewrite the flow to "if url contains xxx" it gets a specific treatment that is more detailed? same for home installation and the extended warranty urls ive done.

### Message 2 — 2026-03-31T06:05

What other patterns?
What other patterns?

### Message 3 — 2026-03-31T06:08

not apple specific - in ALL the redirects where can we add in more detail - compared to the breadcrumb you'd get in the attached files (Breadcrumb (product.metafields.tgg.breadcrumb)
)
not apple specific - in ALL the redirects where can we add in more detail - compared to the breadcrumb you'd get in the attached files (Breadcrumb (product.metafields.tgg.breadcrumb)
)

### Message 4 — 2026-03-31T06:10

you sure? youve checked all existing redirects vs breadcrumbs and looked if theres any optimisation we can do?
you sure? youve checked all existing redirects vs breadcrumbs and looked if theres any optimisation we can do?

### Message 5 — 2026-03-31T06:14

we are not (currently) re-mapping existing redirects, we are rebuilding the automation flow - create the new flow (justify your ideas) but also provide a Brief for another LLM down the line to re-work the existing redirects
we are not (currently) re-mapping existing redirects, we are rebuilding the automation flow - create the new flow (justify your ideas) but also provide a Brief for another LLM down the line to re-work the existing redirects

### Message 6 — 2026-04-07T04:45

this is far to complex - just note the base rules we should have in place.
this is far to complex - just note the base rules we should have in place.

### Message 7 — 2026-04-07T04:52

add in if breadcrumb is ipad or macbook, we dont want to accidentally do this to ipad-pro-screen-protector
add in if breadcrumb is ipad or macbook, we dont want to accidentally do this to ipad-pro-screen-protector

### Message 8 — 2026-04-07T04:58

`   - Only apply if breadcrumb does NOT contain `ipad` or `macbook``

no, only append IF 

so if the breadcrumb was computers-and-tables/ipad but it contains ipad air send it to ipad air instead
`   - Only apply if breadcrumb does NOT contain `ipad` or `macbook``

no, only append IF 

so if the breadcrumb was computers-and-tables/ipad but it contains ipad air send it to ipad air instead

### Message 9 — 2026-04-07T04:59

remove warranty part - remove the brand mention, i never said anything about that, did i?
remove warranty part - remove the brand mention, i never said anything about that, did i?

### Message 10 — 2026-04-07T04:59

im asking did i?
im asking did i?

### Message 11 — 2026-04-07T05:09

FOR INSTALLS TOO BROAD, ONLY IF THOSE + BREADCRUMB CONTAINS: 

installation-and-services_installs-and-services

REMOVE THE BRAND HUBS AND WARRANTY AND DEFAULT
FOR INSTALLS TOO BROAD, ONLY IF THOSE + BREADCRUMB CONTAINS: 

installation-and-services_installs-and-services

REMOVE THE BRAND HUBS AND WARRANTY AND DEFAULT

### Message 12 — 2026-04-07T05:17

what other concepts could you ideate based off this?

e.g. find product patterns and breadcrumbs similar to the issue with too simple breadcrumbs happening from ipad and macbook
what other concepts could you ideate based off this?

e.g. find product patterns and breadcrumbs similar to the issue with too simple breadcrumbs happening from ipad and macbook

### Message 13 — 2026-04-07T05:19

why gas oven to freestanding if its got: /cooking-and-dishwashers/ovens/gas-ovens ??
you are to improve the redirect breadcrumbs by making them less general, not overwrite??
why gas oven to freestanding if its got: /cooking-and-dishwashers/ovens/gas-ovens ??
you are to improve the redirect breadcrumbs by making them less general, not overwrite??

### Message 14 — 2026-04-07T05:19

why didnt you see that in sitemap audit? that the page existed?
why didnt you see that in sitemap audit? that the page existed?

### Message 15 — 2026-04-07T05:24

look properly - and remember, the breadcrumb URL rules are #1, only nische if you feel the breadcrumb isnt clear enough. like on ipad. 

note the breadcrumb url in the export doc
look properly - and remember, the breadcrumb URL rules are #1, only nische if you feel the breadcrumb isnt clear enough. like on ipad. 

note the breadcrumb url in the export doc

### Message 16 — 2026-04-07T05:27

audit the sheet you just got as well as the previous one with sitemap audit for skus - idenitfy any more opportjunitie
audit the sheet you just got as well as the previous one with sitemap audit for skus - idenitfy any more opportjunitie
