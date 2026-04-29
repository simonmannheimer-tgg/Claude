---
title: GraphQL query for expanded FAQ items (medium)
parent: Chat/Light/2026-04-28-graphql-query-for-expanded-faq-items-93aa4c
uuid: 93aa4c1d-58a0-4188-8538-abb0954e0599
---

#chat/medium #project/contentful-graphql-universal-export #status/active

# GraphQL query for expanded FAQ items — Key User Messages

→ Light view: [[Chat/Light/2026-04-28-graphql-query-for-expanded-faq-items-93aa4c]]
→ Full transcript: [[Chat/Full/2026-04-28-graphql-query-for-expanded-faq-items-93aa4c]]

**Total user messages:** 11

---

### Message 1 — 2026-04-23T02:54

need help to get article introduction, with this  type of logic:

{    faqCollection(limit: 1000, where: {isExpanded: true}) {      total      items {        sys {          id        }        isExpanded        name      }    }  }
 
{    faqCollection(limit: 1000, where: {isExpanded: true}) {      total      items {        sys {          id        }        name        linkedFrom {          collectionPageCollection {            items {              sys {                id              }            }          }          l1BrandstoreCollection {            items {              sys {                id              }            }          }          sectionCollection {            items {              sys {                id              }            }          }        }      }    }  }
 

from graphiql contentful
need help to get article introduction, with this  type of logic:

{    faqCollection(limit: 1000, where: {isExpanded: true}) {      total      items {        sys {          id        }        isExpanded        name      }    }  }
 
{    faqCollection(limit: 1000, where: {isExpanded: true}) {      total      items {        sys {          id        }        name        linkedFrom {          collectionPageCollection {            items {              sys {                id              }            }          }          l1BrandstoreCollection {            items {              sys {                id              }            }          }          sectionCollection {          

[truncated — see full transcript]

### Message 2 — 2026-04-23T02:59

{
  "errors": [
    {
      "message": "Cannot query field \"articleIntroductionCollection\" on type \"Query\". Did you mean \"articleCursorCollection\", \"richCollectionCollection\", \"articleCollection\", \"inputOptionCollection\", or \"promoProductTileCollection\"?",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ]
    }
  ]
}
{
  "errors": [
    {
      "message": "Cannot query field \"articleIntroductionCollection\" on type \"Query\". Did you mean \"articleCursorCollection\", \"richCollectionCollection\", \"articleCollection\", \"inputOptionCollection\", or \"promoProductTileCollection\"?",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ]
    }
  ]
}

### Message 3 — 2026-04-23T02:59

{
  "errors": [
    {
      "message": "Cannot query field \"title\" on type \"Article\". Did you mean \"date\"?",
      "locations": [
        {
          "line": 8,
          "column": 7
        }
      ]
    },
    {
      "message": "Cannot query field \"collectionPageCollection\" on type \"ArticleLinkingCollections\". Did you mean \"richCollectionCollection\" or \"richCollectionCursorCollection\"?",
      "locations": [
        {
          "line": 13,
          "column": 9
        }
      ]
    },
    {
      "message": "Cannot query field \"l1BrandstoreCollection\" on type \"ArticleLinkingCollections\". Did you mean \"bentoGridCollection\", \"entryCollection\", or \"entryCursorCollection\"?",
      "locations": [
        {
          "line": 21,
          "column": 9
        }
      ]
    },
    {
      "message": "Cannot query field \"sectionCollection\" on type \"ArticleLinkingCollections\". Did you mean \"entryCollection\", \"articleCollection\", or \"bentoGridCollection\"?",
      "locations": [
        {
          "line": 28,
          "column": 9
        }
      ]
    }
  ]
}
{
  "errors": [
    {
      "message": "Cannot query field \"title\" on type \"Article\". Did you mean \"date\"?",
      "locations": [
        {
          "line": 8,
          "column": 7
        }
      ]
    },
    {
      "message": "Cannot query field \"collectionPageCollection\" on type \"ArticleLinkingCollections\". Did you mean \"richCollectionCollection\" or \"richCollectionCursorColl

[truncated — see full transcript]

### Message 4 — 2026-04-23T03:00

get the code to first show all, ill give you that to narrow down
get the code to first show all, ill give you that to narrow down

### Message 5 — 2026-04-23T03:02

working?

check against this part of each page across a set of tests.https://www.thegoodguys.com.au/whats-new/best-smart-fridge-for-you

<div data-testid="contentful-richtext" class="_richText_fzyd0_11 _rte_14tfn_11 _richText_h0rye_61"><p>Gone are the days when a <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/fridges-and-freezers" target="_self">fridge</a> was simply a safe storage unit for your food, with the best <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/search?q=smart%20fridges" target="_self">smart fridges</a> around, a fridge is now much more than this.&nbsp;</p><p>In the world of home appliances, technology is everchanging and design is becoming more focussed around easing everyday tasks. This strategy has seen the development of fridge features like Wi-Fi connectability to check the contents of your fridge when you’re out and about, or a ‘knock twice’ feature on your fridge door to reveal the contents without affecting indoor temperatures and keep food fresher for longer.</p><p>With more and more fridge features regularly being created, it can be difficult to find the best smart fridge for you. So, we have come up with the ultimate guide to remove the tough work and ensure that you find the perfect addition to your <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/cooking-and-dishwashers" target="_self">kitchen</a>.</p></div>
working?

check against this part of each page across a set of tests.https://www.thegoodguys.co

[truncated — see full transcript]

### Message 6 — 2026-04-23T03:04

pick a few, do spotchecks
pick a few, do spotchecks

### Message 7 — 2026-04-23T03:08

pick a few, do spotchecks
pick a few, do spotchecks

### Message 8 — 2026-04-23T03:18

add so it also gets the article slugs
add so it also gets the article slugs

### Message 9 — 2026-04-23T03:19

add so it also gets the article slugs
add so it also gets the article slugs

### Message 10 — 2026-04-28T23:17

i would like to be able to export any page on contentful, regardless of type
i would like to be able to export any page on contentful, regardless of type

### Message 11 — 2026-04-28T23:35

write a short instruction to build the url based on the output
write a short instruction to build the url based on the output
