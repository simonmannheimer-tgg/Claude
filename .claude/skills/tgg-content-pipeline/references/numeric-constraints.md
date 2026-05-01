# Numeric Constraints by Content Type

Hard limits enforced by `verification-gate-protocol` and checked by `tgg-ce-qa`.
Source of truth: individual YAML files at `.claude/skills/verification-gate-protocol/constraints/<type>.yaml`.

---

## buying-guide

| Constraint | Min | Max | Notes |
|---|---|---|---|
| Word count | 1,800 | 2,500 | Body only, excluding FAQ block |
| H2 count | 6 | 9 | Includes FAQ H2 |
| Internal links | 8 | 12 | Resolved to Contentful entry IDs in final |
| FAQ questions | 5 | 8 | |
| FAQ answer words | 50 | 120 | Per answer |

Required sections: Australian retail considerations, EAV attributes block, recommendation callout

---

## how-to

| Constraint | Min | Max | Notes |
|---|---|---|---|
| Word count | 800 | 1,400 | |
| H2 count | 4 | 7 | |
| Internal links | 4 | 8 | |

Required sections: numbered steps (action verb openers), tools/requirements, time estimate

---

## comparison

| Constraint | Min | Max | Notes |
|---|---|---|---|
| Word count | 1,200 | 2,000 | |
| H2 count | 4 | 6 | |
| Internal links | 6 | 10 | |
| Comparison table rows | 4 | — | Minimum 4 attribute rows |

Required sections: comparison table, recommendation callout, Australian retail considerations

---

## eav-explainer

| Constraint | Min | Max | Notes |
|---|---|---|---|
| Word count | 1,000 | 1,800 | |
| H2 count | 4 | 7 | |
| Internal links | 6 | 10 | |
| EAV attributes | 5 | — | Minimum 5 defined attributes |

Required sections: EAV mapping table, Australian retail considerations, buyer decision summary

---

## plp-intro

| Constraint | Min | Max | Notes |
|---|---|---|---|
| Character count | 220 | 250 | Total including spaces |
| Sentences | 2 | 2 | Exactly 2 |
| TGG mentions | 1 | 1 | In S2 only |

Banned S1 openers: Discover, Explore, Shop, Find, Browse
Brand PLP banned words: trusted, reliable, enjoy, features

---

## faq-block

| Constraint | Min | Max | Notes |
|---|---|---|---|
| Question count | 5 | 8 | |
| Answer words | 50 | 120 | Per answer |
| Question words | 6 | 18 | |

Answers must be plain prose (no markdown). Schema-ready for JSON-LD FAQPage.

---

## Universal (all types)

- Australian English spelling (organise, colour, optimise)
- No em dashes as sentence connectors (use full stop + space)
- No AI banned phrases (defers to tgg-humanizer 29-pattern list)
- Claim-evidence pairing for factual claims
