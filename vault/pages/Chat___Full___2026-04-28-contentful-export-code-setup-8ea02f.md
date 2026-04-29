---
title: Contentful export code setup (full)
parent: Chat/Light/2026-04-28-contentful-export-code-setup-8ea02f
uuid: 8ea02ff8-9e99-4fc6-b430-39d7b8f688fc
---

#chat/full #project/main #status/active

# Contentful export code setup — Full Transcript

→ Light view: [[Chat/Light/2026-04-28-contentful-export-code-setup-8ea02f]]
→ Medium view: [[Chat/Medium/2026-04-28-contentful-export-code-setup-8ea02f]]

**Messages:** 4 | **Date:** 2026-04-28

---

### 1. **Human** — 2026-04-28T23:14

what chat did we set up contentful export code
what chat did we set up contentful export code

---

### 2. **Claude** — 2026-04-28T23:14

```
This block is not supported on your current device yet.
```

The deals page Contentful work (auditing and restoring missing internal link blocks across 23 /deals/ pages) is here:

https://claude.ai/chat/ef3335b2-e56c-4de1-a0b0-d51c1b639e88

That's the one with the CSV export code, encoding fixes, and the shared Contentful entry flag for /deals/kitchen and /deals/fridge-and-laundry.
The deals page Contentful work (auditing and restoring missing internal link blocks across 23 /deals/ pages) is here:

https://claude.ai/chat/ef3335b2-e56c-4de1-a0b0-d51c1b639e88

That's the one with the CSV export code, encoding fixes, and the shared Contentful entry flag for /deals/kitchen and /deals/fridge-and-laundry.

---

### 3. **Human** — 2026-04-28T23:14

no we set up code like {
  articleCollection(
    limit: 1000,
    where: { introduction_exists: true }
  ) {
    total
    items {
      sys { id }
      slug
      introduction { json }
      articleBody { json }
      linkedFrom {
        richCollectionCollection { items { sys { id } } }
        bentoGridCollection { items { sys { id } } }
      }
    }
  }
}
no we set up code like {
  articleCollection(
    limit: 1000,
    where: { introduction_exists: true }
  ) {
    total
    items {
      sys { id }
      slug
      introduction { json }
      articleBody { json }
      linkedFrom {
        richCollectionCollection { items { sys { id } } }
        bentoGridCollection { items { sys { id } } }
      }
    }
  }
}

---

### 4. **Claude** — 2026-04-28T23:14

```
This block is not supported on your current device yet.
```

Found it. Two relevant chats:

**The query build:** https://claude.ai/chat/93aa4c1d-58a0-4188-8538-abb0954e0599
Started from the FAQ query pattern, built out the `articleCollection` query with `introduction`, `linkedFrom`, and the `richCollectionCollection`/`bentoGridCollection` structure.

**Iteration with slug + body:** https://claude.ai/chat/4fb802f6-77a9-4626-83ef-a6c19586cf7d
This is where the `slug` field was added, the `body { json }` field was tried, and you hit the 796-article result. The last message was "full command" so there may be more work in that thread.
Found it. Two relevant chats:

**The query build:** https://claude.ai/chat/93aa4c1d-58a0-4188-8538-abb0954e0599
Started from the FAQ query pattern, built out the `articleCollection` query with `introduction`, `linkedFrom`, and the `richCollectionCollection`/`bentoGridCollection` structure.

**Iteration with slug + body:** https://claude.ai/chat/4fb802f6-77a9-4626-83ef-a6c19586cf7d
This is where the `slug` field was added, the `body { json }` field was tried, and you hit the 796-article result. The last message was "full command" so there may be more work in that thread.
