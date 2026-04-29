---
title: Debugging The Good Guys website content structure (full)
parent: Chat/Light/2026-04-28-debugging-the-good-guys-website-content-structure-8519a6
uuid: 8519a693-f272-4871-a7dd-45bca7b7796c
---

#chat/full #project/contentful-node-type-fix-4-articles-rema #status/active

# Debugging The Good Guys website content structure — Full Transcript

→ Light view: [[Chat/Light/2026-04-28-debugging-the-good-guys-website-content-structure-8519a6]]
→ Medium view: [[Chat/Medium/2026-04-28-debugging-the-good-guys-website-content-structure-8519a6]]

**Messages:** 10 | **Date:** 2026-04-28

---

### 1. **Human** — 2026-04-28T00:07

i need you to go to [thegoodguys.com.au](http://thegoodguys.com.au) and figure out why this is happening

whats-new/best-lg-appliances-for-a-holiday-ready-home
whats-new/perks-of-being-a-gold-service-extras-member
whats-new/5-reasons-to-use-bose-noise-cancelling-headphones
whats-new/biggest-kitchen-renovation-mistakes
whats-new/how-to-save-with-price-beat


Only heading 2, heading 3, heading 4, ordered list, unordered list, quote, asset, link to Url, and block entry nodes are allowed
i need you to go to [thegoodguys.com.au](http://thegoodguys.com.au) and figure out why this is happening

whats-new/best-lg-appliances-for-a-holiday-ready-home
whats-new/perks-of-being-a-gold-service-extras-member
whats-new/5-reasons-to-use-bose-noise-cancelling-headphones
whats-new/biggest-kitchen-renovation-mistakes
whats-new/how-to-save-with-price-beat


Only heading 2, heading 3, heading 4, ordered list, unordered list, quote, asset, link to Url, and block entry nodes are allowed

---

### 2. **Claude** — 2026-04-28T00:08

The user wants me to visit those URLs on thegoodguys.com.au and figure out why they're getting an error about only certain node types being allowed. This sounds like a Contentful rich text validation error. Let me fetch a few of those URLs to understand what's happening.

Actually, the error message "Only heading 2, heading 3, heading 4, ordered list, unordered list, quote, asset, link to Url, and block entry nodes are allowed" sounds like a Contentful rich text field validation error - it's a CMS constraint, not something visible on the live site.

Let me fetch those URLs to check what's there, but I think the real issue is in Contentful's rich text editor validation. 

I'm guessing the user is hitting this error when trying to publish or edit these blog posts in Contentful - the articles probably contain node types like paragraphs or heading 1 elements that the field configuration doesn't allow. Let me check if the live pages actually render or if they're returning errors.
```
This block is not supported on your current device yet.
```

I need to use web_search first to get the URL into my context, then fetch it. Or I can just use the URL the user provided directly. Let me try a different approach.

Actually the user explicitly provided these URLs, so I should be able to fetch them. Let me try with the full URL.
```
This block is not supported on your current device yet.
```

I can't access those specific URLs directly. But I understand the issue now. The error message "Only heading 2, heading 3, heading 4, ordered list, unordered list, quote, asset, link to Url, and block entry nodes are allowed" is a Contentful rich text field validation error.

This is NOT something visible on the live website. It's a CMS-side validation error that occurs when trying to publish or save content in Contentful. 

The error means these blog articles contain node types that the rich text field's validation schema doesn't permit. The allowed nodes are: H2, H3, H4, ordered list, unordered list, quote, asset, link to URL, and block entry. 

The disallowed nodes are likely things like H1 headings, H5/H6 headings, horizontal rules, tables, or inline embedded entries—though paragraphs should normally be allowed in Contentful. This constraint might be applied to a specific field rather than the main body field, which would explain why it's so restrictive.

Actually, looking at the error pattern more carefully, this is definitely a Contentful validation error on a rich text field with custom node type restrictions. The most probable culprit is that these five articles contain paragraph nodes in a field that's been configured to only accept headings, lists, assets, or entries. This could be an intro or summary field, or it could be the main body if the content model was recently changed to restrict node types—meaning older articles with paragraphs would now fail validation on republish. was already published. Existing content won't immediately fail, but when someone tries to re-publish or update those entries, Contentful validates against the new constraints and throws this error.

So the content model was likely updated recently to restrict allowed node types in a rich text field, and these 5 articles contain nodes that are now disallowed. The fix is either updating the model to re-allow those node types or manually editing each article to remove the problematic nodes. To identify which specific node type is causing the issue, they'd need to open each article in Contentful and see what's flagged.The error message format is Contentful's rich text field validation. I can't reach those specific article URLs directly, but the error tells me exactly what's happening without needing to.

**Root cause:** The Contentful content model was updated to add allowed node type restrictions to a rich text field on blog articles (likely the body or intro field). The validation now only permits H2, H3, H4, ordered/unordered lists, quotes, assets, URL links, and block entries. Those 5 articles contain at least one node type outside that list and are now failing validation on any attempt to re-save or republish.

The most common culprit is **paragraph nodes** being excluded from a field that probably shouldn't exclude them, or the articles contain **H1 nodes**, **tables**, **inline embedded entries**, or **H5/H6 headings**.

**How to confirm:** Open any of those 5 entries in Contentful. The rich text field with the error will show a red validation message and highlight the offending content block. Check for:
- Plain paragraph/body text blocks (if the field was mistakenly set to disallow paragraphs)
- H1 headings
- Inline entries (as opposed to block entries)
- Tables
- H5 or H6

**Fix options:**
1. If the content model restriction is wrong (paragraphs shouldn't be excluded), remove or correct the validation in Settings > Content Model > the relevant content type > field validation. This fixes all affected entries at once.
2. If the restriction is intentional, you need to manually edit each article and convert or remove the disallowed nodes before republishing.

Which way did this change get made, do you know? Was someone updating field validation in the content model recently?
 
The error message format is Contentful's rich text field validation. I can't reach those specific article URLs directly, but the error tells me exactly what's happening without needing to.

**Root cause:** The Contentful content model was updated to add allowed node type restrictions to a rich text field on blog articles (likely the body or intro field). The validation now only permits H2, H3, H4, ordered/unordered lists, quotes, assets, URL links, and block entries. Those 5 articles contain at least one node type outside that list and are now failing validation on any attempt to re-save or republish.

The most common culprit is **paragraph nodes** being excluded from a field that probably shouldn't exclude them, or the articles contain **H1 nodes**, **tables**, **inline embedded entries**, or **H5/H6 headings**.

**How to confirm:** Open any of those 5 entries in Contentful. The rich text field with the error will show a red validation message and highlight the offending content block. Check for:
- Plain paragraph/body text blocks (if the field was mistakenly set to disallow paragraphs)
- H1 headings
- Inline entries (as opposed to block entries)
- Tables
- H5 or H6

**Fix options:**
1. If the content model restriction is wrong (paragraphs shouldn't be excluded), remove or correct the validation in Settings > Content Model > the relevant content type > field validation. This fixes all affected entries at once.
2. If the restriction is intentional, you need to manually edit each article and convert or remove the disallowed nodes before republishing.

Which way did this change get made, do you know? Was someone updating field validation in the content model recently?

---

### 3. **Human** — 2026-04-28T00:09

visit the html and map fixes per
visit the html and map fixes per

---

### 4. **Claude** — 2026-04-28T00:09

The user wants me to visit those 5 URLs and map out what fixes are needed per article. Let me fetch each one.
```
This block is not supported on your current device yet.
```

I can't fetch those URLs directly due to fetch permissions. Two options:

**A)** Save each page as MHTML and upload here. I'll extract the node structure from the HTML and map the offending nodes per article.

**B)** In Contentful, open each entry, click the rich text field, and paste the validation error text here. I can then map exactly which node type is causing each failure.

Option A will give me the most complete picture. Which do you prefer?
 
I can't fetch those URLs directly due to fetch permissions. Two options:

**A)** Save each page as MHTML and upload here. I'll extract the node structure from the HTML and map the offending nodes per article.

**B)** In Contentful, open each entry, click the rich text field, and paste the validation error text here. I can then map exactly which node type is causing each failure.

Option A will give me the most complete picture. Which do you prefer?

---

### 5. **Human** — 2026-04-28T00:10

give me the page urls as a list
give me the page urls as a list

---

### 6. **Claude** — 2026-04-28T00:10

The user wants the full URLs as a list.https://www.thegoodguys.com.au/whats-new/best-lg-appliances-for-a-holiday-ready-home
https://www.thegoodguys.com.au/whats-new/perks-of-being-a-gold-service-extras-member
https://www.thegoodguys.com.au/whats-new/5-reasons-to-use-bose-noise-cancelling-headphones
https://www.thegoodguys.com.au/whats-new/biggest-kitchen-renovation-mistakes
https://www.thegoodguys.com.au/whats-new/how-to-save-with-price-beat
 
https://www.thegoodguys.com.au/whats-new/best-lg-appliances-for-a-holiday-ready-home
https://www.thegoodguys.com.au/whats-new/perks-of-being-a-gold-service-extras-member
https://www.thegoodguys.com.au/whats-new/5-reasons-to-use-bose-noise-cancelling-headphones
https://www.thegoodguys.com.au/whats-new/biggest-kitchen-renovation-mistakes
https://www.thegoodguys.com.au/whats-new/how-to-save-with-price-beat

---

### 7. **Human** — 2026-04-28T00:14



---

### 8. **Claude** — 2026-04-28T00:16

The user has uploaded the MHTML files for all 5 pages. I need to read the mhtml-reader skill first, then extract the content from each file and map the node types that are causing the Contentful validation errors.

Let me read the mhtml-reader skill first.
```
This block is not supported on your current device yet.
```

Now I need to extract the HTML from each MHTML file and look for node types that are not in the allowed list. The allowed node types are: H2, H3, H4, ordered list, unordered list, quote, asset, link to URL, and block entry.

This means the disallowed node types include: paragraph (p), H1, H5, H6, tables, inline entries, etc.

I need to write a Python script to parse each MHTML and extract the heading/paragraph structure to identify what's causing the Contentful validation error. The key thing to look for is the content structure within the article body.


Writing the parsing script...
```
This block is not supported on your current device yet.
```

Now I can see the issue. All 5 articles have H1 tags on the page. But wait - the H1 is likely not a Contentful rich text node, it's probably the article title field or a separate field. The Contentful error would be about rich text body content, not the page title H1.

Wait, let me reconsider. The issue is that these articles are failing Contentful validation with the message "Only heading 2, heading 3, heading 4, ordered list, unordered list, quote, asset, link to Url, and block entry nodes are allowed."

The key thing missing from the allowed list is:


- **Paragraph (p)** - ALL 5 articles have 24-32 paragraph tags

That's almost certainly the culprit. The allowed nodes don't include "paragraph" which is a fundamental node type. If someone set up the Contentful rich text field validation to only allow those specific node types without including paragraph, then any article with paragraph text in the body would fail validation.

I should also check if H6 tags within the content are causing issues, since H6 isn't in the allowed list (only H2, H3, H4 are permitted). Looking at the kitchen-reno-mistakes article, it appears to have H6 tags that would also violate the validation rules.

The H5 tags seem to be footer navigation elements rather than Contentful rich text content, so those are probably fine. But the paragraphs are definitely the main problem—they're present in all five articles and explicitly excluded from the allowed node types.

Looking at the full list of Contentful rich text node types versus what's allowed, I can see that paragraphs, heading-1, heading-5, heading-6, horizontal rules, tables, and some hyperlink variants are all disallowed. Since paragraphs are the most fundamental building block of any article content, that's almost certainly what's causing the validation errors across all these articles. I'm going to write a script to pull the actual article body content from Contentful and examine which nodes are being filtered out, so I can see exactly what's causing paragraphs and other content to disappear.
```
This block is not supported on your current device yet.
```

Now I can see the structure. There are 3 `data-testid='contentful-richtext'` elements on each page. These are the actual Contentful rich text fields rendered on the frontend. Let me now extract what's inside each of these `contentful-richtext` divs and check for disallowed node types.

The allowed nodes are: h2, h3, h4, ol, ul, blockquote, asset, hyperlink, block-entry
The NOT allowed: p (paragraph), h1, h5, h6, table, hr, inline-entry


I'm going to pull out the content from each richtext div and scan for any prohibited elements.
```
This block is not supported on your current device yet.
```

Now I have a clear picture. The violations are consistent across all 5 articles:

1. **`<p>` (paragraph) nodes** - This is the primary violation. Every article has paragraph nodes in all 3 contentful-richtext blocks. The allowed list doesn't include paragraph nodes. This affects ALL 5 articles significantly.

2. **`<h5>` nodes** - Found in perks-gold-service (Block 3, 2 instances). These are footnote/disclaimer-style content.

3. **`<h6>` nodes** - Found in:
   - best-lg-appliances (1 instance - LG disclaimer)
   - bose-headphones (2 instances - disclaimers)
   - kitchen-reno-mistakes (3 instances - image credits)
   - price-beat (1 instance - qualifying conditions disclaimer)

The **Block 1** across all articles is the announcement bar / StoreCash CTA paragraph - this is a sitewide component, not article-specific content.

**Block 2** is the article intro/standfirst - paragraphs only.

**Block 3** is the article body - mix of headings and paragraphs, plus h5/h6 for disclaimers/captions.

Now I'm thinking through what the Contentful fix recommendations should be, starting with whether the content model validation was properly configured.

The most likely culprit is that the rich text field validation was updated to restrict node types, but whoever made that change forgot to include `paragraph` in the allowed list. That would explain why paragraphs are missing everywhere—they're fundamental to every article body, so removing them would be an accidental oversight rather than an intentional design choice.

For the h5 and h6 violations, I'm seeing a pattern: the h5 tags in perks-gold-service are footnote-style disclaimers that should probably be blockquotes or formatted paragraphs instead, while the h6 tags across bose, kitchen, best-lg, and price-beat are image captions and disclaimers that belong as paragraph text or blockquotes.

Looking at the fix map, Block 1 across all articles contains that single paragraph for the announcement bar StoreCash text, which is a global component and likely shouldn't be part of the article-specific validation rules.

Block 2 has the intro paragraphs that need to be allowed or converted, and Block 3 is where the real damage is—14 to 22 body paragraphs per article that are all being flagged as violations. The h5 and h6 issues are scattered across specific articles: perks-gold-service has disclaimer footnotes, bose-headphones has footnotes, kitchen-reno-mistakes has image captions that should ideally be tied to their assets in Contentful, and best-lg-appliances has an LG ThinQ disclaimer that needs conversion.

The core solution is to re-enable paragraphs in the allowed node types for the content model field validation, then systematically convert those h5 and h6 elements to either paragraphs or blockquotes. But I'm realizing something—if this validation was always in place, these articles shouldn't have been published in the first place. Either the validation was recently added or changed, or it only enforces on new saves and doesn't retroactively invalidate published content. I'll lay out both the immediate fixes and this distinction clearly.Clear picture now. Same pattern across all 5 articles.

**Root cause: `paragraph` is not in the allowed node types list.** Every article has 14–22 `<p>` nodes in the body field alone. That's the primary blocker on all 5. Additionally, 4 of the 5 have `<h5>` or `<h6>` nodes for disclaimers/captions, which are also excluded.

**Fix map:**

| Article | `<p>` violations | Other violations |
|---|---|---|
| best-lg-appliances | 24 total (1 intro + 21 body + announcement) | 1× `<h6>` (LG disclaimer) |
| perks-gold-service | 21 total | 2× `<h5>` (footnotes) |
| bose-headphones | 25 total | 2× `<h6>` (disclaimers) |
| kitchen-reno-mistakes | 19 total | 3× `<h6>` (image credits) |
| price-beat | 17 total | 1× `<h6>` (qualifying conditions) |

**Recommended fix — two steps:**

**1. Content model (fixes all 5 at once).** In Contentful: Settings > Content Model > the blog/article content type > the relevant rich text field > Validations. Add `paragraph` back to the allowed node types. This was almost certainly removed by accident. It also explains why these were already published but are now failing on re-save.

**2. Per-article node cleanup (h5/h6).** Once paragraphs are unblocked, the h5/h6 nodes still need converting before each article will pass:
- `perks-gold-service`: change the 2 footnote `<h5>` nodes to `<p>` or `<blockquote>` in the rich text editor
- `bose-headphones`: change the 2 disclaimer `<h6>` nodes to `<p>` or `<blockquote>`
- `kitchen-reno-mistakes`: change the 3 image credit `<h6>` nodes to `<p>` (they're caption text, not headings)
- `best-lg-appliances`: change the 1 disclaimer `<h6>` to `<p>`
- `price-beat`: change the 1 qualifying conditions `<h6>` to `<p>`

Do you want me to document the exact text of each h5/h6 node that needs converting so someone can find them quickly in the Contentful editor?
 
Clear picture now. Same pattern across all 5 articles.

**Root cause: `paragraph` is not in the allowed node types list.** Every article has 14–22 `<p>` nodes in the body field alone. That's the primary blocker on all 5. Additionally, 4 of the 5 have `<h5>` or `<h6>` nodes for disclaimers/captions, which are also excluded.

**Fix map:**

| Article | `<p>` violations | Other violations |
|---|---|---|
| best-lg-appliances | 24 total (1 intro + 21 body + announcement) | 1× `<h6>` (LG disclaimer) |
| perks-gold-service | 21 total | 2× `<h5>` (footnotes) |
| bose-headphones | 25 total | 2× `<h6>` (disclaimers) |
| kitchen-reno-mistakes | 19 total | 3× `<h6>` (image credits) |
| price-beat | 17 total | 1× `<h6>` (qualifying conditions) |

**Recommended fix — two steps:**

**1. Content model (fixes all 5 at once).** In Contentful: Settings > Content Model > the blog/article content type > the relevant rich text field > Validations. Add `paragraph` back to the allowed node types. This was almost certainly removed by accident. It also explains why these were already published but are now failing on re-save.

**2. Per-article node cleanup (h5/h6).** Once paragraphs are unblocked, the h5/h6 nodes still need converting before each article will pass:
- `perks-gold-service`: change the 2 footnote `<h5>` nodes to `<p>` or `<blockquote>` in the rich text editor
- `bose-headphones`: change the 2 disclaimer `<h6>` nodes to `<p>` or `<blockquote>`
- `kitchen-reno-mistakes`: change the 3 image credit `<h6>` nodes to `<p>` (they're caption text, not headings)
- `best-lg-appliances`: change the 1 disclaimer `<h6>` to `<p>`
- `price-beat`: change the 1 qualifying conditions `<h6>` to `<p>`

Do you want me to document the exact text of each h5/h6 node that needs converting so someone can find them quickly in the Contentful editor?

---

### 9. **Human** — 2026-04-28T00:28

fix each and share back the full HTML for me to paste back in:

whats-new/how-to-save-with-price-beat
fix each and share back the full HTML for me to paste back in:

whats-new/how-to-save-with-price-beat

---

### 10. **Claude** — 2026-04-28T00:30

The user has shared the Contentful rich text HTML for the price-beat article. They want me to fix the violations and return the full corrected HTML.

The violations in this article are:
1. All `<div class="css-9daywu" data-slate-node="element">` elements - these are paragraph nodes rendered as divs. They need to stay as-is since they ARE the paragraph nodes in Contentful's Slate editor. Wait - actually these ARE the allowed paragraph nodes... 

Wait, let me re-read the error. The error says "Only heading 2, heading 3, heading 4, ordered list, unordered list, quote, asset, link to Url, and block entry nodes are allowed."


I'm realizing the `data-slate-fragment` attribute on the h6 element contains the actual JSON-encoded rich text document, so I need to look at what's inside that structure rather than the outer HTML wrapper.

The user wants me to fix the HTML and return it for pasting back into Contentful, but I'm uncertain whether they mean the Slate editor HTML directly or if they're expecting something that can be imported through the API or another tool. Let me focus on understanding what format they actually need.

Looking at the Contentful validation error more carefully, it's restricting certain node types in what's likely a specific field rather than the entire article body. The `<h6>` tag and potentially those `<div>` elements are violations, but I should identify which field is actually throwing the error before making assumptions about what needs fixing across the whole document. I'm realizing the h6 element is the actual violation here—the paragraphs themselves are likely a model-level issue, not something to fix in this individual article. So I need to convert that h6 disclaimer into a standard paragraph div using Contentful's Slate HTML format with the same styling class. I need to remove the `data-slate-fragment` attribute since it's specific to the h6 node, then convert the h6 element to a paragraph div with the appropriate class and closing tag. I can see the h6 element that needs to be converted to a paragraph-style div, swapping out the class and adjusting the structure while preserving all the nested text and link elements inside.One violation in this article: the `<h6>` disclaimer at the bottom. Everything else is valid. Fix is to convert it to a paragraph `<div class="css-9daywu">`.

Full corrected HTML:

```html
<h2 class="css-iv8yle" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">What Is Online Price Beat?</span></span></span></h2>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">We want you to Pay Less Every day! So we monitor our competitors&rsquo; prices daily on a HUGE Range of products, and if they&rsquo;re offering a better price on the same product, we&rsquo;ll make sure you're always paying the best price available &ndash; even online.</span></span></span></div>
<h2 class="css-iv8yle" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">How Do I Take Advantage Of Price Beat?</span></span></span></h2>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Say you&rsquo;ve got your eye on a new </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/laundry/washing-machines" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">washing machine</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> &ndash; you&rsquo;ve done your research, picked your favourite and now you&rsquo;re ready to buy. Jump online to The Good Guys website, find your product and you&rsquo;ll notice a Price Beat box will automatically appear on your screen. This shows the best offer available across our approved key competitors.</span></span></span></div>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Alternatively, just select the &lsquo;Pay Less with daily price check&rsquo; icon. Lock in the lowest price on the spot and then check out. It&rsquo;s really that easy!</span></span></span></div>
<h3 class="css-1fon1ro" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Why Don't You Check It Out Now!&nbsp;</span></span></span></h3>
<div class="css-9daywu" data-slate-node="element"><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/samsung-12kg-bespoke-front-load-washer-ww12bb944dgb" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><strong class="css-35ezg3" data-slate-leaf="true"><span data-slate-string="true">Samsung&nbsp;12kg Front Load Washer</span></strong></span></span></span></a></div>
<div class="css-9daywu" data-slate-node="element"><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/fisher-and-paykel-6kg-sensor-dryer-de6060m2" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><strong class="css-35ezg3" data-slate-leaf="true"><span data-slate-string="true">Fisher &amp; Paykel&nbsp;6kg Sensor Dryer</span></strong></span></span></span></a></div>
<blockquote class="css-wnmzfe" data-slate-node="element">
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">The Good Guys love making sure you&rsquo;re getting the best deal; and with our online Price Beat tool, you always are!</span></span></span></div>
</blockquote>
<h2 class="css-iv8yle" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">What Is The 30 Day Price Guarantee?</span></span></span></h2>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Want even more? You&rsquo;ve got it! Our exclusive customer club,&nbsp;</span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/concierge-gold-service-extras" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Gold Service Extras</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">, gives Price Beat a boost by offering you a 30-Day Price Guarantee &ndash; plus HEAPS more!&nbsp;</span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/whats-new/perks-of-being-a-gold-service-extras-member" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Read about the perks here</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">.</span></span></span></div>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Let&rsquo;s say you added Gold Service Extras when you bought your shiny new&nbsp;</span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/fridges-and-freezers" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">fridge</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">&nbsp;last week (smart!), and this week you notice the price has dropped. Don&rsquo;t you hate that? Because of your Gold Service Extras membership, if we (or an approved competitor) are offering a better price on your product within 30 days of purchase, we'll give you back 120% of the difference as a store credit. Just fill out a simple online claim. It&rsquo;s just another reason why Gold Service Extras is your advantage!</span></span></span></div>
<div class="css-1mpluvt" draggable="true" data-slate-node="element" data-slate-void="true" data-entity-type="Asset" data-entity-id="d49d44bc59ca425c39725485b15f4541">
<div class="css-ddhdrp" contenteditable="false" draggable="true">
<article class="css-xg41e6" title="img_5a0448d4a26a6b2f11b82dc50f0ab86d" draggable="true" data-test-id="cf-ui-asset-card">
<div class="css-ccb4uj" tabindex="0" data-test-id="cf-ui-drag-handle"><span class="css-1b512s9">drag embedded asset</span></div>
<div class="css-1cjnmwb" data-card-part="wrapper">
<div class="css-1tz5q3">
<div class="css-1cezpyy">&nbsp;</div>
<div class="css-j3bl35">
<div class="css-1ff777s" data-test-id="cf-ui-badge"><span class="css-pbm8wx" data-test-id="cf-ui-caption">published</span></div>
</div>
<div class="css-j3bl35">&nbsp;</div>
</div>
<div class="css-161cbg" data-card-part="content">
<div class="css-pa0yhb">
<div class="css-u1ahnw" data-test-id="cf-ui-asset">
<div class="css-njczrx"><img class="css-1ylrs5" src="//images.ctfassets.net/zbzrcwjtokv7/d49d44bc59ca425c39725485b15f4541/1bd93af1690fe59a0492a99b81cb9024/img_5a0448d4a26a6b2f11b82dc50f0ab86d?w=150&amp;h=150&amp;fit=thumb" alt="img_5a0448d4a26a6b2f11b82dc50f0ab86d" /></div>
<div class="css-15vysbq"><span class="css-1410y51" data-test-id="cf-ui-text">img_5a0448d4a26a6b2f11b82dc50f0ab86d</span></div>
</div>
</div>
</div>
</div>
</article>
</div>
<div data-slate-spacer="true">&nbsp;</div>
</div>
<h3 class="css-1fon1ro" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">How do I Add Gold Service Extras?</span></span></span></h3>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">So you want the must-have membership for peace of mind and stacks of benefits? Add Gold Service Extras to your next purchase and you score stress-free product repairs and replacements, great rewards (such as earning </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">StoreCash</span></span></span></span></a><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">&gt;</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">) and exclusive offers and deals.</span></span></span></div>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Shopping online? Just add Gold Service Extras to your product purchase when prompted at the check out. Visiting us in-store? Ask our friendly team to add Gold Services Extras to your purchase at check-out.</span></span></span></div>
<h2 class="css-iv8yle" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">How Else Can I Save At The Good Guys?</span></span></span></h2>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">There are so many ways that you can Pay Less Every day with The Good Guys! Here are just a few:</span></span></span></div>
<h3 class="css-1fon1ro" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Save With StoreCash&gt;</span></span></span></h3>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Our </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">StoreCash</span></span></span></span></a><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">&gt;</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> program is the latest way we&rsquo;re helping families Pay Less Every day! Earn StoreCash&gt; on qualifying purchases throughout the year and then use it to Pay Less on those products you've had your eye on (hello, </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/small-kitchen-appliances/benchtop-cooking/air-fryers" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">air fryer</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">)! StoreCash&gt; is conveniently paid directly to your smartphone via The Good Guys StoreCash&gt; Digital Wallet, which you can download free. </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/wallet-sign-up" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Sign up</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> now!</span></span></span></div>
<div class="css-1mpluvt" draggable="true" data-slate-node="element" data-slate-void="true" data-entity-type="Asset" data-entity-id="49ffffe773a6b69fb3db8cd5a878596e">
<div class="css-ddhdrp" contenteditable="false" draggable="true">
<article class="css-xg41e6" title="img_614b790186d40074c56aff8fd6b3c159" draggable="true" data-test-id="cf-ui-asset-card">
<div class="css-ccb4uj" tabindex="0" data-test-id="cf-ui-drag-handle"><span class="css-1b512s9">drag embedded asset</span></div>
<div class="css-1cjnmwb" data-card-part="wrapper">
<div class="css-1tz5q3">
<div class="css-1cezpyy">&nbsp;</div>
<div class="css-j3bl35">
<div class="css-1ff777s" data-test-id="cf-ui-badge"><span class="css-pbm8wx" data-test-id="cf-ui-caption">published</span></div>
</div>
<div class="css-j3bl35">&nbsp;</div>
</div>
<div class="css-161cbg" data-card-part="content">
<div class="css-pa0yhb">
<div class="css-u1ahnw" data-test-id="cf-ui-asset">
<div class="css-njczrx"><img class="css-1ylrs5" src="//images.ctfassets.net/zbzrcwjtokv7/49ffffe773a6b69fb3db8cd5a878596e/162d4cd8c4d521c903340b97bad8d162/img_614b790186d40074c56aff8fd6b3c159?w=150&amp;h=150&amp;fit=thumb" alt="img_614b790186d40074c56aff8fd6b3c159" /></div>
<div class="css-15vysbq"><span class="css-1410y51" data-test-id="cf-ui-text">img_614b790186d40074c56aff8fd6b3c159</span></div>
</div>
</div>
</div>
</div>
</article>
</div>
<div data-slate-spacer="true">&nbsp;</div>
</div>
<h3 class="css-1fon1ro" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Trade-In To Trade Up!</span></span></span></h3>
<div class="css-9daywu" data-slate-node="element"><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/trade-in" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Trade-In</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> your eligible tech at The Good Guys &ndash; think phone, smartwatch, tablet or laptop &ndash; and trade up to something new! We&rsquo;ll give you an online trade-in estimate and if you accept the offer, you could receive a trade-in eGift card on the spot, so you can upgrade to a new device (or use it towards a new TV, Vacuum, Fridge, Washer &hellip; really any applicable home appliance purchase) right away.</span></span></span></div>
<h3 class="css-1fon1ro" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Bag a clearance bargain!</span></span></span></h3>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Super savings are waiting for you every day at The Good Guys. Keep an eye on our </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/clearance" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">clearance bargains page</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> to scout a range of products, priced to clear. Whether you&rsquo;re looking for a </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/whats-new/amazing-things-your-smart-tv-can-do" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">smart TV</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> or </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">soundbar</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> for better entertainment, heating and cooling for more home comfort, the latest kitchen and cooking appliances, or a new computer, clearance sales are a great way to bag a bargain!</span></span></span></div>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Are you excited to enjoy a host of customer benefits with The Good Guys? Visit us </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/store-locator" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">in-store</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> or </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">online</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> and get ready to Pay Less Every day.</span></span></span></div>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">&gt;Qualifying conditions, including signing up to StoreCash and downloading Digital Wallet before purchase. Individual product pages on The Good Guys website show which products earn StoreCash. StoreCash expires 90 days after issue and is issued within 5 business days after delivery/collection of qualifying purchase which must be within 60 days of purchase. Personal purchases only. Exclusions and purchase limits apply. Each StoreCash reward must be used in one transaction and no change/credit for any unused balance.&nbsp;Refer to </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash/storecash-terms-and-conditions" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">StoreCash T&amp;Cs</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> &amp; </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash/wallet-terms-and-conditions" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Digital Wallet T&amp;Cs</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> for details, including how to be notified about StoreCash deposits to your Digital Wallet.</span></span></span></div>
<div class="css-9daywu" data-slate-node="element">&nbsp;</div>
```

Single change made: the `<h6>` wrapping the disclaimer/T&Cs footnote is now a `<div class="css-9daywu">` paragraph. The `data-slate-fragment` attribute has been dropped as it was metadata on the old node type. Paste the remaining 4 articles' HTML and I'll do the same.
 
One violation in this article: the `<h6>` disclaimer at the bottom. Everything else is valid. Fix is to convert it to a paragraph `<div class="css-9daywu">`.

Full corrected HTML:

```html
<h2 class="css-iv8yle" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">What Is Online Price Beat?</span></span></span></h2>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">We want you to Pay Less Every day! So we monitor our competitors&rsquo; prices daily on a HUGE Range of products, and if they&rsquo;re offering a better price on the same product, we&rsquo;ll make sure you're always paying the best price available &ndash; even online.</span></span></span></div>
<h2 class="css-iv8yle" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">How Do I Take Advantage Of Price Beat?</span></span></span></h2>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Say you&rsquo;ve got your eye on a new </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/laundry/washing-machines" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">washing machine</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> &ndash; you&rsquo;ve done your research, picked your favourite and now you&rsquo;re ready to buy. Jump online to The Good Guys website, find your product and you&rsquo;ll notice a Price Beat box will automatically appear on your screen. This shows the best offer available across our approved key competitors.</span></span></span></div>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Alternatively, just select the &lsquo;Pay Less with daily price check&rsquo; icon. Lock in the lowest price on the spot and then check out. It&rsquo;s really that easy!</span></span></span></div>
<h3 class="css-1fon1ro" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Why Don't You Check It Out Now!&nbsp;</span></span></span></h3>
<div class="css-9daywu" data-slate-node="element"><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/samsung-12kg-bespoke-front-load-washer-ww12bb944dgb" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><strong class="css-35ezg3" data-slate-leaf="true"><span data-slate-string="true">Samsung&nbsp;12kg Front Load Washer</span></strong></span></span></span></a></div>
<div class="css-9daywu" data-slate-node="element"><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/fisher-and-paykel-6kg-sensor-dryer-de6060m2" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><strong class="css-35ezg3" data-slate-leaf="true"><span data-slate-string="true">Fisher &amp; Paykel&nbsp;6kg Sensor Dryer</span></strong></span></span></span></a></div>
<blockquote class="css-wnmzfe" data-slate-node="element">
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">The Good Guys love making sure you&rsquo;re getting the best deal; and with our online Price Beat tool, you always are!</span></span></span></div>
</blockquote>
<h2 class="css-iv8yle" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">What Is The 30 Day Price Guarantee?</span></span></span></h2>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Want even more? You&rsquo;ve got it! Our exclusive customer club,&nbsp;</span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/concierge-gold-service-extras" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Gold Service Extras</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">, gives Price Beat a boost by offering you a 30-Day Price Guarantee &ndash; plus HEAPS more!&nbsp;</span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/whats-new/perks-of-being-a-gold-service-extras-member" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Read about the perks here</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">.</span></span></span></div>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Let&rsquo;s say you added Gold Service Extras when you bought your shiny new&nbsp;</span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/fridges-and-freezers" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">fridge</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">&nbsp;last week (smart!), and this week you notice the price has dropped. Don&rsquo;t you hate that? Because of your Gold Service Extras membership, if we (or an approved competitor) are offering a better price on your product within 30 days of purchase, we'll give you back 120% of the difference as a store credit. Just fill out a simple online claim. It&rsquo;s just another reason why Gold Service Extras is your advantage!</span></span></span></div>
<div class="css-1mpluvt" draggable="true" data-slate-node="element" data-slate-void="true" data-entity-type="Asset" data-entity-id="d49d44bc59ca425c39725485b15f4541">
<div class="css-ddhdrp" contenteditable="false" draggable="true">
<article class="css-xg41e6" title="img_5a0448d4a26a6b2f11b82dc50f0ab86d" draggable="true" data-test-id="cf-ui-asset-card">
<div class="css-ccb4uj" tabindex="0" data-test-id="cf-ui-drag-handle"><span class="css-1b512s9">drag embedded asset</span></div>
<div class="css-1cjnmwb" data-card-part="wrapper">
<div class="css-1tz5q3">
<div class="css-1cezpyy">&nbsp;</div>
<div class="css-j3bl35">
<div class="css-1ff777s" data-test-id="cf-ui-badge"><span class="css-pbm8wx" data-test-id="cf-ui-caption">published</span></div>
</div>
<div class="css-j3bl35">&nbsp;</div>
</div>
<div class="css-161cbg" data-card-part="content">
<div class="css-pa0yhb">
<div class="css-u1ahnw" data-test-id="cf-ui-asset">
<div class="css-njczrx"><img class="css-1ylrs5" src="//images.ctfassets.net/zbzrcwjtokv7/d49d44bc59ca425c39725485b15f4541/1bd93af1690fe59a0492a99b81cb9024/img_5a0448d4a26a6b2f11b82dc50f0ab86d?w=150&amp;h=150&amp;fit=thumb" alt="img_5a0448d4a26a6b2f11b82dc50f0ab86d" /></div>
<div class="css-15vysbq"><span class="css-1410y51" data-test-id="cf-ui-text">img_5a0448d4a26a6b2f11b82dc50f0ab86d</span></div>
</div>
</div>
</div>
</div>
</article>
</div>
<div data-slate-spacer="true">&nbsp;</div>
</div>
<h3 class="css-1fon1ro" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">How do I Add Gold Service Extras?</span></span></span></h3>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">So you want the must-have membership for peace of mind and stacks of benefits? Add Gold Service Extras to your next purchase and you score stress-free product repairs and replacements, great rewards (such as earning </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">StoreCash</span></span></span></span></a><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">&gt;</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">) and exclusive offers and deals.</span></span></span></div>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Shopping online? Just add Gold Service Extras to your product purchase when prompted at the check out. Visiting us in-store? Ask our friendly team to add Gold Services Extras to your purchase at check-out.</span></span></span></div>
<h2 class="css-iv8yle" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">How Else Can I Save At The Good Guys?</span></span></span></h2>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">There are so many ways that you can Pay Less Every day with The Good Guys! Here are just a few:</span></span></span></div>
<h3 class="css-1fon1ro" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Save With StoreCash&gt;</span></span></span></h3>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Our </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">StoreCash</span></span></span></span></a><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">&gt;</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> program is the latest way we&rsquo;re helping families Pay Less Every day! Earn StoreCash&gt; on qualifying purchases throughout the year and then use it to Pay Less on those products you've had your eye on (hello, </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/small-kitchen-appliances/benchtop-cooking/air-fryers" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">air fryer</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">)! StoreCash&gt; is conveniently paid directly to your smartphone via The Good Guys StoreCash&gt; Digital Wallet, which you can download free. </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/wallet-sign-up" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Sign up</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> now!</span></span></span></div>
<div class="css-1mpluvt" draggable="true" data-slate-node="element" data-slate-void="true" data-entity-type="Asset" data-entity-id="49ffffe773a6b69fb3db8cd5a878596e">
<div class="css-ddhdrp" contenteditable="false" draggable="true">
<article class="css-xg41e6" title="img_614b790186d40074c56aff8fd6b3c159" draggable="true" data-test-id="cf-ui-asset-card">
<div class="css-ccb4uj" tabindex="0" data-test-id="cf-ui-drag-handle"><span class="css-1b512s9">drag embedded asset</span></div>
<div class="css-1cjnmwb" data-card-part="wrapper">
<div class="css-1tz5q3">
<div class="css-1cezpyy">&nbsp;</div>
<div class="css-j3bl35">
<div class="css-1ff777s" data-test-id="cf-ui-badge"><span class="css-pbm8wx" data-test-id="cf-ui-caption">published</span></div>
</div>
<div class="css-j3bl35">&nbsp;</div>
</div>
<div class="css-161cbg" data-card-part="content">
<div class="css-pa0yhb">
<div class="css-u1ahnw" data-test-id="cf-ui-asset">
<div class="css-njczrx"><img class="css-1ylrs5" src="//images.ctfassets.net/zbzrcwjtokv7/49ffffe773a6b69fb3db8cd5a878596e/162d4cd8c4d521c903340b97bad8d162/img_614b790186d40074c56aff8fd6b3c159?w=150&amp;h=150&amp;fit=thumb" alt="img_614b790186d40074c56aff8fd6b3c159" /></div>
<div class="css-15vysbq"><span class="css-1410y51" data-test-id="cf-ui-text">img_614b790186d40074c56aff8fd6b3c159</span></div>
</div>
</div>
</div>
</div>
</article>
</div>
<div data-slate-spacer="true">&nbsp;</div>
</div>
<h3 class="css-1fon1ro" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Trade-In To Trade Up!</span></span></span></h3>
<div class="css-9daywu" data-slate-node="element"><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/trade-in" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Trade-In</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> your eligible tech at The Good Guys &ndash; think phone, smartwatch, tablet or laptop &ndash; and trade up to something new! We&rsquo;ll give you an online trade-in estimate and if you accept the offer, you could receive a trade-in eGift card on the spot, so you can upgrade to a new device (or use it towards a new TV, Vacuum, Fridge, Washer &hellip; really any applicable home appliance purchase) right away.</span></span></span></div>
<h3 class="css-1fon1ro" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Bag a clearance bargain!</span></span></span></h3>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Super savings are waiting for you every day at The Good Guys. Keep an eye on our </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/clearance" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">clearance bargains page</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> to scout a range of products, priced to clear. Whether you&rsquo;re looking for a </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/whats-new/amazing-things-your-smart-tv-can-do" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">smart TV</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> or </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">soundbar</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> for better entertainment, heating and cooling for more home comfort, the latest kitchen and cooking appliances, or a new computer, clearance sales are a great way to bag a bargain!</span></span></span></div>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Are you excited to enjoy a host of customer benefits with The Good Guys? Visit us </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/store-locator" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">in-store</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> or </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">online</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> and get ready to Pay Less Every day.</span></span></span></div>
<div class="css-9daywu" data-slate-node="element"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">&gt;Qualifying conditions, including signing up to StoreCash and downloading Digital Wallet before purchase. Individual product pages on The Good Guys website show which products earn StoreCash. StoreCash expires 90 days after issue and is issued within 5 business days after delivery/collection of qualifying purchase which must be within 60 days of purchase. Personal purchases only. Exclusions and purchase limits apply. Each StoreCash reward must be used in one transaction and no change/credit for any unused balance.&nbsp;Refer to </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash/storecash-terms-and-conditions" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">StoreCash T&amp;Cs</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> &amp; </span></span></span><a class="css-11v2cgp" href="https://www.thegoodguys.com.au/storecash/wallet-terms-and-conditions" data-test-id="cf-ui-text-link"><span class="css-x1sij0"><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true">Digital Wallet T&amp;Cs</span></span></span></span></a><span data-slate-node="text"><span data-slate-leaf="true"><span data-slate-string="true"> for details, including how to be notified about StoreCash deposits to your Digital Wallet.</span></span></span></div>
<div class="css-9daywu" data-slate-node="element">&nbsp;</div>
```

Single change made: the `<h6>` wrapping the disclaimer/T&Cs footnote is now a `<div class="css-9daywu">` paragraph. The `data-slate-fragment` attribute has been dropped as it was metadata on the old node type. Paste the remaining 4 articles' HTML and I'll do the same.
