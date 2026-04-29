---
title: Product descriptions for Google Merchant Centre (medium)
parent: Chat/Light/2026-04-23-product-descriptions-for-google-merchant-centre-e9f9fc
uuid: e9f9fc9c-5773-4ca2-87ac-08dfb64fe131
---

#chat/medium #project/main #status/active

# Product descriptions for Google Merchant Centre — Key User Messages

→ Light view: [[Chat/Light/2026-04-23-product-descriptions-for-google-merchant-centre-e9f9fc]]
→ Full transcript: [[Chat/Full/2026-04-23-product-descriptions-for-google-merchant-centre-e9f9fc]]

**Total user messages:** 5

---

### Message 1 — 2026-04-23T03:10

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
- Model number — the alphanumeric part number (SKU), not the marketing name. Found in the spec table, labelled model number, part number, or item number. Cont

[truncated — see full transcript]

### Message 2 — 2026-04-23T03:11

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
- He

[truncated — see full transcript]

### Message 3 — 2026-04-23T03:12

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
- He

[truncated — see full transcript]

### Message 4 — 2026-04-23T03:13

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
- He

[truncated — see full transcript]

### Message 5 — 2026-04-23T03:17

act on prompt
act on prompt
