---
title: HTTP status code tracker with caching (medium)
parent: Chat/Light/2026-04-27-http-status-code-tracker-with-caching-419a95
uuid: 419a955f-473c-49f3-bf42-c28acff585ab
---

#chat/medium #project/main #status/active

# HTTP status code tracker with caching — Key User Messages

→ Light view: [[Chat/Light/2026-04-27-http-status-code-tracker-with-caching-419a95]]
→ Full transcript: [[Chat/Full/2026-04-27-http-status-code-tracker-with-caching-419a95]]

**Total user messages:** 19

---

### Message 1 — 2026-04-27T03:31

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

  return JSON.parse(result

[truncated — see full transcript]

### Message 2 — 2026-04-27T03:40

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
        const res

[truncated — see full transcript]

### Message 3 — 2026-04-27T03:41

was the base code the same
was the base code the same

### Message 4 — 2026-04-27T03:42

now this
now this

### Message 5 — 2026-04-27T03:42

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


        cache.put(u

[truncated — see full transcript]

### Message 6 — 2026-04-27T03:51

how woould it work with e.g. =IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I3)),I3,J3)),"")
how woould it work with e.g. =IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I3)),I3,J3)),"")

### Message 7 — 2026-04-27T03:51

why cant the formula just check the cells that contain getstatuscode for a statuscode, if its there save that cell as a value
why cant the formula just check the cells that contain getstatuscode for a statuscode, if its there save that cell as a value

### Message 8 — 2026-04-27T03:52

full code
full code

### Message 9 — 2026-04-27T03:52

i can set up the hourly trigger your run didnt work
i can set up the hourly trigger your run didnt work

### Message 10 — 2026-04-27T03:52

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

### Message 11 — 2026-04-27T03:53

full code fix
full code fix

### Message 12 — 2026-04-27T03:54

this is supposed to check for 404s etc. what happens if a page goes 404 and is locked as a 200 due to the save as values?
this is supposed to check for 404s etc. what happens if a page goes 404 and is locked as a 200 due to the save as values?

### Message 13 — 2026-04-27T03:55

issue is it used to re-calc every time the sheet loaded or i sorted - which cost me my daily check limits
issue is it used to re-calc every time the sheet loaded or i sorted - which cost me my daily check limits

### Message 14 — 2026-04-27T03:55

how will the hourly trigger know where to run if the =getstatus is replaced?
how will the hourly trigger know where to run if the =getstatus is replaced?

### Message 15 — 2026-04-27T03:56

do you know what the columns are?
do you know what the columns are?

### Message 16 — 2026-04-27T03:56

check I and J for "https" if none in I use J, if none at all error but blank.
check I and J for "https" if none in I use J, if none at all error but blank.

### Message 17 — 2026-04-27T03:57

in my ooriginal code i gave you and asked you to fix - was there some sort of "run daily" we can do instead of on change etc?
in my ooriginal code i gave you and asked you to fix - was there some sort of "run daily" we can do instead of on change etc?

### Message 18 — 2026-04-27T03:58

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
no,

[truncated — see full transcript]

### Message 19 — 2026-04-27T03:58

i need to rework it in some way to not run every time i sort a column
i need to rework it in some way to not run every time i sort a column
