---
title: Checking product highlight comma separation (full)
parent: Chat/Light/2026-03-31-checking-product-highlight-comma-separation-70a4c2
uuid: 70a4c27b-e9ad-468c-8dc9-48c325219571
---

#chat/full #project/main #status/completed

# Checking product highlight comma separation — Full Transcript

→ Light view: [[Chat/Light/2026-03-31-checking-product-highlight-comma-separation-70a4c2]]
→ Medium view: [[Chat/Medium/2026-03-31-checking-product-highlight-comma-separation-70a4c2]]

**Messages:** 2 | **Date:** 2026-03-31

---

### 1. **Human** — 2026-03-31T05:45

I need you to check product_highlight in this sheet for comma separation issues - refer to this conversation:
I need you to check product_highlight in this sheet for comma separation issues - refer to this conversation:

---

### 2. **Claude** — 2026-03-31T05:46

I'll read the spreadsheet and check for the comma delimiter issue in product_highlight values.
```
This block is not supported on your current device yet.
```

Now I'll load the XLSX skill to properly read and analyse the spreadsheet.
```
This block is not supported on your current device yet.
```

Now I'll load and analyse the spreadsheet with pandas to check for comma delimiter issues in the product_highlight column.
```
This block is not supported on your current device yet.
```

Now let me get a better breakdown of the comma pattern and identify SKUs that match the specific fridge/freezer pattern mentioned in the Searchspring ticket.
```
This block is not supported on your current device yet.
```

Perfect. Now I'll create a comprehensive analysis document with the before/after export that you can send to Searchspring.
```
This block is not supported on your current device yet.
```

Now I'll create a professional summary document that you can send to Searchspring.
```
This block is not supported on your current device yet.
```

Now I'll present both files to you.
```
This block is not supported on your current device yet.
```

## Summary

Your product_highlight column has **140 SKUs** affected by the comma delimiter issue — exactly matching the scale Searchspring identified. All affected products are refrigeration models where capacity specs are split between fridge and freezer compartments.

The before/after export shows the fix is clean and safe. Replacing `Litre fridge, Litre freezer` with `Litre fridge and Litre freezer` is:

- **Linguistically correct** — preserves meaning and product specifications
- **Isolated** — affects only 2.1% of your feed (140 of 6,520 SKUs)
- **Semantically valid** — commas here are natural-language conjunctions between independent clauses, not field delimiters

The analysis document and CSV provide everything Searchspring needs to move forward with confidence on implementation. You can send both files to them as your pre-approval validation.
 I'll read the spreadsheet and check for the comma delimiter issue in product_highlight values.
Now I'll load the XLSX skill to properly read and analyse the spreadsheet.
Now I'll load and analyse the spreadsheet with pandas to check for comma delimiter issues in the product_highlight column.
Now let me get a better breakdown of the comma pattern and identify SKUs that match the specific fridge/freezer pattern mentioned in the Searchspring ticket.
Perfect. Now I'll create a comprehensive analysis document with the before/after export that you can send to Searchspring.
Now I'll create a professional summary document that you can send to Searchspring.
Now I'll present both files to you.
## Summary

Your product_highlight column has **140 SKUs** affected by the comma delimiter issue — exactly matching the scale Searchspring identified. All affected products are refrigeration models where capacity specs are split between fridge and freezer compartments.

The before/after export shows the fix is clean and safe. Replacing `Litre fridge, Litre freezer` with `Litre fridge and Litre freezer` is:

- **Linguistically correct** — preserves meaning and product specifications
- **Isolated** — affects only 2.1% of your feed (140 of 6,520 SKUs)
- **Semantically valid** — commas here are natural-language conjunctions between independent clauses, not field delimiters

The analysis document and CSV provide everything Searchspring needs to move forward with confidence on implementation. You can send both files to them as your pre-approval validation.
