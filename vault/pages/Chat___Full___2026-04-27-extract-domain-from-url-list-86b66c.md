---
title: Extract domain from URL list (full)
parent: Chat/Light/2026-04-27-extract-domain-from-url-list-86b66c
uuid: 86b66c66-402f-4ea3-9ad2-6f953baf3959
---

#chat/full #project/closed-tactical-tasks #status/tactical

# Extract domain from URL list — Full Transcript

→ Light view: [[Chat/Light/2026-04-27-extract-domain-from-url-list-86b66c]]
→ Medium view: [[Chat/Medium/2026-04-27-extract-domain-from-url-list-86b66c]]

**Messages:** 6 | **Date:** 2026-04-27

---

### 1. **Human** — 2026-04-27T01:03

exact match regex, keep only one domain

https://www.thegoodguys.com.au/sunbeam-sleep-perfect-fitted-antibacterial-single-bla6321|https://www.thegoodguys.com.au/solt-freestanding-dishwasher-white-ggsdw6013w|https://www.thegoodguys.com.au/westinghouse-60cm-ceramic-cooktop-whc642bc|https://www.thegoodguys.com.au/westinghouse-60cm-silver-14-place-freestanding-dishwasher-wsf6602xc|https://www.thegoodguys.com.au/westinghouse-60cm-slideout-rangehood-wrr604sb|https://www.thegoodguys.com.au/solt-freestanding-dishwasher-stainless-steel-ggsdw6013x|https://www.thegoodguys.com.au/solt-99l-hybrid-chest-freezer-ggscf99w|https://www.thegoodguys.com.au/solt-9kg-front-load-washer-ggsflw900b|https://www.thegoodguys.com.au/solt-60cm-electric-oven-stainless-steel-ggso605ms|https://www.thegoodguys.com.au/solt-8kg-vented-dryer-ggsvd8w|https://www.thegoodguys.com.au/solt-45kg-vented-dryer-ggsvde45w|https://www.thegoodguys.com.au/shark-powerpro-cordless-vacuum-iz373hanz|https://www.thegoodguys.com.au/shark-cordless-vacuum-with-self-cleaning-brushroll-iz102|https://www.thegoodguys.com.au/samsung-galaxy-tab-a11-plus-wi-fi-6gb-128gb-grey-sm-x230nzaaxsa|https://www.thegoodguys.com.au/sennheiser-cx-true-wireless-508973|https://www.thegoodguys.com.au/samsung-65-inches-u8500f-crystal-uhd-4k-smart-tv-2025-ua65u8500fwxxy|https://www.thegoodguys.com.au/samsung-495l-french-door-refrigerator-srf5300sd|https://www.thegoodguys.com.au/roborock-q7b-plus-robotic-vacuum-rr-q7bp52-03-blk|https://www.thegoodguys.com.au/pacifica-extendable-clothes-airer-ca01|https://www.thegoodguys.com.au/nutribullet-mega-pack-1000-watts-n10-1107ak|https://www.thegoodguys.com.au/ninja-slushi-professional-frozen-drink-maker-fs301anz|https://www.thegoodguys.com.au/linsar-101-inches-digital-photo-frame-wifi-16gb-frameo-ls10dpwf|https://www.thegoodguys.com.au/lg-8kg-front-load-washer-wv5-1208w|https://www.thegoodguys.com.au/lg-635l-instaview-sxs-refrigerator-gs-v600mblc|https://www.thegoodguys.com.au/lenovo-ideapad-slim-3-mediatek-kompanio-520-4gb-128gb-chromebook-82xj0016au|https://www.thegoodguys.com.au/kindle-paperwhite-7-inches-12th-gen-16gb-ereader-b0cfpl6cfy|https://www.thegoodguys.com.au/fisher-and-paykel-7kg-sensor-dryer-de7060g2|https://www.thegoodguys.com.au/hisense-145l-hybrid-chest-freezer-hrcf146|https://www.thegoodguys.com.au/dji-osmo-pocket-3-creator-combo-5932238|https://www.thegoodguys.com.au/delonghi-2400w-dragon-4-oil-column-heater-wtimer-trd42400mt|https://www.thegoodguys.com.au/hisense-40-inches-a4qau-full-hd-smart-tv-2025-40a4qau|https://www.thegoodguys.com.au/ffalcon-50-inches-u65-led-google-tv-2025-ff50u65|https://www.thegoodguys.com.au/dimplex-2kw-windlesham-revillusion-electric-fireplace-wds20-au|https://www.thegoodguys.com.au/crest-kids-digital-camera-with-flip-lens-green-opn11301|https://www.thegoodguys.com.au/chiq-118l-top-mount-refrigerator-ctm118dw|https://www.thegoodguys.com.au/breville-barista-express-salted-liquorice-bes870slq|https://www.thegoodguys.com.au/apple-airpods-4-mxp63zaa|https://www.thegoodguys.com.au/bose-quietcomfort-earbuds-888507-0100
exact match regex, keep only one domain

https://www.thegoodguys.com.au/sunbeam-sleep-perfect-fitted-antibacterial-single-bla6321|https://www.thegoodguys.com.au/solt-freestanding-dishwasher-white-ggsdw6013w|https://www.thegoodguys.com.au/westinghouse-60cm-ceramic-cooktop-whc642bc|https://www.thegoodguys.com.au/westinghouse-60cm-silver-14-place-freestanding-dishwasher-wsf6602xc|https://www.thegoodguys.com.au/westinghouse-60cm-slideout-rangehood-wrr604sb|https://www.thegoodguys.com.au/solt-freestanding-dishwasher-stainless-steel-ggsdw6013x|https://www.thegoodguys.com.au/solt-99l-hybrid-chest-freezer-ggscf99w|https://www.thegoodguys.com.au/solt-9kg-front-load-washer-ggsflw900b|https://www.thegoodguys.com.au/solt-60cm-electric-oven-stainless-steel-ggso605ms|https://www.thegoodguys.com.au/solt-8kg-vented-dryer-ggsvd8w|https://www.thegoodguys.com.au/solt-45kg-vented-dryer-ggsvde45w|https://www.thegoodguys.com.au/shark-powerpro-cordless-vacuum-iz373hanz|https://www.thegoodguys.com.au/shark-cordless-vacuum-with-self-cleaning-brushroll-iz102|https://www.thegoodguys.com.au/samsung-galaxy-tab-a11-plus-wi-fi-6gb-128gb-grey-sm-x230nzaaxsa|https://www.thegoodguys.com.au/sennheiser-cx-true-wireless-508973|https://www.thegoodguys.com.au/samsung-65-inches-u8500f-crystal-uhd-4k-smart-tv-2025-ua65u8500fwxxy|https://www.thegoodguys.com.au/samsung-495l-french-door-refrigerator-srf5300sd|https://www.thegoodguys.com.au/roborock-q7b-plus-robotic-vacuum-rr-q7bp52-03-blk|https://www.thegoodguys.com.au/pacifica-extendable-clothes-airer-ca01|https://www.thegoodguys.com.au/nutribullet-mega-pack-1000-watts-n10-1107ak|https://www.thegoodguys.com.au/ninja-slushi-professional-frozen-drink-maker-fs301anz|https://www.thegoodguys.com.au/linsar-101-inches-digital-photo-frame-wifi-16gb-frameo-ls10dpwf|https://www.thegoodguys.com.au/lg-8kg-front-load-washer-wv5-1208w|https://www.thegoodguys.com.au/lg-635l-instaview-sxs-refrigerator-gs-v600mblc|https://www.thegoodguys.com.au/lenovo-ideapad-slim-3-mediatek-kompanio-520-4gb-128gb-chromebook-82xj0016au|https://www.thegoodguys.com.au/kindle-paperwhite-7-inches-12th-gen-16gb-ereader-b0cfpl6cfy|https://www.thegoodguys.com.au/fisher-and-paykel-7kg-sensor-dryer-de7060g2|https://www.thegoodguys.com.au/hisense-145l-hybrid-chest-freezer-hrcf146|https://www.thegoodguys.com.au/dji-osmo-pocket-3-creator-combo-5932238|https://www.thegoodguys.com.au/delonghi-2400w-dragon-4-oil-column-heater-wtimer-trd42400mt|https://www.thegoodguys.com.au/hisense-40-inches-a4qau-full-hd-smart-tv-2025-40a4qau|https://www.thegoodguys.com.au/ffalcon-50-inches-u65-led-google-tv-2025-ff50u65|https://www.thegoodguys.com.au/dimplex-2kw-windlesham-revillusion-electric-fireplace-wds20-au|https://www.thegoodguys.com.au/crest-kids-digital-camera-with-flip-lens-green-opn11301|https://www.thegoodguys.com.au/chiq-118l-top-mount-refrigerator-ctm118dw|https://www.thegoodguys.com.au/breville-barista-express-salted-liquorice-bes870slq|https://www.thegoodguys.com.au/apple-airpods-4-mxp63zaa|https://www.thegoodguys.com.au/bose-quietcomfort-earbuds-888507-0100

---

### 2. **Claude** — 2026-04-27T01:03

```
^https://www\.thegoodguys\.com\.au/[^|]+$
```

Applied per-URL (split on `|`, match, deduplicate domain):

All 39 URLs are from `www.thegoodguys.com.au`. No duplicates to remove.

If you want the regex to extract just the slug:

```
^https://www\.thegoodguys\.com\.au/(.+)$
```

Or if you're filtering a mixed list to keep only TGG URLs:

```
^https://www\.thegoodguys\.com\.au/
```

Which use case do you need this for? (Filtering, validation, extraction, or deduplication across a multi-domain list?)
 ```
^https://www\.thegoodguys\.com\.au/[^|]+$
```

Applied per-URL (split on `|`, match, deduplicate domain):

All 39 URLs are from `www.thegoodguys.com.au`. No duplicates to remove.

If you want the regex to extract just the slug:

```
^https://www\.thegoodguys\.com\.au/(.+)$
```

Or if you're filtering a mixed list to keep only TGG URLs:

```
^https://www\.thegoodguys\.com\.au/
```

Which use case do you need this for? (Filtering, validation, extraction, or deduplication across a multi-domain list?)

---

### 3. **Human** — 2026-04-27T01:04

i want one domain, then a array of slugs, exact match
i want one domain, then a array of slugs, exact match

---

### 4. **Claude** — 2026-04-27T01:04

```js
const domain = "https://www.thegoodguys.com.au";

const slugs = [
  "/sunbeam-sleep-perfect-fitted-antibacterial-single-bla6321",
  "/solt-freestanding-dishwasher-white-ggsdw6013w",
  "/westinghouse-60cm-ceramic-cooktop-whc642bc",
  "/westinghouse-60cm-silver-14-place-freestanding-dishwasher-wsf6602xc",
  "/westinghouse-60cm-slideout-rangehood-wrr604sb",
  "/solt-freestanding-dishwasher-stainless-steel-ggsdw6013x",
  "/solt-99l-hybrid-chest-freezer-ggscf99w",
  "/solt-9kg-front-load-washer-ggsflw900b",
  "/solt-60cm-electric-oven-stainless-steel-ggso605ms",
  "/solt-8kg-vented-dryer-ggsvd8w",
  "/solt-45kg-vented-dryer-ggsvde45w",
  "/shark-powerpro-cordless-vacuum-iz373hanz",
  "/shark-cordless-vacuum-with-self-cleaning-brushroll-iz102",
  "/samsung-galaxy-tab-a11-plus-wi-fi-6gb-128gb-grey-sm-x230nzaaxsa",
  "/sennheiser-cx-true-wireless-508973",
  "/samsung-65-inches
 ```js
const domain = "https://www.thegoodguys.com.au";

const slugs = [
  "/sunbeam-sleep-perfect-fitted-antibacterial-single-bla6321",
  "/solt-freestanding-dishwasher-white-ggsdw6013w",
  "/westinghouse-60cm-ceramic-cooktop-whc642bc",
  "/westinghouse-60cm-silver-14-place-freestanding-dishwasher-wsf6602xc",
  "/westinghouse-60cm-slideout-rangehood-wrr604sb",
  "/solt-freestanding-dishwasher-stainless-steel-ggsdw6013x",
  "/solt-99l-hybrid-chest-freezer-ggscf99w",
  "/solt-9kg-front-load-washer-ggsflw900b",
  "/solt-60cm-electric-oven-stainless-steel-ggso605ms",
  "/solt-8kg-vented-dryer-ggsvd8w",
  "/solt-45kg-vented-dryer-ggsvde45w",
  "/shark-powerpro-cordless-vacuum-iz373hanz",
  "/shark-cordless-vacuum-with-self-cleaning-brushroll-iz102",
  "/samsung-galaxy-tab-a11-plus-wi-fi-6gb-128gb-grey-sm-x230nzaaxsa",
  "/sennheiser-cx-true-wireless-508973",
  "/samsung-65-inches

---

### 5. **Human** — 2026-04-27T01:04

as regex
as regex

---

### 6. **Claude** — 2026-04-27T01:04

```regex
^https://www\.thegoodguys\.com\.au/(sunbeam-sleep-perfect-fitted-antibacterial-single-bla6321|solt-freestanding-dishwasher-white-ggsdw6013w|westinghouse-60cm-ceramic-cooktop-whc642bc|westinghouse-60cm-silver-14-place-freestanding-dishwasher-wsf6602xc|westinghouse-60cm-slideout-rangehood-wrr604sb|solt-freestanding-dishwasher-stainless-steel-ggsdw6013x|solt-99l-hybrid-chest-freezer-ggscf99w|solt-9kg-front-load-washer-ggsflw900b|solt-60cm-electric-oven-stainless-steel-ggso605ms|solt-8kg-vented-dryer-ggsvd8w|solt-45kg-vented-dryer-ggsvde45w|shark-powerpro-cordless-vacuum-iz373hanz|shark-cordless-vacuum-with-self-cleaning-brushroll-iz102|samsung-galaxy-tab-a11-plus-wi-fi-6gb-128gb-grey-sm-x230nzaaxsa|sennheiser-cx-true-wireless-508973|samsung-65-inches-u8500f-crystal-uhd-4k-smart-tv-2025-ua65u8500fwxxy|samsung-495l-french-door-refrigerator-srf5300sd|roborock-q7b-plus-robotic-vacuum-rr-q7bp52-03-blk|pacifica-extendable-clothes-airer-ca01|nutribullet-mega-pack-1000-watts-n10-1107ak|ninja-slushi-professional-frozen-drink-maker-fs301anz|linsar-101-inches-digital-photo-frame-wifi-16gb-frameo-ls10dpwf|lg-8kg-front-load-washer-wv5-1208w|lg-635l-instaview-sxs-refrigerator-gs-v600mblc|lenovo-ideapad-slim-3-mediatek-kompanio-520-4gb-128gb-chromebook-82xj0016au|kindle-paperwhite-7-inches-12th-gen-16gb-ereader-b0cfpl6cfy|fisher-and-paykel-7kg-sensor-dryer-de7060g2|hisense-145l-hybrid-chest-freezer-hrcf146|dji-osmo-pocket-3-creator-combo-5932238|delonghi-2400w-dragon-4-oil-column-heater-wtimer-trd42400mt|hisense-40-inches-a4qau-full-hd-smart-tv-2025-40a4qau|ffalcon-50-inches-u65-led-google-tv-2025-ff50u65|dimplex-2kw-windlesham-revillusion-electric-fireplace-wds20-au|crest-kids-digital-camera-with-flip-lens-green-opn11301|chiq-118l-top-mount-refrigerator-ctm118dw|breville-barista-express-salted-liquorice-bes870slq|apple-airpods-4-mxp63zaa|bose-quietcomfort-earbuds-888507-0100)$
```
 ```regex
^https://www\.thegoodguys\.com\.au/(sunbeam-sleep-perfect-fitted-antibacterial-single-bla6321|solt-freestanding-dishwasher-white-ggsdw6013w|westinghouse-60cm-ceramic-cooktop-whc642bc|westinghouse-60cm-silver-14-place-freestanding-dishwasher-wsf6602xc|westinghouse-60cm-slideout-rangehood-wrr604sb|solt-freestanding-dishwasher-stainless-steel-ggsdw6013x|solt-99l-hybrid-chest-freezer-ggscf99w|solt-9kg-front-load-washer-ggsflw900b|solt-60cm-electric-oven-stainless-steel-ggso605ms|solt-8kg-vented-dryer-ggsvd8w|solt-45kg-vented-dryer-ggsvde45w|shark-powerpro-cordless-vacuum-iz373hanz|shark-cordless-vacuum-with-self-cleaning-brushroll-iz102|samsung-galaxy-tab-a11-plus-wi-fi-6gb-128gb-grey-sm-x230nzaaxsa|sennheiser-cx-true-wireless-508973|samsung-65-inches-u8500f-crystal-uhd-4k-smart-tv-2025-ua65u8500fwxxy|samsung-495l-french-door-refrigerator-srf5300sd|roborock-q7b-plus-robotic-vacuum-rr-q7bp52-03-blk|pacifica-extendable-clothes-airer-ca01|nutribullet-mega-pack-1000-watts-n10-1107ak|ninja-slushi-professional-frozen-drink-maker-fs301anz|linsar-101-inches-digital-photo-frame-wifi-16gb-frameo-ls10dpwf|lg-8kg-front-load-washer-wv5-1208w|lg-635l-instaview-sxs-refrigerator-gs-v600mblc|lenovo-ideapad-slim-3-mediatek-kompanio-520-4gb-128gb-chromebook-82xj0016au|kindle-paperwhite-7-inches-12th-gen-16gb-ereader-b0cfpl6cfy|fisher-and-paykel-7kg-sensor-dryer-de7060g2|hisense-145l-hybrid-chest-freezer-hrcf146|dji-osmo-pocket-3-creator-combo-5932238|delonghi-2400w-dragon-4-oil-column-heater-wtimer-trd42400mt|hisense-40-inches-a4qau-full-hd-smart-tv-2025-40a4qau|ffalcon-50-inches-u65-led-google-tv-2025-ff50u65|dimplex-2kw-windlesham-revillusion-electric-fireplace-wds20-au|crest-kids-digital-camera-with-flip-lens-green-opn11301|chiq-118l-top-mount-refrigerator-ctm118dw|breville-barista-express-salted-liquorice-bes870slq|apple-airpods-4-mxp63zaa|bose-quietcomfort-earbuds-888507-0100)$
```
