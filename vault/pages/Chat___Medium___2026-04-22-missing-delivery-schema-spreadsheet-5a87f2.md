---
title: Missing delivery schema spreadsheet (medium)
parent: Chat/Light/2026-04-22-missing-delivery-schema-spreadsheet-5a87f2
uuid: 5a87f256-8439-422c-8752-b5431ed674bb
---

#chat/medium #project/main #status/completed

# Missing delivery schema spreadsheet — Key User Messages

→ Light view: [[Chat/Light/2026-04-22-missing-delivery-schema-spreadsheet-5a87f2]]
→ Full transcript: [[Chat/Full/2026-04-22-missing-delivery-schema-spreadsheet-5a87f2]]

**Total user messages:** 75

---

### Message 1 — 2026-04-21T04:25



### Message 2 — 2026-04-21T04:36



### Message 3 — 2026-04-21T04:55

you cant make up dynamics like (LLT) it needs to be the same format as we get out of shopify or fledgling. 

you also need to show where the data is from (shopify, metafields etc.)

if fledling is referenced and we can get it from metafields, we want that instead. 

If doing HTML - it should be a PY file so it can be hosted on streamlit, make the colours lighter and nicer, make it more intuitive, ensure there's a flowchart of if this then that with clickable types, ensure there's a checklist 

and finally, before you begin, ensure that you think my recommended plan is good and bestpractice.
you cant make up dynamics like (LLT) it needs to be the same format as we get out of shopify or fledgling. 

you also need to show where the data is from (shopify, metafields etc.)

if fledling is referenced and we can get it from metafields, we want that instead. 

If doing HTML - it should be a PY file so it can be hosted on streamlit, make the colours lighter and nicer, make it more intuitive, ensure there's a flowchart of if this then that with clickable types, ensure there's a checklist 

and finally, before you begin, ensure that you think my recommended plan is good and bestpractice.

### Message 4 — 2026-04-21T05:31

For Liquid to compute `OOS_PO-Y_LT7` transit times at render time, LLT must be in a metafield < do not assume my schema is liquid rendered? 

do not assume anything - you are simply following my format - our job is to simply (based on the plan in the matrix) show a dev how the new schema will work and what data to pull for what. also for releasedate you will need to specify a suggested method for if release date later than today, take releasedate - today get number of days 

if i click on a specific part of the matrix at the front of the html (which i really like) it should show inputs and also example code with dynamic toekn. do a before and after 

remove any notes like "same logic as xxx sm v2 noes this is the same 

instead  ASK me for any quesiotns you have, we cannot under any circumstances have the dev confused. 

for any changes like remove shipping details, show a before and after - ensure theres a example of real pdp json (you can pick one sku and parse its dom and get the pdp schema json) to show the actual before after.

Same as "PREORDER-PL" (pick one?) if state is PRE ORDER treat as add to cart preorder-pl. 


the same as agency miele note is overpowered by remove avaliability and all shipping note. 

also i need to look into best schema for "coming soon"

coming soon is its not yet able to be purchased, so cant do pre-order, we usually go coming soon > preorder > available

dont love outofstock for coming soon but unsure best option. 


aslo ignore: General Sch

[truncated — see full transcript]

### Message 5 — 2026-04-21T06:37

if Lowest leadtime isnt a metafield you need to same "lowest lead time" (same as fledgling product report) - but in a nicer way. 

for release date field,

* tgg.pre_order_date is when customers can reserve the product before it’s officially released.
* tgg.release_date is when the product is available for everyone to buy, and pre-orders typically end.


lets do option B for coming soon. 

all agency- gets the remove avaliablity and shipping 

order now, learn to read:

ADD TO CARTSTAND-ALONE-SERVICEn/an/aRemove all schemaRemove all schemaNOT LIVE, ONLY USED IN CARTADD TO CARTUNCLASSIFIEDn/an/aRemove Shipping DetailsRemove Shipping Details
if Lowest leadtime isnt a metafield you need to same "lowest lead time" (same as fledgling product report) - but in a nicer way. 

for release date field,

* tgg.pre_order_date is when customers can reserve the product before it’s officially released.
* tgg.release_date is when the product is available for everyone to buy, and pre-orders typically end.


lets do option B for coming soon. 

all agency- gets the remove avaliablity and shipping 

order now, learn to read:

ADD TO CARTSTAND-ALONE-SERVICEn/an/aRemove all schemaRemove all schemaNOT LIVE, ONLY USED IN CARTADD TO CARTUNCLASSIFIEDn/an/aRemove Shipping DetailsRemove Shipping Details

### Message 6 — 2026-04-21T06:53

Continue
Continue

### Message 7 — 2026-04-21T07:05

no, STAND-ALONE-SERVICE = remove all schema

UNCLASSIFIED = Remove Shipping Details
no, STAND-ALONE-SERVICE = remove all schema

UNCLASSIFIED = Remove Shipping Details

### Message 8 — 2026-04-21T07:14

ALSO SHOW IT AS HTML ARTIFACT IN CLAUDE :)
ALSO SHOW IT AS HTML ARTIFACT IN CLAUDE :)

### Message 9 — 2026-04-21T08:24

nothing happens when i click them. much worse
nothing happens when i click them. much worse

### Message 10 — 2026-04-21T23:30

I preferred the previous format where it opened up on click, also the design is goofy. The flow should be like a flowchart if this then that. LLT source HAS been determined?

where is my JIRA description?
I preferred the previous format where it opened up on click, also the design is goofy. The flow should be like a flowchart if this then that. LLT source HAS been determined?

where is my JIRA description?

### Message 11 — 2026-04-22T01:15

I want this matrix back, but less AI looking, clearner - remove blockers, flag those only to me. unless already resolved. keep long ab on discontinued and instore.

I also need a detailed Jira that uses the same tables we see in the matrix, e.g. 

purchase_state
ADD TO CART
product_life_cycle
PARCELISED
product_state_message
IS_PO-Y or IS_PO-N
Schema Output
availability
https://schema.org/InStock
shippingDetails
[shipping detrails shown here as example schema]
handling (min/max)
0 / 0
transit (min/max)
0 / 1
Standard parcelised delivery. Transit 0–1 day. No dynamic tokens required — availability is fixed InStock, transit is fixed 0–1.



im going to keep auditing while i wait for confirmation on the LLT source, take notes, do not yet implement fixes.

* tgg.pre_order_date is when customers can reserve the product before it’s officially released. <  why do you use     "availabilityStarts": "{{ tgg.release_date }}",?? that is when the preorder ends and isnt part of this schema as it then just goes to add to cart with not preorder.

remove     "availableAtOrFrom": { "@type": "Place", "url": "https://www.thegoodguys.com.au/store-finder" }, < never said to add this. I said to change availability.

sold out OOS_PO-Y_LT61 = Handling time =61 days, then delivery 1 or 2 depending on PL or BB.

buy at miele gets no offer and no availability on all purchase states - same as agency, right?

OOS still purchasable shoouldnt be clicked by a tab should be its own element. 

oos parcelised sh

[truncated — see full transcript]

### Message 12 — 2026-04-22T01:29

tgg.pre_order_date = yes

remove availableator from - yes remove. 

sold out 61 fixed, and yes to pl bb
oos yes

Agency dropship remove only availabilty and shipping - not the whole offer. these are sold on other sites than ours, so cant guarantee stock or shipping times, but we get the prices etc. from them so that should be corect
tgg.pre_order_date = yes

remove availableator from - yes remove. 

sold out 61 fixed, and yes to pl bb
oos yes

Agency dropship remove only availabilty and shipping - not the whole offer. these are sold on other sites than ours, so cant guarantee stock or shipping times, but we get the prices etc. from them so that should be corect

### Message 13 — 2026-04-22T01:30

* Remove `external_product_url` token — never specified < yes and any other additions notes, warnigns or assumptions youve added - flag to me what you added first.
coming soon yes

remove commentary that isnt about dev implementation

premium is same as Bug bulky. not parecelised.
* Remove `external_product_url` token — never specified < yes and any other additions notes, warnigns or assumptions youve added - flag to me what you added first.
coming soon yes

remove commentary that isnt about dev implementation

premium is same as Bug bulky. not parecelised.

### Message 14 — 2026-04-22T02:31

we should only be changing what we are changing, so if in before, should be in after, but shouldnt include anything outside of what we need, just the parts needing change, and some context (e.g. offer block up until x point)

* `acceptedPaymentMethod` array — same, BEFORE only
* `seller` block — same, BEFORE only
as above

* All commentary notes not about dev implementation (e.g. "product is still purchasable", "not BackOrder or OutOfStock", "confirm with fulfilment") — removing < yes

dropship bb is = agency- so should have no instock and no shipping. 

incorrect combo same as instore only

order now same as STAND-ALONE-SERVICE
we should only be changing what we are changing, so if in before, should be in after, but shouldnt include anything outside of what we need, just the parts needing change, and some context (e.g. offer block up until x point)

* `acceptedPaymentMethod` array — same, BEFORE only
* `seller` block — same, BEFORE only
as above

* All commentary notes not about dev implementation (e.g. "product is still purchasable", "not BackOrder or OutOfStock", "confirm with fulfilment") — removing < yes

dropship bb is = agency- so should have no instock and no shipping. 

incorrect combo same as instore only

order now same as STAND-ALONE-SERVICE

### Message 15 — 2026-04-22T02:48

where is my jira ticket
where is my jira ticket

### Message 16 — 2026-04-22T03:13

do you feel you have followed my instructionos around the html? i dont see you updateing it back to how it was before, using a long block for things like discoontinued, the colours should be back as v1 was, and no emojis, no unclickable piulls, no reference to simon v2 ets.
do you feel you have followed my instructionos around the html? i dont see you updateing it back to how it was before, using a long block for things like discoontinued, the colours should be back as v1 was, and no emojis, no unclickable piulls, no reference to simon v2 ets.

### Message 17 — 2026-04-22T03:14

alsoo text centered and middle aligned, cleaner UI
alsoo text centered and middle aligned, cleaner UI

### Message 18 — 2026-04-22T03:53

i asked for one long box for things that has only 1 state like discontinued. i asked to not include anything that isnt changing, e.g. "category model height - only the part thats changing (offer)

use this one product as the example for all states and lifecycles but state its an example (if xxx was oos this that) 

dont need to use it for any example where all schema is removed. 

use other parts
i asked for one long box for things that has only 1 state like discontinued. i asked to not include anything that isnt changing, e.g. "category model height - only the part thats changing (offer)

use this one product as the example for all states and lifecycles but state its an example (if xxx was oos this that) 

dont need to use it for any example where all schema is removed. 

use other parts

### Message 19 — 2026-04-22T03:53

remove any reference to incorrect combo also
remove any reference to incorrect combo also

### Message 20 — 2026-04-22T04:33

fix the codeblock colour formats.

also - not "removed removed removed just show before and after, the difference will be clear?

same with // was: "WebPage" < before after clears this oout. 


```
// Example: Dyson V8 Cyclone Cordless Vacuum — SKU 50096116
// If this product had purchase_state: NOT AVAILABLE (any lifecycle)

```
fix the codeblock colour formats.

also - not "removed removed removed just show before and after, the difference will be clear?

same with // was: "WebPage" < before after clears this oout. 


```
// Example: Dyson V8 Cyclone Cordless Vacuum — SKU 50096116
// If this product had purchase_state: NOT AVAILABLE (any lifecycle)

```

### Message 21 — 2026-04-22T04:34

// Example: Dyson V8 Cyclone Cordless Vacuum — SKU 50096116
// If this product had purchase_state: NOT AVAILABLE (any lifecycle)


should be above the before after result
// Example: Dyson V8 Cyclone Cordless Vacuum — SKU 50096116
// If this product had purchase_state: NOT AVAILABLE (any lifecycle)


should be above the before after result

### Message 22 — 2026-04-22T04:34

where did i approve this?

price
REMOVERemove
where did i approve this?

price
REMOVERemove

### Message 23 — 2026-04-22T04:34

where else did you take liberties?
where else did you take liberties?

### Message 24 — 2026-04-22T04:39

remove anything you werent instructed - justify after why you added in the first place

cooming soon yes remove offer block

i want harcoded 61 

premium = same as big bulky. 

revew the attached conversation for fuller context.
remove anything you werent instructed - justify after why you added in the first place

cooming soon yes remove offer block

i want harcoded 61 

premium = same as big bulky. 

revew the attached conversation for fuller context.

### Message 25 — 2026-04-22T04:56

all should have before after except ones where all schema is removed?
all should have before after except ones where all schema is removed?

### Message 26 — 2026-04-22T04:57

clarify that it is PRODUCT schema that should be removed, not others
clarify that it is PRODUCT schema that should be removed, not others

### Message 27 — 2026-04-22T05:02

quality control against plan and feedback
quality control against plan and feedback

### Message 28 — 2026-04-22T05:19

Instock and OOS parcelised (and any version) should have its own clickable box... not be under the add to cart parcelised... the acceptedpayment methos seller etc. is not needed as i said we shouls only show  the sections being changed.

idont need any fucking coomments?? i said im happy for you to tell me what you do but if the comment doesnt help a dev who has no understanding of the project outside the jira or this tool, it shouldnt be in there. 

preorder bb is Pre-Order Release Date - Today's date (this becomes its handling time) it does not have any LLT on it. then because its bb 2 days transit.

Are the 1d (PL) / 2d (BB) transit days relative to the release date or the order date? doesnt matter, because transit and handling are separate values, you arent putting any dates, only day counts - what the fuck even does release date vs order date mean
Instock and OOS parcelised (and any version) should have its own clickable box... not be under the add to cart parcelised... the acceptedpayment methos seller etc. is not needed as i said we shouls only show  the sections being changed.

idont need any fucking coomments?? i said im happy for you to tell me what you do but if the comment doesnt help a dev who has no understanding of the project outside the jira or this tool, it shouldnt be in there. 

preorder bb is Pre-Order Release Date - Today's date (this becomes its handling time) it does not have any LLT on it. then because its bb 2 days transit.

Are the 1d (PL) / 2d (BB)

[truncated — see full transcript]

### Message 29 — 2026-04-22T05:28

should the min max be 0-1 not 1-1?
should the min max be 0-1 not 1-1?

### Message 30 — 2026-04-22T05:31

No, im asking you, if instock parelised its 0 day handling, 1 day transit, is that 0/0 and 1/1 or? is there a risk when putting 0/1 transit google could think 0 days transit? should we lock the range?

(IS) is redundant, if not (OOS) it is instock, so remove that.
No, im asking you, if instock parelised its 0 day handling, 1 day transit, is that 0/0 and 1/1 or? is there a risk when putting 0/1 transit google could think 0 days transit? should we lock the range?

(IS) is redundant, if not (OOS) it is instock, so remove that.

### Message 31 — 2026-04-22T05:38

can we fix the ui so its not so compressed, oos not on its own line? center headers vertical and horizontal, can we add to the front summary:

Parcelised: instock + shipping > instead Instock 0 day handling 1 day shipping
can we fix the ui so its not so compressed, oos not on its own line? center headers vertical and horizontal, can we add to the front summary:

Parcelised: instock + shipping > instead Instock 0 day handling 1 day shipping

### Message 32 — 2026-04-22T05:40

no i wanted "InStock
0d handling / 1d transit" to be what was on the clickable card in the matrix, not a separate line

also UI wise the popup with product information should take up half the screenwidth, its so small rihgt now.
no i wanted "InStock
0d handling / 1d transit" to be what was on the clickable card in the matrix, not a separate line

also UI wise the popup with product information should take up half the screenwidth, its so small rihgt now.

### Message 33 — 2026-04-22T05:42

make them wider so it doesnt break the line, you have space
make them wider so it doesnt break the line, you have space

### Message 34 — 2026-04-22T05:45

availableAtOrFrom
OMIT — cannot specify individual storesRemove < if this isnt recommended anywhere... why the fuck woould you include it
availableAtOrFrom
OMIT — cannot specify individual storesRemove < if this isnt recommended anywhere... why the fuck woould you include it

### Message 35 — 2026-04-22T05:47

shouldnt have   // "shippingDetails": REMOVED - shoule be 

before:


```
// Dyson V8 Cyclone Cordless Vacuum — SKU 50096116
"mainEntityOfPage": { "@type": "WebPage" },
"offers": {
  "availability": "https://schema.org/InStock",
  "shippingDetails": {
    "deliveryTime": {
      "handlingTime": { "@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY" },
      "transitTime":  { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 7, "unitCode": "DAY" }
    }
  }
}
```



after


```
"mainEntityOfPage": { "@type": "WebPage" },
"offers": {
  "availability": "https://schema.org/InStock",
 
}
```
shouldnt have   // "shippingDetails": REMOVED - shoule be 

before:


```
// Dyson V8 Cyclone Cordless Vacuum — SKU 50096116
"mainEntityOfPage": { "@type": "WebPage" },
"offers": {
  "availability": "https://schema.org/InStock",
  "shippingDetails": {
    "deliveryTime": {
      "handlingTime": { "@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY" },
      "transitTime":  { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 7, "unitCode": "DAY" }
    }
  }
}
```



after


```
"mainEntityOfPage": { "@type": "WebPage" },
"offers": {
  "availability": "https://schema.org/InStock",
 
}
```

### Message 36 — 2026-04-22T05:49

eh keep the //removed lines but make them more obvious, perhaps a red highliught
eh keep the //removed lines but make them more obvious, perhaps a red highliught

### Message 37 — 2026-04-22T05:51

highlight on changes like itempage? thoughts?
highlight on changes like itempage? thoughts?

### Message 38 — 2026-04-22T05:53

sure
sure

### Message 39 — 2026-04-22T05:54

beaitiful, but doont limit it to the length of others , in not avaliuable it goes yellow on discontinued until ued", as thats the negth of the other 2
beaitiful, but doont limit it to the length of others , in not avaliuable it goes yellow on discontinued until ued", as thats the negth of the other 2

### Message 40 — 2026-04-22T05:57

great, now help me update the MD:

TGG Product Schema: Dynamic Lifecycle / Product State Responses
We want to update the Product JSON-LD Schema block on all TGGs PDPs so that availability, shippingDetails, handlingTime, and transitTime values reflect each product's live purchase state and lifecycle — rather than the current hardcoded values.
Global Change (apply to all PDPs regardless of state)
In mainEntityOfPage, change @type from "WebPage" to "ItemPage".
Justification:
ItemPage is defined by https://schema.org/ItemPage  as "a page devoted to a single item, such as a particular product or hotel." 
It is a subtype of WebPage, so it is strictly more specific and semantically accurate for our PDPs
Data Sources
Field
Source
How to access
tgg.purchase_state
Shopify Metafield
product.metafields.tgg.purchase_state
tgg.product_life_cycle
Shopify Metafield
product.metafields.tgg.product_life_cycle
tgg.product_state_message
Shopify Metafield
product.metafields.tgg.product_state_message
Lowest Lead Time (integer)
Shopify Metafield
product.metafields.tgg.web_ready_rule_checks → parse JSON → extract lowestLeadTime
Pre-order reservation date
Shopify Metafield
product.metafields.tgg.pre_order_date — when customers can first reserve
Product release date
Shopify Metafield
product.metafields.tgg.release_date — when product releases to everyone; used to calculate handling days
Decision Order
Read fields in this order:
tgg.purchase_state
tgg.product_life_cycle
tgg.product_state_message (only f

[truncated — see full transcript]

### Message 41 — 2026-04-22T06:03

shippingDetailsYes — include block < why is there any question if it would be included? is this needeD? 

if 

REMOVE ENTIRELY — remove `availability` and `shippingDetails`

Woa only coming soon loses full offer block, others like unclassified or agency-* lose specific parts like availability or shipping details? also wheres before after?
shippingDetailsYes — include block < why is there any question if it would be included? is this needeD? 

if 

REMOVE ENTIRELY — remove `availability` and `shippingDetails`

Woa only coming soon loses full offer block, others like unclassified or agency-* lose specific parts like availability or shipping details? also wheres before after?

### Message 42 — 2026-04-22T06:03

apply this to the matrix tool and the jira.
apply this to the matrix tool and the jira.

### Message 43 — 2026-04-22T06:07

what other potential mistakes have you done? look over it? flag first, await approval.
what other potential mistakes have you done? look over it? flag first, await approval.

### Message 44 — 2026-04-22T06:08

also since the jira has 

Global Change (apply to all PDPs regardless of state)
In `mainEntityOfPage`, change `@type` from `"WebPage"` to `"ItemPage"`.
Justification: `ItemPage` is defined by schema.org as "a page devoted to a single item, such as a particular product or hotel." It is a subtype of `WebPage`, so it is strictly more specific and semantically accurate for PDPs.

we shouldnt keep rehashing that at all levels, do one beore after under that text, then remove from all others.
also since the jira has 

Global Change (apply to all PDPs regardless of state)
In `mainEntityOfPage`, change `@type` from `"WebPage"` to `"ItemPage"`.
Justification: `ItemPage` is defined by schema.org as "a page devoted to a single item, such as a particular product or hotel." It is a subtype of `WebPage`, so it is strictly more specific and semantically accurate for PDPs.

we shouldnt keep rehashing that at all levels, do one beore after under that text, then remove from all others.

### Message 45 — 2026-04-22T06:18

1. correct, remove from jira and matrix app. 
2. correct, remove from jira, keep in matrix app as theres no "global" change communicated there
3. should remove what i said, availability, shipping details, not full offer block, only coming soon loses offer block. BTW if sold by someone else, remove "seller" too. 
4. i want the before after in the jira ticket, like you have:
`**Before**`
````json`
`"mainEntityOfPage": { "@type": "WebPage" },`
`"offers": {`
`  "availability": "https://schema.org/InStock",`
`  "shippingDetails": {`
`    "deliveryTime": {`
`      "handlingTime": { "minValue": 0, "maxValue": 1, "unitCode": "DAY" },`
`      "transitTime":  { "minValue": 1, "maxValue": 7, "unitCode": "DAY" }`
`    }`
`  }`
`}`
`````
` `
`**After**`
````json`
`"mainEntityOfPage": { "@type": "ItemPage" },`
`"offers": {`
`  "availability": "https://schema.org/PreOrder",`
`  "availabilityStarts": "{{ tgg.pre_order_date }}",`
`  "shippingDetails": {`
`    "@type": "OfferShippingDetails",`
`    "deliveryTime": {`
`      "@type": "ShippingDeliveryTime",`
`      "handlingTime": { "@type": "QuantitativeValue", "minValue": {{ days(tgg.release_date - today) }}, "maxValue": {{ days(tgg.release_date - today) }}, "unitCode": "DAY" },`
`      "transitTime":  { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 1, "unitCode": "DAY" }`
`    }`
`  }`
`}`
`````

1. yes, remove it 
2. just say that product schema should not render at all if these are met.
3. `availableAtOrFrom` still in the JSON c

[truncated — see full transcript]

### Message 46 — 2026-04-22T06:20

the dyson v8 comments arent needed, it should just be a filler example when doing before after so its not just ... as it was before, no need to mention it, comment it, include it in any way, as long as its clear its an example
the dyson v8 comments arent needed, it should just be a filler example when doing before after so its not just ... as it was before, no need to mention it, comment it, include it in any way, as long as its clear its an example

### Message 47 — 2026-04-22T06:21

alsoo in the app, Decision Inputs
tgg.purchase_state
ADD TO CARTproduct.metafields.tgg.purchase_state
tgg.product_life_cycle
PARCELISEDproduct.metafields.tgg.product_life_cycle
tgg.product_state_message
IS_PO-Y or IS_PO-Nproduct.metafields.tgg.product_state_message 

decision inputs the labels go over the cell into the next column, fix that
alsoo in the app, Decision Inputs
tgg.purchase_state
ADD TO CARTproduct.metafields.tgg.purchase_state
tgg.product_life_cycle
PARCELISEDproduct.metafields.tgg.product_life_cycle
tgg.product_state_message
IS_PO-Y or IS_PO-Nproduct.metafields.tgg.product_state_message 

decision inputs the labels go over the cell into the next column, fix that

### Message 48 — 2026-04-22T06:23

make the coloour highlight go the full length, not just on discontinued. 

youo fucked up and added 0 / 1 in on transit? 

Yoou didnt give me Jira? i need you to reprocess the goal, task, constraints, all feedback, create a workorder for yoourself, checklist, and run through it all recursively until happy, then present to me.
make the coloour highlight go the full length, not just on discontinued. 

youo fucked up and added 0 / 1 in on transit? 

Yoou didnt give me Jira? i need you to reprocess the goal, task, constraints, all feedback, create a workorder for yoourself, checklist, and run through it all recursively until happy, then present to me.

### Message 49 — 2026-04-22T06:34

the highglight isnt working also look at the column width of decition inputs..
the highglight isnt working also look at the column width of decition inputs..

### Message 50 — 2026-04-22T06:44

ok rerun the full recursive looped check
ok rerun the full recursive looped check

### Message 51 — 2026-04-22T06:52

can you write somethign to go under scenarios nothing the addition of quantitative value to the after and why
can you write somethign to go under scenarios nothing the addition of quantitative value to the after and why

### Message 52 — 2026-04-22T06:53

shorter
shorter

### Message 53 — 2026-04-22T06:54

Note: current schemas shippingxxx misses "quantitatvie" which can xxx, add in qith deployment of new values
Note: current schemas shippingxxx misses "quantitatvie" which can xxx, add in qith deployment of new values

### Message 54 — 2026-04-22T06:59

how many unique if this then that conditions will the dev need to code?
how many unique if this then that conditions will the dev need to code?

### Message 55 — 2026-04-22T07:04

summarise it into a very brief wording:

We wanting to update the Product JSON-LD block on all TGG PDPs so that availability, shippingDetails, handlingTime, and transitTime reflect each product's live purchase state and lifecycle - rather than the current hardcoded values.
 This requires some conditional logic applied based oon shopify metafields, as well as some minor live calculation.
summarise it into a very brief wording:

We wanting to update the Product JSON-LD block on all TGG PDPs so that availability, shippingDetails, handlingTime, and transitTime reflect each product's live purchase state and lifecycle - rather than the current hardcoded values.
 This requires some conditional logic applied based oon shopify metafields, as well as some minor live calculation.

### Message 56 — 2026-04-22T07:04

can we create an if this then that flow map?
can we create an if this then that flow map?

### Message 57 — 2026-04-22T07:04

oon a oonline map rendering tool
oon a oonline map rendering tool

### Message 58 — 2026-04-22T07:05

where is the data and what tool
where is the data and what tool

### Message 59 — 2026-04-22T07:05

no, you map it into a tool that i can paste and send as a link
no, you map it into a tool that i can paste and send as a link

### Message 60 — 2026-04-22T07:06

whatever doesnt need an accoount.
whatever doesnt need an accoount.

### Message 61 — 2026-04-22T07:07

or, create the visual yourself, add it to a packet - export our entire matrix tool + this visual (as its own tab of the tool) with a choice to show the map or the matrix, as a file zip i can download and upload to github to get pulled into Streamlit
or, create the visual yourself, add it to a packet - export our entire matrix tool + this visual (as its own tab of the tool) with a choice to show the map or the matrix, as a file zip i can download and upload to github to get pulled into Streamlit

### Message 62 — 2026-04-22T07:15

that isnt a flow? like this, but much cleaner looking:
that isnt a flow? like this, but much cleaner looking:

### Message 63 — 2026-04-22T07:24

moore separation, more spacing, clickable cards at the end to open the same drawer as on matrix
moore separation, more spacing, clickable cards at the end to open the same drawer as on matrix

### Message 64 — 2026-04-22T07:30

show me what file to change and the full copy pasted change too make the decision flow the defult tab
show me what file to change and the full copy pasted change too make the decision flow the defult tab

### Message 65 — 2026-04-22T07:31

also make the css consistent, font, fix the whitespace down here, and the scrollbar being not at the bottom of boxes.
also make the css consistent, font, fix the whitespace down here, and the scrollbar being not at the bottom of boxes.

### Message 66 — 2026-04-22T07:37

not dynamic? cant handle different screens?
not dynamic? cant handle different screens?

### Message 67 — 2026-04-22T07:37

also shoulduse real logohttps://en.wikipedia.org/wiki/The_Good_Guys_%28Australian_company%29
also shoulduse real logohttps://en.wikipedia.org/wiki/The_Good_Guys_%28Australian_company%29

### Message 68 — 2026-04-22T07:38

size on both matrix and floow
size on both matrix and floow

### Message 69 — 2026-04-22T07:46

WAAAY to big? goo back to the other logic - its noto about size its about width and height? no size of input or design should change?
WAAAY to big? goo back to the other logic - its noto about size its about width and height? no size of input or design should change?

### Message 70 — 2026-04-22T07:50

how do i remove the logo entirely
how do i remove the logo entirely

### Message 71 — 2026-04-22T07:51

how to make it so big it matches its blue coloured box
how to make it so big it matches its blue coloured box

### Message 72 — 2026-04-22T07:53

doesnt look good it is 100% full screen!
doesnt look good it is 100% full screen!

### Message 73 — 2026-04-22T07:53

give me back full replace
give me back full replace

### Message 74 — 2026-04-22T07:53

full html file
full html file

### Message 75 — 2026-04-22T07:54

undo the logoo size back to what it was use this url:

https://upload.wikimedia.org/wikipedia/commons/3/3b/The_Good_Guys_Logo.png
undo the logoo size back to what it was use this url:

https://upload.wikimedia.org/wikipedia/commons/3/3b/The_Good_Guys_Logo.png
