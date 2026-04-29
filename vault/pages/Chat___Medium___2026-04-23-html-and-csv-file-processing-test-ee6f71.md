---
title: HTML and CSV file processing test (medium)
parent: Chat/Light/2026-04-23-html-and-csv-file-processing-test-ee6f71
uuid: ee6f71c6-a956-4643-acea-7633005d8e4e
---

#chat/medium #project/main #status/active

# HTML and CSV file processing test — Key User Messages

→ Light view: [[Chat/Light/2026-04-23-html-and-csv-file-processing-test-ee6f71]]
→ Full transcript: [[Chat/Full/2026-04-23-html-and-csv-file-processing-test-ee6f71]]

**Total user messages:** 9

---

### Message 1 — 2026-04-23T03:17

I need you to act on the prompt for the attached htmls as a test, in conjunction with the csv
I need you to act on the prompt for the attached htmls as a test, in conjunction with the csv

### Message 2 — 2026-04-23T03:25

get the html yourself
get the html yourself

### Message 3 — 2026-04-23T03:32

DO ALL 38
DO ALL 38

### Message 4 — 2026-04-23T03:46

Rerun the taste against the 38 - same process - use the new prompt file (forget the previous, freshly reload the file) same as:
Rerun the taste against the 38 - same process - use the new prompt file (forget the previous, freshly reload the file) same as:

### Message 5 — 2026-04-23T04:30

now redo it, but only using the csv, your html pull and this prompt.
now redo it, but only using the csv, your html pull and this prompt.

### Message 6 — 2026-04-23T04:42

check agains:

You are a QA reviewer for product descriptions.
You will be given a CSV containing multiple product descriptions. Process every row and return one pass/fail table per product labelled by product name. Do not stop early. Do not ask for clarification.
If a product H1 is not provided, infer the intended product heading from the opening sentence of the description. The product name as used in the first sentence is treated as the H1 for rules 2, 3, and 4.
For each description check every rule and return a table: Rule | Pass/Fail | Note. One-line note on every failure. If a rule does not apply to the product type, mark it N/A.
RULES:

1. OPENING WORD - Does the description begin with The, This, or A?
2. BRAND IN S1 - Does the first sentence include the brand name?
3. TITLE INTACT - Does the first sentence reproduce the product heading exactly, without abbreviation, reordering, inserted specs, or added words?
4. SPEC PLACEMENT - If the product heading naturally contains a spec as part of the product name (e.g., "Solt 9kg Front Load Washer", "Solt 99L Hybrid Chest Freezer"), reproducing it in the opening sentence is correct. Fail only if: (a) a spec NOT in the H1 has been inserted into the product name, or (b) a spec from the H1 is restated in the body of the description after the opening sentence.
5. NO RUN-ONS - Are there sentences chaining three or more independent clauses with "and"?
6. DIMENSION REPEAT - Does any measurement or dimension appear more than once in t

[truncated — see full transcript]

### Message 7 — 2026-04-23T04:47

how come?
how come?

### Message 8 — 2026-04-23T04:47

What would the prompt need to say to fix it? what wouldve steered you right?
What would the prompt need to say to fix it? what wouldve steered you right?

### Message 9 — 2026-04-23T04:59

run it one last time, again forget all context except the original csv, html, and this new file for prompt
run it one last time, again forget all context except the original csv, html, and this new file for prompt
