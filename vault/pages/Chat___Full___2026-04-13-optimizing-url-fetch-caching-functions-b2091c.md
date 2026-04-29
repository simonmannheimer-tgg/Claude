---
title: Optimizing URL fetch caching functions (full)
parent: Chat/Light/2026-04-13-optimizing-url-fetch-caching-functions-b2091c
uuid: b2091cfe-fdf7-4b84-9520-f9b0d877262d
---

#chat/full #project/main #status/completed

# Optimizing URL fetch caching functions — Full Transcript

→ Light view: [[Chat/Light/2026-04-13-optimizing-url-fetch-caching-functions-b2091c]]
→ Medium view: [[Chat/Medium/2026-04-13-optimizing-url-fetch-caching-functions-b2091c]]

**Messages:** 4 | **Date:** 2026-04-13

---

### 1. **Human** — 2026-04-12T23:59

without changing the =getstatuscode things, optimise this:


```
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
without changing the =getstatuscode things, optimise this:


```
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

### 2. **Claude** — 2026-04-13T00:00

```javascript
function getStatusCode(url) {
  const trimmedUrl = url.trim();
  const cache = CacheService.getScriptCache();
  const cached = cache.get(trimmedUrl);
  
  if (cached) return cached;
  
  const response = UrlFetchApp.fetch(trimmedUrl, {
    muteHttpExceptions: true,
    followRedirects: false
  });
  const statusCode = response.getResponseCode();
  
  cache.put(trimmedUrl, statusCode, 21600);
  return statusCode;
}

function getRedirects(url) {
  const trimmedUrl = url.trim();
  const cacheKey = trimmedUrl + "k";
  const cache = CacheService.getScriptCache();
  const cached = cache.get(cacheKey);
  
  if (cached) return cached;
  
  const response = UrlFetchApp.fetch(trimmedUrl, {
    followRedirects: false,
    muteHttpExceptions: true
  });
  const location = response.getHeaders()['Location'];
  
  cache.put(cacheKey, location, 21600);
  return location;
}
```

**Changes:**

1. **Early return pattern** — eliminates nested if/else, flattens control flow
2. **const over let** — variables never reassign, use const for immutability
3. **Inline options object** — removes unnecessary variable declaration
4. **Consistent naming** — `trimmedUrl` matches convention, `cached` clearer than `result`, `statusCode`/`location` more descriptive than generic `responseCode`/`finalURL`
5. **DRY trim() call** in `getRedirects` — you were trimming once for cache key construction but passing untrimmed URL to fetch (likely unintentional bug)

**Issue flagged:** Your `getRedirects` cache key (`url.trim()+"k"`) appends "k" to distinguish it from status code cache. This works but is fragile — if you ever need a third cache type, the pattern breaks. Consider namespaced keys like `redirect:${trimmedUrl}` and `status:${trimmedUrl}` for maintainability.
 ```javascript
function getStatusCode(url) {
  const trimmedUrl = url.trim();
  const cache = CacheService.getScriptCache();
  const cached = cache.get(trimmedUrl);
  
  if (cached) return cached;
  
  const response = UrlFetchApp.fetch(trimmedUrl, {
    muteHttpExceptions: true,
    followRedirects: false
  });
  const statusCode = response.getResponseCode();
  
  cache.put(trimmedUrl, statusCode, 21600);
  return statusCode;
}

function getRedirects(url) {
  const trimmedUrl = url.trim();
  const cacheKey = trimmedUrl + "k";
  const cache = CacheService.getScriptCache();
  const cached = cache.get(cacheKey);
  
  if (cached) return cached;
  
  const response = UrlFetchApp.fetch(trimmedUrl, {
    followRedirects: false,
    muteHttpExceptions: true
  });
  const location = response.getHeaders()['Location'];
  
  cache.put(cacheKey, location, 21600);
  return location;
}
```

**Changes:**

1. **Early return pattern** — eliminates nested if/else, flattens control flow
2. **const over let** — variables never reassign, use const for immutability
3. **Inline options object** — removes unnecessary variable declaration
4. **Consistent naming** — `trimmedUrl` matches convention, `cached` clearer than `result`, `statusCode`/`location` more descriptive than generic `responseCode`/`finalURL`
5. **DRY trim() call** in `getRedirects` — you were trimming once for cache key construction but passing untrimmed URL to fetch (likely unintentional bug)

**Issue flagged:** Your `getRedirects` cache key (`url.trim()+"k"`) appends "k" to distinguish it from status code cache. This works but is fragile — if you ever need a third cache type, the pattern breaks. Consider namespaced keys like `redirect:${trimmedUrl}` and `status:${trimmedUrl}` for maintainability.

---

### 3. **Human** — 2026-04-13T00:00

i said to optimise it, if theres an issue, fix
i said to optimise it, if theres an issue, fix

---

### 4. **Claude** — 2026-04-13T00:00

```javascript
function getStatusCode(url) {
  const trimmedUrl = url.trim();
  const cacheKey = `status:${trimmedUrl}`;
  const cache = CacheService.getScriptCache();
  const cached = cache.get(cacheKey);
  
  if (cached) return cached;
  
  const response = UrlFetchApp.fetch(trimmedUrl, {
    muteHttpExceptions: true,
    followRedirects: false
  });
  const statusCode = response.getResponseCode();
  
  cache.put(cacheKey, statusCode, 21600);
  return statusCode;
}

function getRedirects(url) {
  const trimmedUrl = url.trim();
  const cacheKey = `redirect:${trimmedUrl}`;
  const cache = CacheService.getScriptCache();
  const cached = cache.get(cacheKey);
  
  if (cached) return cached;
  
  const response = UrlFetchApp.fetch(trimmedUrl, {
    followRedirects: false,
    muteHttpExceptions: true
  });
  const location = response.getHeaders()['Location'];
  
  cache.put(cacheKey, location, 21600);
  return location;
}
```

**Fixed:**
- Namespaced cache keys (`status:` and `redirect:` prefixes) prevent collisions and allow future cache types
- `getRedirects` now trims URL before fetch (was missing, would cause cache misses on padded URLs)
 ```javascript
function getStatusCode(url) {
  const trimmedUrl = url.trim();
  const cacheKey = `status:${trimmedUrl}`;
  const cache = CacheService.getScriptCache();
  const cached = cache.get(cacheKey);
  
  if (cached) return cached;
  
  const response = UrlFetchApp.fetch(trimmedUrl, {
    muteHttpExceptions: true,
    followRedirects: false
  });
  const statusCode = response.getResponseCode();
  
  cache.put(cacheKey, statusCode, 21600);
  return statusCode;
}

function getRedirects(url) {
  const trimmedUrl = url.trim();
  const cacheKey = `redirect:${trimmedUrl}`;
  const cache = CacheService.getScriptCache();
  const cached = cache.get(cacheKey);
  
  if (cached) return cached;
  
  const response = UrlFetchApp.fetch(trimmedUrl, {
    followRedirects: false,
    muteHttpExceptions: true
  });
  const location = response.getHeaders()['Location'];
  
  cache.put(cacheKey, location, 21600);
  return location;
}
```

**Fixed:**
- Namespaced cache keys (`status:` and `redirect:` prefixes) prevent collisions and allow future cache types
- `getRedirects` now trims URL before fetch (was missing, would cause cache misses on padded URLs)
