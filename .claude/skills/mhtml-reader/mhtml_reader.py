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
        'text': text[:2000] + '...' if len(text) > 2000 else text  # Truncate for display
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
