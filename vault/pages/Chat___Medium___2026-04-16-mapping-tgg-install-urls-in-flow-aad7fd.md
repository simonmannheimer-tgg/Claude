---
title: Mapping tgg-install URLs in flow (medium)
parent: Chat/Light/2026-04-16-mapping-tgg-install-urls-in-flow-aad7fd
uuid: aad7fd80-ef08-4a41-9908-923bc717c4c4
---

#chat/medium #project/main #status/completed

# Mapping tgg-install URLs in flow — Key User Messages

→ Light view: [[Chat/Light/2026-04-16-mapping-tgg-install-urls-in-flow-aad7fd]]
→ Full transcript: [[Chat/Full/2026-04-16-mapping-tgg-install-urls-in-flow-aad7fd]]

**Total user messages:** 7

---

### Message 1 — 2026-04-16T02:47

Need help to update this flow to map tgg-install urls correctly. attached is file of previous uploaded redirects for regerence.
Need help to update this flow to map tgg-install urls correctly. attached is file of previous uploaded redirects for regerence.

### Message 2 — 2026-04-16T02:49

Q: What's the core problem you're solving with the flow update?
A: I want to update the current flow to use my home-service urls instead of breadcrumb - read the files

Q: What is the breadcrumb metafield currently populated with for tgg-install products?
A: [No preference]
Q: What's the core problem you're solving with the flow update?
A: I want to update the current flow to use my home-service urls instead of breadcrumb - read the files

Q: What is the breadcrumb metafield currently populated with for tgg-install products?
A: [No preference]

### Message 3 — 2026-04-16T02:52

Write a super simple brief for an AI to build this flow
Write a super simple brief for an AI to build this flow

### Message 4 — 2026-04-16T02:54

It must be a simple brief to shopifys built in ai so it will make edits.

`## What the Flow Must Do`
` `
`When a product is archived (status: ACTIVE → ARCHIVED):`
` `
`1. **Check:** Does the product handle contain "tgg-install"?`
`2. **If yes:** Route to the appropriate `/home-services/*` destination based on the product handle.`
`3. **If no:** Fall back to breadcrumb metafield logic or first collection.`
`4. **Log:** Record the redirect (source, destination, date) to Google Sheets.`
`---`
` `
`## Mapping Rules`
` `
`Use these 98 explicit redirects. Route by matching the product handle (the part after `/tgg-install-`):`
` `
`| Handle (truncated) | Destination |`
`|---|---|`
`| `thermawash-air-con-service-thermawash` | `/home-services/air-conditioning-installation` |`
`| `install-receiver-with-new-ac-install-insrnewac90000` | `/home-services/air-conditioning-installation` |`
`| `fridge-water-new-connection-install-fwncinst9084` | `/home-services/freezers-and-fridges-services` |`
`| `dryer-del-install-and-removal-drinhdibidr90049` | `/home-services/laundry-installation` |`
`| `decommission-existing-receiver-dcomre90085` | `/home-services/antenna-installation` |`
`| *[70 more air-con, 13 fridge, 8 laundry, 6 root home-services]* | *[See attached CSV]* |`
` `
`**Full mapping:** See `tgg_installs_redirect_mapping.csv` (98 rows).`
` `
`---`
` `
`## Flow Structure`
` `
`````
`Trigger: Product status updated`
`  ↓`
`Check: Is product moving from ACTIVE → ARCHIVED?`
`  └─ YES → Check:

[truncated — see full transcript]

### Message 5 — 2026-04-16T02:56

be careful about "ac" other urls can contain ac without meaning "aircon" - "-ac-" is safer, review the redirect file csv i gave before, match the regex to how urls are usually setup
be careful about "ac" other urls can contain ac without meaning "aircon" - "-ac-" is safer, review the redirect file csv i gave before, match the regex to how urls are usually setup

### Message 6 — 2026-04-16T03:00

happy?
happy?

### Message 7 — 2026-04-16T03:12

its supposed to do ALL products, if ipad macbook etc use that routing, if install use install, else use normal breadcrumb
its supposed to do ALL products, if ipad macbook etc use that routing, if install use install, else use normal breadcrumb
