---
title: Optimizing URL fetch caching functions
date: 2026-04-13
project: main
status: completed
score: 2/5
uuid: b2091cfe-fdf7-4b84-9520-f9b0d877262d
---

#chat/light #project/main #status/completed #topic/redirect

# Optimizing URL fetch caching functions

- **Date:** [[2026-04-13]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 2/5: deliverable, project-keyword)
- **Messages:** 4
- **Chat URL:** https://claude.ai/chat/b2091cfe-fdf7-4b84-9520-f9b0d877262d
- **Medium view:** [[Chat/Medium/2026-04-13-optimizing-url-fetch-caching-functions-b2091c]]
- **Full transcript:** [[Chat/Full/2026-04-13-optimizing-url-fetch-caching-functions-b2091c]]

## Summary

without changing the =getstatuscode things, optimise this:   ``` function getStatusCode(url) {     const url_trimmed = url.trim();      let cache = CacheService.getScriptCache();     let result = cache.get(url_trimmed);       if (!result) {

## First user message

> without changing the =getstatuscode things, optimise this:   ``` function getStatusCode(url) {     const url_trimmed = url.trim();      let cache = CacheService.getScriptCache();     let result = cache.get(url_trimmed);       if (!result) {          const options = {             'muteHttpExceptions': true,             'followRedirects': false         };         const response = UrlFetchApp.fetch(u

## Topics

[[topic/redirect]]

## Skills referenced

none detected
