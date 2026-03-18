Poll GitHub Discussion #5 for new @claude messages, process them with the SEO agent team, and post replies back.

Discussion URL: https://github.com/simonmannheimer-tgg/Claude/discussions/5

## Steps

1. Run the polling script:
   ```bash
   bash scripts/github-poll.sh
   ```
   If output is `{"pending":[]}`, say "No pending tasks." and stop.

2. For each item in `pending`, extract `id`, `db_id`, `task`.

3. Determine what kind of task it is and run the right agent:
   - SEO copy / PLP / FAQs / metadata → use **seo-team-lead**
   - Keyword research / competitor analysis → use **seo-team-lead**
   - Code question → answer directly
   - General question → answer directly

   For seo-team-lead tasks:
   ```
   Use the seo-team-lead to: <task>
   Context: thegoodguys.com.au. Save outputs to seo/outputs/. Return a concise summary.
   ```

4. Format the reply. It MUST:
   - Lead with the key output or answer (not preamble)
   - Use markdown — headings, bullets, code blocks as appropriate
   - End with: `_— Claude Code_`
   - NOT contain `@claude` anywhere (prevents re-trigger)

5. Post the reply to the discussion:
   ```bash
   BODY="<formatted reply>" TASK_ID="<id from step 2>" bash scripts/github-post-comment.sh
   ```

6. Process all pending tasks before stopping.
