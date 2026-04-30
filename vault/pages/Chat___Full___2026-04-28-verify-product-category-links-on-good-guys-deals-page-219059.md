---
title: Verify product category links on Good Guys deals page (full)
parent: Chat/Light/2026-04-28-verify-product-category-links-on-good-guys-deals-page-219059
uuid: 219059f1-601c-416c-9e7f-e976b5c07198
---

#chat/full #project/deals-page-slider-audit-14-pages #status/completed

# Verify product category links on Good Guys deals page — Full Transcript

→ Light view: [[Chat/Light/2026-04-28-verify-product-category-links-on-good-guys-deals-page-219059]]
→ Medium view: [[Chat/Medium/2026-04-28-verify-product-category-links-on-good-guys-deals-page-219059]]

**Messages:** 6 | **Date:** 2026-04-28

---

### 1. **Human** — 2026-04-28T06:02

check that this page has all these linked?
https://www.thegoodguys.com.au/deals/bbqshttps://www.thegoodguys.com.au/deals/coffee-machineshttps://www.thegoodguys.com.au/deals/dishwashershttps://www.thegoodguys.com.au/deals/dryershttps://www.thegoodguys.com.au/deals/fridgeshttps://www.thegoodguys.com.au/deals/headphones-and-soundbarshttps://www.thegoodguys.com.au/deals/laptopshttps://www.thegoodguys.com.au/deals/microwaveshttps://www.thegoodguys.com.au/deals/phone-and-smart-watcheshttps://www.thegoodguys.com.au/deals/tvshttps://www.thegoodguys.com.au/deals/vacuums-and-cleaninghttps://www.thegoodguys.com.au/deals/washing-machines
check that this page has all these linked?
https://www.thegoodguys.com.au/deals/bbqshttps://www.thegoodguys.com.au/deals/coffee-machineshttps://www.thegoodguys.com.au/deals/dishwashershttps://www.thegoodguys.com.au/deals/dryershttps://www.thegoodguys.com.au/deals/fridgeshttps://www.thegoodguys.com.au/deals/headphones-and-soundbarshttps://www.thegoodguys.com.au/deals/laptopshttps://www.thegoodguys.com.au/deals/microwaveshttps://www.thegoodguys.com.au/deals/phone-and-smart-watcheshttps://www.thegoodguys.com.au/deals/tvshttps://www.thegoodguys.com.au/deals/vacuums-and-cleaninghttps://www.thegoodguys.com.au/deals/washing-machines

---

### 2. **Claude** — 2026-04-28T06:03

Let me read the MHTML file to check for these links.
```
This block is not supported on your current device yet.
```

Now let me parse the MHTML file and check for the links.
```
This block is not supported on your current device yet.
```

All 12 target URLs are present. There are also some additional /deals/ links on the page that weren't in the check list.All 12 present. ✓

Two additional /deals/ links on the page not in your list, for awareness:
- https://www.thegoodguys.com.au/deals/black-friday-tvs
- https://www.thegoodguys.com.au/deals/kitchen-appliances
 
All 12 present. ✓

Two additional /deals/ links on the page not in your list, for awareness:
- https://www.thegoodguys.com.au/deals/black-friday-tvs
- https://www.thegoodguys.com.au/deals/kitchen-appliances

---

### 3. **Human** — 2026-04-28T06:11

where is black friday tvs? also we are only checking this module:
where is black friday tvs? also we are only checking this module:

---

### 4. **Claude** — 2026-04-28T06:12

The user is asking about the internal link block (the deals navigation module with the category links), not the "Shop EOFY Deals!" carousel shown in the screenshot. They want to know where /deals/black-friday-tvs appears in context of the module they're checking.

Looking at the screenshot, this shows a "Shop EOFY Deals!" carousel - this is NOT the module Simon is checking. He's checking the internal link block with the 12 deals category links.

The black-friday-tvs link I found was present on the page but likely in a different module/section, not the specific internal link block Simon cares about. The screenshot shows the EOFY deals carousel at the top of the page.


I need to locate the 12-link internal module in the HTML and see where black-friday-tvs actually appears relative to it, since that link might be in a completely different section of the page.
```
This block is not supported on your current device yet.
```

The black-friday-tvs link is in the FAQ/intro text section (_collectionPageFaq_1fo6t_99 / _richText_fzyd0_11), not in the internal link module. So the 12 links I checked earlier are in the correct module. The black-friday-tvs link is in the body copy/FAQ area.

Simon said "we are only checking this module" - referring to the internal link block with the 12 category links. So the black-friday-tvs is in the FAQ/copy section, not in that module. 

So my earlier check was valid - all 12 links are accounted for in that specific module. But I should double-check whether Simon's scope is really just that internal link navigation block or if he wants me to verify the entire page structure.
```
This block is not supported on your current device yet.
```

So the 12 target links are all in `_slider_1frmw_16 _hasFade_1frmw_36` / `_sliderContainer` - this is the "Shop EOFY Deals!" carousel shown in the screenshot. That IS the module shown in the image.

Wait, but the screenshot shows "Shop EOFY Deals!" with items like "EOFY Deals 2026", "TV Deals", "Fridge Deals", "Washing Machine Deals", etc. Those are carousel/slider items. But those are the 12 links (fridges, washing-machines, dishwashers, coffee-machines, microwaves, vacuums-and-cleaning, dryers, laptops, headphones-and-soundbars, phone-and-smart-watches, bbqs, tvs).
 
Ah, so Simon is specifically checking just this carousel module, and the black-friday-tvs link actually appears in the FAQ copy text below, not in the slider itself. That means all 12 target links are accounted for in the carousel, and black-friday-tvs doesn't need to be there since it wasn't part of his original list anyway.Good news and clarification together:

All 12 of your target links are in the slider module (`_sliderContainer` / `_slider`), which is exactly what's shown in the screenshot.

The `/deals/black-friday-tvs` link is **not** in that module. It appears in the FAQ/body copy text (`_collectionPageFaq`), inline within a paragraph alongside `/deals/boxing-day-tvs`. So it's not a slider tile, just a contextual link in the copy. Nothing to action there.
 
Good news and clarification together:

All 12 of your target links are in the slider module (`_sliderContainer` / `_slider`), which is exactly what's shown in the screenshot.

The `/deals/black-friday-tvs` link is **not** in that module. It appears in the FAQ/body copy text (`_collectionPageFaq`), inline within a paragraph alongside `/deals/boxing-day-tvs`. So it's not a slider tile, just a contextual link in the copy. Nothing to action there.

---

### 5. **Human** — 2026-04-28T07:38

Can you now go to each of those pages and any other /deals pages (not Black Friday or Boxing Day) and check if the new slider is live?
Can you now go to each of those pages and any other /deals pages (not Black Friday or Boxing Day) and check if the new slider is live?

---

### 6. **Claude** — 2026-04-28T07:39

The user wants me to visit each of the /deals/ pages and check if the new slider module (the one with class `_sliderContainer_1frmw_16` / `_slider_1frmw_16`) is live. Let me identify all the deals pages first:

From the earlier extraction, the /deals/ pages found were:
1. https://www.thegoodguys.com.au/deals/bbqs
2. https://www.thegoodguys.com.au/deals/coffee-machines


3. https://www.thegoodguys.com.au/deals/dishwashers
4. https://www.thegoodguys.com.au/deals/dryers
5. https://www.thegoodguys.com.au/deals/fridges
6. https://www.thegoodguys.com.au/deals/headphones-and-soundbars
7. https://www.thegoodguys.com.au/deals/laptops
8. https://www.thegoodguys.com.au/deals/microwaves
9. https://www.thegoodguys.com.au/deals/phone-and-smart-watches
10. https://www.thegoodguys.com.au/deals/tvs
11. https://www.thegoodguys.com.au/deals/washing-machines (and possibly more)

I need to check the main /deals page and all category pages for the slider module, which uses the class `_sliderContainer_1frmw_16` or `_slider_1frmw_16`. I'll write a script to systematically fetch and inspect each page.The full list to check: the 12 from your list + `/deals/kitchen-appliances` + `/deals` (main). Excluding Black Friday and Boxing Day. That's 14 pages. Fetching now.
```
This block is not supported on your current device yet.
```

All 14 pages: 200 OK, slider present. ✓
 
The full list to check: the 12 from your list + `/deals/kitchen-appliances` + `/deals` (main). Excluding Black Friday and Boxing Day. That's 14 pages. Fetching now.
All 14 pages: 200 OK, slider present. ✓
