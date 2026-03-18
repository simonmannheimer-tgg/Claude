Poll GitHub for new @claude task requests, run them through the SEO agent team, and post results back as issue comments.

## Steps

1. Run the polling script to find pending tasks:
   ```bash
   bash scripts/github-poll.sh
   ```
   If the output is `{"pending":[]}`, say "No pending @claude tasks found." and stop.

   If GITHUB_TOKEN is not set, say:
   > GITHUB_TOKEN is not set. Run: `export GITHUB_TOKEN=<your-pat>`
   > Get a free PAT at: GitHub → Settings → Developer settings → Personal access tokens → Fine-grained → New token
   > Required permissions: Issues (Read/Write), Contents (Read)
   and stop.

2. For each item in `pending`, extract `id`, `number`, `title`, `task`.
   Strip the `@claude` prefix from the task text to get the clean instruction.

3. For each task, use the **seo-team-lead** agent:
   ```
   Use the seo-team-lead to: <clean task instruction>
   
   Context: This is for thegoodguys.com.au. GitHub issue #<number>: "<title>".
   Save any output files to seo/outputs/. Return a concise summary of what was done.
   ```

4. Format the result as a GitHub comment. The comment MUST:
   - Start with a one-line summary of what was done
   - Include the key output (copy, data, analysis) inline or reference the file path
   - End with: `_Processed by Claude Code — [view outputs in seo/outputs/]_`
   - NOT contain the text `@claude` anywhere (would re-trigger the loop)

5. Post the comment:
   ```bash
   bash scripts/github-post-comment.sh <number> "<formatted result>" "<task id>"
   ```

6. If multiple tasks are pending, process them one at a time in order.

7. After all tasks are done, say how many were processed and which issues they were on.
