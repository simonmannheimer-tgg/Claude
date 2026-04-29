---
title: Update sale SKUs and summary tables (full)
parent: Chat/Light/2026-04-15-update-sale-skus-and-summary-tables-baad36
uuid: baad369c-e69a-42ec-b15d-239ecb411ba3
---

#chat/full #project/eofy #status/completed

# Update sale SKUs and summary tables — Full Transcript

→ Light view: [[Chat/Light/2026-04-15-update-sale-skus-and-summary-tables-baad36]]
→ Medium view: [[Chat/Medium/2026-04-15-update-sale-skus-and-summary-tables-baad36]]

**Messages:** 4 | **Date:** 2026-04-15

---

### 1. **Human** — 2026-04-15T03:13

We need to update tab 7 of this doc - on sale skus. the goal is to fill in the table that has all skus and their sale periods (obviously deduping any already there where you match sku and onsale period and decide its already there ) then adding in the new skus and their periods, naming them by EOFY [YEAR] - then updating the summary tables to match the new data.
We need to update tab 7 of this doc - on sale skus. the goal is to fill in the table that has all skus and their sale periods (obviously deduping any already there where you match sku and onsale period and decide its already there ) then adding in the new skus and their periods, naming them by EOFY [YEAR] - then updating the summary tables to match the new data.

---

### 2. **Human** — 2026-04-15T03:20

We need to update tab 7 of this doc - on sale skus. the goal is to fill in the table that has all skus and their sale periods (obviously deduping any already there where you match sku and onsale period and decide its already there ) then adding in the new skus and their periods, naming them by EOFY [YEAR] - then updating the summary tables to match the new data.
We need to update tab 7 of this doc - on sale skus. the goal is to fill in the table that has all skus and their sale periods (obviously deduping any already there where you match sku and onsale period and decide its already there ) then adding in the new skus and their periods, naming them by EOFY [YEAR] - then updating the summary tables to match the new data.

---

### 3. **Claude** — 2026-04-15T03:31

```
This block is not supported on your current device yet.
```

Now let me read the uploaded file to understand tab 7's structure.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

I have a clear picture now. Let me read the rest of the detail table to find where it ends, then check the project files for EOFY data.
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

Now I have the full picture. Let me also check what the summary tables look like and then build the updated file.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now I have everything. Let me build the updated file.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**What I've established:**

**Current state of tab 7:**
- Detail table (cols I–N): 1,035 rows covering Black Friday 2025 (813 SKUs), EOFY 2025 (174), and EOFY 2024 (48)
- Summary table 1 (B2:G17): top-level category counts
- Summary table 2 (B19:G123): subcategory breakdown
- Existing EOFY sale periods: `27/06/2024 - 03/07/2024` (2024) and `26/06/2025 - 02/07/2025` (2025)

**New SKUs to add (9, after full dedup)** — all EOFY 2025, two new sale periods from WK51 press ads:

| Heading | SKU | Sale Event | Sale Period |
|---|---|---|---|
| 85" C6K QD Mini LED Google TV 2025 | 50093892 | EOFY 2025 | 19/06/2025 - 02/07/2025 |
| 75" Q6QAU 4K QLED Smart TV 2025 | 50094493 | EOFY 2025 | 19/06/2025 - 02/07/2025 |
| 65" OLED EVO C5 AI UHD 4K Smart TV 2025 | 50093941 | EOFY 2025 | 19/06/2025 - 02/07/2025 |
| 70" UHD WebOS TV | 50088715 | EOFY 2025 | 19/06/2025 - 02/07/2025 |
| 8kg Front Load Washer | 50094053 | EOFY 2025 | 19/06/2025 - 30/06/2025 |
| 559L Side By Side Refrigerator | 50091794 | EOFY 2025 | 19/06/2025 - 30/06/2025 |
| 427L Bottom Mount Refrigerator | 50091703 | EOFY 2025 | 19/06/2025 - 30/06/2025 |
| 11kg Front Load Washer | 50091501 | EOFY 2025 | 19/06/2025 - 30/06/2025 |
| Freestanding Dishwasher - Stainless Steel | 50090879 | EOFY 2025 | 19/06/2025 - 30/06/2025 |

**Issue I hit:** Summary cells use `=SUM(D6:E6)` formulas (not hardcoded values), so I can't just add integers to them — I need to handle formula cells differently. I need to either recalculate via the formula after adding data, or update only the raw input cells that feed those formulas.

Before I continue: the summary tables appear to use hardcoded counts (not COUNTIF formulas pulling from the detail table). Do you want me to:
1. Update the hardcoded numeric cells in the summary tables directly (adding the deltas on top of existing values), or
2. Replace the summary table with COUNTIF formulas that pull from the detail table dynamically?

Option 2 is more robust long-term but changes the structure. Option 1 preserves the existing approach. Your call before I proceed.
Now let me read the uploaded file to understand tab 7's structure.
I have a clear picture now. Let me read the rest of the detail table to find where it ends, then check the project files for EOFY data.
Now I have the full picture. Let me also check what the summary tables look like and then build the updated file.
Now I have everything. Let me build the updated file.
**What I've established:**

**Current state of tab 7:**
- Detail table (cols I–N): 1,035 rows covering Black Friday 2025 (813 SKUs), EOFY 2025 (174), and EOFY 2024 (48)
- Summary table 1 (B2:G17): top-level category counts
- Summary table 2 (B19:G123): subcategory breakdown
- Existing EOFY sale periods: `27/06/2024 - 03/07/2024` (2024) and `26/06/2025 - 02/07/2025` (2025)

**New SKUs to add (9, after full dedup)** — all EOFY 2025, two new sale periods from WK51 press ads:

| Heading | SKU | Sale Event | Sale Period |
|---|---|---|---|
| 85" C6K QD Mini LED Google TV 2025 | 50093892 | EOFY 2025 | 19/06/2025 - 02/07/2025 |
| 75" Q6QAU 4K QLED Smart TV 2025 | 50094493 | EOFY 2025 | 19/06/2025 - 02/07/2025 |
| 65" OLED EVO C5 AI UHD 4K Smart TV 2025 | 50093941 | EOFY 2025 | 19/06/2025 - 02/07/2025 |
| 70" UHD WebOS TV | 50088715 | EOFY 2025 | 19/06/2025 - 02/07/2025 |
| 8kg Front Load Washer | 50094053 | EOFY 2025 | 19/06/2025 - 30/06/2025 |
| 559L Side By Side Refrigerator | 50091794 | EOFY 2025 | 19/06/2025 - 30/06/2025 |
| 427L Bottom Mount Refrigerator | 50091703 | EOFY 2025 | 19/06/2025 - 30/06/2025 |
| 11kg Front Load Washer | 50091501 | EOFY 2025 | 19/06/2025 - 30/06/2025 |
| Freestanding Dishwasher - Stainless Steel | 50090879 | EOFY 2025 | 19/06/2025 - 30/06/2025 |

**Issue I hit:** Summary cells use `=SUM(D6:E6)` formulas (not hardcoded values), so I can't just add integers to them — I need to handle formula cells differently. I need to either recalculate via the formula after adding data, or update only the raw input cells that feed those formulas.

Before I continue: the summary tables appear to use hardcoded counts (not COUNTIF formulas pulling from the detail table). Do you want me to:
1. Update the hardcoded numeric cells in the summary tables directly (adding the deltas on top of existing values), or
2. Replace the summary table with COUNTIF formulas that pull from the detail table dynamically?

Option 2 is more robust long-term but changes the structure. Option 1 preserves the existing approach. Your call before I proceed.

---

### 4. **Claude** — 2026-04-15T03:32

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

Now I have a clear picture of the structure. Let me now read all the project files to extract new EOFY SKUs.
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

**Before I proceed with writing the file**, I need to flag some important issues so you can decide how to proceed:

**What I've found from the project files:**

The project files contain SKUs from these EOFY events:

- **EOFY 2024** (from WK47 Mag and WK52 Press): 55 SKUs total, sale period 27/06/2024 - 03/07/2024
- **EOFY 2025** (from WK51 Whitegoods, WK51 TVs, WK52 Final Days): 325 SKUs total, with 3 distinct sale periods (19/06/2025-30/06/2025, 19/06/2025-02/07/2025, 26/06/2025-02/07/2025)

**Issues I need you to resolve before writing:**

**1. Naming mismatch.** The existing tab already has "EOFY 2024" and "EOFY 2025" as sale event labels. The project files match those names. But the WK47 Mag has no sale period in the file itself. I've used 27/06/2024 - 03/07/2024 (from the WK52 Press) as a proxy. Is that correct, or was the magazine on a different date?

**2. WK52 Final Days Linelist has two identical sheets** (Sheet_DIGITAL ONLY and Sheet_-National) with the same 158 rows each. This looks like a duplicate. Should I dedupe by SKU+period within that file, or are they intended to be different subsets?

**3. Category data is missing** for WK47 and WK52 2024 sources. The 2024 line lists don't have a Marketing Category column (just brand/model/product description). The existing SKU table requires a Category field. Do you want me to leave that blank for those rows, or try to infer it from the product description?

**4. The WK52 Final Days sheets** contain 316 rows after deduping within the file, but many of these will already exist in the current SKU table under "EOFY 2025". The dedup logic I'll apply is: exact match on SKU number + sale event + sale period. Anything where those three match gets dropped.

Quick confirm on these before I write the file?
Now I have a clear picture of the structure. Let me now read all the project files to extract new EOFY SKUs.
**Before I proceed with writing the file**, I need to flag some important issues so you can decide how to proceed:

**What I've found from the project files:**

The project files contain SKUs from these EOFY events:

- **EOFY 2024** (from WK47 Mag and WK52 Press): 55 SKUs total, sale period 27/06/2024 - 03/07/2024
- **EOFY 2025** (from WK51 Whitegoods, WK51 TVs, WK52 Final Days): 325 SKUs total, with 3 distinct sale periods (19/06/2025-30/06/2025, 19/06/2025-02/07/2025, 26/06/2025-02/07/2025)

**Issues I need you to resolve before writing:**

**1. Naming mismatch.** The existing tab already has "EOFY 2024" and "EOFY 2025" as sale event labels. The project files match those names. But the WK47 Mag has no sale period in the file itself. I've used 27/06/2024 - 03/07/2024 (from the WK52 Press) as a proxy. Is that correct, or was the magazine on a different date?

**2. WK52 Final Days Linelist has two identical sheets** (Sheet_DIGITAL ONLY and Sheet_-National) with the same 158 rows each. This looks like a duplicate. Should I dedupe by SKU+period within that file, or are they intended to be different subsets?

**3. Category data is missing** for WK47 and WK52 2024 sources. The 2024 line lists don't have a Marketing Category column (just brand/model/product description). The existing SKU table requires a Category field. Do you want me to leave that blank for those rows, or try to infer it from the product description?

**4. The WK52 Final Days sheets** contain 316 rows after deduping within the file, but many of these will already exist in the current SKU table under "EOFY 2025". The dedup logic I'll apply is: exact match on SKU number + sale event + sale period. Anything where those three match gets dropped.

Quick confirm on these before I write the file?
