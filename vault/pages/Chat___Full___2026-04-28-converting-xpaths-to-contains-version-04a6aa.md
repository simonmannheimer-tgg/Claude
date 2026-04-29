---
title: Converting xpaths to contains version (full)
parent: Chat/Light/2026-04-28-converting-xpaths-to-contains-version-04a6aa
uuid: 04a6aad6-5de0-4f8a-b872-d460856d1962
---

#chat/full #project/eofy #status/active

# Converting xpaths to contains version — Full Transcript

→ Light view: [[Chat/Light/2026-04-28-converting-xpaths-to-contains-version-04a6aa]]
→ Medium view: [[Chat/Medium/2026-04-28-converting-xpaths-to-contains-version-04a6aa]]

**Messages:** 6 | **Date:** 2026-04-28

---

### 1. **Human** — 2026-04-28T09:35

I'll need help to change these xpaths to the contains version:


this (csspath) body > main > div > article > div > div:nth-child(4) with 

<div data-testid="contentful-richtext" class="_richText_fzyd0_11 _rte_14tfn_11 _richText_h0rye_61">

as either xpath or css

//div[contains(@class, '_header_')]
I'll need help to change these xpaths to the contains version:


this (csspath) body > main > div > article > div > div:nth-child(4) with 

<div data-testid="contentful-richtext" class="_richText_fzyd0_11 _rte_14tfn_11 _richText_h0rye_61">

as either xpath or css

//div[contains(@class, '_header_')]

---

### 2. **Claude** — 2026-04-28T09:35

The user wants to convert CSS paths to XPath using `contains()` for class matching. They have a CSS path and want the XPath equivalent using contains for the class attribute.

The element is: `<div data-testid="contentful-richtext" class="_richText_fzyd0_11 _rte_14tfn_11 _richText_h0rye_61">`

They want something like `//div[contains(@class, '_header_')]` but for this element.

The best approach would be to target the `data-testid` attribute since it's stable, or use contains on one of the class names.


I can provide a few XPath options here: the simplest is targeting the data-testid directly, but I could also use contains on one of the class names like `_richText_`, or combine both attributes for extra precision.Target `data-testid` directly, it's the stable anchor here:

```xpath
//div[@data-testid="contentful-richtext"]
```

If you need the `contains` class pattern to match the same pattern as your example:

```xpath
//div[contains(@class, '_richText_')]
```

Combined (most precise):

```xpath
//div[@data-testid="contentful-richtext" and contains(@class, '_richText_')]
```

CSS equivalent using attribute selector:

```css
div[data-testid="contentful-richtext"]
```

The `data-testid` version is the right call. Class names with hashed suffixes like `_richText_fzyd0_11` will change on next build. `data-testid` values are intentionally stable.
 
Target `data-testid` directly, it's the stable anchor here:

```xpath
//div[@data-testid="contentful-richtext"]
```

If you need the `contains` class pattern to match the same pattern as your example:

```xpath
//div[contains(@class, '_richText_')]
```

Combined (most precise):

```xpath
//div[@data-testid="contentful-richtext" and contains(@class, '_richText_')]
```

CSS equivalent using attribute selector:

```css
div[data-testid="contentful-richtext"]
```

The `data-testid` version is the right call. Class names with hashed suffixes like `_richText_fzyd0_11` will change on next build. `data-testid` values are intentionally stable.

---

### 3. **Human** — 2026-04-28T09:37

the most precise gets 4 results... /html/body/main/div/article/div/div[3] this is waht i want:

<div data-testid="contentful-richtext" class="_richText_fzyd0_11 _rte_14tfn_11 _richText_h0rye_61"><p>EOFY is one of the best times of year to save on tech, home appliances and everyday essentials. Whether you’re upgrading your work-from-home setup, replacing an older appliance or finally buying that TV or coffee machine you’ve had your eye on, <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/eofy-sale" target="_self">EOFY deals</a> are a smart time to shop.</p><p>At The Good Guys, you’ll find fantastic deals on home appliances, entertainment and tech, plus helpful advice to make choosing easier. From <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/computers-tablets-and-gaming" target="_self">laptops</a> and <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/phones-and-wearables" target="_self">mobile phones</a> to <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/fridges-and-freezers/refrigerators" target="_self">fridges</a>, <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/laundry/washing-machines" target="_self">washing machines </a>and <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/vacuums-and-cleaners" target="_self">vacuums</a>, there are plenty of EOFY offers worth checking out.</p><p>Before making any purchase for work or tax purposes, it’s always a good idea to speak with a qualified accountant or financial professional to understand what may be right for your situation.</p><p><a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/eofy-sale" target="_self">Want to find out more EOFY tips &amp; top picks? Check out our buying guide!</a></p></div>
the most precise gets 4 results... /html/body/main/div/article/div/div[3] this is waht i want:

<div data-testid="contentful-richtext" class="_richText_fzyd0_11 _rte_14tfn_11 _richText_h0rye_61"><p>EOFY is one of the best times of year to save on tech, home appliances and everyday essentials. Whether you’re upgrading your work-from-home setup, replacing an older appliance or finally buying that TV or coffee machine you’ve had your eye on, <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/eofy-sale" target="_self">EOFY deals</a> are a smart time to shop.</p><p>At The Good Guys, you’ll find fantastic deals on home appliances, entertainment and tech, plus helpful advice to make choosing easier. From <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/computers-tablets-and-gaming" target="_self">laptops</a> and <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/phones-and-wearables" target="_self">mobile phones</a> to <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/fridges-and-freezers/refrigerators" target="_self">fridges</a>, <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/laundry/washing-machines" target="_self">washing machines </a>and <a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/vacuums-and-cleaners" target="_self">vacuums</a>, there are plenty of EOFY offers worth checking out.</p><p>Before making any purchase for work or tax purposes, it’s always a good idea to speak with a qualified accountant or financial professional to understand what may be right for your situation.</p><p><a class="_link_14tfn_19" href="https://www.thegoodguys.com.au/eofy-sale" target="_self">Want to find out more EOFY tips &amp; top picks? Check out our buying guide!</a></p></div>

---

### 4. **Claude** — 2026-04-28T09:37

The user wants to target specifically the 3rd div child, which is `div[3]` in the xpath `/html/body/main/div/article/div/div[3]`. The element has `data-testid="contentful-richtext"` but there are 4 of them on the page. They need to narrow it to the third one specifically.

The xpath `/html/body/main/div/article/div/div[3]` suggests it's the 3rd `div` child of `article > div`. Let me think about how to express this with contains.

The most precise xpath would combine the position with the data-testid:


I can target it with either `//article/div/div[3][@data-testid="contentful-richtext"]` to get the 3rd div with that attribute, or `(//div[@data-testid="contentful-richtext"])[3]` to grab the 3rd matching element overall. There's a discrepancy between the original CSS path showing `div:nth-child(4)` and the xpath showing `div[3]` — that's likely because nth-child counts all element types while XPath's positional predicate counts only divs.The issue is there are 4 `contentful-richtext` divs on the page. You need to combine the positional context with the attribute:

```xpath
//article/div/div[3][@data-testid="contentful-richtext"]
```

Or if you want the nth-match approach:

```xpath
(//div[@data-testid="contentful-richtext"])[3]
```

CSS equivalent of the first:

```css
article > div > div:nth-child(3)[data-testid="contentful-richtext"]
```

Note the discrepancy between your original CSS (`nth-child(4)`) and the XPath (`div[3]`): `nth-child` counts all element siblings regardless of type, while XPath's `div[3]` counts only div siblings. If the first two match, use the XPath positional version as the reliable one.
 
The issue is there are 4 `contentful-richtext` divs on the page. You need to combine the positional context with the attribute:

```xpath
//article/div/div[3][@data-testid="contentful-richtext"]
```

Or if you want the nth-match approach:

```xpath
(//div[@data-testid="contentful-richtext"])[3]
```

CSS equivalent of the first:

```css
article > div > div:nth-child(3)[data-testid="contentful-richtext"]
```

Note the discrepancy between your original CSS (`nth-child(4)`) and the XPath (`div[3]`): `nth-child` counts all element siblings regardless of type, while XPath's `div[3]` counts only div siblings. If the first two match, use the XPath positional version as the reliable one.

---

### 5. **Human** — 2026-04-28T09:41

NOW /html/body/main/div/article/div
NOW /html/body/main/div/article/div

---

### 6. **Claude** — 2026-04-28T09:41

The user wants the XPath `contains` version for `/html/body/main/div/article/div`.

Simple answer:

```xpath
//article/div
```

Or with contains if they need a class-based version. But they haven't given me the HTML for this element, so I'll just give the clean XPath equivalent.```xpath
//article/div
```

If you need it more anchored:

```xpath
//main/div/article/div
```

What's the element's HTML? If it has a `data-testid` or stable class, that's cleaner than relying on position.
 
```xpath
//article/div
```

If you need it more anchored:

```xpath
//main/div/article/div
```

What's the element's HTML? If it has a `data-testid` or stable class, that's cleaner than relying on position.
