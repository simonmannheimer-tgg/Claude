---
title: GraphQL query for expanded FAQ items
date: 2026-04-28
project: Contentful GraphQL Universal Export
status: active
score: 4/5
uuid: 93aa4c1d-58a0-4188-8538-abb0954e0599
---

#chat/light #project/contentful-graphql-universal-export #status/active #topic/blog #topic/contentful #topic/schema #skill/mhtml-reader

# GraphQL query for expanded FAQ items

- **Date:** [[2026-04-28]]
- **Project:** [[Projects/Contentful GraphQL Universal Export]]
- **Status:** #status/active (score 4/5: deliverable, 5+turns, project-keyword, lasting-effect)
- **Messages:** 16
- **Chat URL:** https://claude.ai/chat/93aa4c1d-58a0-4188-8538-abb0954e0599
- **Medium view:** [[Chat/Medium/2026-04-28-graphql-query-for-expanded-faq-items-93aa4c]]
- **Full transcript:** [[Chat/Full/2026-04-28-graphql-query-for-expanded-faq-items-93aa4c]]

## Summary

need help to get article introduction, with this  type of logic:  {    faqCollection(limit: 1000, where: {isExpanded: true}) {      total      items {        sys {          id        }        isExpanded        name      }    }  }   {    faq

## First user message

> need help to get article introduction, with this  type of logic:  {    faqCollection(limit: 1000, where: {isExpanded: true}) {      total      items {        sys {          id        }        isExpanded        name      }    }  }   {    faqCollection(limit: 1000, where: {isExpanded: true}) {      total      items {        sys {          id        }        name        linkedFrom {          collecti

## Topics

[[topic/blog]], [[topic/contentful]], [[topic/schema]]

## Skills referenced

[[skill/mhtml-reader]]
