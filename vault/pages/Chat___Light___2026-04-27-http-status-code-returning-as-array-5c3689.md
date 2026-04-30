---
title: HTTP status code returning as array
date: 2026-04-27
project: main
status: active
score: 2/5
uuid: 5c368922-c9b1-4c33-8d42-b197ad8c9a52
---

#chat/light #project/main #status/active

# HTTP status code returning as array

- **Date:** [[2026-04-27]]
- **Project:** [[Projects/main]]
- **Status:** #status/active (score 2/5: deliverable, 5+turns)
- **Messages:** 12
- **Chat URL:** https://claude.ai/chat/5c368922-c9b1-4c33-8d42-b197ad8c9a52
- **Medium view:** [[Chat/Medium/2026-04-27-http-status-code-returning-as-array-5c3689]]
- **Full transcript:** [[Chat/Full/2026-04-27-http-status-code-returning-as-array-5c3689]]

## Summary

=IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I19)),I19,J19)),"")  why ouputting as: [200]   ```javascript function getStatusCode(url) {   if (!url || typeof url !== 'string') return '';   const url_trimmed = url.trim();   const cache 

## First user message

> =IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I19)),I19,J19)),"")  why ouputting as: [200]   ```javascript function getStatusCode(url) {   if (!url || typeof url !== 'string') return '';   const url_trimmed = url.trim();   const cache = CacheService.getScriptCache();   let result = cache.get(url_trimmed);    if (!result) {     const options = { muteHttpExceptions: true, followRedirects: false

## Topics

none detected

## Skills referenced

none detected
