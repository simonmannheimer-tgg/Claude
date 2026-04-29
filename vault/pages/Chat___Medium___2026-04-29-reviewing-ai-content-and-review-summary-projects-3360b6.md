---
title: Reviewing AI content and review summary projects (medium)
parent: Chat/Light/2026-04-29-reviewing-ai-content-and-review-summary-projects-3360b6
uuid: 3360b620-171d-4c36-9df6-2e3a72baef27
---

#chat/medium #project/main #status/active

# Reviewing AI content and review summary projects — Key User Messages

→ Light view: [[Chat/Light/2026-04-29-reviewing-ai-content-and-review-summary-projects-3360b6]]
→ Full transcript: [[Chat/Full/2026-04-29-reviewing-ai-content-and-review-summary-projects-3360b6]]

**Total user messages:** 62

---

### Message 1 — 2026-04-28T04:01

I need to review two new projects - one is to add ai content summaries (bullets etc.) one is to add ai summary to reviews - need help reviewing for JS and schema

AI eCommerce content (overview): https://01kq6ab9ca2aaaenx1tzksz8t8-da87140d0aabd640f914.myshopify.dev/tst-logitech-m235-wireless-mo…
AI Review Summaries: https://01kpysmcs45fvx4vhf2qk1k7vx-da87140d0aabd640f914.myshopify.dev/tst-roborock-updated-qrevo-ed…

also pasted some context - happy to be overruled
I need to review two new projects - one is to add ai content summaries (bullets etc.) one is to add ai summary to reviews - need help reviewing for JS and schema

AI eCommerce content (overview): https://01kq6ab9ca2aaaenx1tzksz8t8-da87140d0aabd640f914.myshopify.dev/tst-logitech-m235-wireless-mo…
AI Review Summaries: https://01kpysmcs45fvx4vhf2qk1k7vx-da87140d0aabd640f914.myshopify.dev/tst-roborock-updated-qrevo-ed…

also pasted some context - happy to be overruled

### Message 2 — 2026-04-28T04:08

lets start over - first off, lets only talk about the additions of ai summary content and review summary - it should be checked as dom, schema, HAR file, source code - check against AI / crawler (google) visisbility and schema rendering + schema correctness.

Don't bring in anything new, such as the haspart, graph etc. thats from a tech item roadmap which isnt relevant here. tell me more about things like react tree and whats happening. break down each file and what it is, what it shows, summarise nicely for me
lets start over - first off, lets only talk about the additions of ai summary content and review summary - it should be checked as dom, schema, HAR file, source code - check against AI / crawler (google) visisbility and schema rendering + schema correctness.

Don't bring in anything new, such as the haspart, graph etc. thats from a tech item roadmap which isnt relevant here. tell me more about things like react tree and whats happening. break down each file and what it is, what it shows, summarise nicely for me

### Message 3 — 2026-04-28T04:11

need clearer language. SSR'd - does it mean its ai and crawler friendly? should things be in source code?
need clearer language. SSR'd - does it mean its ai and crawler friendly? should things be in source code?

### Message 4 — 2026-04-28T04:14

ok, just re-do it as a docx in plan style, no fancy AI stuff - map what the project is as header, the URL for the preview, then section by section and what type of file was used "rendered dom" or "source code" or "HAR file of full page reload with all accordions opened" etc.
ok, just re-do it as a docx in plan style, no fancy AI stuff - map what the project is as header, the URL for the preview, then section by section and what type of file was used "rendered dom" or "source code" or "HAR file of full page reload with all accordions opened" etc.

### Message 5 — 2026-04-28T04:22

can you follow my format more?


```
**AI Feature Review:** eCommerce Summary & Review Summary

This is a review of two AI content features currently in development on TGG staging. 

# **Project 1:** AI Product Summary

**Preview URL:** [https://01kq6ab9ca2aaaenx1tzksz8t8-da87140d0aabd640f914.myshopify.dev/tst-logitech-m235-wireless-mouse-red-910-003412](https://01kq6ab9ca2aaaenx1tzksz8t8-da87140d0aabd640f914.myshopify.dev/tst-logitech-m235-wireless-mouse-red-910-003412) 

**Product:** Logitech M235 Wireless Mouse (Red)

* Adds an AI-generated content panel to the product page.   
* When expanded, it shows a plain-language product summary and use case categories, target user profiles etc.

##  **Checks:**

## ***Source Code*** 

* The content is in the HTML but the accordion starts collapsed.  
* All AI content is present in the server-rendered HTML.   
* The panel and its contents exist as real DOM elements in the source.   
* Google and AI crawlers can read the content without needing to run JavaScript.

**Confirmed present in source:**

1. *What it is paragraph (the aiSummary text)*  
2. *Primary Use Case*  
3. *Ideal Environment*  
4. *Workspaces*  
5. *Target User Profile*  
6. *Positioning Tier: Entry-level*  
7. *Key Trade-Off*  
8. *Universal Compatibility Score*  
9. *Work-from-Home Suitability*  
10. *Student Suitability*  
11. *Durability Rating*  
12. *Feature Benefits*
```
can you follow my format more?


```
**AI Feature Review:** eCommerce Summary & Review Summ

[truncated — see full transcript]

### Message 6 — 2026-04-28T04:27

also check over these - ensure fixes align

https://tgg-au.atlassian.net/browse/RENO-3696

https://tgg-au.atlassian.net/browse/RENO-3510
also check over these - ensure fixes align

https://tgg-au.atlassian.net/browse/RENO-3696

https://tgg-au.atlassian.net/browse/RENO-3510

### Message 7 — 2026-04-28T04:28

before recommendations - do full research into best practice for AI visibility and [schema.org](http://schema.org) / recognised structured data
before recommendations - do full research into best practice for AI visibility and [schema.org](http://schema.org) / recognised structured data

### Message 8 — 2026-04-28T04:46

you went against my format? i pasted my MD for you
you went against my format? i pasted my MD for you

### Message 9 — 2026-04-28T04:47

remove research - you are just to use it in recommendatins, stated as fact not with lots of research proof - assume high understanding of coding - JIRA only supplied for context so you can better map our recommendations (as they
remove research - you are just to use it in recommendatins, stated as fact not with lots of research proof - assume high understanding of coding - JIRA only supplied for context so you can better map our recommendations (as they

### Message 10 — 2026-04-28T04:52

i literally gave you: * The content is in the HTML but the accordion starts collapsed.  
* All AI content is present in the server-rendered HTML.   
* The panel and its contents exist as real DOM elements in the source.   
* Google and AI crawlers can read the content without needing to run JavaScript.



and you still did this?
i literally gave you: * The content is in the HTML but the accordion starts collapsed.  
* All AI content is present in the server-rendered HTML.   
* The panel and its contents exist as real DOM elements in the source.   
* Google and AI crawlers can read the content without needing to run JavaScript.



and you still did this?

### Message 11 — 2026-04-28T04:53

need you to also map out the ID and hasparts that will be used for the new parts of the schema
need you to also map out the ID and hasparts that will be used for the new parts of the schema

### Message 12 — 2026-04-28T04:53

remove file reference
remove file reference

### Message 13 — 2026-04-28T05:11

only keep whats needed to show audit of the projects against assumptions, goals and requirements - remove fluff
only keep whats needed to show audit of the projects against assumptions, goals and requirements - remove fluff

### Message 14 — 2026-04-28T05:11

write as jira ticket comments
write as jira ticket comments

### Message 15 — 2026-04-28T05:23

well, the classy schema and dom mthml shows current schema - the new things need to be added into it.
well, the classy schema and dom mthml shows current schema - the new things need to be added into it.

### Message 16 — 2026-04-28T05:43

include test notes, then fixes needed as summary, then fix ecamples.
include test notes, then fixes needed as summary, then fix ecamples.

### Message 17 — 2026-04-28T06:21

need cited official source for: Google may weight collapsed content lower
need cited official source for: Google may weight collapsed content lower

### Message 18 — 2026-04-28T06:22

link
link

### Message 19 — 2026-04-28T06:23

link to that section
link to that section

### Message 20 — 2026-04-28T06:25

I need understanding of the current schema load (is there any) and the proposed (Enriched At etc) - Also prefer this format   

## **Test Notes**

Reviewed against source code, rendered DOM, and HAR (network graph recorded with full page reload + accordions opened).

-   All AI content (What it is, Use Case, Environment… etc.) is server-rendered. Googlebot and AI crawlers read it without executing JavaScript.  
    
-   Content is not fetched client-side. Arrives bundled in the React hydration payload on the initial response. No separate metafield calls after load.  
    
-   The accordion starts collapsed but is visible in HTML - However note Google may weight collapsed content lower than content visible on load - but should be resolved if Phase 2 goes ahead (content moved outside of accordion).  
    
-   The AI content has no JSON-LD representation. The Product block contains name, description, brand, sku, gtin, image, offers, AggregateRating, and reviews. The aiSummary text and all attribute data are DOM-only.
    

##   
**Fixes Needed**

also no emdashed - EVER. stop using them, memorise that. 
I need understanding of the current schema load (is there any) and the proposed (Enriched At etc) - Also prefer this format   

## **Test Notes**

Reviewed against source code, rendered DOM, and HAR (network graph recorded with full page reload + accordions opened).

-   All AI content (What it is, Use Case, Environment… etc.) is server-rendered. Googlebot and AI crawlers read it

[truncated — see full transcript]

### Message 21 — 2026-04-28T07:20

I want you to go through and rewrite it a bit for me so it's better. I would like you to...
I want you to go through and rewrite it a bit for me so it's better. I would like you to...

### Message 22 — 2026-04-28T07:21

You need to go to... you need to go and look at all of the checks we've done, all the files, the source, blah blah blah, and compare that to how it affects the AI crawlers and even crawlers and if it doesn't, you're gonna need to include it. For example, the React, something something. I don't know if that's needed or if it's enough to say that it's not in this email. Or schema. I need you to tell me all this can only include the ad. Basically, it's already there, and if not, the AI element adding. For example, the
You need to go to... you need to go and look at all of the checks we've done, all the files, the source, blah blah blah, and compare that to how it affects the AI crawlers and even crawlers and if it doesn't, you're gonna need to include it. For example, the React, something something. I don't know if that's needed or if it's enough to say that it's not in this email. Or schema. I need you to tell me all this can only include the ad. Basically, it's already there, and if not, the AI element adding. For example, the

### Message 23 — 2026-04-28T07:21

Hey,
Hey,

### Message 24 — 2026-04-28T07:21

Go
Go

### Message 25 — 2026-04-28T07:24

Jira tickets no? What happened to our established format?
Jira tickets no? What happened to our established format?

### Message 26 — 2026-04-28T07:26

How could we make better use of the things we have access to like taxonomy?
How could we make better use of the things we have access to like taxonomy?

### Message 27 — 2026-04-28T07:28

Simplify your justifications and what you want to do / why outside the jira add if I approve
Simplify your justifications and what you want to do / why outside the jira add if I approve

### Message 28 — 2026-04-28T07:29

Is this all or either or? What are you suggesting and why?
Is this all or either or? What are you suggesting and why?

### Message 29 — 2026-04-28T07:30

Show examples per
Show examples per

### Message 30 — 2026-04-28T07:31

We already have type product and category?
We already have type product and category?

### Message 31 — 2026-04-28T07:31

Why use shopify taxonomy and not our?
Why use shopify taxonomy and not our?

### Message 32 — 2026-04-28T07:32

Wtf that makes no sense
Wtf that makes no sense

### Message 33 — 2026-04-28T07:32

But I’m asking about the taxonomy?
But I’m asking about the taxonomy?

### Message 34 — 2026-04-28T07:33

So what’s your point then?
So what’s your point then?

### Message 35 — 2026-04-28T07:34

I asked what from the example schema shared by Alex could we (should we) add?
I asked what from the example schema shared by Alex could we (should we) add?

### Message 36 — 2026-04-28T07:34

It was a paste I asked your thoughts if it’s
It was a paste I asked your thoughts if it’s

### Message 37 — 2026-04-28T07:37

Review this entire conversation- I need you to map the task, all references, files, their contents (with actual content) the findings the outcome / meaning, how it relates to the live jira dev stuff and how my audit and recommendations should be formatted. 

Goal: confirm that the planned AI optimisations and review stuff will render well, be helpful, and have schema and any other info required (semantic HTML) all available information that will be generated should be leveraged if possible 

Output should be a summary of what’s been checked, outcome, recommendations with implementation examples
Review this entire conversation- I need you to map the task, all references, files, their contents (with actual content) the findings the outcome / meaning, how it relates to the live jira dev stuff and how my audit and recommendations should be formatted. 

Goal: confirm that the planned AI optimisations and review stuff will render well, be helpful, and have schema and any other info required (semantic HTML) all available information that will be generated should be leveraged if possible 

Output should be a summary of what’s been checked, outcome, recommendations with implementation examples

### Message 38 — 2026-04-28T08:00

Run concepts by me,  with examples if approved we add to final JIRA
Run concepts by me,  with examples if approved we add to final JIRA

### Message 39 — 2026-04-29T03:53

ok show me examples of how the code would look before after
ok show me examples of how the code would look before after

### Message 40 — 2026-04-29T03:54

css selector? what is that for?
css selector? what is that for?

### Message 41 — 2026-04-29T04:39

need help to answer some of peters q's:



so for the above, there's four issues that will make it invalid or non-functional as SEO [schema.org](http://schema.org) markup:

1. `enrichedAt` isn't a [schema.org](http://schema.org) property. Crawlers will just ignore it.  
2. `aiSummary` same thing, not a real property.  
3. `shopify taxonomy` has a space in the key and is sitting inside the [schema.org](http://schema.org) object. Those are two completely unrelated data systems  
4. `additionalProperty` values are arrays, but `PropertyValue.value` needs a single value, string, number, or boolean.
need help to answer some of peters q's:



so for the above, there's four issues that will make it invalid or non-functional as SEO [schema.org](http://schema.org) markup:

1. `enrichedAt` isn't a [schema.org](http://schema.org) property. Crawlers will just ignore it.  
2. `aiSummary` same thing, not a real property.  
3. `shopify taxonomy` has a space in the key and is sitting inside the [schema.org](http://schema.org) object. Those are two completely unrelated data systems  
4. `additionalProperty` values are arrays, but `PropertyValue.value` needs a single value, string, number, or boolean.

### Message 42 — 2026-04-29T04:43

As i said, the issue isn't the data, more the format! issues are with the current metafield Json not being the format we need for [Schema.org](http://Schema.org) recognition:
 
1. enrichedAtNot a [schema.org](http://schema.org) property. Crawlers will ignore it completely. The correct field is `dateModified`, which is a standard [schema.org](http://schema.org) Thing property and does the same job.
 
2. aiSummarySame issue. Not recognised by [schema.org](http://schema.org). The correct mapping is `disambiguatingDescription`, which is a defined [schema.org](http://schema.org) property on the Product type specifically for a short description that distinguishes the product from similar items. Same content, correct field name.
 
3. shopify taxonomy blockTwo problems. The key has a space in it (`"shopify taxonomy"`) which makes it invalid JSON-LD. More importantly, this is TGG/Shopify internal data sitting inside a [schema.org](http://schema.org) object. [Schema.org](http://Schema.org) crawlers will see an unrecognised property with an invalid key and ignore the whole block. It needs to be moved to a separate `<script type="application/json">` block entirely. It has no place in the ld+json block.
 
4. additionalProperty values as arrays`PropertyValue.value` in [schema.org](http://schema.org) only accepts a single value: a string, number, or boolean. Arrays are invalid. The fix is to join the array values into a semicolon-separated string. So `["Home Espresso", "Manual Coffee Brewin

[truncated — see full transcript]

### Message 43 — 2026-04-29T04:44

you changed too much i didnt ask you to change the intro?
you changed too much i didnt ask you to change the intro?

### Message 44 — 2026-04-29T04:46

was this 100% on point then
was this 100% on point then

### Message 45 — 2026-04-29T04:46

can you redo it? same format as the photo
can you redo it? same format as the photo

### Message 46 — 2026-04-29T04:49

can you change it to : instead of . for emdash? why emdash an issue?
can you change it to : instead of . for emdash? why emdash an issue?

### Message 47 — 2026-04-29T04:50

redo both the example schema + changes list
redo both the example schema + changes list

### Message 48 — 2026-04-29T04:58

you are only to change things in product schema to match the metafield - nothing else
you are only to change things in product schema to match the metafield - nothing else

### Message 49 — 2026-04-29T05:21

why is the shopify taxonomy there when its not a schema.org? whouldnt it be added into the pdp schema?
why is the shopify taxonomy there when its not a schema.org? whouldnt it be added into the pdp schema?

### Message 50 — 2026-04-29T05:22

is there a way to leverage everything in the metafield in a way that benefits us?
is there a way to leverage everything in the metafield in a way that benefits us?

### Message 51 — 2026-04-29T05:27

redo the example json and changed list
redo the example json and changed list

### Message 52 — 2026-04-29T05:28

why?

* Score values: em dashes replaced with `:`
*
why?

* Score values: em dashes replaced with `:`
*

### Message 53 — 2026-04-29T05:28

if not in metafield we shouldnt need it?
if not in metafield we shouldnt need it?

### Message 54 — 2026-04-29T05:28

no you added it for a reason with json rendering - you just didnt explain
no you added it for a reason with json rendering - you just didnt explain

### Message 55 — 2026-04-29T05:29

rewrite that bullet, remove keywords, redo example
rewrite that bullet, remove keywords, redo example

### Message 56 — 2026-04-29T05:31

wrap this in tags so i can test them side by side in rich text tester:

{  "@context": "https://schema.org/["](https://schema.org/%22),  "@type": "Product",  "enrichedAt": "2026-04-20T06:37:54.378232+00:00",  "shopify taxonomy": {    "coffee machine": {      "id": ["ap-3-1"],      "fields": [        "Daily Usage Volume",        "Skill Level Required",        "Maintenance Complexity",        "Milk Capability Type",        "Entertaining Suitability"      ]    }  },  "name": "Breville The Barista Espresso Coffee Machine - the good guys test16",  "brand": {    "@type": "Brand",    "name": "Breville"  },  "category": "Coffee Machine",  "aiSummary": "The Breville The Barista Espresso Coffee Machine is a versatile, semi-automatic espresso maker with a built-in conical burr grinder, perfect for coffee lovers who want to craft café-style drinks at home. It suits those who appreciate hands-on control and customisation, offering rich espresso and silky milk texturing. While it excels in quality and value, it requires regular cleaning and a learning curve for beginners.",  "description": "The Breville The Barista Espresso Coffee Machine delivers café-quality espresso at home with integrated grinder and manual controls, ideal for coffee enthusiasts seeking hands-on brewing.",  "additionalProperty": [    {      "name": "Primary Use Case",      "value": [        "Home Espresso",        "Manual Coffee Brewing",        "Milk-Based Drinks"      ]    },    {      "name": "Ideal Environment",   

[truncated — see full transcript]

### Message 57 — 2026-04-29T05:32

in your changed version, it causes this:
in your changed version, it causes this:

### Message 58 — 2026-04-29T05:32

merge it
merge it

### Message 59 — 2026-04-29T05:39

ensure the same offer is here:

<script type="application/ld+json">
{  "@context": "https://schema.org/",  "@type": "Product",  "enrichedAt": "2026-04-20T06:37:54.378232+00:00",  "shopify taxonomy": {    "coffee machine": {      "id": ["ap-3-1"],      "fields": [        "Daily Usage Volume",        "Skill Level Required",        "Maintenance Complexity",        "Milk Capability Type",        "Entertaining Suitability"      ]    }  },  "name": "Breville The Barista Espresso Coffee Machine - the good guys test16",  "brand": {    "@type": "Brand",    "name": "Breville"  },  "category": "Coffee Machine",  "aiSummary": "The Breville The Barista Espresso Coffee Machine is a versatile, semi-automatic espresso maker with a built-in conical burr grinder, perfect for coffee lovers who want to craft café-style drinks at home. It suits those who appreciate hands-on control and customisation, offering rich espresso and silky milk texturing. While it excels in quality and value, it requires regular cleaning and a learning curve for beginners.",  "description": "The Breville The Barista Espresso Coffee Machine delivers café-quality espresso at home with integrated grinder and manual controls, ideal for coffee enthusiasts seeking hands-on brewing.",  "additionalProperty": [    {      "name": "Primary Use Case",      "value": [        "Home Espresso",        "Manual Coffee Brewing",        "Milk-Based Drinks"      ]    },    {      "name": "Ideal Environment",      "value": [        "Home Kit

[truncated — see full transcript]

### Message 60 — 2026-04-29T06:14

so, the thought is the changes add onto existing schema, so there will be an offer, i want you to simulate what it would look like if we added using the wrong metafield stuff rather than correcting it
so, the thought is the changes add onto existing schema, so there will be an offer, i want you to simulate what it would look like if we added using the wrong metafield stuff rather than correcting it

### Message 61 — 2026-04-29T06:16

it should be same as <script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Breville The Barista Espresso Coffee Machine",
  "dateModified": "2026-04-20T06:37:54.378232+00:00",
  "description": "The Breville The Barista Espresso Coffee Machine delivers café-quality espresso at home with integrated grinder and manual controls, ideal for coffee enthusiasts seeking hands-on brewing.",
  "disambiguatingDescription": "The Breville The Barista Espresso Coffee Machine is a versatile, semi-automatic espresso maker with a built-in conical burr grinder, perfect for coffee lovers who want to craft café-style drinks at home. It suits those who appreciate hands-on control and customisation, offering rich espresso and silky milk texturing. While it excels in quality and value, it requires regular cleaning and a learning curve for beginners.",
  "category": "Coffee Machine",
  "brand": {
    "@type": "Brand",
    "name": "Breville"
  },
  "sku": "50077212",
  "gtin": "097855092137",
  "model": "910-003412",
  "image": [
    "https://www.thegoodguys.com.au/..."
  ],
  "offers": {
    "@type": "Offer",
    "price": "35.00",
    "priceCurrency": "AUD",
    "availability": "https://schema.org/InStock",
    "url": "https://www.thegoodguys.com.au/...",
    "seller": {
      "@type": "Organization",
      "name": "The Good Guys"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "5",
  

[truncated — see full transcript]

### Message 62 — 2026-04-29T06:23

surely more issues? why are things like enrichedat not throwing issue?
surely more issues? why are things like enrichedat not throwing issue?
