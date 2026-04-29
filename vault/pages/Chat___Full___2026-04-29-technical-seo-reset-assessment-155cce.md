---
title: Technical SEO reset assessment (full)
parent: Chat/Light/2026-04-29-technical-seo-reset-assessment-155cce
uuid: 155cce4b-b9c0-4738-9521-8c3b3b4738e0
---

#chat/full #project/eofy #status/completed

# Technical SEO reset assessment — Full Transcript

→ Light view: [[Chat/Light/2026-04-29-technical-seo-reset-assessment-155cce]]
→ Medium view: [[Chat/Medium/2026-04-29-technical-seo-reset-assessment-155cce]]

**Messages:** 4 | **Date:** 2026-04-29

---

### 1. **Human** — 2026-04-29T02:27

I need to do a technical seo reset against the tech roadmap and delivery - it was a lot of hours so want to understand where we are at.
I need to do a technical seo reset against the tech roadmap and delivery - it was a lot of hours so want to understand where we are at.

---

### 2. **Claude** — 2026-04-29T02:28

```
This block is not supported on your current device yet.
```

I have multiple inputs here. Let me read all of them systematically before synthesising.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good, I now have a complete picture. Here's the reset.

---

**Technical SEO: Where things actually stand**

**Hours logged vs. output**

The retainer allocated 50 hours to tech SEO across three months: 10hrs Feb (discovery), 25hrs Mar (ticket descriptions), 15hrs Apr (checks, tracking, briefing). That's the full spend.

What came out:

- **Feb.** Initial audit with 16 prioritised issues documented in the Tech Items spreadsheet. Quality is actually decent: specific fixes, code examples, schema rewrites, concrete URLs. This is usable work.
- **Mar.** Full ticket descriptions delivered. 1,027 broken breadcrumb URLs identified, 485 broken backlinks catalogued, detailed schema upgrades spec'd out (Product, Article, CollectionPage, Store, OnlineStore, homepage). The heading/H1 model-number issue is well-evidenced.
- **Apr.** Seb delivered 1,300+ mapped 404 redirect URLs (after deduplication across crawl, GSC, Ahrefs), has handled the mapping himself, and the file is Shopify-ready. He also confirmed the `/en/auonline/` robots.txt block as a backlink reclaim opportunity and agreed 410 was too aggressive for regular 404s.

**The real problem**

Very little has been implemented. You have 16 prioritised issues, a Shopify-ready redirect CSV, and detailed schema specs, but looking at what's actually been actioned:

- Shopify Flow auto-redirect (your work, not OD's)
- Internal 404 link reduction (your work)
- 410 idea raised and correctly killed

The OD deliverables are sitting as specs, not shipped changes. That's the gap. The audit is fine. The prioritisation is fine. The bottleneck is dev execution.

**What's still open and needs a decision**

The 16 tech issues break into three buckets:

*Dev tickets needed (you can't do these alone)*: robots.txt additions (Title=, krypto=, sortBy=), store pages HTML link fallback, filter `<div>` to `<aside>`, semantic heading restructure, schema upgrades (OnlineStore, ItemPage, @graph, unitCode fix), breadcrumb schema absolute URLs, paginated title tags.

*Simon-executable*: H1/model number audit, breadcrumb L2 redirects setup, 410 decision (closed), 404 redirect CSV upload to Shopify (pending Seb finalising confidence threshold review).

*In progress now*: 1,300 redirect mapping. Seb is reviewing the low-confidence matches (below ~0.92 score) before handing over the final file.

**The honest assessment**

The 50 hours produced a solid audit and actionable specs. The concern in your Slack message ("everything wrong and what to do") is partially valid, but Seb's response is also valid: metadata length and smaller BAU items were deliberately excluded as low-impact. Where the retainer fell short is that it didn't drive any dev tickets into the queue. You got a roadmap, not implementation. Whether that's the right scope for this retainer depends on whether OD has dev access, but it's worth naming: the next phase needs either OD briefing devs directly or a clear handoff process to your internal/agency dev team.

**Immediate priorities**

1. Upload Seb's 404 redirect CSV once he's done reviewing confidence scores.
2. Decide which schema upgrades go to dev first. OnlineStore on homepage and product weight unitCode fix are the easiest wins.
3. robots.txt additions (Title=, krypto=, sortBy=) are a five-minute dev change. Get them in.
4. Store page HTML link fallback is the highest structural risk item. Keep it on the radar for EOFY.
I have multiple inputs here. Let me read all of them systematically before synthesising.
Good, I now have a complete picture. Here's the reset.

---

**Technical SEO: Where things actually stand**

**Hours logged vs. output**

The retainer allocated 50 hours to tech SEO across three months: 10hrs Feb (discovery), 25hrs Mar (ticket descriptions), 15hrs Apr (checks, tracking, briefing). That's the full spend.

What came out:

- **Feb.** Initial audit with 16 prioritised issues documented in the Tech Items spreadsheet. Quality is actually decent: specific fixes, code examples, schema rewrites, concrete URLs. This is usable work.
- **Mar.** Full ticket descriptions delivered. 1,027 broken breadcrumb URLs identified, 485 broken backlinks catalogued, detailed schema upgrades spec'd out (Product, Article, CollectionPage, Store, OnlineStore, homepage). The heading/H1 model-number issue is well-evidenced.
- **Apr.** Seb delivered 1,300+ mapped 404 redirect URLs (after deduplication across crawl, GSC, Ahrefs), has handled the mapping himself, and the file is Shopify-ready. He also confirmed the `/en/auonline/` robots.txt block as a backlink reclaim opportunity and agreed 410 was too aggressive for regular 404s.

**The real problem**

Very little has been implemented. You have 16 prioritised issues, a Shopify-ready redirect CSV, and detailed schema specs, but looking at what's actually been actioned:

- Shopify Flow auto-redirect (your work, not OD's)
- Internal 404 link reduction (your work)
- 410 idea raised and correctly killed

The OD deliverables are sitting as specs, not shipped changes. That's the gap. The audit is fine. The prioritisation is fine. The bottleneck is dev execution.

**What's still open and needs a decision**

The 16 tech issues break into three buckets:

*Dev tickets needed (you can't do these alone)*: robots.txt additions (Title=, krypto=, sortBy=), store pages HTML link fallback, filter `<div>` to `<aside>`, semantic heading restructure, schema upgrades (OnlineStore, ItemPage, @graph, unitCode fix), breadcrumb schema absolute URLs, paginated title tags.

*Simon-executable*: H1/model number audit, breadcrumb L2 redirects setup, 410 decision (closed), 404 redirect CSV upload to Shopify (pending Seb finalising confidence threshold review).

*In progress now*: 1,300 redirect mapping. Seb is reviewing the low-confidence matches (below ~0.92 score) before handing over the final file.

**The honest assessment**

The 50 hours produced a solid audit and actionable specs. The concern in your Slack message ("everything wrong and what to do") is partially valid, but Seb's response is also valid: metadata length and smaller BAU items were deliberately excluded as low-impact. Where the retainer fell short is that it didn't drive any dev tickets into the queue. You got a roadmap, not implementation. Whether that's the right scope for this retainer depends on whether OD has dev access, but it's worth naming: the next phase needs either OD briefing devs directly or a clear handoff process to your internal/agency dev team.

**Immediate priorities**

1. Upload Seb's 404 redirect CSV once he's done reviewing confidence scores.
2. Decide which schema upgrades go to dev first. OnlineStore on homepage and product weight unitCode fix are the easiest wins.
3. robots.txt additions (Title=, krypto=, sortBy=) are a five-minute dev change. Get them in.
4. Store page HTML link fallback is the highest structural risk item. Keep it on the radar for EOFY.

---

### 3. **Human** — 2026-04-29T03:00

write up as a document with summary etc. and next steps
write up as a document with summary etc. and next steps

---

### 4. **Claude** — 2026-04-29T03:02

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Six sections: summary, hours and phases, what was delivered (16-issue table + phase 3 work + internal contributions), what's still open (dev tickets table, Simon actions, stakeholder decisions), assessment (what went well, where it fell short, root cause), and next steps split across immediate, EOFY, and governance.
Six sections: summary, hours and phases, what was delivered (16-issue table + phase 3 work + internal contributions), what's still open (dev tickets table, Simon actions, stakeholder decisions), assessment (what went well, where it fell short, root cause), and next steps split across immediate, EOFY, and governance.
