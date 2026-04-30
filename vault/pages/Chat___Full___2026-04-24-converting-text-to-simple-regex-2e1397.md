---
title: Converting text to simple regex (full)
parent: Chat/Light/2026-04-24-converting-text-to-simple-regex-2e1397
uuid: 2e1397b7-c40f-4849-82ab-b17faf687a43
---

#chat/full #project/closed-tactical-tasks #status/tactical

# Converting text to simple regex — Full Transcript

→ Light view: [[Chat/Light/2026-04-24-converting-text-to-simple-regex-2e1397]]
→ Medium view: [[Chat/Medium/2026-04-24-converting-text-to-simple-regex-2e1397]]

**Messages:** 4 | **Date:** 2026-04-24

---

### 1. **Human** — 2026-04-24T04:06

turn this into a regex, keep it simple so no need for good guys washer|good guys phone etc.
turn this into a regex, keep it simple so no need for good guys washer|good guys phone etc.

---

### 2. **Claude** — 2026-04-24T04:06

What's the string you want to turn into a regex? I don't see any text or pattern in your message, only the uploaded file.
 What's the string you want to turn into a regex? I don't see any text or pattern in your message, only the uploaded file.

---

### 3. **Human** — 2026-04-24T04:07

look at the file
look at the file

---

### 4. **Claude** — 2026-04-24T04:07

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

These are all brand queries (navigational, "good guys" + product). The simple regex to match all of them in one pattern:

```
(good\s*guys|goodguys|the\s+good\s+guys)
```

That covers:
- `good guys` (with space)
- `goodguys` (no space, e.g. `goodguys tv`, `goodguys iron`)
- `the good guys` (full name variant)

If you need it case-insensitive, add the `i` flag. If you want to exclude the two non-brand outliers (`dyson v8 cyclone`, `induction cooktop`, `phone holder`, `eufy`), this regex already handles that since those don't contain any variant of the brand name.
These are all brand queries (navigational, "good guys" + product). The simple regex to match all of them in one pattern:

```
(good\s*guys|goodguys|the\s+good\s+guys)
```

That covers:
- `good guys` (with space)
- `goodguys` (no space, e.g. `goodguys tv`, `goodguys iron`)
- `the good guys` (full name variant)

If you need it case-insensitive, add the `i` flag. If you want to exclude the two non-brand outliers (`dyson v8 cyclone`, `induction cooktop`, `phone holder`, `eufy`), this regex already handles that since those don't contain any variant of the brand name.
