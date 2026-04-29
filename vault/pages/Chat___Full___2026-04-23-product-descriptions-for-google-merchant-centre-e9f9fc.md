---
title: Product descriptions for Google Merchant Centre (full)
parent: Chat/Light/2026-04-23-product-descriptions-for-google-merchant-centre-e9f9fc
uuid: e9f9fc9c-5773-4ca2-87ac-08dfb64fe131
---

#chat/full #project/main #status/active

# Product descriptions for Google Merchant Centre — Full Transcript

→ Light view: [[Chat/Light/2026-04-23-product-descriptions-for-google-merchant-centre-e9f9fc]]
→ Medium view: [[Chat/Medium/2026-04-23-product-descriptions-for-google-merchant-centre-e9f9fc]]

**Messages:** 7 | **Date:** 2026-04-23

---

### 1. **Human** — 2026-04-23T03:10

You are writing product descriptions for Google Merchant Centre. The descriptions must perform on three axes:
- Google Shopping relevance and attribute extraction
- Shopper conversion (clear, benefit-led prose)
- Conversational commerce — natural real-life usage context
==================== BATCH INSTRUCTIONS ====================
You will be given a CSV or list of products. Process every product row by row without stopping. Do not ask for clarification. Do not ask to confirm scope. Do not stop early. If a product page has insufficient data to reach 90 words after applying all suppression rules, write what you can and append DATA-INSUFFICIENT at the end of that description rather than inventing content.
Output a CSV with columns: index, h1, model, colour, warranty, description.
==================== INPUT ====================
Below are product page HTML files. Each HTML file is the full page extract — treat it as the {CUSTOM_EXTRACTOR2} input. Do not reuse or paraphrase the existing product description found on the page. Write entirely from the structured spec data in the HTML.
STEP 1 — EXTRACT (internal, do not output)
Before writing, pull the following from the HTML. If a field is not clearly stated, mark it as MISSING and do NOT invent it.
- Brand
- Product heading — the exact H1 or page title as it appears on the page
- Model number — the alphanumeric part number (SKU), not the marketing name. Found in the spec table, labelled model number, part number, or item number. Contains a mix of letters and numbers (e.g., RR-Q7BP52-03-BLK, 508973, IZ373HANZ). The marketing name is not the model number: Q7B+ is a marketing name; CX True Wireless is a marketing name. If no alphanumeric SKU can be found, mark as MODEL-MISSING.
- Headline capacity or size (L, kg, cm, inches, etc.)
- Colour or finish
- Energy / water / star rating (if applicable)
- Core technology or standout feature (1–2 max)
- Convenience and safety features (only those that affect a buying decision)
- Physical dimensions (only if they affect fit or installation)
- Warranty length — numeric duration only (e.g., 2 year, 3 year). If warranty is mentioned but no duration is stated, mark as WARRANTY-DURATION-MISSING. If not mentioned at all, mark as WARRANTY-MISSING.
- Any manufacturer-stated use case or target user
Suppression rules:
- If a feature is marked No, N/A, or Not Available — suppress it entirely.
- If an energy or water rating is below 4 stars — do not include it.
- If a field is not clearly stated — do not include it. Do not infer or fill from general knowledge.
- Ignore: customer reviews, ratings, customers also bought, delivery/returns/finance copy, price, promotions, competitor mentions.
STEP 2 — ACCURACY VERIFICATION (internal, do not output)
Before writing, check every claim you intend to make:
- Does this feature appear explicitly in the HTML? If not, exclude it.
- Does the description contradict the attribute value? If so, correct or remove it.
- Am I converting units correctly? Verify before including.
- Am I using a synonym or shorthand that changes the meaning? Examples: Full HD when the spec says HD Ready; 5G when the connectivity spec says Wi-Fi. Connectivity type must be reproduced exactly.
- If any critical field cannot be verified, do not include it.
STEP 3 — WRITE
HARD RULES:
- Use ONLY facts from the HTML. Do not reuse, paraphrase, or echo the existing description.
- Australian English: colour, optimise, centre, metre, fibre.
- Plain prose paragraphs. No bullets, headings, markdown, emoji, all-caps, or em dashes.
- Length: 90–150 words total. If the page has insufficient verified data to reach 90 words, write what you can and append DATA-INSUFFICIENT.
- No pricing, promotions, shipping or stock claims.
- No competitor names, comparative claims, or unverifiable superlatives.
- No filler: amazing, revolutionary, stunning, ultimate, perfect, premium, cutting-edge, state-of-the-art, game-changing.
PRODUCT-TYPE RULE — HEADPHONES AND EARBUDS ONLY:
Battery life must appear in the opening sentence or as a grammatically complete sentence immediately following it. Not a fragment.
- AVOID: The Sennheiser 27-hour CX True Wireless delivers... (battery life mid-title)
- AVOID standalone: Up to 27 hours battery life including the charging case. (no verb)
- DO: The Sennheiser CX True Wireless delivers crystal-clear audio for up to 27 hours with the charging case.
OPENING SENTENCE RULES:
- Begin with The, This, or A. Never with an imperative verb, gerund, question, or product feature.
- Use the product heading exactly as it appears on the page. Do not reconstruct, abbreviate, or reorder it.
- Always include the brand name. It is not optional and may not be dropped for length.
- TGG product headings naturally include specs as part of the product name (e.g., "Solt 9kg Front Load Washer", "Westinghouse 60cm Stainless Steel 14 Place Freestanding Dishwasher"). Reproduce these headings exactly — specs embedded in the H1 are part of the product name and are correct to include. Do not restate those same specs again later in the description.
- Any additional specs beyond what is already in the H1 (e.g., energy rating, features, accessories) should appear after the opening sentence, not inserted into it.
- Be a grammatically complete, definitive statement.
- AVOID: The Sunbeam Single fitted antibacterial electric blanket... (H1 not reproduced — Sleep Perfect missing)
- AVOID: This 60cm dishwasher handles... (brand dropped)
- DO: The Sunbeam Sleep Perfect Fitted Antibacterial Electric Blanket Single provides...
- DO: The Solt 9kg Front Load Washer handles large household loads while saving water and energy.
- DO: The Westinghouse 60cm Stainless Steel 14 Place Freestanding Dishwasher suits family kitchens and households that entertain.
SENTENCE & CLAUSE CONSTRUCTION
You are writing product descriptions for Google Merchant Centre. The descriptions must perform on three axes:
- Google Shopping relevance and attribute extraction
- Shopper conversion (clear, benefit-led prose)
- Conversational commerce — natural real-life usage context
==================== BATCH INSTRUCTIONS ====================
You will be given a CSV or list of products. Process every product row by row without stopping. Do not ask for clarification. Do not ask to confirm scope. Do not stop early. If a product page has insufficient data to reach 90 words after applying all suppression rules, write what you can and append DATA-INSUFFICIENT at the end of that description rather than inventing content.
Output a CSV with columns: index, h1, model, colour, warranty, description.
==================== INPUT ====================
Below are product page HTML files. Each HTML file is the full page extract — treat it as the {CUSTOM_EXTRACTOR2} input. Do not reuse or paraphrase the existing product description found on the page. Write entirely from the structured spec data in the HTML.
STEP 1 — EXTRACT (internal, do not output)
Before writing, pull the following from the HTML. If a field is not clearly stated, mark it as MISSING and do NOT invent it.
- Brand
- Product heading — the exact H1 or page title as it appears on the page
- Model number — the alphanumeric part number (SKU), not the marketing name. Found in the spec table, labelled model number, part number, or item number. Contains a mix of letters and numbers (e.g., RR-Q7BP52-03-BLK, 508973, IZ373HANZ). The marketing name is not the model number: Q7B+ is a marketing name; CX True Wireless is a marketing name. If no alphanumeric SKU can be found, mark as MODEL-MISSING.
- Headline capacity or size (L, kg, cm, inches, etc.)
- Colour or finish
- Energy / water / star rating (if applicable)
- Core technology or standout feature (1–2 max)
- Convenience and safety features (only those that affect a buying decision)
- Physical dimensions (only if they affect fit or installation)
- Warranty length — numeric duration only (e.g., 2 year, 3 year). If warranty is mentioned but no duration is stated, mark as WARRANTY-DURATION-MISSING. If not mentioned at all, mark as WARRANTY-MISSING.
- Any manufacturer-stated use case or target user
Suppression rules:
- If a feature is marked No, N/A, or Not Available — suppress it entirely.
- If an energy or water rating is below 4 stars — do not include it.
- If a field is not clearly stated — do not include it. Do not infer or fill from general knowledge.
- Ignore: customer reviews, ratings, customers also bought, delivery/returns/finance copy, price, promotions, competitor mentions.
STEP 2 — ACCURACY VERIFICATION (internal, do not output)
Before writing, check every claim you intend to make:
- Does this feature appear explicitly in the HTML? If not, exclude it.
- Does the description contradict the attribute value? If so, correct or remove it.
- Am I converting units correctly? Verify before including.
- Am I using a synonym or shorthand that changes the meaning? Examples: Full HD when the spec says HD Ready; 5G when the connectivity spec says Wi-Fi. Connectivity type must be reproduced exactly.
- If any critical field cannot be verified, do not include it.
STEP 3 — WRITE
HARD RULES:
- Use ONLY facts from the HTML. Do not reuse, paraphrase, or echo the existing description.
- Australian English: colour, optimise, centre, metre, fibre.
- Plain prose paragraphs. No bullets, headings, markdown, emoji, all-caps, or em dashes.
- Length: 90–150 words total. If the page has insufficient verified data to reach 90 words, write what you can and append DATA-INSUFFICIENT.
- No pricing, promotions, shipping or stock claims.
- No competitor names, comparative claims, or unverifiable superlatives.
- No filler: amazing, revolutionary, stunning, ultimate, perfect, premium, cutting-edge, state-of-the-art, game-changing.
PRODUCT-TYPE RULE — HEADPHONES AND EARBUDS ONLY:
Battery life must appear in the opening sentence or as a grammatically complete sentence immediately following it. Not a fragment.
- AVOID: The Sennheiser 27-hour CX True Wireless delivers... (battery life mid-title)
- AVOID standalone: Up to 27 hours battery life including the charging case. (no verb)
- DO: The Sennheiser CX True Wireless delivers crystal-clear audio for up to 27 hours with the charging case.
OPENING SENTENCE RULES:
- Begin with The, This, or A. Never with an imperative verb, gerund, question, or product feature.
- Use the product heading exactly as it appears on the page. Do not reconstruct, abbreviate, or reorder it.
- Always include the brand name. It is not optional and may not be dropped for length.
- TGG product headings naturally include specs as part of the product name (e.g., "Solt 9kg Front Load Washer", "Westinghouse 60cm Stainless Steel 14 Place Freestanding Dishwasher"). Reproduce these headings exactly — specs embedded in the H1 are part of the product name and are correct to include. Do not restate those same specs again later in the description.
- Any additional specs beyond what is already in the H1 (e.g., energy rating, features, accessories) should appear after the opening sentence, not inserted into it.
- Be a grammatically complete, definitive statement.
- AVOID: The Sunbeam Single fitted antibacterial electric blanket... (H1 not reproduced — Sleep Perfect missing)
- AVOID: This 60cm dishwasher handles... (brand dropped)
- DO: The Sunbeam Sleep Perfect Fitted Antibacterial Electric Blanket Single provides...
- DO: The Solt 9kg Front Load Washer handles large household loads while saving water and energy.
- DO: The Westinghouse 60cm Stainless Steel 14 Place Freestanding Dishwasher suits family kitchens and households that entertain.
SENTENCE & CLAUSE CONSTRUCTION

---

### 2. **Claude** — 2026-04-23T03:10

I'll process this batch according to your specifications. Let me first extract and verify the uploaded files.
```
This block is not supported on your current device yet.
```

 I'll process this batch according to your specifications. Let me first extract and verify the uploaded files.

---

### 3. **Human** — 2026-04-23T03:11

```
You are writing product descriptions for Google Merchant Centre. The descriptions must perform on three axes:
- Google Shopping relevance and attribute extraction
- Shopper conversion (clear, benefit-led prose)
- Conversational commerce — natural real-life usage context

==================== SCOPE ====================
You have been given HTML files for multiple product pages. Process every product. Do not stop. Do not ask for clarification. Do not ask to confirm scope. Deliver all descriptions in a single CSV with columns: index, h1, model, colour, warranty, description.

Do not reuse, paraphrase, or edit the existing product description from the page. Write every description from scratch using only the product specs and attributes in the HTML.

==================== PER PRODUCT — REPEAT FOR EACH ====================

STEP 1 — EXTRACT (internal, do not output)
Pull the following from the HTML. If a field is not clearly stated, mark it as MISSING. Do not invent it.

- Brand
- Product type / category
- Product heading — the exact H1 or page title as it appears on the page
- Model number — the alphanumeric part number (SKU), not the marketing name. Found in the spec table, labelled "model number", "part number", or "item number". Contains a mix of letters and numbers (e.g., RR-Q7BP52-03-BLK, 508973, IZ373HANZ). Marketing names are not model numbers: "Q7B+" is a marketing name; "CX True Wireless" is a marketing name. If no alphanumeric SKU is found, mark as MODEL-MISSING.
- Headline capacity or size (L, kg, cm, inches, etc.)
- Colour or finish
- Energy / water / star rating (if applicable)
- Core technology or standout feature (1–2 max)
- Convenience and safety features (only those that affect a buying decision)
- Physical dimensions (only if they affect fit or installation)
- Warranty length — numeric duration only (e.g., 2 year, 3 year). If warranty is mentioned but no duration stated, mark as WARRANTY-DURATION-MISSING. If not mentioned, mark as WARRANTY-MISSING.
- Any manufacturer-stated use case or target user

Suppression rules:
- If a feature is marked No, N/A, or Not Available — suppress it entirely.
- If an energy or water rating is below 4 stars — do not include it.
- If a field is not clearly stated — do not include it. Do not infer from general knowledge.
- Ignore: customer reviews, ratings, "customers also bought", delivery/returns/finance copy, price, promotions, competitor mentions.

STEP 2 — ACCURACY VERIFICATION (internal, do not output)
Before writing, check every claim:
- Does this feature appear explicitly in the HTML? If not, exclude it.
- Does my description contradict the attribute value? If so, correct or remove it.
- Am I converting units correctly? Verify before including.
- Am I using a synonym that changes the meaning? Example: "5G" when the spec says "Wi-Fi". Connectivity type must match exactly.
- If any critical field cannot be verified, do not include it.

STEP 3 — WRITE

HARD RULES:
- Use ONLY facts from the HTML. Do not reuse or adapt the existing product description.
- Australian English: colour, optimise, centre, metre, fibre.
- Plain prose paragraphs. No bullets, headings, markdown, emoji, all-caps, or em dashes.
- Length: 90–150 words total. If the page has genuinely sparse specs and 90 words cannot be reached without invention, write as many words as the verified facts support and flag the row as SPARSE-PAGE.
- No pricing, promotions, shipping or stock claims.
- No competitor names, comparative claims, or unverifiable superlatives.
- No filler: amazing, revolutionary, stunning, ultimate, perfect, premium, cutting-edge, state-of-the-art, game-changing.

PRODUCT-TYPE RULE — HEADPHONES AND EARBUDS ONLY:
Battery life must appear in the opening sentence or as a grammatically complete sentence immediately following it. Not a fragment.
- AVOID: The Sennheiser 27-hour CX True Wireless delivers... (battery life mid-title)
- AVOID standalone: Up to 27 hours battery life including the charging case. (no verb — fragment)
- DO: The Sennheiser CX True Wireless delivers crystal-clear audio for up to 27 hours with the charging case.

OPENING SENTENCE RULES:
- Begin with The, This, or A. Never with an imperative verb, a gerund, a question, or a product feature.
- Use the product heading exactly as it appears on the page. Do not reconstruct, abbreviate, or reorder it.
- Always include the brand name. It may not be dropped for length.
- Be a grammatically complete, definitive statement.
- AVOID: Tackle laundry day with... / Experience the convenience of... / Looking for a dryer...
- AVOID: The Sunbeam Single fitted antibacterial electric blanket... (H1 not reproduced — "Sleep Perfect" missing)
- DO: The Sunbeam Sleep Perfect Fitted Antibacterial Electric Blanket Single provides...
- DO: The Solt 9kg Front Load Washer saves water and energy...
- DO: The Westinghouse 60cm Stainless Steel 14 Place Freestanding Dishwasher handles family-sized loads...

NOTE ON SPECS IN THE H1: TGG product headings include specs as part of the product name (e.g., "Solt 9kg Front Load Washer", "Westinghouse 60cm Ceramic Cooktop"). Reproduce the H1 exactly including those specs — they are part of the product name, not additional specs being inserted. Do not restate the same spec again later in the description body.

SENTENCE & CLAUSE CONSTRUCTION:
- Each sentence expresses one complete idea or one feature-benefit pair.
- Do not chain independent clauses with and...and or a semicolon joining unrelated specs.
- AVOID: Two filters are dishwasher safe and the controls make operation simple and it runs at 57–66dB.
- DO: Two filters are dishwasher safe. Pull or push controls make operation simple. It runs at 57–66dB.

REPETITION RULES:
- Each measurement or spec appears once only across the full description. If a spec is in the H1, do not repeat it in the body.
- Do not repeat multi-word phrases more than twice.

NUMERIC FORMATTING:
- No trailing decimal zeros: 11.0 litres becomes 11 litres.
- No space before abbreviated units: 70 L becomes 70L; 52 dB becomes 52dB.
- Keep meaningful decimals from the extract: 4.5 Star, 1.53kg.

CONTEXTUAL FLOW:
- Do not pair unrelated contexts back-to-back.
- AVOID: noise low during mealtimes and open-plan living (time and setting mixed)
- DO: It runs at 52dB so it won't disturb conversation or TV time in open-plan living.

STRUCTURE:

Sentence 1 — Opening. Must follow all OPENING SENTENCE RULES above.

Paragraph 1 (2–3 sentences) — Who it's for and where it fits. Infer from specs and category. Do not open with "ideal for" or "perfect for".

Paragraph 2 (2–3 sentences) — Features that matter, each paired with the benefit. Spec then benefit. Cover standout technology, efficiency rating (4 stars+ only), and decision-changing convenience features. Split multi-spec sentences.

Closing sentence — mandatory. All three fields required. This sentence is exempt from the suppression rule for missing fields — it is always required.

Mandatory template: Model [SKU] in [colour] comes with a [X] year manufacturer's warranty.

- SKU must be the alphanumeric part number, not the marketing name.
- Warranty must include a numeric or written-out duration.
- If any field is absent from the HTML, write MODEL-MISSING, COLOUR-MISSING, or WARRANTY-MISSING in its place. Do not omit the sentence. Do not invent values.
- AVOID: Model BLA6321 is the manufacturer's part number. (wrong format)
- AVOID: Model WHC642BC in black comes with a manufacturer's warranty. (no duration)
- DO: Model BLA6321 in white comes with a 3 year manufacturer's warranty.

KEYWORD HANDLING:
Each of these must appear naturally at least once: brand, product type, capacity or size, energy rating (4 stars+ only), colour, model number, one defining feature. Do not pack into one sentence.

CONVERSATIONAL COMMERCE:
Ground the product in at least one of: household composition, routine, space, or lifestyle moment. Choose based on specs. Never use a template opener.

==================== OUTPUT ====================
Deliver a single CSV. No preamble. No commentary. No per-product summaries.

Columns: index | h1 | model | colour | warranty | description

One row per product. Process all products. Do not skip any. Do not truncate.
```
```
You are writing product descriptions for Google Merchant Centre. The descriptions must perform on three axes:
- Google Shopping relevance and attribute extraction
- Shopper conversion (clear, benefit-led prose)
- Conversational commerce — natural real-life usage context

==================== SCOPE ====================
You have been given HTML files for multiple product pages. Process every product. Do not stop. Do not ask for clarification. Do not ask to confirm scope. Deliver all descriptions in a single CSV with columns: index, h1, model, colour, warranty, description.

Do not reuse, paraphrase, or edit the existing product description from the page. Write every description from scratch using only the product specs and attributes in the HTML.

==================== PER PRODUCT — REPEAT FOR EACH ====================

STEP 1 — EXTRACT (internal, do not output)
Pull the following from the HTML. If a field is not clearly stated, mark it as MISSING. Do not invent it.

- Brand
- Product type / category
- Product heading — the exact H1 or page title as it appears on the page
- Model number — the alphanumeric part number (SKU), not the marketing name. Found in the spec table, labelled "model number", "part number", or "item number". Contains a mix of letters and numbers (e.g., RR-Q7BP52-03-BLK, 508973, IZ373HANZ). Marketing names are not model numbers: "Q7B+" is a marketing name; "CX True Wireless" is a marketing name. If no alphanumeric SKU is found, mark as MODEL-MISSING.
- Headline capacity or size (L, kg, cm, inches, etc.)
- Colour or finish
- Energy / water / star rating (if applicable)
- Core technology or standout feature (1–2 max)
- Convenience and safety features (only those that affect a buying decision)
- Physical dimensions (only if they affect fit or installation)
- Warranty length — numeric duration only (e.g., 2 year, 3 year). If warranty is mentioned but no duration stated, mark as WARRANTY-DURATION-MISSING. If not mentioned, mark as WARRANTY-MISSING.
- Any manufacturer-stated use case or target user

Suppression rules:
- If a feature is marked No, N/A, or Not Available — suppress it entirely.
- If an energy or water rating is below 4 stars — do not include it.
- If a field is not clearly stated — do not include it. Do not infer from general knowledge.
- Ignore: customer reviews, ratings, "customers also bought", delivery/returns/finance copy, price, promotions, competitor mentions.

STEP 2 — ACCURACY VERIFICATION (internal, do not output)
Before writing, check every claim:
- Does this feature appear explicitly in the HTML? If not, exclude it.
- Does my description contradict the attribute value? If so, correct or remove it.
- Am I converting units correctly? Verify before including.
- Am I using a synonym that changes the meaning? Example: "5G" when the spec says "Wi-Fi". Connectivity type must match exactly.
- If any critical field cannot be verified, do not include it.

STEP 3 — WRITE

HARD RULES:
- Use ONLY facts from the HTML. Do not reuse or adapt the existing product description.
- Australian English: colour, optimise, centre, metre, fibre.
- Plain prose paragraphs. No bullets, headings, markdown, emoji, all-caps, or em dashes.
- Length: 90–150 words total. If the page has genuinely sparse specs and 90 words cannot be reached without invention, write as many words as the verified facts support and flag the row as SPARSE-PAGE.
- No pricing, promotions, shipping or stock claims.
- No competitor names, comparative claims, or unverifiable superlatives.
- No filler: amazing, revolutionary, stunning, ultimate, perfect, premium, cutting-edge, state-of-the-art, game-changing.

PRODUCT-TYPE RULE — HEADPHONES AND EARBUDS ONLY:
Battery life must appear in the opening sentence or as a grammatically complete sentence immediately following it. Not a fragment.
- AVOID: The Sennheiser 27-hour CX True Wireless delivers... (battery life mid-title)
- AVOID standalone: Up to 27 hours battery life including the charging case. (no verb — fragment)
- DO: The Sennheiser CX True Wireless delivers crystal-clear audio for up to 27 hours with the charging case.

OPENING SENTENCE RULES:
- Begin with The, This, or A. Never with an imperative verb, a gerund, a question, or a product feature.
- Use the product heading exactly as it appears on the page. Do not reconstruct, abbreviate, or reorder it.
- Always include the brand name. It may not be dropped for length.
- Be a grammatically complete, definitive statement.
- AVOID: Tackle laundry day with... / Experience the convenience of... / Looking for a dryer...
- AVOID: The Sunbeam Single fitted antibacterial electric blanket... (H1 not reproduced — "Sleep Perfect" missing)
- DO: The Sunbeam Sleep Perfect Fitted Antibacterial Electric Blanket Single provides...
- DO: The Solt 9kg Front Load Washer saves water and energy...
- DO: The Westinghouse 60cm Stainless Steel 14 Place Freestanding Dishwasher handles family-sized loads...

NOTE ON SPECS IN THE H1: TGG product headings include specs as part of the product name (e.g., "Solt 9kg Front Load Washer", "Westinghouse 60cm Ceramic Cooktop"). Reproduce the H1 exactly including those specs — they are part of the product name, not additional specs being inserted. Do not restate the same spec again later in the description body.

SENTENCE & CLAUSE CONSTRUCTION:
- Each sentence expresses one complete idea or one feature-benefit pair.
- Do not chain independent clauses with and...and or a semicolon joining unrelated specs.
- AVOID: Two filters are dishwasher safe and the controls make operation simple and it runs at 57–66dB.
- DO: Two filters are dishwasher safe. Pull or push controls make operation simple. It runs at 57–66dB.

REPETITION RULES:
- Each measurement or spec appears once only across the full description. If a spec is in the H1, do not repeat it in the body.
- Do not repeat multi-word phrases more than twice.

NUMERIC FORMATTING:
- No trailing decimal zeros: 11.0 litres becomes 11 litres.
- No space before abbreviated units: 70 L becomes 70L; 52 dB becomes 52dB.
- Keep meaningful decimals from the extract: 4.5 Star, 1.53kg.

CONTEXTUAL FLOW:
- Do not pair unrelated contexts back-to-back.
- AVOID: noise low during mealtimes and open-plan living (time and setting mixed)
- DO: It runs at 52dB so it won't disturb conversation or TV time in open-plan living.

STRUCTURE:

Sentence 1 — Opening. Must follow all OPENING SENTENCE RULES above.

Paragraph 1 (2–3 sentences) — Who it's for and where it fits. Infer from specs and category. Do not open with "ideal for" or "perfect for".

Paragraph 2 (2–3 sentences) — Features that matter, each paired with the benefit. Spec then benefit. Cover standout technology, efficiency rating (4 stars+ only), and decision-changing convenience features. Split multi-spec sentences.

Closing sentence — mandatory. All three fields required. This sentence is exempt from the suppression rule for missing fields — it is always required.

Mandatory template: Model [SKU] in [colour] comes with a [X] year manufacturer's warranty.

- SKU must be the alphanumeric part number, not the marketing name.
- Warranty must include a numeric or written-out duration.
- If any field is absent from the HTML, write MODEL-MISSING, COLOUR-MISSING, or WARRANTY-MISSING in its place. Do not omit the sentence. Do not invent values.
- AVOID: Model BLA6321 is the manufacturer's part number. (wrong format)
- AVOID: Model WHC642BC in black comes with a manufacturer's warranty. (no duration)
- DO: Model BLA6321 in white comes with a 3 year manufacturer's warranty.

KEYWORD HANDLING:
Each of these must appear naturally at least once: brand, product type, capacity or size, energy rating (4 stars+ only), colour, model number, one defining feature. Do not pack into one sentence.

CONVERSATIONAL COMMERCE:
Ground the product in at least one of: household composition, routine, space, or lifestyle moment. Choose based on specs. Never use a template opener.

==================== OUTPUT ====================
Deliver a single CSV. No preamble. No commentary. No per-product summaries.

Columns: index | h1 | model | colour | warranty | description

One row per product. Process all products. Do not skip any. Do not truncate.
```

---

### 4. **Claude** — 2026-04-23T03:12

I'll process all products from the uploaded files. Let me start by extracting and examining the content.
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

Now I'll process all 38 products. This is a full-scope task with explicit hard constraints. I'll extract, verify, and write descriptions for each product without stopping or asking for confirmation.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The extraction isn't working well for colour. Let me manually inspect a few HTML files to understand the structure, then build proper descriptions for all 38 products.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


 I'll process all products from the uploaded files. Let me start by extracting and examining the content.
Now I'll process all 38 products. This is a full-scope task with explicit hard constraints. I'll extract, verify, and write descriptions for each product without stopping or asking for confirmation.
The extraction isn't working well for colour. Let me manually inspect a few HTML files to understand the structure, then build proper descriptions for all 38 products.

---

### 5. **Human** — 2026-04-23T03:12

```
You are writing product descriptions for Google Merchant Centre. The descriptions must perform on three axes:
- Google Shopping relevance and attribute extraction
- Shopper conversion (clear, benefit-led prose)
- Conversational commerce — natural real-life usage context

==================== SCOPE ====================
You have been given HTML files for multiple product pages. Process every product. Do not stop. Do not ask for clarification. Do not ask to confirm scope. Deliver all descriptions in a single CSV with columns: index, h1, model, colour, warranty, description.

Do not reuse, paraphrase, or edit the existing product description from the page. Write every description from scratch using only the product specs and attributes in the HTML.

==================== PER PRODUCT — REPEAT FOR EACH ====================

STEP 1 — EXTRACT (internal, do not output)
Pull the following from the HTML. If a field is not clearly stated, mark it as MISSING. Do not invent it.

- Brand
- Product type / category
- Product heading — the exact H1 or page title as it appears on the page
- Model number — the alphanumeric part number (SKU), not the marketing name. Found in the spec table, labelled "model number", "part number", or "item number". Contains a mix of letters and numbers (e.g., RR-Q7BP52-03-BLK, 508973, IZ373HANZ). Marketing names are not model numbers: "Q7B+" is a marketing name; "CX True Wireless" is a marketing name. If no alphanumeric SKU is found, mark as MODEL-MISSING.
- Headline capacity or size (L, kg, cm, inches, etc.)
- Colour or finish
- Energy / water / star rating (if applicable)
- Core technology or standout feature (1–2 max)
- Convenience and safety features (only those that affect a buying decision)
- Physical dimensions (only if they affect fit or installation)
- Warranty length — numeric duration only (e.g., 2 year, 3 year). If warranty is mentioned but no duration stated, mark as WARRANTY-DURATION-MISSING. If not mentioned, mark as WARRANTY-MISSING.
- Any manufacturer-stated use case or target user

Suppression rules:
- If a feature is marked No, N/A, or Not Available — suppress it entirely.
- If an energy or water rating is below 4 stars — do not include it.
- If a field is not clearly stated — do not include it. Do not infer from general knowledge.
- Ignore: customer reviews, ratings, "customers also bought", delivery/returns/finance copy, price, promotions, competitor mentions.

STEP 2 — ACCURACY VERIFICATION (internal, do not output)
Before writing, check every claim:
- Does this feature appear explicitly in the HTML? If not, exclude it.
- Does my description contradict the attribute value? If so, correct or remove it.
- Am I converting units correctly? Verify before including.
- Am I using a synonym that changes the meaning? Example: "5G" when the spec says "Wi-Fi". Connectivity type must match exactly.
- If any critical field cannot be verified, do not include it.

STEP 3 — WRITE

HARD RULES:
- Use ONLY facts from the HTML. Do not reuse or adapt the existing product description.
- Australian English: colour, optimise, centre, metre, fibre.
- Plain prose paragraphs. No bullets, headings, markdown, emoji, all-caps, or em dashes.
- Length: 90–150 words total. If the page has genuinely sparse specs and 90 words cannot be reached without invention, write as many words as the verified facts support and flag the row as SPARSE-PAGE.
- No pricing, promotions, shipping or stock claims.
- No competitor names, comparative claims, or unverifiable superlatives.
- No filler: amazing, revolutionary, stunning, ultimate, perfect, premium, cutting-edge, state-of-the-art, game-changing.

PRODUCT-TYPE RULE — HEADPHONES AND EARBUDS ONLY:
Battery life must appear in the opening sentence or as a grammatically complete sentence immediately following it. Not a fragment.
- AVOID: The Sennheiser 27-hour CX True Wireless delivers... (battery life mid-title)
- AVOID standalone: Up to 27 hours battery life including the charging case. (no verb — fragment)
- DO: The Sennheiser CX True Wireless delivers crystal-clear audio for up to 27 hours with the charging case.

OPENING SENTENCE RULES:
- Begin with The, This, or A. Never with an imperative verb, a gerund, a question, or a product feature.
- Use the product heading exactly as it appears on the page. Do not reconstruct, abbreviate, or reorder it.
- Always include the brand name. It may not be dropped for length.
- Be a grammatically complete, definitive statement.
- AVOID: Tackle laundry day with... / Experience the convenience of... / Looking for a dryer...
- AVOID: The Sunbeam Single fitted antibacterial electric blanket... (H1 not reproduced — "Sleep Perfect" missing)
- DO: The Sunbeam Sleep Perfect Fitted Antibacterial Electric Blanket Single provides...
- DO: The Solt 9kg Front Load Washer saves water and energy...
- DO: The Westinghouse 60cm Stainless Steel 14 Place Freestanding Dishwasher handles family-sized loads...

NOTE ON SPECS IN THE H1: TGG product headings include specs as part of the product name (e.g., "Solt 9kg Front Load Washer", "Westinghouse 60cm Ceramic Cooktop"). Reproduce the H1 exactly including those specs — they are part of the product name, not additional specs being inserted. Do not restate the same spec again later in the description body.

SENTENCE & CLAUSE CONSTRUCTION:
- Each sentence expresses one complete idea or one feature-benefit pair.
- Do not chain independent clauses with and...and or a semicolon joining unrelated specs.
- AVOID: Two filters are dishwasher safe and the controls make operation simple and it runs at 57–66dB.
- DO: Two filters are dishwasher safe. Pull or push controls make operation simple. It runs at 57–66dB.

REPETITION RULES:
- Each measurement or spec appears once only across the full description. If a spec is in the H1, do not repeat it in the body.
- Do not repeat multi-word phrases more than twice.

NUMERIC FORMATTING:
- No trailing decimal zeros: 11.0 litres becomes 11 litres.
- No space before abbreviated units: 70 L becomes 70L; 52 dB becomes 52dB.
- Keep meaningful decimals from the extract: 4.5 Star, 1.53kg.

CONTEXTUAL FLOW:
- Do not pair unrelated contexts back-to-back.
- AVOID: noise low during mealtimes and open-plan living (time and setting mixed)
- DO: It runs at 52dB so it won't disturb conversation or TV time in open-plan living.

STRUCTURE:

Sentence 1 — Opening. Must follow all OPENING SENTENCE RULES above.

Paragraph 1 (2–3 sentences) — Who it's for and where it fits. Infer from specs and category. Do not open with "ideal for" or "perfect for".

Paragraph 2 (2–3 sentences) — Features that matter, each paired with the benefit. Spec then benefit. Cover standout technology, efficiency rating (4 stars+ only), and decision-changing convenience features. Split multi-spec sentences.

Closing sentence — mandatory. All three fields required. This sentence is exempt from the suppression rule for missing fields — it is always required.

Mandatory template: Model [SKU] in [colour] comes with a [X] year manufacturer's warranty.

- SKU must be the alphanumeric part number, not the marketing name.
- Warranty must include a numeric or written-out duration.
- If any field is absent from the HTML, write MODEL-MISSING, COLOUR-MISSING, or WARRANTY-MISSING in its place. Do not omit the sentence. Do not invent values.
- AVOID: Model BLA6321 is the manufacturer's part number. (wrong format)
- AVOID: Model WHC642BC in black comes with a manufacturer's warranty. (no duration)
- DO: Model BLA6321 in white comes with a 3 year manufacturer's warranty.

KEYWORD HANDLING:
Each of these must appear naturally at least once: brand, product type, capacity or size, energy rating (4 stars+ only), colour, model number, one defining feature. Do not pack into one sentence.

CONVERSATIONAL COMMERCE:
Ground the product in at least one of: household composition, routine, space, or lifestyle moment. Choose based on specs. Never use a template opener.

==================== OUTPUT ====================
Deliver a single CSV. No preamble. No commentary. No per-product summaries.

Columns: index | h1 | model | colour | warranty | description

One row per product. Process all products. Do not skip any. Do not truncate.
```
```
You are writing product descriptions for Google Merchant Centre. The descriptions must perform on three axes:
- Google Shopping relevance and attribute extraction
- Shopper conversion (clear, benefit-led prose)
- Conversational commerce — natural real-life usage context

==================== SCOPE ====================
You have been given HTML files for multiple product pages. Process every product. Do not stop. Do not ask for clarification. Do not ask to confirm scope. Deliver all descriptions in a single CSV with columns: index, h1, model, colour, warranty, description.

Do not reuse, paraphrase, or edit the existing product description from the page. Write every description from scratch using only the product specs and attributes in the HTML.

==================== PER PRODUCT — REPEAT FOR EACH ====================

STEP 1 — EXTRACT (internal, do not output)
Pull the following from the HTML. If a field is not clearly stated, mark it as MISSING. Do not invent it.

- Brand
- Product type / category
- Product heading — the exact H1 or page title as it appears on the page
- Model number — the alphanumeric part number (SKU), not the marketing name. Found in the spec table, labelled "model number", "part number", or "item number". Contains a mix of letters and numbers (e.g., RR-Q7BP52-03-BLK, 508973, IZ373HANZ). Marketing names are not model numbers: "Q7B+" is a marketing name; "CX True Wireless" is a marketing name. If no alphanumeric SKU is found, mark as MODEL-MISSING.
- Headline capacity or size (L, kg, cm, inches, etc.)
- Colour or finish
- Energy / water / star rating (if applicable)
- Core technology or standout feature (1–2 max)
- Convenience and safety features (only those that affect a buying decision)
- Physical dimensions (only if they affect fit or installation)
- Warranty length — numeric duration only (e.g., 2 year, 3 year). If warranty is mentioned but no duration stated, mark as WARRANTY-DURATION-MISSING. If not mentioned, mark as WARRANTY-MISSING.
- Any manufacturer-stated use case or target user

Suppression rules:
- If a feature is marked No, N/A, or Not Available — suppress it entirely.
- If an energy or water rating is below 4 stars — do not include it.
- If a field is not clearly stated — do not include it. Do not infer from general knowledge.
- Ignore: customer reviews, ratings, "customers also bought", delivery/returns/finance copy, price, promotions, competitor mentions.

STEP 2 — ACCURACY VERIFICATION (internal, do not output)
Before writing, check every claim:
- Does this feature appear explicitly in the HTML? If not, exclude it.
- Does my description contradict the attribute value? If so, correct or remove it.
- Am I converting units correctly? Verify before including.
- Am I using a synonym that changes the meaning? Example: "5G" when the spec says "Wi-Fi". Connectivity type must match exactly.
- If any critical field cannot be verified, do not include it.

STEP 3 — WRITE

HARD RULES:
- Use ONLY facts from the HTML. Do not reuse or adapt the existing product description.
- Australian English: colour, optimise, centre, metre, fibre.
- Plain prose paragraphs. No bullets, headings, markdown, emoji, all-caps, or em dashes.
- Length: 90–150 words total. If the page has genuinely sparse specs and 90 words cannot be reached without invention, write as many words as the verified facts support and flag the row as SPARSE-PAGE.
- No pricing, promotions, shipping or stock claims.
- No competitor names, comparative claims, or unverifiable superlatives.
- No filler: amazing, revolutionary, stunning, ultimate, perfect, premium, cutting-edge, state-of-the-art, game-changing.

PRODUCT-TYPE RULE — HEADPHONES AND EARBUDS ONLY:
Battery life must appear in the opening sentence or as a grammatically complete sentence immediately following it. Not a fragment.
- AVOID: The Sennheiser 27-hour CX True Wireless delivers... (battery life mid-title)
- AVOID standalone: Up to 27 hours battery life including the charging case. (no verb — fragment)
- DO: The Sennheiser CX True Wireless delivers crystal-clear audio for up to 27 hours with the charging case.

OPENING SENTENCE RULES:
- Begin with The, This, or A. Never with an imperative verb, a gerund, a question, or a product feature.
- Use the product heading exactly as it appears on the page. Do not reconstruct, abbreviate, or reorder it.
- Always include the brand name. It may not be dropped for length.
- Be a grammatically complete, definitive statement.
- AVOID: Tackle laundry day with... / Experience the convenience of... / Looking for a dryer...
- AVOID: The Sunbeam Single fitted antibacterial electric blanket... (H1 not reproduced — "Sleep Perfect" missing)
- DO: The Sunbeam Sleep Perfect Fitted Antibacterial Electric Blanket Single provides...
- DO: The Solt 9kg Front Load Washer saves water and energy...
- DO: The Westinghouse 60cm Stainless Steel 14 Place Freestanding Dishwasher handles family-sized loads...

NOTE ON SPECS IN THE H1: TGG product headings include specs as part of the product name (e.g., "Solt 9kg Front Load Washer", "Westinghouse 60cm Ceramic Cooktop"). Reproduce the H1 exactly including those specs — they are part of the product name, not additional specs being inserted. Do not restate the same spec again later in the description body.

SENTENCE & CLAUSE CONSTRUCTION:
- Each sentence expresses one complete idea or one feature-benefit pair.
- Do not chain independent clauses with and...and or a semicolon joining unrelated specs.
- AVOID: Two filters are dishwasher safe and the controls make operation simple and it runs at 57–66dB.
- DO: Two filters are dishwasher safe. Pull or push controls make operation simple. It runs at 57–66dB.

REPETITION RULES:
- Each measurement or spec appears once only across the full description. If a spec is in the H1, do not repeat it in the body.
- Do not repeat multi-word phrases more than twice.

NUMERIC FORMATTING:
- No trailing decimal zeros: 11.0 litres becomes 11 litres.
- No space before abbreviated units: 70 L becomes 70L; 52 dB becomes 52dB.
- Keep meaningful decimals from the extract: 4.5 Star, 1.53kg.

CONTEXTUAL FLOW:
- Do not pair unrelated contexts back-to-back.
- AVOID: noise low during mealtimes and open-plan living (time and setting mixed)
- DO: It runs at 52dB so it won't disturb conversation or TV time in open-plan living.

STRUCTURE:

Sentence 1 — Opening. Must follow all OPENING SENTENCE RULES above.

Paragraph 1 (2–3 sentences) — Who it's for and where it fits. Infer from specs and category. Do not open with "ideal for" or "perfect for".

Paragraph 2 (2–3 sentences) — Features that matter, each paired with the benefit. Spec then benefit. Cover standout technology, efficiency rating (4 stars+ only), and decision-changing convenience features. Split multi-spec sentences.

Closing sentence — mandatory. All three fields required. This sentence is exempt from the suppression rule for missing fields — it is always required.

Mandatory template: Model [SKU] in [colour] comes with a [X] year manufacturer's warranty.

- SKU must be the alphanumeric part number, not the marketing name.
- Warranty must include a numeric or written-out duration.
- If any field is absent from the HTML, write MODEL-MISSING, COLOUR-MISSING, or WARRANTY-MISSING in its place. Do not omit the sentence. Do not invent values.
- AVOID: Model BLA6321 is the manufacturer's part number. (wrong format)
- AVOID: Model WHC642BC in black comes with a manufacturer's warranty. (no duration)
- DO: Model BLA6321 in white comes with a 3 year manufacturer's warranty.

KEYWORD HANDLING:
Each of these must appear naturally at least once: brand, product type, capacity or size, energy rating (4 stars+ only), colour, model number, one defining feature. Do not pack into one sentence.

CONVERSATIONAL COMMERCE:
Ground the product in at least one of: household composition, routine, space, or lifestyle moment. Choose based on specs. Never use a template opener.

==================== OUTPUT ====================
Deliver a single CSV. No preamble. No commentary. No per-product summaries.

Columns: index | h1 | model | colour | warranty | description

One row per product. Process all products. Do not skip any. Do not truncate.
```

---

### 6. **Human** — 2026-04-23T03:13

```
You are writing product descriptions for Google Merchant Centre. The descriptions must perform on three axes:
- Google Shopping relevance and attribute extraction
- Shopper conversion (clear, benefit-led prose)
- Conversational commerce — natural real-life usage context

==================== SCOPE ====================
You have been given HTML files for multiple product pages. Process every product. Do not stop. Do not ask for clarification. Do not ask to confirm scope. Deliver all descriptions in a single CSV with columns: index, h1, model, colour, warranty, description.

Do not reuse, paraphrase, or edit the existing product description from the page. Write every description from scratch using only the product specs and attributes in the HTML.

==================== PER PRODUCT — REPEAT FOR EACH ====================

STEP 1 — EXTRACT (internal, do not output)
Pull the following from the HTML. If a field is not clearly stated, mark it as MISSING. Do not invent it.

- Brand
- Product type / category
- Product heading — the exact H1 or page title as it appears on the page
- Model number — the alphanumeric part number (SKU), not the marketing name. Found in the spec table, labelled "model number", "part number", or "item number". Contains a mix of letters and numbers (e.g., RR-Q7BP52-03-BLK, 508973, IZ373HANZ). Marketing names are not model numbers: "Q7B+" is a marketing name; "CX True Wireless" is a marketing name. If no alphanumeric SKU is found, mark as MODEL-MISSING.
- Headline capacity or size (L, kg, cm, inches, etc.)
- Colour or finish
- Energy / water / star rating (if applicable)
- Core technology or standout feature (1–2 max)
- Convenience and safety features (only those that affect a buying decision)
- Physical dimensions (only if they affect fit or installation)
- Warranty length — numeric duration only (e.g., 2 year, 3 year). If warranty is mentioned but no duration stated, mark as WARRANTY-DURATION-MISSING. If not mentioned, mark as WARRANTY-MISSING.
- Any manufacturer-stated use case or target user

Suppression rules:
- If a feature is marked No, N/A, or Not Available — suppress it entirely.
- If an energy or water rating is below 4 stars — do not include it.
- If a field is not clearly stated — do not include it. Do not infer from general knowledge.
- Ignore: customer reviews, ratings, "customers also bought", delivery/returns/finance copy, price, promotions, competitor mentions.

STEP 2 — ACCURACY VERIFICATION (internal, do not output)
Before writing, check every claim:
- Does this feature appear explicitly in the HTML? If not, exclude it.
- Does my description contradict the attribute value? If so, correct or remove it.
- Am I converting units correctly? Verify before including.
- Am I using a synonym that changes the meaning? Example: "5G" when the spec says "Wi-Fi". Connectivity type must match exactly.
- If any critical field cannot be verified, do not include it.

STEP 3 — WRITE

HARD RULES:
- Use ONLY facts from the HTML. Do not reuse or adapt the existing product description.
- Australian English: colour, optimise, centre, metre, fibre.
- Plain prose paragraphs. No bullets, headings, markdown, emoji, all-caps, or em dashes.
- Length: 90–150 words total. If the page has genuinely sparse specs and 90 words cannot be reached without invention, write as many words as the verified facts support and flag the row as SPARSE-PAGE.
- No pricing, promotions, shipping or stock claims.
- No competitor names, comparative claims, or unverifiable superlatives.
- No filler: amazing, revolutionary, stunning, ultimate, perfect, premium, cutting-edge, state-of-the-art, game-changing.

PRODUCT-TYPE RULE — HEADPHONES AND EARBUDS ONLY:
Battery life must appear in the opening sentence or as a grammatically complete sentence immediately following it. Not a fragment.
- AVOID: The Sennheiser 27-hour CX True Wireless delivers... (battery life mid-title)
- AVOID standalone: Up to 27 hours battery life including the charging case. (no verb — fragment)
- DO: The Sennheiser CX True Wireless delivers crystal-clear audio for up to 27 hours with the charging case.

OPENING SENTENCE RULES:
- Begin with The, This, or A. Never with an imperative verb, a gerund, a question, or a product feature.
- Use the product heading exactly as it appears on the page. Do not reconstruct, abbreviate, or reorder it.
- Always include the brand name. It may not be dropped for length.
- Be a grammatically complete, definitive statement.
- AVOID: Tackle laundry day with... / Experience the convenience of... / Looking for a dryer...
- AVOID: The Sunbeam Single fitted antibacterial electric blanket... (H1 not reproduced — "Sleep Perfect" missing)
- DO: The Sunbeam Sleep Perfect Fitted Antibacterial Electric Blanket Single provides...
- DO: The Solt 9kg Front Load Washer saves water and energy...
- DO: The Westinghouse 60cm Stainless Steel 14 Place Freestanding Dishwasher handles family-sized loads...

NOTE ON SPECS IN THE H1: TGG product headings include specs as part of the product name (e.g., "Solt 9kg Front Load Washer", "Westinghouse 60cm Ceramic Cooktop"). Reproduce the H1 exactly including those specs — they are part of the product name, not additional specs being inserted. Do not restate the same spec again later in the description body.

SENTENCE & CLAUSE CONSTRUCTION:
- Each sentence expresses one complete idea or one feature-benefit pair.
- Do not chain independent clauses with and...and or a semicolon joining unrelated specs.
- AVOID: Two filters are dishwasher safe and the controls make operation simple and it runs at 57–66dB.
- DO: Two filters are dishwasher safe. Pull or push controls make operation simple. It runs at 57–66dB.

REPETITION RULES:
- Each measurement or spec appears once only across the full description. If a spec is in the H1, do not repeat it in the body.
- Do not repeat multi-word phrases more than twice.

NUMERIC FORMATTING:
- No trailing decimal zeros: 11.0 litres becomes 11 litres.
- No space before abbreviated units: 70 L becomes 70L; 52 dB becomes 52dB.
- Keep meaningful decimals from the extract: 4.5 Star, 1.53kg.

CONTEXTUAL FLOW:
- Do not pair unrelated contexts back-to-back.
- AVOID: noise low during mealtimes and open-plan living (time and setting mixed)
- DO: It runs at 52dB so it won't disturb conversation or TV time in open-plan living.

STRUCTURE:

Sentence 1 — Opening. Must follow all OPENING SENTENCE RULES above.

Paragraph 1 (2–3 sentences) — Who it's for and where it fits. Infer from specs and category. Do not open with "ideal for" or "perfect for".

Paragraph 2 (2–3 sentences) — Features that matter, each paired with the benefit. Spec then benefit. Cover standout technology, efficiency rating (4 stars+ only), and decision-changing convenience features. Split multi-spec sentences.

Closing sentence — mandatory. All three fields required. This sentence is exempt from the suppression rule for missing fields — it is always required.

Mandatory template: Model [SKU] in [colour] comes with a [X] year manufacturer's warranty.

- SKU must be the alphanumeric part number, not the marketing name.
- Warranty must include a numeric or written-out duration.
- If any field is absent from the HTML, write MODEL-MISSING, COLOUR-MISSING, or WARRANTY-MISSING in its place. Do not omit the sentence. Do not invent values.
- AVOID: Model BLA6321 is the manufacturer's part number. (wrong format)
- AVOID: Model WHC642BC in black comes with a manufacturer's warranty. (no duration)
- DO: Model BLA6321 in white comes with a 3 year manufacturer's warranty.

KEYWORD HANDLING:
Each of these must appear naturally at least once: brand, product type, capacity or size, energy rating (4 stars+ only), colour, model number, one defining feature. Do not pack into one sentence.

CONVERSATIONAL COMMERCE:
Ground the product in at least one of: household composition, routine, space, or lifestyle moment. Choose based on specs. Never use a template opener.

==================== OUTPUT ====================
Deliver a single CSV. No preamble. No commentary. No per-product summaries.

Columns: index | h1 | model | colour | warranty | description

One row per product. Process all products. Do not skip any. Do not truncate.
```
```
You are writing product descriptions for Google Merchant Centre. The descriptions must perform on three axes:
- Google Shopping relevance and attribute extraction
- Shopper conversion (clear, benefit-led prose)
- Conversational commerce — natural real-life usage context

==================== SCOPE ====================
You have been given HTML files for multiple product pages. Process every product. Do not stop. Do not ask for clarification. Do not ask to confirm scope. Deliver all descriptions in a single CSV with columns: index, h1, model, colour, warranty, description.

Do not reuse, paraphrase, or edit the existing product description from the page. Write every description from scratch using only the product specs and attributes in the HTML.

==================== PER PRODUCT — REPEAT FOR EACH ====================

STEP 1 — EXTRACT (internal, do not output)
Pull the following from the HTML. If a field is not clearly stated, mark it as MISSING. Do not invent it.

- Brand
- Product type / category
- Product heading — the exact H1 or page title as it appears on the page
- Model number — the alphanumeric part number (SKU), not the marketing name. Found in the spec table, labelled "model number", "part number", or "item number". Contains a mix of letters and numbers (e.g., RR-Q7BP52-03-BLK, 508973, IZ373HANZ). Marketing names are not model numbers: "Q7B+" is a marketing name; "CX True Wireless" is a marketing name. If no alphanumeric SKU is found, mark as MODEL-MISSING.
- Headline capacity or size (L, kg, cm, inches, etc.)
- Colour or finish
- Energy / water / star rating (if applicable)
- Core technology or standout feature (1–2 max)
- Convenience and safety features (only those that affect a buying decision)
- Physical dimensions (only if they affect fit or installation)
- Warranty length — numeric duration only (e.g., 2 year, 3 year). If warranty is mentioned but no duration stated, mark as WARRANTY-DURATION-MISSING. If not mentioned, mark as WARRANTY-MISSING.
- Any manufacturer-stated use case or target user

Suppression rules:
- If a feature is marked No, N/A, or Not Available — suppress it entirely.
- If an energy or water rating is below 4 stars — do not include it.
- If a field is not clearly stated — do not include it. Do not infer from general knowledge.
- Ignore: customer reviews, ratings, "customers also bought", delivery/returns/finance copy, price, promotions, competitor mentions.

STEP 2 — ACCURACY VERIFICATION (internal, do not output)
Before writing, check every claim:
- Does this feature appear explicitly in the HTML? If not, exclude it.
- Does my description contradict the attribute value? If so, correct or remove it.
- Am I converting units correctly? Verify before including.
- Am I using a synonym that changes the meaning? Example: "5G" when the spec says "Wi-Fi". Connectivity type must match exactly.
- If any critical field cannot be verified, do not include it.

STEP 3 — WRITE

HARD RULES:
- Use ONLY facts from the HTML. Do not reuse or adapt the existing product description.
- Australian English: colour, optimise, centre, metre, fibre.
- Plain prose paragraphs. No bullets, headings, markdown, emoji, all-caps, or em dashes.
- Length: 90–150 words total. If the page has genuinely sparse specs and 90 words cannot be reached without invention, write as many words as the verified facts support and flag the row as SPARSE-PAGE.
- No pricing, promotions, shipping or stock claims.
- No competitor names, comparative claims, or unverifiable superlatives.
- No filler: amazing, revolutionary, stunning, ultimate, perfect, premium, cutting-edge, state-of-the-art, game-changing.

PRODUCT-TYPE RULE — HEADPHONES AND EARBUDS ONLY:
Battery life must appear in the opening sentence or as a grammatically complete sentence immediately following it. Not a fragment.
- AVOID: The Sennheiser 27-hour CX True Wireless delivers... (battery life mid-title)
- AVOID standalone: Up to 27 hours battery life including the charging case. (no verb — fragment)
- DO: The Sennheiser CX True Wireless delivers crystal-clear audio for up to 27 hours with the charging case.

OPENING SENTENCE RULES:
- Begin with The, This, or A. Never with an imperative verb, a gerund, a question, or a product feature.
- Use the product heading exactly as it appears on the page. Do not reconstruct, abbreviate, or reorder it.
- Always include the brand name. It may not be dropped for length.
- Be a grammatically complete, definitive statement.
- AVOID: Tackle laundry day with... / Experience the convenience of... / Looking for a dryer...
- AVOID: The Sunbeam Single fitted antibacterial electric blanket... (H1 not reproduced — "Sleep Perfect" missing)
- DO: The Sunbeam Sleep Perfect Fitted Antibacterial Electric Blanket Single provides...
- DO: The Solt 9kg Front Load Washer saves water and energy...
- DO: The Westinghouse 60cm Stainless Steel 14 Place Freestanding Dishwasher handles family-sized loads...

NOTE ON SPECS IN THE H1: TGG product headings include specs as part of the product name (e.g., "Solt 9kg Front Load Washer", "Westinghouse 60cm Ceramic Cooktop"). Reproduce the H1 exactly including those specs — they are part of the product name, not additional specs being inserted. Do not restate the same spec again later in the description body.

SENTENCE & CLAUSE CONSTRUCTION:
- Each sentence expresses one complete idea or one feature-benefit pair.
- Do not chain independent clauses with and...and or a semicolon joining unrelated specs.
- AVOID: Two filters are dishwasher safe and the controls make operation simple and it runs at 57–66dB.
- DO: Two filters are dishwasher safe. Pull or push controls make operation simple. It runs at 57–66dB.

REPETITION RULES:
- Each measurement or spec appears once only across the full description. If a spec is in the H1, do not repeat it in the body.
- Do not repeat multi-word phrases more than twice.

NUMERIC FORMATTING:
- No trailing decimal zeros: 11.0 litres becomes 11 litres.
- No space before abbreviated units: 70 L becomes 70L; 52 dB becomes 52dB.
- Keep meaningful decimals from the extract: 4.5 Star, 1.53kg.

CONTEXTUAL FLOW:
- Do not pair unrelated contexts back-to-back.
- AVOID: noise low during mealtimes and open-plan living (time and setting mixed)
- DO: It runs at 52dB so it won't disturb conversation or TV time in open-plan living.

STRUCTURE:

Sentence 1 — Opening. Must follow all OPENING SENTENCE RULES above.

Paragraph 1 (2–3 sentences) — Who it's for and where it fits. Infer from specs and category. Do not open with "ideal for" or "perfect for".

Paragraph 2 (2–3 sentences) — Features that matter, each paired with the benefit. Spec then benefit. Cover standout technology, efficiency rating (4 stars+ only), and decision-changing convenience features. Split multi-spec sentences.

Closing sentence — mandatory. All three fields required. This sentence is exempt from the suppression rule for missing fields — it is always required.

Mandatory template: Model [SKU] in [colour] comes with a [X] year manufacturer's warranty.

- SKU must be the alphanumeric part number, not the marketing name.
- Warranty must include a numeric or written-out duration.
- If any field is absent from the HTML, write MODEL-MISSING, COLOUR-MISSING, or WARRANTY-MISSING in its place. Do not omit the sentence. Do not invent values.
- AVOID: Model BLA6321 is the manufacturer's part number. (wrong format)
- AVOID: Model WHC642BC in black comes with a manufacturer's warranty. (no duration)
- DO: Model BLA6321 in white comes with a 3 year manufacturer's warranty.

KEYWORD HANDLING:
Each of these must appear naturally at least once: brand, product type, capacity or size, energy rating (4 stars+ only), colour, model number, one defining feature. Do not pack into one sentence.

CONVERSATIONAL COMMERCE:
Ground the product in at least one of: household composition, routine, space, or lifestyle moment. Choose based on specs. Never use a template opener.

==================== OUTPUT ====================
Deliver a single CSV. No preamble. No commentary. No per-product summaries.

Columns: index | h1 | model | colour | warranty | description

One row per product. Process all products. Do not skip any. Do not truncate.
```

---

### 7. **Human** — 2026-04-23T03:17

act on prompt
act on prompt
