---
title: HTTP status code returning as array (medium)
parent: Chat/Light/2026-04-27-http-status-code-returning-as-array-5c3689
uuid: 5c368922-c9b1-4c33-8d42-b197ad8c9a52
---

#chat/medium #project/main #status/active

# HTTP status code returning as array — Key User Messages

→ Light view: [[Chat/Light/2026-04-27-http-status-code-returning-as-array-5c3689]]
→ Full transcript: [[Chat/Full/2026-04-27-http-status-code-returning-as-array-5c3689]]

**Total user messages:** 6

---

### Message 1 — 2026-04-27T04:00

=IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I19)),I19,J19)),"")

why ouputting as: [200]


```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string') return '';
  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  let result = cache.get(url_trimmed);

  if (!result) {
    const options = { muteHttpExceptions: true, followRedirects: false };
    const response = UrlFetchApp.fetch(url_trimmed, options);
    const responseCode = response.getResponseCode();
    cache.put(url_trimmed, responseCode, 21600);
    result = responseCode;
  }

  return result;
}

function getRedirects(url) {
  if (!url || typeof url !== 'string') return '';
  const urlKey = url.trim() + "k";
  const cache = CacheService.getScriptCache();
  let result = cache.get(urlKey);

  if (!result) {
    const params = { followRedirects: false, muteHttpExceptions: true };
    const res = UrlFetchApp.fetch(url, params);
    const finalURL = res.getHeaders()['Location'];
    cache.put(urlKey, finalURL, 21600);
    result = finalURL;
  }

  return result;
}

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const col = 10; // adjust to your getStatusCode formula column
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const n = Number(v);
    return [(!isNa

[truncated — see full transcript]

### Message 2 — 2026-04-27T04:03

change the full code
change the full code

### Message 3 — 2026-04-27T04:05

ErrorResult was not a number.
ErrorResult was not a number.

### Message 4 — 2026-04-27T04:07

its just empty now
its just empty now

### Message 5 — 2026-04-27T04:10

back now but with [2--]
back now but with [2--]

### Message 6 — 2026-04-27T04:10

[200]
[200]
