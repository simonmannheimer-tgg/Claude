---
title: Shopify Matrixify data export setup (medium)
parent: Chat/Light/2026-04-21-shopify-matrixify-data-export-setup-08df8f
uuid: 08df8f81-0eec-4ff7-951e-0022281729ab
---

#chat/medium #project/main #status/completed

# Shopify Matrixify data export setup — Key User Messages

→ Light view: [[Chat/Light/2026-04-21-shopify-matrixify-data-export-setup-08df8f]]
→ Full transcript: [[Chat/Full/2026-04-21-shopify-matrixify-data-export-setup-08df8f]]

**Total user messages:** 10

---

### Message 1 — 2026-04-21T00:50

any way to get date set up? shopify matrixify redirct export
any way to get date set up? shopify matrixify redirct export

### Message 2 — 2026-04-21T00:51

can you write an azure query that finds 301 responses and when first recorded from / to?
can you write an azure query that finds 301 responses and when first recorded from / to?

### Message 3 — 2026-04-21T00:54

this is the current request count:

requests
| where resultCode == "301"
| extend FromPath = tostring(parse_url(url).Path)
| summarize FirstSeen = min(timestamp), HitCount = count() by FromPath
| order by FirstSeen asc

// Request count trend 
// Chart Request count over the last day. 
// To create an alert for this query, click '+ New alert rule'
AppRequests
| summarize totalCount=sum(ItemCount) by bin(TimeGenerated, 30m), _ResourceId
| render timechart

update it with our new, make it very very long back (3 months pre june 2025 to now.)
this is the current request count:

requests
| where resultCode == "301"
| extend FromPath = tostring(parse_url(url).Path)
| summarize FirstSeen = min(timestamp), HitCount = count() by FromPath
| order by FirstSeen asc

// Request count trend 
// Chart Request count over the last day. 
// To create an alert for this query, click '+ New alert rule'
AppRequests
| summarize totalCount=sum(ItemCount) by bin(TimeGenerated, 30m), _ResourceId
| render timechart

update it with our new, make it very very long back (3 months pre june 2025 to now.)

### Message 4 — 2026-04-21T00:56

*
Save
Share
Show:1000 results
KQL mode
2
3
4
5
6
'where' operator: Failed to resolve table or column expression named 'requests' Request id: 7fbd8945-5809-418e-b10f-cba1619bf20e
*
Save
Share
Show:1000 results
KQL mode
2
3
4
5
6
'where' operator: Failed to resolve table or column expression named 'requests' Request id: 7fbd8945-5809-418e-b10f-cba1619bf20e

### Message 5 — 2026-04-21T01:05

'where' operator: Failed to resolve table or column expression named 'AppRequests' Request id: 30cd54e5-5237-41f3-a468-99ddaa39e6c5
'where' operator: Failed to resolve table or column expression named 'AppRequests' Request id: 30cd54e5-5237-41f3-a468-99ddaa39e6c5

### Message 6 — 2026-04-21T01:05

Go to Log Analytics and run query

 $table browserTimingspageViewsdependenciesrequests
Go to Log Analytics and run query

 $table browserTimingspageViewsdependenciesrequests

### Message 7 — 2026-04-21T01:26

do research into profounds agent analytics - how do they work? what do they look at?
do research into profounds agent analytics - how do they work? what do they look at?

### Message 8 — 2026-04-21T01:27

how could we build it with non-profound tools like azure?
how could we build it with non-profound tools like azure?

### Message 9 — 2026-04-21T01:28

consider screamingfrogs logfile analyzer too - where in azure can i export a log that i could then somehow analyze with llm?
consider screamingfrogs logfile analyzer too - where in azure can i export a log that i could then somehow analyze with llm?

### Message 10 — 2026-04-21T01:28

if you merged all findings from SF and profound and their data needs, what would we export and from where?
if you merged all findings from SF and profound and their data needs, what would we export and from where?
