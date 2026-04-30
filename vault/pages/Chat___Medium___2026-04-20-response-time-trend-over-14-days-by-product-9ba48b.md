---
title: Response time trend over 14 days by product (medium)
parent: Chat/Light/2026-04-20-response-time-trend-over-14-days-by-product-9ba48b
uuid: 9ba48b82-e7c8-40f0-bcd8-083a9edd0846
---

#chat/medium #project/main #status/completed

# Response time trend over 14 days by product — Key User Messages

→ Light view: [[Chat/Light/2026-04-20-response-time-trend-over-14-days-by-product-9ba48b]]
→ Full transcript: [[Chat/Full/2026-04-20-response-time-trend-over-14-days-by-product-9ba48b]]

**Total user messages:** 14

---

### Message 1 — 2026-04-20T00:06

help me rewrite this query:

// Response time trend 
// Chart request duration over the last 12 hours. 
// To create an alert for this query, click '+ New alert rule'
requests
| where timestamp > ago(12h) 
| summarize avgRequestDuration=avg(duration) by bin(timestamp, 10m) // use a time grain of 10 minutes
| render timechart

i want response time last 14 days

for products, so URLs like the attached - you may want to make some sort of regex handling sequential numbers and only 3 / slashes
help me rewrite this query:

// Response time trend 
// Chart request duration over the last 12 hours. 
// To create an alert for this query, click '+ New alert rule'
requests
| where timestamp > ago(12h) 
| summarize avgRequestDuration=avg(duration) by bin(timestamp, 10m) // use a time grain of 10 minutes
| render timechart

i want response time last 14 days

for products, so URLs like the attached - you may want to make some sort of regex handling sequential numbers and only 3 / slashes

### Message 2 — 2026-04-20T00:08

change this to match my new url
change this to match my new url

### Message 3 — 2026-04-20T00:09

no findings in that range
no findings in that range

### Message 4 — 2026-04-20T00:17

what does this mean?

tried to do a regex for product urls, sequential numbers, only one slash etc.
 
yeah that is UTC too
what does this mean?

tried to do a regex for product urls, sequential numbers, only one slash etc.
 
yeah that is UTC too

### Message 5 — 2026-04-20T00:21

can you create a few other regexes for pages types with large number of representations, e.g. /store/ or categories (more levels than a product, etc)
can you create a few other regexes for pages types with large number of representations, e.g. /store/ or categories (more levels than a product, etc)

### Message 6 — 2026-04-20T00:25

summarize' operator: Failed to resolve scalar expression named 'totalDuration' Request id: 144295d7-916e-4444-8106-13f1472e5508
summarize' operator: Failed to resolve scalar expression named 'totalDuration' Request id: 144295d7-916e-4444-8106-13f1472e5508

### Message 7 — 2026-04-20T00:26

any way to show each as its own colour line
any way to show each as its own colour line

### Message 8 — 2026-04-20T00:27

what about bot types like google, llms etc
what about bot types like google, llms etc

### Message 9 — 2026-04-20T00:28

'extend' operator: Failed to resolve scalar expression named 'user_Agent' Request id: 1423e1e5-10a7-4259-b1f1-1cabc0a499f8
'extend' operator: Failed to resolve scalar expression named 'user_Agent' Request id: 1423e1e5-10a7-4259-b1f1-1cabc0a499f8

### Message 10 — 2026-04-20T00:29

url success resultCode duration performanceBucket customDimensions operation_Id itemType operation_ParentId client_Type client_IP client_City client_StateOrProvince client_CountryOrRegion appId appName iKey
Key Value timestamp [UTC]	2026-04-19T23:43:54.621Z	id	e2c474d8-9c83-41b2-b742-6e11c5725d1a-1776642234621	source	13.236.87.116	name	GET /__manifest	url	https://www.thegoodguys.com.au/__manifest?paths=%2Freolink-4k-dual-lens-wireless-security-camera-plus-solar-panel-bwptdb4k10sp64%2C%2Ftp-link-2k-solar-powered-pantilt-4g-lte-security-camera-tapo-c615g-kit%2C%2Ftp-link-3k-solar-powered-pantilt-security-camera-kit-tapo-c630-kit&version=df4d3487	success	True	resultCode	200	duration	0	performanceBucket	<250ms	itemType	request	customDimensions	{"requestHeaders":"{\"accept-language\":\"en-US,en;q=0.9\",\"oxygen-buyer-city\":\"Sydney\",\"oxygen-buyer-continent\":\"OC\",\"oxygen-buyer-country\":\"AU\",\"oxygen-buyer-deployment-id\":\"4413233\",\"oxygen-buyer-region\":\"New South Wales\",\"oxygen-buyer-region-code\":\"NSW\",\"oxygen-buyer-shop-id\":\"64193888321\",\"oxygen-buyer-storefront-id\":\"1000035166\",\"oxygen-buyer-timezone\":\"Australia/Sydney\",\"referer\":\"https://www.thegoodguys.com.au/\",\"sec-ch-ua\":\"\\\"Chromium\\\";v=\\\"146\\\", \\\"Not-A.Brand\\\";v=\\\"24\\\", \\\"Avast Secure Browser\\\";v=\\\"146\\\"\",\"sec-ch-ua-mobile\":\"?0\",\"sec-ch-ua-platform\":\"\\\"Windows\\\"\",\"sec-fetch-mode\":\"cors\",\"sec-fetch-site\":\"same-origin\",\"user-agent\":\"Mozilla/

[truncated — see full transcript]

### Message 11 — 2026-04-20T00:31

06/04/2026, 00:00:00.000	Human	Store	171.1945147679325	Key Value timestamp [UTC]	2026-04-06T00:00:00Z	BotType	Human	UrlType	Store	AvgRequestDuration	171.1945147679325		06/04/2026, 00:00:00.000	Google AI	Product	490.2692307692308	06/04/2026, 00:00:00.000	Google AI	Category	621.3770491803278	06/04/2026, 00:00:00.000	Apple	Store	316.5508196721311	06/04/2026, 00:00:00.000	Apple	Category	388.05454545454546	06/04/2026, 00:00:00.000	Apple	Product	515.453744493392	06/04/2026, 00:00:00.000	Googlebot	Store	331.22127659574465	06/04/2026, 00:00:00.000	Bing	Store	366.953125	06/04/2026, 00:00:00.000	Bing	Product	590.6588898525586	06/04/2026, 00:00:00.000	Googlebot	Category	338.0252844500632	06/04/2026, 00:00:00.000	Bing	Category	466.72380619205876	06/04/2026, 00:00:00.000	Googlebot	Product	496.5496595043378
06/04/2026, 00:00:00.000	Human	Store	171.1945147679325	Key Value timestamp [UTC]	2026-04-06T00:00:00Z	BotType	Human	UrlType	Store	AvgRequestDuration	171.1945147679325		06/04/2026, 00:00:00.000	Google AI	Product	490.2692307692308	06/04/2026, 00:00:00.000	Google AI	Category	621.3770491803278	06/04/2026, 00:00:00.000	Apple	Store	316.5508196721311	06/04/2026, 00:00:00.000	Apple	Category	388.05454545454546	06/04/2026, 00:00:00.000	Apple	Product	515.453744493392	06/04/2026, 00:00:00.000	Googlebot	Store	331.22127659574465	06/04/2026, 00:00:00.000	Bing	Store	366.953125	06/04/2026, 00:00:00.000	Bing	Product	590.6588898525586	06/04/2026, 00:00:00.000	Googlebot	Category	338.0252844500632	06/04/202

[truncated — see full transcript]

### Message 12 — 2026-04-20T00:34

requests
| where timestamp > ago(14d)
| extend UserAgent = tostring(parse_json(customDimensions).requestHeaders)
| extend BotType = case(
    UserAgent contains "Googlebot", "Googlebot",
    UserAgent contains "GPTBot", "OpenAI",
    UserAgent contains "Claude-Web", "Anthropic",
    UserAgent contains "Gemini", "Google AI",
    UserAgent contains "Bingbot", "Bing",
    UserAgent contains "Applebot", "Apple",
    "Human"
)
| extend UrlType = case(
    url matches regex @"^https://www\.thegoodguys\.com\.au/stores/[a-z0-9\-]+$", "Store",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+(/[a-z0-9\-]+){1,}$", "Category",
    url matches regex @"^https://www\.thegoodguys\.com\.au/[a-z0-9\-]+$", "Product",
    "Other"
)
| where UrlType != "Other"
| summarize AvgRequestDuration = avg(duration) by bin(timestamp, 1d), BotType, UrlType
| order by timestamp asc
| render timechart

// Response time trend 
// Chart request duration over the last 12 hours. 
// To create an alert for this query, click '+ New alert rule'
requests
| where timestamp > ago(12h) 
| summarize avgRequestDuration=avg(duration) by bin(timestamp, 10m) // use a time grain of 10 minutes
| render timechart

is avg request duration the same as respojse time
requests
| where timestamp > ago(14d)
| extend UserAgent = tostring(parse_json(customDimensions).requestHeaders)
| extend BotType = case(
    UserAgent contains "Googlebot", "Googlebot",
    UserAgent contains "GPT

[truncated — see full transcript]

### Message 13 — 2026-04-20T00:34

can i do breakdown of page type by bots
can i do breakdown of page type by bots

### Message 14 — 2026-04-20T00:47

and over time?
and over time?
