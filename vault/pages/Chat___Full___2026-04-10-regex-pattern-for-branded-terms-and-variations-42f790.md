---
title: Regex pattern for branded terms and variations (full)
parent: Chat/Light/2026-04-10-regex-pattern-for-branded-terms-and-variations-42f790
uuid: 42f7902b-ae3c-4edd-8e5d-3df8311dd364
---

#chat/full #project/main #status/completed

# Regex pattern for branded terms and variations — Full Transcript

→ Light view: [[Chat/Light/2026-04-10-regex-pattern-for-branded-terms-and-variations-42f790]]
→ Medium view: [[Chat/Medium/2026-04-10-regex-pattern-for-branded-terms-and-variations-42f790]]

**Messages:** 6 | **Date:** 2026-04-10

---

### 1. **Human** — 2026-04-10T05:59

create a simple regex that catches all branded terms and any variations of brand you can notice from the full data.
create a simple regex that catches all branded terms and any variations of brand you can notice from the full data.

---

### 2. **Claude** — 2026-04-10T06:02

I'll read both CSV files to analyze the full dataset and identify branded term patterns.
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

Found false positives. "01 guys" and "1000 guys one day" are matching because they contain "guys". Also "$30 gift ideas for guys" is matching on "guys".
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Missing "godguys". Need to fix concatenated variations.
```
This block is not supported on your current device yet.
```

Looking at 59,397 unique queries from your GSC data, here's the brand term regex that catches all variations:

```regex
(?:^|\W)(?:(?:the|teh|te|th3|t3h|5he)?\s*[._-]?\s*(?:good|gud|god|goo|goog|gd)[\s._-]+(?:guy|giy|gys|guyz|guyy|giya|giyd)s?|(?:the|te|teh)?(?:good|god|gud|goo)guy(?:s|a|d|e|y|z|ya|yd)?|tgg)(?:\W|$)
```

**What it catches:**

**Spaced variations:**
- `good guys`, `the good guys`, `good guy`, `the good guy`
- Common typos: `good giys`, `good giy`, `good giya`, `good giyd`, `good gys`, `good guyz`
- Alternate spellings: `god guys`, `gud guys`, `goo guys`
- "The" typos: `te good guys`, `teh good guys`, `th3 good guys`, `5he good guys`

**Concatenated variations:**
- `goodguys`, `thegoodguys`, `goodguy`, `thegoodguy`
- Alternate: `godguys`, `godguy`, `gudguy`, `googuy`
- With typo suffixes: `goodguya`, `goodguyd`, `goodguye`, `goodguyy`, `tehgoodguys`

**Delimiters:**
- `good-guys`, `good.guys`, `good_guys`, `the-good-guys`, `the.good.guys`

**Abbreviation:**
- `tgg`

**What it filters out:**
- "guys" alone (gift ideas for guys, 01 guys, 1000 guys one day)
- "the guys" without brand context

Applied to your 59K query dataset, this pattern matches 16,541 queries (27.8%).
 I'll read both CSV files to analyze the full dataset and identify branded term patterns.
Found false positives. "01 guys" and "1000 guys one day" are matching because they contain "guys". Also "$30 gift ideas for guys" is matching on "guys".
Missing "godguys". Need to fix concatenated variations.
Looking at 59,397 unique queries from your GSC data, here's the brand term regex that catches all variations:

```regex
(?:^|\W)(?:(?:the|teh|te|th3|t3h|5he)?\s*[._-]?\s*(?:good|gud|god|goo|goog|gd)[\s._-]+(?:guy|giy|gys|guyz|guyy|giya|giyd)s?|(?:the|te|teh)?(?:good|god|gud|goo)guy(?:s|a|d|e|y|z|ya|yd)?|tgg)(?:\W|$)
```

**What it catches:**

**Spaced variations:**
- `good guys`, `the good guys`, `good guy`, `the good guy`
- Common typos: `good giys`, `good giy`, `good giya`, `good giyd`, `good gys`, `good guyz`
- Alternate spellings: `god guys`, `gud guys`, `goo guys`
- "The" typos: `te good guys`, `teh good guys`, `th3 good guys`, `5he good guys`

**Concatenated variations:**
- `goodguys`, `thegoodguys`, `goodguy`, `thegoodguy`
- Alternate: `godguys`, `godguy`, `gudguy`, `googuy`
- With typo suffixes: `goodguya`, `goodguyd`, `goodguye`, `goodguyy`, `tehgoodguys`

**Delimiters:**
- `good-guys`, `good.guys`, `good_guys`, `the-good-guys`, `the.good.guys`

**Abbreviation:**
- `tgg`

**What it filters out:**
- "guys" alone (gift ideas for guys, 01 guys, 1000 guys one day)
- "the guys" without brand context

Applied to your 59K query dataset, this pattern matches 16,541 queries (27.8%).

---

### 3. **Human** — 2026-04-10T06:10

i ran your vs the current filter we have in seogets, as well as full keyword list, help me identify the final best regex
i ran your vs the current filter we have in seogets, as well as full keyword list, help me identify the final best regex

---

### 4. **Claude** — 2026-04-10T06:12

I'll analyze all three files to compare pattern performance and identify the optimal regex.
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


```
This block is not supported on your current device yet.
```

The current regex has massive false positives. It's catching "5 guys", "3 guys", "gift ideas for guys", "air con guys", etc.
```
This block is not supported on your current device yet.
```

My regex is catching legitimate variations but also some Omega model numbers (obo691tgg) and TGG product codes.
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

These are legitimate typos. Let me check click volume:
```
This block is not supported on your current device yet.
```

"good fuys" has 8,295 clicks. That's legitimate. Let me check what the current regex is catching:
```
This block is not supported on your current device yet.
```

I see the issue. Current regex is catching anything with "goodguys" or "guys" anywhere. Let me look at legitimate TGG queries:
```
This block is not supported on your current device yet.
```

These are legitimate. People search "[product] goodguys". Let me check volume:
```
This block is not supported on your current device yet.
```

Low volume but legitimate. My regex needs to catch these. Let me check the core issue with my pattern:
```
This block is not supported on your current device yet.
```

It does match! Let me check why it's not in my results:
```
This block is not supported on your current device yet.
```

They're not there. The issue is that SEOGets might be applying the regex differently than my test. Let me check what my actual file contains:
```
This block is not supported on your current device yet.
```

**Analysis Results:**

**Current regex:** 18,150 queries (1,915 false positives)
**My regex:** 16,274 queries (40 additions, mostly model numbers)

**Current regex problems:**
- Catches "5 guys", "3 guys", "gift ideas for guys", "air con guys", "plumbing guys", etc.
- Massive false positive rate (10.5% of results are junk)

**My regex problems:**
- Missing concatenated product searches: "agl goodguys", "airfryer goodguys", "airpods goodguys"
- Catching Omega model numbers (obo691tgg, ocg64ffetgg) because they end in "tgg"
- Missing typos: "good fuys" (8,295 clicks), "good fuy", "good bguys"

**Recommendation:**

Your current regex is too loose. My regex is more precise but needs refinement. The optimal pattern should:

1. Catch spaced/concatenated brand variations
2. Catch product+brand concatenations (airfryer goodguys)
3. Add more typo variants (fuy, fuys, bguys)
4. Exclude model numbers ending in tgg

Need me to build v2 fixing these issues?
 I'll analyze all three files to compare pattern performance and identify the optimal regex.
The current regex has massive false positives. It's catching "5 guys", "3 guys", "gift ideas for guys", "air con guys", etc.
My regex is catching legitimate variations but also some Omega model numbers (obo691tgg) and TGG product codes.
These are legitimate typos. Let me check click volume:
"good fuys" has 8,295 clicks. That's legitimate. Let me check what the current regex is catching:
I see the issue. Current regex is catching anything with "goodguys" or "guys" anywhere. Let me look at legitimate TGG queries:
These are legitimate. People search "[product] goodguys". Let me check volume:
Low volume but legitimate. My regex needs to catch these. Let me check the core issue with my pattern:
It does match! Let me check why it's not in my results:
They're not there. The issue is that SEOGets might be applying the regex differently than my test. Let me check what my actual file contains:
**Analysis Results:**

**Current regex:** 18,150 queries (1,915 false positives)
**My regex:** 16,274 queries (40 additions, mostly model numbers)

**Current regex problems:**
- Catches "5 guys", "3 guys", "gift ideas for guys", "air con guys", "plumbing guys", etc.
- Massive false positive rate (10.5% of results are junk)

**My regex problems:**
- Missing concatenated product searches: "agl goodguys", "airfryer goodguys", "airpods goodguys"
- Catching Omega model numbers (obo691tgg, ocg64ffetgg) because they end in "tgg"
- Missing typos: "good fuys" (8,295 clicks), "good fuy", "good bguys"

**Recommendation:**

Your current regex is too loose. My regex is more precise but needs refinement. The optimal pattern should:

1. Catch spaced/concatenated brand variations
2. Catch product+brand concatenations (airfryer goodguys)
3. Add more typo variants (fuy, fuys, bguys)
4. Exclude model numbers ending in tgg

Need me to build v2 fixing these issues?

---

### 5. **Human** — 2026-04-10T06:15

Continue
Continue

---

### 6. **Claude** — 2026-04-10T06:18

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Perfect! Model numbers excluded, typos added, product+brand caught. Let me verify false positives are blocked:
```
This block is not supported on your current device yet.
```

Excellent! Zero false positives. Now test on full dataset:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Excellent! Now capturing product+brand queries. Let me verify the model numbers are excluded:
```
This block is not supported on your current device yet.
```

Perfect! Model numbers excluded. Let me check for any remaining false positives:
```
This block is not supported on your current device yet.
```

"gift card good guys" is legitimate! Let me verify no other false positives:
```
This block is not supported on your current device yet.
```

All legitimate! These are "[product] good guys" searches. Let me check one edge case - "3 good guys":
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Not in dataset. Let me run final comparison:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me test one final edge case - make sure the negative lookahead doesn't break legitimate queries:
```
This block is not supported on your current device yet.
```

Good! It catches legitimate queries but blocks double-s typos (goodguyss) and nonsense (goodguysau). Let me check if those exist in the dataset:
```
This block is not supported on your current device yet.
```

They exist! Need to allow double-s. Let me refine:
```
This block is not supported on your current device yet.
```

Perfect! Let me verify model numbers still blocked:
```
This block is not supported on your current device yet.
```

Excellent! Final count:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

## **Final Recommendation**

**Use this regex:**
```regex
(?:^|\W)(?:(?:the|teh|te|th3|t3h|5he)?\s*[._-]?\s*(?:good|gud|god|goo|goog|gd)[\s._-]+(?:guy|giy|gys|guyz|guyy|giya|giyd|fuy|fuys|bguy)s?|(?:the|te|teh)?(?:good|god|gud|goo)guy(?:s{1,2}|a|d|e|y|z|ya|yd)?(?![a-z])|(?<![a-z0-9])tgg(?![a-z0-9]))(?:\W|$)
```

**Results:**
- **16,535 queries** (27.8% of dataset)
- **Zero false positives** (vs 1,915 in current regex)
- **+300 legitimate queries** vs current (product+brand terms like "airpods goodguys")
- **Blocks all junk:** 5 guys, gift ideas for guys, air con guys, model numbers

**Critical improvements over current:**
1. Negative lookahead blocks model numbers (obo691tgg, tggce64-5)
2. Word boundaries block "N guys" false positives
3. Comprehensive typo coverage including "good fuys" (8,295 clicks)
4. Catches product+brand concatenations (dyson goodguys, iphone goodguys)

Your current regex has 10.5% false positive rate. This one is clean.
 
Perfect! Model numbers excluded, typos added, product+brand caught. Let me verify false positives are blocked:
Excellent! Zero false positives. Now test on full dataset:
Excellent! Now capturing product+brand queries. Let me verify the model numbers are excluded:
Perfect! Model numbers excluded. Let me check for any remaining false positives:
"gift card good guys" is legitimate! Let me verify no other false positives:
All legitimate! These are "[product] good guys" searches. Let me check one edge case - "3 good guys":
Not in dataset. Let me run final comparison:
Now let me test one final edge case - make sure the negative lookahead doesn't break legitimate queries:
Good! It catches legitimate queries but blocks double-s typos (goodguyss) and nonsense (goodguysau). Let me check if those exist in the dataset:
They exist! Need to allow double-s. Let me refine:
Perfect! Let me verify model numbers still blocked:
Excellent! Final count:
## **Final Recommendation**

**Use this regex:**
```regex
(?:^|\W)(?:(?:the|teh|te|th3|t3h|5he)?\s*[._-]?\s*(?:good|gud|god|goo|goog|gd)[\s._-]+(?:guy|giy|gys|guyz|guyy|giya|giyd|fuy|fuys|bguy)s?|(?:the|te|teh)?(?:good|god|gud|goo)guy(?:s{1,2}|a|d|e|y|z|ya|yd)?(?![a-z])|(?<![a-z0-9])tgg(?![a-z0-9]))(?:\W|$)
```

**Results:**
- **16,535 queries** (27.8% of dataset)
- **Zero false positives** (vs 1,915 in current regex)
- **+300 legitimate queries** vs current (product+brand terms like "airpods goodguys")
- **Blocks all junk:** 5 guys, gift ideas for guys, air con guys, model numbers

**Critical improvements over current:**
1. Negative lookahead blocks model numbers (obo691tgg, tggce64-5)
2. Word boundaries block "N guys" false positives
3. Comprehensive typo coverage including "good fuys" (8,295 clicks)
4. Catches product+brand concatenations (dyson goodguys, iphone goodguys)

Your current regex has 10.5% false positive rate. This one is clean.
