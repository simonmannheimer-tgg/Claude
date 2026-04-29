---
title: Contentful entry URL generator for TGG (medium)
parent: Chat/Light/2026-04-28-contentful-entry-url-generator-for-tgg-4149de
uuid: 4149de58-434b-4c3a-b3bc-6219950239f0
---

#chat/medium #project/main #status/completed

# Contentful entry URL generator for TGG — Key User Messages

→ Light view: [[Chat/Light/2026-04-28-contentful-entry-url-generator-for-tgg-4149de]]
→ Full transcript: [[Chat/Full/2026-04-28-contentful-entry-url-generator-for-tgg-4149de]]

**Total user messages:** 7

---

### Message 1 — 2026-04-28T23:38

Let's create a skill together using your skill-creator skill. I want it to be able to recognize when i am working on content on the tgg website, and offer me the contentful link using this logic:

The `environmentId` in the data is a UUID (`8370f673-69c6-417a-a841-0d3fe48edc9b`), not the string `master`. The URL uses the environment name, not the UUID. So the instruction is:
Building the Contentful entry URL from this JSON
Each entry in the JSON has a `sys` object with `id` and `environmentId`. Use them like this:

```
https://app.contentful.com/spaces/zbzrcwjtokv7/environments/master/entries/{sys.id}
```

Important: Use `master` literally, not the `environmentId` UUID from the JSON. The UUID is an internal identifier, not the URL-safe environment name.
Example — for this entry:
json

```json
"sys": {
  "id": "1nY8w50g7LnFFowLk2RRsJ",
  "environmentId": "8370f673-69c6-417a-a841-0d3fe48edc9b"
}
```

The URL is:

```
https://app.contentful.com/spaces/zbzrcwjtokv7/environments/master/entries/1nY8w50g7LnFFowLk2RRsJ
```

If you're ever working against a non-master environment, replace `master` with the environment name (e.g. `staging`), not the UUID.

hardcode this JSON file to the skill, extract the instructions for requesting re-running periodically as a silent check when running. using todays date as the benchmark
Let's create a skill together using your skill-creator skill. I want it to be able to recognize when i am working on content on the tgg website, and offer me the cont

[truncated — see full transcript]

### Message 2 — 2026-04-28T23:50

help me run more than 1000
help me run more than 1000

### Message 3 — 2026-04-28T23:50

cant i just set limit to 3000
cant i just set limit to 3000

### Message 4 — 2026-04-28T23:50

ok, redo the graphql for me
ok, redo the graphql for me

### Message 5 — 2026-04-28T23:51

the full one that's in the start of my json
the full one that's in the start of my json

### Message 6 — 2026-04-28T23:51

cant we run it all in one
cant we run it all in one

### Message 7 — 2026-04-28T23:57

I have re-run it with more than 1000 - re-read this and update the skill and references accordingly as the graphql has changed and the output is larger now
I have re-run it with more than 1000 - re-read this and update the skill and references accordingly as the graphql has changed and the output is larger now
