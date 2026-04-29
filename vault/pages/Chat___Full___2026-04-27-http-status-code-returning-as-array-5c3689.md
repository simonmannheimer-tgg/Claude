---
title: HTTP status code returning as array (full)
parent: Chat/Light/2026-04-27-http-status-code-returning-as-array-5c3689
uuid: 5c368922-c9b1-4c33-8d42-b197ad8c9a52
---

#chat/full #project/main #status/active

# HTTP status code returning as array — Full Transcript

→ Light view: [[Chat/Light/2026-04-27-http-status-code-returning-as-array-5c3689]]
→ Medium view: [[Chat/Medium/2026-04-27-http-status-code-returning-as-array-5c3689]]

**Messages:** 12 | **Date:** 2026-04-27

---

### 1. **Human** — 2026-04-27T04:00

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
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```
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
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

---

### 2. **Claude** — 2026-04-27T04:01

The issue is that `cache.put()` stores values as strings, and `cache.get()` returns strings. So when the cached value is retrieved, it's the string `"200"`. But the function returns it directly.

Wait, the output is `[200]` not `200`. The brackets suggest it's being returned as an array.

Actually, looking more carefully: `cache.put(url_trimmed, responseCode, 21600)` stores the integer responseCode. Then `result = responseCode` (integer). The function returns either the cached string "200" or the integer 200.

But the output shows `[200]` with brackets. This looks like the value is being wrapped in an array somewhere.
 
I'm wondering if the square brackets in the cell output are coming from how Google Sheets displays the return value—maybe `cache.get()` is actually returning a string that looks like an array, or the function itself is inadvertently wrapping the result. I'm wondering if this could be a Google Sheets-specific behavior where the display format is adding brackets, or maybe there's something about how the custom function is returning the value that's causing this formatting issue. I'm realizing the `[200]` display might actually be Google Sheets interpreting the return value as an array—if the function somehow returns a JavaScript array with one element instead of a plain value, or if the formula was entered as an array formula with Ctrl+Shift+Enter, it would show the bracket notation. But looking at the code logic, neither the cached string nor the response code should be returning an array, so I need to figure out what's actually being returned.

Wait, I think I found it—the `runStatusCheck` function is mapping each value to a single-element array `[n]`, which creates a 2D array structure that gets set directly into the cells via `setValues()`. That means each cell is literally receiving `[200]` as its value instead of just `200`. The issue is in how the mapped values are being wrapped in arrays before being written back to the sheet. I'm wondering if the cache itself is the culprit—maybe when `cache.put()` stores the integer `200`, something in how Google Apps Script handles cache serialization and retrieval is wrapping it in an array. Let me trace through what happens: the response code gets cached as an integer, but when it comes back out via `cache.get()`, it might be getting converted to `[200]` somehow, which would explain why the cells end up with array values instead of plain numbers. I'm wondering if the issue stems from how `runStatusCheck` processes the cell value—when it reads a cached string `"200"`, converting it with `Number()` works fine, but maybe there's something about how the initial integer `200` gets stored and retrieved that's causing the array wrapping.

Let me step back: the most likely culprit is either `runStatusCheck` incorrectly wrapping values in arrays, or the cache returning values in a way that breaks the expected format. The practical fix would be to ensure `getStatusCode` always returns a clean scalar value by explicitly casting it to `Number()`.

Actually, I think I've been overcomplicating this—the `[200]` display in Google Sheets typically means a custom function is returning an array instead of a scalar. Looking at `runStatusCheck`, it's returning `[(!isNaN(n) && n > 0) ? n : v]`, which wraps the value in an array. When `.map()` processes this across multiple rows, it creates `[[200], [201], ...]`, which is the correct format for `setValues()` on a range. But if the range dimensions don't match the values array dimensions, that could cause the display issue.

Let me trace through the logic: the range is a single column with N rows, `getValues()` returns `[[v1], [v2], ...]`, the map transforms each to `[n]`, and `setValues()` applies them back. This should work correctly and display scalar numbers, not arrays. Maybe the issue is something simpler, like text formatting making `200` appear as `[200]`.

Actually, thinking about this more carefully—the user is probably seeing `[200]` in the formula bar or because Google Sheets is interpreting the function call as an array formula. The real culprit is likely that `getStatusCode` is returning a string instead of a number, or `runStatusCheck` has an issue with how it's structuring the 2D array when calling `setValues()`. I should recommend ensuring the return type is consistently a number and double-checking the array structure in `setValues()`. a string representation into the cell. 

Let me trace through once more:
- `values` = `[["200"]]` (string from custom function, 1 row, 1 col)
- `([v])` destructures to `v = "200"`  
- `Number("200")` = `200`
- `return [200]` 
- `updated` = `[[200]]`
- `setValues([[200]])` writes `200` to the cell

This should work. Unless `setValues` is getting something malformed.

Wait, what if `values` has more rows and the mapping produces some rows as `[[200]]` and this 3D structure gets flattened oddly?

I think I need to just give a clear answer. The most likely culprit is that the cache stores/returns values as strings and there's a parsing mismatch somewhere, but the `[200]` with brackets specifically suggests an array is being returned.

Looking at the actual flow: `cache.put()` requires a string, so `responseCode` gets implicitly converted to `"200"`. When retrieved, it comes back as a string. The non-cached path returns the integer directly. Neither path should produce `[200]` with brackets—unless Google Sheets is treating the return value as an array, possibly because of how the custom function is being invoked or how the signature is defined.

The practical fix is to ensure explicit type casting and verify that `runStatusCheck` isn't accidentally returning a nested array structure that's causing the brackets to appear. cell), so that's not the path.

Actually I just realized: maybe the issue is much simpler. The user might be looking at the RESULT in a Google Sheets cell where the formula returned an array result because `I19` or `J19` themselves are array formulas, causing the `IF` in the formula to return an array, which then gets passed to `getStatusCode`. If `getStatusCode` returns an array, Sheets would try to display it.

But `getStatusCode` takes a single URL string...

OK final answer: the most likely cause is that `cache.put(url_trimmed, responseCode, 21600)` - when `responseCode` is an integer, Apps Script internally calls `.toString()` on it before storing. BUT what if there's some edge case where the cache stores an object or array representation?

Actually, I just found it. I think the issue might be with how Google Sheets handles custom function return values. If the custom function returns a JavaScript number `200`, Sheets shows `200`. If it returns the string `"200"`, Sheets shows `200` (left-aligned). Neither shows `[200]`.

The only way `[200]` appears is if the cell contains the literal text `"[200]"` or displays an array formula result. But `response.getResponseCode()` should return an integer, not an array. Unless in some Apps Script version it's actually returning an array instead of a single value—that would explain the bracket notation appearing in the cell.

The practical fix is to explicitly cast to integer at every return point to ensure we're always working with scalars, not arrays.The brackets indicate an array value is landing in the cell, not a scalar. Two likely causes:

**1. `runStatusCheck` is the culprit (most likely)**

When it reads a cell that already contains the string `"200"` (from a prior cache hit), traces through fine. But if the cell contains something unexpected, the map returns `[n]` which becomes `[[200]]` passed to `setValues`. Under most conditions this is fine, but if the range dimensions mismatch even by one row, Apps Script can write the inner array as a string representation: `[200]`.

**2. Cache returns a string, not a number**

`cache.put()` silently coerces the integer to `"200"`. `cache.get()` returns `"200"`. Your function then returns a string. Sheets left-aligns it, which isn't `[200]`, but if `runStatusCheck` then reads that string cell and something goes wrong with `Number("200")` parsing in context, the array wrapping can surface.

**Fix:** Explicitly cast at every return point in `getStatusCode`:

```javascript
return Number(result);  // covers both cache hit (string) and fresh fetch (int)
```

And in `runStatusCheck`, your `return [n]` inside the map is correct for `setValues` 2D format, but add a guard:

```javascript
const updated = values.map(([v]) => {
  const raw = String(v).replace(/[\[\]]/g, '').trim(); // strip any stray brackets
  const n = Number(raw);
  return [(!isNaN(n) && n > 0) ? n : v];
});
```

The `replace` strips brackets if a `[200]` string has already been written to the sheet, breaking the loop.
 
The brackets indicate an array value is landing in the cell, not a scalar. Two likely causes:

**1. `runStatusCheck` is the culprit (most likely)**

When it reads a cell that already contains the string `"200"` (from a prior cache hit), traces through fine. But if the cell contains something unexpected, the map returns `[n]` which becomes `[[200]]` passed to `setValues`. Under most conditions this is fine, but if the range dimensions mismatch even by one row, Apps Script can write the inner array as a string representation: `[200]`.

**2. Cache returns a string, not a number**

`cache.put()` silently coerces the integer to `"200"`. `cache.get()` returns `"200"`. Your function then returns a string. Sheets left-aligns it, which isn't `[200]`, but if `runStatusCheck` then reads that string cell and something goes wrong with `Number("200")` parsing in context, the array wrapping can surface.

**Fix:** Explicitly cast at every return point in `getStatusCode`:

```javascript
return Number(result);  // covers both cache hit (string) and fresh fetch (int)
```

And in `runStatusCheck`, your `return [n]` inside the map is correct for `setValues` 2D format, but add a guard:

```javascript
const updated = values.map(([v]) => {
  const raw = String(v).replace(/[\[\]]/g, '').trim(); // strip any stray brackets
  const n = Number(raw);
  return [(!isNaN(n) && n > 0) ? n : v];
});
```

The `replace` strips brackets if a `[200]` string has already been written to the sheet, breaking the loop.

---

### 3. **Human** — 2026-04-27T04:03

change the full code
change the full code

---

### 4. **Claude** — 2026-04-27T04:03

The user wants the full updated code with the fixes applied.```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string') return '';
  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  const cached = cache.get(url_trimmed);

  if (cached !== null) return Number(cached);

  const options = { muteHttpExceptions: true, followRedirects: false };
  const response = UrlFetchApp.fetch(url_trimmed, options);
  const responseCode = response.getResponseCode();
  cache.put(url_trimmed, String(responseCode), 21600);
  return Number(responseCode);
}

function getRedirects(url) {
  if (!url || typeof url !== 'string') return '';
  const urlKey = url.trim() + 'k';
  const cache = CacheService.getScriptCache();
  const cached = cache.get(urlKey);

  if (cached !== null) return cached;

  const params = { followRedirects: false, muteHttpExceptions: true };
  const res = UrlFetchApp.fetch(url.trim(), params);
  const finalURL = res.getHeaders()['Location'] || '';
  cache.put(urlKey, finalURL, 21600);
  return finalURL;
}

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const col = 10;
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const raw = String(v).replace(/[\[\]]/g, '').trim();
    const n = Number(raw);
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

Two substantive changes beyond the bracket fix: `cached !== null` replaces the falsy check (so a cached `"0"` isn't skipped), and `getRedirects` now returns `''` instead of `undefined` when no `Location` header exists.
 
```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string') return '';
  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  const cached = cache.get(url_trimmed);

  if (cached !== null) return Number(cached);

  const options = { muteHttpExceptions: true, followRedirects: false };
  const response = UrlFetchApp.fetch(url_trimmed, options);
  const responseCode = response.getResponseCode();
  cache.put(url_trimmed, String(responseCode), 21600);
  return Number(responseCode);
}

function getRedirects(url) {
  if (!url || typeof url !== 'string') return '';
  const urlKey = url.trim() + 'k';
  const cache = CacheService.getScriptCache();
  const cached = cache.get(urlKey);

  if (cached !== null) return cached;

  const params = { followRedirects: false, muteHttpExceptions: true };
  const res = UrlFetchApp.fetch(url.trim(), params);
  const finalURL = res.getHeaders()['Location'] || '';
  cache.put(urlKey, finalURL, 21600);
  return finalURL;
}

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const col = 10;
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const raw = String(v).replace(/[\[\]]/g, '').trim();
    const n = Number(raw);
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

Two substantive changes beyond the bracket fix: `cached !== null` replaces the falsy check (so a cached `"0"` isn't skipped), and `getRedirects` now returns `''` instead of `undefined` when no `Location` header exists.

---

### 5. **Human** — 2026-04-27T04:05

ErrorResult was not a number.
ErrorResult was not a number.

---

### 6. **Claude** — 2026-04-27T04:05

The error "Result was not a number" comes from the cell formula expecting a number but getting a string or empty string. The issue is that `getStatusCode` returns `''` (empty string) for invalid URLs, and `IFERROR` wraps it, but when the function returns `Number(cached)` and `cached` is a non-numeric string, `Number()` returns `NaN`.

Wait, actually the error "Result was not a number" is a Google Sheets error that occurs when a custom function returns a non-numeric value to a cell that expects a number. But that's not quite right either.


Actually, I think the real problem is that `cache.get()` returns `null` when nothing is cached, not `undefined`, so when I try to convert that with `Number()`, it's not handling the null case properly. The issue might be that `UrlFetchApp.fetch()` throws an error when the URL is malformed, which IFERROR should catch in the formula. I'm wondering if "Result was not a number" is a specific error from Apps Script that occurs in certain edge cases, maybe when the function doesn't return a proper value type.

Let me trace through the logic: the guard returns empty string for invalid URLs, which is fine. For cache hits, we're checking that `cached` isn't null before converting it to a number. For fresh fetches, `getResponseCode()` returns an integer. So the NaN must be coming from somewhere unexpected—either `getResponseCode()` is returning something odd, or `cache.get()` is returning a value that can't be converted to a number properly.

I think the cleanest fix is to be more defensive about parsing: use `parseInt` with a radix on the cached string and check if the result is NaN before returning it, and for the fresh response, just return the integer code directly without unnecessary conversion.

Refactoring the function...`Number(cached)` returns `NaN` if the cache ever stored a non-numeric string (e.g. an error message or empty string from a bad fetch). Sheets surfaces `NaN` as "Result was not a number."

```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string') return '';
  const url_trimmed = url.trim();
  if (!url_trimmed.startsWith('http')) return '';

  const cache = CacheService.getScriptCache();
  const cached = cache.get(url_trimmed);

  if (cached !== null) {
    const n = parseInt(cached, 10);
    return isNaN(n) ? '' : n;
  }

  try {
    const options = { muteHttpExceptions: true, followRedirects: false };
    const response = UrlFetchApp.fetch(url_trimmed, options);
    const responseCode = response.getResponseCode();
    cache.put(url_trimmed, String(responseCode), 21600);
    return responseCode;
  } catch (e) {
    return '';
  }
}

function getRedirects(url) {
  if (!url || typeof url !== 'string') return '';
  const urlKey = url.trim() + 'k';
  const cache = CacheService.getScriptCache();
  const cached = cache.get(urlKey);

  if (cached !== null) return cached;

  try {
    const params = { followRedirects: false, muteHttpExceptions: true };
    const res = UrlFetchApp.fetch(url.trim(), params);
    const finalURL = res.getHeaders()['Location'] || '';
    cache.put(urlKey, finalURL, 21600);
    return finalURL;
  } catch (e) {
    return '';
  }
}

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const col = 10;
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const raw = String(v).replace(/[\[\]]/g, '').trim();
    const n = parseInt(raw, 10);
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

Key changes: `parseInt` with radix 10 replaces `Number()` everywhere, NaN guard returns `''` instead of propagating NaN, and both fetch calls are wrapped in try/catch so network errors return `''` rather than throwing into the cell.
 
`Number(cached)` returns `NaN` if the cache ever stored a non-numeric string (e.g. an error message or empty string from a bad fetch). Sheets surfaces `NaN` as "Result was not a number."

```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string') return '';
  const url_trimmed = url.trim();
  if (!url_trimmed.startsWith('http')) return '';

  const cache = CacheService.getScriptCache();
  const cached = cache.get(url_trimmed);

  if (cached !== null) {
    const n = parseInt(cached, 10);
    return isNaN(n) ? '' : n;
  }

  try {
    const options = { muteHttpExceptions: true, followRedirects: false };
    const response = UrlFetchApp.fetch(url_trimmed, options);
    const responseCode = response.getResponseCode();
    cache.put(url_trimmed, String(responseCode), 21600);
    return responseCode;
  } catch (e) {
    return '';
  }
}

function getRedirects(url) {
  if (!url || typeof url !== 'string') return '';
  const urlKey = url.trim() + 'k';
  const cache = CacheService.getScriptCache();
  const cached = cache.get(urlKey);

  if (cached !== null) return cached;

  try {
    const params = { followRedirects: false, muteHttpExceptions: true };
    const res = UrlFetchApp.fetch(url.trim(), params);
    const finalURL = res.getHeaders()['Location'] || '';
    cache.put(urlKey, finalURL, 21600);
    return finalURL;
  } catch (e) {
    return '';
  }
}

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const col = 10;
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const raw = String(v).replace(/[\[\]]/g, '').trim();
    const n = parseInt(raw, 10);
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

Key changes: `parseInt` with radix 10 replaces `Number()` everywhere, NaN guard returns `''` instead of propagating NaN, and both fetch calls are wrapped in try/catch so network errors return `''` rather than throwing into the cell.

---

### 7. **Human** — 2026-04-27T04:07

its just empty now
its just empty now

---

### 8. **Claude** — 2026-04-27T04:07

The function returns '' in too many cases. Let me think about what's happening. The formula is:

=IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I19)),I19,J19)),"")

The IFERROR wraps it, so if the function throws, it returns "". But now the function itself returns '' in error cases too, so either:

1. The URL isn't passing the `startsWith('http')` check
2. The fetch is throwing and returning ''
3. The cache has a bad value

The most likely issue: the URL being passed might have leading/trailing spaces or the `startsWith` check is too strict. 

I think the real problem is that I'm being too defensive with the validation. The response code is already a number from `getResponseCode()`, so I should just return it directly without extra parsing. The cache stores it as a string, so on a cache hit I'll parse it back. Let me write a simpler version that removes the overly strict URL validation and handles the return value properly.The `startsWith('http')` guard is probably rejecting valid URLs, and the catch-all `return ''` is swallowing the real error. Strip it back to the minimum:

```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string' || !url.trim()) return '';
  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  const cached = cache.get(url_trimmed);

  if (cached !== null) {
    const n = parseInt(cached, 10);
    return isNaN(n) ? cached : n;
  }

  const options = { muteHttpExceptions: true, followRedirects: false };
  const response = UrlFetchApp.fetch(url_trimmed, options);
  const responseCode = response.getResponseCode();
  cache.put(url_trimmed, String(responseCode), 21600);
  return responseCode;
}

function getRedirects(url) {
  if (!url || typeof url !== 'string' || !url.trim()) return '';
  const urlKey = url.trim() + 'k';
  const cache = CacheService.getScriptCache();
  const cached = cache.get(urlKey);
  if (cached !== null) return cached;

  const params = { followRedirects: false, muteHttpExceptions: true };
  const res = UrlFetchApp.fetch(url.trim(), params);
  const finalURL = res.getHeaders()['Location'] || '';
  cache.put(urlKey, finalURL, 21600);
  return finalURL;
}

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const col = 10;
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const raw = String(v).replace(/[\[\]]/g, '').trim();
    const n = parseInt(raw, 10);
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

No try/catch on the fetch now. If it errors, the IFERROR in your formula catches it and you'll at least see something went wrong rather than silent empty. Also removed the `startsWith` guard entirely since that was the most likely blocker.
 
The `startsWith('http')` guard is probably rejecting valid URLs, and the catch-all `return ''` is swallowing the real error. Strip it back to the minimum:

```javascript
function getStatusCode(url) {
  if (!url || typeof url !== 'string' || !url.trim()) return '';
  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  const cached = cache.get(url_trimmed);

  if (cached !== null) {
    const n = parseInt(cached, 10);
    return isNaN(n) ? cached : n;
  }

  const options = { muteHttpExceptions: true, followRedirects: false };
  const response = UrlFetchApp.fetch(url_trimmed, options);
  const responseCode = response.getResponseCode();
  cache.put(url_trimmed, String(responseCode), 21600);
  return responseCode;
}

function getRedirects(url) {
  if (!url || typeof url !== 'string' || !url.trim()) return '';
  const urlKey = url.trim() + 'k';
  const cache = CacheService.getScriptCache();
  const cached = cache.get(urlKey);
  if (cached !== null) return cached;

  const params = { followRedirects: false, muteHttpExceptions: true };
  const res = UrlFetchApp.fetch(url.trim(), params);
  const finalURL = res.getHeaders()['Location'] || '';
  cache.put(urlKey, finalURL, 21600);
  return finalURL;
}

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const col = 10;
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const raw = String(v).replace(/[\[\]]/g, '').trim();
    const n = parseInt(raw, 10);
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

No try/catch on the fetch now. If it errors, the IFERROR in your formula catches it and you'll at least see something went wrong rather than silent empty. Also removed the `startsWith` guard entirely since that was the most likely blocker.

---

### 9. **Human** — 2026-04-27T04:10

back now but with [2--]
back now but with [2--]

---

### 10. **Claude** — 2026-04-27T04:10

The user is seeing `[2--]` which suggests the value being returned is something like `[200]` but displayed differently, or it's actually returning an array. Wait, `[2--]` is odd. Could be `[200]` being truncated in a narrow cell? Or could it be the cell is actually showing `[2--]` as in the number is partially displayed?

Actually wait - `[2--]` looks like it could be a cell display issue where the column is too narrow to show `[200]` fully. But that would show `###` not `[2--]`.

More likely: the value being stored is still somehow wrapped in brackets.

---

### 11. **Human** — 2026-04-27T04:10

[200]
[200]

---

### 12. **Claude** — 2026-04-27T04:11

The issue is that `runStatusCheck` is writing values back to the sheet, but the formula cells are being overwritten with array representations. Actually, the core issue is simpler: `getResponseCode()` returns an integer, which is fine. But when it comes back through the custom function into Sheets, something is wrapping it.

Wait - the user is calling `getStatusCode` as a custom function from a formula: `=IFERROR(getstatuscode(...), "")`. Custom functions in Google Sheets return values directly to the cell. If the function returns a plain number like `200`, it should display as `200`.


The `[200]` display is a strong signal that the function is returning an array instead of a scalar value. Let me trace through what's happening: `response.getResponseCode()` returns an integer, which should work fine as a custom function return value, but something in the flow is wrapping it in an array before it gets back to the sheet. I'm wondering if the cache is storing the value as a stringified array like `"[200]"` instead of just `"200"` — that would explain the brackets showing up, though I'm not sure how that would happen given how we're storing it.

Actually, I think I've found it: if `runStatusCheck` ran before when the cell displayed `[200]`, it might have cached that exact string. Then when `parseInt("[200]", 10)` runs, it returns `NaN`, and the fallback logic returns the cached string `"[200]"` back to the cell. That would perfectly explain the behavior.

The real issue is that `runStatusCheck` is replacing formula results with hard values, which creates this caching problem. The simplest solution is either to clear the script cache or rethink whether `runStatusCheck` should be running at all if the formulas are already working correctly.

For an immediate fix, I should add a cache-clearing function the user can run, and modify the `isNaN` fallback to return an empty string instead of potentially corrupted cached data.The cache has `"[200]"` stored as a string from a previous bad run. `parseInt("[200]", 10)` returns `NaN`, so the code falls through to `return cached` and writes `[200]` back to the cell.

Two fixes: return `''` on bad cache hits instead of the raw string, and add a cache-clearing function to run once.

```javascript
function clearStatusCache() {
  CacheService.getScriptCache().removeAll(
    SpreadsheetApp.getActiveSpreadsheet().getActiveSheet()
      .getDataRange().getValues().flat()
      .filter(v => typeof v === 'string' && v.startsWith('http'))
      .map(v => [v.trim(), v.trim() + 'k'])
      .flat()
  );
}

function getStatusCode(url) {
  if (!url || typeof url !== 'string' || !url.trim()) return '';
  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  const cached = cache.get(url_trimmed);

  if (cached !== null) {
    const n = parseInt(cached, 10);
    if (isNaN(n)) {
      cache.remove(url_trimmed); // evict corrupt entry
      return '';
    }
    return n;
  }

  const options = { muteHttpExceptions: true, followRedirects: false };
  const response = UrlFetchApp.fetch(url_trimmed, options);
  const responseCode = response.getResponseCode();
  cache.put(url_trimmed, String(responseCode), 21600);
  return responseCode;
}

function getRedirects(url) {
  if (!url || typeof url !== 'string' || !url.trim()) return '';
  const urlKey = url.trim() + 'k';
  const cache = CacheService.getScriptCache();
  const cached = cache.get(urlKey);
  if (cached !== null) return cached;

  const params = { followRedirects: false, muteHttpExceptions: true };
  const res = UrlFetchApp.fetch(url.trim(), params);
  const finalURL = res.getHeaders()['Location'] || '';
  cache.put(urlKey, finalURL, 21600);
  return finalURL;
}

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const col = 10;
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const raw = String(v).replace(/[\[\]]/g, '').trim();
    const n = parseInt(raw, 10);
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

Run `clearStatusCache` once from the Apps Script editor, then reload the sheet.
 
The cache has `"[200]"` stored as a string from a previous bad run. `parseInt("[200]", 10)` returns `NaN`, so the code falls through to `return cached` and writes `[200]` back to the cell.

Two fixes: return `''` on bad cache hits instead of the raw string, and add a cache-clearing function to run once.

```javascript
function clearStatusCache() {
  CacheService.getScriptCache().removeAll(
    SpreadsheetApp.getActiveSpreadsheet().getActiveSheet()
      .getDataRange().getValues().flat()
      .filter(v => typeof v === 'string' && v.startsWith('http'))
      .map(v => [v.trim(), v.trim() + 'k'])
      .flat()
  );
}

function getStatusCode(url) {
  if (!url || typeof url !== 'string' || !url.trim()) return '';
  const url_trimmed = url.trim();
  const cache = CacheService.getScriptCache();
  const cached = cache.get(url_trimmed);

  if (cached !== null) {
    const n = parseInt(cached, 10);
    if (isNaN(n)) {
      cache.remove(url_trimmed); // evict corrupt entry
      return '';
    }
    return n;
  }

  const options = { muteHttpExceptions: true, followRedirects: false };
  const response = UrlFetchApp.fetch(url_trimmed, options);
  const responseCode = response.getResponseCode();
  cache.put(url_trimmed, String(responseCode), 21600);
  return responseCode;
}

function getRedirects(url) {
  if (!url || typeof url !== 'string' || !url.trim()) return '';
  const urlKey = url.trim() + 'k';
  const cache = CacheService.getScriptCache();
  const cached = cache.get(urlKey);
  if (cached !== null) return cached;

  const params = { followRedirects: false, muteHttpExceptions: true };
  const res = UrlFetchApp.fetch(url.trim(), params);
  const finalURL = res.getHeaders()['Location'] || '';
  cache.put(urlKey, finalURL, 21600);
  return finalURL;
}

function runStatusCheck() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const col = 10;
  const range = sheet.getRange(2, col, lastRow - 1, 1);
  const values = range.getValues();

  const updated = values.map(([v]) => {
    const raw = String(v).replace(/[\[\]]/g, '').trim();
    const n = parseInt(raw, 10);
    return [(!isNaN(n) && n > 0) ? n : v];
  });

  range.setValues(updated);
}
```

Run `clearStatusCache` once from the Apps Script editor, then reload the sheet.
