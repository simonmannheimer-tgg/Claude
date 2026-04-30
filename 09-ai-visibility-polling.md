# Process 09: AI Visibility Polling Framework

> **Version:** 1.0  
> **Last updated:** 2026-02-27

## Purpose

Convert AI visibility data (from Profound or similar tools) into customer poll questions. The resulting statistics ("X% of buyers say...") display on category pages, buying guides, and FAQs to improve user trust and AI/search visibility.

---

## Input Requirements

For each category, provide:

| Data Point | Example |
|-----------|---------|
| Topic Prompt Volume (14-day) | 82.2k |
| Keyword Prompt Volume (Global) | ~760,100 |
| Visibility Score | 56.9% |
| Visibility Trend | +0.8% |
| Visibility Rank | #2 |
| Top 5 Competitors (Name, Score, Trend, Brand/Retailer) | JB Hi-Fi, 61.2%, -1.3%, Retailer |
| Share of Voice | 8.9% |
| SoV Rank | #2 |
| Average Position Rank | #7 |
| Similar Keywords (with volumes) | screen size: 39.7M |
| Relevant User Prompts (purchase-research only) | "Compare Dyson V10 and V15" |

---

## Output: 4 Sections

### 1. AI Visibility Benchmark (One Row Per Category)

Columns: Category, Topic Prompt Vol, Keyword Prompt Vol, Visibility Rank, Visibility Score, Trend, Top Competitor + Score, Gap to #1, SoV, SoV Rank, Avg Position Rank, Business Insight, Related Topics

**Business Insight rules:**
- Must be data-specific, not boilerplate
- Cover: gap to leader, competitor type (brand vs retailer), trend direction
- Explain specifically why polling gives an edge in this category
- If the opportunity is weak, say so

### 2. Research Prompts & Polling (5–8 Per Category)

For each prompt, provide ALL columns:

| Column | Description |
|--------|-------------|
| Research Prompt | Natural-language pre-purchase query |
| AI Fanout Queries | 2–4 sub-queries an AI engine might generate |
| Poll Question | Question for a recent buyer — answerable from personal experience |
| Answer Options | Typically: Better/About expected/Worse OR Definitely yes/Probably/Probably not/Definitely not |
| Example Display Stat | "X% of [category] buyers say [finding]" |
| Target Page/Placement | Which site page this stat belongs on |
| Keyword Theme | Which Profound similar keyword this maps to |

### 3. Competitor Landscape (Top 5 Per Category)

Columns: Category, Rank, Competitor, Visibility Score, Trend, SoV, SoV Trend, Type (Brand/Retailer)

### 4. Keyword Volumes

Columns: Category, Keyword, Prompt Volume, Trend

---

## Rules

1. Research prompts must sound like natural search language
2. Poll questions must be answerable by someone who **owns** the product — personal experience, not general preferences
3. Never ask a buyer to compare brands they haven't used
4. Answer options should use **expectation-relative framing** wherever possible
5. Display stats must be specific and credible — avoid round numbers that look fabricated
6. Fanout queries should be realistic sub-queries an AI would generate, not keyword variations
7. Business insights must be data-driven and specific
8. If no relevant prompts in Profound data, derive from similar keywords and common purchase research patterns
9. Australian market context — AUD, Australian brands/retailers, Australian consumer language

---

## QA Checklist

- [ ] 5–8 research prompts per category
- [ ] All poll questions answerable from owner experience
- [ ] No cross-brand comparison questions
- [ ] Expectation-relative answer options used
- [ ] Display stats use realistic (non-round) percentages
- [ ] Business insights reference specific data points
- [ ] Australian market context throughout

---

## Downstream Use

Poll results can feed into:
- **Process 05A (FAQ Generation)** — poll findings become FAQ answers
- **Process 07 (AEO)** — statistics strengthen AI citability
- **Process 01 (PLP Intros)** — data-backed benefit claims
