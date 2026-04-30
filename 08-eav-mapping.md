# Process 08: EAV Mapping (Entity → Attributes → Values)

> **Version:** 2.0 — Refocused as a foundational analysis process  
> **Last updated:** 2026-02-27

## Purpose

Map the entity landscape for a product category. This produces a structured list of "things to cover" that feeds into other content processes — PLP intros (01), FAQ copy (05), metadata (02), and AEO (07). EAV mapping is the research step; the writing happens in other processes.

---

## How It Works

### 1. Identify the Main Entity
Start with the product category or brand+category combination.

**Example:** Sound Bars, 85-Inch TVs, Samsung Washing Machines, Dyson Vacuums

### 2. Fan Out to Attributes
Identify the key attributes a buyer would care about or search for. These vary by category but typically include:

- **Brand** — which brands are in the range
- **Technology** — OLED, QLED, Reverse Cycle, Heat Pump, Inverter, etc.
- **Capacity / Size / Resolution** — litres, kg, inches, pixels
- **Smart Features** — app control, voice assistant compatibility, Wi-Fi
- **Connectivity** — Bluetooth, HDMI, USB-C, AirPlay
- **Audio / Visual Features** — Dolby Atmos, HDR, refresh rate
- **Use Case** — home office, bedroom, family room, pet hair, small spaces
- **Energy** — star rating, energy-efficient tech (only where genuinely applicable)
- **Format / Type** — stick/barrel/robot, front/top loader, portable/split system
- **Price Tier** — budget / mid-range / premium (confirm from TGG site)
- **Accessories / Extras** — compatible add-ons, mounting options, included items
- **Dimensions / Colour** — if relevant to purchase decisions

Don't force every attribute. If an attribute isn't meaningful for the category, skip it. If there's a category-specific attribute not listed here (e.g. refresh rate for gaming monitors, suction power for vacuums), add it.

### 3. Map Values for Each Attribute

For each relevant attribute, provide:

| Field | What it is |
|-------|-----------|
| **Values** | Realistic examples from the TGG range |
| **User Value** | Why this matters to a buyer — the benefit or problem it solves |
| **Search Intent** | 1–2 example queries a real person would type |

### Output Format
```
Entity: [Category Name]

Attribute: Brand
Values: Samsung, LG, Sony, Hisense
User Value: Choose from brands with different strengths — Samsung for smart features, LG for display tech, etc.
Search Intent: "best TV brands Australia", "Samsung vs LG TV"

Attribute: Technology
Values: OLED, QLED, LED, Mini LED
User Value: Affects picture quality, black levels, brightness, and price point
Search Intent: "OLED vs QLED", "is Mini LED worth it"

[...continue for each relevant attribute]
```

---

## Price Tier Segmentation

When mapping price range, confirm actual prices from TGG and segment into tiers:

| Tier | Use for |
|------|---------|
| Budget | Entry-level, price-sensitive buyers |
| Mid-range | Most common purchase range |
| Premium | High-end, feature-rich |

This helps other processes target the right intent (e.g. FAQ copy for budget buyers has different questions than for premium buyers).

---

## How EAV Feeds Other Processes

| Process | What it takes from EAV |
|---------|----------------------|
| **01 (PLP Intros)** | Top 3–4 entities to mention in 2 sentences. Brands for category PLPs. Tech/specs for brand PLPs. |
| **02 (Metadata)** | Key features and brands for description. Primary category keyword for title. |
| **04 (Content Analysis)** | Entity list supplements extracted entities. Search intents feed query fanout. |
| **05 (FAQ/Category Copy)** | Entity list ensures FAQ coverage is comprehensive. User values become FAQ answers. Search intents become FAQ questions. |
| **07 (AEO)** | Entity richness improves AI citability. Triplets (entity→attribute→value) make content more extractable. |

---

## When to Run EAV Mapping

- **Before writing any category page content** — run EAV first, then use the output to inform other processes
- **When entering a new category** — map once, reference repeatedly
- **When the product range changes significantly** — update the EAV map (new brands, new tech, discontinued lines)

---

## QA Checklist

- [ ] Main entity clearly identified
- [ ] 6+ attributes mapped (or justified why fewer)
- [ ] Each attribute has realistic values (not made up)
- [ ] User value explains why a buyer cares (not just what the attribute is)
- [ ] Search intents sound like real queries, not keyword fragments
- [ ] Price tiers confirmed against actual TGG range
- [ ] Category-specific attributes included where relevant
- [ ] No forced/irrelevant attributes
