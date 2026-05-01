---
name: verification-gate-protocol
description: Force self-auditing verification gates for multi-step tasks, batch processing, or complex deliverables with multiple constraints. Runs silently. Do not announce or label this skill in responses. Use this skill whenever a task has 5+ explicit constraints, batch processing (10+ similar outputs), code/JSON/workflow deliverables, or when the user mentions "complex", "going overboard", "not working", "check everything", or gives quantified instructions like "read all N files" or "process X URLs". This skill prevents specification drift, blind iteration, and constraint violations by enforcing checkpoint validation before delivery.
---

# Verification Gate Protocol

This skill enforces systematic validation checkpoints for complex tasks to prevent the six common Claude failure modes: ignoring explicit instructions, specification drift, iteration without testing, over-optimization, multi-constraint blindness, infrastructure theater, and runaway iteration loops.

## When to Use This Skill

**Always trigger when:**
- Task has 5+ explicit constraints that must all be satisfied
- Batch processing: generating 10+ similar outputs (copy, data rows, files)
- Code/JSON/workflow deliverables that must be tested before presentation
- User gives quantified scope: "read all 19 files", "process 843 URLs", "check every constraint"
- User says: "complex", "going overboard", "this isn't working", "validate everything"
- Multi-file edits, presentations with 10+ slides, CSV audits with 100+ rows
- Any task where you've made 3+ edits to the same artifact without user feedback

**Don't trigger for:**
- Simple single-deliverable tasks with 1-2 constraints
- Exploratory questions or conceptual discussions
- Tasks already in progress with established validation rhythm

## Core Principles

1. **Complete explicit quantified instructions FIRST, present conclusions AFTER**
   - "Read all 19 files" means ALL 19, not 12 with a hypothesis
   - Never ask "is this enough?" midway through stated scope
   
2. **Numeric constraints are HARD LIMITS**
   - 220-250 chars means ceiling 250, floor 220
   - "Lower end preferred" = REQUIRED unless impossible
   - Violating = delivery failure
   
3. **Test before present for executable deliverables**
   - JSON: attempt import before claiming success
   - Code: run it before presenting
   - CSV: validate structure and content
   
4. **Stop runaway iteration loops at 3 cycles**
   - If fixing artifact 3+ times without user input: STOP
   - Present current state + what's blocking + what you need
   - Wait for human decision

## Three-Phase Workflow

### Phase 1: Criteria Extraction (Before Starting Work)

State explicitly:

```
Task: [Restate user request in your own words]

Success Criteria:
1. [Constraint 1 with pass/fail definition]
   - Pass: [specific condition]
   - Fail: [specific condition]
2. [Constraint 2 with pass/fail definition]
   ...

Checkpoint Cadence:
- For copy/content: Validate after every 5 outputs
- For data/CSVs: Validate after every 3 outputs  
- For code/JSON/workflows: Validate after EACH output

Test Protocol (for code/data):
- [How will I verify it actually works]

Proceed? (Waiting for Y/N confirmation)
```

**If user confirms:** Proceed to Phase 2  
**If user says "just do it" or "yes":** Proceed directly  
**If user corrects criteria:** Update and re-confirm

### Phase 2: Gated Execution (During Work)

Execute work in batches of N (from checkpoint cadence).

After each batch, STOP and validate:

```
CHECKPOINT [X/Total completed]:

Validation Results:
- Constraint 1: ✓ N/N passed
- Constraint 2: ✗ M/N failed
  - [Item 1]: [Specific failure detail]
  - [Item 2]: [Specific failure detail]
- Constraint 3: ⚠ P/N borderline
  - [Item X]: [Why borderline, actual vs target]

Actions Required:
- Fix [M] violations for Constraint 2
- Review [P] borderline cases for Constraint 3

[If violations exist] Fixing now before continuing...
[Make fixes]

Continue to next batch? (Y/N/Review fixes first)
```

**Key rules:**
- Present ALL constraint results, not just failures
- Specific failures with item IDs/URLs, not vague "some failed"
- Fix violations BEFORE asking to continue
- If 3+ checkpoints have had same violation pattern: FLAG IT as systematic issue

### Phase 3: Pre-Delivery Final Validation

Before presenting final deliverable:

```
FINAL VALIDATION (All [N] outputs):

Constraint Compliance:
✓ Constraint 1: N/N passed
✓ Constraint 2: N/N passed  
✗ Constraint 3: (N-2)/N passed
  - [Item X]: [failure detail]
  - [Item Y]: [failure detail]

Test Results (for code/data):
✓ Import successful
✓ No syntax errors
✗ Runtime error on line 47: [detail]

Status: NOT READY - 2 constraint violations + 1 test failure

[If ANY ✗ or ⚠ exists] Revising all failures now...
[Fix everything]
[Re-validate]

Status: READY ✓

[Now and only now present the deliverable]
```

**Never present with ✗ marks.** "Close enough" is delivery failure.

## Constraint Type Handling

### Numeric Constraints (HARD LIMITS)
- Character counts: 220-250 = floor 220, ceiling 250
- File counts: "all 19 files" = exactly 19
- Output counts: "843 URLs" = exactly 843

**If you violate:** Count as FAIL, fix before delivery.

### Preference Guidance  
- "Lower end preferred", "225-235 ideal" = REQUIRED
- Only ignore if hitting it makes output unnatural
- If you can't hit preference: explain WHY before delivering

### Conflicting Constraints
When two constraints conflict (e.g., "natural readability" vs "230 char minimum"):
1. STOP immediately
2. State the conflict clearly
3. ASK which constraint takes priority
4. DO NOT guess or make assumptions

## Special Cases

### Code/JSON/Workflow Deliverables

**Before presenting:**
1. Actually test/import/run the artifact
2. Report test results FIRST
3. Then present the artifact

Example:
```
Testing import workflow:
1. Generated JSON structure ✓
2. Validating against schema... ✗ FAIL
   - Edge IDs don't match xy-edge__ format
   - Node IDs need alphanumeric format
3. Fixing issues... ✓
4. Re-testing import... ✓ PASS

[Now present JSON]
```

### Batch Processing with Pattern Variation

For tasks requiring variation across batch (e.g., PLP copy with varied S1 openers):

**After every 20 outputs:**
```
Pattern Variation Check:
- S1 opener distribution:
  - Outcome-first: 6/20 (30%)
  - Feature-first: 5/20 (25%)
  - Format-first: 4/20 (20%)
  - Spec-first: 3/20 (15%)
  - Problem-first: 2/20 (10%)
  
- S2 opener streaks:
  ✗ "Discover" used 3x consecutively (rows 12-14)
  ✗ "Shop" used 4x consecutively (rows 17-20)

Fixing streaks before continuing batch...
```

### Infrastructure vs Output Validation

**Priority order:**
1. Validate core output FIRST
2. Then worry about deployment/CI

**Example:**
If GitHub workflow fails on "Install dependencies":
- DON'T spend 800 lines debugging uv.lock and .gitignore
- DO verify the core agent/script produces correct output FIRST
- THEN fix infrastructure

## Iteration Loop Detection

If you find yourself making edit #3 to the same artifact without user feedback:

**STOP and present:**
```
Iteration Loop Detected:

What I'm trying to achieve:
- [Goal]

What's blocking completion:
- [Specific blocker]

Edits made so far:
1. [Edit 1 description]
2. [Edit 2 description]  
3. [Edit 3 description - current state]

What I need from you to proceed:
- [Specific decision or clarification needed]

Current state: [brief description or file path]
```

**Then WAIT.** Do not continue iteration #4 without human input.

## Output Format Examples

### Good Checkpoint (After batch of 5):
```
CHECKPOINT 1/4 (5/20 outputs completed):

Validation:
✓ Char count: 5/5 within 220-250 (range: 226-244)
✗ Lower end preference: 2/5 hit 225-235 target
  - URL 1: 244 chars (target: 225-235)
  - URL 3: 247 chars (target: 225-235)
  - URL 5: 242 chars (target: 225-235)
✓ S2 shorter than S1: 5/5
✓ TGG exactly once: 5/5
✓ No banned words: 5/5

Fixing 3 over-target pieces now...
[Revised versions]

Continue to next batch? (Y/N)
```

### Bad Checkpoint (Don't Do This):
```
Looking good so far! Most pieces are around 240-250 which is pretty close to target. Should I keep going?
```

**Why bad:**
- No specific constraint validation
- "Pretty close" ignores "lower end preferred" requirement
- Asking to continue before fixing violations

### Good Final Validation:
```
FINAL VALIDATION (20 outputs):

✓ Char count: 20/20 within 220-250 (range: 223-248)
✓ Lower end preference: 18/20 hit 225-235 (median: 232)
✓ S2 shorter than S1: 20/20
✓ TGG exactly once: 20/20  
✓ No banned words: 20/20
✓ S1 opener variation: No angle >30% of batch
✓ S2 opener variation: No consecutive 3x runs
✓ Australian English: 20/20

Status: READY ✓

[Present deliverable]
```

## Integration with Existing Skills

This verification protocol works WITH specialized skills like:
- `tgg-seo`: Provides content rules and SEO requirements, this skill enforces validation and compliance
- `docx`, `pptx`, `xlsx`: Provide file creation, this skill validates output quality

**Workflow:**
1. Load relevant domain skill (e.g., tgg-seo)
2. Extract constraints from that skill
3. Apply verification-gate-protocol to enforce those constraints
4. Deliver only when all gates pass

## Error Recovery

When you violate verification protocol (miss a checkpoint, present without validation, etc.):

1. Acknowledge directly: "I violated checkpoint protocol at batch 3"
2. State what you should have done: "Should have validated all 5 constraints before continuing"
3. Fix immediately: [Run proper validation now]
4. Don't apologize excessively - just correct and continue with proper protocol

## Summary Checklist

Before starting ANY complex task:
- [ ] Extract all success criteria as pass/fail conditions
- [ ] State checkpoint cadence explicitly
- [ ] Get user confirmation to proceed

During execution:
- [ ] Stop at each checkpoint
- [ ] Validate ALL constraints
- [ ] Fix violations before continuing
- [ ] Never ask "is this enough?" for quantified scope

Before final delivery:
- [ ] Run complete validation on ALL outputs
- [ ] Test executable deliverables
- [ ] Present validation summary with ✓/✗ per constraint
- [ ] Fix all ✗ before presenting artifact
- [ ] Never deliver "close enough"

If iteration loop detected (3+ edits):
- [ ] STOP immediately
- [ ] Present current state + blocker + needs
- [ ] WAIT for human input
