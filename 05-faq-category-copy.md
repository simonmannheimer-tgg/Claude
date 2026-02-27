# Process 05: FAQ & Category Copy

> **Version:** 1.0 — Extracted from Master Prompt Tasks 6–8  
> **Last updated:** 2026-02-27

## Purpose

Generate FAQ sections and longer category copy for The Good Guys product pages. Three sub-tasks: general FAQ, brand+category FAQ with links, and extended PLP intro copy.

---

## Task 5A: FAQ Generation

**Input:** Primary search query + URL domain  
**Output:** 5–7 Q&A pairs

**Rules:**
- Questions closely related to the primary intent
- Natural, conversational phrasing
- Answers: factual, clear, 1–3 sentences
- Align with TGG context but not explicitly promotional
- Do not repeat the original query

**Output Format:**
```
Q: [Question]
A: [1-3 sentence answer]
```

---

## Task 5B: Brand+Category FAQ Copy (150–250 Words)

**Input:** URL, existing intro text, validated inlinks, sitemap data  
**Output:** HTML copy block with internal links

### Execution Steps

**Step 1 — Intent Analysis:** Determine primary intent from URL, generate 5+ related sub-queries

**Step 2 — Existing Intro Check:** Review existing intro, avoid repeating exact phrases or covering same features the same way. Provide complementary information with a different angle.

**Step 3 — Link Validation**

Calculate URL depth by counting forward slashes:
```
IF link_depth > current_depth → CHILD ✅ USE
IF link_depth == current_depth → SIBLING ✅ USE
IF link_depth < current_depth → PARENT ❌ NEVER USE
```

Only use links with HTTP status = 200. Never use 301, 302, 404, 410, 500.

**Step 4 — Entity Identification:** Extract minimum 5 entities (technologies, models/formats, capacities, specifications, smart features)

**Step 5 — Write 4 Paragraphs:**

| Paragraph | Content |
|-----------|---------|
| 1 | Overview with key technology/differentiator |
| 2 | Deep dive on main feature with specific benefits |
| 3 | Strategic list with intro sentence + ONE `<ul>` or `<ol>` (3–7 items). Each item: `<a href="[URL]">[Anchor]</a> — [benefit]` |
| 4 | Capacity/connectivity + related products (siblings only) |

**Step 6 — Linking Best Practices:**
- Link on FIRST mention
- Natural, descriptive anchor text
- Never use: "click here", "learn more", "read more"

### Tone
- Conversational and helpful (The Good Guys voice)
- Natural, not robotic
- Benefit-focused explanations
- Specific without overly precise percentages
- Avoid: "Best for:" templates, AI giveaway phrases, generic anchor text

### Output Format
```html
<p>[Overview with technology/benefit]</p>
<p>[Feature deep-dive]</p>
<p>[List intro:]</p>
<ul>
<li><a href="[URL]">[Anchor]</a> — [benefit]</li>
</ul>
<p>[Capacity/connectivity + related products]</p>
```

### QA Checklist
- [ ] 150–250 words
- [ ] Primary intent + 5 sub-intents addressed
- [ ] 5+ specific entities
- [ ] Exactly 1 list
- [ ] 0 parent links
- [ ] All links status = 200
- [ ] Natural brand tone
- [ ] No cannibalisation of existing intro

---

## Task 5C: Extended PLP Intro Copy (230–260 Words)

> **Note:** This is a LONGER format than Process 01 (which is 2 sentences, 230–260 characters). This is 230–260 WORDS.

**Input:** URL, category, brand info  
**Output:** Multi-paragraph category introduction

**Structure:**
1. **Hook** — Primary keyword in first 100 words
2. **Overview** — Category explanation and what's available
3. **Key options** — Main variations or formats
4. **Benefits/features** — Why users choose this category
5. **Soft guidance** — Help users understand selection criteria

**Requirements:**
- 230–260 words total
- Primary keyword in first 100 words
- 5+ entities included naturally
- Query fanout addressed
- Conversational brand tone
- Optional: One short list (3–5 items) for scannability

---

## Chaining

| Input from | This task | Feeds into |
|-----------|-----------|-----------|
| 04A/04B (Query + Fanout) | 5A (FAQ) | On-page FAQ sections |
| 04B (Fanout) + 06 (Links) | 5B (Brand+Category FAQ) | Category page bottom copy |
| 04B (Fanout) + 08 (EAV) | 5C (Extended PLP Intro) | Category page top/mid copy |
