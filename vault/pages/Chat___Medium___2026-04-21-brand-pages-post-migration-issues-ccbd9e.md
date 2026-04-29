---
title: Brand pages post-migration issues (medium)
parent: Chat/Light/2026-04-21-brand-pages-post-migration-issues-ccbd9e
uuid: ccbd9e03-b28c-461f-8589-480d189f8e50
---

#chat/medium #project/main #status/completed

# Brand pages post-migration issues — Key User Messages

→ Light view: [[Chat/Light/2026-04-21-brand-pages-post-migration-issues-ccbd9e]]
→ Full transcript: [[Chat/Full/2026-04-21-brand-pages-post-migration-issues-ccbd9e]]

**Total user messages:** 30

---

### Message 1 — 2026-04-21T00:07

What happened post migration to our brand pages? migration end of june.
What happened post migration to our brand pages? migration end of june.

### Message 2 — 2026-04-21T00:32

two files, one is date and page, one is page and query, you need to use logic to merge and map them (it would have been to large a file to do data, page, query
two files, one is date and page, one is page and query, you need to use logic to merge and map them (it would have been to large a file to do data, page, query

### Message 3 — 2026-04-21T00:36

create a short report of what happened, remove any duplicates due to paramaters, check this export of current 301s
create a short report of what happened, remove any duplicates due to paramaters, check this export of current 301s

### Message 4 — 2026-04-21T00:39

there was not that many brand pages? you have to de-duplicate by URL, map the before URL to the after and treat as one
there was not that many brand pages? you have to de-duplicate by URL, map the before URL to the after and treat as one

### Message 5 — 2026-04-21T00:43

the redirect mappings are only in response to your comment: Redirect quality: Are 301s landing on the right targeting pages, or diffusing across the new tree?

to be analazyed by you in your migration audit
the redirect mappings are only in response to your comment: Redirect quality: Are 301s landing on the right targeting pages, or diffusing across the new tree?

to be analazyed by you in your migration audit

### Message 6 — 2026-04-21T01:00

these are our logs around redirects, so you can see pre and post migration differences
these are our logs around redirects, so you can see pre and post migration differences

### Message 7 — 2026-04-21T01:04

Is this data unbiased an not based on any other conversations we've had?
Is this data unbiased an not based on any other conversations we've had?

### Message 8 — 2026-04-21T01:10

heres better 301 request from our logs data. same unbiased format
heres better 301 request from our logs data. same unbiased format

### Message 9 — 2026-04-21T01:11

the reason why i asked about bias and other conversatoins is we are also (in another session) working on mapping brand redirects, and theres a discussion there around if /brand should go to another /brand or to a category... felt like you were intermixing the topics
the reason why i asked about bias and other conversatoins is we are also (in another session) working on mapping brand redirects, and theres a discussion there around if /brand should go to another /brand or to a category... felt like you were intermixing the topics

### Message 10 — 2026-04-21T01:19

re-frame your task and bias - you are an SEO and data analysis expert - audit the data given and without Bias present facts with proof.
re-frame your task and bias - you are an SEO and data analysis expert - audit the data given and without Bias present facts with proof.

### Message 11 — 2026-04-21T01:20

the second is the full data set, use that. it is a azure log export to show you what redirects set up and when - see this conv:
the second is the full data set, use that. it is a azure log export to show you what redirects set up and when - see this conv:

### Message 12 — 2026-04-21T01:22

that isnt the question - the azure log + shopify redirec texport shows you when redirects where set up, to what, what changed over time, themain goal is still an migraiton audit, the 301 element is just a layer.
that isnt the question - the azure log + shopify redirec texport shows you when redirects where set up, to what, what changed over time, themain goal is still an migraiton audit, the 301 element is just a layer.

### Message 13 — 2026-04-21T01:24

i thought the logs was set to start 3 months before mig?

see the latest code in the azure query creation conv?
i thought the logs was set to start 3 months before mig?

see the latest code in the azure query creation conv?

### Message 14 — 2026-04-21T01:27



### Message 15 — 2026-04-21T01:56

Go to Log Analytics and run query
requests
| where timestamp >= datetime(2024-03-30) and timestamp <= now()
| where resultCode == "301"
| extend FromPath = tostring(parse_url(url).Path)
| summarize FirstSeen = min(timestamp), LastSeen = max(timestamp), HitCount = count() by FromPath
| order by FirstSeen asc

is it still too short?

requests
| where timestamp >= datetime(2024-03-30) and timestamp <= now()
| where resultCode == "301"
| extend FromPath = tostring(parse_url(url).Path)
| summarize FirstSeen = min(timestamp), LastSeen = max(timestamp), HitCount = count() by FromPath
| order by FirstSeen asc
Go to Log Analytics and run query
requests
| where timestamp >= datetime(2024-03-30) and timestamp <= now()
| where resultCode == "301"
| extend FromPath = tostring(parse_url(url).Path)
| summarize FirstSeen = min(timestamp), LastSeen = max(timestamp), HitCount = count() by FromPath
| order by FirstSeen asc

is it still too short?

requests
| where timestamp >= datetime(2024-03-30) and timestamp <= now()
| where resultCode == "301"
| extend FromPath = tostring(parse_url(url).Path)
| summarize FirstSeen = min(timestamp), LastSeen = max(timestamp), HitCount = count() by FromPath
| order by FirstSeen asc

### Message 16 — 2026-04-21T02:13



### Message 17 — 2026-04-21T02:14

canyou write the query you need to get that? maybe simplify it as theres a 500k limit? maybe something like removing duplication
canyou write the query you need to get that? maybe simplify it as theres a 500k limit? maybe something like removing duplication

### Message 18 — 2026-04-21T02:15

option 1

A syntax error has been identified in the query. Query could not be parsed at 'date' on line [4,10] Token: date Line: 4 Position: 10 Request id: 94aa935b-cceb-4542-a02e-e10f914fa563
option 1

A syntax error has been identified in the query. Query could not be parsed at 'date' on line [4,10] Token: date Line: 4 Position: 10 Request id: 94aa935b-cceb-4542-a02e-e10f914fa563

### Message 19 — 2026-04-21T02:16

No results found from the specified time range Try __selecting another time range__
No results found from the specified time range Try __selecting another time range__

### Message 20 — 2026-04-21T02:20

same thing.
same thing.

### Message 21 — 2026-04-21T02:20

sure
sure

### Message 22 — 2026-04-21T02:23

just focus on brand page redirects, i dont think we have 32k of those? restate the purpose of the audit, the methodology, the data you have and how you want to use it
just focus on brand page redirects, i dont think we have 32k of those? restate the purpose of the audit, the methodology, the data you have and how you want to use it

### Message 23 — 2026-04-21T02:24

go ahead
go ahead

### Message 24 — 2026-04-21T02:30

0%?

first off, you have all the gsc data to audit performance and category changes and rankings, - yhou are too 301 focused atm - 301 is a side of it but not all of it
0%?

first off, you have all the gsc data to audit performance and category changes and rankings, - yhou are too 301 focused atm - 301 is a side of it but not all of it

### Message 25 — 2026-04-21T02:32

* URL expansion: 8,636 → 141,134 pages < what?
* URL expansion: 8,636 → 141,134 pages < what?

### Message 26 — 2026-04-21T02:36

you have it all i uploaded
you have it all i uploaded

### Message 27 — 2026-04-21T02:42

yes check all causes - were pages going down before migration? etc.
yes check all causes - were pages going down before migration? etc.

### Message 28 — 2026-04-21T02:44

migration was June 2025 - full audit of pre, post, why
migration was June 2025 - full audit of pre, post, why

### Message 29 — 2026-04-21T02:47

what about avg. position - could google have just started ranking urls different e.g. now brands rank for their keywords, not retailer
what about avg. position - could google have just started ranking urls different e.g. now brands rank for their keywords, not retailer

### Message 30 — 2026-04-21T02:49

301 audit
301 audit
