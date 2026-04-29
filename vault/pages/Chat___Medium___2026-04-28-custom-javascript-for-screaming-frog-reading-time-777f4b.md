---
title: Custom JavaScript for Screaming Frog reading time (medium)
parent: Chat/Light/2026-04-28-custom-javascript-for-screaming-frog-reading-time-777f4b
uuid: 777f4b97-7ce7-4af4-b2ae-089acdff2099
---

#chat/medium #project/main #status/completed

# Custom JavaScript for Screaming Frog reading time — Key User Messages

→ Light view: [[Chat/Light/2026-04-28-custom-javascript-for-screaming-frog-reading-time-777f4b]]
→ Full transcript: [[Chat/Full/2026-04-28-custom-javascript-for-screaming-frog-reading-time-777f4b]]

**Total user messages:** 4

---

### Message 1 — 2026-04-28T09:42

i need a custom js for screamingfrog - which sometimes looks like this:

// Gets all people's names from web page
//
//
// This script shows how you can import external libraries. In this example we
// use the compromise natural-language processing library.
// https://github.com/spencermountain/compromise
// 
// We use it here to extract all people's names from web pages along with a 
// count of occurrences. See the documentation for further examples of how it
// can be used.
//
function nameFreq(namesList) {
    var freqMap = {};
    namesList.forEach(name => {
        if (!freqMap[name]) {
            freqMap[name] = 0;
        }
        freqMap[name] += 1;
    });
    let sorted = Object.entries(freqMap).sort(([, a], [, b]) => b - a);
    let colonSeparatedList = [sorted.map](http://sorted.map)(entry => entry.join(':'));
    return colonSeparatedList;
}
 
return seoSpider.loadScript("https://unpkg.com/compromise")
    .then(() => {
        // You can now use the compromise library here
        let visibleText = document.body.innerText;
        let doc = nlp(visibleText);
        
        let json = doc.people().json();
        let namesList = json
          .filter(item => item.hasOwnProperty("text"))
          .map(item => item["text"]);
        
        // This will be returned to the Spider
        return [seoSpider.data](http://seoSpider.data)(nameFreq(namesList));
    })
    .catch(error => seoSpider.error(error));


to read the copy in this section:
/html/body/main/

[truncated — see full transcript]

### Message 2 — 2026-04-28T09:43

hoow loong would this take to read?

https://www.thegoodguys.com.au/whats-new/eofy-deals
hoow loong would this take to read?

https://www.thegoodguys.com.au/whats-new/eofy-deals

### Message 3 — 2026-04-28T09:46



### Message 4 — 2026-04-28T09:50

i want your js to be able to detect the difference between what you found and the 9 minutes it told me when i tested it
i want your js to be able to detect the difference between what you found and the 9 minutes it told me when i tested it
