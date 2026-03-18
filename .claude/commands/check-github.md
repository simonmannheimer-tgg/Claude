Poll GitHub Issues for new @claude messages, process them with the SEO agent team, write outputs to disk, and post replies back.

## Steps

1. Run the polling script:
   ```bash
   bash scripts/github-poll.sh
   ```
   If output is `{"pending":[]}`, say "No pending tasks." and stop.

2. For each item in `pending`, extract `id`, `number`, `task`.

3. Determine what kind of task it is and run the right agent:
   - SEO copy / PLP / FAQs / metadata → use **seo-team-lead**
   - Keyword research / competitor analysis → use **seo-team-lead**
   - Code question → answer directly
   - General question → answer directly

   For seo-team-lead tasks:
   ```
   Use the seo-team-lead to: <task>
   Context: thegoodguys.com.au. Save all outputs to seo/outputs/. Commit and push when done. Return a concise summary.
   ```

4. After all agents complete, commit any new output files:
   ```bash
   git add seo/outputs/
   git diff --cached --quiet || git commit -m "feat(outputs): process @claude tasks from GitHub Issues"
   git push -u origin HEAD
   ```

5. Format the reply. It MUST:
   - Lead with the key output or answer (not preamble)
   - Use markdown — headings, bullets, code blocks as appropriate
   - Include the file path(s) written (e.g. `seo/outputs/plp-robot-vacuums-2026-03-18.md`)
   - End with: `_— Claude Code_`
   - NOT contain `@claude` anywhere (prevents re-trigger)

6. Post the reply to the issue:
   ```bash
   BODY="<formatted reply>" TASK_ID="<id from step 2>" ISSUE_NUMBER="<number>" bash scripts/github-post-comment.sh
   ```

7. Process all pending tasks before stopping.
