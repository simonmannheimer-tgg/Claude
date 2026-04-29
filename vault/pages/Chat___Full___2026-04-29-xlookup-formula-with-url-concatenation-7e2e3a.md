---
title: XLOOKUP formula with URL concatenation (full)
parent: Chat/Light/2026-04-29-xlookup-formula-with-url-concatenation-7e2e3a
uuid: 7e2e3aeb-3c42-4946-89c1-b15145ed6d63
---

#chat/full #project/main #status/tactical

# XLOOKUP formula with URL concatenation — Full Transcript

→ Light view: [[Chat/Light/2026-04-29-xlookup-formula-with-url-concatenation-7e2e3a]]
→ Medium view: [[Chat/Medium/2026-04-29-xlookup-formula-with-url-concatenation-7e2e3a]]

**Messages:** 10 | **Date:** 2026-04-29

---

### 1. **Human** — 2026-04-29T06:34

=XLOOKUP("https://www.thegoodguys.com.au"&B191,G:G,G:G)

OR a191
=XLOOKUP("https://www.thegoodguys.com.au"&B191,G:G,G:G)

OR a191

---

### 2. **Claude** — 2026-04-29T06:34

That's an XLOOKUP formula searching for a concatenated value in column G. It won't work as written because:

1. **XLOOKUP searches for exact matches.** Concatenating `https://www.thegoodguys.com.au` + a cell value (B191) creates a lookup key that likely doesn't exist in column G as-is.

2. **The return array is G:G.** You're looking up in column G and returning from column G, which just echoes the match back. That's redundant unless you meant a different return column.

3. **Context missing.** What are you trying to do? Look up a product ID? Match a URL? Cross-reference data across sheets?

Post the actual goal and show me what B191 contains and what's in column G. Then I can write a formula that works.
 That's an XLOOKUP formula searching for a concatenated value in column G. It won't work as written because:

1. **XLOOKUP searches for exact matches.** Concatenating `https://www.thegoodguys.com.au` + a cell value (B191) creates a lookup key that likely doesn't exist in column G as-is.

2. **The return array is G:G.** You're looking up in column G and returning from column G, which just echoes the match back. That's redundant unless you meant a different return column.

3. **Context missing.** What are you trying to do? Look up a product ID? Match a URL? Cross-reference data across sheets?

Post the actual goal and show me what B191 contains and what's in column G. Then I can write a formula that works.

---

### 3. **Human** — 2026-04-29T06:34

im telling you to add b191 or a191
im telling you to add b191 or a191

---

### 4. **Claude** — 2026-04-29T06:34

I understand. You're asking me to replace that formula with either `=B191` or `=A191`.

Which one? What's the difference between what's in A191 vs B191, and which value do you need in that cell?
 I understand. You're asking me to replace that formula with either `=B191` or `=A191`.

Which one? What's the difference between what's in A191 vs B191, and which value do you need in that cell?

---

### 5. **Human** — 2026-04-29T06:34

both
both

---

### 6. **Claude** — 2026-04-29T06:34

Cell can't hold two values simultaneously. You need one formula that combines them.

Do you want:
- **Concatenation:** `=A191&B191`
- **A191 if it exists, otherwise B191:** `=IF(A191="",B191,A191)`
- **Both in one cell with a separator:** `=A191&" "&B191`
- **Something else entirely**

Which one?
 Cell can't hold two values simultaneously. You need one formula that combines them.

Do you want:
- **Concatenation:** `=A191&B191`
- **A191 if it exists, otherwise B191:** `=IF(A191="",B191,A191)`
- **Both in one cell with a separator:** `=A191&" "&B191`
- **Something else entirely**

Which one?

---

### 7. **Human** — 2026-04-29T06:34

you can, fallback
you can, fallback

---

### 8. **Claude** — 2026-04-29T06:34

Got it.
```
This block is not supported on your current device yet.
```

`=IF(A191="",B191,A191)`

Uses A191 if it has a value. Falls back to B191 if A191 is empty.
 Got it.
`=IF(A191="",B191,A191)`

Uses A191 if it has a value. Falls back to B191 if A191 is empty.

---

### 9. **Human** — 2026-04-29T06:34

build into the xlookup
build into the xlookup

---

### 10. **Claude** — 2026-04-29T06:35

```
This block is not supported on your current device yet.
```

`=XLOOKUP(IF(A191="",B191,A191),G:G,G:G)`

Uses A191 as the lookup key if it has a value, falls back to B191 if A191 is empty. Still returns the match from column G.
`=XLOOKUP(IF(A191="",B191,A191),G:G,G:G)`

Uses A191 as the lookup key if it has a value, falls back to B191 if A191 is empty. Still returns the match from column G.
