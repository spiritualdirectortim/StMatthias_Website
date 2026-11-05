# Anchor Church (anchortacoma.org) — design pattern study

Researched 2026-11-04. Sources: Firecrawl scrapes of `/`, `/visit`, `/give`, `/central`, `/teachings` (html, rawHtml, markdown, 1920x1080 screenshot), plus the first-party Webflow stylesheet `anchor-253.webflow.shared.a9077d86f.min.css` (292 KB) and the Webflow runtime chunk `webflow.schunk.4a5e09fe93c20d6b.js` (810 KB) which embeds the site's Interactions 2.0 (IX2) definitions. Values quoted as `px`, `rem`, `ms`, easing names, etc. are read directly from those files unless marked **(inference)**.

Note on method: Firecrawl's `html`/`rawHtml` output stripped the `<link rel="stylesheet">` tag, so the CSS URL was recovered from a direct fetch of the page head. Raw files are kept in

---

## 1. Platform & stack

- **Webflow** site (`data-wf-site="6420fa025220aa44780a0a7a"`, "Site by Sunday Best" credit in footer — a church-focused Webflow agency). Last published 2026-11-04.
- Built on the **Finsweet Client-First** class convention: `section_header`, `padding-global`, `container-large`, `padding-section-large`, `heading-style-h2`, `text-size-medium`, `margin-bottom margin-small`, `hide-mobile-landscape`, `icon-embed-xxsmall`, etc.
- CSS: one minified Webflow stylesheet. No CSS framework beyond Webflow's base. `:root` custom properties for colors.
- JS:
  - Webflow runtime (jQuery 3.5.1 bundled) + 3 chunks; IX2 interactions drive almost all motion.
  - `@finsweet/attributes-cmsslider@1` (turns a CMS collection into a Webflow slider) and `@finsweet/attributes-scrolldisable@1` (locks scroll while the menu is open).
  - jQuery 3.6.0 loaded separately (for small inline scripts: accordion, copyright year, "today" highlighting).
  - Google Analytics gtag `G-3QD7Z705PM` via first-party proxy.
  - A hand-written vanilla JS module (~190 lines, inline) that retrofits the Webflow mega-menu with proper dialog semantics, focus trap, `inert` on background, Escape-to-close, and staggered CSS reveal classes. This is the most "engineered" piece and is worth copying (see §5 and §13).
- Lottie: the hamburger icon is a Lottie JSON (`Lottie Menu.json`, 0.667 s default duration) played by IX2 `PLUGIN_LOTTIE` actions.
- Video: no `<video>` tags on any page scraped. Teaching video is a **YouTube playlist in a Webflow lightbox** (Embedly iframe). Livestream and location teachings link out to YouTube / Apple Podcasts.
- Giving is outsourced to **Planning Center Church Center** (`anchorgiving.churchcenter.com/giving`) and events registration to Church Center as well. Planned giving links to `inspire-giving.com`.
- JSON-LD: `WebPage`, `WebSite`, and `Church` schema with address, phone, email, `sameAs` socials, `subOrganization` for each campus. Good SEO hygiene.
- Images: `.webp` for most photography, served from Webflow CDN, `loading="eager"` nearly everywhere (a weakness; see §12).
- Fonts: self-hosted **Metropolis** (woff/eot/ttf, `font-display: swap`). No Google Fonts or Typekit.

---

## 2. Typography

### Families
- Single family: **Metropolis** (geometric grotesque, free/open license), `font-family: Metropolis, sans-serif` on `body`. Weights loaded: 400, 400 italic, 500, 500 italic, 600, 600 italic, 700. Weight usage in CSS: 500 (42 rules), 700 (38), 400 (16), 600 (7), 300 (2).
- `* { -webkit-font-smoothing: antialiased; }` globally.

### Root scale (fluid rem)
`html { font-size: 1rem }` with fluid overrides so every rem-based value scales with viewport:
```
@media (max-width:1440px) html { font-size: calc(0.398664rem + 0.668151vw); }
@media (max-width:991px)  html { font-size: calc(0.446987rem + 0.892857vw); }
@media (max-width:767px)  html { font-size: calc(0.334201rem + 1.38889vw); }
@media (max-width:479px)  html { font-size: calc(0.749477rem + 0.83682vw); }
```
At 1440 px that works out to 16 px; at 991 px ≈ 13.6 px; at 767 px ≈ 15.8 px; at 479 px ≈ 16 px; at 375 px ≈ 15.1 px. **(inference: the intent is "design at 1440, shrink proportionally below it, re-normalize on phones")**. No `clamp()` in the main stylesheet; one `clamp(2.5rem, 3.85vw, 3rem)` in the inline menu CSS.

### Heading scale (desktop → tablet ≤991 → mobile-landscape ≤767 → ≤479)
| Element | Desktop | ≤991 | ≤767 | Line-height | Tracking | Case |
|---|---|---|---|---|---|---|
| `h1` / `.heading-style-h1` | **7.813rem** (125 px) | 3.25rem | 2.5rem | **90%** | -0.02em | uppercase |
| `.header_heading` (hero) | **12.5rem** (200 px) | 10rem | 7.25rem → 4.375rem | 90% (100% on phone) | -0.02em | uppercase |
| `h2` / `.heading-style-h2` | 3.5rem (56 px) | 2.75rem | 2.25rem | 100% | -0.02em | uppercase |
| `h3` | 2.75rem | 2.25rem | 2rem | 100% | -0.02em | uppercase |
| `h4` | 2rem | 1.75rem | 1.5rem (lh 1.4) | 100% | -0.02em | uppercase |
| `h5` | 1.75rem | — | 1.25rem | 100% | -0.02em | uppercase |
| `h6` | 1.5rem | — | 1.125rem | 125% | -0.02em | uppercase |

All headings: `font-weight: 700; margin: 0`. Uppercase is applied at the element level (48 `text-transform: uppercase` rules in the CSS), so the source text is typed in lowercase ("anchor", "visit on sunday", "give to the mission") and the CSS shouts it.

### Body / utility text
- `body`: 1rem / line-height 1.5, color `var(--black)` `#272727`.
- `.text-size-large` 1.25rem (→1.125rem mobile), `.text-size-medium` 1.125rem (→1rem), `.text-size-regular` 1rem, `.text-size-small` 0.813rem, `.text-size-tiny` 0.75rem; all `line-height: 150%`.
- Body tracking: `-0.01em` on small descriptive text (28 rules), `-0.02em` on headings and buttons (58 rules). Nothing is positively tracked, even the uppercase labels; the "tight caps" look is deliberate.
- Hero subtitle `.header_subtitle`: 1.25rem, weight 600, uppercase, `max-width: 32rem`, 150% line-height, color `#fbf8f3`.
- Card title `.next-steps_item-heading`: 2rem, line-height 1, color `--anchor-grey`. Card body `.next-steps_item-description-text`: **0.813rem** (13 px), `--light-grey`. The jump from 32 px title to 13 px body is a signature ratio (~2.5:1).
- Button text: 0.875rem (14 px), weight 600, uppercase, 150% line-height; nav button variant 16 px.
- Links `a`: inherit size, underline, color `--anchor-grey`.
- Blockquote: `border-left: .1875rem solid #000; padding: .75rem 1.25rem; font-size: 1.25rem`.

### Takeaway
One sans, two weights that matter (700 for display, 500/400 for text), everything uppercase, negative tracking, line-height 0.9–1.0 on display sizes. The hero wordmark at 200 px is the brand.

---

## 3. Color & imagery

### Palette (from `:root`)
```
--black:        #272727   page background for dark bands, footer, locations
--anchor-grey:  #313436   button fill, body headings on light bg, borders
--off-white:    #fbf8f3   page background (warm, not pure white)
--white:        #ffffff
--light-grey:   #636363   card descriptions
--hover:        #7e7e7e   universal hover color for links/icons
--accessible-components--dark-grey:   #9b9b9b
--accessible-components--dodger-blue: #1378d1   (focus ring/accessible component; unused visually)
--lincoln-blue: #2fabaa   (legacy campus accent; not seen on current pages)
```
Overlays: hero image overlay `#0003` (20% black) on home, `#00000026` (15%) on Visit/In-Awe pages. Shadows essentially absent; `#00000080` appears 48 times but these are Webflow base/lightbox styles.

The site is effectively **monochrome**: near-black, warm off-white, two greys. No accent color on the homepage at all. Warmth comes from photography and the cream `#fbf8f3`.

### Imagery
- Documentary-style candid photography of people (laughing friends in front of a white brick mural reading "...of imperfect ... love", pastor on stage, kids' rooms, coffee counter). Alt text is descriptive and human ("A group of friends smiling and laughing in front of a white brick wall.").
- Every image is clipped with **large radii**: 35px (hero card, 141 rule occurrences), 30px (74), 50px (featured-teaching lightbox, section tops), 25px (next-steps cards), 20px (locations), 15px (what-to-expect strip), 18px on mobile. Radii step down on smaller breakpoints (35→30→18).
- Section *tops* are rounded too: `.locations_header { border-top-left-radius:50px; border-top-right-radius:50px }` (40px on mobile), `.section_what-to-expect`, `.section_faq.is-school` 3.125rem. Combined with negative margins this gives the "cards sliding over each other" look.
- Logo: white anchor line icon, 66 px wide in nav, 4.25rem in footer, `opacity: .3` on hover.
- Icons: inline SVG (Iconify `ic` arrows), stroke 2, `currentColor`, sized via `.icon-embed-xxsmall` 1rem … `.icon-embed-xlarge` 6.5rem.

---

## 4. Layout & page structure

### Containers and spacing
- `.padding-global { padding-left:5%; padding-right:5% }` (percent, not px).
- `.container-large` max-width **80rem** (1280 px), `.container-medium` 64rem, `.container-small` 48rem, `.max-width-xlarge` 64rem. Content max-widths are tight: headings 27–41rem, `.about_content-right` 24rem, `.locations-central_content` 26.75rem.
- Section padding: `.padding-section-large` 7rem (→6rem ≤991 →4rem ≤767), `-medium` 5rem (→4 →3), `-small` 3rem (→2).
- Grids are CSS Grid via Webflow `w-layout-grid`, e.g. `.about_component { grid-template-columns: 1.25fr .75fr; gap: 4rem }`, `.locations-central_component { grid-template-columns: 1fr auto; gap 5rem/4rem; max-width 61rem }`, footer `1fr x5`, mega-menu `1.5fr 1.5fr 1fr 1fr`.
- Breakpoints (Webflow defaults): **991px, 767px, 479px** down; 1280, 1440, 1920 up (used only for the fluid root font size and a few tweaks).

### Homepage, section by section (desktop)
1. **Announcement banner slot** (`banner_list-wrapper`, CMS, currently empty → `display:none`). Off-white bar, 0.75rem padding, centered 500-weight text.
2. **Navbar** — `position:absolute`, transparent, min-height 6.125rem (98 px), 5% side padding. Three-column grid `1fr auto 1fr`: left = hamburger (Lottie) + "VISION"; center = logo; right = "GIVE" + outlined "VISIT US" pill. Starts `opacity:0` and fades in on page load.
3. **Hero** (`section_header`) — a **43.5rem** tall `#272727` band, `margin-bottom: 11rem`. Inside, a `.header_card` (`min-height 37.5rem`, radius 35px) holds the photo with a 20% black overlay. The text block (`.max-width-xlarge.home_hero-offset`) is pulled up **-31rem** so the 200 px "ANCHOR" wordmark straddles the top edge of the photo card, with the card then extending below the dark band onto the cream page (see screenshot: band ends at ~y=695 of 1080 while the card runs to ~y=870). This overlap is the most distinctive composition on the site.
4. **About** (`section_about`, cream) — two-column: left h2 "Walking with Jesus and loving our neighbors." (56 px caps), right 24rem paragraph + outlined "OUR VISION" pill. Followed by a `.scroll-spacer` (8rem) for the sticky reveal.
5. **Locations block** (`.section_locations.is-sticky-section`) — a dark `#272727` sheet with 50px rounded top corners that slides up over the About section (`position: sticky; top: -87vw`, `margin-bottom:-1rem`). Header h2 "ONE CHURCH / TWO CONGREGATIONS" centered, then two alternating image/text rows (Central: image left, text right; Lakewood: text left, image right), each an entire-card link with h3 campus name, h6 times/address at 1.5rem, and a "Learn more about Central" text link with a diagonal arrow. Bottom padding 7.375rem.
6. **Featured teaching** — centered h2 "WATCH THE FEATURED TEACHING" + outlined "MORE SERMONS" pill, then a full-width 16:9 photo (radius 50px) with a circular "WATCH" button (164 px SVG circle, 2 px white stroke) that opens a YouTube playlist lightbox.
7. **Next steps** — h2 "TAKE YOUR NEXT STEP AT ANCHOR" (max-width 41rem, left aligned) with two 3rem round arrow buttons positioned top-right (`inset: -8rem 2.1875% auto auto`), then a 7-card Webflow slider (CMS-driven), 3 cards visible (`.next-steps_slide { max-width: 33.35%; padding-right: 1.75rem }`), each card: image (radius 25px, max-width 25rem) + h4 + 13 px description + "Learn More ↗" link; whole card is clickable via an absolutely positioned overlay anchor. Mobile shows one card at 92.5% mask width with a "swipe" hint and hides arrows.
8. **Footer** — dark, `position: sticky; bottom: 0` with `.footer_wrapper { margin-top:-100vh }` so the page content scrolls up to *reveal* the footer, whose inner block fades from 0→1 between 47% and 58% scroll progress (IX2 "Footer Scroll Reveal"). Five columns: logo, Locations, Quick Links, Ministries, More; bottom row © year (JS) + social icons + "Site by Sunday Best".

### Z-index / stacking conventions
Low integers only: nav `z-index:3`, menu `999` when open, sticky sections `z-index:1`, content `z-index:0`.

---

## 5. Navigation & header behavior

- **Transparent absolute header** over the dark hero; no sticky header, no scroll-shrink. The hero band's own 98 px top area carries the nav. After you scroll, there is no persistent nav; you rely on the footer or scroll back. **(weakness; see §12)**
- Visible top-level links are deliberately minimal: **Vision · [logo] · Give · Visit Us**. Everything else lives behind the hamburger.
- Hamburger = Lottie two-line icon (`.navbar-lottie` 3.75rem) that morphs to an X (IX2 `PLUGIN_LOTTIE` value 0→100 over 250 ms).
- **Mega menu** (`.navbar_mega-menu_component`, `position: fixed; inset: 0; background: var(--black)`): full-screen dark takeover. Content `max-width: 80rem`, `padding-top: 9rem`, 4-column grid `1.5fr 1.5fr 1fr 1fr`:
  - *Locations*: Central, Lakewood as 3rem 700 caps "main links".
  - *Quick links*: Visit, Teachings, Vision, Give, Events — same 3rem caps.
  - *Ministries* and *About* / *Formation* groups: 1.125rem 700 caps secondary links.
  - Footer row inside the menu: Contact Us (email, phone), Mail (PO Box), Follow Along (Instagram/Facebook/YouTube icons 2.375rem).
  - Hover: main links `color: #7e7e7e; transform: translateX(5%)` over `.5s cubic-bezier(.19,1,.22,1)`; secondary links color only.
  - Tablet: 2 columns, 3rem→3.25rem link size; phone: single centered column, 2.5rem links, group separators `1px solid #313436`, hover translate removed.
- Open/close choreography (IX2 action list a-30, 4 groups): set display flex → fade panel in 250 ms `outSine` → stagger groups in from `translateY(10%)`/opacity 0 to 0/1, 500 ms `outSine`, delays 150, 250, 450, 550, 650, 750 ms. The newer inline CSS reproduces the same stagger with pure CSS classes (`.anchor-menu_motion` → `.anchor-menu_in`, `transition: opacity .5s, transform .5s`, delays .15/.25/.45/.55/.65/.75 s) and honors `prefers-reduced-motion`.
- Accessibility retrofit script: adds `role="dialog" aria-modal="true" aria-label="Site navigation"`, `aria-controls`/`aria-expanded` on the trigger, sets `inert` on every sibling up the tree while open, traps Tab/Shift-Tab, closes on Escape, returns focus to the open button, treats Space as click, closes the menu when a link inside is clicked, and uses a `MutationObserver` on the menu's `style/class/hidden` to sync state with Webflow's display toggling. Focus rings: `outline: currentColor solid .125rem; outline-offset: .1875rem`.

---

## 6. Hero treatment

- Structure: dark band → rounded photo card → giant wordmark pulled up over the card edge → uppercase one-line mission statement → single outlined pill CTA ("VISIT US").
- Sizes: band 43.5rem; card min-height 37.5rem, radius 35px; wordmark 12.5rem (200 px) at 90% line-height; subtitle 1.25rem/600/uppercase, max-width 32rem; CTA 14 px.
- Image: `object-fit: cover`, separate desktop (2520 px wide) and portrait-mobile crops swapped with `display` classes; overlay 20% black so white text passes on busy photos.
- Load-in (IX2 a-86, PAGE_START): everything starts `opacity:0; translateY(2rem)`. Then h1 fades/rises 1500 ms `ease` at 0 ms; photo card at +250 ms; subtitle at +500 ms; button group, navbar and banner at +750 ms. Total ≈ 2.25 s. **(Note: Webflow writes the initial `opacity:0` inline, so without JS the hero would be invisible — Webflow adds `html.w-mod-js:not(.w-mod-ix)` fallbacks only for some targets.)**
- Secondary pages reuse the same hero shell with per-page offsets (`.central_hero-offset -31.5rem`, `.visit-page` card min-height 36rem, overlay 15%). Give page hero includes a solid "GIVE ONLINE" pill directly in the hero.
- Mobile: band 33.125rem, card radius 30px, wordmark 4.375rem, subtitle 0.875rem, header margin-top 15.75rem.

---

## 7. Video usage

- **No background/autoplay video anywhere scraped.** The "feel" of motion comes from photography + interactions, not video.
- Featured teaching: still image + circular "WATCH" button → Webflow lightbox (`w-lightbox`, `aria-haspopup="dialog"`) that loads a **YouTube playlist** (`videoseries?list=…`) through Embedly at 853x480, `allow="autoplay; fullscreen; encrypted-media; picture-in-picture"`.
- Teachings page: hero card "Latest Sermon" with the same WATCH control (lightbox), then two campus cards: Central → internal `/central-teachings`, Lakewood → Apple Podcasts. Livestream link on campus pages → YouTube `/streams`.
- Watch button hover: two stacked copies of the word "watch" inside a 16 px tall `overflow:hidden` wrapper; on hover both translate `-100%` over 500 ms `inOutCirc` so the second copy rolls up into place (text-roll effect).

---

## 8. Animations & transitions

All timing from the IX2 data or CSS. Easing names are Webflow's: `ease` = CSS ease; `outExpo` ≈ `cubic-bezier(.19,1,.22,1)`; `inOutCirc` ≈ `cubic-bezier(.785,.135,.15,.86)`; `outSine` ≈ `cubic-bezier(.39,.575,.565,1)`.

| What moves | Trigger | From → To | Duration / delay | Easing | Implementation |
|---|---|---|---|---|---|
| Hero h1, image card, subtitle, buttons, navbar | PAGE_START | opacity 0, translateY 2rem → 1, 0 | 1500 ms; stagger 0/250/500/750 ms | `ease` | IX2 a-86 |
| Every section wrapper (`.padding-global` in about, locations header/cards, teaching, next steps) | SCROLL_INTO_VIEW, offset 10% (some 20%) | opacity 0, translateY 2rem → 1, 0 | 1500 ms | `easeOut` | IX2 a-105 and siblings; one-shot (no reverse) |
| Footer inner block | SCROLLING_IN_VIEW (continuous) | opacity 0 → 1 between keyframes 47% → 58% | smoothing 85 | `easeIn` | IX2 a-109 "Footer Scroll Reveal" |
| Locations dark sheet | scroll | `position: sticky; top: -87vw` so it parks and the next section slides over | n/a | n/a | CSS |
| Footer | scroll | `position: sticky; bottom: 0`, preceded by `margin-top: -100vh` wrapper → curtain reveal | n/a | n/a | CSS |
| Outlined pill button (`.button.is-secondary`) | MOUSE_OVER / MOUSE_OUT | `.button-fill-on-hover` circle (2rem × 1rem, radius 2.5rem, z -1) scales 0 → **13×**; two stacked label copies translateY 0 → -100% (text roll); label color → `#272727` | 400 ms | `inOutCirc` | IX2 a-45/a-46; CSS also has `transition: all .4s cubic-bezier(.785,.135,.15,.86)` and plain `:hover` bg/color swap as fallback |
| Solid pill button (`.button`) | hover | bg `#313436` → white, text → grey | 400 ms | `cubic-bezier(.785,.135,.15,.86)` | CSS |
| Next-steps card | MOUSE_OVER | image scale 1 → **1.05**; arrow icon translate (10%, -10%); link text + icon color → `#7e7e7e` | 400 ms | `inOutCirc` | IX2 a-60/a-61 |
| Location card | MOUSE_OVER | big left arrow translateX -2%; small arrow (20%, -20%); text/icon color white → `#7e7e7e` | 500 ms | `outExpo` | IX2 a-52/a-53 |
| "Learn More ↗" text link | MOUSE_OVER | color → `#7e7e7e`; icon translate (2px, -2px) | 500 ms | `outExpo` | IX2 a-35/a-37 |
| Slider arrows (3rem circles) | MOUSE_OVER | `.button-fill-on-hover-circle` (1rem) scales 1 → 7; arrow icon slides out +200% while a second copy slides in from -200% | 400 ms | `inOutCirc` | IX2 a-47/a-48 |
| Watch button | MOUSE_OVER | stacked "watch" labels translateY -100% | 500 ms | `inOutCirc` | IX2 a-33/a-34 |
| Nav/footer logo, nav links, footer links, social icons | `:hover` | opacity → .3 (logos) or color → `--hover` | 500 ms | `cubic-bezier(.19,1,.22,1)` (17 rules use exactly `all .5s cubic-bezier(.19,1,.22,1)`) | CSS |
| Mega menu | MOUSE_CLICK (open/second click) | display → flex; panel opacity 0→1 250 ms; groups translateY 10% → 0 + opacity, 500 ms, delays 150–750 ms; Lottie 0→100 in 250 ms | see left | `outSine` | IX2 a-30 + inline CSS |
| FAQ accordion (Visit page) | click | plus icon / answer open; jQuery toggles `.open`, closes others | 500 ms | `cubic-bezier(.19,1,.22,1)` on `.faq_question` | CSS + inline jQuery |
| Next-steps slider | arrows / swipe, `data-animation="slide"`, `data-duration="500"`, `data-easing="ease"`, `data-infinite="true"`, autoplay off | | 500 ms | ease | Webflow slider |
| "What to expect" photo strip (Visit/Central) | **(inference)** two rows of 5 duplicated images in `100vw` overflow-hidden tracks offset `margin-left: -7.75%` and `-53%`; duplication strongly suggests an infinite horizontal marquee driven by IX2 loop (no `@keyframes` for it in CSS) | | | | IX2 |
| Spinner | `@keyframes spin` 0→360deg | | | linear | Webflow base only |

Reduced motion: the **main stylesheet has no `prefers-reduced-motion` rule** and IX2 ignores it; only the newer inline menu CSS has `@media (prefers-reduced-motion: reduce) { transition-duration: .01ms; transform: none }`.

Easing vocabulary summary: slow, expressive **ease-out-expo** `cubic-bezier(.19,1,.22,1)` at 500 ms for color/opacity hovers; snappier **in-out-circ** `cubic-bezier(.785,.135,.15,.86)` at 400 ms for the fill/scale/text-roll button choreography; long 1500 ms `ease`/`easeOut` 2rem rises for entrances. Nothing bounces or overshoots.

---

## 9. Interaction patterns

### Buttons
- Pill geometry everywhere: `border-radius: 2.5rem; padding: .75rem 1.5rem; font-size: .875rem; font-weight: 600; text-transform: uppercase; line-height: 150%; border: .0625rem solid`.
- Variants: `.button` solid (`#313436` bg, white text), `.button.is-secondary` outlined (transparent bg, grey text/border, `overflow:hidden; position:relative; z-index:0` to host the fill circle), `.is-alternate` white-on-dark versions, `.is-small` (`.5rem 1.25rem`), `.is-link` (no border/padding, optional `.is-icon` with 0.25–0.75rem gap), `.form-submit` (an arrow image, `opacity .8`, hover `opacity .5; transform: translateX(10%)`).
- Text-roll: label duplicated in a wrapper `max-height: 19px; overflow: hidden` (14px on mobile, 11px for `.mobile-size`). Fill circle starts `scale(0)` and grows 13× from the center. On ≤767 px the fill element is `display:none` (hover effects dropped on touch).
- `.button-group { display:flex; gap:1rem; flex-wrap:wrap }`, `.is-center` to center.

### Cards
- Whole-card link via an absolutely positioned empty `<a class="dynamic-next-steps-link">` with `inset:0; z-index:10` **and** a visible "Learn More ↗" pseudo-link (a `div`) for affordance. Card is a flex column `justify-content: space-between; min-height: 26rem; max-width: 25rem`.
- Image wrapper `overflow:hidden; border-radius:25px` so the 1.05 scale stays clipped.
- Staff cards on `/central`: photo, name, long role string, "Email" mailto link.

### Carousels
- Webflow native slider fed by Finsweet CMS slider; 3-up desktop (`33.35%`), 2-up tablet (`52.125%`), 1-up phone at 92.5% mask so the next card peeks; arrows are custom 3rem outlined circles placed in the heading row; dots hidden; "swipe" caption (12 px, capitalize, two 0.75rem arrows in `--hover`) shown only on mobile.
- Slide `aria-label="2 of 7"`, `role="group"`, inactive slides `aria-hidden="true"` with `tabindex="-1"` on inner links (Webflow does this; good).

### Accordion (Visit FAQ)
- `.faq_accordion { border-bottom: 1px solid var(--anchor-grey) }`, `.faq_question { padding: 1.25rem 0; padding-right: 2.25rem; cursor: pointer }`, 2rem plus icon absolutely right. Two-column layout `.75fr 1fr` with a **16rem** gap: left column "HAVE QUESTIONS?" + Contact Us pill, right column the questions.

### Forms
- Newsletter "Get central updates": single email field, placeholder white (`#Email-Events-Sign-Up::placeholder { color: white }`), submit is an arrow icon overlaying the field's right edge.

### Misc
- `.text-style-2lines/3lines` line clamps, `.truncate-width`, `.div-square::after { padding-bottom:100% }` aspect helper, `.no-scrollbar`.
- "Today" highlighter: inline script shows the element whose `id` equals `new Date().getDay()` — used on campus pages for service-day info **(inference)**.

---

## 10. Content & CTA strategy

- **Visitor-first hierarchy.** The only CTA in the hero is "VISIT US". The nav reserves a permanent outlined "VISIT US" pill at top right. The Visit page title is "VISIT ON SUNDAY" with subtitle "There's a place for you at anchor".
- Voice: lowercase-typed, uppercase-rendered short phrases; warm, inclusive, self-deprecating copy ("imperfect jesus-followers", "Seekers, cynics, Christ-followers and Christ-forgetters. Belief is not a prerequisite for belonging.", "There's no dress code").
- Homepage CTA sequence: Visit Us → Our Vision → Learn more about Central / Lakewood → More Sermons / Watch → 7 "next steps" (Visit, Groups, Kids, Students, Watch a Teaching, Start Serving, Celebrate Recovery). That next-steps slider is a **global component repeated at the bottom of every page** (home, visit, give, central, teachings) so every page ends with the same funnel.
- Locations are framed as "one church, two congregations" with times and addresses on the homepage itself (8:30/10:00/11:30 AM; 10:00 AM at a middle school) — no click needed to learn when/where.
- Give: nav-level link; page is short: h1 "GIVE TO THE MISSION" + hero pill "GIVE ONLINE" (external Church Center) + one gratitude/why paragraph + "More Ways to Give" (planned giving). No embedded form; outsource the transaction.
- Watch: never the lead CTA; appears third (featured teaching) and as a next-step card. Serve appears only as a next-step card and in the menu.
- Contact is a `mailto:` with a prefilled subject (`?subject=Contact%20Inquiry`, campus-specific variants) rather than a form.
- Footer repeats Locations / Quick Links / Ministries / More, plus socials, "© 2026 Anchor Church", agency credit.

---

## 11. Secondary page templates

All share: transparent nav → dark hero band with rounded photo card and oversized caps h1 → cream content sections with rounded tops → "take your next step" slider → sticky-reveal footer.

**/visit** — h1 "VISIT ON SUNDAY" + subtitle; two hero photos (desktop/mobile swap). Sections: "A community of imperfect Jesus followers." (belonging paragraph) → "one church gathering in two locations" (two campus cards with photo, name, times, address, "Visit Central/Lakewood") → "what to expect" paragraph + two-row photo marquee (10 images, duplicated) → "have questions?" FAQ accordion (4 Q&As: spiritual standing, serving, kids, dress) → "a place for your kids to belong" (Kids + Students cards, mobile swipe variant) → next steps → footer.

**/give** — h1 "GIVE TO THE MISSION" with "GIVE ONLINE" pill in hero → "thank you for your generosity" two paragraphs + two CTAs (Give Online, More Ways to Give) → next steps → footer. Deliberately minimal.

**/central** (campus) — h1 "ANCHOR CENTRAL" → "join us on sundays" with h3 times/address, "GET DIRECTIONS" (Google Maps) + "Watch the Teaching" (YouTube streams) → photo marquee → "the latest at anchor central" 3-card slider (teachings / events / contact; cards show campus eyebrow, bold title, photo, pill) → "Get central updates" email form → "anchor central staff" grid of 12 staff cards → next steps → footer.

**/teachings** — eyebrow "Anchor Central" + h2 "Latest Sermon" hero card with WATCH lightbox → "Learn from God's Word" two campus cards (Central teachings internal; Lakewood → Apple Podcasts) → next steps → footer. Sermon archive itself is not on-site.

Template rule: **hero band + 2–5 content modules + shared next-steps + footer**; modules are reused with per-page modifier classes (`.visit-page`, `.is-school`, `.kids`, `.mission-local`).

---

## 12. Accessibility notes

Positives
- Semantic `header/main/section/footer`, single h1 per page, logical heading levels (h2 sections, h3 campus names, h4 card titles, h6 for address lines).
- Descriptive alt text on photography; decorative images `alt=""`.
- Mega menu retrofit: dialog role, aria-modal, focus trap, `inert` background, Escape, focus return, visible focus outlines, `prefers-reduced-motion` handled for the menu.
- Slider slides carry `aria-label="n of 7"`, hidden slides `aria-hidden` and un-tabbable.
- Lightbox trigger has `aria-label="open lightbox"` and `aria-haspopup="dialog"`.
- JSON-LD `Church` schema; `lang="en"`.

Concerns
- `#7e7e7e` hover text on `#fbf8f3` is ~3.3:1 and on `#272727` ~3.6:1 — below 4.5:1 for 13–14 px text. `--light-grey #636363` card descriptions at 13 px on cream ≈ 5.6:1 (fine).
- 13 px (0.813rem) card body text is small, and the fluid root drops it to ~11 px around 991 px.
- Hero and all sections start at `opacity:0` inline; a JS failure leaves a blank page below the fold. Only some ids have `html.w-mod-js:not(.w-mod-ix)` fallbacks.
- Hamburger and close controls are `<a href="#">` with `role="button"` patched on; native `<button>` would be cleaner.
- No `prefers-reduced-motion` coverage for IX2 entrances/hover choreography.
- `loading="eager"` on nearly every image, including below-fold slider images.
- Clickable `div`s ("Learn More" is a `div` inside a card whose real link is an invisible overlay anchor) — works for mouse, but screen readers announce an empty link.

---

## 13. Weaknesses to avoid

1. **No persistent navigation after scroll** — absolute header disappears; visitors must scroll to the top or footer.
2. **Opacity-0-until-JS** entrance pattern on every section wrapper; add CSS fallbacks or animate only on `.js` class.
3. 1.5 s entrance durations plus 2.25 s hero stagger feel slow on repeat visits; no reduced-motion opt-out.
4. Heavy Webflow runtime (≈1.2 MB JS across chunks, two jQuery copies) for what is mostly CSS-achievable motion.
5. Hover-only affordances (text roll, fill circle) silently disappear on touch (`.button-fill-on-hover { display:none }` ≤767) — fine, but means mobile buttons have no pressed state at all.
6. Hover grey `#7e7e7e` fails contrast for small text.
7. Small 13 px card copy with fluid shrink.
8. Duplicate/legacy classes (`.button-2`, `.navbar_mega-menu_*` old menu vs new `.anchor-menu_*`, `--lincoln-blue`) show accretion; one bug-ish line survives: `transition: color .5s cubic-bezier(.19,1,.22,1), transform undefined undefined`.
9. Giving/events/sermons all leave the site (Church Center, YouTube, Apple Podcasts); consistent, but the site has no on-site sermon archive or event list to crawl.
10. The CMS announcement banner renders "No items found." text node (hidden by CSS, but exposed in markdown/screen-reader order unless `w-dyn-empty` is removed).

---

## 14. Reusable patterns (codeable rules)

### Tokens
```css
:root{
  --ink:#272727; --ink-2:#313436; --paper:#fbf8f3; --muted:#636363; --hover:#7e7e7e;
  --r-card:35px; --r-card-m:30px; --r-tile:25px; --r-sheet:50px; --r-pill:2.5rem;
  --ease-out-expo:cubic-bezier(.19,1,.22,1);
  --ease-in-out-circ:cubic-bezier(.785,.135,.15,.86);
  --ease-out-sine:cubic-bezier(.39,.575,.565,1);
  --t-hover:.5s var(--ease-out-expo);
  --t-button:.4s var(--ease-in-out-circ);
}
html{font-size:1rem}
@media (max-width:1440px){html{font-size:calc(.398664rem + .668151vw)}}
@media (max-width:991px){html{font-size:calc(.446987rem + .892857vw)}}
@media (max-width:767px){html{font-size:calc(.334201rem + 1.38889vw)}}
@media (max-width:479px){html{font-size:calc(.749477rem + .83682vw)}}
body{font-family:Metropolis,system-ui,sans-serif;color:var(--ink);background:var(--paper);line-height:1.5;-webkit-font-smoothing:antialiased}
```

### Type
```css
h1,h2,h3,h4,h5,h6{margin:0;font-weight:700;text-transform:uppercase;letter-spacing:-.02em;line-height:1}
h1{font-size:7.813rem;line-height:.9} h2{font-size:3.5rem} h3{font-size:2.75rem} h4{font-size:2rem} h6{font-size:1.5rem;line-height:1.25}
.hero-title{font-size:12.5rem;line-height:.9;color:#fff}
.eyebrow,.subtitle{text-transform:uppercase;font-weight:600;font-size:1.25rem;max-width:32rem}
.small{font-size:.813rem;letter-spacing:-.01em;color:var(--muted)}
@media (max-width:991px){h1{font-size:3.25rem}h2{font-size:2.75rem}h3{font-size:2.25rem}h4{font-size:1.75rem}.hero-title{font-size:10rem}}
@media (max-width:767px){h1{font-size:2.5rem}h2{font-size:2.25rem}h3{font-size:2rem}h4{font-size:1.5rem;line-height:1.4}.hero-title{font-size:7.25rem}}
@media (max-width:479px){.hero-title{font-size:4.375rem;line-height:1}}
```
Rule: type the copy in lowercase; let CSS uppercase it. Never positive-track caps here.

### Layout
```css
.padding-global{padding-inline:5%}
.container-large{max-width:80rem;margin-inline:auto} .container-medium{max-width:64rem} .container-small{max-width:48rem}
.section-lg{padding-block:7rem} .section-md{padding-block:5rem} .section-sm{padding-block:3rem}
@media (max-width:991px){.section-lg{padding-block:6rem}.section-md{padding-block:4rem}}
@media (max-width:767px){.section-lg{padding-block:4rem}.section-md{padding-block:3rem}.section-sm{padding-block:2rem}}
.two-col{display:grid;grid-template-columns:1.25fr .75fr;gap:4rem;align-items:start}
@media (max-width:767px){.two-col{grid-template-columns:1fr;gap:2rem}}
```

### Hero overlap
```css
.hero{background:var(--ink);height:43.5rem;margin-bottom:11rem}
.hero__card{position:relative;min-height:37.5rem;border-radius:var(--r-card);overflow:hidden;margin-top:10rem}
.hero__img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero__overlay{position:absolute;inset:0;background:rgba(0,0,0,.2)}
.hero__text{position:relative;z-index:1;max-width:64rem;margin:-31rem auto 0;text-align:center}
@media (max-width:767px){.hero{height:33.125rem;margin-bottom:7.125rem}.hero__card{border-radius:var(--r-card-m);min-height:18.75rem}}
```
Rule: the band ends before the card does; the title straddles the card's top edge.

### Sheet-over-section scroll
```css
.sheet{position:sticky;top:-87vw;background:var(--ink);color:#fff;border-radius:var(--r-sheet) var(--r-sheet) 0 0;margin-bottom:-1rem}
.footer-wrap{margin-top:-100vh}
.footer{position:sticky;bottom:0;background:var(--ink);color:#fff;padding-top:4.375rem;margin-top:-4.375rem}
```
Plus a scroll-progress fade on the footer's inner block from 47% to 58% visibility (IntersectionObserver or scroll-timeline).

### Pill button with fill + text roll
```css
.btn{display:inline-flex;align-items:center;justify-content:center;position:relative;overflow:hidden;z-index:0;
  border:1px solid currentColor;border-radius:var(--r-pill);padding:.75rem 1.5rem;
  font:600 .875rem/1.5 inherit;text-transform:uppercase;letter-spacing:-.02em;transition:color var(--t-button)}
.btn__fill{position:absolute;z-index:-1;width:2rem;height:1rem;border-radius:var(--r-pill);background:#fff;transform:scale(0);transition:transform var(--t-button)}
.btn__label{display:block;max-height:19px;overflow:hidden}
.btn__label span{display:block;transition:transform var(--t-button)}
.btn:hover .btn__fill{transform:scale(13)}
.btn:hover .btn__label span{transform:translateY(-100%)}
.btn.is-light{color:#fff} .btn.is-light:hover{color:#272727}
@media (hover:none){.btn__fill{display:none}}
```
Markup: `<a class="btn is-light"><span class="btn__label"><span>visit us<br>visit us</span></span><i class="btn__fill"></i></a>`.

### Card hover
```css
.card{position:relative;display:flex;flex-direction:column;justify-content:space-between;min-height:26rem;max-width:25rem}
.card__media{overflow:hidden;border-radius:var(--r-tile)}
.card__media img{transition:transform var(--t-button)}
.card:hover .card__media img{transform:scale(1.05)}
.card__link{color:var(--ink-2);transition:color var(--t-hover)} .card__link svg{transition:transform var(--t-hover)}
.card:hover .card__link{color:var(--hover)} .card:hover .card__link svg{transform:translate(10%,-10%)}
.card a.stretched{position:absolute;inset:0;z-index:10}
```

### Scroll-in reveal (replace IX2)
```css
.reveal{opacity:0;transform:translateY(2rem);transition:opacity 1.5s ease-out,transform 1.5s ease-out}
.reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
```
Trigger at 10% visibility, once. Hero: same values but 1.5 s `ease` with 0/250/500/750 ms stagger for title / image / subtitle / buttons+nav.

### Full-screen menu
Fixed dark panel; 4-col grid `1.5fr 1.5fr 1fr 1fr` → 2 → 1; main links 3rem/700/caps with hover `color:#7e7e7e; transform:translateX(5%)`; group stagger 150/250/450/550/650/750 ms, 500 ms `ease-out-sine`, from `translateY(10%)`; dialog semantics, inert background, focus trap, Escape, reduced-motion zeroing — copy the inline script's behavior.

### Content rules
- Nav shows at most 3 words + logo + one pill ("Visit Us").
- Hero = name, one-sentence identity, one CTA.
- Put service times and addresses on the homepage.
- End every page with the same "next steps" card rail.
- Outsource give/register/watch to specialist platforms; keep on-site pages short.
- Photography of people, always rounded 25–50 px; a 15–20% black overlay under white type.
