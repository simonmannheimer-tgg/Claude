---
title: Conditional status code formula with error handling (full)
parent: Chat/Light/2026-04-27-conditional-status-code-formula-with-error-handling-8a49b6
uuid: 8a49b600-e982-4351-82bb-e87b300fdb31
---

#chat/full #project/main #status/tactical

# Conditional status code formula with error handling — Full Transcript

→ Light view: [[Chat/Light/2026-04-27-conditional-status-code-formula-with-error-handling-8a49b6]]
→ Medium view: [[Chat/Medium/2026-04-27-conditional-status-code-formula-with-error-handling-8a49b6]]

**Messages:** 2 | **Date:** 2026-04-27

---

### 1. **Human** — 2026-04-27T03:50

help me create this:

=getstatuscode(I3,if not contains https: then use j3), if error empty
help me create this:

=getstatuscode(I3,if not contains https: then use j3), if error empty

---

### 2. **Claude** — 2026-04-27T03:50

The user wants a Google Sheets formula that:
1. Calls a custom function `getstatuscode()` with a URL
2. Uses I3 as the primary URL, but if I3 doesn't contain "https:", use J3 instead
3. Returns empty string on error

This looks like they want:
`=IFERROR(getstatuscode(IF(NOT(ISNUMBER(SEARCH("https:",I3))),J3,I3)),"")`

Or more simply:
`=IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I3)),I3,J3)),"")````
=IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I3)),I3,J3)),"")
```

`SEARCH` returns a number if found, error if not. `ISNUMBER` converts that to TRUE/FALSE cleanly.
 
```
=IFERROR(getstatuscode(IF(ISNUMBER(SEARCH("https:",I3)),I3,J3)),"")
```

`SEARCH` returns a number if found, error if not. `ISNUMBER` converts that to TRUE/FALSE cleanly.
