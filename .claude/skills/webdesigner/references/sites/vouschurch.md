# VOUS Church (vouschurch.com) — design pattern study

Studied 2026-11-04. Sources: Firecrawl scrapes of the homepage (html, rawHtml, links,
screenshot), /visit (markdown + rawHtml), /give, /crews (markdown), the main Webflow
stylesheet (`vousdev.shared.270d9b24d.min.css`, 287 KB), the page JS bundle
(`vousdev.47662693.*.js`, IX2/IX3 interaction definitions) and the first-party scripts
`home-card-reveal.js`, `side-scroll.js`, `hero-broll-preload.js`, `vous-nav-2026-09-20a.js`.
Computed styles and the live GSAP/ScrollTrigger registry were read from the page in the
built-in browser at 1440×900 and 375×812 because Firecrawl's DOM serialisation drops the
Webflow `<link rel=stylesheet>`.

Everything marked **(inferred)** is a judgement; everything else is a value read from
CSS, JS, or the live DOM. Firecrawl could not read the hover state of the Webflow IX3
nav interactions directly; those come from `gsap.globalTimeline.getChildren()`.

Working files kept beside this report in
(`home.raw.html`, `home.inline.css`, `home.inline.js`, `webflow.clean.css`,
`page-bundle.js`, `visit.raw.html`).

---

## 1. Platform & stack

- **Webflow** site (`data-wf-site="6945a22d265e7438ae833c5b"`, assets on
  `cdn.prod.website-files.com`), short name `vousdev`. Last published 2 Nov 2026 — it is
  re-published almost daily.
- Webflow **Interactions 3 (IX3, GSAP-backed)** is on: `<html class="w-mod-ix3">`, and
  both `Webflow.require('ix2')` and `('ix3')` resolve. Legacy IX2 presets still drive a few
  things (hero fade/slide-in, FAQ accordions, dropdowns).
- **GSAP 3.15.0 + ScrollTrigger** loaded from Webflow's GSAP CDN
  (`cdn.prod.website-files.com/gsap/3.15.0/`). All scroll reveals are hand-written GSAP,
  not a library like AOS.
- jQuery 3.5.1 (Webflow runtime dependency only).
- Fonts via **Google Fonts** + `webfont.js` 1.6.26 loader:
  `Inter:300,400,500,600,700 | Inter Tight:300,400,500,600,700 | Spline Sans Mono:300,400,500,600,700`.
  The stylesheet also self-hosts `@font-face` for campaign/sub-brand faces (JetBrains Mono,
  Edsonna, Huddle, Instrument Serif, "Video", PPSupplyMono, HelveticaNowDisplay, Kimane) —
  these are for event/collection pages, not the core site.
- First-party JS on a GCS-backed CDN (`cdn.vouschurch.com/CDN/site/js/…`), each with a
  `?version=` cache-buster and a header comment explaining itself. Files seen on the home
  page: `faq-accordion.js`, `scroll-remeasure.js`, `home-card-reveal.js`, `side-scroll.js`,
  `crewhub-*.js`, `crew-type-clamp.js`, `location-preview-*.js`, `hero-broll-preload.js`,
  `analytics-*.js`, `vous-nav-*.js`, `build-pill-*.js`, `menu-icon.js`, `calendar.js`,
  `side-scroll-wheel-*.js`, `ported-card-reveal-*.js`, plus Webflow "registered scripts"
  (`placeholderstrip`, `vccalendartoday`, `vcmobilereveal`, `stickysubnavscroll`,
  `vcconfetti`, `vcdropdownlayer`, `vcmodalfromurl`, `vousblreport`, `externallinks`,
  `sitepopup`).
- Analytics: GA4 `G-6K6D71VQ2X`. Cloudflare Turnstile on forms.
- Church management: CCB (`vouschurch.ccbchurch.com`) for login/forms; giving via
  Overflow (`app.overflow.co/vouschurch/...`) for stock/crypto.
- Images: `.webp` everywhere, `loading="lazy"`, lots of SVG icons. OG image is webp.
- No `clamp()` anywhere in the CSS; no `prefers-reduced-motion` in the Webflow CSS, but
  every hand-written inline `<style>` block and every custom script honours it.

## 2. Typography

### Families (CSS variables on `:root`)
| Variable | Value | Role |
|---|---|---|
| `--main-font` | `"Inter Tight", sans-serif` | all headings h1–h4, section body copy, modal titles |
| `--secondary-font` | `Inter, sans-serif` | nav links, footer links, card descriptions, popup copy, inputs |
| `--alternate-font` | `"Spline Sans Mono", sans-serif` | overlines, buttons, addresses, dates (h5), vertical rail labels, footer legal |

Body default is Webflow's `Arial, Helvetica Neue, Helvetica, sans-serif` 14px/20px
#333 — never visible because every text element sets its own family.

### Scale (`--_typography---*`)
`text-xs 12px · text-sm 14px · text-base 16px · text-lg 20px · text-xl 22px · text-2xl 24px ·
text-3xl 28px · text-4xl 36px · text-5xl 48px · text-6xl 64px · text-7xl 80px`

Fixed pixel steps, no fluid type. Responsiveness is done by swapping the variable per
breakpoint, e.g. `.heading-hero-title` = 80px → 64px (≤991) → 36px (≤479).

### Heading rules (base stylesheet)
- `h1`: Inter Tight 36px / 1.1em, weight **500**, colour `--off-white` by default
  (headings are designed to sit on dark hero video), `.heading-black` flips to `--off-black`.
- `h2`: Inter Tight 28px / 1em, weight 500.
- `h3`: Inter Tight 22px / 30px, weight 600, **letter-spacing .75px**; `.weight-normal`
  (400) is used for the service-times line so name and times share one size.
- `h4`: Inter Tight 20px / 24px, weight 500 (calendar card titles).
- `h5`: **Spline Sans Mono 14px / 20px, weight 400** (calendar dates) — mono is used as a
  heading level, which is the most distinctive typographic move.
- `h6.heading-menu`: Inter 20px (`--small-heading-font-size`), weight 500 (mega-menu
  column heads).
- Hero page title `.heading-hero-title`: Inter Tight **80px / 1em, weight 600**, white.
- Body `.text-section-body`: Inter Tight 20px, **weight 300**, line-height 1.15em,
  letter-spacing .5px, centred.
- Card body `.text-cta-body`, `.text-calendar-card-description`: Inter 16px/20px 400,
  colour `--golden-brown` (#7e705f) or `--gray-font-color` (#757370).
- Address `.text-location-address`: Spline Sans Mono 14px/20px, `--golden-brown`.
- Overline `.overline`: Spline Sans Mono 12px, **letter-spacing 4px, uppercase**, colour
  `--gold` (#c6beab) ("WATCH NOW", also "FOLLOW" / "DISCOVER" rails).
- Buttons: Spline Sans Mono 14px (or 12px), weight 500, letter-spacing 1px, uppercase
  (CTA labels like LEARN MORE, DISCOVER CREWS, PRE-SAVE NOW).
- Mobile menu primary links `.mobile-main-nav-link`: Inter **28px, weight 600** (≤991).

### Casing & tracking rules
- Sentence case for headings ("Visit VOUS", "Our mission is simple:", "VOUS is for you").
- ALL-CAPS only in the mono face: overlines (4px tracking), buttons/labels (1px), footer
  legal (12px, `.div-footer-copyright.legal`).
- Negative tracking (-1px/-2px) appears only on campaign/collection pages, not the core site.
- Most frequent letter-spacing values in the CSS: 1px (41 uses), 1.5px (25), 2px (13).
- Line-heights: headings 1em–1.1em (tight), body 1.3–1.5em.

## 3. Color & imagery

### Palette (`:root` variables)
| Token | Hex | Use |
|---|---|---|
| `--off-white` / `--main-gray` | `#e8e6e3` | page background (`body.body-off-white`), hero text, input borders |
| `--off-black` | `#131212` | primary text, button borders, hero b-roll wash |
| `--main-white` | `#fff` | cards, navbar, footer |
| `--main-black` | `#000` | nav link text, footer button border |
| `--gold` | `#c6beab` | accent: overlines, sticky sub-nav pill background |
| `--golden-brown` | `#7e705f` | secondary text (addresses, card copy, footer copyright) |
| `--gray-font-color` | `#757370` | muted text, mega-menu links, nav divider rgba(117,115,112,.1) |
| `--white-transparent-background` | `#fffffff2` | mega-menu panel (95% white + blur) |
| role aliases | `--_color-roles---surface-page/card/inverse, text-primary/secondary/muted/on-inverse, accent, border-subtle` | semantic layer over the raw tokens |

Other colours in the stylesheet (`#f2f2e8`, `#191617`, `#1f3c53`, `#4c5522`, `#6a84b5`)
belong to campaign pages (Vision Sunday, Bricklayers).

Net effect: a **warm greige, near-monochrome** system. No saturated brand colour on the
core site; warmth comes from `#c6beab`/`#7e705f` and from photography.

### Imagery
- Hero: full-bleed autoplaying sermon loop (4K `.webm`, 3840×2160), real room, warm stage
  light, crowd from behind. Cinematic, not stock.
- Location cards: aerial / exterior photo of each building, 16:9-ish, object-fit cover.
- Mission band: single dark photo (paper planes) with the off-white statement centred on it.
- Calendar: poster-style event artwork, each its own colour world (the only place colour
  appears).
- "VOUS is for you": one tall B&W worship photo left, three white text boxes right.
- Pastors: a single wide photo + two short paragraphs.
- Gallery: 18 black-and-white "Rectangle NN.webp" crowd photos in the stack-to-grid stage.
- Icons: thin single-colour SVGs (play button, long arrow, left/right arrows, socials).
  Arrow glyph is a long thin line with a small head (`long-arrow.svg`, 21×8 for pagers).

## 4. Layout & page structure

### Spacing tokens
`space-4 … space-120` in steps (4, 8, 12, 16, 20, 24, 32, 36, 40, 48, 50, 60, 80, 120).
`--_spacing---section-y: 60px` (40px ≤767) · `section-y-tight: 40px` (32px) ·
`section-y-opener: 120px` (80px) · `section-y-bleed: 0px` · `section-header-gap: 60px`
(32px ≤767) · `gutter-page / gutter-x: 10%` · `gutter-page-wide: 15%` (≥1440) ·
`gutter-page-mobile: 5%`.
Radii: `sm 4 · md 8 · lg 16 · xl 20 · 2xl 40 · full 9999`. Core UI uses **xl (20px)** on
buttons/panels and **0** on cards (cards are sharp white rectangles).

### Breakpoints (Webflow defaults, plus two wide ones)
`max-width:991px` (tablet) · `767px` (landscape phone) · `479px` (phone) ·
`min-width:1280px` and `min-width:1440px` (wide desktop: gutters go from 10% to 15%).
Mobile (≤767) re-declares the whole spacing variable set on `body`.

### Containers
- Sections are full-bleed with **percentage gutters** (10% each side; 15% ≥1440px, 5%
  ≤479px), so at 1440 the content column is ≈998px, at 375px ≈300px.
- Section intro block `.div-section-top-title`: max-width **500px**, centred, column flex
  with 32px gap (h1 → one-line body → outline button), margin-bottom 60px. On ≤991 it is
  75% wide, ≤479 95%.
- Horizontal rows `.div-scroll-wrapper`: `display:flex; overflow:scroll; gap 50px`
  (32px ≤479), scrollbar hidden, `overscroll-behavior-x: contain`, `overflow-y: hidden`.
- Grids elsewhere (visit page locations): `repeat(3, minmax(0,1fr))`, gap 20px,
  max-width 1200px → 2 cols ≤991 → 1 col ≤767. Growth-track steps: 4 cols → 2 → 1.
- `max-width` values seen: 1200px (16×), 500px, 680px, 750/760px, 800px, 900px, 1400px.

### Homepage, section by section (desktop 1440×900 offsets)
1. **Hero** `.hero-video-wrapper` — 0–900px. `height/min/max: 100svh`, `max-width: 100svw`,
   overflow hidden, flex centred. Video behind at z-index -1. Three absolutely positioned
   overlays: socials rail top-left (`top:15%; left:4%`), play-title bottom-left
   (`inset: auto auto 10% 8%`), discover rail bottom-right (`inset: auto 1% 10% auto`).
   Background colour of body (off-white) shows nowhere; no gradient scrim is used.
2. **Visit VOUS** `.section-visit` — 900–1809 (909px tall), `padding 60px 15%`. Intro
   block, then a horizontal row of 6 white **location cards** (350px wide, min-width 350
   / max 450, `padding 60px 50px`, gap 50px) each: index "01", photo (250×176, with a
   "▶ PREVIEW" pill), h3 name, h3.weight-normal times, mono address. Below: two 21px arrow
   pagers (left disabled at 25% opacity). Last card is "VOUS Online" with "Watch Online →".
3. **Mission band** `.section-mission` — 1809–2278 (469px). A dark full-width photo inside
   the 15% gutters (998px wide) with the statement centred in off-white 36px Inter Tight:
   "Our mission is simple: / To bring those who are far from God close to him."
4. **Calendar** `.section-calendar` — 2278–3030 (752px). Left-aligned h1 "Calendar"
   (hidden "Full Calendar →" link), horizontal row of 8 **calendar cards** (342px wide,
   white, no padding on the card; image full-width top, then h4 title, h5 mono date,
   3-line-clamped description with a "…" expander, outlined mono button "PRE-SAVE NOW /
   BE A PART / REGISTER / GET TICKETS / LEARN MORE / SIGN UP"). Arrow pagers below.
5. **VOUS is for you** `.section-cta` — 3029–3873 (844px), `padding 60px 0` (no side
   gutter). h1 centred, then a two-column band: tall B&W photo left, right column of three
   stacked white **CTA boxes** (`max-width 500px`, `padding 20px 32px`, 20px gap): h2 title,
   16px brown body, mono uppercase label + long arrow ("DISCOVER CREWS", "LEARN MORE",
   "DISCOVER MORE") → /crews, /kids, /voushigh.
6. **Our Pastors** `.section-pastors` — 3873–4101 (228px, bleed). Two short paragraphs +
   one 518×228 photo (desktop), h2 "Our Pastors".
7. **Our Values** `.section-values` — 4101–4605 (504px). Left "about" column (h1 "Our
   Values" + brown one-liner) and a horizontal row of 7 `.div-value-wrap` cards
   (max-width 425px, 40px gap, no background): h2 "01" / h2 "Jesus is our message" /
   mono paragraph. Arrow pagers.
8. **Gallery** `.section-gallery` / `#wf-stack-grid-stage` — 4605–5235 (630px, bleed,
   full width). 18 B&W photos that start stacked in the centre and fly out into a 6×3
   grid (see §8).
9. **Footer** `.section-footer` — 5235–5598 (363px), white, `padding 48px 0`.
   Row 1: wordmark | links (Watch, Visit VOUS, Give, Resources, For Churches, Shop) |
   three outlined mono pill buttons (NEED CARE?, LOGIN, CONTACT US). Divider 1px
   `#7573701a`. Row 2: six sub-brand logos (VOUSCon, Friends & Family, Merch, VOUS Worship,
   VOUS Girl, VOUS College) | six 24px social icons. Row 3: "©2015 · PRIVACY POLICY ·
   SMS TERMS & CONDITIONS" in 12px mono uppercase brown.
   Also in the footer component: five hidden modals (Prayer Request, Need Care?, Contact
   Us, General Contact, Speaking Inquiry) and the fixed "Connect with Us" popup.

Total page height 5598px at 1440 — short for a church homepage; everything scrolls
horizontally instead of vertically.

### Mobile (375×812) layout changes
- Hero stays `100svh`; `padding-bottom: 12.5svh` so the play-title sits above the bottom
  edge; socials rail `top:10%`, `left:5%`; discover rail moves to `top:25%; right:0`
  (both rails still shown on phones).
- Sections `padding 40px 10%` (gutter-x stays 10% on phone; the 5% mobile gutter is used
  by navbar/footer only).
- Location cards `min-width 95%` of the row, `padding 32px`, row gap 32px → one card per
  swipe with a sliver of the next.
- CTA boxes become full-width stacked; values become a vertical column (≤767) with the
  row flattened; footer links become a 2-column grid 75% wide; footer buttons `flex: 40%`.
- Mission statement drops to 28px/1.25em (≤479).
- Mega-menu becomes 90% wide, `padding 24px 20px`, scrollable `max-height: calc(100svh - 80px)`.

## 5. Navigation & header behavior

- `.menu-wrapper` is `position: fixed; top: 0; z-index: 100`, containing the navbar and
  the mega-menu panel. Navbar is **60px tall**, solid white (`--main-white`), no shadow, no
  transparency, no hide-on-scroll; it simply sits over the hero (which is 100svh behind it).
  Padding `0 10%` (12px vertical + 5% ≤479). Subpages push content down with
  `margin-top: 60px` on `.section-subpage-hero`.
- Contents: 71×28 wordmark SVG left; five Inter 14px/500 links centred in a `.w-container`
  (max 940px) — **Visit · Sermons · Crews · Serve · Give**; a 44×44 hamburger right
  (two bars: 35px and 20px wide, 3px tall, offset so the shorter bar is right-aligned).
- The hamburger opens a **mega-menu panel** `.open-menu` on every breakpoint, including
  desktop: `position:absolute; top:100%`, width 80% (90% ≤479), `padding 40px`,
  background `#fffffff2` + `backdrop-filter: blur(5px)`, bottom radii 20px. GSAP tween
  (IX3): from `y:-100%, opacity:0` to rest, **duration 0.5s** (`force3D`). The wrapper's
  z-index is lifted to 9000 only while `.menu-hamburger.is-open` via `:has()`, with a
  0.6s `transition-delay` on close so the panel can animate back up.
- Hamburger morph: `::before/::after` bars animate `width/left/top/transform` with
  `0.3s cubic-bezier(0.4, 0, 0.2, 1)` into an X (both bars 35px, rotated ±45°).
- Panel contents: on mobile a repeat of the five primary links at Inter 28px/600; then a
  five-column row (`.nav-menu-row`) of h6 column heads — **New Here · Community · Grow ·
  Next Gen · Events** — each with 3–6 Inter 16px grey links (hover → black). Below: two
  mono uppercase 12px links with grey arrow icons: "NEED CARE? →" (opens modal) and
  "LOGIN →" (CCB).
- IX3 hover tweens on nav items: `.main-nav-link` scales to **1.125 in 0.05s, ease none**;
  mega-menu list items `.nav-link-collection-item` scale 1.125 in 0.25s; the arrow icon
  `.button-arrow` moves `x: 8px` and scales 1.125 in 0.5s. Links also carry CSS
  `transition: all .3s ease-out`.
- Mobile (≤991): the five columns collapse into **accordions** ("Title ›" rows, 16px
  vertical padding, 1px rgba(117,115,112,.1) dividers), chevron rotates -45°→45°, list
  height animates `0.3s cubic-bezier(0.33, 1, 0.68, 1)`. Outside click closes the menu.
- An events link in the menu auto-hides after its date (`navEvents`).
- Mobile menu font-size for the primary links: `--_typography---text-3xl` (28px).
- No skip link, no search, no language toggle in the header.

## 6. Hero treatment

- Full-viewport **video hero**, no headline. The only text is a bottom-left play block:
  a 48px circular play icon, then the overline `WATCH NOW` (12px mono, 4px tracking,
  gold) above the sermon title (h1 Inter Tight 36px/500, off-white; a CMS "series : title"
  pattern — two inline h1s + colon that hide when the series is empty). The block is an
  `<a>` to YouTube, 32px gap between icon and text, `inset: auto auto 10% 8%`.
- Left rail `.hero-socials` (top 15%, left 4%): YouTube, Instagram, TikTok icons (24px,
  white) stacked, a 70px 1px vertical line, and the word **FOLLOW** rotated -90°
  (`matrix(0,-1,1,0,0,0)`), mono, 4px tracking.
- Right rail `.hero-discover` (bottom 10%, right 1%, 16px column gap): three stacked
  chevrons SVG, the word **DISCOVER** rotated -90° (mono 14px/500, 4px tracking,
  40px top/bottom margin), a 70px vertical divider, a small cross icon, a single chevron.
  It is decorative; it is not a link.
- Entrance (Webflow IX2 presets): socials rail and discover rail use `slideInBottom`
  on SCROLL_INTO_VIEW (they start at `opacity:0` inline and slide up); the play block uses
  `fadeIn`. Both rails were static after load when sampled (no loop).
- Sunday logic ("Today at VOUS"): on Sundays in America/New_York, until the new sermon's
  loop (named by date, `/sermon_loops/YYYY/Month/MMDD web loop.webm`) is posted, the hero
  swaps to a church-online b-roll, the overline becomes the date ("Sunday, Sep 13th"),
  the title becomes "Today at VOUS" and the link points to /online. The title wrap is
  hidden via `html.tav-deciding` for up to 3s while that decision is made, to avoid a
  flash of the wrong title. `?tav=1` previews it.
- **Subpage heroes** `.section-subpage-hero`: `min-height: calc(100svh - 60px)`
  (75svh ≤991), centred 80px/600 white h1 over a looping b-roll `.mp4` with a poster.
  An `::after` layer in `--off-black` covers the video and clears when the clip can paint:
  `@keyframes vcBrollHold` (0–85% opaque, →0 at 100%, 4s linear) as a CSS fallback, or
  class `.broll-ready` with `transition: opacity 0.4s` from `hero-broll-preload.js`
  (listens to `loadeddata/canplay/playing/error/stalled`, 3s safety timeout; a cached
  load adds `.broll-instant` to skip the fade). Visit hero copy: "We can't wait to meet
  you"; Give: "Generosity is our privilege"; Crews: "VOUS Crews: Find Community" with two
  pill anchors beneath.

## 7. Video usage

| Where | Source | Attributes | Notes |
|---|---|---|---|
| Home hero | `cdn.vouschurch.com/CDN/sermon_loops/2026/November/1101 web loop.webm` (3840×2160) | `autoplay loop muted playsinline`, `preload="metadata"`, no poster | CMS-bound per sermon; `.video { aspect-ratio:16/9; object-fit:cover; min-height:100svh; max-width:100svw; z-index:-1 }` |
| Home hidden b-roll | `/CDN/video-loops/vous_high/vh-heor-roll.mp4` | same flags, `poster` (broken: points at the page URL) | inside `.hero-broll-embed.hide` — left over / preloaded for a sub-page **(inferred)** |
| Sunday swap | `/CDN/church-online/wiv-online-2026b.mp4` + jpg poster | set by script | see §6 |
| Visit hero | `/CDN/visit-vous/visitHeroLoop2026.mp4` | `autoplay loop muted playsinline`, poster, inline `object-fit:cover; opacity:0` until ready | black wash + fade in |
| Location "Preview" | YouTube iframe in a modal (`.vlp-frame` 16/9, max-width 1040px) | lazy, opened by the ▶ PREVIEW pill | overlay `rgba(10,9,9,.88)` + `blur(4px)`, fade 0.2s, dialog `translateY(8px)→0` 0.2s |
| Sermons | not embedded; "Sermons" links straight to YouTube (`@VOUSChurch`), /online for live | no iframes on the homepage at all |

Rules they follow: always muted/inline/looping, always a dark hold layer so the first
frame never flashes, WebM for the 4K hero, MP4 for subpages, YouTube only inside a
user-opened modal.

## 8. Animations & transitions

### Library inventory
GSAP 3.15 core + ScrollTrigger (hand-written), Webflow IX3 (nav/hover tweens via GSAP)
and IX2 presets (`fadeIn`, `slideInBottom`, dropdown/accordion height tweens), plain CSS
transitions, one CSS keyframe (`vcBrollHold`; Webflow's own `spin`), `IntersectionObserver`
for the gallery start, `requestAnimationFrame` for the row glide/fling.

### A. Section reveal on scroll (`home-card-reveal.js`, homepage only)
For `.section-visit, .section-mission, .section-calendar, .section-cta, .section-pastors,
.section-values` (gallery and footer excluded):
```
gsap.timeline({ defaults:{ ease:'power3.out' },
  scrollTrigger:{ trigger: section,
    start: phone ? 'top 92%' : 'top 88%',
    end:   phone ? 'bottom 50%' : 'bottom 45%',
    scrub: phone ? false : 0.65 } })
 .fromTo(section, { autoAlpha:0, y:72, scale: phone?1:0.985, force3D:true },
                  { autoAlpha:1, y:0, scale:1, duration:0.95 }, 0)
 .fromTo(directChildren, { autoAlpha:0, y:34 },
                  { autoAlpha:1, y:0, duration: phone?0.45:0.7, stagger:0.06 }, 0.04)
```
Desktop is **scrubbed** (0.65s lag) so the section rises with the scroll; phones play it
straight. Children skip the horizontal row itself (cards do their own), wrappers around a
row, and the `.vc-scroll-fade` overlays. `ScrollTrigger.refresh()` after binding; reduced
motion → everything just stays visible.

### B. Card reveal inside horizontal rows
Every card in the Visit, Calendar and Values rows:
`gsap.from(card, { opacity:0, duration:0.95, ease:'power3.out', paused:true })` —
**opacity only, no y** (a translate inside a horizontal scroller clipped the card and
added vertical overflow). Played by `flush()` in batches **0.07s apart**; on desktop a
card only plays once its left edge is ≥24px inside the row's right edge, so off-screen
cards still fade when dragged in. Phones reveal the whole row at once. Row trigger
`start: phone ? 'top 99%' : 'top 88%'`; scrolling back above the row resets the cards
(`onLeaveBack → pause(0)`), so it replays. Rows already in view are "primed" so nothing
stays hidden; a refresh handler snaps any tween whose trigger is past max scroll to
`progress(1)`.

### C. Hero stack-to-grid gallery (inline page script, GSAP core only)
Config: `gap 22, padding 18, desktopColumns 6, desktopRows 3, mobileColumns 3, mobileRows 6,
stackWidth 220, sizePattern [1.18,.9,1.05,.84,1.12,.96] ± sin-wave 0.08, min/max scale
.82/1.24, fadeDuration 0.12, fadeOverlap 0.18, settleDuration 0.05, moveDuration 0.28,
moveOverlap 0.06, desktopWideWidthVw 80 (≥1280)`.
Sequence: images primed absolutely at the stage centre at 220px wide, `autoAlpha:0`.
When the stage is ≥20% in view (4% on phones; rootMargin -10%/-3%), a timeline with
`defaults.ease 'power2.out'` fades them in reverse order (each 0.12s, overlapping by
0.18s), pauses 0.05s, then moves each to its grid slot with
`ease 'power2.inOut', duration 0.28`, staggered 0.06s, animating `left/top/width/height`
(not transforms). A follow-up override spreads each row edge-to-edge across the full
width (sizes kept, gaps absorb the slack). Resize re-lays out with `skipIntro`.
Mobile ignores height-only resizes (<8px width delta) to survive address-bar changes.

### D. Horizontal rows: arrows, drag, fling, edge fade (`side-scroll.js`, site-wide)
- Arrow click glides to the next card's `offsetLeft` (absolute stops, rebased on the
  first card), duration `clamp(200, 170 + |dist|·0.28, 420)` ms with **ease-out cubic**
  `1-(1-t)^3` (replaces native smooth scroll, measured at 337ms per 400px card and judged
  too slow at the tail). Second click measures from the in-flight target.
- Mouse drag: `pointerType === 'mouse'` only, 5px slop, `DRAG_SPEED 1.2`, pointer capture,
  cursor `grab/grabbing`; click suppressed after a drag. Release velocity from a 90ms
  sample window → **exponential fling, time constant 330ms**, capped at 2.2× row width;
  ignored below 8px.
- Arrows dim to `opacity .25` (`transition opacity .2s`) at either end; hidden scrollbar.
- Left edge fade `.vc-scroll-fade`: 108px wide, `backdrop-filter: blur(16px)`, background
  = section colour at 35% plus a solid 52px plateau fading over 26px, masked by a 12-stop
  gradient; toggled `.is-on` when `scrollLeft > 2px`, `transition opacity .25s ease-out`,
  hidden ≤479px. Starts 28px before the row's edge.
- Lazy card images get a reserved `aspect-ratio` (median of loaded siblings, default 1.43)
  so off-screen cards don't collapse.

### E. CSS micro-transitions
| Element | Transition | Hover result |
|---|---|---|
| `.button-default`, `.button-black`, `.button-white`, `.give-26-button` | `all .2s` / `transform .2s, box-shadow .2s` | `translateY(-4px)` + `box-shadow 0 2px 5px rgba(0,0,0,.2)` |
| `.div-location-card`, `.div-resource-card`, growth-track cards, `.div-more-vw-card` | `transform .28s cubic-bezier(.33,1,.68,1), box-shadow .28s …` | `translateY(-4px)` — only inside `@media (hover:hover) and (pointer:fine) and (min-width:992px)`, and only if the card is/contains a link |
| `.div-worship-music-card` | same | `translateY(-4px) scale(1.02)` |
| `.div-calendar-card` | same | card itself does **not** lift; its button lifts `translate(0,-4px)` + shadow (card with no button lifts instead) |
| `.div-cta-button-arrow`, `.link-scroll-title`, `.link-cta-button-arrow` | `all .2s` | `translate(4px)` (arrow label nudges right; `.is-back` nudges left) |
| IX2 "CTA Hover-in" | 200ms move x:4px, hover-out 100ms back | same idea, older pages |
| `.main-nav-link`, `.footer-link` | `all .3s ease-out` | colour / IX3 scale 1.125 |
| `.nav-link`, `.mobile-main-nav-link` | `all .3s` | grey → black |
| `.vlp-button` (PREVIEW pill) | `background-color .2s, transform .2s` | bg 92%→100% white, `translateY(-1px)` |
| `.vc-more` ("…" expander) | colour | brown → black; 2px focus ring |
| FAQ `.dropdown-faq-answer-block` | `height .3s cubic-bezier(.33,1,.68,1)` | plus icon `rotate(45deg)`, chevron `rotate(180deg)`, `transition transform .3s` same curve |
| IX2 accordion presets | open 500/300ms, close 300–400ms `inOutCubic` | height 0 ↔ auto |
| `.site-popup` | `opacity .3s ease` + `translateY(8px)→0` | appears bottom-right |
| `.vlp-overlay` / `.vlp-dialog` | `opacity .2s` / `transform .2s` | modal in |
| `.menu-wrapper` | `z-index 0s linear .6s` | stacking hand-off |

The house easing is **`cubic-bezier(0.33, 1, 0.68, 1)`** (ease-out cubic) at 0.28–0.3s
for anything hand-written; GSAP code uses `power3.out` (reveals) and `power2.out/inOut`
(gallery). Durations cluster at 0.2s (buttons), 0.28–0.3s (cards/accordions), 0.5s
(menu panel), 0.95s (reveals).

### F. Reduced motion
Every custom block has `@media (prefers-reduced-motion: reduce)` → `transition: none`,
hover transforms off, GSAP reveals skipped entirely (content visible), glide/fling replaced
by instant `scrollLeft`. Webflow's own CSS has no reduced-motion rules.

## 9. Interaction patterns

- **Buttons**: one family — outlined pill. `padding 16px 24px` (12px 24px for the small
  variant), `border 1px solid --off-black`, `border-radius 20px`, transparent background,
  Spline Sans Mono 14px/12px 500, 1px tracking, uppercase label. Variants: `.button-black`
  (filled off-black, white text, weight 600, line-height 1.5em), `.button-white` (white
  outline on dark), `.button-footer` (138px wide, 12px). Hover = lift 4px + soft shadow.
  Give page uses the same pill in filled form for "Give Now".
- **Text-link CTA**: mono uppercase 12px label + 40px long-arrow SVG, 16px gap, arrow
  nudges 4px on hover. Used in CTA boxes, calendar "Full Calendar", popup "CONNECT".
- **Cards**: white, square corners, generous padding (50–60px on location cards), content
  left-aligned, index numerals ("01") in mono, media on top, title/meta/body/CTA stack
  with 20px gaps; no borders or shadows at rest.
- **Carousels**: never a slider library — a native overflow row with hidden scrollbar,
  arrow pagers beneath (not overlaid), mouse drag + fling, left-edge blur fade, and
  per-card fade-in. One card per arrow click, snapped to card boundaries.
- **Accordions** (FAQ on /visit): title row with plus icon, 1px bottom border, height
  animated, one open at a time **(inferred)**.
- **Modals**: `.modal-overlay` fixed, `rgba(0,0,0,.6)` backdrop, `z-index 9999`, white
  card max-width 560px / max-height 90svh, `padding 40px`, h2 28px/600 title, short lead
  paragraph, Webflow form (inputs 16px Inter, `padding 12px`, radius 8px, border
  `1px solid #e8e6e3`, 20px between fields). Opened by `href="#id"` or `data-modal-open`,
  closes on backdrop, ✕, or Escape; focus moves in and is restored.
- **Site popup** "Connect with Us": fixed bottom-right (40px; 16px inset full-width on
  phones), 330px wide, frosted (`#fff6` + `blur(24px)`, 1px `#fff6` border, radius 20px,
  shadow `0 0 0 1px #1312121a, 0 10px 30px #13121229`), title 20px/500, copy 16px, mono
  CTA with arrow, ✕ close.
- **Sticky sub-nav** (campaign pages): `position: sticky; top: 80px` pill bar in `--gold`,
  radius 20px, links 16px/500, current link underlined.
- **"…" expander** on clamped card text: an inline button with a 320px fixed tooltip
  card (white, radius 12px, shadow `0 12px 32px rgba(0,0,0,.14)`, 14px/1.45).
- Focus styles: hand-written `:focus-visible` rings (2px, offset 2px) on custom controls.

## 10. Content & CTA strategy

- **Primary nav is verbs/outcomes**: Visit · Sermons · Crews · Serve · Give. "Sermons" goes
  straight to YouTube from the top bar (and to /collections from the mobile list).
- **Visitor-first**: the first scrolled section is "Visit VOUS — Join us every Sunday at
  one of our locations — LEARN MORE", with every campus card showing times, address and
  a video preview. The /visit page repeats the exact same section order
  (Times & Locations → Prayer Room → Calendar → VOUS is for you → Pastors → FAQ).
- **Identity statements** in the hero's absence of copy: the mission band and the seven
  values ("Jesus is our message", "People are our heart", "Generosity is our privilege",
  "Excellence is our spirit", "Servant Leadership is our identity", "Honor is our calling",
  "Passion is our pursuit") each with a short paragraph.
- **Next-step boxes**: "VOUS is for you" → Join a Crew / VOUS Kids / VOUS High — community,
  children, students, in that order.
- **Give**: one page, hero statement "Generosity is our privilege", then stacked blocks:
  Give (single/recurring, "Give Now"), Bricklayers Offering (annual above-and-beyond,
  "Give Now"), Stock & Crypto (two arrow links to Overflow), Mail a Check (address),
  "Building Legacy Together" annual-report block with a photo, then a contact email.
  Tone: plain, practical, tax-aware, no guilt copy.
- **Serve** = /grow ("Growth Track"), **Care** = modal "Need Care?" → Prayer Request /
  Support Request, surfaced in the menu, footer and popup. Prayer Request categories:
  Grief, Healing, Direction, Relationship, Provision, Salvation, Deliverance, Other.
- **Calendar** mixes church events, campaigns (building project), ordinances (baptism,
  child dedication), and products (album pre-save) in one row — "what's happening" rather
  than a strict events list. Every card has a verb button.
- **Footer** doubles as the ecosystem map: six sub-brands with their own logos.
- Bilingual signals: Spanish service (5PM ESP online), Spanish/Portuguese crew discussions,
  two FAQ entries in Spanish.
- Wording is short, warm, second person: "We can't wait to meet you", "Hugging is
  optional. We like you the way you are.", "No one should walk through life alone."

## 11. Secondary page templates

Common shell: fixed 60px white navbar, `section-subpage-hero` (100svh−60px video hero
with a single 80px headline), alternating 60px-padded off-white sections, same footer +
modals. Section intros reuse `.div-section-top-title` (centred 500px block). Every
horizontally scrolling list reuses `.div-scroll-wrapper` + arrows.

- **/visit** — hero "We can't wait to meet you" (video `visitHeroLoop2026.mp4`);
  "Times & Locations" (same six cards, numbered, with Apple/Google Maps "Get Directions"
  sheet); "Join us for Prayer Room every Wednesday" full-width card with photo background
  and three arrow links; Calendar row; "VOUS is for you" boxes; Our Pastors; FAQ accordion
  (8 questions, two in Spanish).
- **/give** — hero statement; stacked giving blocks each an h1 + one paragraph + pill
  button; stock/crypto as two white arrow buttons; annual report feature with photo;
  "VOUS Giving" explainer. No cards, no carousels — a calm vertical page.
- **/crews** — hero "VOUS Crews: Find Community" with two pill anchors (VOUS Crews / VOUS
  Care); "What are Crews?" intro + "Join a Crew" button; "Find a Crew for You" horizontal
  row of 7 crew-type cards (photo, name, "In Person / Online" h5, 3-line clamped copy,
  deep-linked `?type=`); a month calendar grid with "Crew Week #5/#6" markers; "Crew
  Discussions" in three languages as CTA boxes; the same pattern repeated for Care Crews
  (13 cards, each with Registration / Materials prices).
- Campaign pages (Vision, Bricklayers, VOUSCon) switch fonts and colours per
  "collection theme" variables (`--_collection-theme---font-display`, `---band`, `---accent`)
  — the core system is a neutral frame that lets event art take over.

## 12. Accessibility notes

Good:
- `role="banner"`, `role="navigation"`, `aria-label="home"` on the brand, `aria-expanded`
  on the hamburger and menu column heads, `role="button" tabindex="0"` on accordion heads.
- Hand-written focus rings (`:focus-visible` 2px) on custom buttons; modals manage focus,
  close on Escape, and lock body scroll.
- `prefers-reduced-motion` honoured by all custom motion; `(hover:hover) and (pointer:fine)`
  gates hover lifts off touch.
- 44×44 hamburger hit area; `-webkit-tap-highlight-color: transparent`.
- Calendar card images carry descriptive `alt`.

Weak:
- Most imagery has empty `alt=""`, including the logo in the navbar (link has aria-label,
  footer logo does not), location photos, social icons in the hero rail.
- Heading order is broken: multiple `h1`s per page (section titles are h1), h5 used for
  dates, h6 for menu headings, h2 numerals "01".
- Hero video has no pause control, no captions (it is muted b-roll, but still motion).
- Grey-on-white link text `#757370` on white ≈ 4.5:1 borderline; `#7e705f` on white
  passes; gold `#c6beab` overline on video varies with the frame.
- Arrow pagers are `<a href="#">` with no accessible name.
- Scrollbar hidden on rows with no keyboard affordance besides native tab-into-links.

## 13. Weaknesses to avoid

- Section titles as `h1` and dates as `h5` — use semantic levels and style with classes.
- Hero carries no headline or value statement; a first-time visitor must scroll to learn
  what the church is. Keep the cinematic video but add one line and a visible primary CTA.
- 4K `.webm` hero on every load (no `poster`, `preload="metadata"`); heavy on mobile data.
  Ship a poster, a 1080p file, and a reduced-motion/image fallback.
- "Sermons" in the top nav leaves the site for YouTube with no warning.
- Horizontal rows everywhere (three on the homepage) hide content behind a drag; the
  values list in particular would read better as a vertical list on desktop.
- The frosted "Connect with Us" popup covers the bottom-right of every page, including
  the hero's discover rail on phones.
- Fixed pixel type scale with no `clamp()` → 80px hero titles until 991px then a cliff to
  64px; a fluid scale would be smoother.
- A hidden second hero video (`.hero-broll-embed.hide`) still downloads.
- Card hover lift is suppressed on calendar cards but applied to their button, and the
  rule set needs `!important` guards and `:not(a):not(:has(a))` exceptions — a sign the
  hover system grew by patches.
- Empty alt text on meaningful photos; arrow pagers without labels.

## 14. Reusable patterns (concrete, codeable rules)

1. **Three-font system**: display sans (Inter Tight 500/600, tight 1–1.1 line-height)
   for headings; humanist sans (Inter 400/500) for UI and body; **monospace (Spline Sans
   Mono 400/500) for every label, date, address, overline and button**, uppercase with
   1px tracking (4px for overlines at 12px). Mono-as-metadata is the signature.
2. **Palette as four tokens**: page `#e8e6e3`, card `#fff`, ink `#131212`, accent pair
   `#c6beab` (gold) / `#7e705f` (brown). Everything else is photography.
3. **Type scale**: 12 / 14 / 16 / 20 / 22 / 24 / 28 / 36 / 48 / 64 / 80 px; hero title
   80→64→36 across 991/479px breakpoints; section h1 36px/1.1; body 20px weight 300.
4. **Spacing**: section padding 60px (40px mobile); side gutters 10% (15% ≥1440, 5% phone
   for chrome); section header block max-width 500px, 32px internal gap, 60px below
   (32px mobile); card internal gap 20px; card padding 50–60px desktop, 32px phone.
5. **Pill button**: `padding:16px 24px; border:1px solid currentColor; border-radius:20px;
   font:500 14px/20px "Spline Sans Mono"; letter-spacing:1px; text-transform:uppercase;
   transition:all .2s` and `:hover{transform:translateY(-4px); box-shadow:0 2px 5px
   rgba(0,0,0,.2)}`. Small variant 12px / `12px 24px`.
6. **Arrow link**: mono 12px uppercase label + 40px thin arrow SVG, `gap:16px`,
   `:hover{transform:translateX(4px)}` on the whole link, `transition:all .2s`.
7. **White square card** on a greige page: no border, no radius, no shadow; media
   full-width top (`object-fit:cover`), numeral "01" in mono above; lift on hover
   `translateY(-4px)` over `.28s cubic-bezier(.33,1,.68,1)` only under
   `(hover:hover) and (pointer:fine) and (min-width:992px)`.
8. **Native horizontal row**: `display:flex; gap:50px; overflow-x:auto; overflow-y:hidden;
   scrollbar-width:none; overscroll-behavior-x:contain`, cards `min-width:350px`
   (95% on phones). Pager arrows below the row; disabled state `opacity:.25`. Arrow
   click = glide to next card's `offsetLeft` in `200–420ms` ease-out cubic; mouse drag at
   1.2× with a 330ms exponential fling; left-edge blur fade (108px, blur 16px) when
   `scrollLeft > 2`.
9. **Scroll reveal recipe (GSAP)**: section `autoAlpha 0→1, y 72→0, scale .985→1,
   0.95s power3.out`, children `y 34→0, 0.7s, stagger .06`, trigger `top 88%` →
   `bottom 45%`, `scrub 0.65` on desktop, no scrub/no scale on phones (trigger `top 92%`).
   Cards in rows: **opacity-only** fade `0.95s power3.out`, batch stagger `0.07s`, gated on
   being ≥24px inside the row. Skip all of it under `prefers-reduced-motion`.
10. **Video hero**: `height:100svh; overflow:hidden`, `<video autoplay muted loop
    playsinline>` with `object-fit:cover; z-index:-1`; cover it with an `::after` in the
    ink colour that fades out `0.4s` on `loadeddata/canplay` (CSS keyframe fallback at
    4s); corner rails: socials + rotated "FOLLOW" top-left, rotated "DISCOVER" + chevrons
    bottom-right, play-block bottom-left at `8% / 10%` insets, 32px gap icon-to-text.
11. **Fixed solid header, 60px**, white, no shadow, links 14px/500 centred, wordmark left,
    44px hamburger right; mega-menu panel slides from `y:-100%, opacity:0` in 0.5s, 80%
    wide, `rgba(255,255,255,.95)` + `backdrop-filter:blur(5px)`, bottom radius 20px,
    five link columns with 20px/500 heads and 16px grey links; hamburger bars morph with
    `0.3s cubic-bezier(.4,0,.2,1)`; collapse columns into accordions ≤991px.
12. **Statement band**: one photo inside the gutters, dark, with a centred 36px/500
    light headline in two lines ("Our mission is simple: / …"). No button.
13. **Next-step trio**: photo left, three stacked white boxes right (h2 28px, 16px brown
    body, arrow link), each a single `<a>`.
14. **Stack-to-grid gallery**: 18 B&W photos, stage 630px tall (full width), prime at
    220px centred, fade in 0.12s each overlapping 0.18s, then move to a 6×3 grid with
    size pattern `[1.18,.9,1.05,.84,1.12,.96]`, 22px gap, `0.28s power2.inOut`,
    stagger 0.06; start at 20% intersection; relayout on resize without the intro.
15. **Modal + popup**: overlay `rgba(0,0,0,.6)`, card 560px/40px padding/white, title
    28px/600, inputs 12px padding radius 8px; popup 330px frosted (`#fff6`, blur 24px,
    radius 20px, 8px rise + 0.3s fade).
16. **Motion vocabulary**: 0.2s for hover, 0.28–0.3s `cubic-bezier(.33,1,.68,1)` for
    state changes, 0.5s for panels, ~1s `power3.out` for scroll reveals; movement amounts
    4px (hover), 8px (popup/arrow), 34–72px (reveals). Nothing bounces, nothing loops.
17. **Reduced-motion contract**: wrap every transition and every GSAP bind in
    `prefers-reduced-motion: reduce` checks; hover transforms only on
    `(hover:hover) and (pointer:fine)`.
18. **Content order for a church homepage** (as practised here): video hero → visit
    (times/locations) → mission statement → what's happening → next steps (groups,
    kids, students) → leadership → values → photo wall → footer with care/login/contact.
