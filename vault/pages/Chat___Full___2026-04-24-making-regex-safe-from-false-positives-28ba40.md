---
title: Making regex safe from false positives (full)
parent: Chat/Light/2026-04-24-making-regex-safe-from-false-positives-28ba40
uuid: 28ba404d-dce9-446d-aa65-a46d4f4f99b1
---

#chat/full #project/colour-keyword-gsc-analysis #status/active

# Making regex safe from false positives — Full Transcript

→ Light view: [[Chat/Light/2026-04-24-making-regex-safe-from-false-positives-28ba40]]
→ Medium view: [[Chat/Medium/2026-04-24-making-regex-safe-from-false-positives-28ba40]]

**Messages:** 8 | **Date:** 2026-04-24

---

### 1. **Human** — 2026-04-24T02:19

help me figure out to make this regex safe:

(?i)\b(black|white|grey|gray|silver|gold|rose\s+gold|copper|bronze|brass|chrome|nickel|gunmetal|red|orange|yellow|green|blue|navy|teal|turquoise|cyan|indigo|purple|violet|magenta|pink|beige|cream|ivory|tan|taupe|brown|charcoal|graphite|slate|stone|pewter|pearl|coral|lilac|lavender|mauve|plum|peach|amber|ruby|burgundy|olive|mint|jade|emerald|clear|transparent|multicolou?r|assorted|saffron|sand|dune|midnight|starlight)\b

to not catch against the fixes in this "does not contain" version

(?i)(friday|gold service|gold coast|gold card|gold coast|concierge|membership|black week|boxing day|cyber monday|clearance|cream maker|cast|black november|black froday|black frisay|black firday|black fridsy|black fridya|black fridat|black fridy|black frida|black feiday|black firday|black froday|black frifay|black fridau|black fridya|black frisay|black fruday|black fryday)
help me figure out to make this regex safe:

(?i)\b(black|white|grey|gray|silver|gold|rose\s+gold|copper|bronze|brass|chrome|nickel|gunmetal|red|orange|yellow|green|blue|navy|teal|turquoise|cyan|indigo|purple|violet|magenta|pink|beige|cream|ivory|tan|taupe|brown|charcoal|graphite|slate|stone|pewter|pearl|coral|lilac|lavender|mauve|plum|peach|amber|ruby|burgundy|olive|mint|jade|emerald|clear|transparent|multicolou?r|assorted|saffron|sand|dune|midnight|starlight)\b

to not catch against the fixes in this "does not contain" version

(?i)(friday|gold service|gold coast|gold card|gold coast|concierge|membership|black week|boxing day|cyber monday|clearance|cream maker|cast|black november|black froday|black frisay|black firday|black fridsy|black fridya|black fridat|black fridy|black frida|black feiday|black firday|black froday|black frifay|black fridau|black fridya|black frisay|black fruday|black fryday)

---

### 2. **Claude** — 2026-04-24T02:19

The simplest fix is a negative lookahead anchored around the conflict words. The problem is that your colour regex fires on `black`, `gold`, `cream`, `white` etc. inside phrases like "Black Friday" or "Gold Coast".

Add a negative lookahead after the opening `(?i)`:

```
(?i)(?!.*\b(friday|gold\s+service|gold\s+coast|gold\s+card|concierge|membership|black\s+week|boxing\s+day|cyber\s+monday|clearance|cream\s+maker|black\s+november|black\s+fr[io][ds]?[au]?[yd]?[a]?[yu]?)\b)\b(black|white|grey|gray|silver|gold|rose\s+gold|copper|bronze|brass|chrome|nickel|gunmetal|red|orange|yellow|green|blue|navy|teal|turquoise|cyan|indigo|purple|violet|magenta|pink|beige|cream|ivory|tan|taupe|brown|charcoal|graphite|slate|stone|pewter|pearl|coral|lilac|lavender|mauve|plum|peach|amber|ruby|burgundy|olive|mint|jade|emerald|clear|transparent|multicolou?r|assorted|saffron|sand|dune|midnight|starlight)\b
```

A few things to note:

**What the lookahead does.** `(?!.*\b...\b)` tests the entire string before any colour match fires. If the string contains any of the exclusion phrases, the whole match fails.

**The Black Friday typo variants.** Your exclusion list has ~14 typos of "Black Friday". Rather than enumerate them all, collapse to one fuzzy pattern: `black\s+fr[a-z]{4,6}` catches all plausible misspellings without bloating the list. I've simplified this above, but you can tighten or loosen the character class.

**"cast" and "clearance".** These are in your exclusion list but don't contain any colour terms, so they'd never trigger the colour regex anyway. They're harmless but dead weight, remove them if you want a clean list.

**Where this breaks.** If you're matching at the field level (one product title per match attempt), the lookahead works cleanly. If you're running this against a bulk string with multiple titles concatenated, the `.*` in the lookahead will scan across title boundaries and produce false negatives. Confirm your matching scope before deploying.
 The simplest fix is a negative lookahead anchored around the conflict words. The problem is that your colour regex fires on `black`, `gold`, `cream`, `white` etc. inside phrases like "Black Friday" or "Gold Coast".

Add a negative lookahead after the opening `(?i)`:

```
(?i)(?!.*\b(friday|gold\s+service|gold\s+coast|gold\s+card|concierge|membership|black\s+week|boxing\s+day|cyber\s+monday|clearance|cream\s+maker|black\s+november|black\s+fr[io][ds]?[au]?[yd]?[a]?[yu]?)\b)\b(black|white|grey|gray|silver|gold|rose\s+gold|copper|bronze|brass|chrome|nickel|gunmetal|red|orange|yellow|green|blue|navy|teal|turquoise|cyan|indigo|purple|violet|magenta|pink|beige|cream|ivory|tan|taupe|brown|charcoal|graphite|slate|stone|pewter|pearl|coral|lilac|lavender|mauve|plum|peach|amber|ruby|burgundy|olive|mint|jade|emerald|clear|transparent|multicolou?r|assorted|saffron|sand|dune|midnight|starlight)\b
```

A few things to note:

**What the lookahead does.** `(?!.*\b...\b)` tests the entire string before any colour match fires. If the string contains any of the exclusion phrases, the whole match fails.

**The Black Friday typo variants.** Your exclusion list has ~14 typos of "Black Friday". Rather than enumerate them all, collapse to one fuzzy pattern: `black\s+fr[a-z]{4,6}` catches all plausible misspellings without bloating the list. I've simplified this above, but you can tighten or loosen the character class.

**"cast" and "clearance".** These are in your exclusion list but don't contain any colour terms, so they'd never trigger the colour regex anyway. They're harmless but dead weight, remove them if you want a clean list.

**Where this breaks.** If you're matching at the field level (one product title per match attempt), the lookahead works cleanly. If you're running this against a bulk string with multiple titles concatenated, the `.*` in the lookahead will scan across title boundaries and produce false negatives. Confirm your matching scope before deploying.

---

### 3. **Human** — 2026-04-24T02:19

doeos that work in gsc?
doeos that work in gsc?

---

### 4. **Claude** — 2026-04-24T02:19

No. GSC custom filters use simple contains/does not contain logic. No regex support at all.

What's the actual goal? Filtering out sale/promo titles from a colour-keyword report, or something else? That'll determine the right approach.
 No. GSC custom filters use simple contains/does not contain logic. No regex support at all.

What's the actual goal? Filtering out sale/promo titles from a colour-keyword report, or something else? That'll determine the right approach.

---

### 5. **Human** — 2026-04-24T02:36

goal is to look at colour keywords without catching some of these issue urls. maybe a url regex exclude?

i want a way to get as much colouors as i can, but not matching category pages or the attaced ones that would catch on
goal is to look at colour keywords without catching some of these issue urls. maybe a url regex exclude?

i want a way to get as much colouors as i can, but not matching category pages or the attaced ones that would catch on

---

### 6. **Claude** — 2026-04-24T02:37

Let me read the files first to understand what URL patterns are causing the problem.
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

Now I have a clear picture. Here are the URL pattern clusters you need to exclude, and what to do in GSC.

**The problem URL patterns (colour in URL but not colour pages):**

1. `/deals/black-friday-*` — all Black Friday subpages
2. `/gold-service-extras*` — all Gold Service pages
3. `/clearance*` — clearance pages
4. `/stores/*` — store locator pages
5. `/whats-new/*` — editorial/blog pages that mention Black Friday, "black kitchens" etc.
6. `/black-and-decker*` — brand pages where "black" is the brand name
7. `/black-friday-sale` — the main BF landing page
8. `commercial.thegoodguys.com.au/*` — entire commercial subdomain (no colour PLPs there, only nav structure and `freestanding` etc. triggering false positives like "sand" in "sandwich")
9. `/contact-gold-service-extras-team` — misc support page

**GSC approach since regex isn't available:**

GSC's Page filter supports "URL contains" and "URL does not contain". You can chain multiple exclusions. The practical approach:

In your GSC filter, set **Page** to:
- Does not contain: `/deals/black-friday`
- Does not contain: `/gold-service-extras`
- Does not contain: `/clearance`
- Does not contain: `/whats-new/`
- Does not contain: `/stores/`
- Does not contain: `/black-and-decker`
- Does not contain: `commercial.thegoodguys.com.au`

GSC lets you add multiple page filters in sequence. That covers the main problem clusters.

**What you'll still catch that needs manual review:** `/whats-new/black-kitchens`, `/whats-new/black-washing-machines-and-dryers`, `/televisions/wall-mounts-and-stands/black-tv-units`, and `/cooking-and-dishwashers/sinks-and-taps/black-mixer-taps` are actually legitimate colour pages. The `/whats-new/` exclusion above will drop those editorial articles too, which is probably fine for a colour-keyword analysis.

The cleanest approach for deeper analysis is to export to Sheets and apply the regex there, but for in-GSC filtering, the seven exclusions above will remove most of the noise.
 Let me read the files first to understand what URL patterns are causing the problem.
Now I have a clear picture. Here are the URL pattern clusters you need to exclude, and what to do in GSC.

**The problem URL patterns (colour in URL but not colour pages):**

1. `/deals/black-friday-*` — all Black Friday subpages
2. `/gold-service-extras*` — all Gold Service pages
3. `/clearance*` — clearance pages
4. `/stores/*` — store locator pages
5. `/whats-new/*` — editorial/blog pages that mention Black Friday, "black kitchens" etc.
6. `/black-and-decker*` — brand pages where "black" is the brand name
7. `/black-friday-sale` — the main BF landing page
8. `commercial.thegoodguys.com.au/*` — entire commercial subdomain (no colour PLPs there, only nav structure and `freestanding` etc. triggering false positives like "sand" in "sandwich")
9. `/contact-gold-service-extras-team` — misc support page

**GSC approach since regex isn't available:**

GSC's Page filter supports "URL contains" and "URL does not contain". You can chain multiple exclusions. The practical approach:

In your GSC filter, set **Page** to:
- Does not contain: `/deals/black-friday`
- Does not contain: `/gold-service-extras`
- Does not contain: `/clearance`
- Does not contain: `/whats-new/`
- Does not contain: `/stores/`
- Does not contain: `/black-and-decker`
- Does not contain: `commercial.thegoodguys.com.au`

GSC lets you add multiple page filters in sequence. That covers the main problem clusters.

**What you'll still catch that needs manual review:** `/whats-new/black-kitchens`, `/whats-new/black-washing-machines-and-dryers`, `/televisions/wall-mounts-and-stands/black-tv-units`, and `/cooking-and-dishwashers/sinks-and-taps/black-mixer-taps` are actually legitimate colour pages. The `/whats-new/` exclusion above will drop those editorial articles too, which is probably fine for a colour-keyword analysis.

The cleanest approach for deeper analysis is to export to Sheets and apply the regex there, but for in-GSC filtering, the seven exclusions above will remove most of the noise.

---

### 7. **Human** — 2026-04-24T02:47

give me query regex and page not include regex
give me query regex and page not include regex

---

### 8. **Claude** — 2026-04-24T02:48

**Query regex** (your original is fine, no changes needed for GSC since you're doing this outside GSC):

```
(?i)\b(black|white|grey|gray|silver|gold|rose\s*gold|copper|bronze|brass|chrome|nickel|gunmetal|red|orange|yellow|green|blue|navy|teal|turquoise|cyan|indigo|purple|violet|magenta|pink|beige|cream|ivory|tan|taupe|brown|charcoal|graphite|slate|stone|pewter|pearl|coral|lilac|lavender|mauve|plum|peach|amber|ruby|burgundy|olive|mint|jade|emerald|clear|transparent|multicolou?r|assorted|saffron|sand|dune|midnight|starlight)\b
```

---

**Page exclusion regex:**

```
(?i)(\/deals\/black-friday|\/gold-service-extras|\/clearance|\/whats-new\/|\/stores\/|\/black-and-decker|commercial\.thegoodguys\.com\.au|\/black-friday-sale|razer-gold|ledger-nano.*gold|boost-prepaid-sim-kit.*black|\/contact-gold|goldair|\/sandisk$)
```

A few decisions baked in:
- `razer-gold` and `ledger-nano.*gold` catch gift card and crypto wallet PDPs where gold is a brand/product name, not a colour filter
- `boost-prepaid-sim-kit.*black` catches the SIM SKUs where black is the SKU suffix
- `goldair` catches the brand pages
- `\/sandisk$` catches the brand hub page (individual Sandisk PDPs with colour in the slug are fine to keep)

If you want a simpler version without the edge cases:

```
(?i)(\/deals\/black-friday|\/gold-service-extras|\/clearance|\/whats-new\/|\/stores\/|\/black-and-decker|commercial\.thegoodguys\.com\.au|\/black-friday-sale|goldair)
```
 **Query regex** (your original is fine, no changes needed for GSC since you're doing this outside GSC):

```
(?i)\b(black|white|grey|gray|silver|gold|rose\s*gold|copper|bronze|brass|chrome|nickel|gunmetal|red|orange|yellow|green|blue|navy|teal|turquoise|cyan|indigo|purple|violet|magenta|pink|beige|cream|ivory|tan|taupe|brown|charcoal|graphite|slate|stone|pewter|pearl|coral|lilac|lavender|mauve|plum|peach|amber|ruby|burgundy|olive|mint|jade|emerald|clear|transparent|multicolou?r|assorted|saffron|sand|dune|midnight|starlight)\b
```

---

**Page exclusion regex:**

```
(?i)(\/deals\/black-friday|\/gold-service-extras|\/clearance|\/whats-new\/|\/stores\/|\/black-and-decker|commercial\.thegoodguys\.com\.au|\/black-friday-sale|razer-gold|ledger-nano.*gold|boost-prepaid-sim-kit.*black|\/contact-gold|goldair|\/sandisk$)
```

A few decisions baked in:
- `razer-gold` and `ledger-nano.*gold` catch gift card and crypto wallet PDPs where gold is a brand/product name, not a colour filter
- `boost-prepaid-sim-kit.*black` catches the SIM SKUs where black is the SKU suffix
- `goldair` catches the brand pages
- `\/sandisk$` catches the brand hub page (individual Sandisk PDPs with colour in the slug are fine to keep)

If you want a simpler version without the edge cases:

```
(?i)(\/deals\/black-friday|\/gold-service-extras|\/clearance|\/whats-new\/|\/stores\/|\/black-and-decker|commercial\.thegoodguys\.com\.au|\/black-friday-sale|goldair)
```
