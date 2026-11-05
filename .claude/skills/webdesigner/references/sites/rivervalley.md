# River Valley Church (rivervalley.org) — design teardown

Researched 2026-11-04. Sources: Firecrawl scrape of the homepage (rendered HTML, raw HTML,
links, 1920x1080 screenshot), the two first-party Webflow stylesheets
(`rivervalleychurch.webflow.shared.0e753df24.min.css`, 34 KB and
`rivervalleychurch.webflow.6696de90740e44393c25e790.02c4b2f49.opt.min.css`, 57 KB), the
Webflow JS chunks (IX2 interaction definitions live in `webflow.schunk.f5cb2a42e331bc47.js`),
and markdown scrapes of `/connect/visit`, `/impact/give`, `/watch-listen`,
`/locations/apple-valley`. Working copies are in

Every value below marked **(measured)** was read from CSS/JS/HTML. Items marked
**(inference)** are my reading of intent and were not directly observable.

---

## 1. Platform & stack

| Layer | What they use | Evidence |
|---|---|---|
| CMS / host | **Webflow** (site id `6696de90740e44393c25e78f`), published Nov 2 2026 | `data-wf-site`, `cdn.prod.website-files.com`, `<!-- Last Published -->` comment |
| CSS framework | Webflow's **Client-First** naming (`padding-global`, `container-large`, `text-style-eyebrow`, `spacer-small`, `heading-style-h3`, `button is-secondary`) plus Relume-style section ids (`cta70_component`, `cta39_card-content-top`, `layout133`, `stats26`) | class names throughout |
| Interactions | **Webflow IX2** (native interactions engine, `w-mod-ix` on `<html>`, `data-w-id` hooks, 234 `SCROLL_INTO_VIEW` triggers, 93 `MOUSE_CLICK`, 33 `MOUSE_OVER`/`MOUSE_OUT`) | `webflow.schunk.f5cb2a42e331bc47.js` |
| Carousels | **Swiper 10** from jsDelivr (`swiper-bundle.min.css/js`), initialised in inline scripts | `<link>` + inline `new Swiper(...)` |
| Video player (secondary pages) | **Plyr 3.5.6**, lazy-loaded only when a `.js-player` exists | inline "SKROL, Oct 2026" loader script |
| Search / app widgets | **Apollos embeds** `@apollosproject/apollos-embeds@0.2.45` (styled-components classes `sc-aXZVg`), lazy-loaded only when `.apollos-widget` exists | inline loader |
| Utilities | `@finsweet/attributes-scrolldisable@1`, jQuery 3.5.1 (Webflow default), WebFont loader 1.6.26 | script tags |
| Fonts | Google Fonts (Open Sans, loaded but **not used** in the visible UI), **Adobe Fonts / Typekit** kit `ddo4yrq` (Minion Pro family, Benton Modern Display, Realist, Ohno Fatface), and **self-hosted OTF/TTF** `@font-face` for Realist, Realist Wide, Alte Haas, Gin Jus, Bulletin Typewriter, Chromatic Condensed, Variera, Luminaire Script, Aileron | head + shared.css |
| Analytics / a11y | GTM `GTM-P2Q5GSQ5`, GA4 `G-TF99Y5XDKG`, Ahrefs analytics, **accessiBe** overlay (`acsbapp.com`, trigger colour `#146FF8`, bottom-right) | head scripts |
| Third-party destinations | Tithe.ly (giving forms per campus), Engiven (crypto), Planning Center Church Center (login, forms, groups, calendar), Shopify store, Managed Missions, online.church | links |
| Images | Mostly **AVIF** and WebP from the Webflow CDN, `loading="lazy"`, `alt=""` almost everywhere | `<img>` tags |
| Structured data | `schema.org/Church` JSON-LD with founders, foundingDate 1995, every campus as a `Place` | inline JSON-LD |

Performance note: the team wrote a custom loader (comment dated "Oct 2026") so Plyr and the
~1.4 MB Apollos bundle only load on pages that contain them. Worth copying as a principle:
gate heavy third-party scripts behind a `querySelector` check.

---

## 2. Typography

### Families (measured)

- **Body / UI:** `Realist, sans-serif` — self-hosted OTF, weights 300 (Light, also mapped to 400), 500 (Medium), 700 (Bold). A geometric grotesk with a slightly wide stance.
- **Display accents:** `Realist Wide, sans-serif` — 400 and 700. Used for the hero wordmark heading (`.home-hero_heading`), footer column headers (`.footer5_link-header`), and menu group headers (`.nav1_menu-link-heading`).
- Loaded but unused on the pages studied: Open Sans (Google), Minion Pro / Benton Modern Display / Ohno Fatface (Typekit), Alte Haas, Gin Jus, Bulletin Typewriter MN, Chromatic Condensed Pro, Variera, Luminaire Script, Aileron. **(inference)** these are campaign fonts for seasonal landing pages (Easter, Christmas, One Day, 21 Days) that share the stylesheet; the heavy font payload is a weakness, see section 13.
- `font-display: swap` on every self-hosted face; Typekit faces use `font-display: auto`.

### Base body (measured)

```css
body {
  font-family: Realist, sans-serif;
  font-size: 1.1rem;        /* 17.6px */
  font-weight: 500;         /* medium is the default body weight */
  line-height: 1.5;
  letter-spacing: .01em;
  color: var(--text-color--text-primary);   /* #231f20 */
  background: var(--base-color-brand--white);
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizelegibility;
}
```

### Heading scale (measured; all `margin: 0`, weight 700)

| Element | Desktop | <= 767px | line-height |
|---|---|---|---|
| h1 | 4rem (64px) | 2.5rem | 1.1 |
| h2 | 3rem (48px) | 2rem | 1.2 |
| h3 | 2rem (32px) | 1.5rem | 1.2 |
| h4 | 1.5rem | 1.25rem | 1.4 |
| h5 | 1.25rem | 1rem | 1.5 |
| h6 | 1rem | .875rem | 1.5 |

Utility overrides: `.heading-style-h1 { 2.5rem }`, `.heading-style-h2 { 2rem }`,
`.heading-style-h3 { 2rem; lh 1.2 }`, `.heading-style-h4 { 1rem }`, `.heading-style-h5 { .875rem }`,
`.heading-style-h6 { .75rem }`. Note these are *smaller* than the element defaults: the team
uses semantic tags for SEO and then dials size down with classes (e.g. location cards use
`<h2 class="heading-style-h3">`).

Campaign-only fluid sizes exist in the same sheet: `clamp(4rem, 22vw, 20rem)`,
`clamp(6rem, 8vw, 12rem)`, `clamp(10rem, 13vw, 16rem)`, `clamp(2rem, 18vw, 14rem)`,
`clamp(2.75rem, 14vw, 4rem)`. The core pages do **not** use fluid type; they step at breakpoints.

### Text styles (measured)

- **Eyebrow** `.text-style-eyebrow`: Realist 500, `.9rem`, `letter-spacing: .2em`, `text-transform: uppercase`. Variant `.is-text-shadow` adds `text-shadow: 0 1px 3px #87878780` for use over imagery. Often paired with `.text-color-secondary` (gold, weight 700).
- **Hero heading** `.home-hero_heading`: Realist Wide 700, `1.68rem` desktop, `2rem` at <= 991px, `5.5vw` at <= 479px, `letter-spacing: .175em`, uppercase. The site name is set as a small spaced wordmark, not a giant headline.
- **Nav links** `.nav1_link`: Realist 500, `1rem`, `letter-spacing: .2em`, uppercase.
- **Menu group header** `.nav1_menu-link-heading`: Realist Wide, `.875rem`, `.2em` tracking, uppercase, colour `#aba7a5`.
- **Menu links** `.nav1_menu-link`: `1.1rem` (1.2rem on mobile), weight **300**, `border-bottom: 2px solid transparent`.
- **Footer header** `.footer5_link-header`: Realist Wide 400, `.9rem`, `.2em` tracking, uppercase, gold.
- **Footer link** `.footer5_link`: `1.1rem`, 500.
- **Buttons**: Realist 500, inherit size (`.875rem` for `.is-small`), `letter-spacing: .1em`, uppercase.
- **Card CTA text** `.background-card_button`: `.9rem`, `.2em` tracking, uppercase, `text-shadow: 0 1px 3px #00000080`.
- **Card heading** `.background-card_heading`: h3 size with `text-shadow: 0 3px 10px #00000026`.
- **"SOAP" pill heading** `.soap-heading`: `1rem` (`.7rem` for `.is-small`), `.2em` tracking, uppercase, 500.
- **Lead paragraph** `.text-size-large`: `1.5rem` desktop, `1.25rem` mobile.
- **Service-time label** `.locations-card_heading`: `.875rem`, uppercase, 500, `#aba7a5`.
- Line clamps available: `.text-style-2lines`, `.text-style-3lines` (`-webkit-line-clamp`).

### Casing & tracking rule of thumb (inference from the above)

Anything that is a *label* (eyebrow, nav, button, column header, pill) is uppercase with
`.1em` to `.2em` tracking at 0.875rem to 1rem. Anything that is *content* (headings,
paragraphs) is sentence case with normal tracking. The hero title is the one exception:
uppercase + `.175em` tracking in the wide cut, intentionally sized like a label so the
video carries the hero.

---

## 3. Color & imagery

### Tokens (measured, `:root` in page CSS)

```css
--base-color-brand--next-generation-sable: #231f20;  /* near-black, warm */
--base-color-brand--visa-gold:            #d3b975;  /* muted gold, the accent */
--base-color-brand--multisite-gray:       #aba7a5;  /* warm mid gray */
--base-color-brand--inspiration-gray:     #efecea;  /* warm off-white */
--base-color-brand--unity-blue:           #b4c3bf;  /* sage, rarely used */
--base-color-brand--generosity-blue:      #6f7f87;  /* slate, rarely used */
--base-color-brand--white:                white;

--text-color--text-primary:    var(--next-generation-sable);
--text-color--text-secondary:  var(--visa-gold);
--text-color--text-alternate:  white;
--background-color--background-primary:   white;
--background-color--background-secondary: var(--visa-gold);   /* buttons */
--background-color--background-alternate: var(--next-generation-sable); /* dark sections, footer, menu */
--background-color--background-tertiary:  var(--multisite-gray);
--border-color--border-primary:   var(--multisite-gray);
--border-color--border-alternate: var(--inspiration-gray);
--link-color--link-primary:   var(--visa-gold);
--base-color-system--focus-state: #2d62ff;
/* system: success #cef5ca / #114e0b, warning #fcf8d8 / #5e5515, error #f8e4e4 / #3b0b0b */
```

Hard-coded supporting darks used for cards and glass: `#262626` (location card body),
`#322f30` (location card bg) with `#454545` border, `#373737` divider, `#474747` glass border,
`#00000069` glass fill (41% black), `#00000080` overlay (50% black), `#211d1e` and `#12121200`
in gradients. Campaign accents: `#ff4f00`, `#ff5800`, `#f50` (Easter/One Day orange),
`#fee90a`, `#ffc05a`.

### Palette character

Essentially a **two-colour system**: warm near-black and muted gold, with white and warm
grays. The gold is used sparingly as the single accent: primary buttons, eyebrows, footer
headers, hover underline colour, card arrows, the "Give" link in menu and footer
(`text-color-secondary`), and the hamburger lines on hover. Brand blues exist as tokens but
are not visible on the pages studied.

### Light/dark rhythm on the homepage (measured from section classes)

1. Hero: full-bleed **video**, white text.
2. "The Latest": **white** section, dark text, dark image cards.
3. "You Belong Here": full-bleed **photo** with dark glass card.
4. Locations: **dark** (`background-color-alternate`, #231f20) with dark cards.
5. Pastors: full-bleed **photo** with dark glass card, right-aligned.
6. App CTA: **white** section containing a dark rounded card (`cta70_component`).
7. Footer: **dark**.

So the page alternates white / imagery / dark rather than white / gray / white.

### Imagery

- Photography is documentary-style church-life: stage shots with purple/blue stage lighting,
  people laughing, kids, serve days. Hero video is a 1080p MP4 + WebM "Landing Page Update -
  2026" with a JPEG poster.
- Cards always put a gradient/scrim over the photo, never raw photo under text. The
  overlay gradients are:
  - `.background-overlay`: `linear-gradient(180deg, #211d1e, #12121200 61%), radial-gradient(circle farthest-corner at 0% 100%, #231f20 16%, #231f2000 50%)` (dark top edge + dark bottom-left corner).
  - `.background-overlay.is-all`: `linear-gradient(180deg, #231f2000 45%, #231f20 75%), radial-gradient(circle farthest-corner at 50% 100%, #231f2000 43%, #231f20)` (fade to dark at bottom).
  - `.header-background_overlay`: `radial-gradient(circle farthest-corner at 50% 100%, #231f2000 77%, #231f20), linear-gradient(0deg, #231f20, #231f2000 48%)`.
- Rounded corners everywhere: cards `1.25rem` (20px), location cards `2rem`, glass cards `1.5rem` to `2rem`, buttons fully round (`4rem`/`5rem`/`100px`).
- Icons: Iconify SVGs inline (`iconify--tabler`, `iconify--ic`), `currentColor`, sized via
  `.icon-embed-xxsmall` (1rem), `.icon-embed-xsmall` (1.5rem).

---

## 4. Layout & page structure

### Global grid and spacing (measured)

- `.padding-global { padding-left: 2.5rem; padding-right: 2.5rem }` (1.25rem on <= 767px).
- `.container-large { max-width: 120rem /* 1920px */; margin: 0 auto }`. Also `70rem` (`cta70_component`), `45rem` (menu card), `40rem` (glass card), `25rem` (card text), `31rem`.
- Section vertical rhythm: `.padding-section-small` 2rem, `.padding-section-medium` 4rem (3rem mobile), `.padding-section-large` 8rem (6rem tablet, 4rem mobile). `.padding-section-header` 10rem top / 4rem bottom.
- Spacer utilities (padding-top only): xsmall .5rem, small 1rem, medium 2rem (1.5 tablet), large 2.5rem, xlarge 3rem, xxlarge 4rem, huge 5rem, xhuge 6rem, xxhuge 8rem.
- `.button-group { display: flex; gap: 2rem; flex-flow: column }` on home hero; `.is-centered` variant.
- Dividers: `.divider { height: 1px; margin: 1rem 0; background: #231f20 }`, `.is-alternate` gray `#aba7a5`, `.is-secondary` gold, `.is-small { width: 5rem }` (used as a short rule under headings inside glass cards), `.line-divider` 1px gray full-width (footer).
- Webflow default grid `.w-layout-grid { gap: 16px; grid-template-columns: 1fr 1fr }`.
- Footer top grid: `1fr 1fr 1fr 1fr` desktop, `1fr 1fr 1fr` <= 991px, `1fr` <= 479px, gap 2rem / 1rem.
- App CTA: `cta70_component` 2-col grid `1fr 1fr`, `max-width: 70rem`, `border-radius: 1.25rem`, dark bg, content padding `2rem 4rem 2rem 2rem`, phone image `max-width: 80%; max-height: 22rem; position: absolute; bottom: 0` (phones bleed out of the card bottom). Single column at <= 991px.

### Breakpoints (measured)

Webflow defaults only: `max-width: 991px` (tablet), `767px` (mobile landscape), `479px` (mobile portrait). Swiper adds its own: 0 / 480 / 767 / 990 / **1755**.

### Homepage, section by section (measured)

1. **Notification bar slot** `.skrol-noti` (CMS list, empty on this visit; JS measures its height and pushes the nav down by that many px).
2. **Header** `.skrol-nav` absolutely positioned over the hero, transparent (`#231f2000`), `padding: 1rem 0`, `z-index: 9999`. Logo left (icon mark, 2.5rem tall, white SVG), six text links + hamburger right. `.skrol-nav.dark` variant exists (solid #231f20) for non-hero pages.
3. **Hero** `<header class="section_home-hero">` > `.home-hero_component { min-height: 100svh; display: flex; flex-direction: column; justify-content: flex-end }` (80svh on <= 479px). Content sits **bottom-left**: h1 wordmark, then a column of two gold pill buttons ("Plan a visit", "Give"), then a glass "TODAY'S SOAP / 1 John 1-2" pill linking to `/bible-reading`. Background: `.w-background-video` autoplay/muted/loop/playsinline, `object-fit: cover`.
4. **"The Latest at River Valley"** `.section > .padding-global.padding-section-medium > .container-large`: h2, full-width 1px divider, 2rem spacer, **Swiper** of 7 `background-card`s (Recent Message -> YouTube, Operation Christmas Child, Holy Spirit Retreat, First Saturday Serve, Miracle Offering, Christmas Spectacular, River Valley Calendar -> Church Center). Then prev/next round gold arrows (`.swiper_nav-wrapper`, `margin-bottom: 8rem`).
5. **"You Belong Here"** `.section > .background_component { padding: 8rem 0 }` with full-bleed photo and a left-aligned glass card: h2, 5rem gold-less gray rule, mission paragraph, "Learn More" gold button -> `/about`.
6. **Locations** `<section id="locations" class="section_visit-locations background-color-alternate">` dark: eyebrow "River Valley Locations" (gold) + h2 "One Church, Multiple Locations", gray divider, Swiper of 15 location cards (image top 12rem, name, address, "SERVICE TIMES" label, time pills, outline "Learn More"), arrows.
7. **Pastors** same `background_component` pattern as 5 but `data-card-align="right"` (custom CSS flips the glass card to the right): eyebrow "River Valley Leadership", h2 "Pastors Rob & Becca Ketterling", paragraph, "Learn more".
8. **App CTA** `cta70` dark rounded card inside white section: h2 "Download Our App", lead, App Store + Google Play badges, phone screens image.
9. **Footer** dark: logo, 4 link columns (River Valley / Locations / Connect / Ministries) with gold uppercase headers, 1px divider, bottom row with copyright + legal links left and social icons right.

### Secondary layout notes

- Section wrappers are consistently `section > .padding-global[.padding-section-*] > .container-large > content`, so the same horizontal gutter and max width apply site-wide.
- Dark cards on dark sections get a 1px lighter border (`#454545` on `#322f30`) to separate them, instead of shadows. **There are no box-shadows in the custom CSS** at all; depth comes from borders, glass blur, and gradients.

---

## 5. Navigation & header behavior

### Structure (measured)

```
.skrol-nav-test_wrapper (flex column, z 9999, color #efecea)
  .skrol-noti            (announcement bar slot; display:none when empty)
  .skrol-nav             (position:absolute; inset:auto 0%; transparent; padding 1rem 0)
    .nav1_wrapper        (flex, space-between, padding 1rem 2.5rem)
      .nav_left > a > img.nav_logo (white icon mark, max-height 2.5rem, max-width 225px)
      .nav1_right (gap 1rem)
        .nav1_link-wrapper (gap 2rem): About, Visit, Connect, Events, Watch, GIVE
        .nav1_hamburger-wrapper (3rem circle, two 1.25rem x .125rem white lines, gap .3rem)
  .nav1_menu (position:fixed; inset 0; display:none; z 99)
    .nav1_menu-overlay (50% black, opacity 0)
    .nav1_menu-card (right-anchored drawer, max-width 45rem, bg #231f20, padding 5rem 3rem 3rem, overflow:auto)
      .nav1_menu-top > Apollos search widget
      .nav1_menu-grid (2 cols, gap 4rem/3rem, min-width 32rem): Locations (CMS list), River Valley, Connect, Ministries
```

### Behaviors (measured from CSS + IX2)

- **Transparent over hero, no sticky state.** The nav is `position: absolute`, so it scrolls away. There is no scroll-triggered background change on the homepage. A `.skrol-nav.dark` class exists for solid-dark headers on inner pages. **(inference)** the team intentionally keeps the hero chrome-free; the hamburger menu is the persistent navigation.
- **Text links hide at <= 991px** (`.nav1_link { display: none }`), leaving logo + hamburger only. The six links are therefore a desktop shortcut; the drawer is the canonical menu on every width.
- **Link hover:** `transition: all .2s`; colour -> gold and `border-bottom-color` -> gold (2px underline reserved in layout via `margin-bottom: -2px`).
- **Hamburger hover (IX2 "Menu Hamburger [HOVER IN]"):** both lines grow from `1.25rem` to `1.75rem` width over **300ms** `cubic-bezier(.673,.007,.304,.971)` and fade from white to gold `#d3b975` over **500ms**. Hover out reverses with the same timings.
- **Menu open (IX2 "MENU 1 OPEN", click on hamburger):** set `.nav1_menu` and overlay to `display: block`, then slide `.nav1_menu-card` from `translateX(100%)` to `0` over **300ms** `cubic-bezier(.696,.012,.298,.983)` while overlay opacity 0 -> 1 over **500ms** linear-ish `cubic-bezier(.25,.25,.75,.75)`.
- **Menu close (click overlay or close button):** card to `translateX(100%)` over **300ms** `cubic-bezier(.708,-.005,.298,.995)` (slight anticipation, negative y1), overlay opacity to 0 over **500ms** `inQuad`, then `display: none`.
- Menu links are weight 300 at 1.1rem with `transition: border-color .2s` and a white 2px underline on hover. Group headers are gray, wide, uppercase. "Give" is coloured gold inside the menu.
- On tablet the drawer becomes full width (`clip-path` polygon reset, `width: 100%`), close button moves to top (`order: -1`) on mobile.
- Body scroll lock via Finsweet `scrolldisable` attribute script.
- Announcement bar: JS sets `nav.style.top = notification.offsetHeight + 'px'` on load/resize so the absolute nav sits under the bar.

---

## 6. Hero treatment

- **Full-viewport autoplaying video** (`min-height: 100svh`, `80svh` on phones), no text overlay gradient in CSS; legibility comes from the footage itself and from the glass/solid pills rather than from a scrim. **(inference)** footage is colour-graded dark and lit from behind so white text works; a reusable version should still add a bottom gradient for safety.
- **Content anchored bottom-left** with `padding: 2.5rem` (1.25rem mobile), `align-items: flex-end` on the row.
- **Hierarchy is inverted from the usual pattern:** the headline is a small, wide, tracked wordmark ("RIVER VALLEY CHURCH", 1.68rem), and the *buttons* are the visual anchors: two stacked gold pills `padding: .8rem 1.75rem`, `border-radius: 4rem`, uppercase, `letter-spacing: .1em`. Primary = "Plan a visit", secondary = "Give". Both use the same solid gold style; hover turns them white.
- **Daily-content pill:** `.home-hero_soap-wrapper` is a glass chip (`backdrop-filter: blur(20px)`, bg `#00000069`, `border: 1px solid #474747`, `border-radius: 2rem`, `padding: .7rem 1.25rem`) showing "TODAY'S SOAP" (eyebrow at .7rem) and the day's reading, pulled from a CMS collection. Hover: border -> white over `300ms`. This is a nice "the site is alive today" signal.
- **No hero entrance animation on the homepage.** The IX2 fade-ups start with the first content section. The hero relies on motion from the video alone. (Older template classes like `home-hero---content` with opacity 0 + translateY(5rem) exist in a different site's bundle but not here.)
- Mobile: buttons stack full-width-ish in a column; the SOAP pill goes `width: 100%` and `align-self: flex-end`.

---

## 7. Video usage

| Where | Implementation | Attributes |
|---|---|---|
| Homepage hero | Webflow background video component `.w-background-video` wrapping `<video>` | `autoplay muted loop playsinline`, poster set as inline `background-image`, `data-object-fit="cover"`, sources: MP4 then WebM, 1080p encode, `data-wf-ignore` |
| Visit page hero | **Plyr** player (controls, captions, PIP, speed menu) — an on-demand welcome video, not autoplay | lazy-loaded Plyr 3.5.6 |
| Recent message card | Links out to **YouTube** (`youtu.be/...`, `target=_blank`) rather than embedding | background-card |
| Watch + Listen page | "Recent Messages" heading with an Apollos feed (client-rendered; empty in markdown), podcast cards linking to Spotify/Apple, nine YouTube channel cards | links, no iframes |
| Give page FAQ | Links to a hosted MP4 (hopestream) for a teaching clip | link |

Observations: **no YouTube/Vimeo iframes on the homepage**, which keeps it fast; the only
embedded media is the self-hosted background video. Video is used as *atmosphere* (hero) and
otherwise delegated to platforms via links. Hero video has no visible pause control, which is
an accessibility gap (see section 12).

---

## 8. Animations & transitions

All scroll/hover choreography is **Webflow IX2** (no GSAP, AOS, Lottie, Lenis, Locomotive,
or `@keyframes` in first-party CSS; the only keyframes are Webflow's `spin` and Apollos'
modal slide). Swiper handles carousel motion. CSS transitions handle simple hovers.

### 8.1 Scroll-in reveals — "move up fade" (IX2 action list `a-9`, measured)

- **Trigger:** `SCROLL_INTO_VIEW`, offset `0%` (element enters viewport), play once.
- **Initial state** (applied inline on load): `transform: translate3d(0, 1.5rem, 0); opacity: 0`.
- **Animation:** `translateY 1.5rem -> 0` and `opacity 0 -> 1`, **500ms**, easing `ease`, **150ms delay**.
- **Applied to:** `.blur-card` glass cards, `.heading-wrapper` of the Locations section, and *each* child of the App CTA separately (`cta70_component` wrapper, h2, paragraph, button group) — so the CTA appears as a short stagger created by nesting rather than by explicit stagger delays (each child starts 150ms after it individually enters view; in practice they enter together so they animate nearly simultaneously, with a subtle offset from the parent's own transform).
- A `SCROLLING_IN_VIEW` continuous interaction ("Large Text [LEFT]", `a-21`) is bound to the App CTA section: `translateX 0% -> -10%` mapped to scroll progress 0 -> 100%, `smoothing: 90`. **(inference)** this is a leftover for a large marquee text element; no visible marquee exists in the rendered homepage.

### 8.2 Card hover — "Background Card [HOVER IN]/[HOVER OUT]" (`a-33` / `a-37`, measured)

Target: `a.background-card` ("The Latest" carousel). Children animate via `useEventTarget: CHILDREN`.

| Child | Rest state | Hover | Duration / easing |
|---|---|---|---|
| `.background-card_background-image` | `scale(1.1)` | `scale(1)` | 300ms `cubic-bezier(.591,.012,.404,.989)` |
| `.background-card_arrow` (3rem gold arrow top-right, clipped by `overflow:hidden` wrapper) | `translateY(101%)` (hidden below) | `translateY(0)` | 500ms `cubic-bezier(.19,1,.22,1)` (expo-out) |
| `.background-card_button-underline` (2px gold bar under "Learn More", clipped) | `translateX(-101%)` | `translateX(0)` | 500ms `cubic-bezier(.19,1,.22,1)` |

Hover out: image back to `scale(1.1)` (300ms, same bezier), arrow back down (500ms), underline exits **to the right** (`translateX(101%)`, 500ms) and is then reset instantly to `-101%` (duration 0) so the next hover wipes in from the left again. This "wipe out the far side, reset off-screen" trick is worth copying.

Note the inversion: the image is **pre-zoomed at rest and settles to 1:1 on hover**, the opposite of the common zoom-in-on-hover. It reads as the card "coming into focus".

### 8.3 Location card hover (`a-31` / `a-32`, measured)

Target `.locations-item`: image scales `1 -> 1.1` over **250ms** default ease on hover in, back to 1 over 250ms on out. (A conventional zoom; the two listed targets are the image and, inferred, the wrapper.)

### 8.4 Menu / hamburger (see section 5)

- Drawer slide: 300ms, `cubic-bezier(.696,.012,.298,.983)` in / `cubic-bezier(.708,-.005,.298,.995)` out.
- Overlay: 500ms, `cubic-bezier(.25,.25,.75,.75)` in / `inQuad` out.
- Hamburger lines: width 1.25rem -> 1.75rem, 300ms `cubic-bezier(.673,.007,.304,.971)`; colour white -> `#d3b975`, 500ms.

### 8.5 CSS transitions (measured)

- `.button { transition: all .3s }` (bg gold -> white on hover; outline variant border/colour -> gold).
- `.nav1_link { transition: all .2s }`, `.nav1_menu-link { transition: border-color .2s }`.
- `.footer5_link { transition: color .2s }` (-> gold).
- `.ll_address-link { transition: all .2s }` (-> gold).
- `.home-hero_soap-wrapper { transition: border-color .3s }` (-> white); `.home-hero_soap-button { transition: background-color .2s }` (gold -> white).
- Webflow base: `.w-nav-link { transition: background-color .1s, color .1s }`.
- Apollos widget: `transition: .132s ease-out`, modal `opacity .3s ease-in-out`, slide keyframe `0.3s ease-in-out`.

### 8.6 Swiper (measured)

```js
new Swiper('.swiper-events' /* and .swiper-locations */, {
  speed: 500, slidesPerGroup: 1, spaceBetween: 16,
  keyboard: true, allowTouchMove: true, mousewheel: { forceToAxis: true }, a11y: false,
  navigation: { nextEl: '#home-link-next', prevEl: '#home-link-prev' },
  breakpoints: { 0: {slidesPerView: 1.1}, 480: {1.5}, 767: {2.25}, 990: {3.25}, 1755: {4.25} }
});
```

Fractional `slidesPerView` (x.25) deliberately shows a peeking next card. `.swiper { overflow: visible }` on these instances lets cards bleed past the container edge to the viewport edge. Rendered slide width at 1920px was ~432px with 16px gaps. Cards are `height: 40rem; max-height: 65vh` desktop, `30rem / 75vh` tablet.

### 8.7 Easing vocabulary (measured, site-wide across all IX2 lists)

Durations used: 500ms (271 actions), 400ms (86), 300ms (21), 250ms (12), 200ms (5). Delays: 0 or 150ms only. Named easings: `ease` (187), `outQuart` (7), `inQuad` (2). Custom beziers in use: `[.19,1,.22,1]` (expo-out, "snappy settle"), `[.591,.012,.404,.989]`, `[.673,.007,.304,.971]`, `[.696,.012,.298,.983]`, `[.708,-.005,.298,.995]` (all "ease-in-out with a long slow tail"), `[.215,.61,.355,1]` (cubic-out), `[.25,.25,.75,.75]` (near-linear).

### 8.8 Reduced motion

**None.** `prefers-reduced-motion` appears 0 times in both first-party stylesheets and is not
honoured by IX2 by default. The background video also autoplays regardless. A reproduction
should add a reduced-motion guard (see section 14).

---

## 9. Interaction patterns

### Buttons (measured)

```css
.button {            /* primary */
  background: #d3b975; color: #231f20;
  padding: .8rem 1.75rem; border-radius: 4rem;
  font: 500 1em Realist; text-transform: uppercase; letter-spacing: .1em;
  transition: all .3s; display: inline; text-align: center;
}
.button:hover { background: #fff; }
.button.is-small { padding: .5rem 1.25rem; font-size: .875rem; }
.button.is-large { padding: 1rem 2rem; }
.button.is-secondary { border: 1px solid #d3b975; background: #d3b975; }   /* hover -> white bg + border */
.button.is-alternate { background: #fff; color: #231f20; }                 /* hover -> gold */
.button.is-outline { border: 1px solid #231f20; background: transparent; } /* hover -> gold border + text */
.button.is-outline.is-alternate { border-color: #fff; color: #fff; }       /* on dark; hover -> gold */
.button.is-text { background: transparent; border: 2px solid transparent; }
.button.is-icon { display: flex; gap: 1rem; }
```

Pattern: pills only; two fills (gold, white) and one outline; hover always swaps to the
*other* neutral (gold -> white, white -> gold, outline -> gold). No shadows, no lifts.

### Cards

- **Background card** (`.background-card`): link wrapper, `border-radius: 1.25rem`, `overflow: clip`, dark bg fallback, image absolutely filling, overlay layer, content split top (eyebrow + h3, `max-width: 25rem`, `padding: 2rem 5rem 2rem 2rem` to leave room for the arrow) and bottom ("Learn More" + animated underline). Arrow icon is gold, 3rem, revealed on hover.
- **Location card** (`.locations-item`): `bg #322f30; border: 1px solid #454545; border-radius: 2rem; text-align: center`; image band `min/max-height: 12rem`; content `padding: 2rem 1rem; gap 2rem; flex: 1; justify-content: space-between` so the outline button pins to the bottom; service times rendered as **gold pills** (`.location-card_time.is-dark`: `padding .25rem .75rem; border-radius 3rem; font-size .875rem`).
- **Glass card** (`.blur-card`): `backdrop-filter: blur(20px); background: #00000069; border: 1px solid #474747; border-radius: 1.5rem; padding: 2rem; max-width: 40rem`; loses border and max-width on tablet. Content recipe: [eyebrow] / h2 / 5rem rule / 1rem / paragraph / 1rem / button.
- **Dark CTA card** (`.cta70_component`): 2-col, dark on white, radius 1.25rem, image breaks the card edge.

### Carousel controls

`.swiper_arrow-wrapper { width: 3rem; height: 3rem; border-radius: 5rem; background: #d3b975; color: #231f20 }`, two of them with `.5rem` gap, placed **below** the track, left-aligned; disabled state uses Swiper's `.swiper-button-disabled` (opacity .35 from Swiper CSS).

### Hover summary

Gold is the universal hover signal: text -> gold, underline -> gold, border -> gold, bg gold -> white. Images: 300ms settle (latest cards) or 250ms zoom (locations). Nothing moves on the y-axis on hover except the hidden arrow reveal.

### FAQ accordions

Visit, Give and campus pages end with an "FAQ" section (question rows that expand). Markdown shows plain Q/A text; **(inference)** Webflow dropdown/accordion with IX2 `MOUSE_CLICK` + `MOUSE_SECOND_CLICK` pairs (81 second-click events site-wide) rotating a chevron (`TRANSFORM_ROTATE`, 42 actions) and animating `STYLE_SIZE` height (86 actions) over 400ms. Also, the "**Hey!** What are you looking for?" line on the Give page is the Apollos search prompt.

---

## 10. Content & CTA strategy

### Visitor-first wording (measured)

- Title tag: "River Valley Church | Life-Changing Faith in Jesus Christ". Meta: "There's a place for you at River Valley Church!"
- Hero: name + **"Plan a visit"** (first) + **"Give"** (second). Nothing else competes.
- Second section is *news* ("The Latest"), third is *welcome* ("You Belong Here" + mission statement), fourth is *where* (locations with service times inline), fifth is *who* (pastors), sixth is *app*.
- Repeated phrases: "You Belong Here" / "You Belong Here!" (homepage and Visit page h2), "There is room for you", "We can't wait to meet you!", "One Church, Multiple Locations".
- Button copy is short and uniform: "Plan a visit", "Give", "Learn More" (overused, see weaknesses), "Find a location", "Discover", "Visit Channel", "Join Us".

### Primary nav as a funnel

About / Visit / Connect / Events / Watch / **GIVE** (the only all-caps-in-source item and the only gold item in menus and footer). Visit precedes Connect; Give is last and highlighted.

### Give

Dedicated `/impact/give` page: per-campus Tithe.ly buttons first ("Give with Credit Card or Bank Account"), then "How to Find Giving Statements" (app + web steps), then "Ways to Give" (direct deposit, text-to-give 94000, stock, Thrivent, QCD, crypto via Engiven per campus, assets, legacy), then two promo cards (Kingdom Builders, Support Missionaries), then FAQ explaining tithe vs offering. Give is also a tile on every campus page.

### Serve

"Serve" lives under Connect in the drawer and footer; campus pages show "Dream Teams" and "Serve Our Community" tiles linking to Church Center registrations. Homepage surfaces "First Saturday Serve" as a news card rather than a permanent section.

### Watch

`/watch-listen`: Recent Messages feed (Apollos), four podcasts with Spotify/Apple links, three worship brands, nine YouTube channels as image tiles. Weekend online times are stated in meta ("Join us online Saturday at 4pm, Sunday at 9 & 11am").

### Locations

Fifteen campuses (12 MN, Online, Tokyo, Vancouver, Eswatini). Shown three times: nav drawer list, homepage carousel with addresses + time pills, footer column. `/connect/visit` is the hub ("Visit River Valley Church" h1, "You Belong Here!" h2, "Find a location" anchor button to `#locations`, Plyr welcome video, full card grid with map links and "SERVICE TIMES", FAQ, app CTA). Each campus page: Join Us (address, Discord), Contact (phone, email), Social, "Plan Your Visit" paragraph + button, "Take Your Next Step" tile grid (Connect Card, Welcome Home, Small Groups, Dream Teams, Give, Serve Our Community, Events, Global Teams), Next Generation (Kids, Youth), Staff grid (name, role, email), FAQ.

### App

"Download Our App" CTA (h2 + one-line lead + two store badges + phone mock) appears on the homepage, Visit, Watch and campus pages — a reusable global CTA block placed just above the footer.

---

## 11. Secondary page templates

| Template | Header | Body modules | Closing |
|---|---|---|---|
| **Visit hub** `/connect/visit` | h1 "Visit River Valley Church", h2 "You Belong Here!", one-line lead, anchor button, Plyr video | Eyebrow "River Valley Locations" + h2 "One Church, Multiple Locations"; grid of location cards (image, name, address link to Google Maps, SERVICE TIMES label, times text, Learn More) | FAQ accordion, App CTA, footer |
| **Campus page** `/locations/{slug}` | (image header with `.header-background_overlay` radial/linear dark gradient, inferred from CSS) | App CTA (placed high), Join Us / Contact Info / Social Media three-up, "Plan Your Visit" text + button to `/connect/next-steps`, "Take Your Next Step" 8-tile grid (image + bold title + "Learn More"), Next Generation 2 cards, Staff grid | FAQ, footer |
| **Give** `/impact/give` | (hero not captured in main content) | h3 sections in a long single column: campus button cloud, statements how-to, Ways to Give rich text, two image+text promo cards, FAQ | footer |
| **Watch + Listen** | h2 "Recent Messages" feed | Podcasts (image, h3, blurb, "listen On" Spotify or Apple), River Valley Worship (3 artist cards with "Stream On"), YouTube channels (9 image tiles) | App CTA, footer |

Shared template traits: stacked h2 modules separated by `padding-section-medium`; every
module repeats the eyebrow -> heading -> divider -> spacer -> content recipe; tile grids use
image + bold title + generic "Learn More"; FAQ and App CTA are reusable closers; the same
nav drawer and footer on every page.

Template CSS seen but not visited: `visit-header_component` (2-col grid, 1 col tablet),
`leadership_list` (grid, 2-col tablet), `stats26` (numbers at 3rem), `articles_grid`,
`missions-list`, `give-methods_component`, `serve-team_component`, `careers-*` timeline.

---

## 12. Accessibility notes

Positives (measured):
- Semantic landmarks: `<header>`, `<main>`, `<footer>`, `<section id="locations">`, role=list/listitem on CMS lists, h1 present once per page.
- Visible focus style: `[tabindex]:focus-visible { outline: .125rem solid #4d65ff; outline-offset: .125rem }` and a `--focus-state: #2d62ff` token.
- Body text 17.6px / 1.5 line-height on near-black; buttons are gold on near-black text (contrast roughly 9:1, inference from values).
- Swiper has `keyboard: true` and `mousewheel.forceToAxis`.
- ASL interpretation times are listed for campuses.

Gaps (measured):
- `alt=""` on nearly every image including meaningful photos, logo (`nav_logo` alt empty), and app badges; link images have no text alternative (e.g. YouTube channel tiles rely on adjacent bold text, campus-card image links have no name).
- Swiper initialised with `a11y: false`, and the prev/next controls are `<div>`s with no role, name, or keyboard handler.
- Autoplaying hero video with no pause control and no `prefers-reduced-motion` handling.
- Hamburger and menu close controls are `<div>`s with `data-w-id` click handlers, not buttons; the overlay is also a click target div.
- Uppercase + `.2em` tracking at `.7rem` to `.9rem` is small for eyebrow/pill labels.
- Gray `#aba7a5` labels on `#322f30` cards are low contrast (approx 4:1, inference).
- Relies on an accessiBe overlay rather than fixing markup.
- Duplicate links in the drawer (each campus rendered twice: internal page + conditional external link, one hidden via `w-condition-invisible`).

---

## 13. Weaknesses to avoid

1. **Font bloat:** 14 self-hosted faces plus a Typekit kit of ~40 faces plus Google Open Sans are loaded site-wide although the UI uses two families. Load only what the page uses; split campaign fonts into their pages.
2. **"Learn More" everywhere:** 7 of 7 news cards, 15 of 15 location cards, pastor and welcome cards. Use verb-specific labels ("Watch the message", "Get directions", "See service times").
3. **Generic empty alt text** and div-buttons (see section 12).
4. **No reduced-motion path** and an autoplay video with no pause.
5. **Repetition of the campus list** three times per page (drawer, carousel, footer) plus duplicate hidden links; heavy DOM (15 slides with full images in two carousels).
6. **Placeholder content shipped:** campus staff cards contain "This is some text inside of a div block." under Saturday/Sunday — CMS conditional visibility not applied.
7. **Dead `#` links:** first-render location cards link to `/#` before Swiper/CMS swaps; several "Learn More" buttons point to `https://www.rivervalley.org/#`.
8. **Transparent nav with no scroll state** means once you scroll the hero away there is no header until you scroll back to top; combined with text links hidden under 992px, discoverability depends on the hamburger.
9. **Hero headline is tiny**; works for a brand people already know (10,000 attendees) but a smaller parish would want a real headline + one-line promise.
10. **Swiper `overflow: visible` + peeking cards** can cause horizontal scroll on some mobile browsers if the section lacks `overflow: clip` (they do add `.section_visit-locations { overflow: clip }` and `.section_home-hero { overflow: hidden }`; copy that guard).
11. Leftover interactions (scroll-progress marquee bound to a section with no marquee) and dozens of campaign-specific classes in the global sheet.

---

## 14. Reusable patterns (concrete, codeable)

### 14.1 Tokens

```css
:root {
  --ink: #231f20;  --accent: #d3b975;  --gray: #aba7a5;  --paper: #efecea;  --white: #fff;
  --card-dark: #322f30;  --card-border: #454545;  --glass-fill: #00000069;  --glass-border: #474747;
  --radius-card: 1.25rem;  --radius-card-lg: 2rem;  --radius-pill: 4rem;
  --gutter: 2.5rem;  --container: 120rem;
  --section-sm: 2rem;  --section-md: 4rem;  --section-lg: 8rem;
  --ease-settle: cubic-bezier(.19, 1, .22, 1);          /* expo-out, 500ms reveals */
  --ease-inout-soft: cubic-bezier(.696, .012, .298, .983); /* 300ms drawers/scale */
  --t-fast: .2s;  --t-base: .3s;  --t-slow: .5s;
}
@media (max-width: 767px) { :root { --gutter: 1.25rem; --section-md: 3rem; --section-lg: 4rem; } }
```

### 14.2 Type

- Body: 500 weight sans at 1.1rem / 1.5 / .01em tracking. Headings 700, h1 4rem/1.1, h2 3rem/1.2, h3 2rem/1.2; mobile h1 2.5rem, h2 2rem, h3 1.5rem.
- Label style (eyebrow, nav, footer header, pill): `font-size: .9rem; letter-spacing: .2em; text-transform: uppercase; font-weight: 500` (gold when it labels a section, gray when it labels a list).
- Button text: uppercase, `.1em` tracking, 500.
- Hero: small wide uppercase wordmark (1.5–2rem, `.175em`) over video; let buttons anchor.

### 14.3 Section skeleton

```html
<section class="section [is-dark]">
  <div class="padding-global padding-section-medium">
    <div class="container-large">
      <div class="heading-wrapper reveal">
        <div class="eyebrow accent">Eyebrow</div>
        <h2>Heading</h2>
      </div>
      <div class="divider"></div>          <!-- 1px, full width, 1rem margins -->
      <div class="spacer-medium"></div>    <!-- 2rem -->
      ...content...
    </div>
  </div>
</section>
```

### 14.4 Scroll reveal (replicates IX2 "move up fade")

```css
.reveal { opacity: 0; transform: translateY(1.5rem); }
.reveal.is-in { opacity: 1; transform: none;
  transition: opacity .5s ease .15s, transform .5s ease .15s; }
@media (prefers-reduced-motion: reduce) { .reveal { opacity: 1; transform: none; transition: none; } }
```
JS: IntersectionObserver, `threshold: 0`, add `.is-in` once. Apply to glass cards, section
heading wrappers, and CTA children individually.

### 14.5 Image card with hover choreography (replicates "Background Card")

```css
.card { position: relative; overflow: clip; border-radius: var(--radius-card);
        height: 40rem; max-height: 65vh; color: #fff; background: var(--ink);
        display: flex; flex-direction: column; justify-content: space-between; }
.card img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;
        transform: scale(1.1); transition: transform .3s cubic-bezier(.591,.012,.404,.989); }
.card:hover img { transform: scale(1); }
.card .arrow-clip { position: absolute; top: 1rem; right: 1rem; overflow: hidden; }
.card .arrow { width: 3rem; height: 3rem; color: var(--accent);
        transform: translateY(101%); transition: transform .5s var(--ease-settle); }
.card:hover .arrow { transform: none; }
.card .cta { position: relative; overflow: hidden; align-self: flex-start;
        font-size: .9rem; letter-spacing: .2em; text-transform: uppercase; }
.card .cta::after { content: ""; display: block; height: .125rem; background: var(--accent);
        transform: translateX(-101%); transition: transform .5s var(--ease-settle); }
.card:hover .cta::after { transform: none; }
/* optional: on mouseleave wipe out to the right, then reset — needs JS or an animation */
.card .top { max-width: 25rem; padding: 2rem 5rem 2rem 2rem; }
.card .bottom { padding: 2rem; }
.card h3, .card .cta { text-shadow: 0 3px 10px #00000026; }
```

### 14.6 Glass card over full-bleed photo

```css
.band { position: relative; overflow: hidden; padding: 8rem 0; color: #fff; }
.band > img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.band .glass { position: relative; max-width: 40rem; padding: 2rem; border-radius: 1.5rem;
  background: var(--glass-fill); border: 1px solid var(--glass-border);
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); }
.band[data-align="right"] .glass { margin-left: auto; }
.glass .rule { width: 5rem; height: 1px; background: var(--gray); margin: 1rem 0; }
@media (max-width: 991px) { .band { padding: 0 0 4rem; } .band .glass { max-width: none; border: 0; } }
```
Alternate bands left/right down the page (homepage does left for Welcome, right for Pastors).

### 14.7 Pill buttons

Primary gold pill `padding .8rem 1.75rem; border-radius 4rem; transition all .3s; hover bg
white`; outline on dark `border 1px solid #fff; hover border+text gold`. Group as a column
with 2rem gap in heroes, row with 1rem gap elsewhere.

### 14.8 Peeking carousel

Swiper (or CSS scroll-snap) with `gap 16px`, `speed 500`, fractional slides per view
1.1 / 1.5 / 2.25 / 3.25 / 4.25 at 0 / 480 / 767 / 990 / 1755px, track allowed to overflow the
container but the *section* set to `overflow: clip`. Round 3rem gold prev/next buttons below
the track, left-aligned, 8rem bottom margin before the next band (4rem on mobile). Make
them real `<button>`s with `aria-label`.

### 14.9 Off-canvas drawer menu

Fixed full-screen wrapper; 50% black overlay fading 0 -> 1 over 500ms; right-anchored dark
panel (`max-width 45rem`, `padding 5rem 3rem 3rem`) sliding `translateX(100%) -> 0` over
300ms `var(--ease-inout-soft)`; close reverses with a slightly anticipatory bezier
`cubic-bezier(.708,-.005,.298,.995)`. Panel content: search at top, then a 2-column grid of
link groups with gray uppercase wide headers (.875rem, .2em) and light-weight 1.1rem links
that underline in white on hover. Hamburger = two 1.25rem lines that grow to 1.75rem and
turn gold on hover (300ms). Lock body scroll while open. Full-width panel under 992px.

### 14.10 Location card

Dark card (`#322f30`, 1px `#454545` border, radius 2rem, centered text): 12rem image band,
h3 name, address, uppercase gray "SERVICE TIMES" label with a thin `#373737` rule, times as
gold pills (`.25rem .75rem`, radius 3rem, .875rem), outline white "Learn More"/"Get
directions" pinned to the bottom via `flex: 1; justify-content: space-between`.

### 14.11 Page-level rules

- Alternate **white -> photo band -> dark -> photo band -> white (with dark card) -> dark footer**.
- First section after the hero is *news*, second is *welcome/mission*, third is *where/when*.
- Keep a single accent colour and use it for: primary buttons, eyebrows, hover states, the
  Give link, carousel arrows, card arrows. Everything else is ink, white and warm gray.
- Depth via borders, blur and gradients; no drop shadows.
- Put "Plan a visit" and "Give" in the hero; put a daily-content chip (reading plan, this
  week's message) in the hero so the page feels current.
- Close every inner page with FAQ + the global App/Next-step CTA.
- Gate heavy third-party scripts behind `document.querySelector('.needs-x')`.
- Add what they lack: `prefers-reduced-motion` guards, a video pause button, real
  `<button>`s, descriptive alt text, and specific CTA verbs.

---

## Appendix A — Files and selectors of note

- Stylesheets: `https://cdn.prod.website-files.com/6696de90740e44393c25e78f/css/rivervalleychurch.webflow.shared.0e753df24.min.css` and `.../css/rivervalleychurch.webflow.6696de90740e44393c25e790.02c4b2f49.opt.min.css`
- IX2 definitions: `.../js/webflow.schunk.f5cb2a42e331bc47.js` (search `actionLists:{` at byte ~431,891; action list titles: "move up fade" `a-9`, "Background Card [HOVER IN]" `a-33`, "Background Card [HOVER OUT]" `a-37`, "MENU 1 OPEN" `a-28`, "MENU1 CLOSE" `a-29`, "Menu Hamburger [HOVER IN]" `a-35`, "location-hover (OVER)" `a-31`, "Large Text [LEFT]" `a-21`).
- Hero video poster/MP4/WebM: `.../6989b969f981ef94ec9d6c96_Landing%20Page%20Update%20-%202026%20%281080%29_{poster.0000000.jpg|mp4.mp4|webm.webm}`
- Key selectors: `.skrol-nav`, `.nav1_*`, `.home-hero_*`, `.soap-heading`, `.background-card*`, `.blur-card`, `.background_component`, `.locations-item*`, `.location-card_time`, `.swiper_arrow-wrapper`, `.cta70_*`, `.footer5_*`, `.text-style-eyebrow`, `.button.is-*`.

## Appendix B — What could not be observed

- Hover/scroll behaviour on inner pages beyond what the shared IX2 bundle and CSS reveal (no inner-page screenshots were taken).
- The "Recent Messages" feed content (client-rendered by Apollos; empty in scrapes).
- The campus page hero and the Give page hero were stripped by main-content extraction; their overlay CSS (`.header-background_overlay`) is documented from the stylesheet only.
- Exact accordion timings (inferred from site-wide IX2 statistics, not from a homepage instance).
