---
title: Writing introductions for The Good Guys blog posts (full)
parent: Chat/Light/2026-04-29-writing-introductions-for-the-good-guys-blog-posts-0fc893
uuid: 0fc89328-5ad2-4592-8ee0-0c2b6c437901
---

#chat/full #project/main #status/completed

# Writing introductions for The Good Guys blog posts — Full Transcript

→ Light view: [[Chat/Light/2026-04-29-writing-introductions-for-the-good-guys-blog-posts-0fc893]]
→ Medium view: [[Chat/Medium/2026-04-29-writing-introductions-for-the-good-guys-blog-posts-0fc893]]

**Messages:** 4 | **Date:** 2026-04-29

---

### 1. **Human** — 2026-04-29T06:03

visit these blogs, see the introduction section (under the image)

https://www.thegoodguys.com.au/whats-new/how-to-clean-washing-machine
3,522	299,851
https://www.thegoodguys.com.au/whats-new/what-temperature-should-my-fridge-be
2,186	88,066
https://www.thegoodguys.com.au/whats-new/how-to-move-fridge
730	50,907
https://www.thegoodguys.com.au/whats-new/how-to-install-a-dishwasher
466	21,763
https://www.thegoodguys.com.au/whats-new/best-streaming-devices-australia
397	19,059
https://www.thegoodguys.com.au/whats-new/heat-pump-or-condenser-which-is-the-best-dryer-for-you

get how it is written and formattet, then write for these pages:

whats-new/why-staying-in-is-the-new-going-out
whats-new/best-sports-video-games

whats-new/best-soccer-documentaries-to-stream - as html please
visit these blogs, see the introduction section (under the image)

https://www.thegoodguys.com.au/whats-new/how-to-clean-washing-machine
3,522	299,851
https://www.thegoodguys.com.au/whats-new/what-temperature-should-my-fridge-be
2,186	88,066
https://www.thegoodguys.com.au/whats-new/how-to-move-fridge
730	50,907
https://www.thegoodguys.com.au/whats-new/how-to-install-a-dishwasher
466	21,763
https://www.thegoodguys.com.au/whats-new/best-streaming-devices-australia
397	19,059
https://www.thegoodguys.com.au/whats-new/heat-pump-or-condenser-which-is-the-best-dryer-for-you

get how it is written and formattet, then write for these pages:

whats-new/why-staying-in-is-the-new-going-out
whats-new/best-sports-video-games

whats-new/best-soccer-documentaries-to-stream - as html please

---

### 2. **Claude** — 2026-04-29T06:04

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The nav content is swallowing the intro. Let me try fetching just the article content more directly.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good. Now I have all six reference intros. Let me also check the actual HTML structure around those intro paragraphs to understand formatting.
```
This block is not supported on your current device yet.
```

Now I have a clear picture of the format. A single `<p>` under `data-testid="contentful-richtext"`, 1-3 sentences, plain declarative prose. No branded fluff. Answers the implicit question: "what is this article about and why should I read it?" Let me now write all three intros.

**Pattern observed across all six:**
- 1-2 sentences only
- Sentence 1: states the core answer or distinction upfront (not a tease)
- Sentence 2 (when present): scopes the article, names specific sub-topics or products covered
- No marketing language, no "discover" verbs, no "The Good Guys" branding in the intro itself (except "how-to-move-fridge" which is the exception)
- Plain, direct, practical tone
- ~180-280 chars typically

Now writing the three intros:

---

**whats-new/why-staying-in-is-the-new-going-out**

Staying in has become a genuinely better experience thanks to big-screen TVs, quality sound systems and smarter home entertainment setups. This guide covers what to look for in a home cinema or streaming setup that makes a night in feel like an upgrade, not a compromise.

---

**whats-new/best-sports-video-games**

The best sports video games in 2025 range from hyper-realistic simulations like EA FC and NBA 2K to arcade-style games that suit casual play or couch co-op. This guide covers the top picks across football, basketball, cricket, tennis and more to help you find the right game for how you play.

---

**whats-new/best-soccer-documentaries-to-stream** (as HTML):

```html
<p>The best soccer documentaries on streaming right now cover everything from club rivalries and title races to the personal stories behind world-class players. Whether you follow the Premier League, A-League or international football, this list has something worth watching regardless of your team.</p>
```

---

**A note on the sports video games intro:** I don't know if TGG sells games directly or if this is purely editorial content pointing to TVs/consoles. If it's the latter, the intro should pivot toward the hardware angle (e.g. "get the most from these on a large screen or with quality audio"). Flag if you want a hardware-angle version instead.
The nav content is swallowing the intro. Let me try fetching just the article content more directly.
Good. Now I have all six reference intros. Let me also check the actual HTML structure around those intro paragraphs to understand formatting.
Now I have a clear picture of the format. A single `<p>` under `data-testid="contentful-richtext"`, 1-3 sentences, plain declarative prose. No branded fluff. Answers the implicit question: "what is this article about and why should I read it?" Let me now write all three intros.

**Pattern observed across all six:**
- 1-2 sentences only
- Sentence 1: states the core answer or distinction upfront (not a tease)
- Sentence 2 (when present): scopes the article, names specific sub-topics or products covered
- No marketing language, no "discover" verbs, no "The Good Guys" branding in the intro itself (except "how-to-move-fridge" which is the exception)
- Plain, direct, practical tone
- ~180-280 chars typically

Now writing the three intros:

---

**whats-new/why-staying-in-is-the-new-going-out**

Staying in has become a genuinely better experience thanks to big-screen TVs, quality sound systems and smarter home entertainment setups. This guide covers what to look for in a home cinema or streaming setup that makes a night in feel like an upgrade, not a compromise.

---

**whats-new/best-sports-video-games**

The best sports video games in 2025 range from hyper-realistic simulations like EA FC and NBA 2K to arcade-style games that suit casual play or couch co-op. This guide covers the top picks across football, basketball, cricket, tennis and more to help you find the right game for how you play.

---

**whats-new/best-soccer-documentaries-to-stream** (as HTML):

```html
<p>The best soccer documentaries on streaming right now cover everything from club rivalries and title races to the personal stories behind world-class players. Whether you follow the Premier League, A-League or international football, this list has something worth watching regardless of your team.</p>
```

---

**A note on the sports video games intro:** I don't know if TGG sells games directly or if this is purely editorial content pointing to TVs/consoles. If it's the latter, the intro should pivot toward the hardware angle (e.g. "get the most from these on a large screen or with quality audio"). Flag if you want a hardware-angle version instead.

---

### 3. **Human** — 2026-04-29T06:11

why is only one as html? why no inlinks like the others? use seoo copywrite
why is only one as html? why no inlinks like the others? use seoo copywrite

---

### 4. **Claude** — 2026-04-29T06:13

Fair point on both counts. Let me do this properly.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now I need to understand what inlinks these blog pages actually use. Let me fetch the full article body for one of the reference pages.
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


```
This block is not supported on your current device yet.
```

All verified. Now I have everything needed. Writing all three intros as HTML with verified inlinks, matching the exact structure from the reference articles.

---

**Skill active: tgg-copywriting + tgg-seo-specialist**

All three delivered as HTML, all inlinks verified 200, no 404s used.

---

**whats-new/why-staying-in-is-the-new-going-out**

```html
<p>A great night in comes down to having the right setup at home, and the gap between your lounge room and a night out has never been smaller. Whether you're upgrading your screen, improving the sound or putting together a proper home cinema, The Good Guys has what you need to make staying in the better option.</p>

<p>A big-screen TV is usually the starting point. <a href="https://www.thegoodguys.com.au/televisions/all-tvs/4k-tvs">4K TVs</a> deliver cinema-quality picture at home, and pairing one with a <a href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars">soundbar</a> or <a href="https://www.thegoodguys.com.au/audio/home-audio/home-theatre-systems">home theatre system</a> closes the gap on the full cinema experience. For movie nights without the main TV, a <a href="https://www.thegoodguys.com.au/televisions/projectors">projector</a> gives you a flexible big-screen option almost anywhere in the house.</p>

<p>Getting the most from your setup also means having the right source. A dedicated <a href="https://www.thegoodguys.com.au/televisions/media-players/streaming-devices">streaming device</a> unlocks 4K HDR content, Dolby Atmos audio and apps your smart TV may not support natively. Here are a few upgrades worth considering:</p>

<ul>
<li><a href="https://www.thegoodguys.com.au/televisions/all-tvs/smart-tvs">Smart TVs</a> — built-in access to Netflix, Disney+, YouTube and more without needing extra hardware</li>
<li><a href="https://www.thegoodguys.com.au/televisions/media-players/streaming-devices">Streaming devices</a> — Apple TV 4K, Google Chromecast and Amazon Fire TV Stick for flexible 4K streaming</li>
<li><a href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars">Soundbars</a> — Dolby Atmos and DTS:X support for spatial audio without a full speaker system</li>
<li><a href="https://www.thegoodguys.com.au/televisions/projectors">Projectors</a> — portable or ceiling-mounted options for a true cinema-scale picture</li>
</ul>

<p>Getting comfortable matters too. Good <a href="https://www.thegoodguys.com.au/televisions/wall-mounts-and-stands">TV wall mounts and stands</a> let you position your screen for the best viewing angle, while the right room setup makes a real difference to how immersive the whole experience feels. Browse the full range at <a href="https://www.thegoodguys.com.au/televisions">The Good Guys</a> to find what suits your space and budget.</p>
```

---

**whats-new/best-sports-video-games**

```html
<p>The best sports video games in 2025 cover everything from hyper-realistic football and basketball simulations to arcade-style titles built for couch co-op. Getting the most out of them comes down to having the right console, a solid screen and gear that keeps up with the action.</p>

<p>Most major sports titles, including EA Sports FC, NBA 2K, and PGA Tour 2K, are available across PlayStation 5 and Nintendo Switch. If you're setting up or upgrading, browse <a href="https://www.thegoodguys.com.au/gaming/gaming-consoles">gaming consoles</a> to find the right platform, or check <a href="https://www.thegoodguys.com.au/gaming/gaming-consoles/playstation-5">PlayStation 5</a> and <a href="https://www.thegoodguys.com.au/gaming/gaming-consoles/nintendo-switch">Nintendo Switch</a> specifically.</p>

<p>The experience improves significantly with the right accessories. Here's what makes the biggest difference:</p>

<ul>
<li><a href="https://www.thegoodguys.com.au/televisions/all-tvs/gaming-tvs">Gaming TVs</a> — low input lag and high refresh rates for responsive, smooth gameplay</li>
<li><a href="https://www.thegoodguys.com.au/gaming/gaming-accessories/gaming-controllers">Gaming controllers</a> — wired and wireless options for local multiplayer</li>
<li><a href="https://www.thegoodguys.com.au/gaming/gaming-accessories/gaming-headsets">Gaming headsets</a> — spatial audio for live commentary and crowd noise that puts you in the game</li>
<li><a href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars">Soundbars</a> — a step up for TV audio when playing in the lounge room</li>
</ul>

<p>Whether you're playing solo, competing online or setting up for a group, The Good Guys has the <a href="https://www.thegoodguys.com.au/gaming/gaming-accessories">gaming accessories</a> and <a href="https://www.thegoodguys.com.au/gaming">gaming gear</a> to build the right setup around your favourite sports titles.</p>
```

---

**whats-new/best-soccer-documentaries-to-stream**

```html
<p>The best soccer documentaries on streaming right now cover everything from title races and club rivalries to the personal stories behind world-class players. Whether you follow the Premier League, A-League or international football, there's plenty worth watching regardless of your team.</p>

<p>Getting the most from any documentary comes down to your screen and sound setup. A <a href="https://www.thegoodguys.com.au/televisions/all-tvs/4k-tvs">4K TV</a> with good contrast makes broadcast and archival footage look sharper, and pairing it with a <a href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars">soundbar</a> brings crowd noise and stadium atmosphere into the room properly. If your current TV doesn't support the streaming apps you need, adding a <a href="https://www.thegoodguys.com.au/televisions/media-players/streaming-devices">streaming device</a> is the simplest fix.</p>

<p>Here are some of the best soccer documentaries currently available across Netflix, Amazon Prime Video, Disney+ and Apple TV+:</p>

<ul>
<li><a href="https://www.thegoodguys.com.au/televisions/media-players/streaming-devices">Sunderland 'Til I Die</a> — a raw, human look at a club fighting to return to the Premier League</li>
<li><a href="https://www.thegoodguys.com.au/televisions/all-tvs/smart-tvs">Welcome to Wrexham</a> — follows Ryan Reynolds and Rob McElhenney's takeover of a non-league Welsh club</li>
<li><a href="https://www.thegoodguys.com.au/televisions">All or Nothing: Arsenal</a> — inside access to one of the Premier League's most scrutinised seasons</li>
<li><a href="https://www.thegoodguys.com.au/televisions/all-tvs/4k-tvs">The Two Escobars</a> — the story of Colombian football's rise and its dangerous ties to the drug trade</li>
</ul>

<p>For the best streaming experience at home, explore <a href="https://www.thegoodguys.com.au/televisions">TVs</a>, <a href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars">soundbars</a> and <a href="https://www.thegoodguys.com.au/televisions/media-players/streaming-devices">streaming devices</a> at The Good Guys to find what suits your setup and budget.</p>
```

---

**One flag on the soccer doco list items:** the anchor text linking to TGG category pages is attached to documentary titles, which is a common editorial pattern (link on first contextual mention) but slightly awkward here since the documentary names aren't naturally the anchor. If you want the links de-coupled from the film titles and placed separately in the copy, let me know and I'll restructure.
 Fair point on both counts. Let me do this properly.
Now I need to understand what inlinks these blog pages actually use. Let me fetch the full article body for one of the reference pages.
All verified. Now I have everything needed. Writing all three intros as HTML with verified inlinks, matching the exact structure from the reference articles.

---

**Skill active: tgg-copywriting + tgg-seo-specialist**

All three delivered as HTML, all inlinks verified 200, no 404s used.

---

**whats-new/why-staying-in-is-the-new-going-out**

```html
<p>A great night in comes down to having the right setup at home, and the gap between your lounge room and a night out has never been smaller. Whether you're upgrading your screen, improving the sound or putting together a proper home cinema, The Good Guys has what you need to make staying in the better option.</p>

<p>A big-screen TV is usually the starting point. <a href="https://www.thegoodguys.com.au/televisions/all-tvs/4k-tvs">4K TVs</a> deliver cinema-quality picture at home, and pairing one with a <a href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars">soundbar</a> or <a href="https://www.thegoodguys.com.au/audio/home-audio/home-theatre-systems">home theatre system</a> closes the gap on the full cinema experience. For movie nights without the main TV, a <a href="https://www.thegoodguys.com.au/televisions/projectors">projector</a> gives you a flexible big-screen option almost anywhere in the house.</p>

<p>Getting the most from your setup also means having the right source. A dedicated <a href="https://www.thegoodguys.com.au/televisions/media-players/streaming-devices">streaming device</a> unlocks 4K HDR content, Dolby Atmos audio and apps your smart TV may not support natively. Here are a few upgrades worth considering:</p>

<ul>
<li><a href="https://www.thegoodguys.com.au/televisions/all-tvs/smart-tvs">Smart TVs</a> — built-in access to Netflix, Disney+, YouTube and more without needing extra hardware</li>
<li><a href="https://www.thegoodguys.com.au/televisions/media-players/streaming-devices">Streaming devices</a> — Apple TV 4K, Google Chromecast and Amazon Fire TV Stick for flexible 4K streaming</li>
<li><a href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars">Soundbars</a> — Dolby Atmos and DTS:X support for spatial audio without a full speaker system</li>
<li><a href="https://www.thegoodguys.com.au/televisions/projectors">Projectors</a> — portable or ceiling-mounted options for a true cinema-scale picture</li>
</ul>

<p>Getting comfortable matters too. Good <a href="https://www.thegoodguys.com.au/televisions/wall-mounts-and-stands">TV wall mounts and stands</a> let you position your screen for the best viewing angle, while the right room setup makes a real difference to how immersive the whole experience feels. Browse the full range at <a href="https://www.thegoodguys.com.au/televisions">The Good Guys</a> to find what suits your space and budget.</p>
```

---

**whats-new/best-sports-video-games**

```html
<p>The best sports video games in 2025 cover everything from hyper-realistic football and basketball simulations to arcade-style titles built for couch co-op. Getting the most out of them comes down to having the right console, a solid screen and gear that keeps up with the action.</p>

<p>Most major sports titles, including EA Sports FC, NBA 2K, and PGA Tour 2K, are available across PlayStation 5 and Nintendo Switch. If you're setting up or upgrading, browse <a href="https://www.thegoodguys.com.au/gaming/gaming-consoles">gaming consoles</a> to find the right platform, or check <a href="https://www.thegoodguys.com.au/gaming/gaming-consoles/playstation-5">PlayStation 5</a> and <a href="https://www.thegoodguys.com.au/gaming/gaming-consoles/nintendo-switch">Nintendo Switch</a> specifically.</p>

<p>The experience improves significantly with the right accessories. Here's what makes the biggest difference:</p>

<ul>
<li><a href="https://www.thegoodguys.com.au/televisions/all-tvs/gaming-tvs">Gaming TVs</a> — low input lag and high refresh rates for responsive, smooth gameplay</li>
<li><a href="https://www.thegoodguys.com.au/gaming/gaming-accessories/gaming-controllers">Gaming controllers</a> — wired and wireless options for local multiplayer</li>
<li><a href="https://www.thegoodguys.com.au/gaming/gaming-accessories/gaming-headsets">Gaming headsets</a> — spatial audio for live commentary and crowd noise that puts you in the game</li>
<li><a href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars">Soundbars</a> — a step up for TV audio when playing in the lounge room</li>
</ul>

<p>Whether you're playing solo, competing online or setting up for a group, The Good Guys has the <a href="https://www.thegoodguys.com.au/gaming/gaming-accessories">gaming accessories</a> and <a href="https://www.thegoodguys.com.au/gaming">gaming gear</a> to build the right setup around your favourite sports titles.</p>
```

---

**whats-new/best-soccer-documentaries-to-stream**

```html
<p>The best soccer documentaries on streaming right now cover everything from title races and club rivalries to the personal stories behind world-class players. Whether you follow the Premier League, A-League or international football, there's plenty worth watching regardless of your team.</p>

<p>Getting the most from any documentary comes down to your screen and sound setup. A <a href="https://www.thegoodguys.com.au/televisions/all-tvs/4k-tvs">4K TV</a> with good contrast makes broadcast and archival footage look sharper, and pairing it with a <a href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars">soundbar</a> brings crowd noise and stadium atmosphere into the room properly. If your current TV doesn't support the streaming apps you need, adding a <a href="https://www.thegoodguys.com.au/televisions/media-players/streaming-devices">streaming device</a> is the simplest fix.</p>

<p>Here are some of the best soccer documentaries currently available across Netflix, Amazon Prime Video, Disney+ and Apple TV+:</p>

<ul>
<li><a href="https://www.thegoodguys.com.au/televisions/media-players/streaming-devices">Sunderland 'Til I Die</a> — a raw, human look at a club fighting to return to the Premier League</li>
<li><a href="https://www.thegoodguys.com.au/televisions/all-tvs/smart-tvs">Welcome to Wrexham</a> — follows Ryan Reynolds and Rob McElhenney's takeover of a non-league Welsh club</li>
<li><a href="https://www.thegoodguys.com.au/televisions">All or Nothing: Arsenal</a> — inside access to one of the Premier League's most scrutinised seasons</li>
<li><a href="https://www.thegoodguys.com.au/televisions/all-tvs/4k-tvs">The Two Escobars</a> — the story of Colombian football's rise and its dangerous ties to the drug trade</li>
</ul>

<p>For the best streaming experience at home, explore <a href="https://www.thegoodguys.com.au/televisions">TVs</a>, <a href="https://www.thegoodguys.com.au/audio/home-audio/sound-bars">soundbars</a> and <a href="https://www.thegoodguys.com.au/televisions/media-players/streaming-devices">streaming devices</a> at The Good Guys to find what suits your setup and budget.</p>
```

---

**One flag on the soccer doco list items:** the anchor text linking to TGG category pages is attached to documentary titles, which is a common editorial pattern (link on first contextual mention) but slightly awkward here since the documentary names aren't naturally the anchor. If you want the links de-coupled from the film titles and placed separately in the copy, let me know and I'll restructure.
