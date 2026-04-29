---
title: Contentful export code setup (medium)
parent: Chat/Light/2026-04-28-contentful-export-code-setup-8ea02f
uuid: 8ea02ff8-9e99-4fc6-b430-39d7b8f688fc
---

#chat/medium #project/main #status/active

# Contentful export code setup — Key User Messages

→ Light view: [[Chat/Light/2026-04-28-contentful-export-code-setup-8ea02f]]
→ Full transcript: [[Chat/Full/2026-04-28-contentful-export-code-setup-8ea02f]]

**Total user messages:** 2

---

### Message 1 — 2026-04-28T23:14

what chat did we set up contentful export code
what chat did we set up contentful export code

### Message 2 — 2026-04-28T23:14

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
