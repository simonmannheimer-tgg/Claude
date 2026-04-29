---
title: Semrush organic research data export automation (medium)
parent: Chat/Light/2026-04-17-semrush-organic-research-data-export-automation-b1d232
uuid: b1d23251-cf48-4550-8d09-b60c56dabf97
---

#chat/medium #project/main #status/completed

# Semrush organic research data export automation — Key User Messages

→ Light view: [[Chat/Light/2026-04-17-semrush-organic-research-data-export-automation-b1d232]]
→ Full transcript: [[Chat/Full/2026-04-17-semrush-organic-research-data-export-automation-b1d232]]

**Total user messages:** 14

---

### Message 1 — 2026-04-17T05:42

Can you help me create a script for chrome console that could go to semrush, go to organic research, and begin exporting it month by month as far back as i ask it to?

e.g it should goo to https://www.semrush.com/analytics/organic/overview/?db=au&searchType=domain&fid=4698283

enter a domain it asks me for (e.g. harveynorman.com.au https://www.semrush.com/analytics/organic/overview/?db=au&q=harveynorman.com.au&searchType=domain&fid=4698283)

then ask hoow many months back from current (telling me when current is), mobile or desktop, and brand or no brand or all (i supply a do not match regex, which you input as comma separated keyword not match)

final file is a compiled and merged file with month and all the info, as a xlsx.
Can you help me create a script for chrome console that could go to semrush, go to organic research, and begin exporting it month by month as far back as i ask it to?

e.g it should goo to https://www.semrush.com/analytics/organic/overview/?db=au&searchType=domain&fid=4698283

enter a domain it asks me for (e.g. harveynorman.com.au https://www.semrush.com/analytics/organic/overview/?db=au&q=harveynorman.com.au&searchType=domain&fid=4698283)

then ask hoow many months back from current (telling me when current is), mobile or desktop, and brand or no brand or all (i supply a do not match regex, which you input as comma separated keyword not match)

final file is a compiled and merged file with month and all the info, as a xlsx.

### Message 2 — 2026-04-17T05:52

cant it just stay on the same page and click the button?
cant it just stay on the same page and click the button?

### Message 3 — 2026-04-17T05:52

load a page, set up, download 1 month, change the month, click button, change the month, click button - theres no page reload its a parramater
load a page, set up, download 1 month, change the month, click button, change the month, click button - theres no page reload its a parramater

### Message 4 — 2026-04-17T06:03

ok a few things, i ran it on the main semrush page and it bullied me until i went to the right page and look, instead, ask first the url, then use the url parapmaters to autoo nav to the right spot. also, epxorrt not working:

<div class="_inAfterOutline_false_1gmko_gg_ ___SBox_1gmko_gg_" data-ui-name="Box" data-at="export" style="position: relative;"><button class="_inAfterOutline_false_1gmko_gg_ ___SBox_1gmko_gg_ _inAfterOutline_false_1gmko_gg_ ___SBoxInline_1gmko_gg_ ___SBox_1gmko_gg_ ___SButton_gw5o3_gg_ _size_m_gw5o3_gg_ _size_m_103ag_gg_ _theme_secondary-muted_gw5o3_gg_" data-ui-name="Dropdown.Trigger" type="button" aria-busy="false" tabindex="0" aria-haspopup="dialog" role="button" id="igc-ui-kit-rj1-trigger" aria-expanded="false" aria-label="Export position changes data" data-path="positions.table.export"><span class="_inAfterOutline_false_1gmko_gg_ ___SBox_1gmko_gg_ ___SInner_gw5o3_gg_" data-ui-name="Dropdown.Trigger.InnerWrapper"><span class="_inAfterOutline_false_1gmko_gg_ ___SBox_1gmko_gg_ _size_m_gw5o3_gg_ _size_m_103ag_gg_ ___SAddon_gw5o3_gg_" data-ui-name="Button.Addon"><svg aria-hidden="true" tabindex="-1" disabled="" class="___SIcon_18qo9_gg_ _inAfterOutline_false_1gmko_gg_ ___SBox_1gmko_gg_" data-ui-name="FileExport" width="16" height="16" viewBox="0 0 16 16" data-name="FileExport" data-group="m"><path d="m8 1 3.696 3.7a1 1 0 1 1-1.415 1.413L9 4.83v6.083a1 1 0 1 1-2 0V4.828l-1.289 1.29a1 1 0 1 1-1.414-1.415L8 1Z" shape-rendering="geometricPrecision"></path><

[truncated — see full transcript]

### Message 5 — 2026-04-17T06:08

hmm, it seems by navigating to the organic rankings page and needing to give you the doomain, it reset - so maybe we need to just do it the first way
hmm, it seems by navigating to the organic rankings page and needing to give you the doomain, it reset - so maybe we need to just do it the first way

### Message 6 — 2026-04-17T06:12

ok, what if we built an extension? then you could do the whole question and then nav to the right page?

also, it didnt ask me mobile or dekstip, and it donwoaded the same month twice. you need to use these for navigation:

<div class="_inAfterOutline_false_1gmko-red-team ___SBox_1gmko-red-team _size_m_1tow4-red-team _size_m_1hlru-red-team ___SDropdownMenuList_1tow4-red-team ___SScrollArea_nbn5a-red-team __size_nbn5a-red-team _size_m_1tow4-red-team _size_m_1hlru-red-team" data-ui-name="Select.Menu" id="igc-ui-kit-r6m-list" role="listbox" aria-label="Select device" style="--size_nbn5a: m;"><div class="_inAfterOutline_true_1gmko-red-team ___SBox_1gmko-red-team ___SContainer_nbn5a-red-team" data-ui-name="ScrollArea.Container" id="igc-ui-kit-r3hj-scroll-container" style="--focusRingTopOffset_nbn5a: 0; --focusRingRightOffset_nbn5a: 0; --focusRingBottomOffset_nbn5a: 0; --focusRingLeftOffset_nbn5a: 0; height: 100%;"><div class=""><div class="___SBoxInnerOutline_1gmko-red-team _inAfterOutline_false_1gmko-red-team ___SBox_1gmko-red-team __selected_1hlru-red-team _size_m_1hlru-red-team ___SDropdownItem_e6u0b-red-team __selected_e6u0b-red-team __selected_1hlru-red-team _size_m_e6u0b-red-team _size_m_1tow4-red-team _size_m_1hlru-red-team" data-ui-name="Select.Option" id="igc-ui-kit-r6m-option-0" role="option" aria-selected="true" aria-disabled="false" value="0" direction="row"><div class="___SFlex_6pord-red-team _inAfterOutline_false_1gmko-red-team ___SBox_1gmko-red-team" data-ui-name="F

[truncated — see full transcript]

### Message 7 — 2026-04-17T06:24

it doesnt do anything once on the page... also rename brand non brand to regex include exclude so i coudl use it to filter in terms not just brand non brand.

this is another semrrush exporrter i built, i want you to use it where logical - i like how its persistent overr time, wehereas your stopped if i clicked away from the ui
it doesnt do anything once on the page... also rename brand non brand to regex include exclude so i coudl use it to filter in terms not just brand non brand.

this is another semrrush exporrter i built, i want you to use it where logical - i like how its persistent overr time, wehereas your stopped if i clicked away from the ui

### Message 8 — 2026-04-17T06:55

its stuck.. not doing anything? its not changing device, month, adding keywords OR changing date . I will recoord another HAR to showyoou, the semrush.har is your plugin running, the other one is me showing what functions should be going on.
its stuck.. not doing anything? its not changing device, month, adding keywords OR changing date . I will recoord another HAR to showyoou, the semrush.har is your plugin running, the other one is me showing what functions should be going on.

### Message 9 — 2026-04-17T06:57

documentation.
Discover more extensions and themes on the Chrome Web Store
Errors
[BG] Script injection failed: Could not load file: 'xlsx.full.min.js'.
Context
background.js
Stack Trace

* background.js:79 (anonymous function)
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83
// background.js // Uses tabs.onUpdated (like PT exporter) — no race condition vs webNavigation.onCompleted. // Injects xlsx.full.min.js first so XLSX is in scope when content.js runs.  const POSITIONS_PATH = '/analytics/organic/positions/';  // ── Messages ──────────────────────────────────────────────────────────────────  chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {    if (msg.type === 'START') {     const { config, tabId } = msg;     const url =       `https://www.semrush.com/analytics/organic/positions/` +       `?db=${encodeURIComponent(config.db)}` +       `&q=${encodeURIComponent(config.domain)}` +       `&searchType=domain`;      chrome.storage.local.set({       running:       true,       done:          false,       config,       currentMonth:  0,       totalMonths:   config.monthsBack,       rowsCollected: 0,       errors:        []     }, () => chrome.tabs.update(tabId, { url }));   }    if (msg.type === 'PROGRESS') {     chrome.storage.local.set({       currentMonth:  msg.currentMo

[truncated — see full transcript]

### Message 10 — 2026-04-17T07:05

Failed to load extension
File~\OneDrive - JB HI-FI Group Pty Ltd\Desktop\Other\semrush-exporter
ErrorManifest is not valid JSON. trailing comma at line 15 column 1
Could not load manifest.
Failed to load extension
File~\OneDrive - JB HI-FI Group Pty Ltd\Desktop\Other\semrush-exporter
ErrorManifest is not valid JSON. trailing comma at line 15 column 1
Could not load manifest.

### Message 11 — 2026-04-17T07:51

now working, deepdive into this file.
now working, deepdive into this file.

### Message 12 — 2026-04-17T07:57

fix the plugin
fix the plugin

### Message 13 — 2026-04-17T08:12

still empty, and you still havent added the trendlinenext to each barchart like i asked, do a full redo of the sheet format and script.
still empty, and you still havent added the trendlinenext to each barchart like i asked, do a full redo of the sheet format and script.

### Message 14 — 2026-04-17T08:46

Ignore this file
Ignore this file
