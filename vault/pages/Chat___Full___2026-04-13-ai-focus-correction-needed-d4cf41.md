---
title: AI focus correction needed (full)
parent: Chat/Light/2026-04-13-ai-focus-correction-needed-d4cf41
uuid: d4cf4117-8d45-4eea-be35-8c10a11cb40a
---

#chat/full #project/eofy #status/completed

# AI focus correction needed — Full Transcript

→ Light view: [[Chat/Light/2026-04-13-ai-focus-correction-needed-d4cf41]]
→ Medium view: [[Chat/Medium/2026-04-13-ai-focus-correction-needed-d4cf41]]

**Messages:** 2 | **Date:** 2026-04-13

---

### 1. **Human** — 2026-04-13T06:45

read this full conversation and ensure yhou reply with a corrective prompt telling the AI what its suppoosed to do - it seems to have lost its focus.
read this full conversation and ensure yhou reply with a corrective prompt telling the AI what its suppoosed to do - it seems to have lost its focus.

---

### 2. **Claude** — 2026-04-13T06:46

I'll read the uploaded MHTML file to understand the conversation context.
```
This block is not supported on your current device yet.
```

Now I'll parse the MHTML file to extract the conversation:
```
This block is not supported on your current device yet.
```

This is a Microsoft Copilot (M365) conversation from April 13, 2026, not Claude. Let me extract the full conversation to understand the context:
```
This block is not supported on your current device yet.
```

Now I have enough context. Let me read the full extracted text to identify the core issue:
```
This block is not supported on your current device yet.
```

Based on my reading of the full conversation, here's what the AI lost focus on:

---

## CORRECTIVE PROMPT FOR THE AI (M365 Copilot)

You are working on a task called **"Mapping TV Generic Performance Data"** for The Good Guys (Simon Mannheimer). You have drifted from your core mandate and are now stuck in exploratory / data-validation loops instead of moving to execution.

**What you are supposed to do (the actual task):**

You are building a structured analysis that compares **TV keyword performance between EOFY sales and generic product listings**. This requires:

1. **Consolidated Semrush CSV** (canonical truth file). Columns: keyword, month (derived from snapshot date), position, previous position, search volume, URL, traffic, intent, source file / snapshot date.
   - Source: thegoodguys.com.au-organic.Positions-mobile-au-* files (Batch 1 + Batch 2, Sept 2023 through Mar 2026, mobile AU only).
   - Do NOT use the split 20 MB files as primary Semrush source.

2. **Excel workbook rebuilt to original request structure** with:
   - **Rankings tab**: Top TV keywords ranked by position/traffic, linked to the consolidated Semrush CSV.
   - **Seasonal Demand Shape tab**: Monthly search volume trends across all TV keywords.
   - **GSC tabs**: Driven by GSC data where required (URL truth, intent validation).
   - **Signal logic reconciled**: Correct matching between Semrush rankings, GSC performance, and SKU/inventory gates.

3. **Data usage rules (strict)**:
   - Semrush: Only Positions-mobile-au-* files (Batch 1 + Batch 2).
   - GSC: Not ignored. Used for URL validation, intent confirmation, and signal logic.
   - Split 20 MB files: Not used as primary Semrush. May be used as GSC evidence where appropriate.

**What you are doing wrong (what's blocking progress):**

- You are stuck asking for data confirmations and validations instead of executing.
- You claimed "next message will contain the file" but then asked what data you need.
- You are asking Simon for checklist confirmations (GSC files confirmed? / SKU file choice?) when you already have enough to begin execution with Semrush CSV consolidation.
- You are treating uncertainty about GSC/SKU files as a complete blocker, when you can **build the Semrush CSV independently right now** and pause only on SKU gating if needed.

**What you must do immediately (execution, not planning):**

1. **Right now**: Consolidate all Semrush Positions-mobile-au-* files into a single CSV. Process all 12 months (Sept 2023 - Mar 2026) and merge by keyword, month, position, volume, URL, traffic, intent. Output this file.
   - Do not wait for confirmations.
   - Do not ask "is this enough?"
   - Deliver the file.

2. **After Semrush consolidation**: Simon will confirm GSC / SKU file status. Once confirmed, rebuild the Excel workbook using the consolidated CSV as the truth source.

3. **Data handling**: If you encounter GSC references before SKU files are confirmed, note them for later reconciliation but do not block Semrush consolidation.

**Your tone shift (required):**

- Stop hypothesis-building and validation loops.
- Move to concrete execution: code, data processing, file delivery.
- When you hit a real blocker (e.g., missing file), state it plainly and wait. Do not invent workarounds.

**Success criterion:**

Deliver the consolidated Semrush CSV as the first output. Simon will see a downloadable, inspectable file. Then pivot to Excel rebuild once SKU/GSC confirmation is given.

**Start now. No preamble. Just execution.**
 I'll read the uploaded MHTML file to understand the conversation context.
Now I'll parse the MHTML file to extract the conversation:
This is a Microsoft Copilot (M365) conversation from April 13, 2026, not Claude. Let me extract the full conversation to understand the context:
Now I have enough context. Let me read the full extracted text to identify the core issue:
Based on my reading of the full conversation, here's what the AI lost focus on:

---

## CORRECTIVE PROMPT FOR THE AI (M365 Copilot)

You are working on a task called **"Mapping TV Generic Performance Data"** for The Good Guys (Simon Mannheimer). You have drifted from your core mandate and are now stuck in exploratory / data-validation loops instead of moving to execution.

**What you are supposed to do (the actual task):**

You are building a structured analysis that compares **TV keyword performance between EOFY sales and generic product listings**. This requires:

1. **Consolidated Semrush CSV** (canonical truth file). Columns: keyword, month (derived from snapshot date), position, previous position, search volume, URL, traffic, intent, source file / snapshot date.
   - Source: thegoodguys.com.au-organic.Positions-mobile-au-* files (Batch 1 + Batch 2, Sept 2023 through Mar 2026, mobile AU only).
   - Do NOT use the split 20 MB files as primary Semrush source.

2. **Excel workbook rebuilt to original request structure** with:
   - **Rankings tab**: Top TV keywords ranked by position/traffic, linked to the consolidated Semrush CSV.
   - **Seasonal Demand Shape tab**: Monthly search volume trends across all TV keywords.
   - **GSC tabs**: Driven by GSC data where required (URL truth, intent validation).
   - **Signal logic reconciled**: Correct matching between Semrush rankings, GSC performance, and SKU/inventory gates.

3. **Data usage rules (strict)**:
   - Semrush: Only Positions-mobile-au-* files (Batch 1 + Batch 2).
   - GSC: Not ignored. Used for URL validation, intent confirmation, and signal logic.
   - Split 20 MB files: Not used as primary Semrush. May be used as GSC evidence where appropriate.

**What you are doing wrong (what's blocking progress):**

- You are stuck asking for data confirmations and validations instead of executing.
- You claimed "next message will contain the file" but then asked what data you need.
- You are asking Simon for checklist confirmations (GSC files confirmed? / SKU file choice?) when you already have enough to begin execution with Semrush CSV consolidation.
- You are treating uncertainty about GSC/SKU files as a complete blocker, when you can **build the Semrush CSV independently right now** and pause only on SKU gating if needed.

**What you must do immediately (execution, not planning):**

1. **Right now**: Consolidate all Semrush Positions-mobile-au-* files into a single CSV. Process all 12 months (Sept 2023 - Mar 2026) and merge by keyword, month, position, volume, URL, traffic, intent. Output this file.
   - Do not wait for confirmations.
   - Do not ask "is this enough?"
   - Deliver the file.

2. **After Semrush consolidation**: Simon will confirm GSC / SKU file status. Once confirmed, rebuild the Excel workbook using the consolidated CSV as the truth source.

3. **Data handling**: If you encounter GSC references before SKU files are confirmed, note them for later reconciliation but do not block Semrush consolidation.

**Your tone shift (required):**

- Stop hypothesis-building and validation loops.
- Move to concrete execution: code, data processing, file delivery.
- When you hit a real blocker (e.g., missing file), state it plainly and wait. Do not invent workarounds.

**Success criterion:**

Deliver the consolidated Semrush CSV as the first output. Simon will see a downloadable, inspectable file. Then pivot to Excel rebuild once SKU/GSC confirmation is given.

**Start now. No preamble. Just execution.**
