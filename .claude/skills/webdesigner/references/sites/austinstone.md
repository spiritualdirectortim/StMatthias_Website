# The Austin Stone (austinstone.org) — design pattern study

Studied 2026-11-04. Sources: Firecrawl scrapes of `/` (rawHtml + screenshot), `/visit`, `/give`,
`/media/sermons`, `/about` (markdown + screenshot); the site's single compiled stylesheet
`austinstone-staging.webflow.shared.48c13ce11.min.css` (380 KB); the Webflow runtime chunk that
carries the site's IX2 interaction definitions (923 KB, 832 events / 105 action lists); one sermon
detail page. Firecrawl's `rawHtml` dropped the `<link rel="stylesheet">`, so the stylesheet and JS
bundles were fetched directly with curl. Note: Firecrawl's first `html` scrape of `/` returned a
cached page from a sibling Webflow template (rivervalley.org); it was discarded. Everything below
is from verified Austin Stone output. Items marked **(inference)** are not directly measured.

schunk.*.js, home-screenshot.png, about-screenshot.png, sermon.curl.html).

---

## 1. Platform & stack

- **Webflow** (CDN `cdn.prod.website-files.com`, site id `60ec2af571038318963f25b5`), with Webflow
  CMS collections for sermons, series, events, articles, music, podcasts, locations, team, FAQs.
- **Interactions: Webflow IX2** (no GSAP, AOS, Framer, Swiper, Lenis, Locomotive, Barba). All
  motion is IX2 action lists + a handful of CSS transitions + one CSS keyframe marquee.
- **Lottie** via Webflow's native Lottie plugin: the hamburger icon only
  (`lottieflow-menu-nav-08-ffffff-easey.json`, white and black variants, `data-renderer="svg"`,
  default duration 2.02 s, scrubbed by IX2 to frame 25/50 on open).
- **Finsweet Attributes v1** scripts: cmscombine, cmsfilter, cmsload, cmsnest, cmstabs,
  countitems, favcustom, sliderdots, cmssort, scrolldisable, copyclip. These power the filterable
  sermon/team archives ("Showing 938 out of 938", "Load More", "Reset Filters").
- jQuery 3.5.1 (Webflow default). Custom inline scripts: accordion keyboard/ARIA support, "close
  other open accordion", hamburger dropdown exclusivity, promo-bar hide rules, footer year.
- Third parties: Google Tag Manager/GA4 (first-party proxied path), OptinMonster (`omappapi`),
  Pushpay for giving, Simplecast for audio, Vimeo via Embedly for sermon video, Shopify for
  resources store, UltiPro for jobs, `my.austinstone.org` for login.
- Schema.org `Church` JSON-LD on the homepage. Favicons: light/dark variants.
- Fonts are **self-hosted woff2** on the Webflow CDN (no Google Fonts, no Typekit).

---

## 2. Typography

### Families (all `@font-face`, `font-display: swap`, woff2 only)
- **Proxima Nova** — the whole site. Weights loaded: 100, 300, 400, 500, 600, 700, 800, 900 plus
  italics. Stack: `font-family: Proxima Nova, Arial, sans-serif`.
- **Freight Text Pro** Medium + Medium Italic (500) — defined but used in only 2 rules (editorial
  accents / pull quotes; **inference**: the Ephesians 3:20 blockquote on /about).
- **Made Sunflower** (400) — one campaign class (`.text-size-3rem---h1.able` for the "ABLE" series).
- **Amarieta** (400) — one campaign rule. Both are series-branding one-offs, not system fonts.
- `webflow-icons` icon font (Webflow default).

### Base
- `body`: Proxima Nova, `1rem / 1.6rem`, color `var(--dark)` `#282828`.
- `p`: `1rem / 1.67rem`, weight 400, color `var(--body)` = `dimgrey` (#696969), margin-bottom 12px.
- `a`: color `var(--brand-blue)` `#00a3e1`, underlined, `1rem / 1.7rem`.

### Heading scale (desktop → ≤991 → ≤767 → ≤479)
| Element | Desktop | ≤991px | ≤767px | ≤479px |
|---|---|---|---|---|
| `.text-size-display.super` (home hero) | 7rem / 7.6rem, 700, -1px tracking | 6rem / 6.6rem | 5rem / 5.6rem | 4rem / 4.6rem (inline override: `clamp(2.5rem, -1.125rem + 10svh, 4rem)`, lh 1.15) |
| `.text-size-display` (page heroes) | 5rem / 5.6rem, 700, letter-spacing -1px | 4rem / 4.4rem | 3.6rem / 4rem | 2.8rem / 3.2rem |
| `.text-size-display.is-sermon-title` | 3.75rem / 4.25rem | 4rem / 4.4rem | 3.6rem / 4rem | 2.4rem / 2.9rem |
| `h1` / `.text-size-3rem---h1` (section titles) | 3rem / 3.6rem, 600 | 2.8rem / 3.4rem | 2.4rem / 3rem | 2.2rem / 2.8rem |
| `h2` | 2.4rem / 3rem, 600 | 2.2rem / 2.8rem | 2rem / 2.6rem | 1.8rem / 2.4rem |
| `h3` | 1.7rem / 2.3rem, 600 | 1.5rem / 2.1rem | | |
| `h4` / `.is-card-title` | 1.4rem / 2.1rem, 600 | 1.3rem / 2rem | | |
| `h5` / `.text-size-1-2rem---h5` | 1.2rem / 1.6–1.8rem, 600 | | | |
| `h6` / `.label-text` | 1rem / 1.6rem, 500, **uppercase, letter-spacing 2px** | | | |

Note the homepage hero on tablet/mobile also uses `svh`-based clamps injected as inline CSS:
`clamp(3rem, 10svh, 6rem)` at 768–991, `clamp(2.5rem, 9svh, 5rem)` at 480–767. This keeps the
two-line "We Are / The Austin Stone" headline inside a 100svh hero regardless of phone height.

### Casing, tracking, weights
- **Eyebrow labels** (`.label-text`, `.text-capitalize-all-caps`, `h6`): uppercase, `letter-spacing: 2px`,
  weight 500, 1rem. Used everywhere: "Welcome to The Austin Stone", "Current Sermon Series",
  "Latest from media", "Watch the Latest Sermon", nav column labels "media / ministry / explore".
- **Buttons**: uppercase, `letter-spacing: 2px` (3px on `.small`), weight 600, `.8rem` (`.7rem` small).
- Display headlines: Proxima Nova **700** with **-1px** tracking; section titles **600**; body 400;
  nav links 600 with `letter-spacing: .1px` and `text-transform: capitalize`.
- Card meta line (`.cms-item-text.line-3`): `#696969`, `letter-spacing: 1.2px`, `line-height 1.4rem`,
  pattern `11.4.26 | Announcements`, category uppercase.
- Footer links: `.9rem / 1.5rem`, 600, `rgba(255,255,255,.9)`, `letter-spacing .75px`.
- Secondary text on dark: `--white-paragraph: #b4bdca` (a cool grey, not pure white) and
  `rgba(255,255,255,.7)` (`.text-color-white-70`).

---

## 3. Color & imagery

### Tokens (`:root`)
```
--dark: #282828           primary text, dark sections, footer, default button
--body: dimgrey (#696969) paragraph text
--brand-blue: #00a3e1     links, hover fills, focus rings, tab underline
--lightest-gray: #f4f4f4  light section fill (.fill-light)
--white: white
--white-paragraph: #b4bdca
--dark-elevated: #3e3e3e   --dark-medium: #5e5e5e   --darkiesh-button: #333
--light-button: #dfdfdf    --light-slate-grey: darkgrey   --pinstripe: #94979e29
--promo-bar-body: #e9e9e9  --pure-black: black   --button: #252629ab
Sub-brand / ministry accents:
--for-the-nations #35b887  --institute #224d98  --counseling #487a7c  --for-the-city #c43b46
--creative #ffd100  --college #d1a02a  --kids #e31b48  --recovery #487a7c  --students #48c2c5
--marriage #00a3e1  --women #8c4799  --men #085e42  --advent-2026 #3c4331
```
- The palette is **near-monochrome**: charcoal `#282828`, white, `#f4f4f4`, one accent blue. Every
  ministry/initiative gets a single accent variable used for `.section.fill-*`, button hover
  borders, empty-image placeholders (`.collection-image.empty.*` with white icon on brand color).
- Navbar is translucent white: `background: #ffffffa3` + `backdrop-filter: blur(5px)`, switching to
  transparent over dark heroes (see §5).
- Dropdown mega-menu: white, `border-radius: 16px`, `box-shadow: 14px 14px 40px #00000012`.
- Hover tint on nav tiles: `rgb(236,242,238)` (a faint mint-grey).
- Focus ring: `outline: 2px solid rgb(0,163,225); outline-offset: 3px` (brand blue), `#282828`
  on brand-filled sections.

### Imagery
- Full-bleed **documentary congregation photography**: wide shots of people worshiping, hands
  raised, warm stage light, slightly desaturated/darkened (hero overlay). Heroes on `/`, `/about`,
  `/visit` all use the same recipe: photo + dark gradient/scrim, white type bottom-left.
- Formats: `.webp` and `.avif` throughout, Webflow responsive `srcset`.
- Icons: thin-line SVG glyphs (sermon, camera, album, mic, kids, students…) at 40px in the
  mega-menu, 24px arrows (`right-arrow.svg`) as the universal "go" affordance.
- Logo: hexagonal "stone" mark + wordmark "THE AUSTIN STONE" in caps; white/black/color variants
  cross-faded by IX2.
- Sermon-series art is square (1024×1024) + wide variants; cards keep square thumbnails.

---

## 4. Layout & page structure

### Grid/spacing system
- `.section { padding: 7.5rem 7.5rem 0 }` desktop (120px); `5rem` at ≤991; `4rem` at ≤767. Dark
  sections add matching bottom padding. Spacing utilities are literal: `bottom-padding---7-5rem`,
  `top-margin---1-5rem`, `c---2-5rem r---4rem` (column/row gap), `grid---3`, `grid---6---hero`.
- `.hero-grid` margins `7.5rem` desktop → `80px` (≤991) → `4rem`/`3rem` on phones. So the content
  gutter is **120px desktop, 80px tablet, 64px/48px mobile**.
- `.container { width: 1920px; max-width: 100%; padding: 120px }`; at ≥1920 `.wrapper` caps at
  **1440px** centered. Everything else is fluid to the viewport.
- Grids: `grid---3` = `1fr 1fr 1fr` (collapses to 2 cols at ≤991 for `.c---2-5rem.r---4rem`, 1 col at
  ≤767). `grid---6---hero` is a 6-column hero overlay grid with 120px top/bottom tracks.
  Footer = 6 equal columns → 2 columns at ≤479.
- Breakpoints (Webflow defaults): **991px, 767px, 479px**, plus a **1920px** up-size query.
- Card radii: images square-cornered (`border-radius: 0` on hero sermon thumb, marquee images);
  only the mega-menu (16px), buttons (pill 100px) and brand cards (`radius---16`) are rounded.

### Homepage, section by section (desktop)
1. **Navbar** (fixed, 7.5rem tall, 5% side padding, logo left, 6 links + pill "VISIT" right).
2. **Hero** `header.hero` — `height: 100vh; max-height: 80vw` (so ultrawide screens don't get a
   short hero), `min-height: 100svh` ≤991. Grid rows `180px auto 1fr auto auto`. Left-bottom:
   eyebrow-less two-line display headline with a **word-cycling slot**, one sentence
   ("You're invited to join us this Sunday at one of our six locations."), buttons
   **VISIT** (white pill) + **GET INVOLVED** (white ghost). Right-bottom: "WATCH THE LATEST SERMON"
   label over a 20rem-wide series thumbnail with a 50px dark play circle. `h1.sr-only` carries
   the real heading; the visible lines are `div`s.
3. **Welcome strip** — `label-text` "Welcome to The Austin Stone", `h2.text-size-3rem---h1`
   "We're one church with six congregations…", buttons **Visit** (dark pill) + **About us** (ghost).
4. **Marquee** — `section-marquee` 30em tall, 6 photos in a 2× duplicated CMS list, continuous
   leftward scroll (see §8).
5. **What's Happening** (`#whats-happening`, `.fill-light` grey) — 3-col grid: left column intro
   ("Let's walk with Jesus together!" + small **GET INVOLVED** button); right: event list rows
   with a stacked **MON / DD** date block, "EVENT" label, title, arrow. Rows separated by
   `1px solid #b4bdca80`, 1.5rem padding. Below: "Current Sermon Series" feature (wide art, title,
   blurb, **EXPLORE SERIES**). A `split-section-background` makes the top half light and lets the
   next dark block overlap.
6. **You are welcome here.** (`section.dark`) — 3-col `is-home-welcome` max-width 64rem: copy block
   left (max 26rem), photo right, buttons **VISIT** + **GET INVOLVED** (white / white ghost).
7. **Latest from media** (`.fill-light`) — label + `h2`, **tab menu** (Articles · Music · Podcasts ·
   Resources · Sermons · Videos), each pane a 3-up card grid (`grid---3 c---2-5rem r---4rem`,
   shows 2 at tablet) + "View All …" button.
8. **Footer** (`section.dark.footer`) — logo row + 6 link columns (About, Get Involved, Locations,
   Media, Ministries, Initiatives) with blue column headers, bottom row: legal text, 7 social icons
   (32px grid, 16px gap), "Contact Us" arrow link. Section titles in footer use `--brand-blue`.
9. Optional **promo bar** (fixed bottom, dark, `padding 12px 40px`, 1.25rem bold heading +
   .875rem body + CTA + close) that hides itself on its own target page and when the footer
   scrolls into view.

### Secondary pages (see §11) all follow: full-bleed photo hero (`.hero` + `.hero-grid` variant)
→ alternating `.section` / `.section.fill-light` / `.section.dark` blocks → closing CTA band →
"Follow us" + "Contact Us" → footer.

---

## 5. Navigation & header behavior

- **Structure**: `.navbar` fixed, `z-index: 2000`, `display:flex; justify-content:space-between`,
  `height: 7.5rem` (80px ≤991, 64px ≤767, 48px ≤479). Links: About · Media ▾ · Ministries ▾ ·
  Get Involved ▾ · Give · Log In · **VISIT** (`.button.small.new-here-button`, dark pill, hover
  brand-blue).
- **Mega-menu dropdowns** (`.dropdown-list.nav`): `position: fixed; inset: 120px 120px auto`
  (full-width panel 120px from each edge), white, radius 16px, big shadow. Inside: a row of
  `.nav-item-special` tiles (`padding: 40px 24px`, right border `#d4d6df`), each = 40px icon,
  eyebrow ("media"), title ("Sermons"), and a hidden second label ("explore") that slides up on
  hover. Get Involved tiles use verb eyebrows: *Take* Classes, *Attend* Events, *Join* Groups,
  *Go* Mission Trips, *Learn* Programs, *Lead* Residencies, *Serve* Volunteer.
- **Open animation** (IX2 "Main Nav Link Hover On"): panel starts `opacity 0, height 0,
  display none`; → `display block` → fade in 200ms `ease` and tiles fade in sequentially
  (each 500ms, staggered **(inference from per-tile opacity items)**). Close is the reverse.
- **Tile hover** (IX2 "Nav Item Hover On", 500ms `outQuint`): the `.nav-content-animate` stack moves
  `translateY(-2em)` inside a 4em-tall `overflow:hidden` container, swapping the top label for
  "explore"; the 24px arrow slides in from `-1em` to 0 while fading 0→1; **sibling** tiles' background
  turns `rgb(236,242,238)`, hovered tile stays white.
- **Logo hover**: color logo fades in over 300ms `ease`, mark scales to `0.975` over 500ms `outCubic`.
- **Hide on scroll down / show on scroll up** (IX2 "Nav scroll - leave/return"): `translateY(-100%)`
  over **700ms `outCubic`**; trigger at 24% page scroll down / 12% up on the homepage (12%/4% on
  most other pages).
- **Dark-hero color mode** (IX2 "HERO DARK - Scroll In (12%) / Scroll Out (72%)"): while the hero is
  in view, nav links are white and the navbar background transparent; when the hero leaves
  (72% threshold) links return to dark and the bar gets its white translucent fill. Transition
  **1000ms `outCubic`** in, **500ms** out. Hamburger icon swaps white/dark Lottie instances the same
  way (`display` toggled with opacity fades).
- **Mobile (≤991)**: desktop links hidden; `.hamburger-menu-container` fixed top-right 5rem square
  with Lottie icon; full-screen `.hamburger-nav-container` (dark `#282828`, 100vw × 100vh) opens via
  IX2 "Ham Nav / White Opens": width animates 0→100vw over **1000ms `outCubic`** while the Lottie
  scrubs to 25% then 50%; the link grid fades in. Items: Give, About, then collapsible groups
  (Get Involved, Locations, Media, Ministries, Initiatives) with rotating chevrons, 1.6rem/600 main
  links, 1.2rem/500 sublinks in `rgba(255,255,255,.8)`, then **VISIT** + **LOG IN** buttons. jQuery
  ensures only one group is open.
- Nav items on desktop get `.nav-item.upper { padding: 5px 2rem; transition: all .2s }` and hover
  color `--brand-blue`.
- Skip-link / `sr-only` utility present; `:focus-visible` rings are defined for tabs, slider arrows,
  nav buttons, inputs.

---

## 6. Hero treatment

- **Homepage**: static photo (`.hero-slider-image`, `object-fit: cover; position:absolute; inset:0`)
  with the dark scrim, no video. Content pinned to the bottom-left by the grid rows
  `180px auto 1fr auto auto`. The two display lines sit in `.hero-home---text-animation-container`
  (`height: 8rem; overflow: hidden`) — a **vertical word-cycler**: lines "We Are" / "One Church" /
  "Six Congregations" stacked 8rem apart; IX2 "Home Hero Load" (PAGE_FINISH, desktop only)
  moves the stack `translateY(-8rem)` after a **3000ms delay over 1000ms `outCubic`**, then
  `-16rem` after another **1500ms**. Below it the fixed second line "The Austin Stone".
  Result: "We Are The Austin Stone" → "One Church The Austin Stone" → "Six Congregations…".
  On tablet/mobile the extra lines are `display:none` (`.tab---hide`) and the cycler is off.
- **Page-load reveal** (IX2 "Slider - Page Finishes Loading v2", all breakpoints): hero text
  blocks start `opacity 0; translateY(5rem)`, hamburger starts `translateY(-100%)`, jump-link
  containers start `translateY(2.5rem)`; everything resolves on load (500ms default steps
  **(inference: exact easing of the resolve group not captured)**).
- **Latest-sermon chip**: `label-text` + 20rem image + centered 50px dark play circle.
  Hover (IX2 "Home Hero Sermon - Hover In"): `scale(1.1)` over **300ms `ease`**; "Homepage Hero -
  Series Hover On" additionally lifts the label `translateY(-2.1rem)` 500ms `outCubic`.
- **Secondary heroes** (`/about`, `/visit`, locations): same photo-scrim recipe, one-line
  `text-size-display` (5rem), two pill buttons (e.g. **MEET OUR TEAM** / **WHAT WE BELIEVE**),
  `.hero { height:100vh; max-height:80vw }`. Sermon pages use `.hero.sermon` with
  `.text-size-display.is-sermon-title` (3.75rem) and series art.
- Hero buttons on dark: `.button.white` (white fill, dark text) + `.button.white.ghost`
  (2px `darkgrey` border → brand-blue fill on hover).

---

## 7. Video usage

- **No autoplay/background video anywhere observed.** The homepage hero is a still photo. (The
  `<video autoplay muted loop playsinline>` tag seen in the first scrape belonged to the
  mis-served River Valley page, not Austin Stone.)
- **Sermon video**: Vimeo, embedded through **Embedly** (`cdn.embedly.com/widgets/media.html?src=
  player.vimeo.com/video/…`) inside a Webflow rich-text/`w-lightbox` block; posters come from
  `i.vimeocdn.com`. Audio per congregation via **Simplecast** iframes (`height: 200px; width: 100%`,
  `loading="lazy"`, `data-src` swapped in by tabs). Sermon cards expose Video / ASL / Audio flags.
- **Play affordance** pattern: `.play-parent` 40px (64px `.large`, 50px `.home-sermon`) absolutely
  centered; `.play-circle-main` dark `#282828` circle `border-radius: 100px` (white on `.large`)
  with a small triangle SVG. "Video Thumbnail Hover In": `opacity .9` + `scale(1.1)` 200ms `easeOut`.
- **Lottie** is the only "video-like" asset: hamburger icon JSON (two color variants).
- Media hub is tabbed, not autoplaying: Articles, Music (Spotify/Apple links), Podcasts,
  Resources, Sermons, Videos.

---

## 8. Animations & transitions

### Library & global rules
- Webflow IX2 for everything stateful; CSS `transition` for buttons/links/tabs; one CSS
  `@keyframes` for the marquee (plus Webflow's `spin`).
- IX2 totals: 832 events (250 MOUSE_OVER / 246 MOUSE_OUT / 60 click / 54 scroll-down / 47 scroll-up /
  40 SCROLL_INTO_VIEW / 38 SCROLL_OUT_OF_VIEW / 14 slider / 5 PAGE_FINISH / 1 PAGE_START /
  10 scroll-progress continuous groups).
- **Durations used**: 500ms (default, 386×), 300ms, 400ms, 200ms, 700ms, 800ms, 1000ms, 1500ms.
- **Easings used**: `outCubic` (241×, the house easing), `outQuint` (49), `ease` (38), `outQuart`,
  `easeIn`, `easeInOut`, `inQuart`, `inQuad`, `outSine`.
- **CSS transitions**: buttons `all .48s cubic-bezier(.509,-.005,.111,1.007)` (a slight
  anticipation curve, 480ms); nav/tabs/footer links `all .2s`; promo bar `opacity .3s, transform .3s`;
  misc `all .3s`, `background-color .4s`.
- **Reduced motion**: only the marquee respects it (`@media (prefers-reduced-motion: reduce)
  { .marquee-track { animation: none } }`). IX2 interactions have no reduced-motion guard — a
  weakness (see §13).

### Catalogue (what moves · trigger · values)
| Motion | Trigger | Values |
|---|---|---|
| Hero word cycler | PAGE_FINISH (desktop) | `translateY` 0 → -8rem → -16rem; delays 3000ms, 1500ms; 1000ms `outCubic` |
| Hero/page-load reveal | PAGE_FINISH | text `opacity 0, y 5rem` → visible; jump-links `y 2.5rem` → 0; 500ms steps |
| Navbar hide/show | PAGE_SCROLL_DOWN 24% / UP 12% | `translateY(-100%)` ↔ 0, 700ms `outCubic` |
| Navbar dark↔light mode | hero SCROLL_INTO_VIEW 12% / OUT 72% | nav text color white↔dark, bg transparent↔`#fff`, 1000ms `outCubic` in / 500ms out |
| Navbar white fill (some pages) | PAGE_SCROLL_DOWN 12–20% | bg `rgba(255,255,255,0)` → `.65`, 500ms `easeIn` |
| Mega-menu open | hover on nav item | `display block` → opacity 200ms `ease`; tiles 500ms |
| Mega-menu tile hover | hover `.nav-item-special` | content `y -2em`, arrow `x -1em→0` + fade, siblings bg `#ecf2ee`; 500ms `outQuint` |
| Logo hover | hover `.nav-logo---full` | color logo fade 300ms `ease`, scale .975 500ms `outCubic` |
| Marquee | always | `translateX(0 → -50%)`, **40s linear infinite**, pauses on `:hover` / `:focus-within`, `will-change: transform`, radius 12px |
| Card hover (media/CMS) | hover card | image `scale(1.05)` 300ms `outQuad` + `translateX(6px)` 300ms `outQuart`; out: `inQuad`/`inQuart` 300ms |
| Card hover (alt "CMS Card Hover On") | hover card | image `scale(1.25)` 500ms `outQuart`, custom cursor dot scales, grayscale filter 0% |
| List-row hover ("What's Happening", "Give", "Directions", "Email") | hover row | arrow `translateX(6px)` 300ms `outQuart`; out 300ms `inQuart` |
| Arrow nudge | hover link | `translateX(.25rem)` 200ms `outQuart`; out 200ms `inQuad` |
| Back button | hover | icon `translateX(-6px)` 300ms `outQuart` |
| Team photo hover | hover team card | image `scale(1.1)` + `opacity .7` 400ms `outCubic`, round overlay `rgba(27,30,46,.8)`, icon set fades in 400ms `ease` |
| Ministries feature hover | hover | text block `y -3rem` 500ms `outCubic`, image `scale(1.2)` 1000ms `outCubic`, corner icon slides in |
| Hero sermon chip | hover | `scale(1.1)` 300ms `ease`; label `y -2.1rem` 500ms `outCubic` |
| Video thumb | hover | `opacity .9`, `scale(1.1)` 200ms `easeOut` |
| FAQ / accordion | click / 2nd click | chevron `rotate(90deg)`, panel height 0 → auto 500ms `easeInOut`, Lottie plus/minus scrub |
| Hamburger menu | click | width 0→100vw 1000ms `outCubic`, Lottie 0→25→50, link grid fade; chevrons rotate |
| Promo bar | footer in/out of view | fade + `translateY(20px)` 300ms `ease`, then `display none` after 300ms |
| "Latest Sermon - Rotate" | (series badge) | 0→180→360deg, 8000ms per half, linear (slow spinning badge) |
| Sticky feature (locations/new-here) | SCROLLING_IN_VIEW | scroll-progress keyframes (34%, 38%, …) cross-fading images/opacity, `smoothing` 50–100 |
| Slider timer bar | slider active | progress width over slide duration |
| Tabs | click | underline switches (`border-bottom: 2px solid --brand-blue`), 200ms |

### Motion grammar (what the above adds up to)
- Default: **500ms `outCubic`** for enter, 300ms `in*` for exit. Hovers 200–300ms. Big reveals
  700–1000ms. Nothing bounces or overshoots except the button's custom bezier (`-0.005` /
  `1.007` — effectively linear-ish with a hair of snap).
- Hover language = **small translate (6px / .25rem / -1em) on an arrow + subtle scale
  (1.05–1.1) on an image**, never color flashes.
- Text "swap" effects are done with **masked vertical slides** (`overflow:hidden` container of
  fixed `height`, child moved by exact em/rem multiples), both in the hero and in nav tiles.
- The site treats reveal animation sparingly: the only scroll-triggered "fade up" is the hero
  load; sections do not animate in one by one.

---

## 9. Interaction patterns

### Buttons
```
.button            bg #282828, color #fff, pill (radius 100px), padding 16px 32px,
                   .8rem/1.2rem, 600, uppercase, letter-spacing 2px, white-space nowrap,
                   transition all .48s cubic-bezier(.509,-.005,.111,1.007); hover bg #00a3e1
.button.small      padding 12px 24px, .7rem, letter-spacing 3px
.button.white      bg #fff, color #282828; hover bg #00a3e1 color #fff
.button.white.ghost  transparent, 2px solid darkgrey, padding 14px 30px; hover brand-blue fill+border
.button.ghost      1px solid darkgrey, dark text, transparent; hover rgba(9,11,25,.1)
.button.black.ghost  border #696969, padding 15px 31px
.button.lightest   bg #f4f4f4 dark text
.icon-only         48×48 circle
Sub-brand variants (.counseling, .city, .nations, .institute, .creative) swap the hover color.
≤479px: white-space: normal (buttons may wrap).
```
Button groups: `.button-group` flex row, `top-margin---1-5rem`; 2 buttons max, primary filled +
secondary ghost; on hero wrap with `gap: .75rem` and padding reduced to 1.25rem.

### Cards
- `.collection-item-container---link`: CSS grid, `row-gap 8px`, no border, no shadow, no radius.
  Image (`.collection-image`, `object-fit: cover`, absolutely positioned in an aspect wrapper) →
  meta line (`date | Category`, uppercase, 1.2px tracking, #696969) → title (`h3.is-card-title`,
  1.4rem/2.1rem, 2-line clamp class `line-2`) → "View" text link. Whole card is the anchor.
- Hover = image scale + 6px arrow shift (see §8). Empty-image fallback = brand-colored block with
  white icon.
- Event rows: horizontal 6-col grid, hairline divider, stacked date, label, title, arrow.
- Location cards (/visit): photo, `h3` name, clock icon + "Services: 9am | 11am", pin icon +
  bold address, mail icon + email, "Learn more about Downtown" link.
- Give-method cards: icon image, `h3`, fee line ("$0.49 per transaction"), "Recommended" tag,
  "Give now →".

### Tabs, filters, accordions
- Tabs: text links with 2px bottom border on current; `margin-right 24px`, `padding-bottom 12px`,
  500 → 600 when active, color `--body` → `--dark`, hover `--brand-blue`.
- Archive filters (Finsweet): dropdown chips Series / Book / Preacher / Format / Year, result
  count "Showing 938 out of 938", "Reset Filters" with circular-arrow icon, "Load More" pagination,
  friendly empty state with illustration ("Sorry, we don't seem to have any matches…").
- Accordions: `.accordion-toggle` reset button, question 1.5rem/500, `overflow:hidden` answer
  container, one-open-at-a-time, keyboard + ARIA added by custom script.

### Cursor
- A custom cursor (`.cursor__dot`, `.cursor__arrow`) exists on slider pages: dot scales to 0.1 and
  an arrow appears/rotates over prev/next zones (500ms `outQuint`). Not on the homepage.

---

## 10. Content & CTA strategy

- **Visitor-first**: the single persistent CTA is **VISIT** (nav pill, hero primary, welcome strip,
  "You are welcome here" band, About closing band "Planning to visit…?", Visit page closing band).
  Secondary CTA everywhere is **GET INVOLVED** (one hub page with anchors #classes #events
  #groups #mission-trips #programs #residencies #volunteer).
- Hero copy is identity + invitation in one breath: "We Are The Austin Stone" / "You're invited
  to join us this Sunday at one of our six locations." Headline cycles One Church → Six
  Congregations to teach the multi-site model without a paragraph.
- Section headlines are short, plain, second person: "You are welcome here.", "What's Happening",
  "Want to get involved…?", "Planning to visit…?". Eyebrows carry the taxonomy.
- **Give**: top-level nav item, dedicated page ordered Why → Ways (ACH recommended, with fees
  disclosed) → Other ways → What giving supports (audited financials PDFs, ECFA badge) → FAQ →
  closing "Give now" + "contact us". Actual transaction is off-site (Pushpay). Give is *not* in
  the hero or homepage body; it lives in nav + footer only.
- **Watch**: "Watch the Latest Sermon" chip in the hero; "Current Sermon Series" block; Sermons tab
  in media feed; Media mega-menu first tile = Sermons.
- **Serve**: framed as "Volunteer" under Get Involved with the eyebrow verb "Serve".
- **Locations**: "One Church, Six Locations" is the organizing message; Visit page = 6 location
  cards with identical service times, address, email, link; location pages exist per congregation.
- Every page ends with a **contextual CTA band → "Follow us" (Facebook, Instagram) → "Contact Us →"
  mailto with subject prefilled → footer**.
- Microcopy habits: lowercase button labels in source ("get involved", "explore Series", "our
  sermons") rendered uppercase by CSS; dates as `11.4.26`; "Learn more about {Location}".

---

## 11. Secondary page templates

### /visit
Hero → intro ("Welcome to The Austin Stone", mission paragraph, **about us** button) → eyebrow
"Join us this Sunday" + `h2` "One Church, Six Locations" + 6 location cards → "What to Expect on
Sundays": 5 alternating image/text rows each with an eyebrow (You belong here / God still speaks /
The right response / Grow your community / For all ages), `h3`, paragraph, contextual button
(our sermons, our music, Get involved, kids + students) → thumbnail strip of the 5 images (sticky
feature on desktop **(inference)**) → CTA band "Want to get involved…?" → Follow us → Contact.

### /about
Hero "About The Austin Stone" + **MEET OUR TEAM** / **WHAT WE BELIEVE** → "Established in 2002"
stat line + mission sentence → Who we are / One Church, Six Locations → What We Believe: two
2-column bullet lists (Convictions, Affirmation of Faith) → two square photos → Our story in three
`h3` beats (How It Started / How We've Grown / Where We're Going) → "Our name" essay → Ephesians
3:20 pull quote (Freight Text Pro italic, **inference**) → full-bleed break image → **Our Team**:
Finsweet-filtered directory (Role / Division / Congregation / Ministry / Initiative), 457 people,
circular photos, name, role, Email link, Load More → CTA band "Planning to visit…?" → footer.

### /give
Hero (`.text-size-display.is-give-hero` max-width 7.5em) + sub-line "Responding to the gift of
mercy…" → Why We Give (2 `h3` columns) → Ways to Give (3 cards + "Other Ways" accordion) → two
square photos → What Giving Supports (PDF links, ECFA) → FAQ accordion (8 items) → CTA band.

### /media/sermons
Hero with featured image + eyebrow "Ruled by God's Word" + paragraph → tabs **Sermons | Sermon
Series** → filter bar + count + reset → card grid (square art, `date | Series`, bold title, "View",
format badges Video/ASL/Audio, reference) → Load More → Series grid (Current/Upcoming badges,
year, title, "View Series").

### /sermons/{slug}
`.hero.sermon` with series art + `h1.is-sermon-title` → Vimeo (Embedly) video in lightbox block →
per-congregation Simplecast audio tabs → "Discussion Guide" `h2` → "Sermon Details" card
(reference, date, book, preachers) → footer.

---

## 12. Accessibility notes

Good:
- `h1.sr-only` on the homepage so the animated display text doesn't produce a broken heading.
- Explicit `:focus-visible` outlines (2px brand blue, 3px offset) on tabs, slider arrows, nav
  button, inputs, dropdown toggles; dark variant inside brand-filled sections.
- Custom script converts IX2 click accordions into real buttons with keyboard + ARIA.
- Marquee pauses on hover/focus-within and honors `prefers-reduced-motion`.
- Lazy-loaded iframes, descriptive iframe `title`s, alt text on most content images
  ("Austin Stone congregation worshiping together").

Gaps:
- Decorative images and many icons have `alt=""` (fine) but several content images (location
  photos, marquee) also have empty alt.
- IX2 motion (hero cycler, nav hide, hovers, hamburger) ignores `prefers-reduced-motion`.
- Navbar auto-hide on scroll can hide the only visible navigation on long pages; mobile relies on
  a 48px-tall bar at ≤479.
- Visible headline is `div`s; nav tiles use `div.nav-title` not list semantics.
- Hero buttons use `white-space: nowrap` until 479px; long translations would overflow.
- Body copy on dark uses `#b4bdca` on `#282828` (~7:1, fine) but `rgba(255,255,255,.7)` on
  photos depends on the scrim.

---

## 13. Weaknesses to avoid

1. **Utility-class soup**: `bottom-margin---1rem.is-card-title`, `.grid---3.c---2-5rem.r---4rem`,
   `.button.white.ghost.small.hover-city` — hundreds of compound selectors and `!important`
   overrides in inline `<style>` blocks. Use tokens + a few variants instead.
2. **Single 380 KB stylesheet** plus a 923 KB interactions bundle and 11 Finsweet scripts; heavy
   for a church site. Keep interactions in a few dozen lines of IntersectionObserver/CSS.
3. **Duplicated media feeds**: the homepage renders 6 tab panes × 3 cards (18 cards + 6 CMS lists)
   plus hidden duplicate event rows for Finsweet; most of it is never seen.
4. **Hover-only mega-menu** with 1000+ IX2 opacity items; touch users get a different (hamburger)
   system — two navs to maintain.
5. Reduced-motion not respected by IX2; headline cycling runs forever on load **(inference:
   it plays once per load, 3 states, then stops — verify)**.
6. Hard-coded pixel tracks (`120px` rows, `inset: 120px 120px auto`) tied to the 7.5rem navbar;
   any navbar height change breaks dropdown placement.
7. Empty `data-src=""` iframes shipped for congregations with no audio; "Boomtown Test" content
   visible in the public sermon list.
8. Give page hero headline forced to `max-width: 7.5em` — brittle for other languages.
9. Dates `11.4.26` are ambiguous outside the US.

---

## 14. Reusable patterns (codeable rules)

### Tokens
```css
:root{
  --ink:#282828; --body:#696969; --accent:#00a3e1; --paper:#fff; --paper-2:#f4f4f4;
  --ink-2:#3e3e3e; --ink-3:#5e5e5e; --on-dark-muted:#b4bdca; --hairline:#b4bdca80;
  --radius-pill:100px; --radius-panel:16px;
  --gutter:7.5rem;            /* 120px desktop */
  --section-y:7.5rem;
  --nav-h:7.5rem;
  --ease-out:cubic-bezier(.215,.61,.355,1);   /* outCubic */
  --ease-out-5:cubic-bezier(.23,1,.32,1);     /* outQuint */
  --btn-ease:cubic-bezier(.509,-.005,.111,1.007);
  --t-fast:200ms; --t-base:300ms; --t-slow:500ms; --t-reveal:700ms; --t-hero:1000ms;
}
@media(max-width:991px){:root{--gutter:5rem;--section-y:5rem;--nav-h:80px}}
@media(max-width:767px){:root{--gutter:4rem;--section-y:4rem;--nav-h:64px}}
@media(max-width:479px){:root{--gutter:3rem;--nav-h:48px}}
@media(min-width:1920px){.wrapper{max-width:1440px;margin-inline:auto}}
```

### Type
```css
body{font:400 1rem/1.6rem "Proxima Nova",Arial,sans-serif;color:var(--ink)}
p{color:var(--body);line-height:1.67rem;margin:0 0 12px}
.display{font-weight:700;letter-spacing:-1px;font-size:5rem;line-height:1.12}
.display--super{font-size:7rem;line-height:7.6rem}
.h1{font-size:3rem;line-height:3.6rem;font-weight:600}
.h2{font-size:2.4rem;line-height:3rem;font-weight:600}
.h3{font-size:1.7rem;line-height:2.3rem;font-weight:600}
.card-title{font-size:1.4rem;line-height:2.1rem;font-weight:600}
.eyebrow{font-size:1rem;line-height:1.6rem;font-weight:500;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px}
.meta{font-size:.9rem;letter-spacing:1.2px;color:var(--body);text-transform:uppercase}
@media(max-width:991px){.display{font-size:4rem}.display--super{font-size:6rem;line-height:6.6rem}.h1{font-size:2.8rem;line-height:3.4rem}.h2{font-size:2.2rem;line-height:2.8rem}}
@media(max-width:767px){.display{font-size:3.6rem}.display--super{font-size:5rem;line-height:5.6rem}.h1{font-size:2.4rem;line-height:3rem}.h2{font-size:2rem;line-height:2.6rem}}
@media(max-width:479px){.display{font-size:2.8rem;line-height:3.2rem}.display--super{font-size:clamp(2.5rem,-1.125rem + 10svh,4rem);line-height:1.15}.h1{font-size:2.2rem;line-height:2.8rem}.h2{font-size:1.8rem;line-height:2.4rem}}
```

### Button
```css
.btn{display:inline-flex;align-items:center;justify-content:center;padding:16px 32px;
  border-radius:var(--radius-pill);background:var(--ink);color:#fff;border:0;
  font:600 .8rem/1.2rem inherit;letter-spacing:2px;text-transform:uppercase;white-space:nowrap;
  text-decoration:none;transition:all .48s var(--btn-ease)}
.btn:hover{background:var(--accent)}
.btn--small{padding:12px 24px;font-size:.7rem;letter-spacing:3px}
.btn--white{background:#fff;color:var(--ink)} .btn--white:hover{background:var(--accent);color:#fff}
.btn--ghost{background:transparent;border:1px solid darkgrey;color:var(--ink)} .btn--ghost:hover{background:#090b191a}
.btn--ghost-white{background:transparent;border:2px solid rgba(255,255,255,.6);color:#fff;padding:14px 30px}
.btn--ghost-white:hover{border-color:var(--accent);background:var(--accent)}
@media(max-width:479px){.btn{white-space:normal;padding-inline:1.25rem}}
```

### Section rhythm
```css
.section{padding:var(--section-y) var(--gutter) 0;position:relative}
.section--dark{background:var(--ink);color:#fff;padding-bottom:var(--section-y)}
.section--light{background:var(--paper-2);padding-bottom:120px}
.split-bg{position:absolute;inset:auto 0 0;height:50%;z-index:0}   /* lets next block overlap */
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);column-gap:2.5rem;row-gap:4rem}
@media(max-width:991px){.grid-3{grid-template-columns:1fr 1fr}}
@media(max-width:767px){.grid-3{grid-template-columns:1fr;row-gap:0}}
.row{display:grid;grid-template-columns:repeat(6,1fr);padding-bottom:1.5rem;margin-bottom:1.5rem;border-bottom:1px solid var(--hairline)}
```

### Hero
```css
.hero{position:relative;display:flex;flex-direction:column;justify-content:center;
  height:100vh;max-height:80vw;overflow:hidden;color:#fff}
.hero__img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero__scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.25),rgba(0,0,0,.55))} /* inference */
.hero__grid{position:relative;z-index:3;display:grid;grid-template-rows:180px auto 1fr auto auto;
  margin-inline:var(--gutter);max-height:80vw}
.hero__chip{position:absolute;right:0;bottom:2.5rem;max-width:20rem}
@media(max-width:991px){.hero{height:auto;min-height:100svh;max-height:none}
  .hero__grid{display:flex;flex-direction:column;justify-content:center;margin:6rem 5rem 4rem}
  .hero__chip{position:static;align-self:flex-end;max-width:18rem}}
```
Word-cycler (hero or nav tile): fixed-height `overflow:hidden` mask; children stacked at exact
multiples of the mask height; animate `transform: translateY(-N × height)` with
`1000ms var(--ease-out)`, 3000ms initial delay, 1500ms between steps; disable under
`prefers-reduced-motion` and on viewports < 992px.

### Navbar behaviors (JS, replace IX2)
```js
// 1. hide on scroll down past 24% of viewport, show on scroll up (700ms outCubic)
// 2. toggle .nav--on-dark while hero intersects (threshold .12 in / .72 out), 1000ms in / 500ms out
// 3. nav background: transparent over hero, rgba(255,255,255,.64)+blur(5px) after
const nav=document.querySelector('.nav');let last=scrollY;
addEventListener('scroll',()=>{const y=scrollY,vh=innerHeight;
  nav.classList.toggle('nav--hidden',y>last&&y>vh*.24);if(y<last||y<vh*.12)nav.classList.remove('nav--hidden');last=y},{passive:true});
new IntersectionObserver(([e])=>nav.classList.toggle('nav--on-dark',e.intersectionRatio>.12),{threshold:[.12,.72]}).observe(document.querySelector('.hero'));
```
```css
.nav{position:fixed;inset:0 0 auto;height:var(--nav-h);padding:0 5%;display:flex;align-items:center;justify-content:space-between;
  z-index:2000;background:rgba(255,255,255,.64);backdrop-filter:blur(5px);
  transition:transform .7s var(--ease-out),background-color 1s var(--ease-out),color 1s var(--ease-out)}
.nav--hidden{transform:translateY(-100%)} .nav--on-dark{background:transparent;color:#fff}
.nav a{font-weight:600;letter-spacing:.1px;padding:5px 2rem;transition:color .2s} .nav a:hover{color:var(--accent)}
.mega{position:fixed;inset:var(--nav-h) 120px auto;background:#fff;border-radius:16px;box-shadow:14px 14px 40px #00000012;overflow:hidden}
.tile{padding:40px 24px;border-right:1px solid #d4d6df;transition:background .5s var(--ease-out-5)}
.tile:hover~.tile,.tile:has(~.tile:hover){background:#ecf2ee}
.tile__mask{height:4em;overflow:hidden;margin-top:2rem} .tile__stack{transition:transform .5s var(--ease-out-5)}
.tile:hover .tile__stack{transform:translateY(-2em)}
.tile__arrow{opacity:0;transform:translateX(-1em);transition:all .5s var(--ease-out-5)} .tile:hover .tile__arrow{opacity:1;transform:none}
```

### Card hover / arrow nudge
```css
.card img{transition:transform .3s cubic-bezier(.25,.46,.45,.94)}        /* outQuad */
.card:hover img{transform:scale(1.05)}
.card .arrow{transition:transform .3s cubic-bezier(.165,.84,.44,1)}       /* outQuart */
.card:hover .arrow{transform:translateX(6px)}
.card:not(:hover) img,.card:not(:hover) .arrow{transition-timing-function:cubic-bezier(.55,.085,.68,.53)} /* inQuad/inQuart out */
```

### Marquee
```css
.marquee{height:30em;overflow:hidden;position:relative}
.marquee__track{position:absolute;display:flex;white-space:nowrap;will-change:transform;
  animation:marquee 40s linear infinite}
.marquee:hover .marquee__track,.marquee:focus-within .marquee__track{animation-play-state:paused}
.marquee__item{flex:none;width:30em;margin-right:2rem} .marquee__item img{width:30em;height:30em;object-fit:cover}
@keyframes marquee{to{transform:translateX(-50%)}}   /* track = list duplicated once */
@media(prefers-reduced-motion:reduce){.marquee__track{animation:none}}
@media(max-width:767px){.marquee{height:24em;font-size:.7em}}
```

### Play button
```css
.play{position:absolute;inset:0;margin:auto;width:50px;height:50px;border-radius:50%;background:var(--ink);display:grid;place-items:center}
.play--large{width:64px;height:64px;background:#fff}
.thumb:hover .play-wrap{transform:scale(1.1);transition:transform .3s ease}
```

### Page-end module (every page)
eyebrow-less `h2` question ("Planning to visit…?") + one sentence + one pill button → "Follow us"
+ 2–3 social icons (32px) → "Contact Us →" mailto with prefilled subject → footer with
blue column headers (`color:var(--accent);margin-bottom:16px`) and `.9rem` 600 links whose
hover is a 1px bottom border in accent (`transition:all .2s`).

### Promo bar
Fixed bottom, `padding:12px 40px`, `box-shadow:0 -2px 12px #0000002e`, heading 1.25rem/700,
body .875rem `#e9e9e9`, pill CTA, 32px close; hide when the footer enters view
(fade + `translateY(20px)` 300ms, then `display:none`), hide on the CTA's own page, hide on
pages listed in `data-promo-exclude`, add `env(safe-area-inset-bottom)` on landscape phones.
