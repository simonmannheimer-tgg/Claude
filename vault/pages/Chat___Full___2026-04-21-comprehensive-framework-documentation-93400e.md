---
title: Comprehensive framework documentation (full)
parent: Chat/Light/2026-04-21-comprehensive-framework-documentation-93400e
uuid: 93400e21-57f3-4b23-879a-313c8d70745d
---

#chat/full #project/main #status/completed

# Comprehensive framework documentation — Full Transcript

→ Light view: [[Chat/Light/2026-04-21-comprehensive-framework-documentation-93400e]]
→ Medium view: [[Chat/Medium/2026-04-21-comprehensive-framework-documentation-93400e]]

**Messages:** 4 | **Date:** 2026-04-21

---

### 1. **Human** — 2026-04-21T06:47

Map out in full the rules, processes, assumptions, best practices etc.
Map out in full the rules, processes, assumptions, best practices etc.

---

### 2. **Claude** — 2026-04-21T06:52

The user wants me to map out in full the rules, processes, assumptions, and best practices from the two uploaded ZIP files. Let me read the file-reading skill first, then extract the ZIP contents.
```
This block is not supported on your current device yet.
```

Now let me extract and read the ZIP files.
```
This block is not supported on your current device yet.
```

Let me extract the key process files. I'll focus on the rule-bearing documents first: the skill reference files, TOV, PLP intros, metadata, FAQ, EAV, and then the process files in the package.
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

Now let me read the AUDIT_AI_SEO.md and some of the plp-copywriting-package files to get the complete picture.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

I now have all the key information needed to produce a comprehensive map of the rules, processes, assumptions, and best practices. Let me synthesize this into a well-organized document. I'll cover:

1. System Architecture & File Structure
2. Workflow / Process Order
3. Page Type Classification
4. TOV - Hard Bans
5. TOV - Overuse Warnings
6. PLP Intro Rules (Process 01)
7. Metadata Rules (Process 02)
8. FAQ/Category Copy Rules (Process 05)
9. EAV Mapping (Process 08)


10. Batch Production Rules
11. QA Checklists
12. Known Gaps & Recommended Changes
13. Infrastructure/Tooling

Given the scope and complexity here, I should deliver this as a structured markdown document that ties everything together coherently.I have everything. Given the volume and its use as a reference, I'll produce this as a structured markdown file.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

I have enough content now to produce a comprehensive reference document. Let me create it.Now I have everything needed. Producing the full reference document.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

16 sections covering everything across both ZIPs. A few things worth flagging:

**Two active conflicts/ambiguities in the files themselves:**

1. The char range migration from 230–260 to 220–250 is documented as complete in the process files, but the brief (plp-copywriting-package) still includes the old find/replace instructions as a pre-flight step. If you have not yet applied those skill-file edits, three skills still carry the wrong range.

2. The EAV vs PLP intro char limits (250–265 vs 220–250) hitting the same CMS field is still unresolved. The docs flag it but there is no confirmation either way.

**The most structurally significant gap** is Gap 4 (EAV skipped in practice). Every other gap is a quality problem. This one is a workflow enforcement problem — the skill routes directly to Process 01 without conditioning on 08 being run first. Until that is a hard step, not an advisory note, entity quality will remain inconsistent.
 
I have everything. Given the volume and its use as a reference, I'll produce this as a structured markdown file.
Now I have everything needed. Producing the full reference document.
16 sections covering everything across both ZIPs. A few things worth flagging:

**Two active conflicts/ambiguities in the files themselves:**

1. The char range migration from 230–260 to 220–250 is documented as complete in the process files, but the brief (plp-copywriting-package) still includes the old find/replace instructions as a pre-flight step. If you have not yet applied those skill-file edits, three skills still carry the wrong range.

2. The EAV vs PLP intro char limits (250–265 vs 220–250) hitting the same CMS field is still unresolved. The docs flag it but there is no confirmation either way.

**The most structurally significant gap** is Gap 4 (EAV skipped in practice). Every other gap is a quality problem. This one is a workflow enforcement problem — the skill routes directly to Process 01 without conditioning on 08 being run first. Until that is a hard step, not an advisory note, entity quality will remain inconsistent.

---

### 3. **Human** — 2026-04-21T07:00

do we adhere?
do we adhere?

---

### 4. **Claude** — 2026-04-21T07:02

The user wants to know if the uploaded Excel file adheres to the rules mapped out. Let me read the file first.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The relevant sheets for the rules audit are the PLP copy sheets: "Page Description" (Type A - generic category), "Page Desc. (Brand Cat) | B1" (Type B), "Page Desc. (Brand Cat) | B2, B3, B4" (Type C). Let me extract all the "New Description" copy and run the audit checks against the rules.

Let me load all copy rows from the relevant sheets and audit them.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now I have a comprehensive picture. Let me summarize the findings clearly.

Key findings:
1. **Char > 250: 870 (45.7%)** - This is the biggest problem. Only affects sheets A (562) and B1 (308). B2/B3/B4 are all within range. The median overrun is 260 chars (old spec was 230-260).
2. **Sentence count != 2: 24 (1.3%)** - Mix of single-sentence (probably a comma instead of a period) and 3-sentence pieces.
3. **TGG not exactly once: 0** - Clean.


4. **Hard bans** are scattered across the content: "sale" appears 21 times mostly on deals and clearance pages, "stunning" shows up 5 times, "save" in price framing context 5 times, and "busy homes" 6 times.
5. **Brand page violations** are concentrated in B1-B4 sheets with "reliable" and "enjoy" each appearing 13 times.

The character count pattern points to these sheets being built under the old 230–260 character spec—the median sits right at 260, the previous target. The A and B1 sheets haven't been updated since then. I'm noticing a conflict in the rules: the hard ban list says "sale" is prohibited, but the Type D specification explicitly allows "{Category} Black Friday sale {year}" as a permitted format. I need to clarify whether "Black Friday sale" is an exception to the hard ban or if there's an inconsistency in the guidelines.

Looking at the actual /deals/ pages, they're using phrases like "on sale" as descriptive language rather than following the "{Category} Black Friday sale {year}" pattern, so these violations are legitimate. The /clearance/ pages are opening with "Save on..." which triggers the price framing ban—these might be a separate page type not covered by the spec, but the hard ban still applies regardless.Here's the full picture.

---

## Compliance audit — 1,902 rows across 5 sheets

### Critical failures

**45.7% breach the 250-character ceiling (870 rows)**

The entire Type A sheet (562 rows) and most of B1 (308 rows) are over. B2, B3, and B4 are clean. The median overrun is 260 chars — the old spec sweet spot. These sheets have not been updated since the char range changed from 230–260 to 220–250 in March 2026. This is not a writing quality issue; it's a systematic version lag.

**24 rows have the wrong sentence count (1.3%)**

17 are single sentences (long, comma-joined run-ons). 7 are three sentences (copy that wasn't trimmed after being drafted). URLs include: /fridges-and-freezers, /gaming/gaming-hardware, /televisions/all-tvs/85-inch-tvs, /phones-and-wearables/mobile-phones/5g-mobile-phones.

---

### Hard ban violations

| Banned term | Count | Notes |
|---|---|---|
| "sale" | 21 | All on /deals/ and /clearance/ paths — phrasing like "on sale", not the Type D permitted "Black Friday sale {year}" structure |
| "busy homes" | 6 | Exact phrase — /chest-freezers, /black-washing-machines, /dyson vacuums, /lg washing machines, /hisense washing machines, /sharp cooking |
| "save" (price framing) | 5 | All /clearance/ pages open with "Save on..." — direct price framing, hard ban violation |
| "stunning" | 5 | /dslr-cameras, /55-inch-tvs, /iphone, /playstation-consoles, /tablets |

---

### Brand page additional bans (B1–B4, 1,335 rows)

| Word | Count | % of brand rows |
|---|---|---|
| "features" | 24 | 1.8% |
| "enjoy" | 13 | 1.0% |
| "reliable" | 13 | 1.0% |

Representative examples:
- "enjoy" on brand pages: /tcl/televisions, /sony/televisions, /apple/audio/headphones, /lg/televisions/oled-tvs
- "features" on brand pages: /tcl/televisions, /lg/televisions, /oppo/mobile-phones, /motorola/mobile-phones
- "reliable" on brand pages: /westinghouse/ovens, /fujitsu/air-conditioners, /lg/tv-accessories

---

### Clean

- TGG appears exactly once in all 1,902 rows — 100% clean
- No exclamation marks
- Only 4 rows (0.2%) use banned S1 openers (Discover/Explore/Shop)

---

### Root cause summary

The 870-row char breach is a single version control failure — sheets A and B1 predate the March 2026 spec update. Everything else is scattered individual violations. Fix priority:

1. Re-trim sheets A and B1 to 220–250 (systematic, ~1,000 rows need cutting)
2. Clear the 21 "sale" and 5 "save" hard ban violations (clearance/deals pages)
3. Fix 24 brand-page "features" violations
4. Fix 13 "enjoy" + 13 "reliable" on brand pages
5. Fix 6 "busy homes" and 5 "stunning"
6. Resolve 24 sentence-count rows

Want a flagged output file with all violations tagged per row?
 
Here's the full picture.

---

## Compliance audit — 1,902 rows across 5 sheets

### Critical failures

**45.7% breach the 250-character ceiling (870 rows)**

The entire Type A sheet (562 rows) and most of B1 (308 rows) are over. B2, B3, and B4 are clean. The median overrun is 260 chars — the old spec sweet spot. These sheets have not been updated since the char range changed from 230–260 to 220–250 in March 2026. This is not a writing quality issue; it's a systematic version lag.

**24 rows have the wrong sentence count (1.3%)**

17 are single sentences (long, comma-joined run-ons). 7 are three sentences (copy that wasn't trimmed after being drafted). URLs include: /fridges-and-freezers, /gaming/gaming-hardware, /televisions/all-tvs/85-inch-tvs, /phones-and-wearables/mobile-phones/5g-mobile-phones.

---

### Hard ban violations

| Banned term | Count | Notes |
|---|---|---|
| "sale" | 21 | All on /deals/ and /clearance/ paths — phrasing like "on sale", not the Type D permitted "Black Friday sale {year}" structure |
| "busy homes" | 6 | Exact phrase — /chest-freezers, /black-washing-machines, /dyson vacuums, /lg washing machines, /hisense washing machines, /sharp cooking |
| "save" (price framing) | 5 | All /clearance/ pages open with "Save on..." — direct price framing, hard ban violation |
| "stunning" | 5 | /dslr-cameras, /55-inch-tvs, /iphone, /playstation-consoles, /tablets |

---

### Brand page additional bans (B1–B4, 1,335 rows)

| Word | Count | % of brand rows |
|---|---|---|
| "features" | 24 | 1.8% |
| "enjoy" | 13 | 1.0% |
| "reliable" | 13 | 1.0% |

Representative examples:
- "enjoy" on brand pages: /tcl/televisions, /sony/televisions, /apple/audio/headphones, /lg/televisions/oled-tvs
- "features" on brand pages: /tcl/televisions, /lg/televisions, /oppo/mobile-phones, /motorola/mobile-phones
- "reliable" on brand pages: /westinghouse/ovens, /fujitsu/air-conditioners, /lg/tv-accessories

---

### Clean

- TGG appears exactly once in all 1,902 rows — 100% clean
- No exclamation marks
- Only 4 rows (0.2%) use banned S1 openers (Discover/Explore/Shop)

---

### Root cause summary

The 870-row char breach is a single version control failure — sheets A and B1 predate the March 2026 spec update. Everything else is scattered individual violations. Fix priority:

1. Re-trim sheets A and B1 to 220–250 (systematic, ~1,000 rows need cutting)
2. Clear the 21 "sale" and 5 "save" hard ban violations (clearance/deals pages)
3. Fix 24 brand-page "features" violations
4. Fix 13 "enjoy" + 13 "reliable" on brand pages
5. Fix 6 "busy homes" and 5 "stunning"
6. Resolve 24 sentence-count rows

Want a flagged output file with all violations tagged per row?
