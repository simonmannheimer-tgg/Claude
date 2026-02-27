# Process 06: Internal Linking

> **Version:** 1.0 — Extracted from Master Prompt Tasks 9–12  
> **Last updated:** 2026-02-27

## Purpose

Find, validate, and insert internal links into content. Four sub-tasks that chain together.

---

## Task 6A: Find Link Opportunities

**Input:** Primary keyword, article summary, candidate URLs (from sitemap)  
**Output:** Ranked list of 10 best URLs

**Evaluation criteria:**
- Topical overlap with article summary
- Semantic relationship to primary keyword
- Whether linking provides genuine reader value
- Complementary depth (covers related subtopic, supports claim, expands concept)

**Rules:**
- Do not hallucinate links — only use provided candidates
- If fewer than 10 candidates exist, rank all available
- No descriptions or explanations

**Output:**
```
1. https://...
2. https://...
...
10. https://...
```

---

## Task 6B: Hierarchical Link Validation

**Input:** Current page URL + candidate link URLs  
**Output:** Links categorised as child/sibling/parent

**Method:** Count forward slashes in each URL:

```
link_depth > current_depth → CHILD ✅ USE
link_depth == current_depth → SIBLING ✅ USE
link_depth < current_depth → PARENT ❌ NEVER USE
```

**Examples:**
```
Current: /brand/category/subcategory

✅ /brand/category/subcategory/model     (CHILD)
✅ /brand/category/other-subcategory     (SIBLING)
❌ /brand/category                       (PARENT)
❌ /brand                                (PARENT)
```

**Output:**
```
CHILD LINKS (USE):
- [URL]

SIBLING LINKS (USE):
- [URL]

PARENT LINKS (NEVER USE):
- [URL]
```

---

## Task 6C: Link Status Verification

**Input:** List of proposed link URLs  
**Output:** Approved/rejected list

**Rules:**
- Only approve HTTP status 200
- Reject: 301, 302, 404, 410, 500

**Output:**
```
✅ 200 OK: [URL]
❌ 404: [URL] — DO NOT USE
❌ 301: [URL] — DO NOT USE
```

---

## Task 6D: Insert Links into Article

**Input:** Article content (markdown) + list of validated links  
**Output:** Full article with links inserted

**Rules:**
- Insert as natural inline hyperlinks on existing anchor text
- Anchor text must be contextually relevant to the linked page
- Never use: "click here", "learn more", "read more"
- Do NOT add, remove, or modify any words, sentences, or paragraphs
- The only changes are wrapping existing text in markdown hyperlinks
- Try to insert all recommended links
- A link may appear more than once if naturally appropriate
- Exclude ads, TOC, and footer from output

---

## Standard Workflow

```
6A (Find Opportunities)
  → 6B (Hierarchy Validation)
    → 6C (Status Verification)
      → 6D (Insert Links)
```

Or chain from content analysis:
```
04C (Summarise) → 04D (Keyword) → 6A → 6B → 6C → 6D
```

---

## Linking Best Practices (Used Across All Processes)

- Link on **first mention** of a term
- Natural, descriptive anchor text — never generic
- Child and sibling links only — never link to parent pages
- Only 200 OK status links
- 1 list per FAQ/copy block, 3–7 items per list
- Each list item format: `<a href="[URL]">[Anchor]</a> — [benefit]`
