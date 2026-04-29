---
title: Removing prompt tracking requirement (full)
parent: Chat/Light/2026-04-21-removing-prompt-tracking-requirement-b4664f
uuid: b4664f1f-c8fc-4176-90e6-4c1abc47b184
---

#chat/full #project/main #status/completed

# Removing prompt tracking requirement — Full Transcript

→ Light view: [[Chat/Light/2026-04-21-removing-prompt-tracking-requirement-b4664f]]
→ Medium view: [[Chat/Medium/2026-04-21-removing-prompt-tracking-requirement-b4664f]]

**Messages:** 7 | **Date:** 2026-04-21

---

### 1. **Human** — 2026-04-20T23:21

im hoping to be able to not need a prompt tracked before running this each time... how?
im hoping to be able to not need a prompt tracked before running this each time... how?

---

### 2. **Claude** — 2026-04-20T23:21

The user wants to avoid needing to track a prompt before running their agent each time. Let me look at the uploaded files to understand what they're working with, then search project knowledge for context.

---

### 3. **Claude** — 2026-04-20T23:22

The user wants to avoid manually tracking/entering a prompt before running their agent each time. Let me look at their uploaded files to understand the current state of their content brief creation agent.
```
This block is not supported on your current device yet.
```

The user is asking how to avoid needing to manually select/track a "Profound Prompt" before running the agent each time. Looking at the Start node, it has two Profound-specific inputs:

1. `Profound Topic` (type: `profound-topic`) - required
2. `Profound Prompt` (type: `profound-prompt`) - required

These are Profound's native data types that link to tracked prompts/topics in the platform. The user is asking: "How can I not need a prompt tracked before running this each time?"

The issue is that `Profound Prompt` is a `profound-prompt` type which requires selecting a tracked prompt from the Profound platform. 

The solution is to change the `Profound Prompt` input from a `profound-prompt` type to a plain `string` type, so users can type in any prompt directly at runtime instead of needing to pre-configure it in Profound. Since this input gets passed to the Generate Title and Generate Personas LLM nodes as the target prompt/query, I just need to update the data type on that input variable. to `string` type so users can enter their query directly without pre-setup. The `Profound Topic` field is trickier since it feeds into the Citation Pages node, which needs a topic to filter results—converting it to a string might break that functionality, so I need to check how Citation Pages actually uses the topic data.

The safest recommendation is to change just the Profound Prompt to `string` type and rename it something like "Target Query" for clarity. For the topic field, I should explain the tradeoff: keeping it as `profound-topic` preserves citation functionality, but switching to `string` would let them run ad-hoc queries without pre-tracking topics. Let me put together a clear answer with the JSON diff showing the change.The problem is your `Profound Prompt` Start variable has `data_type: profound-prompt`, which forces you to select a pre-tracked prompt from Profound's system before every run. Same issue with `Profound Topic` as `profound-topic`.

**The fix:** Change both to plain `string` type. You'll type the query/topic directly at runtime with no pre-setup required. The only tradeoff is that `Citation Pages` uses the Profound Topic natively. If you change it to a string, citation data won't filter correctly by topic.

Two options:

**Option A — Full freeform (no citation filtering).** Change both to `string`. Run anytime, no setup. Citation Pages node will return unfiltered data.

**Option B — Topic stays, prompt goes freeform.** Keep `Profound Topic` as `profound-topic` (so Citation Pages still filters correctly) but change only `Profound Prompt` to `string`. You'd still need a topic configured, but not a prompt tracked.

Given you said "prompt tracked" specifically, Option B is probably what you want. Here's the exact change to make in the JSON:

**Find this in the Start node `output_variables`:**
```json
{
  "variable": {
    "id": "01ea83db-8b86-4bc5-b514-1fa81ed70213",
    "name": "Profound Prompt",
    "data_type": {
      "kind": "profound",
      "type": "profound-prompt"
    },
    "required": true
  }
}
```

**Replace with:**
```json
{
  "variable": {
    "id": "01ea83db-8b86-4bc5-b514-1fa81ed70213",
    "name": "Target Query",
    "data_type": "string",
    "required": true
  }
}
```

No other changes needed. All the downstream nodes already reference this variable by UUID (`01ea83db...`), so renaming it doesn't break anything. It just becomes a text field at runtime instead of a prompt picker.

Want me to produce the full updated JSON with this applied?
 
The problem is your `Profound Prompt` Start variable has `data_type: profound-prompt`, which forces you to select a pre-tracked prompt from Profound's system before every run. Same issue with `Profound Topic` as `profound-topic`.

**The fix:** Change both to plain `string` type. You'll type the query/topic directly at runtime with no pre-setup required. The only tradeoff is that `Citation Pages` uses the Profound Topic natively. If you change it to a string, citation data won't filter correctly by topic.

Two options:

**Option A — Full freeform (no citation filtering).** Change both to `string`. Run anytime, no setup. Citation Pages node will return unfiltered data.

**Option B — Topic stays, prompt goes freeform.** Keep `Profound Topic` as `profound-topic` (so Citation Pages still filters correctly) but change only `Profound Prompt` to `string`. You'd still need a topic configured, but not a prompt tracked.

Given you said "prompt tracked" specifically, Option B is probably what you want. Here's the exact change to make in the JSON:

**Find this in the Start node `output_variables`:**
```json
{
  "variable": {
    "id": "01ea83db-8b86-4bc5-b514-1fa81ed70213",
    "name": "Profound Prompt",
    "data_type": {
      "kind": "profound",
      "type": "profound-prompt"
    },
    "required": true
  }
}
```

**Replace with:**
```json
{
  "variable": {
    "id": "01ea83db-8b86-4bc5-b514-1fa81ed70213",
    "name": "Target Query",
    "data_type": "string",
    "required": true
  }
}
```

No other changes needed. All the downstream nodes already reference this variable by UUID (`01ea83db...`), so renaming it doesn't break anything. It just becomes a text field at runtime instead of a prompt picker.

Want me to produce the full updated JSON with this applied?

---

### 4. **Human** — 2026-04-20T23:32

topic stays and is a locked range of options, prompt is freeform - however, how does this change research? how can we get the most out of it?
topic stays and is a locked range of options, prompt is freeform - however, how does this change research? how can we get the most out of it?

---

### 5. **Claude** — 2026-04-20T23:33

The user wants to understand the implications of:
1. Keeping `Profound Topic` as `profound-topic` (locked dropdown)
2. Making `Profound Prompt` a freeform string

They want to know how this changes the research pipeline and how to get the most out of the freeform prompt input.

Let me look at the full agent to understand where `Profound Prompt` (id: `01ea83db-8b86-4bc5-b514-1fa81ed70213`) is used throughout the pipeline, and how the current research nodes work.

From what I've seen:
- Generate Title LLM uses it as "Target prompt/query"


- Generate Personas LLM also uses it as "Target prompt/query"

I need to trace through the rest of the pipeline to see all the places where this freeform prompt gets injected and how it shapes the downstream research outputs.
```
This block is not supported on your current device yet.
```

Now let me read the remaining truncated section to see the full middle part of the pipeline.
```
This block is not supported on your current device yet.
```

Now let me read the remaining truncated section (572-674) to see the AEO opportunities and page outline nodes.
```
This block is not supported on your current device yet.
```

Now I have a complete picture of the pipeline. Let me map out where the `Profound Prompt` variable (id: `01ea83db-8b86-4bc5-b514-1fa81ed70213`) is used:

1. **Generate Title** (node `8QuvCGQwxJOoklJpjm_ir`) - as "Target prompt/query" 
2. **Generate Personas** (node `g86V0_csBNCr0-Fg-qah3`) - as "Target prompt/query"
3. **Compile Content Brief** (node `JE5pw-_u2fMhlRxrSVr78`) - as "Target prompt" in the final brief output


4. The rest of the pipeline relies on `Primary Keyword` for research operations, so the `Profound Prompt` is really just feeding intent signals into title and persona generation before being displayed in the final output.

I'm thinking about what the `Profound Prompt` could become if we treated it as a richer input—right now it's just a signal for understanding user intent, but as a freeform string it has potential to influence the research phase more directly, not just the framing phase.

The real gap is that the prompt barely touches the actual research work. It shapes how we present findings but doesn't inform SERP research, search queries, citation analysis, or outline generation—those all rely solely on the primary keyword. So the question becomes: how do we leverage freeform prompts to actually improve what research gets surfaced, not just how it's labeled?

The key moves are using the target query to drive richer Perplexity searches instead of keyword-only lookups, running SERP analysis against the actual user question rather than just the keyword to capture what's truly ranking for that intent, feeding the query into AEO opportunities so it shapes the specific angle being addressed, and extending it into the page outline generation as well.

I could also seed a Query Fanout node from this freeform query to surface all the related questions AI systems would tackle—that's valuable for structuring the brief. There's a tradeoff though: the Profound Prompt Responses node won't work without a tracked prompt, but Perplexity Search with the freeform query essentially gives you the same live AI response data anyway.

The real opportunity is treating the target query as a first-class research input rather than just a label for intent. The user should make it the primary driver for Perplexity, add it to SERP analysis or run a separate SERP call against it, and seed the Query Fanout from it—that's where the leverage is.Now I have the full picture. Here's what's actually happening and where the opportunity is.

**Where `Profound Prompt` currently does work:**
- Generate Title (intent signal)
- Generate Personas (intent signal)
- Compile Brief (displayed as "Target Prompt" label)

**Where it does nothing:** Every research node. Perplexity, SERP, Citation Analysis, AEO Opportunities, FAQs, Page Outline. All of those run off `Primary Keyword` only. The prompt is essentially decorative in the research pipeline.

---

**What you lose by going freeform**

One thing: access to the `Prompt Responses` Profound Data node, which shows what AI engines actually returned for that tracked prompt. That node requires a pre-tracked prompt. But Perplexity Search is a live proxy for the same thing, and you already have it.

---

**What you gain, and how to use it**

Right now Perplexity is queried as:
```
FAQs related to: {{primary_keyword}}
```

That's keyword-anchored. If your Target Query is something like *"what is the best robot vacuum for pet hair on carpet?"*, running Perplexity against the actual user question returns what AI engines surface for that intent, which is what you actually want for AEO. Same with PAA and the SERP node.

Three concrete improvements to make alongside the data_type change:

**1. Feed Target Query into Perplexity instead of (or alongside) Primary Keyword.** Change the Perplexity query to the Target Query. You'll get AI-answer-shaped research rather than generic FAQ research. This is the biggest gain.

**2. Add a second SERP call using the Target Query as the keyword.** Your current SERP runs against the Primary Keyword. Long-tail queries rank very different content. Running both gives you keyword-level and intent-level SERP data simultaneously.

**3. Add a Query Fanout Estimator seeded from the Target Query.** Currently there's no fanout in this agent at all. Seeding it from the full question (not just the keyword) maps how AI engines expand the search space around that query. Feed that output into the AEO Opportunities node. This directly shapes the outline and content structure.

---

**Net effect**

The brief goes from keyword-research-driven to intent-driven. The writer gets a structure that matches how an AI engine processes the question, not just how Google indexes the keyword. Want me to produce an updated JSON with these three changes wired in?
 
Now I have the full picture. Here's what's actually happening and where the opportunity is.

**Where `Profound Prompt` currently does work:**
- Generate Title (intent signal)
- Generate Personas (intent signal)
- Compile Brief (displayed as "Target Prompt" label)

**Where it does nothing:** Every research node. Perplexity, SERP, Citation Analysis, AEO Opportunities, FAQs, Page Outline. All of those run off `Primary Keyword` only. The prompt is essentially decorative in the research pipeline.

---

**What you lose by going freeform**

One thing: access to the `Prompt Responses` Profound Data node, which shows what AI engines actually returned for that tracked prompt. That node requires a pre-tracked prompt. But Perplexity Search is a live proxy for the same thing, and you already have it.

---

**What you gain, and how to use it**

Right now Perplexity is queried as:
```
FAQs related to: {{primary_keyword}}
```

That's keyword-anchored. If your Target Query is something like *"what is the best robot vacuum for pet hair on carpet?"*, running Perplexity against the actual user question returns what AI engines surface for that intent, which is what you actually want for AEO. Same with PAA and the SERP node.

Three concrete improvements to make alongside the data_type change:

**1. Feed Target Query into Perplexity instead of (or alongside) Primary Keyword.** Change the Perplexity query to the Target Query. You'll get AI-answer-shaped research rather than generic FAQ research. This is the biggest gain.

**2. Add a second SERP call using the Target Query as the keyword.** Your current SERP runs against the Primary Keyword. Long-tail queries rank very different content. Running both gives you keyword-level and intent-level SERP data simultaneously.

**3. Add a Query Fanout Estimator seeded from the Target Query.** Currently there's no fanout in this agent at all. Seeding it from the full question (not just the keyword) maps how AI engines expand the search space around that query. Feed that output into the AEO Opportunities node. This directly shapes the outline and content structure.

---

**Net effect**

The brief goes from keyword-research-driven to intent-driven. The writer gets a structure that matches how an AI engine processes the question, not just how Google indexes the keyword. Want me to produce an updated JSON with these three changes wired in?

---

### 6. **Human** — 2026-04-21T01:54

I used to spend 4-6 hours on every semantic content brief.30 briefs per month was my hard ceiling.Here is what that 6 hours actually looked like.Open Ahrefs. Pull 2,400 queries.Classify all of them into 5 intent streams by hand.Read 10 competitor pages front to back.Extract 180+ entities. Classify each by Purpose, Property, Relationship.Cross-reference GSC against the Ahrefs dataset.Screenshot the SERP for every target query.Capture every featured snippet, every PAA box, every related search.Map each classified query to a specific heading.Check all 9 semantic frames are filled. Find the gaps.Plan format diversity per section.Layer brand positioning, voice, and conversion angle onto every heading.Compile. Review. Ship.Six hours per brief. One trained operator.And the brief was still not good enough.Source context disconnected from queries.Brand voice bolted on at the end.Conversion angle missing entirely.It reads like a research document, not a production spec.I tried to hire my way out of the ceiling. Training a new brief operator took 6 to 8 weeks. Each one produced slightly different quality.That was my permanent ceiling. 30 briefs a month.Zero scale path.So I spent 6 months building the engine that does all of it for me.The Semantic Content Brief Engine runs all 12 manual steps through a 4-phase automated pipeline.Research → Outline → Brief → Verification.- Every phase runs specialized engines with AI agents.- Competitor intelligence extraction at 6 to 10 layers.- Entity mapping with PPR classification.- 5-stream query networks.- 9-frame coverage checks.- 13 structured fields per section, computed from upstream research.The time has shortened to 15 minutes per brief now.Brutal quality standard. Actually higher, because every field is computed, not guessed.This is NOT ChatGPT with a better prompt.A generic AI brief gives you 3 sentences. "Write 1,500 words on X. Include keywords Y and Z. Use H2 headings."A Semantic Content Brief gives you 13 structured fields per section.Entity maps. Frame context. Modality matching. Content boundaries. Dedup tracking. Bold guidance. Persona targeting. CTA integration.104 to 195 production decisions per brief, all computed before the writer touches it.If your semantic brief can be produced in 90 seconds by a single prompt, it was never a semantic brief. It was an outline with keywords wearing a costume.I wrote a full breakdown of the engine. The 12 manual steps it replaces.The 13 fields it computes per section. A side-by-side brief comparison. How it differs from every generic brief tool on the market.You can also get a free sample brief for one of your own pages.We're only sending out a handful of these. And before we do, we'll review your site to make sure we're the right fit.Built on the semantic SEO methodology pioneered by Koray Tugberk GUBUR

thoughts on this?
I used to spend 4-6 hours on every semantic content brief.30 briefs per month was my hard ceiling.Here is what that 6 hours actually looked like.Open Ahrefs. Pull 2,400 queries.Classify all of them into 5 intent streams by hand.Read 10 competitor pages front to back.Extract 180+ entities. Classify each by Purpose, Property, Relationship.Cross-reference GSC against the Ahrefs dataset.Screenshot the SERP for every target query.Capture every featured snippet, every PAA box, every related search.Map each classified query to a specific heading.Check all 9 semantic frames are filled. Find the gaps.Plan format diversity per section.Layer brand positioning, voice, and conversion angle onto every heading.Compile. Review. Ship.Six hours per brief. One trained operator.And the brief was still not good enough.Source context disconnected from queries.Brand voice bolted on at the end.Conversion angle missing entirely.It reads like a research document, not a production spec.I tried to hire my way out of the ceiling. Training a new brief operator took 6 to 8 weeks. Each one produced slightly different quality.That was my permanent ceiling. 30 briefs a month.Zero scale path.So I spent 6 months building the engine that does all of it for me.The Semantic Content Brief Engine runs all 12 manual steps through a 4-phase automated pipeline.Research → Outline → Brief → Verification.- Every phase runs specialized engines with AI agents.- Competitor intelligence extraction at 6 to 10 layers.- Entity mapping with PPR classification.- 5-stream query networks.- 9-frame coverage checks.- 13 structured fields per section, computed from upstream research.The time has shortened to 15 minutes per brief now.Brutal quality standard. Actually higher, because every field is computed, not guessed.This is NOT ChatGPT with a better prompt.A generic AI brief gives you 3 sentences. "Write 1,500 words on X. Include keywords Y and Z. Use H2 headings."A Semantic Content Brief gives you 13 structured fields per section.Entity maps. Frame context. Modality matching. Content boundaries. Dedup tracking. Bold guidance. Persona targeting. CTA integration.104 to 195 production decisions per brief, all computed before the writer touches it.If your semantic brief can be produced in 90 seconds by a single prompt, it was never a semantic brief. It was an outline with keywords wearing a costume.I wrote a full breakdown of the engine. The 12 manual steps it replaces.The 13 fields it computes per section. A side-by-side brief comparison. How it differs from every generic brief tool on the market.You can also get a free sample brief for one of your own pages.We're only sending out a handful of these. And before we do, we'll review your site to make sure we're the right fit.Built on the semantic SEO methodology pioneered by Koray Tugberk GUBUR

thoughts on this?

---

### 7. **Claude** — 2026-04-21T01:55

The user is sharing a LinkedIn-style post about a "Semantic Content Brief Engine" and asking for my thoughts. They want honest critique, not agreement. Let me analyze this critically given the context of what we're building together.

Key claims to evaluate:
1. 13 structured fields per section computed from upstream research
2. 4-phase pipeline: Research → Outline → Brief → Verification
3. 15 minutes per brief
4. "Built on Koray Tugberk GUBUR's methodology"

The diagram shows: Outline engine (heading architecture) + Architecture engine (conversion flow) → Brief engine (section guidance), with 14 fields per section.


The framework itself is legitimately sophisticated—most briefs don't tackle modality matching, dedup tracking, semantic requirements, and content boundaries the way this does. The PPR entity classification (Purpose, Property, Relationship) is a real methodology. But the "104 to 195 production decisions per brief" metric is just multiplying 14 fields by the number of sections, which feels like inflating the numbers for impact.

What's more useful to think about: how does this compare to what we're building in Profound, and what can we actually learn from their 14-field approach? Our agent covers citation analysis, SERP analysis, keyword data, personas, page outlines, FAQs, and AEO opportunities, but we're missing their explicit question modality matching and gap context analysis—they're identifying what competitors miss per section, whereas we're looking at broader SERP patterns. Their framework also includes frame context, which we haven't explicitly mapped out yet.

The real difference is that their system operates at the section level rather than the article level. They generate 14 fields for each heading, which gives writers much more granular guidance than our current approach of producing one outline and one set of AEO opportunities for the whole piece. We could partially replicate this, though there are some constraints to consider. -by-section computation would require either a loop pattern through a Code node or processing all sections in a single LLM call. The verification phase with its 9-frame coverage check is something we're missing entirely.

So here's what matters: the 14-field-per-section structure is the real takeaway. Our current approach works at the article level, but theirs operates at the section level—after generating the page outline, I should add another LLM pass that fills in 8-10 of those fields for each H2 heading. Adding a verification phase that checks the outline against intent streams and flags gaps would close another gap. The "built on Koray" is a credibility signal, and their methodology is publicly documented.Honest take: there's one genuinely important idea buried under a lot of sales copy, and it's directly relevant to what we're building.

**The real insight**

The 14 fields per section. Not per article. Per H2.

That's the actual delta between this and a standard brief. Most briefs, including ours right now, produce one outline and one set of guidance for the whole article. This system computes section-level instructions. The writer doesn't just get headings, they get format guidance, content boundaries, dedup tracking, bold guidance, and CTA placement for each individual section before they write a word.

That's a meaningfully different production spec.

**What our agent currently does vs what this does**

Our pipeline produces article-level outputs: one keyword table, one AEO opportunities section, one outline, one FAQ table. The outline node generates H2s but gives the writer zero guidance on how to execute each one. The writer still has to make 100+ decisions themselves.

This approach flips that. The outline becomes the input to a brief engine that populates 14 fields per heading. The writer's job is execution, not interpretation.

**What's worth stealing for our agent**

After "Draft Page Outline" generates the H2 structure, add a section brief node that takes each heading and computes at minimum: question modality, format guidance, content boundaries, and semantic reqs. That's 4 of the 14 fields and it would immediately make the brief significantly more useful to a writer.

A verification pass is also worth adding, checking that the outline covers all intent streams from the query fanout before the brief compiles.

**What to ignore**

The 104-195 decisions metric is 14 fields multiplied by section count. The "6 months building" and "brutal quality standard" framing is positioning. The Koray methodology reference is real but the underlying entity classification (PPR) and 9-frame coverage concepts are publicly documented.

The comparison to "ChatGPT with a better prompt" is a strawman. The actual comparison is: article-level guidance vs section-level guidance. That's the real question.

Want to explore adding a section-brief node to our pipeline?
 
Honest take: there's one genuinely important idea buried under a lot of sales copy, and it's directly relevant to what we're building.

**The real insight**

The 14 fields per section. Not per article. Per H2.

That's the actual delta between this and a standard brief. Most briefs, including ours right now, produce one outline and one set of guidance for the whole article. This system computes section-level instructions. The writer doesn't just get headings, they get format guidance, content boundaries, dedup tracking, bold guidance, and CTA placement for each individual section before they write a word.

That's a meaningfully different production spec.

**What our agent currently does vs what this does**

Our pipeline produces article-level outputs: one keyword table, one AEO opportunities section, one outline, one FAQ table. The outline node generates H2s but gives the writer zero guidance on how to execute each one. The writer still has to make 100+ decisions themselves.

This approach flips that. The outline becomes the input to a brief engine that populates 14 fields per heading. The writer's job is execution, not interpretation.

**What's worth stealing for our agent**

After "Draft Page Outline" generates the H2 structure, add a section brief node that takes each heading and computes at minimum: question modality, format guidance, content boundaries, and semantic reqs. That's 4 of the 14 fields and it would immediately make the brief significantly more useful to a writer.

A verification pass is also worth adding, checking that the outline covers all intent streams from the query fanout before the brief compiles.

**What to ignore**

The 104-195 decisions metric is 14 fields multiplied by section count. The "6 months building" and "brutal quality standard" framing is positioning. The Koray methodology reference is real but the underlying entity classification (PPR) and 9-frame coverage concepts are publicly documented.

The comparison to "ChatGPT with a better prompt" is a strawman. The actual comparison is: article-level guidance vs section-level guidance. That's the real question.

Want to explore adding a section-brief node to our pipeline?
