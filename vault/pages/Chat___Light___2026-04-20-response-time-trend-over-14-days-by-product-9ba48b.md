---
title: Response time trend over 14 days by product
date: 2026-04-20
project: main
status: completed
score: 5/5
uuid: 9ba48b82-e7c8-40f0-bcd8-083a9edd0846
---

#chat/light #project/main #status/completed #topic/pdp #topic/regex #topic/schema #topic/shopify #topic/sitemap

# Response time trend over 14 days by product

- **Date:** [[2026-04-20]]
- **Project:** [[Projects/main]]
- **Status:** #status/completed (score 5/5: deliverable, named-tgg, 5+turns, project-keyword, lasting-effect)
- **Messages:** 28
- **Chat URL:** https://claude.ai/chat/9ba48b82-e7c8-40f0-bcd8-083a9edd0846
- **Medium view:** [[Chat/Medium/2026-04-20-response-time-trend-over-14-days-by-product-9ba48b]]
- **Full transcript:** [[Chat/Full/2026-04-20-response-time-trend-over-14-days-by-product-9ba48b]]

## Summary

**Conversation Overview**

The person is working with Azure Application Insights and Kusto Query Language (KQL) to analyze web performance data for The Good Guys (thegoodguys.com.au), an Australian retail site. The conversation focused on rewriting and extending KQL queries to analyze request duration and page load times across different URL types and traffic sources over a 14-day window.

The primary tasks accomplished included rewriting a 12-hour response time query to cover 14 days, building URL-type classification using regex patterns to distinguish Products (single-level slugs like `/brand-product-model`), Categories (multi-level paths like `/cooking-and-dishwashers/rangehoods/undermount-rangehoods`), and Stores (`/stores/location-name`). Claude also built bot detection logic by parsing the user agent string from nested JSON within the `customDimensions.requestHeaders` field. Several errors were encountered and corrected along the way: the field `totalDuration` does not exist in the `requests` table (correct field is `duration`), `user_Agent` is not a top-level field (user agent is nested in `customDimensions` JSON and must be extracted via `parse_json(customDimensions).requestHeaders`), and the initial product URL regex was too strict and returned no results.

Key domain terminology used includes KQL operators (`extend`, `summarize`, `where`, `matches regex`, `parse_json`, `bin`), Application Insights tables (`requests`, `browserTimings`), and URL classification logic. The final working query classifies requests by both `BotType` (Googlebot, OpenAI/GPTBot, Anthropic/Claude-Web, Google AI/Gemini, Bing, Apple, Human) and `UrlType` (Product, Category, Store), summarized by day and rendered as a timechart. Results confirmed bots (Google AI, Bing, Googlebot) averaging 330–621ms vs. humans at ~171ms on store pages. The person noted timestamps are in UTC.

## First user message

> help me rewrite this query:  // Response time trend  // Chart request duration over the last 12 hours.  // To create an alert for this query, click '+ New alert rule' requests | where timestamp > ago(12h)  | summarize avgRequestDuration=avg(duration) by bin(timestamp, 10m) // use a time grain of 10 minutes | render timechart  i want response time last 14 days  for products, so URLs like the 

## Topics

[[topic/pdp]], [[topic/regex]], [[topic/schema]], [[topic/shopify]], [[topic/sitemap]]

## Skills referenced

none detected
