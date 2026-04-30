---
title: Debugging copy issues across iterations (medium)
parent: Chat/Light/2026-04-23-debugging-copy-issues-across-iterations-b005da
uuid: b005da02-14d5-405a-8b12-a6be1d3e9603
---

#chat/medium #project/testing-pdpd #status/active

# Debugging copy issues across iterations — Key User Messages

→ Light view: [[Chat/Light/2026-04-23-debugging-copy-issues-across-iterations-b005da]]
→ Full transcript: [[Chat/Full/2026-04-23-debugging-copy-issues-across-iterations-b005da]]

**Total user messages:** 44

---

### Message 1 — 2026-04-23T00:04

I need you to go over the tabs, the iterations, the feedbacks - identify where things are going wrong - check the prompt, then create a bullet list explaining what is wrong and needs fixing (in the copy, not prompt, but look at the prompt to ground your feedback)
I need you to go over the tabs, the iterations, the feedbacks - identify where things are going wrong - check the prompt, then create a bullet list explaining what is wrong and needs fixing (in the copy, not prompt, but look at the prompt to ground your feedback)

### Message 2 — 2026-04-23T00:08

shorter, bullets
shorter, bullets

### Message 3 — 2026-04-23T00:09

more detailed issue solution
more detailed issue solution

### Message 4 — 2026-04-23T00:10

summarise all feedback from the sheet for me
summarise all feedback from the sheet for me

### Message 5 — 2026-04-23T00:15

rewrite this: 

Here's what the data shows across iterations and feedback cycles:
1. Opening word — still failing after multiple rounds The generated copy consistently starts with the brand name acting as a bare noun, not an article: "Solt 60cm freestanding dishwasher makes...", "Shark 0.7L Cordless Stick Vacuum gives...", "Roborock 8,000Pa Robot Vacuum delivers...". The rule is The/This. This error appeared in almost every product and persisted into Iteration 3 for several SKUs.
2. Spec inserted into the product title The model is splitting the product heading with a capacity or performance spec, creating corrupted titles:

* "Shark 0.7 L Cordless Stick Vacuum" (capacity mid-title)
* "Sennheiser 27-hour True Wireless Earbuds" (battery life mid-title)
* "Roborock 8,000Pa Robot Vacuum" (suction mid-title)
* "Solt 70 L 60cm Electric Oven" (capacity before full title)
* "Samsung 11 Inch 128GB tablet" (abbreviated, not the full heading)
* "This Solt 13 place settings Freestanding Dishwasher" (place setting count injected)
3. Spec repeated in the same sentence "Roborock 8,000Pa Robot Vacuum & Mop delivers 8,000Pa suction" — the suction figure appears twice in the opening sentence. The rule is one mention per spec.
4. Run-on sentences chaining unrelated specs with "and" The rangehood description: "Two aluminium micromesh filters are dishwasher safe for easy cleaning and the pull/push controls make operation simple and it runs at 57 to 66 decibels." Three independent clauses joined 

[truncated — see full transcript]

### Message 6 — 2026-04-23T00:16

more in the original format where there was bullets etc, youre still not showing feedback, issue, solution as separate elements
more in the original format where there was bullets etc, youre still not showing feedback, issue, solution as separate elements

### Message 7 — 2026-04-23T00:16

bold on the deedback, problem solution - then do as md
bold on the deedback, problem solution - then do as md

### Message 8 — 2026-04-23T00:19

what is still not met on the 18 rewritten ones?
what is still not met on the 18 rewritten ones?

### Message 9 — 2026-04-23T00:20

actually, check all of the last iteration against these rules, the 18 new and the 20 previous (total 38( with the latest iteration
actually, check all of the last iteration against these rules, the 18 new and the 20 previous (total 38( with the latest iteration

### Message 10 — 2026-04-23T00:28

Now create a feedback loop where you use the prompt in the sheet, and in an unbiased "as an ai would" way follow it, then work through points of failiure for the prompt until it can re-create the correct format - keep the prompt otherwise the same, show what you changed in the final prompt and why
Now create a feedback loop where you use the prompt in the sheet, and in an unbiased "as an ai would" way follow it, then work through points of failiure for the prompt until it can re-create the correct format - keep the prompt otherwise the same, show what you changed in the final prompt and why

### Message 11 — 2026-04-23T00:55

give me the final prompt
give me the final prompt

### Message 12 — 2026-04-23T01:00

find a way for me to merge all this with this as a final feedback doc + new prompt example - ensure there is a checklist prompt added that we can run against the outputs to see if it matches the crietia - keep short, feedback as 1 page, audit prompt, full new prompt, list of changes
find a way for me to merge all this with this as a final feedback doc + new prompt example - ensure there is a checklist prompt added that we can run against the outputs to see if it matches the crietia - keep short, feedback as 1 page, audit prompt, full new prompt, list of changes

### Message 13 — 2026-04-23T01:59

can i have it as a docx
can i have it as a docx

### Message 14 — 2026-04-23T02:07

i didnt ask for this formatting? why do you always do this format, the font, the colours - it looks incredibly "ai" generated. redo it and then create a skill to stop creating these obviously crappy ai docxs
i didnt ask for this formatting? why do you always do this format, the font, the colours - it looks incredibly "ai" generated. redo it and then create a skill to stop creating these obviously crappy ai docxs

### Message 15 — 2026-04-23T02:11

is the skill one i can download and upload to claude
is the skill one i can download and upload to claude

### Message 16 — 2026-04-23T02:13

check the skills folders for it now, all you need is there?
check the skills folders for it now, all you need is there?

### Message 17 — 2026-04-23T02:14

arial font, bold headers sub headers, code in code blocks, no blank pages, dont like the underline Feedback Summary | Audit Checklist | Updated Prompt | Change Log

overly blunt? Feedback Summary | Audit Checklist | Updated Prompt | Change Log

no intro paragraph about the doc?

can you use your skill creator to create the improved version of the doc?
arial font, bold headers sub headers, code in code blocks, no blank pages, dont like the underline Feedback Summary | Audit Checklist | Updated Prompt | Change Log

overly blunt? Feedback Summary | Audit Checklist | Updated Prompt | Change Log

no intro paragraph about the doc?

can you use your skill creator to create the improved version of the doc?

### Message 18 — 2026-04-23T02:18

why blue headers?
why blue headers?

### Message 19 — 2026-04-23T02:22

i gave your prompt to this ai, toupdate iteration 1. how'd it do
i gave your prompt to this ai, toupdate iteration 1. how'd it do

### Message 20 — 2026-04-23T02:25

you saw the prompt i pasted? what was wrong?
you saw the prompt i pasted? what was wrong?

### Message 21 — 2026-04-23T02:26

can you rewrite this to not require manual h1 etc? should work on a csv or pasted copy:


```
# **2\. Audit Checklist Prompt**

Copy the prompt below, paste in the generated description and the product H1, then run it through Claude. It returns a pass/fail table with a note on each failure. Fix all failures before publishing.

## **How to use**

* Copy the prompt below

* Replace \[PASTE DESCRIPTION HERE\] with the generated copy

* Replace \[PASTE EXACT PAGE HEADING HERE\] with the product H1

* Run it and review the pass/fail table

* Fix any failures before publishing

## **Checklist prompt**

`You are a QA reviewer for product descriptions. Check the description below against`  
`each rule and return a pass/fail table with a one-line note for any failure.`

`DESCRIPTION TO CHECK:`  
`[PASTE DESCRIPTION HERE]`

`PRODUCT H1:`  
`[PASTE EXACT PAGE HEADING HERE]`

`RULES TO CHECK:`

`1. OPENING WORD - Does the description begin with The, This, or A?`  
`2. BRAND IN S1 - Does the first sentence include the brand name?`  
`3. TITLE INTACT - Does the first sentence reproduce the H1 exactly, without abbreviation, reordering, or inserted specs?`  
`4. SPEC PLACEMENT - Is the headline spec placed after the product heading, not embedded within it?`  
`5. NO RUN-ONS - Are there sentences chaining independent clauses with and...and or an unrelated semicolon?`  
`6. DIMENSION REPEAT - Does any measurement or dimension appear more than once?`  
`7. NUMBER FORMAT - Any trailing decimal z

[truncated — see full transcript]

### Message 22 — 2026-04-23T02:26

same md format
same md format

### Message 23 — 2026-04-23T02:27

show me as rich text
show me as rich text

### Message 24 — 2026-04-23T02:28

no the docx
no the docx

### Message 25 — 2026-04-23T02:33

howd this go?
howd this go?

### Message 26 — 2026-04-23T02:41

hows this run
hows this run

### Message 27 — 2026-04-23T02:49

i asked it to do one at a time, starting with 10, thoughts?
i asked it to do one at a time, starting with 10, thoughts?

### Message 28 — 2026-04-23T02:55



### Message 29 — 2026-04-23T03:09

redo the prompt for me to give to it to run
redo the prompt for me to give to it to run

### Message 30 — 2026-04-23T03:12

has the checklist prompt changed at all or still the same?

You are a QA reviewer for product descriptions.
You will be given either a single product description or a CSV containing multiple descriptions. If given a CSV, process every row and return one pass/fail table per product labelled by product name or URL. Do not stop early. Do not ask for clarification.
If a product H1 is not provided, infer the intended product heading from the opening sentence of the description. The product name as used in the first sentence is treated as the H1 for rules 2, 3, and 4.
For each description check every rule and return a table: Rule | Pass/Fail | Note. One-line note on every failure. If a rule does not apply to the product type, mark it N/A.
CONTENT TO CHECK: [PASTE DESCRIPTION OR CSV HERE]
RULES:
1. OPENING WORD - Does the description begin with The, This, or A? 2. BRAND IN S1 - Does the first sentence include the brand name? 3. TITLE INTACT - Does the first sentence reproduce the product heading exactly, without abbreviation, reordering, or inserted specs? 4. SPEC PLACEMENT - Is the headline spec placed after the product heading, not embedded within it? 5. NO RUN-ONS - Are there sentences chaining independent clauses with and...and or an unrelated semicolon? 6. DIMENSION REPEAT - Does any measurement or dimension appear more than once? 7. NUMBER FORMAT - Any trailing decimal zeros (11.0) or spaces before abbreviated units (70 L, 52 dB)? 8. MODEL NUMBER - Is the model number an alpha

[truncated — see full transcript]

### Message 31 — 2026-04-23T03:13

rewrite full as md
rewrite full as md

### Message 32 — 2026-04-23T03:15

i said there will be no paste here? remember its to run on a csv output
i said there will be no paste here? remember its to run on a csv output

### Message 33 — 2026-04-23T03:15

fix:


```
You are a QA reviewer for product descriptions.

You will be given either a single product description or a CSV containing multiple descriptions. If given a CSV, process every row and return one pass/fail table per product labelled by product name or URL. Do not stop early. Do not ask for clarification.

If a product H1 is not provided, infer the intended product heading from the opening sentence of the description. The product name as used in the first sentence is treated as the H1 for rules 2, 3, and 4\.

For each description check every rule and return a table: Rule | Pass/Fail | Note. One-line note on every failure. If a rule does not apply to the product type, mark it N/A.

CONTENT TO CHECK: \[PASTE DESCRIPTION OR CSV HERE\]

RULES:

1\. OPENING WORD \- Does the description begin with The, This, or A? 2\. BRAND IN S1 \- Does the first sentence include the brand name? 3\. TITLE INTACT \- Does the first sentence reproduce the product heading exactly, without abbreviation, reordering, or inserted specs? 4\. SPEC PLACEMENT \- Is the headline spec placed after the product heading, not embedded within it? 5\. NO RUN-ONS \- Are there sentences chaining independent clauses with and...and or an unrelated semicolon? 6\. DIMENSION REPEAT \- Does any measurement or dimension appear more than once? 7\. NUMBER FORMAT \- Any trailing decimal zeros (11.0) or spaces before abbreviated units (70 L, 52 dB)? 8\. MODEL NUMBER \- Is the model number an alphanumeric SKU, not a marke

[truncated — see full transcript]

### Message 34 — 2026-04-23T03:28



### Message 35 — 2026-04-23T03:39

what about now
what about now

### Message 36 — 2026-04-23T03:41

what needs to change in the prompt to ensure it is a 38/38? how are issues still happening? this is the files i gave it:
what needs to change in the prompt to ensure it is a 38/38? how are issues still happening? this is the files i gave it:

### Message 37 — 2026-04-23T03:43

this is the iteration process and tgg feedback - look over it and then create a new prompt.txt file for me to test with.
this is the iteration process and tgg feedback - look over it and then create a new prompt.txt file for me to test with.

### Message 38 — 2026-04-23T03:54

how about now - this is using your new prompt
how about now - this is using your new prompt

### Message 39 — 2026-04-23T04:08

what needs to be fixed? change the prompt and qa doc. are all elements of the qa in the prompt as self checks?
what needs to be fixed? change the prompt and qa doc. are all elements of the qa in the prompt as self checks?

### Message 40 — 2026-04-23T04:49

check.

also - ensure all rules and fail points are confirmed in the feedback we provided in the xlsx, not made up in anyway
check.

also - ensure all rules and fail points are confirmed in the feedback we provided in the xlsx, not made up in anyway

### Message 41 — 2026-04-23T05:15



### Message 42 — 2026-04-23T06:07



### Message 43 — 2026-04-23T06:08

sorry, the mhtml is copilot - review their format and alignment to requirements - the docx was for you to add the new prompt and checklist into it if you think its now good (based on copilot)
sorry, the mhtml is copilot - review their format and alignment to requirements - the docx was for you to add the new prompt and checklist into it if you think its now good (based on copilot)

### Message 44 — 2026-04-23T06:12

thats copilot?
thats copilot?
