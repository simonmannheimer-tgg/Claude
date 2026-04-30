---
name: tgg-contentful-linker
description: >
  Resolve TGG website URLs, slugs, page names, or copy requests to Contentful entry links.
  Trigger this skill whenever Simon is working on TGG content and a Contentful link would
  be useful — PLP intros, metadata, FAQ copy, category descriptions, deals pages, articles,
  brand pages, landing pages, or any Contentful-managed page. Also trigger when Simon says
  "find the Contentful entry", "give me the Contentful link", "what's the entry for", or
  references a TGG slug or URL in a copy/editing context. When in doubt, surface the link
  — it takes seconds and saves a manual search.
---

# TGG Contentful Linker

Provides direct Contentful entry links for any TGG website page by matching slugs from
the exported entry data.

## Data source

- **File:** `references/entries.json`
- **Exported:** 29 April 2026
- **Entries:** 3,666 slugs across 5 content types (full coverage)
- **Space:** `zbzrcwjtokv7`
- **Environment name:** `master`

## URL formula

```
https://app.contentful.com/spaces/zbzrcwjtokv7/environments/master/entries/{sys.id}
```

Always use `master` literally. Never substitute the `environmentId` UUID
(`8370f673-69c6-417a-a841-0d3fe48edc9b`) into the URL — that is an internal identifier,
not the environment name.

## How to resolve a link

1. Extract the slug from the TGG URL or context. Examples:
   - `https://www.thegoodguys.com.au/deals/cooking` → slug: `deals/cooking`
   - `https://www.thegoodguys.com.au/tcl/televisions/all-tvs/latest-tvs` → slug: `tcl/televisions/all-tvs/latest-tvs`
   - `https://www.thegoodguys.com.au/eofy-sale` → slug: `eofy-sale`
   - Blog articles use full path slugs, e.g. `whats-new/how-homedics-compression-therapy-can-help-ease-sore-muscles`

2. Load `references/entries.json` and look up the slug.

3. Build the URL:
   ```
   https://app.contentful.com/spaces/zbzrcwjtokv7/environments/master/entries/{id}
   ```

4. If not found: check whether the page is a `collectionPage` (likely if the slug looks
   like a category path). Tell Simon the entry may exist but was outside the export cap,
   and link to the GraphQL explorer to search manually:
   `https://app.contentful.com/spaces/zbzrcwjtokv7/environments/master/apps/app_installations/graphiql/`

## Content types in the export

| Content type    | Description              | Entries |
|-----------------|--------------------------|---------|
| collectionPages | Collection/category PLPs | 1,957   |
| brandstores     | Brand + deals pages      | 336     |
| articles        | Blog articles            | 799     |
| landingPages    | Landing pages            | 303     |
| pages           | General pages            | 271     |

## Stale data check (silent)

The export date is **29 April 2026**. At the start of any conversation where this skill
is used, silently check today's date against this benchmark.

- **Under 3 months since export:** use the data without comment.
- **3 months or more since export (on or after 29 July 2026):** surface this notice once
  per conversation:

  > The Contentful export bundled in this skill is from 29 April 2026. It may be missing
  > new entries. To refresh it, re-run the GraphQL query in the skill header at:
  > https://app.contentful.com/spaces/zbzrcwjtokv7/environments/master/apps/app_installations/graphiql/
  > and replace `references/entries.json` with the new output.

Do not repeat this notice more than once per conversation.

## GraphQL query (for re-running the export)

```graphql
query GetAllPages {
  collectionPages1: collectionPageCollection(limit: 1000, skip: 0) {
    total
    items {
      sys { id environmentId }
      slug
      pageName
      shortName
      pageDescription { json }
      seoMetaData { title description canonical index follow }
    }
  }
  collectionPages2: collectionPageCollection(limit: 1000, skip: 1000) {
    total
    items {
      sys { id environmentId }
      slug
      pageName
      shortName
      pageDescription { json }
      seoMetaData { title description canonical index follow }
    }
  }
  brandstores: l1BrandstoreCollection(limit: 1000) {
    total
    items {
      sys { id environmentId }
      slug
      pageName
      shortName
      pageDescription { json }
      seoMetaData { title description canonical index follow }
    }
  }
  articles: articleCollection(limit: 1000) {
    total
    items {
      sys { id environmentId }
      slug
      name
      introduction { json }
      seo { title description canonical index follow }
    }
  }
  landingPages: landingPageSimplifiedCollection(limit: 1000) {
    total
    items {
      sys { id environmentId }
      slug
      pageName
      shortName
      seo { title description canonical index follow }
    }
  }
  pages: pageCollection(limit: 1000) {
    total
    items {
      sys { id environmentId }
      slug
      pageName
      shortName
      seo { title description canonical index follow }
    }
  }
}
```

`collectionPages` is split into two aliased calls (`skip: 0` and `skip: 1000`) to work
around the 1,000-item GraphQL limit. If the `total` ever exceeds 2,000, add a third alias
with `skip: 2000`.
