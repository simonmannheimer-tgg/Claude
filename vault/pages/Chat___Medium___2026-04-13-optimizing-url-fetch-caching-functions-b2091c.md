---
title: Optimizing URL fetch caching functions (medium)
parent: Chat/Light/2026-04-13-optimizing-url-fetch-caching-functions-b2091c
uuid: b2091cfe-fdf7-4b84-9520-f9b0d877262d
---

#chat/medium #project/main #status/completed

# Optimizing URL fetch caching functions — Key User Messages

→ Light view: [[Chat/Light/2026-04-13-optimizing-url-fetch-caching-functions-b2091c]]
→ Full transcript: [[Chat/Full/2026-04-13-optimizing-url-fetch-caching-functions-b2091c]]

**Total user messages:** 2

---

### Message 1 — 2026-04-12T23:59

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
        const response = UrlFetchApp.fetch(

[truncated — see full transcript]

### Message 2 — 2026-04-13T00:00

i said to optimise it, if theres an issue, fix
i said to optimise it, if theres an issue, fix
