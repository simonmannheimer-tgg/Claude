---
title: Simple Python SEO script for terminal (full)
parent: Chat/Light/2026-03-27-simple-python-seo-script-for-terminal-fe21d9
uuid: fe21d9bb-451e-438e-a2ff-ef8d48139457
---

#chat/full #project/main #status/completed

# Simple Python SEO script for terminal — Full Transcript

→ Light view: [[Chat/Light/2026-03-27-simple-python-seo-script-for-terminal-fe21d9]]
→ Medium view: [[Chat/Medium/2026-03-27-simple-python-seo-script-for-terminal-fe21d9]]

**Messages:** 20 | **Date:** 2026-03-27

---

### 1. **Human** — 2026-03-27T04:55

write me a simple python script for SEO i can run in terminal
write me a simple python script for SEO i can run in terminal

---

### 2. **Claude** — 2026-03-27T04:55

What kind of SEO task do you want the script to handle?
```
This block is not supported on your current device yet.
```


 What kind of SEO task do you want the script to handle?

---

### 3. **Human** — 2026-03-27T04:56

Q: What should the script do?
A: something more complex, you tell me: thegoodguys.com.au
Q: What should the script do?
A: something more complex, you tell me: thegoodguys.com.au

---

### 4. **Claude** — 2026-03-27T04:56

Given your TGG context, here are some genuinely useful scripts I could build. Each solves a real problem you've hit before:
```
This block is not supported on your current device yet.
```


 Given your TGG context, here are some genuinely useful scripts I could build. Each solves a real problem you've hit before:

---

### 5. **Human** — 2026-03-27T04:56

Q: Which script would be most useful right now?
A: PLP copy auditor — scrape live PLP intros, check char counts, flag non-compliant pages
Q: Which script would be most useful right now?
A: PLP copy auditor — scrape live PLP intros, check char counts, flag non-compliant pages

---

### 6. **Claude** — 2026-03-27T04:57

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good. The rules are clear: 220–250 chars, hard ceiling, 2 sentences, "The Good Guys" once. Here's the script:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

**Setup (one-time):**
```bash
pip install requests beautifulsoup4
```

**Run it:**
```bash
# Basic — prints results to terminal
python tgg_plp_auditor.py urls.txt

# With CSV export
python tgg_plp_auditor.py urls.txt --output report.csv

# Slower crawl to avoid rate limits
python tgg_plp_auditor.py urls.txt --delay 2 --output report.csv
```

**urls.txt format** — full URLs or paths, one per line:
```
/televisions
/samsung/televisions
https://www.thegoodguys.com.au/coffee-machines
# comments are ignored
```

**What it checks per URL:**
- Char count with PASS/FAIL/IDEAL verdict (220–250, ideal 225–235)
- Sentence count (must be exactly 2)
- "The Good Guys" mention count (must be exactly 1)
- Banned S1 openers: Discover, Explore, Shop
- Brand page banned words on Type B/C: trusted, reliable, enjoy, features
- Hard-banned across all types: sale, discount
- S2 must be shorter than S1

**One caveat:** the intro selector targets `div.category-description p` and a few fallbacks. If TGG's Contentful-rendered markup uses a different class, the script will report SKIP. Drop me the page source for one live PLP and I can lock in the exact selector.
Good. The rules are clear: 220–250 chars, hard ceiling, 2 sentences, "The Good Guys" once. Here's the script:
**Setup (one-time):**
```bash
pip install requests beautifulsoup4
```

**Run it:**
```bash
# Basic — prints results to terminal
python tgg_plp_auditor.py urls.txt

# With CSV export
python tgg_plp_auditor.py urls.txt --output report.csv

# Slower crawl to avoid rate limits
python tgg_plp_auditor.py urls.txt --delay 2 --output report.csv
```

**urls.txt format** — full URLs or paths, one per line:
```
/televisions
/samsung/televisions
https://www.thegoodguys.com.au/coffee-machines
# comments are ignored
```

**What it checks per URL:**
- Char count with PASS/FAIL/IDEAL verdict (220–250, ideal 225–235)
- Sentence count (must be exactly 2)
- "The Good Guys" mention count (must be exactly 1)
- Banned S1 openers: Discover, Explore, Shop
- Brand page banned words on Type B/C: trusted, reliable, enjoy, features
- Hard-banned across all types: sale, discount
- S2 must be shorter than S1

**One caveat:** the intro selector targets `div.category-description p` and a few fallbacks. If TGG's Contentful-rendered markup uses a different class, the script will report SKIP. Drop me the page source for one live PLP and I can lock in the exact selector.

---

### 7. **Human** — 2026-03-27T05:07

this is the text area:

<div class="_collectionHeaderDesc_v5z64_33 text-sm"><div class="_visible_1q55e_11 _hide-xxs_1q55e_16 _hide-xs_1q55e_22 _hide-sm_1q55e_28 _hide-md_1q55e_34 _hide-lg_1q55e_40 _hide-xl_1q55e_46" style="--display: block;"><div class="_wrapper_p2ikm_19 _overlay_p2ikm_24" data-testid="readmore" data-readmore-toggle-visible="false"><div class="_content_p2ikm_28" data-testid="readmore-content" style="-webkit-line-clamp: 2;"><div><div data-testid="contentful-richtext" class="_richText_1j2n6_11 _rte_1fbwu_11"><p>Upgrade your home cinema with televisions from Samsung, LG, Sony and Hisense at The Good Guys delivering rich colour, smooth motion and smart streaming. Explore a wide range to choose screen sizes for any room and enjoy immersive movies, sport and gaming.</p></div></div></div><div class="_buttonWrapper_p2ikm_11"><button class="_button_c7qar_11 _ghost_c7qar_131 _md_c7qar_234 _moreButton_p2ikm_37" data-testid="readmore-toggle"><span class="_label_c7qar_37">...read more</span></button></div></div></div></div>

i find using xpath with contains is best, as the _NUMBER changes per page
this is the text area:

<div class="_collectionHeaderDesc_v5z64_33 text-sm"><div class="_visible_1q55e_11 _hide-xxs_1q55e_16 _hide-xs_1q55e_22 _hide-sm_1q55e_28 _hide-md_1q55e_34 _hide-lg_1q55e_40 _hide-xl_1q55e_46" style="--display: block;"><div class="_wrapper_p2ikm_19 _overlay_p2ikm_24" data-testid="readmore" data-readmore-toggle-visible="false"><div class="_content_p2ikm_28" data-testid="readmore-content" style="-webkit-line-clamp: 2;"><div><div data-testid="contentful-richtext" class="_richText_1j2n6_11 _rte_1fbwu_11"><p>Upgrade your home cinema with televisions from Samsung, LG, Sony and Hisense at The Good Guys delivering rich colour, smooth motion and smart streaming. Explore a wide range to choose screen sizes for any room and enjoy immersive movies, sport and gaming.</p></div></div></div><div class="_buttonWrapper_p2ikm_11"><button class="_button_c7qar_11 _ghost_c7qar_131 _md_c7qar_234 _moreButton_p2ikm_37" data-testid="readmore-toggle"><span class="_label_c7qar_37">...read more</span></button></div></div></div></div>

i find using xpath with contains is best, as the _NUMBER changes per page

---

### 8. **Claude** — 2026-03-27T05:07

Good catch. The hashed class suffixes make CSS selectors unreliable. Here's the updated selector using `data-testid` attributes, which are stable:

```python
# Replace the selectors list in fetch_plp_intro() with this:
selectors = [
    '[data-testid="contentful-richtext"] p',
    '[data-testid="readmore-content"] p',
]
```

Both `data-testid` values are static — `contentful-richtext` is the most precise since it targets the Contentful render directly. No xpath needed in BeautifulSoup; `data-testid` attribute selectors work natively.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Updated. One thing worth knowing: TGG's front-end likely renders this via React/Next.js, which means the `<p>` content may not be in the raw HTML response — it could be client-side rendered. If you're getting empty results on live URLs, add this quick test first:

```bash
curl -s "https://www.thegoodguys.com.au/televisions" | grep -o 'contentful-richtext'
```

If that returns nothing, the page is JS-rendered and `requests` won't see the copy. The fix would be to swap `requests` for `playwright` (headless browser). Let me know if that's the case and I'll update the script.
 Good catch. The hashed class suffixes make CSS selectors unreliable. Here's the updated selector using `data-testid` attributes, which are stable:

```python
# Replace the selectors list in fetch_plp_intro() with this:
selectors = [
    '[data-testid="contentful-richtext"] p',
    '[data-testid="readmore-content"] p',
]
```

Both `data-testid` values are static — `contentful-richtext` is the most precise since it targets the Contentful render directly. No xpath needed in BeautifulSoup; `data-testid` attribute selectors work natively.
Updated. One thing worth knowing: TGG's front-end likely renders this via React/Next.js, which means the `<p>` content may not be in the raw HTML response — it could be client-side rendered. If you're getting empty results on live URLs, add this quick test first:

```bash
curl -s "https://www.thegoodguys.com.au/televisions" | grep -o 'contentful-richtext'
```

If that returns nothing, the page is JS-rendered and `requests` won't see the copy. The fix would be to swap `requests` for `playwright` (headless browser). Let me know if that's the case and I'll update the script.

---

### 9. **Human** — 2026-03-27T05:07

let me add urls into the py file itself, simplere
let me add urls into the py file itself, simplere

---

### 10. **Claude** — 2026-03-27T05:08

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done. Now just edit the `URLS` list at the top of the file and run:

```bash
python tgg_plp_auditor.py

# or with CSV export:
python tgg_plp_auditor.py --output report.csv
```

No arguments needed. The list accepts paths (`/televisions`) or full URLs interchangeably.
 
Done. Now just edit the `URLS` list at the top of the file and run:

```bash
python tgg_plp_auditor.py

# or with CSV export:
python tgg_plp_auditor.py --output report.csv
```

No arguments needed. The list accepts paths (`/televisions`) or full URLs interchangeably.

---

### 11. **Human** — 2026-03-27T05:09

https://www.thegoodguys.com.au/laundry/washing-machines/medium-washing-machines
https://www.thegoodguys.com.au/cooking-and-dishwashers/microwaves/microwaves-and-accessories
https://www.thegoodguys.com.au/fridges-and-freezers/refrigerators/french-door-fridges
https://www.thegoodguys.com.au/fridges-and-freezers/refrigerators/bottom-mount-fridges
https://www.thegoodguys.com.au/small-kitchen-appliances/coffee-machines-and-beverages/manual-coffee-machines
https://www.thegoodguys.com.au/televisions/media-players/set-top-boxes
https://www.thegoodguys.com.au/fridges-and-freezers/refrigerators/single-door-fridges
https://www.thegoodguys.com.au/computers-tablets-and-gaming/computer-storage/usb-drives
https://www.thegoodguys.com.au/cooking-and-dishwashers/kitchenware/drinkware
https://www.thegoodguys.com.au/computers-tablets-and-gaming/software-and-accessories/microsoft-surface-accessories
https://www.thegoodguys.com.au/smart-home/home-security/indoor-security
https://www.thegoodguys.com.au/gaming/gaming-accessories/xbox-one-gaming-headsets
https://www.thegoodguys.com.au/small-kitchen-appliances/benchtop-cooking/air-fryers
https://www.thegoodguys.com.au/laundry/washing-machines/small-washing-machines
https://www.thegoodguys.com.au/cooking-and-dishwashers/ovens/wall-ovens
https://www.thegoodguys.com.au/bbqs-and-outdoor-cooking/bbq-accessories/bbq-cleaning
https://www.thegoodguys.com.au/cooking-and-dishwashers/sinks-and-taps/kitchen-sink-accessories
https://www.thegoodguys.com.au/smart-home/automatic-lawn-mowers/robot-lawn-mowers-accessories
https://www.thegoodguys.com.au/computers-tablets-and-gaming/desktop-and-laptop/laptops
https://www.thegoodguys.com.au/phones-and-wearables/wearables/apple-watch
https://www.thegoodguys.com.au/laundry/washing-machines/medium-washing-machines
https://www.thegoodguys.com.au/cooking-and-dishwashers/microwaves/microwaves-and-accessories
https://www.thegoodguys.com.au/fridges-and-freezers/refrigerators/french-door-fridges
https://www.thegoodguys.com.au/fridges-and-freezers/refrigerators/bottom-mount-fridges
https://www.thegoodguys.com.au/small-kitchen-appliances/coffee-machines-and-beverages/manual-coffee-machines
https://www.thegoodguys.com.au/televisions/media-players/set-top-boxes
https://www.thegoodguys.com.au/fridges-and-freezers/refrigerators/single-door-fridges
https://www.thegoodguys.com.au/computers-tablets-and-gaming/computer-storage/usb-drives
https://www.thegoodguys.com.au/cooking-and-dishwashers/kitchenware/drinkware
https://www.thegoodguys.com.au/computers-tablets-and-gaming/software-and-accessories/microsoft-surface-accessories
https://www.thegoodguys.com.au/smart-home/home-security/indoor-security
https://www.thegoodguys.com.au/gaming/gaming-accessories/xbox-one-gaming-headsets
https://www.thegoodguys.com.au/small-kitchen-appliances/benchtop-cooking/air-fryers
https://www.thegoodguys.com.au/laundry/washing-machines/small-washing-machines
https://www.thegoodguys.com.au/cooking-and-dishwashers/ovens/wall-ovens
https://www.thegoodguys.com.au/bbqs-and-outdoor-cooking/bbq-accessories/bbq-cleaning
https://www.thegoodguys.com.au/cooking-and-dishwashers/sinks-and-taps/kitchen-sink-accessories
https://www.thegoodguys.com.au/smart-home/automatic-lawn-mowers/robot-lawn-mowers-accessories
https://www.thegoodguys.com.au/computers-tablets-and-gaming/desktop-and-laptop/laptops
https://www.thegoodguys.com.au/phones-and-wearables/wearables/apple-watch

---

### 12. **Claude** — 2026-03-27T05:10

Done. Updated the `URLS` list with all 20:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

All 20 URLs loaded. Run it:

```bash
python tgg_plp_auditor.py --output report.csv
```

All are Type A (generic category) pages so no B/C brand-word checks will fire — just char count, sentence count, TGG mention, opener, and hard-banned word checks.
 Done. Updated the `URLS` list with all 20:
All 20 URLs loaded. Run it:

```bash
python tgg_plp_auditor.py --output report.csv
```

All are Type A (generic category) pages so no B/C brand-word checks will fire — just char count, sentence count, TGG mention, opener, and hard-banned word checks.

---

### 13. **Human** — 2026-03-27T05:10

At line:19 char:1
+ from bs4 import BeautifulSoup
+ ~~~~
The 'from' keyword is not supported in this version of the language.
At line:44 char:81
+ ... //www.thegoodguys.com.au/phones-and-wearables/wearables/apple-watch",
+                                                                          ~
Missing expression after ','.
At line:45 char:1
+ ]
+ ~
Unexpected token ']' in expression or statement.
At line:60 char:17
+     "User-Agent": (
+                 ~
Unexpected token ':' in expression or statement.
At line:61 char:59
+         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
+                                                           ~
Missing closing ')' in expression.
At line:59 char:11
+ HEADERS = {
+           ~
Missing closing '}' in statement block or type definition.
At line:64 char:5
+     )
+     ~
Unexpected token ')' in expression or statement.
At line:65 char:1
+ }
+ ~
Unexpected token '}' in expression or statement.
At line:71 char:45
+     "electrolux", "aeg", "simpson", "omega",
+                                             ~
Missing expression after ','.
At line:77 char:21
+     raw = raw.strip()
+                     ~
An expression was expected after '('.
Not all parse errors were reported.  Correct the reported errors and try again.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ReservedKeywordNotAllowed
At line:19 char:1
+ from bs4 import BeautifulSoup
+ ~~~~
The 'from' keyword is not supported in this version of the language.
At line:44 char:81
+ ... //www.thegoodguys.com.au/phones-and-wearables/wearables/apple-watch",
+                                                                          ~
Missing expression after ','.
At line:45 char:1
+ ]
+ ~
Unexpected token ']' in expression or statement.
At line:60 char:17
+     "User-Agent": (
+                 ~
Unexpected token ':' in expression or statement.
At line:61 char:59
+         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
+                                                           ~
Missing closing ')' in expression.
At line:59 char:11
+ HEADERS = {
+           ~
Missing closing '}' in statement block or type definition.
At line:64 char:5
+     )
+     ~
Unexpected token ')' in expression or statement.
At line:65 char:1
+ }
+ ~
Unexpected token '}' in expression or statement.
At line:71 char:45
+     "electrolux", "aeg", "simpson", "omega",
+                                             ~
Missing expression after ','.
At line:77 char:21
+     raw = raw.strip()
+                     ~
An expression was expected after '('.
Not all parse errors were reported.  Correct the reported errors and try again.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ReservedKeywordNotAllowed

---

### 14. **Claude** — 2026-03-27T05:10

You're running it with PowerShell instead of Python. Run it like this:

```powershell
python tgg_plp_auditor.py --output report.csv
```

If `python` isn't recognised, try:

```powershell
python3 tgg_plp_auditor.py --output report.csv
```

The error "from keyword not supported" is PowerShell trying to parse the `.py` file as a PS script — it just needs to be passed to Python as an argument, not executed directly.
 You're running it with PowerShell instead of Python. Run it like this:

```powershell
python tgg_plp_auditor.py --output report.csv
```

If `python` isn't recognised, try:

```powershell
python3 tgg_plp_auditor.py --output report.csv
```

The error "from keyword not supported" is PowerShell trying to parse the `.py` file as a PS script — it just needs to be passed to Python as an argument, not executed directly.

---

### 15. **Human** — 2026-03-27T05:11

oh i was entering it into terminal
oh i was entering it into terminal

---

### 16. **Claude** — 2026-03-27T05:11

You're on Windows so the terminal is PowerShell by default. A few things to check:

**1. Confirm Python is installed:**
```powershell
python --version
```

**2. Run the script correctly:**
```powershell
python tgg_plp_auditor.py
```

**3. Install dependencies first if you haven't:**
```powershell
pip install requests beautifulsoup4
```

If `python` returns "not recognised", you either need to install Python from [python.org](https://python.org) or it's installed but not on your PATH. In that case try:
```powershell
py tgg_plp_auditor.py
```

`py` is the Windows Python launcher and usually works even when `python` doesn't.
 You're on Windows so the terminal is PowerShell by default. A few things to check:

**1. Confirm Python is installed:**
```powershell
python --version
```

**2. Run the script correctly:**
```powershell
python tgg_plp_auditor.py
```

**3. Install dependencies first if you haven't:**
```powershell
pip install requests beautifulsoup4
```

If `python` returns "not recognised", you either need to install Python from [python.org](https://python.org) or it's installed but not on your PATH. In that case try:
```powershell
py tgg_plp_auditor.py
```

`py` is the Windows Python launcher and usually works even when `python` doesn't.

---

### 17. **Human** — 2026-03-27T05:11

do i need git so it can store the py
do i need git so it can store the py

---

### 18. **Claude** — 2026-03-27T05:11

No, Git isn't needed just to store and run the script. You just need to save the `.py` file somewhere on your computer and run it from that folder.

Simple setup:

**1. Create a folder**, e.g. `C:\Users\Simon\tgg-tools`

**2. Save the `.py` file there**

**3. Open PowerShell and navigate to it:**
```powershell
cd C:\Users\Simon\tgg-tools
```

**4. Run it:**
```powershell
python tgg_plp_auditor.py
```

Git would only be useful if you want version history or to sync it to GitHub. Not necessary for now — a folder on your machine is fine.
 No, Git isn't needed just to store and run the script. You just need to save the `.py` file somewhere on your computer and run it from that folder.

Simple setup:

**1. Create a folder**, e.g. `C:\Users\Simon\tgg-tools`

**2. Save the `.py` file there**

**3. Open PowerShell and navigate to it:**
```powershell
cd C:\Users\Simon\tgg-tools
```

**4. Run it:**
```powershell
python tgg_plp_auditor.py
```

Git would only be useful if you want version history or to sync it to GitHub. Not necessary for now — a folder on your machine is fine.

---

### 19. **Human** — 2026-03-27T05:12

write terminal to go to:

C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\Other\Python and VSCode

and add it there
write terminal to go to:

C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\Other\Python and VSCode

and add it there

---

### 20. **Claude** — 2026-03-27T05:12

```powershell
cd "C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\Other\Python and VSCode"
```

Quotes are required because of the spaces in the path. Once you're there, just drop the `.py` file into that folder and run it with `python tgg_plp_auditor.py`.
 ```powershell
cd "C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\Other\Python and VSCode"
```

Quotes are required because of the spaces in the path. Once you're there, just drop the `.py` file into that folder and run it with `python tgg_plp_auditor.py`.
