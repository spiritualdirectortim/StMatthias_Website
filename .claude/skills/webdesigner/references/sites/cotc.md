# Church of the City (cotc.com) — design pattern study

Studied 2026-11-04. Sources: homepage raw HTML (post-render DOM plus original source via curl),
the single site stylesheet `cotc-f21faa.webflow.shared.3a40f770a.css` (111 KB), the Webflow JS bundle
(IX2 interaction definitions extracted), inline page scripts, Firecrawl markdown of `/visit`, `/give`,
`/watch`, `/events`, `/franklin`, `/ministry/kidcity`, and screenshots at 1920 desktop (viewport and
full page, 6636 px tall) and 360 mobile.

Everything marked **(inference)** was not directly observed in code and is deduced from screenshots or
behavior. All other values are quoted from the CSS/HTML/JS.

---

## 1. Platform & stack

| Layer | What they use | Notes |
|---|---|---|
| Builder / host | **Webflow** (site id `662ad9ef1194a12394bbe024`, staging `cotc-f21faa.webflow.io`) | Last published `Tue Nov 03 2026`. Webflow CMS (`w-dyn-list`) drives locations, ministries, events, announcement bar, nav ministry lists. Several live links still point at the staging domain. |
| CSS | One compiled stylesheet, ~111 KB, plus 8 small `<style>` blocks from "custom code embeds" (nested-CSS syntax compiled to flat rules) | BEM-ish naming with prefixes: `l-` layout, `c-` component, `o-` object, `u-` utility (`l-section`, `c-hero`, `o-button`, `u-type-h1`). |
| JS | `webflow.js` + 2 chunks (~537 KB total), jQuery 3.5.1 (Webflow default), **cash.js 8.1.5** (jQuery-alike, loaded in head), **Splide 4.1.4** (jsDelivr) for all carousels, Webflow **IX2** for interactions, Webflow **Lottie** plugin (`.lottie` logo), YouTube iframe API (`www-widgetapi.js`), inline FileSaver.js | No GSAP, AOS, Lenis, Locomotive, Framer, Swiper. Motion is mostly CSS transitions plus Splide and two IX2 interactions. |
| Fonts | Self-hosted **Inter Variable** (body) and **Inter Display** static weights (headings), all `.woff2` on Webflow CDN | No Google Fonts / Typekit requests. |
| Media | Webflow CDN images in **AVIF**, WebP, JPG; `loading="lazy"`; hero is a Webflow background-video component (`.mp4` + `.webm` + poster `.jpg`) | |
| Third parties | Planning Center **Church Center** calendar embeds (iframes filtered by `campus` and `category`), **Pushpay** per-campus giving links, Mailchimp list signup, Linktree for socials and weekly announcements, YouTube `live/` links per campus | No analytics tags found in the source HTML (none of GTM/gtag/FB pixel). |
| Head | No `<meta name="description">` or OG tags on the homepage; favicon 32 and 256 px PNG; `preconnect` to Webflow CDN | SEO weakness. |

---

## 2. Typography

### Families and loading
- `--type--body: Inter, sans-serif` → `@font-face "Inter"` variable font, `font-weight: 100 900`, normal + italic, `font-display: swap`.
- `--type--headings: "Inter Display", sans-serif` → 18 static `@font-face` blocks (100–900, normal + italic), `font-display: swap`.
- Payload note: 20 font files declared; only the weights actually used are fetched by the browser, but the CSS is bloated.

### Design tokens (from `:root`)
```
--type--h1-size: 40px;   --type--h1-height: 1.1em;
--type--h2-size: 28px;   --type--h2-height: 1em;
--type--h3-size: 22px;   --type--h3-height: 1.2em;
--type--body-size: 16px; --type--body-height: 1.4em;  --type--body-height-1-5: 1.5em;
--type--body-size-small: 16px;
--type--badge-size: 14px; --type--badge-height: 1em;
--type--button-size: 16px;
--type--form-text-field-size: 16px; --type--form-text-field-height: 19px;
```

### Utility classes (the real type scale)
| Class | Family | Size | Weight | Line-height | Use |
|---|---|---|---|---|---|
| `.u-type-super` | inherits body (Inter) | **64px** | 400 | 1.1em | Scripture pull-quote on home ("Lord, I have heard of your fame…"). `letter-spacing: -1.28px` (= -0.02em). Only tracking rule in the whole site. |
| `.u-type-h1` | Inter Display | 40px | 700 | 1.1 | Page h1, "Ministries" carousel header |
| `.u-type-h3-2` | Inter Display | 32px | 400 | 1.2 | Light display subhead |
| `.u-type-h2` | Inter Display | 28px | 700 | 1.0 | Section headlines, footer "Church of the City", scripture reference |
| `.u-type-title` | Inter Display | 26px | 400 | 1.4 | Titles |
| `.u-type-h3` | Inter Display | 22px | 700 | 1.2 | Card titles (location names, ministry names), footer column heads |
| `.u-type-body.large` | Inter | 22px | 400 | 1.4 | |
| `.u-type-body-2` | Inter | 20px | 400 | 1.4 | |
| `.u-type-body` | Inter | 16px | 400 | 1.4 | Body; `.medium` = 600 black; `.light` = opacity .5; `.faded` = opacity .6 |
| `.u-type-caption` | Inter | 16px | 400 | 1.5 | opacity .6, dark; footer © |
| `.u-type-h4` | Inter | 16px | 400 | — | `text-transform: uppercase` (the only uppercase style; rarely used) |
| `.u-type-h5` / `.u-type-h6` | Inter | 16px | 500 / 600 | — | |
| `.u-type-link` | Inter | — | — | 1.4 | color `#828282` |

Display type outside the utilities:
- Menu overlay large links `.c-nav__dropdown-link-large`: Inter Display **48px / 1em / 400**.
- Menu overlay column headlines `.c-nav__dropdown-headline`: Inter Display 28px / 1em.
- Values ("Our Pursuits") titles `.c-values__item-title`: Inter Display **40px / 1.05em / 400**, two-tone: `<strong>` white `#fff`, remainder `#fff9` (60% white). Also `.o-icon-card__title` same with grey `#828282` second line on light bg.
- Nav links: 16px / 1em, padding 10px 20px. Footer links: 16px / 1em, grey.
- Search input: Inter Display, h2 size, 700, centered.

### Responsive type (Webflow breakpoints)
- `≤991px`: `.u-type-h3` → `calc(22px * .8)` = 17.6px; `.u-type-super` → 40px; `.u-type-h3-2` ×.8.
- `≤767px`: `.u-type-h1` → `calc(40px * .7)` = 28px; `.u-type-h2` → `calc(28px * .75)` = 21px; `.u-type-body` and `.u-type-body-2` → `×.8` = **12.8px** (too small; see weaknesses).
- `≤479px`: `.u-type-title` 18px; `.u-type-h2.mobile-sm` 20px.
- No `clamp()` anywhere; scale is step-based.

### Casing, voice and weight strategy
- Sentence case everywhere, headlines end in periods: "Practicing the Way of Jesus." "One church, multiple locations." "Stay up to date with COTC."
- **"Small and bold, big and light"**: h1–h3 at 22–40px are 700; the big display moments (64px scripture, 48px menu links, 40px values) drop to 400. This is the most distinctive typographic move.
- Tight leading on headings (1.0–1.2), normal body (1.4). Zero tracking except the 64px quote.
- Labels/eyebrows are 14px in bordered "badge" chips rather than uppercase tracked text.

---

## 3. Color & imagery

### Tokens
```
--color--canvas: #fafafa      page background (off-white, not pure white)
--color--dark: #252525        text "black"; --color--black aliases it
--color--light: #ececec       text on dark surfaces (not pure white)
--color--light-grey: #eaeaea  (also legacy --light-grey) grey section bg
--color--off-white: #f1f1f1   light badge borders
--color--grey: #828282        secondary text, addresses, footer links, links inside paragraphs
--color--alternate-grey: #afafaf
--color--white: white         card surfaces
--color--live: #ec2b2b        the ONLY chromatic accent: "Live Now" state
--color--button-dark: #000000e6   (90% black)   --color--button-light: #ffffffe6 (90% white)
--type--badge-border: #25252580
```
- Monochrome system: black / near-white / greys. All colour comes from photography and the hero video. Red appears only for live state.
- Surfaces: white cards on `#fafafa` canvas; dark sections use photography with light text, never flat black (except `.l-section.black`, unused on home).
- Translucency is the brand finish: `rgba` surfaces + `backdrop-filter` (see glass recipe in section 13).

### Imagery
- Documentary congregation photography: worship from the crowd, lobbies, round-table events, aerial of the Village campus. Warm skin tones, stage haze, lots of people. No stock, no illustration except four line icons.
- Aspect control via data attributes compiled to CSS: `.o-image[data-aspect-ratio="ar16x9|ar3x2|ar2x3|ar1x1|ar4x3|ar3x4|ar3x1|auto"]` and `[data-image-align="top left" … "bottom right"]` → `object-position`. Section backgrounds take `[data-image-focus="top|center|bottom"]`.
- Default `.o-image`: `aspect-ratio: 3/2; border-radius: 12px; overflow: hidden;` with `.o-image__img` `object-fit: cover`.
- Location card image: fixed `height: 439px` desktop → `aspect-ratio: 2.39` tablet → `16/9` phone, radius 12.
- Ministry cards: `aspect-ratio: 2/3` portrait, radius 16.
- **Blurred-duplicate scrim** (ministry cards): the same `<img>` is rendered twice; the second gets `filter: brightness(25%) blur(50px)` and `mask-image: linear-gradient(0deg, #000 5%, #0000 70% 80%)`, so the bottom third darkens with the image's own colours instead of a flat black gradient. Images are oversized (`min-width: calc(100% + 100px); inset: 0 -50px -50px`) so the blur has no hard edges. An alternative overlay class exists: `linear-gradient(0deg, #000, #00000061 39%)` (34% ≤991, 23% ≤767).
- Hero scrim is intentionally light: `linear-gradient(0deg, #00000026, #00000026 85%, #0000)` — only 15% black, relying on dark footage.
- Dark "Our Pursuits" band uses a pre-faded background image (`Our Story - BG-fade.webp`) that dissolves to the canvas colour at its top, pulled up under the previous section (see layout).
- Radii: `--size--border-radius: 12px` (images, buttons, popups), `-small: 5px` (badges, small buttons), `-large: 16px` (cards). Nav pill 6px. Circles 24/40/48px.
- Shadows: cards `0 4px 20px #0000001a`; footer "page end" `0 0 14px #0000001a`; glass inner rim `inset 0 -2px 8px 1px #ffffff26`.

---

## 4. Layout & page structure

### Grid system
- `--size--container-max: 1480px`, `--size--gutter: 24px`. `.l-container { width:100%; max-width:1480px; padding: 0 24px }` inside `.l-section { display:flex; flex-flow:column; align-items:center; position:relative }`.
- Spacing is explicit spacer divs: `.l-spacer { height:70px }`, `._24` 24px, `._60` 60px, `._100` 100px, often stacked (two `_60` = 120px between story blocks).
- Breakpoints (Webflow + IX2 `site.mediaQueries`): main ≥992, medium 768–991, small 480–767, tiny ≤479; one `min-width: 1440px` block and one `min-width: 768px`. Custom embeds also use 641px and 769px.
- Columns: CSS grid `1fr 1fr` is the default for heads, heroes, footers; 3 and 4 columns for values/footer nav; text uses **CSS multi-column** (`column-count: 2; column-gap: 75px`, `[data-gap-size="large"]` 150px) rather than two divs.
- `.l-hr { width:100% } .l-hr.dark { color:#828282 } .l-hr.light { opacity:.2 }` as section dividers.

### Homepage, section by section (desktop 1920; full page 6636 px)
1. **Sticky nav pill + announcement bar** (see section 5). Nav is `position: sticky; top:0; margin-bottom: -58px` so section 2 begins underneath it.
2. **Hero** (video, `min-height: 85vh`, 65vh ≤991): headline bottom-left, descriptor, two buttons, then a 60px spacer inside the hero (see section 6).
3. **Section head "Locations"**: `.o-badge` eyebrow "Locations" → `.c-section-head__inner` grid `1fr 1fr`, `margin-top: 24px`: h2 "One church, multiple locations." left, `.o-button` "Watch Online →" right-aligned (`align-items:flex-end`). Two `_24` spacers follow.
4. **Location grid**: `.c-location-grid__list` grid `1fr 1fr`, gap 24, `padding-bottom: 24px`; 5 CMS items (Franklin, Downtown, Spring Hill, Nolensville, The Village); page-specific CSS makes `:nth-child(5)` span 2 columns at ≥767 (on `/visit` and `/give` it is `:nth-child(4)` spanning 3). Card anatomy in section 9.
5. `hr.l-hr.dark` inside a container, then `_60` spacer.
6. **Scripture block** `.c-scripture` (flex column, gap 52): `.o-badge` "Our Story" → `.u-type-super` 64px quote → `.o-scripture__reference` (flex, gap 32, `margin-top: 36px`, opacity .8): 16px black dot + `.u-type-h2` "Habakkuk 3:2".
7. Two `_60` spacers (120px). **2-col text** `.c-2col-text__row` flex: `<p data-gap-size="large">` in two CSS columns (75% width, gap 150px) + `.c-2col-text__button` (25%, text-align right) "About Us →".
8. `_60`. **Section head "Upcoming Citywide Events"** (no badge) + small body "Click on the events below for more information." + "View All Events →".
9. **Events image carousel** (`.c-image-carousel.home-events`, section `overflow--hidden`): Splide `type:'loop', perPage:1, autoplay:true, interval:7000, speed:1000, easing:'cubic-bezier(0.25, 1, 0.5, 1)', arrows:false, pagination:false, snap:true`. Track is `width: 62.5%` centred with `overflow: visible`, slides `margin-right: 24px`, so previous/next slides peek on both sides edge-to-edge. Each slide: `.o-image[data-aspect-ratio="ar16x9"]` radius 12, whole image is a link (several open in new tabs). 4 CMS items.
10. `_60`. **"Our Pursuits" band** `section.l-section[data-overflow-above="true"]`: `margin-top: -400px; z-index: -1` (−200 ≤991, −100 ≤641) with an empty `.l-section__overflow-top` of matching height, so the faded background photo slides up **behind** the carousel above and the dark band appears to emerge from under it. Content `.c-story__wrapper { margin: 80px 0 }`: `.o-badge.light` "Our Pursuits", `.c-values__mission` (`.u-type-h3`, `width: 50%; margin-top: 52px`), `.c-values__list` grid `repeat(4,1fr)` (`margin-top: 72px`; 2 cols ≤991; 1 col ≤479): 48px circle line icon (arrow up / down / in / out), 40px two-tone title ("Presence / of God", "Formation / of People", "Unity / of the Church", "Flourishing / of the City"), body copy.
11. **Ministries card carousel** (`#splide-ministries`, section `overflow--hidden`): `.c-card-carousel__header` grid `1fr 1fr`, `margin-bottom: 24px`: `.u-type-h1` "Ministries" left, custom 48px circular arrows right (`.splide__arrows` justify end; arrows are SVGs rotated ±90°). Splide options `arrows:true, snap:true, pagination:false` (default speed 400ms). 14 CMS cards, `flex: 1 0 440px` (320px ≤991, 90% ≤479), gap 24, track `overflow: visible`, `.splide` `margin-left: 20px; padding-left: 10px`.
12. **Footer** (section 4 of this doc lists anatomy; see section 9 for the "sheet" trick).

### Mobile (360px)
- Nav collapses to logo monogram "COTC" (115×38) + search + "Menu" pill; desktop links hidden (`.c-nav__links { display:none }` ≤991).
- Hero still 65vh+, h1 28px wraps to two lines, buttons stack full width (`.l-button-row` wraps).
- Grid → single column; location card padding 16px, image 16:9.
- Values 1 column; footer 1 column; bottom row centered.

---

## 5. Navigation & header behavior

### Markup / structure
```
div.c-nav.static.w-nav[data-collapse="all"][data-animation="over-right"][data-duration="0"][data-no-scroll="1"]  (position: sticky; top:0; z-index:100; margin-bottom:-58px)
  .l-container
    .c-nav__wrap                 ← the pill
      .c-nav__area  a.c-nav__logo.desktop > .o-logo-lottie (300×38 Lottie)  |  a.c-nav__logo.mobile (115×38)
      .c-nav__area.links  .c-nav__links  a.c-nav__link ×5: Watch · Locations · Give · About Us · Upcoming Events
      .c-nav__area  form.o-search (24px mask-icon button) + .c-nav__menu > .c-nav__menu-button "Menu"
  .c-annc-bar (CMS list, optional)
  nav.c-nav__dropdown.w-nav-menu   ← full-screen overlay menu
```
- Pill: `display:flex; justify-content:space-between; align-items:center; padding:6px; gap:24px; border-radius:6px; background:#ffffffe6; border:1px solid #7b7b7b33; backdrop-filter: blur(7px); transition: background-color .2s`. Logo gets `padding-left: 20px` when current.
- Menu button: `background:#fff; border-radius:6px; padding:4px 20px; transition: background-color .2s, color .2s;` hover → `background:#000; color:#ececec`; `.w--open` → dark bg, light text.

### Transparent-at-top → frosted-on-scroll
Inline script:
```js
const navHeight = 58 + 20;                       // pill height + 20px tolerance
$(document).on('scroll', () => {
  if (window.pageYOffset > navHeight && $nav.hasClass('static')) { $nav.removeClass('static'); return; }
  if (window.pageYOffset === 0) { $nav.addClass('static'); }
});
```
`.c-nav.static` (only at scrollY 0): `.c-nav__wrap { background: transparent; backdrop-filter: none; border: none }`, `.c-nav__logo { filter: invert(1) }` (black Lottie → white), `.c-nav__menu-button { background: transparent; border: 1px solid rgba(255,255,255,.5) }`, `.c-nav.static { color: #ececec }`, announcement bar also goes transparent with light text and its button flips to light. Only `background-color` is transitioned (.2s); border and blur snap. The nav's negative margin is recomputed on load/resize: `$nav.css('marginBottom', -$nav.outerHeight() + 'px')`.

### Scroll-scrubbed Lottie logo
IX2 action list "Logo Scroll Transition": event `PAGE_SCROLL` / `GENERAL_CONTINUOUS_ACTION`, `continuousParameterGroups[type:"SCROLL_PROGRESS"]`, `smoothing: 51`, keyframe `0` → Lottie `value: 0`, keyframe `7` → `value: 100` (easing `[.25,.25,.75,.75]`, nominal duration 500). I.e. in the first **7 % of page scroll** the logo animation plays start→end and scrubs back on scroll-up. Lottie file `COTC Logos.lottie`, viewBox `1024×130`, `data-loop="0" data-autoplay="0" renderer svg`. **(inference)** The animation morphs the full "CHURCH OF THE CITY" wordmark into the "COTC" monogram seen in the mobile screenshot. The same action list is duplicated per page (a-23 … a-27).

### Full-screen menu overlay
- Webflow nav with `data-collapse="all"` → the "Menu" button is used at **every** width (desktop keeps 5 inline links as shortcuts). `data-duration="0"` → opens **instantly**, no slide; `data-no-scroll` locks body scroll.
- `.c-nav__dropdown { position:fixed; inset:0 auto auto 0; width:100%; max-height:100dvh; overflow:auto; background:#000000e6; backdrop-filter: blur(10px); color:#ececec; padding-bottom:100px; z-index:100 }`.
- Top row replicates the pill in `.open` state: transparent, `border-bottom: 1px solid #fff3`, `border-radius:0; padding-bottom:20px`; left shows text "Church of the City", right "Close Menu" + 16px X.
- `.c-nav__dropdown-layout { display:grid; grid-template-columns: 4fr 8fr; gap: 40px 24px; margin-top:60px }` (1 column ≤991).
  - Left: 5 large links (48px Inter Display, 40px arrow icon, gap 40): **Plan a Visit · Watch Online · Give · Events · The Village**.
  - Right: grid `1fr 1fr 1fr` of columns `headline (28px) + links (opacity .75, gap 8px)`: About (Vision & Beliefs, The Village, Our Staff, Elders) · Watch (Messages, COTC Daily) · Get Involved (Upcoming Events, Community Groups, Volunteer, Become a Stakeholder, Baptism) · Ministries (CMS) · Care & Support (CMS: Prayer, Volunteer, Wrap Around, Cars, Marriage, Pastoral Care) · Resources (Missional Partners, Reading Plan, Parents, Join Our Team).
  - Below an `hr`: **Locations** with address, Email, phone for each campus.
- Search: clicking the mask-icon button runs IX2 "Nav Search Open": `.o-search__input-wrap` (absolute, `top:100%`, white, radius 12, `height:0; overflow:hidden`) → `height: 66px` over **300ms `inOutCubic`**; second click → 0 over 300ms.

### Announcement bar
- `.c-annc-bar` under the pill, `padding: 0 48px`; `.c-annc-bar__wrap { background:#ffffffe6; border:1px solid #7b7b7b33; border-top:0; border-radius: 0 0 6px 6px; padding:10px; backdrop-filter: blur(7px); transition: background-color .2s }`; item = 120px 3:2 image + text column + actions (button + icon-only close).
- Dismissal persisted: `localStorage['anncBannerDismissed:' + slugify(title)] = '1'`, keyed by the announcement title so a new announcement re-appears.

---

## 6. Hero treatment

```
section.l-section
  div.l-section__background.w-background-video[data-autoplay][data-loop][data-poster-url][data-video-urls]
    video[autoplay loop muted playsinline style="background-image:url(poster.jpg)" data-object-fit="cover"]
      source .mp4 · source .webm
  .l-container
    .c-hero[data-min-height="vh85"]          (min-height 85vh; 65vh ≤991; flex column; justify-content:flex-end; color:#ececec)
      .c-hero__nav-spacer                     (height: var(--size--nav-spacer) = 100px)
      .c-hero__content                        (grid 1fr 1fr; align-items:end; padding-top:100px)  → 1fr ≤991
        .c-hero__content-gradient             (absolute, width:100vw, top:-100px→bottom, z-index:-1,
                                               linear-gradient(0deg,#00000026,#00000026 85%,#0000))
        .c-hero__content-inner                (flex column; gap 24; align-items:flex-start)
          h1.u-type-h1  "Practicing the Way of Jesus."
          .u-type-body  "Church of the City is a nondenominational church in Nashville, Franklin, Spring Hill, and Nolensville, TN."
          .l-button-row (flex wrap gap 10)
            a.o-button.light        "Join us in person →"
            a.o-button.transparent  "▶ Join us online →"
          .l-spacer._60
```
- `.l-section__background { position:absolute; width:100%; height:100%; object-fit:cover; object-position:50% 0%; z-index:-1; pointer-events:none; transition: opacity .5s linear }`.
- Text occupies the **left half** of the grid and is pinned to the **bottom** of the 85vh box — the top two-thirds of the video are left clean (the transparent nav sits over it).
- Hero variants in CSS: `[data-min-height]` = `vh85 | vh55 | 900 | 600 | 400`; `.c-hero.video { min-height: 56.25vw }` (true 16:9); `.c-hero.large` 85vh.
- `.c-hero__popup` glass card (used on Watch/location heroes **(inference)**): `position:absolute; right:30px; bottom:30px; width:460px; padding:32px 42px; background:#0000004d; border:1px solid #fff3; border-radius:12px; backdrop-filter: blur(15px)`; full width ≤991.
- Watch page hero: `.c-hero__content-cards` flex row of 3 campus cards (`flex: 30%`), each with badge, message title, "▶ Play Video"; `.c-hero__content-card.live.show` swaps in "Franklin is Live Now / Live at: 8am, 9:45am, 11:30am / Watch Live" with `.o-button-play { color: #ec2b2b }`.
- Secondary heroes are **image** backgrounds (AVIF) with an eyebrow badge ("About", "Ministry", "Messages"), h1, and an info row of small `###` columns (Contact / Location / Service Times / Campus / Sundays) followed by a paragraph.

---

## 7. Video usage

| Where | Implementation | Attributes |
|---|---|---|
| Homepage hero | Webflow background video component, `CW_WebBanner_2026Edit` | `autoplay loop muted playsinline`, poster via inline `background-image`, `.mp4` + `.webm`, `object-fit: cover`, no controls, **no pause button, no `prefers-reduced-motion` fallback** |
| Latest message / message cards | `.o-video` click-to-load placeholder: 16:9, radius 12, poster `<img>` + 130px centered play button (`pointer-events:none`), `.o-video__placeholder { cursor:pointer; inset:0 }`; on click JS sets the sibling iframe `src` | Vimeo: `player.vimeo.com/video/{id}?title=0&byline=0&portrait=0&autoplay=1&autopause=0`; YouTube: `youtube.com/embed/{id}?modestbranding=1&rel=0&showinfo=0&color=white&enablejsapi=1&autoplay=1&autopause=0`. IX2 "Placeholder Click": wait 500ms → opacity 0 over 500ms → `display:none`. No iframe is loaded until click (performance). |
| Live services | Links out to `youtube.com/@COTCFranklin/live` etc.; "Live Now" cards toggled by schedule script | `data-element-show-at="Sun: 8am, 9:45am, 11:30am"` (bare times default to Sunday; `|` separates days). Shows from **10 min before** to **90 min after** each start, computed in `America/Chicago`, re-armed with `setTimeout` for the next slot. Variants `data-element-hide-at`, `data-parent-show-at`. |
| Text-image component | `[data-vimeo-id] [data-youtube-id]` on `.c-text-image__image`; image fallback shown when both empty | |
| Video cards | `.o-video-card__image` 16:9 radius 12 with duration chip `.o-video-card__image-duration { background:#000000e6; color:#ececec; border-radius:7px; padding:4px 8px; font-weight:500; position:absolute; right:5px; bottom:5px }` | |
| Latest-video tile | `.o-video-latest { aspect-ratio: 1440/720 }` → 3/2 → 1 → 2/3 as viewport shrinks, content max-width 460px bottom-left | |

Hero video poster is a JPG frame of the clip, so first paint matches the first frame.

---

## 8. Animations & transitions

Overall posture: **quiet**. No scroll-reveal, no parallax, no text splitting, no page transitions. Motion is reserved for (a) the header's response to scroll, (b) carousels, (c) hover zoom on images, (d) disclosure widgets. Complete inventory:

| # | What moves | Trigger | Duration | Easing | Mechanism |
|---|---|---|---|---|---|
| 1 | Nav pill background transparent → `#ffffffe6` (and announcement bar) | scrollY > 78px (class toggle) / back to 0 | `.2s` | default `ease` | CSS `transition: background-color .2s` on `.c-nav__wrap`; blur/border snap |
| 2 | Logo Lottie frame 0→100 (wordmark → monogram **(inference)**) | page scroll progress 0 % → 7 % | scrubbed; `smoothing: 51` | `[.25,.25,.75,.75]` (linear) | Webflow IX2 `PAGE_SCROLL` continuous + Lottie plugin |
| 3 | Menu button bg/color invert | hover | `.2s` | ease | CSS |
| 4 | Image zoom `transform: scale(1.1)` | hover on `.o-image__img` (event carousel images, text-image blocks) | **`.8s`** | `cubic-bezier(.515, .012, .316, 1.001)` (≈ ease-out-quint) | CSS, parent `overflow:hidden` radius 12 |
| 5 | Events carousel slide | autoplay every **7000ms**, drag, snap | **1000ms** | `cubic-bezier(0.25, 1, 0.5, 1)` (ease-out-quart) | Splide `type:'loop'` |
| 6 | Ministries carousel slide | arrow click / drag | Splide default 400ms | Splide default `cubic-bezier(.25,.1,.25,1)` | Splide `snap:true` |
| 7 | Accordion (FAQ) open | click trigger (Webflow dropdown) | **1s** | `cubic-bezier(.526, .012, .456, .995)` | CSS `max-height: 0 → 100vh` on `.o-accordion-item__content` |
| 8 | Accordion plus → minus | same | `.2s` | `cubic-bezier(.77, 0, .175, 1)` | `.o-accordion-item__trigger-icon-vert { transform: scaleY(0) }` when `.w--open` |
| 9 | Search field reveal | click / second click | **300ms** | `inOutCubic` | IX2 `STYLE_SIZE` height 0 ↔ 66px |
| 10 | Video placeholder dismiss | click | 500ms delay + 500ms fade, then `display:none` | default | IX2 `STYLE_OPACITY` + `GENERAL_DISPLAY` |
| 11 | Section background image fade | load **(inference)** | `.5s` | linear | `.l-section__background { transition: opacity .5s linear }` |
| 12 | Menu overlay open/close | click | **0ms** (instant) | — | Webflow nav `data-duration="0"` |
| 13 | Tabs underline / filter chips | hover | none declared (instant) | — | CSS |
| 14 | `@keyframes spin` | — | — | — | Webflow's built-in loader, unused |

Other facts:
- There is **no `prefers-reduced-motion`** rule in the stylesheet and no JS check; autoplaying hero video and carousel autoplay run for everyone.
- `.o-button` has **no hover or active style** at all; only the nav "Menu" button and tabs respond to hover. The arrow icon does not move.
- Easing vocabulary: everything custom is a long, soft **ease-out** (≥ .8s for image zoom, 1s for accordion), while utility state changes are short (.2–.3s). This "slow for content, fast for chrome" split is the thing to copy.
- An IX2 action list titled "Sticky Nav Slide Down" exists but is empty (abandoned).

---

## 9. Interaction patterns

### Buttons `.o-button`
```css
.o-button { display:inline-flex; align-items:center; justify-content:center; gap:10px;
  padding:17px 30px; border-radius:12px; line-height:1em; text-decoration:none;
  background:#000000e6; color:#ececec; border:1px solid #ffffff1a;
  backdrop-filter: blur(7.5px); box-shadow: inset 0 -2px 8px 1px #ffffff26; }
.o-button__label { font-size:16px; white-space:nowrap; }   .o-icon { width:20px; aspect-ratio:1 }
.o-button.light        { background:#ffffffe6; color:#252525; }           /* primary on dark/video */
.o-button.transparent  { background:#ffffff26; color:#ececec; }           /* glass secondary on video */
.o-button.small-outlined { border-radius:5px; background:transparent; border-color:#000; color:#000;
                           padding:6px 8px; font-size:14px; justify-content:space-between; }  /* card "More Info" */
.o-button.border-black { background:transparent; border:1px solid #252525; color:#252525 }
.o-button.icon-only    { padding-left:17px; padding-right:17px }
```
- Every CTA ends with a 20px **arrow →** icon; video CTAs also start with a ▶ icon. Labels are short verbs: "Join us in person", "Join us online", "Watch Online", "More Info", "About Us", "View All Events", "Sign up form", "Give", "Play Video", "Watch Live", "Email Us", "Apply Here".
- Play button `.o-button-play__circle`: 70px circle, `#ffffff26`, blur 15, same inner rim; label beside it.

### Badges / eyebrows
- `.o-badge { display:inline-block; font-size:14px; line-height:1em; padding:4px 8px; border:1px solid #000; border-radius:5px; color:#252525; opacity:.25 }` — eyebrow labels "Locations", "Our Story", "Our Pursuits", "Ministry", "Messages". `.light { border-color:#ececec; color:#ececec; opacity:.6 }`, `.messages { opacity:1; background:#ffffff4d }`, `.live { color:#ec2b2b; background:#fff; border:0; opacity:1 }`.
- `.o-location-badge { display:flex; gap:10px; align-items:center; padding:2px 6px; border:1px solid #252525; border-radius:5px; font-size:14px; line-height:1em }` with `.o-location-badge__bullet` 10px filled circle; `.light` variant on dark cards. Used as campus chips on ministry cards.

### Cards
- **Location card** `.o-location-card`: white, radius 16, `padding:24px` (16 ≤479), `box-shadow: 0 4px 20px #0000001a`, flex column `justify-content: space-between; height:100%`. Head grid `2fr 1fr`: left = `24px dot + h2.u-type-h3 name` and address (`#828282`, 16px); right = times (`#828282`, 14px, right-aligned) and `.o-button.small-outlined` "More Info →" bottom-right (`margin-top:auto`). Image last, radius 12, 439px tall.
- **Ministry card** `.c-card-carousel__card`: `aspect-ratio:2/3; flex:1 0 440px; border-radius:16px; padding:28px 24px; display:flex; flex-flow:column; justify-content:flex-end; overflow:hidden; color:#ececec; border:1px solid transparent`. Two absolutely positioned background images (plain + blurred/masked scrim). `.c-card-carousel__card-content { z-index:2; gap:24 }` = h3 title + wrapped campus chips (gap 10). `a.c-card-carousel__card-link { position:absolute; inset:0; z-index:3 }` makes the entire card clickable (empty anchor — see a11y).
- **Video card**: 16:9 image + duration chip + text below (gap 16).
- **Info cards** `.c-info-cards`: 3-col grid, gap 80/100px, used for "Volunteer & More Info" blocks (h1-size titles + paragraph + button).

### Carousels (Splide)
- Tracks use `overflow: visible` so neighbours peek; sections wrap with `.overflow--hidden` to stop horizontal page scroll.
- Events: track 62.5% (75% ≤991) of container, centered; loop; autoplay 7s; drag.
- Ministries: left-aligned, cards fixed basis, custom arrow buttons in the header (`.splide__arrow { width:48px; height:48px; background:transparent; position:static; transform:none }` — a 48px circle outline SVG rotated ±90°).
- Events hero (`/events`): `.c-events-hero__slide { flex:1 0 100%; margin-right:6px; min-height: calc(1480px / 2) = 740px; border-radius:10px; padding: 100px 30px 60px; justify-content:flex-end }`, gradient `linear-gradient(0deg,#00000040,#00000026 85%,#0000)`, content `width:50%`.
- Watch "latest" strip: `.o-watch-latest__item { flex: 0 0 360px }`.

### Accordion (FAQ "What to Expect", "Frequently Asked Questions")
- Trigger full-width, `padding-bottom: 36px`, title + 48px white circle (32px ≤479) containing a 2px plus made of two bars; vertical bar `scaleY(0)` when open.
- Content `width: 50%` (75% ≤991, 100% ≤767), `max-height 0 → 100vh` over 1s; item `padding-bottom: 24px; overflow:hidden`.

### Tabs
- `.l-tabs__tab:hover { border-bottom: 1px solid #252525 }` — underline tabs for "Grid View / Calendar View" and "Choose a Campus".

### Dot motif
Filled `#252525` circles recur as a brand device: 24px beside each location name, 16px before the scripture reference, 40px at the footer top-left, 10px inside campus chips, 48px icon rings. Reuse: one `.dot` class with size modifiers.

### Footer "sheet" edge
`.c-footer__page-end { height:30px; margin-top:20px; border-radius: 0 0 12px 12px; box-shadow: 0 0 14px #0000001a; position:relative }` + `.c-footer__page-end-top { position:absolute; top:-20px; height:30px; width:100%; background:#fafafa }`: the page canvas appears to end as a rounded card floating 20px above the footer (both are `#fafafa`, separated only by the shadow). Footer container `padding: 0 60px` (20px ≤991). Rows: top `padding:60px 0` (40px dot + h2 brand) → hr → middle grid `1fr 1fr`, `padding:80px 0` ("Stay up to date with COTC." h2 + "Sign up form →" | 3 link columns, links `#828282` 16px gap 10) → hr → bottom grid `2fr 8fr 2fr`, `padding:80px 0 60px` (© left, 32px circular social icons right).

---

## 10. Content & CTA strategy

- **Visitor-first hero**: the h1 is the mission line, not "Welcome"; the one-sentence descriptor names denomination status and all four cities (orientation + SEO). Exactly two CTAs, phrased as invitations in parallel: **"Join us in person"** (→ /visit) and **"Join us online"** (→ /watch). "Give" is deliberately absent from the hero.
- **Primary nav = five visitor jobs**: Watch · Locations · Give · About Us · Upcoming Events. Menu's five large links re-rank them: Plan a Visit · Watch Online · Give · Events · The Village (their campus/community project).
- **Homepage order** = Where (locations with times) → Why (scripture + founding story + About) → When (events) → What we value (4 pursuits) → How to plug in (ministries) → Stay connected (newsletter). Service times appear on the homepage inside each location card ("8am, 9:45am, 11:30am").
- **Multi-site pattern**: every location page shares one template (hero → "Welcome to X" info columns → Latest Message → Upcoming Events filtered by campus → Ministries grid → "What to Expect" FAQ). Every ministry page has "Choose a Campus" tabs with per-campus sub-blocks and campus-filtered calendar.
- **Give**: short rationale ("We are grateful that God is moving you…"), tool explanation (Pushpay), then "**To give today, select a COTC location below.**" → location grid whose button is "Give" → external Pushpay URL per campus. Followed by Legacy/Estate + Non-Cash giving text-image block and a 5-question FAQ accordion (tax deductible? what is Pushpay? need an account? give assets? DAF/IRA?).
- **Watch**: per-campus latest message + live state in the hero; "Watch any service online" schedule table; location cards link to each campus YouTube channel ("Past Messages").
- **Events**: featured carousel hero (eyebrow + h2 + 1–2 sentence copy + CTA), then an embedded Planning Center calendar with Grid/Calendar tabs; location/ministry pages embed the same calendar pre-filtered.
- **Serve/Volunteer**: never a top-level hero CTA; surfaced in menu "Get Involved" and inside ministry pages as "Serve With Us → Apply Here" (Church Center forms).
- **Newsletter**: only in the footer ("Stay up to date with COTC." → "Sign up form"), plus Mailchimp lists on ministry pages.
- Tone: warm, plain, second person ("We look forward to serving your family!"); statement of faith content lives under About/Visit in long accordions, not on the homepage. "What to Expect" FAQs answer arrival, dress code, parking, students, kids, coffee.
- Every list of campuses includes address lines and service times inline; phone and email appear in the menu overlay and location pages.

---

## 11. Secondary page templates

| Page | Hero | Body blocks (in order) |
|---|---|---|
| `/visit` ("Plan a Visit") | Image hero, eyebrow "About", h1 "Welcome to COTC.", `### Contact` column, paragraph | hr → "Locations / Select a Location" section head → 4-card location grid (4th spans 3 cols at ≥769) → Village text-image (image left) → "Mission, Vision & Pursuits" long-form (three accordions: The Christian Life, What We Believe, Vision & Mission) → Our Pursuits band → footer |
| `/give` | Image hero, "About", h1 "Giving", Contact (phone + email), Pushpay paragraph | "Giving / Where would you like to give?" head → location grid with "Give" buttons → Legacy & Non-Cash text-image (two buttons) → FAQ accordion → Our Pursuits band → footer |
| `/watch` | Image hero, "Messages", h1 "Church of the City Messages", three campus message cards with live-state swap | "Messages / Live Schedule / Watch any service online" with three `### Campus` time columns → 3-card location grid ("Past Messages" → YouTube) → footer |
| `/events` | **Carousel hero** of 4 featured items (image bg, eyebrow, h2, copy, CTA) | "Upcoming / Events" head with Contact → tabs "Grid View | Calendar View" wrapping Planning Center iframes → footer |
| `/franklin` (location) | Image hero, h1 "Church of the City Franklin", descriptor, "Watch Latest Message" (YouTube live link) | "Locations / Welcome to Franklin" with `### Location / Service Times / Contact` + paragraph + "This Week's Announcements" (Linktree) → "Latest Message" text-image → "Upcoming Events" (calendar filtered `campus=88236`) → "Ministries" image grid → "What to Expect" FAQ accordion (7 Qs) → footer |
| `/ministry/kidcity` | Image hero, "Ministry", h1, `### Campus / Sundays / Contact` columns, paragraph | "Choose a Campus" tabs → per campus: text-image blocks (Sunday Services, City Friends, Toddlerock) with "Email Us" → "Volunteer & More Info" info cards (h1 titles: Serve With Us / Stay in Touch / Next Steps…) → "Upcoming Events" calendar filtered by campus+category → Our Pursuits band → footer |

Shared components across templates: `.c-section-head` (badge + h2 + right button), `.c-2col-text`, `.c-text-image` (grid `1fr 1fr`, gap 120px, `[data-layout-image="right"]` flips order at ≥992; subhead opacity .5; buttons row hidden unless it has children via `:has(:first-child)`), `.c-location-grid`, `.o-accordion-item`, `.c-info-cards`, "Our Pursuits" band, footer. Page-level `<style>` embeds tweak grid spans per page.

---

## 12. Accessibility notes

Positives
- One `h1` per page; headings follow the visual hierarchy (cards use `h2.u-type-h3`).
- Webflow nav emits `role="banner"`, `role="navigation"`, `aria-label="menu"`, `aria-controls`, `aria-haspopup`, `aria-expanded`; Splide emits `role="group"`, `aria-roledescription="slide"`, `aria-label="1 of 14"`, `aria-live="polite"`, arrows have `aria-label`.
- Buttons are ≥ 50px tall (17px padding + 16px text), good touch targets; `playsinline` + `muted` on video; `font-display: swap`.
- Live state is conveyed with text ("Franklin is Live Now"), not colour alone.

Problems
- **No `prefers-reduced-motion`** handling; autoplaying background video with no pause control; carousel autoplay.
- Body text drops to **12.8px** below 768px (`calc(16px * .8)`).
- Eyebrow `.o-badge` at `opacity: .25` → roughly 2:1 contrast; address/times in `#828282` on white ≈ 3.6:1 (fails AA for 14px times).
- All content images have `alt=""`, including meaningful ones (campus photos, ministry cards).
- Ministry card link is an **empty `<a>` overlay** with no text → announced as "link" with no name; event carousel links contain only an image with empty alt → same.
- Search trigger is a `<div class="o-search__button">` (mask-image icon) with no role, name or keyboard handler; "Menu" is a `div[role=button]` (Webflow default) — acceptable but not a `<button>`.
- No skip link and no `<main>` landmark.
- No `<meta name="description">` / OG tags on the homepage.
- Footer © reads 2024 while the site was published Nov 2026; links leak to the staging domain `cotc-f21faa.webflow.io`.
- Focus styles rely on browser defaults; Webflow's `.wf-force-outline-none[tabindex="-1"]:focus` only affects programmatic focus.

---

## 13. Weaknesses to avoid

1. Reduced-motion and autoplay controls missing (above).
2. Mobile body size 12.8px; h2 at 21px vs h1 at 28px compresses hierarchy on phones.
3. Near-invisible eyebrow labels (opacity .25) — if you want quiet labels, keep ≥ 4.5:1 and lower *size*, not opacity.
4. Empty-anchor card overlays and `alt=""` everywhere — give overlay links visually-hidden text or wrap the title in the anchor.
5. No hover/pressed/focus feedback on primary buttons — the arrow could translate 2–4px or the glass could brighten.
6. Font payload: 18 static Inter Display files declared when a single variable file would do (`InterVariable` is already loaded for body).
7. Two DOM libraries (jQuery + cash.js) and ~537 KB of Webflow JS for ~4 interactions.
8. Hardcoded nav height (`58 + 20`) in JS and a hardcoded `margin-bottom: -58px` in CSS; fragile when the announcement bar is present (JS recalculates, CSS does not).
9. Staging-domain links and stale © year — content hygiene.
10. Hero contrast depends on dark footage because the scrim is only 15% black; a lighter clip would break legibility.
11. Instant (0ms) menu open feels abrupt next to the otherwise soft motion; a 250–300ms fade would match the system.
12. Section eyebrow + h2 + button head pattern leaves the button vertically misaligned with the headline when the headline wraps (`align-items: start`).

---

## 14. Reusable patterns (codeable rules)

### 14.1 Tokens
```css
:root{
  --canvas:#fafafa; --ink:#252525; --ink-light:#ececec; --grey:#828282; --grey-light:#eaeaea; --live:#ec2b2b;
  --btn-dark:rgba(0,0,0,.9); --btn-light:rgba(255,255,255,.9); --glass:rgba(255,255,255,.15); --glass-border:rgba(255,255,255,.1);
  --r:12px; --r-sm:5px; --r-lg:16px; --gutter:24px; --container:1480px; --nav-spacer:100px;
  --font-body:"Inter",sans-serif; --font-display:"Inter Display",sans-serif;
  --h1:40px; --h2:28px; --h3:22px; --body:16px; --badge:14px; --super:64px;
  --ease-out-soft:cubic-bezier(.515,.012,.316,1.001); --ease-out-quart:cubic-bezier(.25,1,.5,1);
  --ease-accordion:cubic-bezier(.526,.012,.456,.995); --ease-snap:cubic-bezier(.77,0,.175,1);
}
body{background:var(--canvas);color:var(--ink);font:400 var(--body)/1.4 var(--font-body)}
```

### 14.2 Type rules
- Headings ≤ 40px: display family, **700**, line-height 1.0–1.2, no tracking, sentence case, trailing period on statements.
- Display moments ≥ 40px (pull quote, menu links, value words): **400**, line-height 1.05–1.1, tracking −0.02em at 64px.
- Two-tone headline: `<p class="t-40"><strong>Presence</strong><br>of God</p>` with `strong{color:#fff}` and `p{color:rgba(255,255,255,.6)}`.
- Eyebrows are 14px bordered chips (`padding:4px 8px; border:1px solid currentColor; border-radius:5px`), never uppercase tracked text.
- Mobile: scale h1 ×.7, h2 ×.75, h3 ×.8, but keep body ≥ 16px (fix their mistake).

### 14.3 Frosted glass button
```css
.btn{display:inline-flex;gap:10px;align-items:center;padding:17px 30px;border-radius:var(--r);line-height:1;
  background:var(--btn-dark);color:var(--ink-light);border:1px solid var(--glass-border);
  backdrop-filter:blur(7.5px);box-shadow:inset 0 -2px 8px 1px rgba(255,255,255,.15)}
.btn--light{background:var(--btn-light);color:var(--ink)}
.btn--glass{background:var(--glass)}
.btn--outline-sm{background:none;border:1px solid var(--ink);color:var(--ink);border-radius:var(--r-sm);padding:6px 8px;font-size:14px;justify-content:space-between}
.btn svg{width:20px;aspect-ratio:1}   /* always trailing arrow; leading play icon for video */
```

### 14.4 Sticky pill nav that is transparent at top
- `header{position:sticky;top:0;z-index:100;margin-bottom:calc(-1 * var(--nav-h))}` so the hero slides underneath; set `--nav-h` from JS on load/resize.
- Pill: `display:flex;justify-content:space-between;align-items:center;padding:6px;border-radius:6px;background:rgba(255,255,255,.9);border:1px solid rgba(123,123,123,.2);backdrop-filter:blur(7px);transition:background-color .2s,border-color .2s`.
- Toggle `.is-top` when `scrollY===0`; remove when `scrollY > navHeight + 20`. `.is-top` → transparent pill, light text, `filter:invert(1)` on a black logo, outlined menu button `border:1px solid rgba(255,255,255,.5)`.
- Keep 5 inline links on desktop **and** a "Menu" button everywhere that opens a full-screen `rgba(0,0,0,.9) + blur(10px)` overlay: left column of 4–5 giant links (48px, arrow icons), right 3-column link lists (28px heads, 16px links at .75 opacity), locations with contact info at the bottom. Lock body scroll; make the overlay `max-height:100dvh; overflow:auto`.
- Optional: scrub a logo Lottie over the first 7% of scroll (`scroll progress 0→0.07 → frame 0→100`, smoothing ~0.5).

### 14.5 Video hero
- `section{position:relative}` + `video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-1;pointer-events:none}` with `autoplay muted loop playsinline poster`, `.webm` then `.mp4`.
- Content box `min-height:85vh` (65vh < 992px), `display:flex;flex-direction:column;justify-content:flex-end`, top spacer = nav height (100px), inner grid `1fr 1fr` so copy stays in the left half; 60px bottom spacer.
- Scrim: `linear-gradient(0deg, rgba(0,0,0,.15), rgba(0,0,0,.15) 85%, transparent)` stretched `100vw` and `top:-100px`. Increase to .35 if footage is bright.
- Exactly two CTAs: light primary ("Join us in person →") + glass secondary ("▶ Join us online →").
- Add what they lack: `@media (prefers-reduced-motion: reduce){video{display:none}}` and show the poster; provide a pause button.

### 14.6 Section head
`.sec-head{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start;margin-top:24px}` preceded by an eyebrow chip; headline left, button right (`justify-self:end`). Collapse to one column < 992px. Follow with 48px of space (two 24px spacers).

### 14.7 Two-column prose
`p.cols{column-count:2;column-gap:75px /* or 150px */;flex:0 0 75%}` + a 25% right-aligned button column; `column-count:1` < 768px.

### 14.8 Peeking carousel (Splide)
- Events: `{type:'loop',perPage:1,autoplay:true,interval:7000,speed:1000,easing:'cubic-bezier(0.25,1,0.5,1)',arrows:false,pagination:false,snap:true}`; `.splide__track{width:62.5%;margin:0 auto;overflow:visible}`; slides `margin-right:24px`; wrap section `overflow:hidden`.
- Cards: `{arrows:true,pagination:false,snap:true}`; slides `flex:1 0 440px` (320px < 992, 90% < 480); arrows are 48px outlined circles placed in the header, not over the slides.
- Image hover: `img{transition:transform .8s var(--ease-out-soft)} a:hover img{transform:scale(1.1)}` inside `overflow:hidden;border-radius:12px`.

### 14.9 Portrait card with blurred-duplicate scrim
```html
<article class="card"><img src=x class="bg"><img src=x class="bg bg--blur" aria-hidden="true">
  <div class="content"><h3>KidCity</h3><ul class="chips">…</ul></div><a href=… class="cover"><span class="sr-only">KidCity</span></a></article>
```
```css
.card{position:relative;aspect-ratio:2/3;border-radius:16px;overflow:hidden;display:flex;flex-direction:column;justify-content:flex-end;padding:28px 24px;color:#ececec}
.bg{position:absolute;inset:0 -50px -50px;min-width:calc(100% + 100px);min-height:calc(100% + 50px);object-fit:cover}
.bg--blur{filter:brightness(25%) blur(50px);-webkit-mask-image:linear-gradient(0deg,#000 5%,transparent 70% 80%);mask-image:linear-gradient(0deg,#000 5%,transparent 70% 80%)}
.content{position:relative;z-index:2}.cover{position:absolute;inset:0;z-index:3}
```

### 14.10 White info card (location)
`background:#fff;border-radius:16px;padding:24px;box-shadow:0 4px 20px rgba(0,0,0,.1);display:flex;flex-direction:column;justify-content:space-between;height:100%`; head grid `2fr 1fr` (dot 24px + name 22px/700; address grey 16px | times grey 14px right; small outlined "More Info →" bottom-right); image radius 12, 439px (or `aspect-ratio:2.39` → `16/9`).

### 14.11 Dark band that emerges from under the section above
```css
.band{position:relative;z-index:-1;margin-top:-400px;color:#ececec}   /* -200 <992, -100 <641 */
.band::before{content:"";display:block;height:400px}                   /* same steps */
.band>img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 0;z-index:-1}
```
Use a background image that already fades to the canvas colour at its top (or add `mask-image: linear-gradient(to bottom, transparent, #000 400px)`). Inside: eyebrow (light chip at .6), one-sentence mission at 22px in a 50% column, then a 4-up grid (`margin-top:72px`) of 48px ring icon + 40px two-tone word + 16px copy; 80px vertical padding.

### 14.12 Scripture / pull-quote block
Eyebrow chip → quote in body family at 64px/1.1/400 with −0.02em tracking (40px < 992) → reference row (`margin-top:36px; opacity:.8; display:flex; gap:32px; align-items:center`) with a 16px filled dot and the reference at 28px/700.

### 14.13 Accordion
Trigger: full-width flex `space-between`, title + 48px white circle with a 2px plus; `.is-open .v{transform:scaleY(0);transition:transform .2s var(--ease-snap)}`. Panel: `max-height:0;overflow:hidden;transition:max-height 1s var(--ease-accordion)` → `max-height:100vh`; panel width 50% on desktop.

### 14.14 Click-to-load video
Poster `<img>` + 130px play glyph, `aspect-ratio:16/9;border-radius:12px;overflow:hidden`; on click set iframe `src` (YouTube `?modestbranding=1&rel=0&color=white&enablejsapi=1&autoplay=1`; Vimeo `?title=0&byline=0&portrait=0&autoplay=1`), then fade the placeholder out over 500ms after a 500ms delay and remove it.

### 14.15 Live-now scheduling attribute
`data-show-at="Sun: 9am, 11am | Wed: 6:30pm"` → show the element from 10 min before to 90 min after each start, in the church's timezone, re-evaluating with a timer; pair with a red `#ec2b2b` "Live" chip and "Watch Live" button.

### 14.16 Dismissible announcement bar
Render under the pill (`border-radius:0 0 6px 6px; border-top:0`, same glass as the pill); store `anncBannerDismissed:<slugified-title>` in `localStorage` so a new message re-appears.

### 14.17 Footer "sheet"
Give the page canvas a rounded bottom edge floating over the footer: a 30px strip with `border-radius:0 0 12px 12px; box-shadow:0 0 14px rgba(0,0,0,.1)` and an absolutely positioned canvas-coloured cover 20px above. Then: 40px dot + brand h2 (60px padding) / hr / newsletter h2 + button | three link columns (80px padding) / hr / © + 32px circular social icons.

### 14.18 Motion budget (what to copy)
- Chrome state changes: **.2–.3s**, default ease or inOutCubic.
- Content motion (image zoom, slide, accordion): **.8–1s**, strong ease-out.
- Carousel autoplay: **7s** dwell, **1s** travel.
- Scroll-linked: only one element (logo), finished within the first 7% of the page, smoothed.
- Nothing fades in on scroll; sections are static. Add `prefers-reduced-motion` guards to everything above.
