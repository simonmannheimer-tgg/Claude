---
title: Simple Python SEO script for terminal (medium)
parent: Chat/Light/2026-03-27-simple-python-seo-script-for-terminal-fe21d9
uuid: fe21d9bb-451e-438e-a2ff-ef8d48139457
---

#chat/medium #project/plp-copy-auditor-script #status/completed

# Simple Python SEO script for terminal — Key User Messages

→ Light view: [[Chat/Light/2026-03-27-simple-python-seo-script-for-terminal-fe21d9]]
→ Full transcript: [[Chat/Full/2026-03-27-simple-python-seo-script-for-terminal-fe21d9]]

**Total user messages:** 10

---

### Message 1 — 2026-03-27T04:55

write me a simple python script for SEO i can run in terminal
write me a simple python script for SEO i can run in terminal

### Message 2 — 2026-03-27T04:56

Q: What should the script do?
A: something more complex, you tell me: thegoodguys.com.au
Q: What should the script do?
A: something more complex, you tell me: thegoodguys.com.au

### Message 3 — 2026-03-27T04:56

Q: Which script would be most useful right now?
A: PLP copy auditor — scrape live PLP intros, check char counts, flag non-compliant pages
Q: Which script would be most useful right now?
A: PLP copy auditor — scrape live PLP intros, check char counts, flag non-compliant pages

### Message 4 — 2026-03-27T05:07

this is the text area:

<div class="_collectionHeaderDesc_v5z64_33 text-sm"><div class="_visible_1q55e_11 _hide-xxs_1q55e_16 _hide-xs_1q55e_22 _hide-sm_1q55e_28 _hide-md_1q55e_34 _hide-lg_1q55e_40 _hide-xl_1q55e_46" style="--display: block;"><div class="_wrapper_p2ikm_19 _overlay_p2ikm_24" data-testid="readmore" data-readmore-toggle-visible="false"><div class="_content_p2ikm_28" data-testid="readmore-content" style="-webkit-line-clamp: 2;"><div><div data-testid="contentful-richtext" class="_richText_1j2n6_11 _rte_1fbwu_11"><p>Upgrade your home cinema with televisions from Samsung, LG, Sony and Hisense at The Good Guys delivering rich colour, smooth motion and smart streaming. Explore a wide range to choose screen sizes for any room and enjoy immersive movies, sport and gaming.</p></div></div></div><div class="_buttonWrapper_p2ikm_11"><button class="_button_c7qar_11 _ghost_c7qar_131 _md_c7qar_234 _moreButton_p2ikm_37" data-testid="readmore-toggle"><span class="_label_c7qar_37">...read more</span></button></div></div></div></div>

i find using xpath with contains is best, as the _NUMBER changes per page
this is the text area:

<div class="_collectionHeaderDesc_v5z64_33 text-sm"><div class="_visible_1q55e_11 _hide-xxs_1q55e_16 _hide-xs_1q55e_22 _hide-sm_1q55e_28 _hide-md_1q55e_34 _hide-lg_1q55e_40 _hide-xl_1q55e_46" style="--display: block;"><div class="_wrapper_p2ikm_19 _overlay_p2ikm_24" data-testid="readmore" data-readmore-toggle-visible="false"><div class="_content_p2ikm_28"

[truncated — see full transcript]

### Message 5 — 2026-03-27T05:07

let me add urls into the py file itself, simplere
let me add urls into the py file itself, simplere

### Message 6 — 2026-03-27T05:09

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
https://www.thegoodguys.com.au/smart-ho

[truncated — see full transcript]

### Message 7 — 2026-03-27T05:10

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
The 'from' keyword

[truncated — see full transcript]

### Message 8 — 2026-03-27T05:11

oh i was entering it into terminal
oh i was entering it into terminal

### Message 9 — 2026-03-27T05:11

do i need git so it can store the py
do i need git so it can store the py

### Message 10 — 2026-03-27T05:12

write terminal to go to:

C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\Other\Python and VSCode

and add it there
write terminal to go to:

C:\Users\simonma\OneDrive - JB HI-FI Group Pty Ltd\Desktop\Other\Python and VSCode

and add it there
