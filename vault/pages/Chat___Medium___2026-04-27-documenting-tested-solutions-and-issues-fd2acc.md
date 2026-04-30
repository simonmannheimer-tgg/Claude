---
title: Documenting tested solutions and issues (medium)
parent: Chat/Light/2026-04-27-documenting-tested-solutions-and-issues-fd2acc
uuid: fd2accb3-83a2-42ab-a9b2-6e9218d6243c
---

#chat/medium #project/main #status/active

# Documenting tested solutions and issues — Key User Messages

→ Light view: [[Chat/Light/2026-04-27-documenting-tested-solutions-and-issues-fd2acc]]
→ Full transcript: [[Chat/Full/2026-04-27-documenting-tested-solutions-and-issues-fd2acc]]

**Total user messages:** 14

---

### Message 1 — 2026-04-27T04:23

help me respond to this with the things we've tested and what the issue is;
help me respond to this with the things we've tested and what the issue is;

### Message 2 — 2026-04-27T04:23



### Message 3 — 2026-04-27T04:26

can you also add in a second section asking about Shopping section of profound - state that Hugo took us through it during out trial and was suprised any data was showing - said we need to set up and configure this section for it to work - emphasise our ongoing work across improving Product pages and also ongoing feed optimisation woork - keen to see if shopping performance can be fully set up and benchmarked so we can see potential improvements
can you also add in a second section asking about Shopping section of profound - state that Hugo took us through it during out trial and was suprised any data was showing - said we need to set up and configure this section for it to work - emphasise our ongoing work across improving Product pages and also ongoing feed optimisation woork - keen to see if shopping performance can be fully set up and benchmarked so we can see potential improvements

### Message 4 — 2026-04-27T04:36

thats good - can you add in a note about how we were told during our evaluation period that native shopify support would come soon and as such arent keen to pay extra for nostra; see here
https://docs.tryprofound.com/agent-analytics/shopify

can you write it up in more of my TOV?

  
Hi Bipan. Lovely to e-meet you!
  
  
Looping in on the Agent Analytics issue as Pete mentioned.
Here's where we've landed after testing with our dev team ([@Jamie Quigg](mailto:jamiequigg@thegoodguys.com.au)):
  
**What we've tested:**
\- Shopify Hydrogen Trace Export configured in Azure, pointed at the Profound log drain endpoint (artemis.api.tryprofound.com/v1/logs/shopify\_hydrogen\_log\_drain) – **did not stabilise**
  
\- Switched to the non-log drain variant (/shopify\_hydrogen) – inconclusive, **no confirmed ingestion**
  
\- Tested the custom endpoint (/v1/logs/custom) – **confirmed not working**
  
\- Swapped from Logs to Traces in Azure as an alternative – **initially looked promising but no confirmed data flow followed**
  
  
**Key constraint:** 
Azure only permits one HTTP trace export at a time, which limits our ability to run parallel configurations or roll back quickly between tests.
  
**Where it sits now:**
No Profound endpoint has successfully ingested data from our Shopify Hydrogen setup. We haven't been able to confirm whether the issue is on the Azure/Hydrogen configuration side, a Profound API maturity issue (we understand the Shopify plugin is relatively new), or somethin

[truncated — see full transcript]

### Message 5 — 2026-04-27T04:40

same format as your first version if you can, just add in bolding etc as i requested
same format as your first version if you can, just add in bolding etc as i requested

### Message 6 — 2026-04-27T04:41

as rich text, like the first one
as rich text, like the first one

### Message 7 — 2026-04-27T04:51

help me with the pasted (if you agree)

  
Hi Bipan, lovely to e-meet you!
Looping in on the Agent Analytics issue as Pete mentioned.
Here's my understanding of where we've landed after testing with our dev team ([@Jamie Quigg](mailto:jamiequigg@thegoodguys.com.au)):
**What we've tested:**
-   Shopify Hydrogen Trace Export configured in Azure, pointed at the Profound log drain endpoint (artemis.api.tryprofound.com/v1/logs/shopify\_hydrogen\_log\_drain) - **did not stabilise**
    
-   Switched to the non-log drain variant (/shopify\_hydrogen) - inconclusive, **no confirmed ingestion**
    
-   Tested the custom endpoint (/v1/logs/custom) - **confirmed not working**
    
-   Swapped from Logs to Traces in Azure as an alternative - **initially looked promising but no confirmed data flow followed**
    
**Potential constraint:** Azure only permits one HTTP trace export at a time, which limits our ability to run parallel configurations or roll back quickly between tests.
**Where it sits now:**
No Profound endpoint to date has successfully ingested data from our Shopify Hydrogen setup. We haven't been able to confirm whether the issue is on the Azure/Hydrogen config side, a Profound API maturity issue, or something in between.
We've also since read through your Shopify docs and noted that Oxygen strips client IP addresses from log drains and trace exports entirely, which means even a working Hydrogen setup would give reduced classification accuracy. Is that something you see as an

[truncated — see full transcript]

### Message 8 — 2026-04-27T04:59

i didnt want you to change my wording on ip trace is this important
i didnt want you to change my wording on ip trace is this important

### Message 9 — 2026-04-27T04:59

Is that something you see as an issue for us?
Is that something you see as an issue for us?

### Message 10 — 2026-04-27T05:00

so all good to send?
so all good to send?

### Message 11 — 2026-04-27T05:01

what else was changed (you removed Is that something you see as an issue for us? and also i see "my understanding" is gone?
what else was changed (you removed Is that something you see as an issue for us? and also i see "my understanding" is gone?

### Message 12 — 2026-04-27T05:01

i want my undersatnign bck
i want my undersatnign bck

### Message 13 — 2026-04-27T05:03

why this Can you confirm the correct endpoint and API key format for our setup?
why this Can you confirm the correct endpoint and API key format for our setup?

### Message 14 — 2026-04-27T05:03

we assume we do we're follpwing their docs
we assume we do we're follpwing their docs
