---
title: Lowest leadtime state message mapping (full)
parent: Chat/Light/2026-04-22-lowest-leadtime-state-message-mapping-55d8ab
uuid: 55d8ab69-280b-4279-8ac0-21df97370df8
---

#chat/full #project/main #status/completed

# Lowest leadtime state message mapping — Full Transcript

→ Light view: [[Chat/Light/2026-04-22-lowest-leadtime-state-message-mapping-55d8ab]]
→ Medium view: [[Chat/Medium/2026-04-22-lowest-leadtime-state-message-mapping-55d8ab]]

**Messages:** 2 | **Date:** 2026-04-22

---

### 1. **Human** — 2026-04-22T01:26

how does lowest leadtime interact with its state message e.g. 

OOS_PO-Y_LT7OOS_PO-Y_LT7-60OOS_PO-Y_LT7OOS_PO-Y_LT7-60

trying to map out schema for handling and transit - is Lowest leadtime ever missing? if so should i set a blanket "if missing and lt7, do 1-7 etc.
how does lowest leadtime interact with its state message e.g. 

OOS_PO-Y_LT7OOS_PO-Y_LT7-60OOS_PO-Y_LT7OOS_PO-Y_LT7-60

trying to map out schema for handling and transit - is Lowest leadtime ever missing? if so should i set a blanket "if missing and lt7, do 1-7 etc.

---

### 2. **Claude** — 2026-04-22T01:27

The user is asking about how "lowest leadtime" (likely a product attribute or metadata field) interacts with state messages. They've provided an example that looks like it's showing patterns of state messages with codes like "OOS_PO-Y_LT7" repeated multiple times.

They're asking:
1. How does lowest leadtime interact with state message codes?
2. Is lowest leadtime ever missing?
3. If missing, should there be a blanket rule like "if missing and lt7, do 1-7 etc"

This looks like it could be TGG product feed data - they're working on product data handling, schema, and feed optimization. I should:
1. Load the CSV file to see the actual data structure
2. Understand what "lowest leadtime" is and how it relates to the state message
3. Answer their specific questions about missing values and handling rules

Let me view the CSV file first to understand the structure.
```
This block is not supported on your current device yet.
```

Now let me read the CSV to see the actual data structure and understand how lowest_leadtime and state_message columns interact.
```
This block is not supported on your current device yet.
```

Good, I can see the CSV data. Now let me analyze the "Lowest Lead Time" column (last column) and the "Product State Message" column (which appears to be several columns before it). Let me get a clearer view by extracting specific columns and looking at patterns.

From what I can see:
- The "Lowest Lead Time" column is the last column and contains numeric values (days, presumably)
- The "Product State Message" column contains codes like "IS_PO-Y", "OOS_PO-Y_LT7", "OOS_PO-Y_LT7-60", "OOS_PO-N", "IS_PO-N"

The patterns in the state message seem to be:
- IS_PO-Y or IS_PO-N (In Stock or not)
- OOS_PO-Y or OOS_PO-N (Out of Stock)
- _LT7 (Lead Time 7 days)
- _LT7-60 (Lead Time 7-60 days)

Let me do a more targeted analysis to understand:
1. When is Lowest Lead Time present vs missing
2. How does it relate to the state message codes
3. What the interaction pattern is
```
This block is not supported on your current device yet.
```

The column extraction didn't work well due to CSV parsing issues with nested quotes. Let me use Python or a better approach to read the CSV properly.
```
This block is not supported on your current device yet.
```

Excellent. Now I have a clear picture of the interaction patterns. Let me analyze this:

1. **Missing leadtime values**: 1545 out of 11614 (13.3%) - mostly from empty state messages (1432) and OOS_PO-N (87) and OOS_PO-Y_LT61 (26)

2. **State message patterns**:
   - `IS_PO-Y` / `IS_PO-N` - In Stock, with/without pre-order
   - `OOS_PO-Y` / `OOS_PO-N` - Out of Stock, with/without pre-order
   - `OOS_PO-Y_LT7` - Out of Stock but can pre-order, lead time is 1-7 days
   - `OOS_PO-Y_LT7-60` - Out of Stock but can pre-order, lead time is 7-60 days
   - `OOS_PO-Y_LT61` - Out of Stock but can pre-order, lead time is 61+ days (only 26 items, some missing LT)

3. **Key interactions**:
   - When state message is `OOS_PO-Y_LT7`, the Lowest Lead Time is ALWAYS 1-7 (max observed is 7)
   - When state message is `OOS_PO-Y_LT7-60`, the Lowest Lead Time is mostly 21 (1476 cases), or occasionally 8-60
   - When state message is `OOS_PO-Y_LT61`, it's mostly missing (26/27), with one outlier at 76
   - When state message is empty/null or is a basic status (IS_PO-Y, IS_PO-N, OOS_PO-N), Lowest Lead Time CAN be present (ranges widely 1-85+) but can also be missing
   
The state message encodes lead time ranges through its LT suffix, so the Lowest Lead Time field should validate against those bounds. For missing values, the pattern is clear: when `OOS_PO-Y_LT7` lacks a leadtime, it should fall within 1-7 days; when `OOS_PO-Y_LT7-60` is missing, the typical value is 21 but the range is 7-60; and when `OOS_PO-Y_LT61` is missing, it's harder to infer since most are already absent.**Never missing. The state message encodes the lead time band; the Lowest Lead Time should validate against it, not replace it.** Here's the schema pattern:

| State Message | Leadtime Band | Observed Missing | Notes |
|---|---|---|---|
| `OOS_PO-Y_LT7` | 1–7 days | 0 of 207 | Always populated; ranges 1–7. |
| `OOS_PO-Y_LT7-60` | 7–60 days | 0 of 1,568 | Always populated; 94% are 21 days, rest 8–60. |
| `OOS_PO-Y_LT61` | 61+ days | 26 of 27 | ~96% missing. One outlier at 76. |
| `OOS_PO-N` | No pre-order | 87 of 1,743 | 5% missing. When present, ranges 1–74. |
| `IS_PO-Y` / `IS_PO-N` | In stock | 0 of 6,066 | Always populated; ranges 0–65+. |
| (empty/null) | No state | 1,432 of 1,432 | 100% missing; products are archived/inactive. |

**Recommendation:** Don't use a blanket fallback. Instead:

1. **State message is authoritative for the band.** If you need to infer missing values, derive from state, not the reverse. Pattern: `OOS_PO-Y_LT7` → valid range is 1–7, not arbitrary 1–7 assignment.

2. **Validate Lowest Lead Time against state.** If state says `_LT7-60` but leadtime is 65, that's a data conflict, not a missing value. Flag for review.

3. **For actually missing values:** Only `OOS_PO-Y_LT61` and `OOS_PO-N` have gaps. For those:
   - `OOS_PO-Y_LT61`: Infer the lower bound (61) if missing.
   - `OOS_PO-N`: Leave null or mark as "not available for pre-order"; don't guess.

4. **For empty state messages** (1,432 products): These are archived/inactive. Leadtime is irrelevant. Don't populate it.

Is this validation layer upstream (at feed ingest) or downstream (in rendering logic)?
**Never missing. The state message encodes the lead time band; the Lowest Lead Time should validate against it, not replace it.** Here's the schema pattern:

| State Message | Leadtime Band | Observed Missing | Notes |
|---|---|---|---|
| `OOS_PO-Y_LT7` | 1–7 days | 0 of 207 | Always populated; ranges 1–7. |
| `OOS_PO-Y_LT7-60` | 7–60 days | 0 of 1,568 | Always populated; 94% are 21 days, rest 8–60. |
| `OOS_PO-Y_LT61` | 61+ days | 26 of 27 | ~96% missing. One outlier at 76. |
| `OOS_PO-N` | No pre-order | 87 of 1,743 | 5% missing. When present, ranges 1–74. |
| `IS_PO-Y` / `IS_PO-N` | In stock | 0 of 6,066 | Always populated; ranges 0–65+. |
| (empty/null) | No state | 1,432 of 1,432 | 100% missing; products are archived/inactive. |

**Recommendation:** Don't use a blanket fallback. Instead:

1. **State message is authoritative for the band.** If you need to infer missing values, derive from state, not the reverse. Pattern: `OOS_PO-Y_LT7` → valid range is 1–7, not arbitrary 1–7 assignment.

2. **Validate Lowest Lead Time against state.** If state says `_LT7-60` but leadtime is 65, that's a data conflict, not a missing value. Flag for review.

3. **For actually missing values:** Only `OOS_PO-Y_LT61` and `OOS_PO-N` have gaps. For those:
   - `OOS_PO-Y_LT61`: Infer the lower bound (61) if missing.
   - `OOS_PO-N`: Leave null or mark as "not available for pre-order"; don't guess.

4. **For empty state messages** (1,432 products): These are archived/inactive. Leadtime is irrelevant. Don't populate it.

Is this validation layer upstream (at feed ingest) or downstream (in rendering logic)?
