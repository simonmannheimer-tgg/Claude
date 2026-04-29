---
name: mhtml-reader
description: Read and extract content from MHTML files (saved web pages and AI conversations). Auto-triggers when any .mhtml file is uploaded. Detects whether the file is an AI conversation transcript (Claude, ChatGPT, Gemini, Copilot, Manus, SubAgents) or a web page snapshot (competitor analysis, TGG pages, analytics tools), then extracts content appropriately and asks what the user wants to do with it. Use this skill whenever you see an .mhtml file path in uploaded_files or when a user mentions an MHTML file.
---

# MHTML Reader

This skill handles MHTML (MIME HTML) files — single-file web page archives commonly saved from browsers. These files bundle HTML, CSS, JavaScript, and images into one `.mhtml` file.

## When This Skill Triggers

**Automatic triggers:**
- Any file with `.mhtml` extension appears in `uploaded_files`
- User references an MHTML file by name or path

**Manual triggers:**
- User says "read this MHTML"
- User asks about content from a saved web page or AI conversation

## File Type Detection

MHTML files fall into three categories based on their `Snapshot-Content-Location` header:

### 1. AI Conversation Transcripts
Conversations saved from AI chat interfaces for context handoff or continuation.

**Domains:**
- `claude.ai/chat/*` — Claude chat conversations
- `claude.ai/code/*` — Claude Code terminal sessions
- `chatgpt.com/c/*` — ChatGPT conversations
- `gemini.google.com/*` — Google Gemini conversations
- `m365.cloud.microsoft/chat` — Microsoft 365 Copilot
- `manus.im/*` — Manus conversations
- `subagents.app/*` — SubAgents conversations

**User intent:** Resume work, understand context, extract decisions/findings

### 2. Web Page Snapshots
Competitor analysis, market research, or TGG's own pages saved for reference.

**Common domains:**
- `thegoodguys.com.au` — TGG's own site (for copy audits, metadata checks)
- `jbhifi.com.au` — JB Hi-Fi competitor
- `ebgames.com.au` — EB Games competitor
- `officeworks.com.au` — Officeworks competitor
- Brand sites: `razer.com`, `logitech.com`, `turtlebeach.com`, etc.
- Other retailers: `centrecom.com.au`, `gamesmen.com.au`, etc.

**User intent:** Analyze competitor copy, extract PLP intros, audit metadata, compare page structure

### 3. Analytics/Tool Snapshots
Dashboards and reports saved for offline reference.

**Common domains:**
- `semrush.com` — Position tracking, keyword data
- Other analytics platforms

**User intent:** Extract data tables, review historical metrics, analyze trends

## Extraction Workflow

### Step 1: Parse the MHTML File

Use Python's `email` library to properly parse the MHTML structure:

```python
import email
from email import policy
from bs4 import BeautifulSoup
import re

def parse_mhtml(filepath):
    """Parse MHTML and extract metadata + clean text content."""
    with open(filepath, 'rb') as f:
        msg = email.message_from_binary_file(f, policy=policy.default)
    
    # Extract metadata from headers
    metadata = {
        'subject': msg.get('Subject', 'Unknown'),
        'url': msg.get('Snapshot-Content-Location', 'Unknown'),
        'date': msg.get('Date', 'Unknown')
    }
    
    # Find the main HTML part
    html_content = None
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            html_content = part.get_content()
            break
    
    if not html_content:
        return metadata, "No HTML content found"
    
    # Parse HTML and extract text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements
    for script in soup(['script', 'style', 'noscript']):
        script.decompose()
    
    # Get text content
    text = soup.get_text(separator='\n', strip=True)
    
    # Clean up excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    
    return metadata, text
```

**Critical:** Always use proper MHTML parsing. Do NOT use `strings`, `grep`, or naive text extraction — these methods mangle quoted-printable encoding and miss content.

### Step 2: Detect File Type

Check the `url` field in metadata:

```python
def detect_mhtml_type(url):
    """Detect whether MHTML is AI conversation, web page, or analytics."""
    ai_patterns = [
        'claude.ai/chat',
        'claude.ai/code',
        'chatgpt.com/c',
        'gemini.google.com',
        'm365.cloud.microsoft/chat',
        'manus.im',
        'subagents.app'
    ]
    
    analytics_patterns = [
        'semrush.com'
    ]
    
    url_lower = url.lower()
    
    for pattern in ai_patterns:
        if pattern in url_lower:
            return 'ai_conversation'
    
    for pattern in analytics_patterns:
        if pattern in url_lower:
            return 'analytics'
    
    return 'web_page'
```

### Step 3: Type-Specific Processing

#### For AI Conversations

Extract the conversation structure:

```python
def extract_ai_conversation(text, url):
    """Extract conversation turns from AI chat transcript."""
    
    # Identify platform
    platform = 'Unknown'
    if 'claude.ai' in url:
        platform = 'Claude' if '/chat/' in url else 'Claude Code'
    elif 'chatgpt.com' in url:
        platform = 'ChatGPT'
    elif 'gemini.google.com' in url:
        platform = 'Google Gemini'
    elif 'm365.cloud.microsoft' in url:
        platform = 'Microsoft Copilot'
    elif 'manus.im' in url:
        platform = 'Manus'
    elif 'subagents.app' in url:
        platform = 'SubAgents'
    
    # Extract conversation content
    # Different platforms have different HTML structures
    # Look for common patterns: message blocks, user/assistant labels
    
    # For now, return cleaned text
    # Platform-specific parsing can be added as needed
    
    return {
        'platform': platform,
        'content': text
    }
```

**Response format for AI conversations:**

1. State the platform and conversation title
2. Summarize the topic/task being worked on
3. Extract key findings, assumptions, decisions, or artifacts produced
4. Identify next steps or where the conversation left off
5. Ask what the user wants to do

**Example response:**

> This is a Claude conversation titled "Click Frenzy FAQ alignment" from March 25, 2026.
> 
> **Topic:** Writing FAQ copy for The Good Guys Click Frenzy 2025 events
> 
> **Key outputs:**
> - FAQ content covering four Click Frenzy 2025 events (PayPal, May, November, Travel)
> - Questions addressed: event timing, duration, online vs. in-store availability, deal types
> 
> **Where it left off:**
> The conversation completed FAQ drafts but didn't finalize whether this content was approved or deployed.
> 
> What would you like to do with this?

#### For Web Pages

Extract structured page elements:

```python
def extract_web_page_info(text, url, soup):
    """Extract key info from a web page snapshot."""
    
    # Get title
    title = soup.find('title')
    title_text = title.get_text(strip=True) if title else 'No title'
    
    # Get meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc.get('content', '') if meta_desc else ''
    
    # Get H1
    h1 = soup.find('h1')
    h1_text = h1.get_text(strip=True) if h1 else 'No H1'
    
    # Identify domain
    from urllib.parse import urlparse
    domain = urlparse(url).netloc
    
    return {
        'domain': domain,
        'url': url,
        'title': title_text,
        'description': description,
        'h1': h1_text
    }
```

**Response format for web pages:**

1. State the domain and page type (PLP, product page, landing page, etc.)
2. Show title, meta description, and H1
3. Briefly describe what the page is
4. Ask what the user wants to analyze

**Example response:**

> This is a JB Hi-Fi category page: **Gaming Headsets - Buy Gaming Equipment & More**
> 
> **URL:** https://www.jbhifi.com.au/collections/games-consoles/gaming-headsets  
> **Meta description:** [extract if present]  
> **H1:** Gaming Headsets
> 
> What would you like me to analyze? (PLP intro copy, product count, metadata structure, internal linking, etc.)

#### For Analytics Pages

Similar to web pages, but emphasize data extraction:

**Response format:**

1. State the tool/platform and report type
2. Identify visible data (tables, charts, metrics)
3. Ask what the user wants to extract or analyze

**Example response:**

> This is a Semrush Position Tracking report for thegoodguys.com.au
> 
> **Date range:** November 5, 2025 to March 17, 2026  
> **Report type:** All Tracked Keywords Overview
> 
> The page contains keyword ranking data in table format. What would you like me to extract or analyze?

## Edge Cases

### Missing or Malformed Headers

If `Snapshot-Content-Location` is missing or empty:
- Fall back to analyzing the `Subject` line
- If both are missing, parse the HTML and make a best guess based on content

### Empty or Failed Extractions

If the MHTML file has no extractable content:
- Report this clearly: "This MHTML file appears to be empty or corrupted."
- Offer to try raw text extraction as a fallback

### Large Files

MHTML files can be 10k–90k lines. If the extracted text is excessively long:
- Summarize rather than dumping full content
- Offer to search for specific sections if the user needs details

## Output Guidelines

**Always:**
- State what type of file this is (AI conversation, web page, analytics)
- Provide enough context for the user to know what they're looking at
- Ask what they want to do with it

**Never:**
- Dump raw HTML or massive text blocks
- Guess at content you can't confidently extract
- Skip the parsing step and use naive text extraction

## Dependencies

**Python libraries:**
- `email` (stdlib) — MHTML parsing
- `BeautifulSoup4` (`bs4`) — HTML parsing
- `re` (stdlib) — Text cleaning

Install if missing:
```bash
pip install beautifulsoup4 --break-system-packages
```

## Example Full Workflow

```python
#!/usr/bin/env python3
"""
MHTML Reader - Extract content from saved web pages and AI conversations
"""

import email
from email import policy
from bs4 import BeautifulSoup
import re
import sys
from urllib.parse import urlparse

def parse_mhtml(filepath):
    """Parse MHTML and return metadata + soup object."""
    with open(filepath, 'rb') as f:
        msg = email.message_from_binary_file(f, policy=policy.default)
    
    metadata = {
        'subject': msg.get('Subject', 'Unknown'),
        'url': msg.get('Snapshot-Content-Location', 'Unknown'),
        'date': msg.get('Date', 'Unknown')
    }
    
    html_content = None
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            html_content = part.get_content()
            break
    
    if not html_content:
        return metadata, None, "No HTML content found"
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove scripts and styles
    for script in soup(['script', 'style', 'noscript']):
        script.decompose()
    
    text = soup.get_text(separator='\n', strip=True)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    
    return metadata, soup, text

def detect_type(url):
    """Detect file type from URL."""
    ai_patterns = [
        'claude.ai/chat', 'claude.ai/code', 'chatgpt.com/c',
        'gemini.google.com', 'm365.cloud.microsoft/chat',
        'manus.im', 'subagents.app'
    ]
    
    analytics_patterns = ['semrush.com']
    
    url_lower = url.lower()
    
    for pattern in ai_patterns:
        if pattern in url_lower:
            return 'ai_conversation'
    
    for pattern in analytics_patterns:
        if pattern in url_lower:
            return 'analytics'
    
    return 'web_page'

def process_file(filepath):
    """Main processing function."""
    metadata, soup, text = parse_mhtml(filepath)
    
    if soup is None:
        return {
            'status': 'error',
            'message': text  # error message
        }
    
    file_type = detect_type(metadata['url'])
    
    result = {
        'type': file_type,
        'metadata': metadata,
        'text': text
    }
    
    if file_type == 'web_page' and soup:
        # Extract web page specifics
        title = soup.find('title')
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        h1 = soup.find('h1')
        
        result['web_info'] = {
            'domain': urlparse(metadata['url']).netloc,
            'title': title.get_text(strip=True) if title else 'No title',
            'description': meta_desc.get('content', '') if meta_desc else '',
            'h1': h1.get_text(strip=True) if h1 else 'No H1'
        }
    
    return result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python mhtml_reader.py <path-to-mhtml-file>")
        sys.exit(1)
    
    result = process_file(sys.argv[1])
    
    # Pretty print result
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))
```

Run this script on any MHTML file, then format the response according to the type-specific guidelines above.
