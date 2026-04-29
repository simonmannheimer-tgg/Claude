---
title: Product metafield feature breakdown and comma detection (full)
parent: Chat/Light/2026-04-08-product-metafield-feature-breakdown-and-comma-detection-97af9d
uuid: 97af9d93-8a49-47c8-91a7-c5c8410fcb7a
---

#chat/full #project/main #status/completed

# Product metafield feature breakdown and comma detection — Full Transcript

→ Light view: [[Chat/Light/2026-04-08-product-metafield-feature-breakdown-and-comma-detection-97af9d]]
→ Medium view: [[Chat/Medium/2026-04-08-product-metafield-feature-breakdown-and-comma-detection-97af9d]]

**Messages:** 2 | **Date:** 2026-04-08

---

### 1. **Human** — 2026-04-08T06:54

I need you to break down the key features for each product as per the metafield, and flag in which there is a comma:

you can do better formatting than me, but thats the jist of it, goal is to understand how large this issue is (see mhtml)
I need you to break down the key features for each product as per the metafield, and flag in which there is a comma:

you can do better formatting than me, but thats the jist of it, goal is to understand how large this issue is (see mhtml)

---

### 2. **Claude** — 2026-04-08T06:56

I'll read the files to understand the data structure and the comma issue you're flagging.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me read the CSV to see what columns you're working with:
```
This block is not supported on your current device yet.
```

Now let me read the Excel export to understand the full data:
```
This block is not supported on your current device yet.
```

Now I understand. You want to analyze the `Metafield: tgg.key_features [json]` column to identify which products have commas in their key features. Let me build a comprehensive analysis:
```
This block is not supported on your current device yet.
```

Now let me create a more detailed visual breakdown showing the patterns:
```
This block is not supported on your current device yet.
```

Now let me create the final formatted output file:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

## The Issue Is Massive

**63% of your products** (5,289 out of 8,390) have at least one key feature containing a comma. That's the scale.

### Hard Numbers

- **31,555 total key features** analyzed across 8,390 products
- **10,280 features contain commas** (32.6%)
- **5,289 products affected** (63.0% of catalog)

### The Real Problem

You're seeing this as a "bulk replace" issue. It's not. The comma serves different functions across your feed:

1. **List separators** (1,695 features): "Touch controls, easy installation, dishwasher safe filters"
2. **Spec separators** (1,327 features): "14.5-70 PSI, 2 Bowls 32 Litre Capacity"
3. **Registration numbers** (307 features): "WELS 5 Star 6L per min, REG #T42148"
4. **Capacity measurements** (1,402 features): "390 Litre fridge, 250 Litre freezer"

If you blindly replace all commas, you'll destroy readability. If you selectively replace, you need pattern rules.

### What Intelligent Reach Already Told You

They can't change the delimiter from comma to pipe. They implemented a **targeted workaround** for refrigeration capacity patterns. That's the only approach that works: **identify the structural patterns causing breaks, then transform those specific patterns only**.

### What You Should Do

1. Accept that there's no universal "comma replacement symbol" that won't register as a linebreak
2. Catalog the specific patterns causing feed breaks (refrigeration specs, WELS ratings, etc.)
3. Work with Intelligent Reach to apply targeted transformations per pattern type
4. Don't ask for a "bulk replace" solution. It doesn't exist for this problem.

The workbook breaks down all 10,280 comma-containing features by product, pattern type, and comma count so you can identify which structural patterns need transformation rules.
 I'll read the files to understand the data structure and the comma issue you're flagging.
Now let me read the CSV to see what columns you're working with:
Now let me read the Excel export to understand the full data:
Now I understand. You want to analyze the `Metafield: tgg.key_features [json]` column to identify which products have commas in their key features. Let me build a comprehensive analysis:
Now let me create a more detailed visual breakdown showing the patterns:
Now let me create the final formatted output file:
## The Issue Is Massive

**63% of your products** (5,289 out of 8,390) have at least one key feature containing a comma. That's the scale.

### Hard Numbers

- **31,555 total key features** analyzed across 8,390 products
- **10,280 features contain commas** (32.6%)
- **5,289 products affected** (63.0% of catalog)

### The Real Problem

You're seeing this as a "bulk replace" issue. It's not. The comma serves different functions across your feed:

1. **List separators** (1,695 features): "Touch controls, easy installation, dishwasher safe filters"
2. **Spec separators** (1,327 features): "14.5-70 PSI, 2 Bowls 32 Litre Capacity"
3. **Registration numbers** (307 features): "WELS 5 Star 6L per min, REG #T42148"
4. **Capacity measurements** (1,402 features): "390 Litre fridge, 250 Litre freezer"

If you blindly replace all commas, you'll destroy readability. If you selectively replace, you need pattern rules.

### What Intelligent Reach Already Told You

They can't change the delimiter from comma to pipe. They implemented a **targeted workaround** for refrigeration capacity patterns. That's the only approach that works: **identify the structural patterns causing breaks, then transform those specific patterns only**.

### What You Should Do

1. Accept that there's no universal "comma replacement symbol" that won't register as a linebreak
2. Catalog the specific patterns causing feed breaks (refrigeration specs, WELS ratings, etc.)
3. Work with Intelligent Reach to apply targeted transformations per pattern type
4. Don't ask for a "bulk replace" solution. It doesn't exist for this problem.

The workbook breaks down all 10,280 comma-containing features by product, pattern type, and comma count so you can identify which structural patterns need transformation rules.
