---
title: HTTP status code tracker with caching (full)
parent: Chat/Light/2026-04-27-http-status-code-tracker-with-caching-419a95
uuid: 419a955f-473c-49f3-bf42-c28acff585ab
---

#chat/full #project/main #status/active

# HTTP status code tracker with caching — Full Transcript

→ Light view: [[Chat/Light/2026-04-27-http-status-code-tracker-with-caching-419a95]]
→ Medium view: [[Chat/Medium/2026-04-27-http-status-code-tracker-with-caching-419a95]]

**Messages:** 38 | **Date:** 2026-04-27

---

### 1. **Human** — 2026-04-27T03:31

can i get this:



```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string') {
    return ['No URL provided'];
  }

  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  let result = cache.get(url_trimmed);

  if (!result) {
    const options = {
      'muteHttpExceptions': true,
      'followRedirects': false
    };

    let currentURL = url_trimmed;
    let chain = [];
    let maxRedirects = 10;

    for (let i = 0; i < maxRedirects; i++) {
      const response = UrlFetchApp.fetch(currentURL, options);
      const status = response.getResponseCode();
      chain.push(status);

      if ([301, 302, 303, 307, 308].includes(status)) {
        let nextLocation = response.getHeaders()['Location'];
        if (!nextLocation) break;

        // ✅ If relative, prepend base domain
        if (nextLocation.startsWith('/')) {
          try {
            const base = currentURL.match(/^(https?:\/\/[^\/]+)/)[1];
            nextLocation = base + nextLocation;
          } catch (e) {
            break; // If regex fails, stop
          }
        }

        // ✅ If protocol-relative (starts with //), add https:
        if (nextLocation.startsWith('//')) {
          nextLocation = 'https:' + nextLocation;
        }

        chain.push(nextLocation);
        currentURL = nextLocation;
      } else {
        break;
      }
    }

    result = JSON.stringify(chain);
    cache.put(url_trimmed, result, 21600);
  }

  return JSON.parse(result);
}



```

with an additional fix that runs every x time (hour idk) and if it says 200, 301, 404 etc. it saves it as value?
can i get this:



```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string') {
    return ['No URL provided'];
  }

  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  let result = cache.get(url_trimmed);

  if (!result) {
    const options = {
      'muteHttpExceptions': true,
      'followRedirects': false
    };

    let currentURL = url_trimmed;
    let chain = [];
    let maxRedirects = 10;

    for (let i = 0; i < maxRedirects; i++) {
      const response = UrlFetchApp.fetch(currentURL, options);
      const status = response.getResponseCode();
      chain.push(status);

      if ([301, 302, 303, 307, 308].includes(status)) {
        let nextLocation = response.getHeaders()['Location'];
        if (!nextLocation) break;

        // ✅ If relative, prepend base domain
        if (nextLocation.startsWith('/')) {
          try {
            const base = currentURL.match(/^(https?:\/\/[^\/]+)/)[1];
            nextLocation = base + nextLocation;
          } catch (e) {
            break; // If regex fails, stop
          }
        }

        // ✅ If protocol-relative (starts with //), add https:
        if (nextLocation.startsWith('//')) {
          nextLocation = 'https:' + nextLocation;
        }

        chain.push(nextLocation);
        currentURL = nextLocation;
      } else {
        break;
      }
    }

    result = JSON.stringify(chain);
    cache.put(url_trimmed, result, 21600);
  }

  return JSON.parse(result);
}



```

with an additional fix that runs every x time (hour idk) and if it says 200, 301, 404 etc. it saves it as value?

---

### 2. **Claude** — 2026-04-27T03:31

The user wants a time-driven trigger in Google Apps Script that runs `getStatusCode` on a list of URLs periodically and saves the results to a spreadsheet.

Let me think about what they actually need:
1. The existing `getStatusCode` function stays as-is
2. A time-based trigger (e.g., hourly) that runs a function
3. That function reads URLs from somewhere (a sheet column presumably)
4. Runs `getStatusCode` on each
5. Writes the status code result back to the sheet

I'll assume URLs are in column A and results go in column B (or adjacent). I should ask about the sheet structure, but it's a simple enough assumption to state and proceed.


I'll need to create a function that pulls URLs from the sheet, loops through them with `getStatusCode`, and writes back just the final status code as a plain value. Then I'll set up an hourly time-based trigger to run this automatically.Assumption: URLs are in column A of the active sheet, results write to column B. Change column indices if different.

```javascript
// ─── existing function, unchanged ───────────────────────────────────────────

function getStatusCode(url) {
  if (!url || typeof url !== 'string') return ['No URL provided'];

  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  let result = cache.get(url_trimmed);

  if (!result) {
    const options = { muteHttpExceptions: true, followRedirects: false };
    let currentURL = url_trimmed;
    let chain = [];

    for (let i = 0; i < 10; i++) {
      const response = UrlFetchApp.fetch(currentURL, options);
      const status = response.getResponseCode();
      chain.push(status);

      if ([301, 302, 303, 307, 308].includes(status)) {
        let next = response.getHeaders()['Location'];
        if (!next) break;
        if (next.startsWith('/')) {
          try { next = currentURL.match(/^(https?:\/\/[^\/]+)/)[1] + next; }
          catch (e) { break; }
        }
        if (next.startsWith('//')) next = 'https:' + next;
        chain.push(next);
        currentURL = next;
      } else {
        break;
      }
    }

    result = JSON.stringify(chain);
    cache.put(url_trimmed, result, 21600);
  }

  return JSON.parse(result);
}

// ─── batch checker ───────────────────────────────────────────────────────────

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return; // nothing to process

  const urls = sheet.getRange(2, 1, lastRow - 1, 1).getValues(); // col A, skip header
  const results = [];

  for (const [url] of urls) {
    if (!url) {
      results.push(['']);
      continue;
    }
    try {
      const chain = getStatusCode(url);
      // Final status is the last numeric entry in the chain
      const finalStatus = [...chain].reverse().find(v => typeof v === 'number') ?? '';
      results.push([finalStatus]);
    } catch (e) {
      results.push(['ERROR']);
    }
  }

  // Write as plain values to col B
  sheet.getRange(2, 2, results.length, 1).setValues(results);
}

// ─── trigger setup (run once manually) ───────────────────────────────────────

function createHourlyTrigger() {
  // Delete any existing triggers for runStatusCheck to avoid duplicates
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'runStatusCheck')
    .forEach(t => ScriptApp.deleteTrigger(t));

  ScriptApp.newTrigger('runStatusCheck')
    .timeBased()
    .everyHours(1)
    .create();
}
```

**Setup:** run `createHourlyTrigger()` once manually from the Apps Script editor. After that, `runStatusCheck` fires every hour, reads all URLs in column A (row 2 onward), and writes the final resolved status code as a plain integer to column B. No formulas, just values.

To change the interval, swap `.everyHours(1)` for `.everyHours(6)`, `.everyMinutes(30)`, etc.
 
Assumption: URLs are in column A of the active sheet, results write to column B. Change column indices if different.

```javascript
// ─── existing function, unchanged ───────────────────────────────────────────

function getStatusCode(url) {
  if (!url || typeof url !== 'string') return ['No URL provided'];

  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  let result = cache.get(url_trimmed);

  if (!result) {
    const options = { muteHttpExceptions: true, followRedirects: false };
    let currentURL = url_trimmed;
    let chain = [];

    for (let i = 0; i < 10; i++) {
      const response = UrlFetchApp.fetch(currentURL, options);
      const status = response.getResponseCode();
      chain.push(status);

      if ([301, 302, 303, 307, 308].includes(status)) {
        let next = response.getHeaders()['Location'];
        if (!next) break;
        if (next.startsWith('/')) {
          try { next = currentURL.match(/^(https?:\/\/[^\/]+)/)[1] + next; }
          catch (e) { break; }
        }
        if (next.startsWith('//')) next = 'https:' + next;
        chain.push(next);
        currentURL = next;
      } else {
        break;
      }
    }

    result = JSON.stringify(chain);
    cache.put(url_trimmed, result, 21600);
  }

  return JSON.parse(result);
}

// ─── batch checker ───────────────────────────────────────────────────────────

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return; // nothing to process

  const urls = sheet.getRange(2, 1, lastRow - 1, 1).getValues(); // col A, skip header
  const results = [];

  for (const [url] of urls) {
    if (!url) {
      results.push(['']);
      continue;
    }
    try {
      const chain = getStatusCode(url);
      // Final status is the last numeric entry in the chain
      const finalStatus = [...chain].reverse().find(v => typeof v === 'number') ?? '';
      results.push([finalStatus]);
    } catch (e) {
      results.push(['ERROR']);
    }
  }

  // Write as plain values to col B
  sheet.getRange(2, 2, results.length, 1).setValues(results);
}

// ─── trigger setup (run once manually) ───────────────────────────────────────

function createHourlyTrigger() {
  // Delete any existing triggers for runStatusCheck to avoid duplicates
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'runStatusCheck')
    .forEach(t => ScriptApp.deleteTrigger(t));

  ScriptApp.newTrigger('runStatusCheck')
    .timeBased()
    .everyHours(1)
    .create();
}
```

**Setup:** run `createHourlyTrigger()` once manually from the Apps Script editor. After that, `runStatusCheck` fires every hour, reads all URLs in column A (row 2 onward), and writes the final resolved status code as a plain integer to column B. No formulas, just values.

To change the interval, swap `.everyHours(1)` for `.everyHours(6)`, `.everyMinutes(30)`, etc.

---

### 3. **Human** — 2026-04-27T03:40

can i apply the same to this


```javascript
function getStatusCode(url) {
    const url_trimmed = url.trim();

    let cache = CacheService.getScriptCache();
    let result = cache.get(url_trimmed);


    if (!result) {

        const options = {
            'muteHttpExceptions': true,
            'followRedirects': false
        };
        const response = UrlFetchApp.fetch(url_trimmed, options);
        const responseCode = response.getResponseCode();


        cache.put(url_trimmed, responseCode, 21600);
        result = responseCode;
    }

    return result;
}

function getRedirects(url) {
    
    const urlKey = url.trim()+"k";
    let cache = CacheService.getScriptCache();
    let result = cache.get(urlKey);


    if (!result) {
        const params = {
            'followRedirects': false,
            'muteHttpExceptions': true
        };
        const res = UrlFetchApp.fetch(url, params);
        const finalURL = res.getHeaders()['Location'];

        cache.put(urlKey, finalURL, 21600);
        
        result = finalURL;
    }

    return result;

}
```
can i apply the same to this


```javascript
function getStatusCode(url) {
    const url_trimmed = url.trim();

    let cache = CacheService.getScriptCache();
    let result = cache.get(url_trimmed);


    if (!result) {

        const options = {
            'muteHttpExceptions': true,
            'followRedirects': false
        };
        const response = UrlFetchApp.fetch(url_trimmed, options);
        const responseCode = response.getResponseCode();


        cache.put(url_trimmed, responseCode, 21600);
        result = responseCode;
    }

    return result;
}

function getRedirects(url) {
    
    const urlKey = url.trim()+"k";
    let cache = CacheService.getScriptCache();
    let result = cache.get(urlKey);


    if (!result) {
        const params = {
            'followRedirects': false,
            'muteHttpExceptions': true
        };
        const res = UrlFetchApp.fetch(url, params);
        const finalURL = res.getHeaders()['Location'];

        cache.put(urlKey, finalURL, 21600);
        
        result = finalURL;
    }

    return result;

}
```

---

### 4. **Claude** — 2026-04-27T03:40

Same pattern: batch runner + hourly trigger. This script has two functions: `getStatusCode` (simpler, no chain) and `getRedirects` (returns the Location header). I need to decide on column layout. I'll assume col A = URLs, col B = status code, col C = redirect destination. I'll state that assumption.Assumption: col A = URLs, col B = status codes, col C = redirect destinations. Adjust indices as needed.

```javascript
// ─── existing functions, unchanged ───────────────────────────────────────────

function getStatusCode(url) {
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

// ─── batch checker ───────────────────────────────────────────────────────────

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const urls = sheet.getRange(2, 1, lastRow - 1, 1).getValues();
  const statusResults = [];
  const redirectResults = [];

  for (const [url] of urls) {
    if (!url) {
      statusResults.push(['']);
      redirectResults.push(['']);
      continue;
    }
    try {
      statusResults.push([getStatusCode(url)]);
    } catch (e) {
      statusResults.push(['ERROR']);
    }
    try {
      redirectResults.push([getRedirects(url) ?? '']);
    } catch (e) {
      redirectResults.push(['ERROR']);
    }
  }

  sheet.getRange(2, 2, statusResults.length, 1).setValues(statusResults);   // col B
  sheet.getRange(2, 3, redirectResults.length, 1).setValues(redirectResults); // col C
}

// ─── trigger setup (run once manually) ───────────────────────────────────────

function createHourlyTrigger() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'runStatusCheck')
    .forEach(t => ScriptApp.deleteTrigger(t));

  ScriptApp.newTrigger('runStatusCheck')
    .timeBased()
    .everyHours(1)
    .create();
}
```

Same setup: run `createHourlyTrigger()` once manually. Non-redirect URLs (200s, 404s, etc.) will write an empty string to col C since there's no `Location` header.
 
Assumption: col A = URLs, col B = status codes, col C = redirect destinations. Adjust indices as needed.

```javascript
// ─── existing functions, unchanged ───────────────────────────────────────────

function getStatusCode(url) {
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

// ─── batch checker ───────────────────────────────────────────────────────────

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const urls = sheet.getRange(2, 1, lastRow - 1, 1).getValues();
  const statusResults = [];
  const redirectResults = [];

  for (const [url] of urls) {
    if (!url) {
      statusResults.push(['']);
      redirectResults.push(['']);
      continue;
    }
    try {
      statusResults.push([getStatusCode(url)]);
    } catch (e) {
      statusResults.push(['ERROR']);
    }
    try {
      redirectResults.push([getRedirects(url) ?? '']);
    } catch (e) {
      redirectResults.push(['ERROR']);
    }
  }

  sheet.getRange(2, 2, statusResults.length, 1).setValues(statusResults);   // col B
  sheet.getRange(2, 3, redirectResults.length, 1).setValues(redirectResults); // col C
}

// ─── trigger setup (run once manually) ───────────────────────────────────────

function createHourlyTrigger() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'runStatusCheck')
    .forEach(t => ScriptApp.deleteTrigger(t));

  ScriptApp.newTrigger('runStatusCheck')
    .timeBased()
    .everyHours(1)
    .create();
}
```

Same setup: run `createHourlyTrigger()` once manually. Non-redirect URLs (200s, 404s, etc.) will write an empty string to col C since there's no `Location` header.

---

### 5. **Human** — 2026-04-27T03:41

was the base code the same
was the base code the same

---

### 6. **Claude** — 2026-04-27T03:41

The user is asking whether the base code (the existing functions) was the same between the two versions. Let me compare.

First version's getStatusCode:
- Has null/type check at top
- Follows redirect chain (loop up to 10 redirects)
- Builds a chain array with all statuses and URLs
- Returns JSON array

Second version's getStatusCode:
- No null/type check
- Single fetch, no redirect following
- Returns just the single response code

These are meaningfully different functions. The first is more complex (redirect chain follower), the second is simpler (single status check).


So while I used the same batch runner pattern for both, the underlying functions they're calling are fundamentally different—one traces the full redirect chain and the other just grabs the immediate response.No. The two `getStatusCode` functions do different things.

The first one follows the full redirect chain, builds an array of every status code and URL hop, and returns that array. The second one makes a single fetch and returns just that one status code. No chaining, no array.

The `runStatusCheck` batch wrapper I wrote for each matches the underlying function, so they differ slightly too. The first version extracts the final numeric status from the chain array. The second just writes the raw return value directly.
 
No. The two `getStatusCode` functions do different things.

The first one follows the full redirect chain, builds an array of every status code and URL hop, and returns that array. The second one makes a single fetch and returns just that one status code. No chaining, no array.

The `runStatusCheck` batch wrapper I wrote for each matches the underlying function, so they differ slightly too. The first version extracts the final numeric status from the chain array. The second just writes the raw return value directly.

---

### 7. **Human** — 2026-04-27T03:42

now this
now this

---

### 8. **Claude** — 2026-04-27T03:42

The user just said "now this" but didn't paste any code. They likely forgot to include it.No code came through. Paste it and I'll apply the same treatment.
 
No code came through. Paste it and I'll apply the same treatment.

---

### 9. **Human** — 2026-04-27T03:42

```javascript
function getStatusCode(url) {
    const url_trimmed = url.trim();

    let cache = CacheService.getScriptCache();
    let result = cache.get(url_trimmed);


    if (!result) {

        const options = {
            'muteHttpExceptions': true,
            'followRedirects': false
        };
        const response = UrlFetchApp.fetch(url_trimmed, options);
        const responseCode = response.getResponseCode();


        cache.put(url_trimmed, responseCode, 21600);
        result = responseCode;
    }

    return result;
}

function getRedirects(url) {
    
    const urlKey = url.trim()+"k";
    let cache = CacheService.getScriptCache();
    let result = cache.get(urlKey);


    if (!result) {
        const params = {
            'followRedirects': false,
            'muteHttpExceptions': true
        };
        const res = UrlFetchApp.fetch(url, params);
        const finalURL = res.getHeaders()['Location'];

        cache.put(urlKey, finalURL, 21600);
        
        result = finalURL;
    }

    return result;

}

```
```javascript
function getStatusCode(url) {
    const url_trimmed = url.trim();

    let cache = CacheService.getScriptCache();
    let result = cache.get(url_trimmed);


    if (!result) {

        const options = {
            'muteHttpExceptions': true,
            'followRedirects': false
        };
        const response = UrlFetchApp.fetch(url_trimmed, options);
        const responseCode = response.getResponseCode();


        cache.put(url_trimmed, responseCode, 21600);
        result = responseCode;
    }

    return result;
}

function getRedirects(url) {
    
    const urlKey = url.trim()+"k";
    let cache = CacheService.getScriptCache();
    let result = cache.get(urlKey);


    if (!result) {
        const params = {
            'followRedirects': false,
            'muteHttpExceptions': true
        };
        const res = UrlFetchApp.fetch(url, params);
        const finalURL = res.getHeaders()['Location'];

        cache.put(urlKey, finalURL, 21600);
        
        result = finalURL;
    }

    return result;

}

```

---

### 10. **Claude** — 2026-04-27T03:42

The user is just pasting the base code again. They probably want me to confirm what it does or compare it with something. Given the conversation context, they're likely asking me to confirm this is the code I based the second batch wrapper on.Yes, that's the exact code I based the second response on. Nothing changed in those two functions.
 
Yes, that's the exact code I based the second response on. Nothing changed in those two functions.

---

### 11. **Human** — 2026-04-27T03:51

how woould it work with e.g. =IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I3)),I3,J3)),"")
how woould it work with e.g. =IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I3)),I3,J3)),"")

---

### 12. **Claude** — 2026-04-27T03:51

The user is asking how the batch/timed approach would interact with a formula like that one.It wouldn't interact at all. They're two separate mechanisms.

The formula calls `getStatusCode` live whenever the cell recalculates. The batch function `runStatusCheck` reads URLs from a fixed column (col A in my example) and writes plain values to another column on a timer.

If you're already using formulas like that to drive the status check, the batch approach needs to match. Two options:

**Option A.** Point `runStatusCheck` at column I/J directly, replicating the `IF(ISNUMBER(SEARCH("https:",I3)),I3,J3)` logic in the script instead of the sheet. Cleaner long-term.

**Option B.** Add a helper column that resolves that formula to a plain URL, then point `runStatusCheck` at that column. Less code change, more columns.

Which column actually holds the resolved URL you want to check?
 
It wouldn't interact at all. They're two separate mechanisms.

The formula calls `getStatusCode` live whenever the cell recalculates. The batch function `runStatusCheck` reads URLs from a fixed column (col A in my example) and writes plain values to another column on a timer.

If you're already using formulas like that to drive the status check, the batch approach needs to match. Two options:

**Option A.** Point `runStatusCheck` at column I/J directly, replicating the `IF(ISNUMBER(SEARCH("https:",I3)),I3,J3)` logic in the script instead of the sheet. Cleaner long-term.

**Option B.** Add a helper column that resolves that formula to a plain URL, then point `runStatusCheck` at that column. Less code change, more columns.

Which column actually holds the resolved URL you want to check?

---

### 13. **Human** — 2026-04-27T03:51

why cant the formula just check the cells that contain getstatuscode for a statuscode, if its there save that cell as a value
why cant the formula just check the cells that contain getstatuscode for a statuscode, if its there save that cell as a value

---

### 14. **Claude** — 2026-04-27T03:52

The user is asking why the batch function can't just find cells that already contain a status code (written by the formula =IFERROR(getStatusCode(...))) and overwrite those cells with their current value (converting formula to static value).

This is actually a reasonable approach. The script could iterate through a range, check if the cell value is a number (status code like 200, 301, 404), and if so, set that cell's value to the plain number, removing the formula.

The answer to "why can't it" is: it can. That's a valid approach. Let me explain how it would work.It can. That's actually the simplest approach.

`runStatusCheck` iterates the range, checks if the cell already has a numeric value (i.e. the formula resolved to a status code), and if so overwrites it with that value directly, stripping the formula.

```javascript
function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  // Adjust column index to wherever your getStatusCode formula lives
  const col = 10; // e.g. column J
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const n = Number(v);
    return [(!isNaN(n) && n > 0) ? n : v]; // freeze if it's a valid status code, leave otherwise
  });

  range.setValues(updated);
}
```

Run `createHourlyTrigger()` once to schedule it. Each hour it scans that column, and any cell where the formula already returned a number gets frozen as a plain value. Cells that are empty or errored get left alone.

Adjust `col` to match whichever column your formula is in.
 
It can. That's actually the simplest approach.

`runStatusCheck` iterates the range, checks if the cell already has a numeric value (i.e. the formula resolved to a status code), and if so overwrites it with that value directly, stripping the formula.

```javascript
function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  // Adjust column index to wherever your getStatusCode formula lives
  const col = 10; // e.g. column J
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const n = Number(v);
    return [(!isNaN(n) && n > 0) ? n : v]; // freeze if it's a valid status code, leave otherwise
  });

  range.setValues(updated);
}
```

Run `createHourlyTrigger()` once to schedule it. Each hour it scans that column, and any cell where the formula already returned a number gets frozen as a plain value. Cells that are empty or errored get left alone.

Adjust `col` to match whichever column your formula is in.

---

### 15. **Human** — 2026-04-27T03:52

full code
full code

---

### 16. **Claude** — 2026-04-27T03:52



---

### 17. **Human** — 2026-04-27T03:52

i can set up the hourly trigger your run didnt work
i can set up the hourly trigger your run didnt work

---

### 18. **Claude** — 2026-04-27T03:52

The user wants the full code and says the trigger setup didn't work but they can set it up manually. So I just need to provide the full code without the trigger setup function, or keep it minimal.```javascript
function getStatusCode(url) {
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
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

Set the hourly trigger pointing at `runStatusCheck`. Change `col = 10` to match your column (A=1, B=2, etc.).
 
```javascript
function getStatusCode(url) {
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
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

Set the hourly trigger pointing at `runStatusCheck`. Change `col = 10` to match your column (A=1, B=2, etc.).

---

### 19. **Human** — 2026-04-27T03:52

Editor

* [Code.gs](http://Code.gs)

* 

* 
.
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
Execution log
1:52:50 PM
Notice
Execution started
1:52:50 PM
Error
TypeError: Cannot read properties of undefined (reading 'trim')
getStatusCode
@ __Code.gs:2__
Saving project...
Editor

* [Code.gs](http://Code.gs)

* 

* 
.
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
Execution log
1:52:50 PM
Notice
Execution started
1:52:50 PM
Error
TypeError: Cannot read properties of undefined (reading 'trim')
getStatusCode
@ __Code.gs:2__
Saving project...

---

### 20. **Claude** — 2026-04-27T03:53

The error is happening because `getStatusCode` is being called with `undefined` as the argument. This happens when the trigger runs `runStatusCheck` and it's not calling `getStatusCode` at all in the current version - it's just reading cell values. 

Wait, the error says `getStatusCode @ Code.gs:2` which means something is calling `getStatusCode` directly with undefined. This could be the trigger firing and somehow... no wait.

Actually the trigger is calling `runStatusCheck`, which doesn't call `getStatusCode`. But the error shows `getStatusCode` on line 2. 
 
I think the trigger might be set to run `getStatusCode` directly instead of `runStatusCheck`, or the user manually executed `getStatusCode` from the editor without passing any arguments. The solution is to add a null check at the beginning of `getStatusCode` - the first version had this protection but the second version removed it.The trigger is calling `getStatusCode` directly instead of `runStatusCheck`, or `getStatusCode` was run manually without an argument.

Two fixes: check your trigger is pointing at `runStatusCheck`, and add a null guard to `getStatusCode`:

```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string') return '';
  // ... rest unchanged
```

That prevents the crash if it ever receives an empty cell.
 
The trigger is calling `getStatusCode` directly instead of `runStatusCheck`, or `getStatusCode` was run manually without an argument.

Two fixes: check your trigger is pointing at `runStatusCheck`, and add a null guard to `getStatusCode`:

```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string') return '';
  // ... rest unchanged
```

That prevents the crash if it ever receives an empty cell.

---

### 21. **Human** — 2026-04-27T03:53

full code fix
full code fix

---

### 22. **Claude** — 2026-04-27T03:53

The user wants the full code with the null guard fix.```javascript
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
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

Make sure your trigger in Apps Script > Triggers points to `runStatusCheck`, not `getStatusCode`.
 
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
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

Make sure your trigger in Apps Script > Triggers points to `runStatusCheck`, not `getStatusCode`.

---

### 23. **Human** — 2026-04-27T03:54

this is supposed to check for 404s etc. what happens if a page goes 404 and is locked as a 200 due to the save as values?
this is supposed to check for 404s etc. what happens if a page goes 404 and is locked as a 200 due to the save as values?

---

### 24. **Claude** — 2026-04-27T03:54

The user raises a valid point - once a value is frozen as 200, if the page later becomes a 404, the script won't catch it because it overwrites the formula with a static value.Good catch. Once frozen as 200, it never rechecks. The whole point of saving as values is to stop recalculation, but that breaks monitoring.

You need to decide which goal matters more:

**A. Monitoring for changes (404s etc.)** — don't freeze values at all. Let the formula stay live and recalculate. The hourly trigger becomes unnecessary.

**B. Performance / quota saving** — freeze values, but `runStatusCheck` needs to re-fetch the URL directly instead of just reading the cell value, then overwrite with the fresh result every run.

Option B is what you actually want for a redirect checker. Updated `runStatusCheck`:

```javascript
function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const urlCol = 9;  // column with URLs (adjust)
  const statusCol = 10; // column with getStatusCode formula (adjust)

  const urls = sheet.getRange(2, urlCol, lastRow - 1, 1).getValues();

  const updated = urls.map(([url]) => {
    if (!url || typeof url !== 'string') return [''];
    try {
      const options = { muteHttpExceptions: true, followRedirects: false };
      const response = UrlFetchApp.fetch(url.trim(), options);
      return [response.getResponseCode()];
    } catch (e) {
      return ['ERROR'];
    }
  });

  sheet.getRange(2, statusCol, updated.length, 1).setValues(updated);
}
```

This re-fetches live each run and overwrites with the current status. A page that was 200 yesterday and is 404 today will show 404 after the next run.
 
Good catch. Once frozen as 200, it never rechecks. The whole point of saving as values is to stop recalculation, but that breaks monitoring.

You need to decide which goal matters more:

**A. Monitoring for changes (404s etc.)** — don't freeze values at all. Let the formula stay live and recalculate. The hourly trigger becomes unnecessary.

**B. Performance / quota saving** — freeze values, but `runStatusCheck` needs to re-fetch the URL directly instead of just reading the cell value, then overwrite with the fresh result every run.

Option B is what you actually want for a redirect checker. Updated `runStatusCheck`:

```javascript
function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const urlCol = 9;  // column with URLs (adjust)
  const statusCol = 10; // column with getStatusCode formula (adjust)

  const urls = sheet.getRange(2, urlCol, lastRow - 1, 1).getValues();

  const updated = urls.map(([url]) => {
    if (!url || typeof url !== 'string') return [''];
    try {
      const options = { muteHttpExceptions: true, followRedirects: false };
      const response = UrlFetchApp.fetch(url.trim(), options);
      return [response.getResponseCode()];
    } catch (e) {
      return ['ERROR'];
    }
  });

  sheet.getRange(2, statusCol, updated.length, 1).setValues(updated);
}
```

This re-fetches live each run and overwrites with the current status. A page that was 200 yesterday and is 404 today will show 404 after the next run.

---

### 25. **Human** — 2026-04-27T03:55

issue is it used to re-calc every time the sheet loaded or i sorted - which cost me my daily check limits
issue is it used to re-calc every time the sheet loaded or i sorted - which cost me my daily check limits

---

### 26. **Claude** — 2026-04-27T03:55

The user is explaining why they wanted to freeze values - the formula was recalculating too often (on sheet load, on sort, etc.) burning through Google Apps Script URL fetch quotas. So Option B is correct - fetch on a schedule, freeze as values. My updated runStatusCheck already does this correctly. The concern they raised about 404s being locked is actually solved by Option B - it re-fetches live each run rather than reading the existing cell value.

So the answer is: Option B is already the right solution. The trigger re-fetches fresh every hour, overwrites with current status, so a 200 that goes 404 will be caught on the next run. 

And since the formula gets replaced with a static value, it won't fire on sheet events anymore, which completely eliminates the quota drain problem.Right, so Option B is exactly correct then. The formula gets replaced with a static value after the first run, so it never recalculates on load or sort. The hourly trigger re-fetches live and overwrites, so a 200 that goes 404 gets caught on the next scheduled run.

No issue. The last code block I posted is what you want.
 
Right, so Option B is exactly correct then. The formula gets replaced with a static value after the first run, so it never recalculates on load or sort. The hourly trigger re-fetches live and overwrites, so a 200 that goes 404 gets caught on the next scheduled run.

No issue. The last code block I posted is what you want.

---

### 27. **Human** — 2026-04-27T03:55

how will the hourly trigger know where to run if the =getstatus is replaced?
how will the hourly trigger know where to run if the =getstatus is replaced?

---

### 28. **Claude** — 2026-04-27T03:56

The user is pointing out a valid issue: once the formula is replaced with a static value, the hourly trigger (which re-fetches from the URL column) doesn't rely on the formula at all. It reads URLs from `urlCol` directly and writes fresh status codes to `statusCol`. The formula column is irrelevant after the first freeze.

So the answer is: it doesn't need to know. The trigger reads URLs from the URL column (col I in their case), fetches live, and writes to the status column. The formula was just the original mechanism to populate the column the first time.It doesn't need to. The trigger reads URLs directly from the URL column, fetches live, and writes the result to the status column. The formula was only ever the original population mechanism. Once the trigger takes over, the formula is irrelevant.

Flow:
1. Formula runs once on first load, writes e.g. `200` to the status cell.
2. `runStatusCheck` fires hourly, reads col I (URLs), re-fetches each one, overwrites col J with the fresh status code.
3. Sheet loads and sorts never trigger a recalculation because there's no formula left to recalculate.

The URL column is the source of truth, not the formula column.
 
It doesn't need to. The trigger reads URLs directly from the URL column, fetches live, and writes the result to the status column. The formula was only ever the original population mechanism. Once the trigger takes over, the formula is irrelevant.

Flow:
1. Formula runs once on first load, writes e.g. `200` to the status cell.
2. `runStatusCheck` fires hourly, reads col I (URLs), re-fetches each one, overwrites col J with the fresh status code.
3. Sheet loads and sorts never trigger a recalculation because there's no formula left to recalculate.

The URL column is the source of truth, not the formula column.

---

### 29. **Human** — 2026-04-27T03:56

do you know what the columns are?
do you know what the columns are?

---

### 30. **Claude** — 2026-04-27T03:56

No. You haven't told me. What columns hold the URLs and the status codes?
 No. You haven't told me. What columns hold the URLs and the status codes?

---

### 31. **Human** — 2026-04-27T03:56

check I and J for "https" if none in I use J, if none at all error but blank.
check I and J for "https" if none in I use J, if none at all error but blank.

---

### 32. **Claude** — 2026-04-27T03:57

The user wants the runStatusCheck function to check column I for a URL (containing "https"), if not found use column J, if neither has a URL then leave blank.```javascript
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

  const colI = 9;
  const colJ = 10;
  const statusCol = 11; // adjust if your status output column differs

  const dataI = sheet.getRange(2, colI, lastRow - 1, 1).getValues();
  const dataJ = sheet.getRange(2, colJ, lastRow - 1, 1).getValues();

  const updated = dataI.map(([i], idx) => {
    const j = dataJ[idx][0];
    const url = (typeof i === 'string' && i.
 
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

  const colI = 9;
  const colJ = 10;
  const statusCol = 11; // adjust if your status output column differs

  const dataI = sheet.getRange(2, colI, lastRow - 1, 1).getValues();
  const dataJ = sheet.getRange(2, colJ, lastRow - 1, 1).getValues();

  const updated = dataI.map(([i], idx) => {
    const j = dataJ[idx][0];
    const url = (typeof i === 'string' && i.

---

### 33. **Human** — 2026-04-27T03:57

in my ooriginal code i gave you and asked you to fix - was there some sort of "run daily" we can do instead of on change etc?
in my ooriginal code i gave you and asked you to fix - was there some sort of "run daily" we can do instead of on change etc?

---

### 34. **Claude** — 2026-04-27T03:57

The user is asking if there was a daily trigger option in the original code. Looking back at the conversation, yes - in my first response I included a `createHourlyTrigger` function using `ScriptApp.newTrigger`. This can easily be changed to daily instead of hourly.Yes, the `createHourlyTrigger` function I wrote. Just swap `.everyHours(1)` for `.everyDays(1)`:

```javascript
function createDailyTrigger() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'runStatusCheck')
    .forEach(t => ScriptApp.deleteTrigger(t));

  ScriptApp.newTrigger('runStatusCheck')
    .timeBased()
    .everyDays(1)
    .atHour(8) // runs around 8am
    .create();
}
```

Run `createDailyTrigger()` once manually. Delete any existing hourly trigger in Apps Script > Triggers first if you already set one up.
 
Yes, the `createHourlyTrigger` function I wrote. Just swap `.everyHours(1)` for `.everyDays(1)`:

```javascript
function createDailyTrigger() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'runStatusCheck')
    .forEach(t => ScriptApp.deleteTrigger(t));

  ScriptApp.newTrigger('runStatusCheck')
    .timeBased()
    .everyDays(1)
    .atHour(8) // runs around 8am
    .create();
}
```

Run `createDailyTrigger()` once manually. Delete any existing hourly trigger in Apps Script > Triggers first if you already set one up.

---

### 35. **Human** — 2026-04-27T03:58

no, this code:


```
function getStatusCode(url) {
  if (!url || typeof url !== 'string') {
    return ['No URL provided'];
  }

  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  let result = cache.get(url_trimmed);

  if (!result) {
    const options = {
      'muteHttpExceptions': true,
      'followRedirects': false
    };

    let currentURL = url_trimmed;
    let chain = [];
    let maxRedirects = 10;

    for (let i = 0; i < maxRedirects; i++) {
      const response = UrlFetchApp.fetch(currentURL, options);
      const status = response.getResponseCode();
      chain.push(status);

      if ([301, 302, 303, 307, 308].includes(status)) {
        let nextLocation = response.getHeaders()['Location'];
        if (!nextLocation) break;

        // ✅ If relative, prepend base domain
        if (nextLocation.startsWith('/')) {
          try {
            const base = currentURL.match(/^(https?:\/\/[^\/]+)/)[1];
            nextLocation = base + nextLocation;
          } catch (e) {
            break; // If regex fails, stop
          }
        }

        // ✅ If protocol-relative (starts with //), add https:
        if (nextLocation.startsWith('//')) {
          nextLocation = 'https:' + nextLocation;
        }

        chain.push(nextLocation);
        currentURL = nextLocation;
      } else {
        break;
      }
    }

    result = JSON.stringify(chain);
    cache.put(url_trimmed, result, 21600);
  }

  return JSON.parse(result);
}
```
no, this code:


```
function getStatusCode(url) {
  if (!url || typeof url !== 'string') {
    return ['No URL provided'];
  }

  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  let result = cache.get(url_trimmed);

  if (!result) {
    const options = {
      'muteHttpExceptions': true,
      'followRedirects': false
    };

    let currentURL = url_trimmed;
    let chain = [];
    let maxRedirects = 10;

    for (let i = 0; i < maxRedirects; i++) {
      const response = UrlFetchApp.fetch(currentURL, options);
      const status = response.getResponseCode();
      chain.push(status);

      if ([301, 302, 303, 307, 308].includes(status)) {
        let nextLocation = response.getHeaders()['Location'];
        if (!nextLocation) break;

        // ✅ If relative, prepend base domain
        if (nextLocation.startsWith('/')) {
          try {
            const base = currentURL.match(/^(https?:\/\/[^\/]+)/)[1];
            nextLocation = base + nextLocation;
          } catch (e) {
            break; // If regex fails, stop
          }
        }

        // ✅ If protocol-relative (starts with //), add https:
        if (nextLocation.startsWith('//')) {
          nextLocation = 'https:' + nextLocation;
        }

        chain.push(nextLocation);
        currentURL = nextLocation;
      } else {
        break;
      }
    }

    result = JSON.stringify(chain);
    cache.put(url_trimmed, result, 21600);
  }

  return JSON.parse(result);
}
```

---

### 36. **Claude** — 2026-04-27T03:58

The user is asking about the first code they shared - the one with the full redirect chain. They want to know if there was a "run daily" mechanism in it. There wasn't - it's just a custom function. The batch runner and trigger were what I added. They want the full code with a daily trigger instead of hourly.No, there's nothing like that in it. It's a pure custom function, only runs when a cell calls it. The `createHourlyTrigger` / `createDailyTrigger` and `runStatusCheck` were entirely my additions from the first response. Nothing in your original code schedules itself.
 
No, there's nothing like that in it. It's a pure custom function, only runs when a cell calls it. The `createHourlyTrigger` / `createDailyTrigger` and `runStatusCheck` were entirely my additions from the first response. Nothing in your original code schedules itself.

---

### 37. **Human** — 2026-04-27T03:58

i need to rework it in some way to not run every time i sort a column
i need to rework it in some way to not run every time i sort a column

---

### 38. **Claude** — 2026-04-27T03:58

The user wants to prevent the custom function from recalculating every time they sort. The core issue is that Google Sheets custom functions recalculate on sort, load, etc.

The solution is to remove the formula from the sheet entirely and replace it with a triggered script that writes plain values. That's exactly what the `runStatusCheck` approach does.

But they need to know which columns to use. They haven't confirmed that yet for this version of the code.

Let me be concise.The only real fix is the same approach we discussed: replace the formula with a triggered function that writes plain values.

The formula recalculates because that's how Google Sheets custom functions work. There's no way to make `=getStatusCode()` ignore a sort. The options are:

1. **Trigger writes values** — `runStatusCheck` runs on a schedule, fetches URLs directly, writes static results. No formula in the cell, nothing to recalculate.
2. **Manual run** — same as above but you trigger it yourself via a menu button or the Apps Script editor instead of a timer.

What are the URL columns for this version (the chain-following one) so I can wire it up correctly?
 
The only real fix is the same approach we discussed: replace the formula with a triggered function that writes plain values.

The formula recalculates because that's how Google Sheets custom functions work. There's no way to make `=getStatusCode()` ignore a sort. The options are:

1. **Trigger writes values** — `runStatusCheck` runs on a schedule, fetches URLs directly, writes static results. No formula in the cell, nothing to recalculate.
2. **Manual run** — same as above but you trigger it yourself via a menu button or the Apps Script editor instead of a timer.

What are the URL columns for this version (the chain-following one) so I can wire it up correctly?
