---
title: Terminal script for HTTP status code checking (full)
parent: Chat/Light/2026-04-21-terminal-script-for-http-status-code-checking-2c95d5
uuid: 2c95d529-6513-40f4-a3f8-3263ddc69c3f
---

#chat/full #project/main #status/completed

# Terminal script for HTTP status code checking — Full Transcript

→ Light view: [[Chat/Light/2026-04-21-terminal-script-for-http-status-code-checking-2c95d5]]
→ Medium view: [[Chat/Medium/2026-04-21-terminal-script-for-http-status-code-checking-2c95d5]]

**Messages:** 6 | **Date:** 2026-04-21

---

### 1. **Human** — 2026-04-20T23:42

can you write a terminal run script to http statuscode check these? ill run in vscod
can you write a terminal run script to http statuscode check these? ill run in vscod

---

### 2. **Claude** — 2026-04-20T23:43

The user wants me to write a terminal script that can HTTP status code check a list of URLs. They've uploaded a CSV file with URLs, and they want to run it in VS Code's terminal.

First, I need to:
1. Read the CSV to understand its structure and extract the URLs
2. Create a script that checks HTTP status codes for each URL
3. Make it executable from terminal/VS Code

Let me read the file first to see what format it's in.
```
This block is not supported on your current device yet.
```

Now let me read the CSV file to see its structure.
```
This block is not supported on your current device yet.
```

Good. The CSV has the structure:
- Column 1: "Redirect from" (the source URL)
- Column 2: "Redirect to" (the target URL)
- Column 3: "From Status"
- Column 4: "To Status"

Some rows have "Loading..." which means the status codes haven't been fetched yet.

The user wants a script to check HTTP status codes. They want to run it in VS Code's terminal. I should write a script that:
1. Reads the CSV
2. Extracts URLs
3. Makes HTTP requests to each
4. Reports status codes
5. Probably outputs to a results file or console

They want it to run in VS Code, so I'll make a simple bash or Node.js script. Bash with `curl` would be the simplest and most portable. Let me create a bash script that:
- Reads the "Redirect from" column (column 1)
- Makes HTTP requests without following redirects (to get the actual status)
- Outputs results with status codes
- Maybe also checks the "Redirect to" column

Actually, let me create a more comprehensive script that checks both the source and target URLs, and outputs the results in a clean format. I'll use curl with `-w` to get status codes and `-L` optionally to follow redirects if needed.

Let me create a bash script that's practical and easy to run.
```
This block is not supported on your current device yet.
```

Good, now let me make the script executable and also create a Node.js alternative since it might be faster and easier to run. Actually, let me provide both options but focus on the bash one first since they said they want to run it in VS Code terminal.

Let me also provide a simpler alternative that's less resource-intensive - checking just the "Redirect from" column (source URLs) first.
```
This block is not supported on your current device yet.
```

Good. Now let me copy the script to the outputs folder so the user can download it, and also create a Node.js version as a faster alternative. Let me also provide clear instructions on how to use it.
```
This block is not supported on your current device yet.
```

Now let me create a faster Node.js version that uses native fetch or axios for parallel requests.
```
This block is not supported on your current device yet.
```

The Node.js script has a dependency on csv-parse which may not be installed. Let me create a simpler version that doesn't require dependencies. Actually, let me just provide the bash version and a simpler Node.js version that doesn't need dependencies.
```
This block is not supported on your current device yet.
```

Now let me copy this to outputs and create a simple instructions file.
```
This block is not supported on your current device yet.
```

Now let me create a README with instructions on how to use both scripts.
```
This block is not supported on your current device yet.
```

Now let me copy the README to outputs as well.
```
This block is not supported on your current device yet.
```

Perfect. Now let me present the files to the user.
```
This block is not supported on your current device yet.
```

Good. Now I should give Simon clear, concise instructions on how to use these scripts. Keep it brief since he has clear preferences about not needing excessive explanation.Two scripts ready. **Node.js version is faster** (5 parallel requests), bash is simpler.

**Quick start in VS Code terminal:**

```bash
node check-status-codes.mjs your-file.csv
```

Both extract unique URLs from both CSV columns, check status codes, output results to `status_check_results.csv` with a summary. Bash version is sequential. Node version includes response times and follows redirects automatically.
Two scripts ready. **Node.js version is faster** (5 parallel requests), bash is simpler.

**Quick start in VS Code terminal:**

```bash
node check-status-codes.mjs your-file.csv
```

Both extract unique URLs from both CSV columns, check status codes, output results to `status_check_results.csv` with a summary. Bash version is sequential. Node version includes response times and follows redirects automatically.

---

### 3. **Human** — 2026-04-20T23:56

python that runs on copied file path of the csv, take col a and b, check them, output a's status into c and bs into d
python that runs on copied file path of the csv, take col a and b, check them, output a's status into c and bs into d

---

### 4. **Claude** — 2026-04-20T23:57

The user wants a Python script that:
1. Takes a CSV file path (copied/pasted)
2. Reads columns A and B (the "Redirect from" and "Redirect to" URLs)
3. Checks HTTP status for column A URLs, puts result in column C
4. Checks HTTP status for column B URLs, puts result in column D
5. Likely outputs to the same file or a new file

This is simpler than what I made before. They want it to modify the existing CSV structure with status codes in place. Let me create a Python script that uses requests library and pandas to do this efficiently.

Actually, I should use urllib to avoid needing requests library. Let me write a clean Python script that can be run from VS Code terminal with just the file path as argument.

Python approach:
1. Read CSV
2. Loop through rows
3. Check each URL in col A and B
4. Add status codes to col C and D
5. Save output

Let me make it simple and practical.
```
This block is not supported on your current device yet.
```

Good. Now let me copy it to outputs and provide clear instructions.
```
This block is not supported on your current device yet.
```

Now let me present just the Python script with a quick usage example.```bash
python check-status.py /path/to/your/file.csv
```

Reads your CSV. Checks column A URLs, writes status codes to column C. Checks column B URLs, writes to column D. Skips "Loading..." rows. Outputs to `file_with_status.csv`. Uses only Python standard library (urllib), no dependencies.

In VS Code: paste the file path after the script name, or drag the file onto terminal.
```bash
python check-status.py /path/to/your/file.csv
```

Reads your CSV. Checks column A URLs, writes status codes to column C. Checks column B URLs, writes to column D. Skips "Loading..." rows. Outputs to `file_with_status.csv`. Uses only Python standard library (urllib), no dependencies.

In VS Code: paste the file path after the script name, or drag the file onto terminal.

---

### 5. **Human** — 2026-04-21T00:08

PS C:\Users\simonma> & "C:/Program Files/Python312/python.exe" "c:/Users/simonma/OneDrive - JB HI-FI Group Pty Ltd/Desktop/Other/VSCode (new)/check-status.py"
Usage: python check-status.py <csv_file_path>
PS C:\Users\simonma> & "C:/Program Files/Python312/python.exe" "c:/Users/simonma/OneDrive - JB HI-FI Group Pty Ltd/Desktop/Other/VSCode (new)/check-status.py"
Usage: python check-status.py <csv_file_path>
PS C:\Users\simonma> python check-status.py "C:\Users\simonma\Downloads\404s _ Ongoing Fixes - 21 APRIL SHOPIFY REDIR EXPORT.csv"
C:\Program Files\Python312\python.exe: can't open file 'C:\\Users\\simonma\\check-status.py': [Errno 2] No such file or directory
PS C:\Users\simonma>
PS C:\Users\simonma> & "C:/Program Files/Python312/python.exe" "c:/Users/simonma/OneDrive - JB HI-FI Group Pty Ltd/Desktop/Other/VSCode (new)/check-status.py"
Usage: python check-status.py <csv_file_path>
PS C:\Users\simonma> & "C:/Program Files/Python312/python.exe" "c:/Users/simonma/OneDrive - JB HI-FI Group Pty Ltd/Desktop/Other/VSCode (new)/check-status.py"
Usage: python check-status.py <csv_file_path>
PS C:\Users\simonma> python check-status.py "C:\Users\simonma\Downloads\404s _ Ongoing Fixes - 21 APRIL SHOPIFY REDIR EXPORT.csv"
C:\Program Files\Python312\python.exe: can't open file 'C:\\Users\\simonma\\check-status.py': [Errno 2] No such file or directory
PS C:\Users\simonma>

---

### 6. **Claude** — 2026-04-21T00:09

The user is having path issues. They're in the Downloads folder but the script is in a different location. Let me give them a simpler approach:

1. Copy the script to the Downloads folder where the CSV is
2. Then run it from there

Or better yet, I can modify the script to be more flexible about where it's run from. Actually, the simplest solution is to just tell them to put the script in the same folder as the CSV and run it with a simple filename.

Let me create a version that's easier to use - one that asks for the file path if not provided, or copies to Downloads.Copy the script to your Downloads folder first, then run from there:

```bash
cd Downloads
python check-status.py "404s _ Ongoing Fixes - 21 APRIL SHOPIFY REDIR EXPORT.csv"
```

Or I'll make a simpler version that just asks for the path:
```
This block is not supported on your current device yet.
```

I need to provide the path. Let me view the file first and then replace the section.
```
This block is not supported on your current device yet.
```

Now I can replace the main function to make it prompt for input if no argument provided.
```
This block is not supported on your current device yet.
```

Perfect. Now the script will prompt for the file path if none is provided. Let me present the updated script and give clear instructions.
```
This block is not supported on your current device yet.
```

Good. Now I need to give Simon clear instructions on how to use the updated script. The script now prompts for input if no argument is provided.Updated. Now it prompts for the path if you don't provide it. Run from anywhere:

```bash
python check-status.py
```

Then paste your file path when prompted. It'll handle the path parsing automatically and output to `file_with_status.csv` in the same folder as your CSV.
Copy the script to your Downloads folder first, then run from there:

```bash
cd Downloads
python check-status.py "404s _ Ongoing Fixes - 21 APRIL SHOPIFY REDIR EXPORT.csv"
```

Or I'll make a simpler version that just asks for the path:
Updated. Now it prompts for the path if you don't provide it. Run from anywhere:

```bash
python check-status.py
```

Then paste your file path when prompted. It'll handle the path parsing automatically and output to `file_with_status.csv` in the same folder as your CSV.
