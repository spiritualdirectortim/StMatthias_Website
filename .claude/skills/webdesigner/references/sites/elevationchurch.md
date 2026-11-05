# Elevation Church (elevationchurch.org) — design pattern study

Studied 2026-11-04 via Firecrawl. Sources read:

- Homepage `/` — rendered HTML (248 KB, Firecrawl "html"), raw HTML with `<head>` (437 KB, "rawHtml"), 52 links.
- First-party CSS: `/_next/static/css/32dd53de51f4ccd8.css` (Tailwind build, 235 KB), `3c09f5ea32d1dccd.css` (next/font: Inter + DM Sans), `d9deea326a69ff62.css` (next/font: EB Garamond), `a28a9a33feb11f1f.css` (slick-carousel base + theme).
- Inline Emotion/MUI `<style>` blocks from the homepage (7 blocks, 75 KB: MUI CSS-variables theme, light + dark palettes, component styles).
- Secondary pages in markdown: `/about`, `/locations`, `/giving`, `/sermons`, `/events`; sermon detail `/sermons/your-best-is-not-behind-you` as raw HTML (882 KB, mostly the embedded YouTube player's own markup).

Not done: the Firecrawl screenshot was returned only as a signed URL and was not downloaded, so all visual conclusions come from the DOM, class names and CSS, not from pixels. Nothing JS-only (actual carousel autoplay timing, scroll-triggered reveals) could be observed; where I infer it, I say so.

Reading coverage: I processed 100% of the homepage HTML/rawHtml and the four CSS files programmatically (regex extraction over the whole text); the sermon-detail rawHtml was processed programmatically for video/iframe/heading/CTA extraction only, not read line by line.

---

## 1. Platform & stack

| Layer | Evidence | Verdict |
|---|---|---|
| Framework | `/_next/static/...` chunks, `__next_f.push`, `<next-route-announcer>`, `next-size-adjust` meta, `app/global-error` chunk | **Next.js App Router** (React Server Components), SSR/streamed |
| Styling | 486 distinct Tailwind utility classes (`flex`, `rounded-2xl`, `max-w-[1200px]`, `dark:` variants, arbitrary values like `h-[var(--site-header-height-mobile,64px)]`) wrapped as `body :is(.class)` in the compiled CSS | **Tailwind CSS v3**, scoped under `body :is()` to beat MUI specificity |
| Component kit | `MuiButton-root`, `MuiPaper-root`, `MuiAppBar`, `MuiDrawer`, `MuiFab`, `MuiTypography`, `emotion-insertion-point` meta, `--mui-*` CSS variables | **MUI v6 with CSS-variables theme** (`cssVariables: true`), Emotion runtime |
| Fonts | `next/font` self-hosted woff2 with `font-display:swap`, size-adjusted local fallbacks | DM Sans (primary), EB Garamond (loaded, used sparingly), Inter (loaded, apparently unused on the pages scraped) |
| CMS / images | `datocms-assets.com/60661/...?dpr=0.25&fm=webp` srcsets, `blurUpThumb`, `focalPoint`, `ResponsiveImage` GraphQL typenames | **DatoCMS** via `react-datocms` `<Image>`; plus a first-party image CDN `content.elevationchurch.org/images/...?width=3840&format=auto` |
| Carousel | `slick-slider slick-initialized slick-track slick-cloned slick-dots` plus slick's own CSS file | **react-slick** (slick-carousel) with custom MUI-styled dots and MUI `Fab` arrows |
| Video | Hero `<video src="blob:...">` with `<track kind="metadata" label="cuepoints">` and `<track kind="chapters">` tracks; sermon page `youtube.com/embed/<id>?playsinline=1` in `#youtube-player-<id>` | Hero = adaptive/MSE-streamed first-party video (blob URL; player SDK not identifiable with certainty, see Video section). Sermons = **YouTube IFrame API** |
| Third parties | GTM `GTM-PX7NX45`, Osano CMP (`osano-cmp-slot`), reCAPTCHA Enterprise, Sentry (trace/baggage meta), `dx.mountain.com` (ad attribution), `p.jmlp.app/sdk.js` | Standard marketing stack; cookie manager is Osano |
| Giving | Pushpay links (`pushpay.com/login?mode=p`), "Give Now" opens Pushpay; MyElevation portal on Salesforce (`myelevation.my.site.com`) | Giving is off-site |
| Hosting hints | `<link rel="preconnect" href="https://content.elevationchurch.org/">`, preload of 4 woff2 + hero image srcset | Vercel-style Next deployment (inference) |
| Theme | `<html lang="en" class="light" dir="ltr">`, every colour utility has a `dark:` twin, MUI light + dark palettes both emitted | **Light/dark theming built in**, defaults to light; class-based toggle (settings modal in the drawer: `aria-label="Open settings modal"`) |
| Reduced motion | `html.reduced-motion *{animation:none!important;transition:none!important;scroll-behavior:auto!important}` and `html.reduced-motion{--animation-duration:0s}` | A **user-toggled** reduced-motion class, in addition to Tailwind's `motion-reduce:` utilities |

No GSAP, Framer Motion, AOS, Lottie, Swiper, Splide, Locomotive, Lenis, Barba or Webflow IX2 anywhere in markup or CSS. Motion is purely CSS transitions (MUI defaults) + slick + an opacity/blur cover fade.

---

## 2. Typography

### Families
- **DM Sans** (Google font, self-hosted via `next/font`): weights 100–900 declared, used at **400, 500, 700**. Fallback: `"DM Sans Fallback"` = `local("Arial")` with `size-adjust:104.53%`, `ascent-override:94.90%`, `descent-override:29.66%` (zero-CLS swap).
- **EB Garamond** 400/500/600/700, fallback Times New Roman (`size-adjust:94.77%`). Only one utility references it (`font-family:var(--font-eb-garamond)!important`) — used as an accent serif somewhere outside the pages scraped (inference: sermon-series titles or devotional content).
- **Inter** variable 100–900 is also shipped (`--font-inter`) but no rule on the scraped pages uses it. Dead weight / legacy.
- Body classes: `__variable_d8ebd1 __variable_c62733` set `--font-inter` and `--font-dm-sans`; Tailwind `font-sans`-style utility resolves to `var(--font-dm-sans),"DM Sans",sans-serif`.

### MUI type scale (from `:root --mui-font-*`)
```
h1        700 96px / 1.167
h2        700 60px / 1.2
h3        700 48px / 1.167
h4        700 34px / 1.235
h5        700 24px / 1.334
h6        700 20px / 1.33
subtitle1 400 16px / 1.75
subtitle2 500 14px / 1.57
body1     400 16px / 1.5    letter-spacing 0.00938rem (0.15px)
body2     400 14px / 1.43   letter-spacing 0.01063rem (0.17px)
caption   400 12px / 1.66   letter-spacing 0.025rem  (0.4px)
overline  400 12px / 2.66
button    500 0.875rem / 1.75  letter-spacing 0.46px  (but text-transform is overridden to none, see below)
```

### What is actually rendered (the theme overrides the scale down hard)
The DOM never uses `MuiTypography-h1/h2/h3` for display text. Observed classes and their emitted CSS:
- Section titles use **`MuiTypography-h5`** → `.mui-1h59vjt { font-weight:700; font-size:1.125rem (18px); line-height:1.334 }` and **`font-size:1.5rem (24px)` from 600px up**.
- Card titles use **`MuiTypography-h6`** → `.mui-11sg6id { 700; 1rem (16px); line-height 1.33; letter-spacing 0.00938rem }` and **1.25rem (20px) at ≥600px**.
- `MuiTypography-h4` appears 4× (ministry grid section header); emitted ~`2.125rem` (34px).
- Body: `16px/1.5`, secondary text colour `rgba(0,0,0,.6)`.
- Captions/overlines: `12px/1.66`, `letter-spacing:0.025rem`, secondary colour.
- Rich-text blocks force headings: `[&_h3]:!text-[20px] [&_h3]:!font-bold [&_h3]:!leading-[26.6px] [&_h3]:!tracking-[0.15px]` and `[&_h2]:py-6`.
- The hero `<h1>` sits over the video and is visually a modest headline, not a 96px display size (inference from the h5/h6 pattern; exact hero size not in the extracted CSS because it is a Tailwind arbitrary class not captured).
- Tailwind sizes seen: `text-xs`(12) ×6, `text-sm`(14) ×1, `text-base`(16) ×23. **No `text-2xl`+ utilities on the homepage.** This is a deliberately small, app-like type scale.

### Casing, tracking, weight
- **Buttons are sentence case**: `normal-case` appears on 20 buttons; the MUI `uppercase` default is cancelled. CTA copy reads "Get connected", "Watch sermon", "Find a location".
- Headings are **Title Case or sentence case**, bold 700, tight line-height (1.33), near-zero tracking (0.15px). No uppercase eyebrow text in the sampled DOM; "Who We Are" / "What to Expect" eyebrows on /about are plain-cased caption text.
- Weight palette is just 400 / 500 / 700. Nothing lighter, nothing black.
- Line clamping: `line-clamp-2` on 20 card descriptions; `min-h-[3rem]` reserves two lines so cards align.
- Tailwind `prose` (typography plugin) is present for rich text: h1 800/2.25em, h2 700/1.5em, h3 600/1.25em, links underlined 500.

---

## 3. Color & imagery

### Palette (MUI CSS variables, light mode)
```
primary.main        #000000     (buttons, icons, dots)
primary.dark        #1D1D1D     (contained button hover)
primary.light       #2E2E2E
primary.contrast    #FFFFFF
secondary.main      #757575
secondary.dark      #616161
secondary.light     #E0E0E0     (ministry card background: bg-light-secondary-light)
background.default  #FFFFFF
background.paper    #F5F5F5 (MUI) / #F4F4F4 (Tailwind token light-background-paper)
text.primary        rgba(0,0,0,0.87)   (#000000DE)
text.secondary      rgba(0,0,0,0.60)
text.disabled       rgba(0,0,0,0.38)
divider             rgba(0,0,0,0.12)
action.hover        rgba(0,0,0,0.04)   focus 0.12   selected 0.08
grey 50..900        #fafafa #f5f5f5 #eeeeee #e0e0e0 #bdbdbd #9e9e9e #757575 #616161 #424242 #212121
error               #D32F2F   success #2E7D32   info #0288D1   warning #ed6c02
focus ring          rgb(147,197,253) solid 2px   (Tailwind blue-300)
```
Dark mode:
```
primary.main #FFFFFF, primary.dark #FFFFFF29, contrast #212121
background.default #0A0A0A, paper #1A1A1A, paper2 #232323
text.primary #FFFFFF, secondary rgba(255,255,255,.7), divider rgba(255,255,255,.12)
secondary.light (cards) #424242
```
Extra Tailwind tokens:
```
gray-light1 #FFFFFF   gray-light2 #EBEBEB   gray-light3 #F5F5F5   (hover fills)
light-secondary-button #EEEEEE   (secondary pill button)
light-primary-contrast #F5F5F5
brands-ec-primary  rgb(255,103,31)  = #FF671F  (Elevation orange; used for text/icon accents only)
orange-500 rgb(249,115,22)         (Tailwind default, appears once)
text-black-translucent #00000099
carousel-dot-active #000 / inactive rgba(0,0,0,.24)  (dark: #fff / rgba(255,255,255,.32))
```
**Takeaway:** the site is essentially **monochrome** — black primary, white/off-white surfaces, 60%-alpha grey body text, 12%-alpha dividers. The brand orange exists (`ec-orange-icon.svg`, `--brands-ec-primary`) but is reserved for the logo mark and rare accents. Colour comes from photography.

### Gradients (text-over-image scrims)
```
bg-home-card-gradient-header:   linear-gradient(180deg, rgba(26,26,26,0) 61%, #1a1a1a 93.5%, #1a1a1a)
bg-home-card-gradient-involved: linear-gradient(180deg, rgba(26,26,26,0) 28%, #1a1a1a)
from-light-background-default / to-transparent, from-light-background-paper, to-dark-background-paper (edge fades on carousels)
```
Both scrims run to **#1A1A1A (not pure black)** and start late (61%) on the hero so the photo stays clean; the "Get involved" variant starts at 28% because its copy is taller.

### Imagery
- Every image goes through an image CDN with `format=auto` and width params; DatoCMS images get `dpr=0.25/0.5/0.75/1` srcsets with `fm=webp`, `focalPoint`, and a **base64 `blurUpThumb` LQIP** painted as `background-image` under the real image.
- Hero poster preloaded via `<link rel="preload" as="image" imagesrcset=...>`.
- Subject matter: wide-shot worship crowds, campus exteriors, kids/youth, outreach volunteers, pastors portrait; all photographic, no illustration, no stock-looking iconography. Alt text is descriptive and long (e.g. "A group of four women hold a sign 'New Here?' while standing outside Elevation Church").
- Sermon art is a **separate title PNG layered over the photo** (`..._title_centered.png` for mobile, `..._title_left.png` for desktop) — the headline is artwork, swapped per breakpoint with `<picture>`.
- Logo variants: `ElevationLogoColorWhite` (over hero/dark), `ElevationLogoFullColor` (light header), `ec-orange-icon.svg` (compact mark, 64px).

---

## 4. Layout & page structure

### Containers and widths
- Header toolbar: `max-w-[1705px] mx-auto`.
- Hero carousel wrapper: `max-w-[1680px] mx-auto`, `mb-10 md:mb-20`.
- Hero caption/CTA row inside the slide: `max-w-[1200px]` centred (`left-[50%] translate-x-[-50%]`), `px-4`.
- Content sections: **`mx-auto max-w-[1200px] px-4 md:px-6`** — the canonical content width.
- Marketing card carousel: `max-w-[1728px]`.
- Ministry grid wrapper: `max-w-[100vw]`, inner `max-w-[1200px] !py-20`.
- CTA button rows: `max-w-[444px]`; feature cards `max-w-[600px]`; info columns `max-w-[900px]`.
- Full-bleed media cards cap at `max-w-[1920px]` / `max-w-[2000px]`.

### Spacing rhythm
- Base unit 8px (`--mui-spacing: 8px`); Tailwind spacing used: `gap-2`(8) ×45, `gap-4`(16) ×37, `gap-6`(24), `px-4`(16) ×62, `md:px-6`(24), `py-6`(24), `py-20`(80) between major sections, `mb-10 md:mb-20` after hero, `pb-[58px] md:pb-[66px]` under feature cards, `--page-bottom-padding: 4rem`.
- Cards: `p-6` padding, `rounded-2xl` (16px) — **67 occurrences** — the single most defining shape token. `rounded-3xl` (24px) exists for larger panels; `rounded-full` for icon buttons / social circles.
- Shadows are suppressed: `shadow-none` ×30 and `hover:shadow-none` ×20 override MUI Paper elevation. Flat surfaces + 1px 12%-alpha borders instead of drop shadows. `shadow-elevation1` = `0 1px 3px rgba(0,0,0,.12)` and `shadow-elevation6` exist for menus.

### Breakpoints (Tailwind config aligned to MUI)
```
xs  435px   (custom; used for aspect-ratio switch)
sm  600px
md  900px
lg  1200px
xl  1536px
2xl 1680px
plus arbitrary: min-[600px], max-[600px], min-w 350px, 561px, 720px, 768px, 1260px, 1280px, 1440px, 1700px
```
MUI's own breakpoints in Emotion CSS: `600px`, `601px`, `1025px`.

### Homepage, section by section (desktop order)
1. **Skip links** ("Skip to main content", "Skip to main nav") — offscreen `left-[-999px]`, `focus:left-4 focus:top-4`, white box with black border.
2. **Sticky header** — `sticky top-0 z-50`, height `64px` mobile / `80px` desktop (CSS vars), white bg, `border-b-2` 12%-alpha divider (no border on mobile). Contents: hamburger IconButton (always present, opens left Drawer), logo, **search field** (`max-w-[444px]`, placeholder "Search", type=search), text links **Give · Groups · Serve · Events · About** (`hover:underline`), account icon ("Login to your account").
3. **Mobile sub-nav** (`block sm:hidden sticky top-[64px] z-[60]`): horizontal scroll-snap strip of 72px-wide icon+label tiles, 80px tall — Sermons, Locations, About, Giving, Groups, Serving, Store, Events, Streaming. Scrollbar hidden.
4. **Hero carousel** (react-slick, 2 slides, `slick-dots` + one `MuiFab` "Next" arrow): 
   - Slide 1: autoplaying welcome video card; `<h1>Welcome to Elevation Church</h1>` + subline "See what God can do through you."; CTAs **"Get connected"** (/connect) and **"Learn more"** (/about).
   - Slide 2: latest sermon art ("The Best Is Not Behind You!") + `<h2>Pastor Steven Furtick</h2>` "Watch the latest sermon"; CTAs **"Watch sermon"** and **"Watch full experience"**.
   - Card aspect ratio: `aspect-[4/3.5]` → `xs:aspect-[1.5]` → `sm:aspect-[24/9]` (ultrawide on desktop). `rounded-2xl` from 720px up (`[@media(min-width:720px)]:rounded-2xl`), square-edged full-bleed on phones.
   - CTA buttons are rendered **twice**: inside the image (`hidden md:block`, bottom-left, over the scrim) and again in a plain card below the image (`-mt-1 pt-4 px-4 pb-6`) for mobile.
5. **"Find the right experience for you"** — h5 heading + body1 intro; four `MuiPaper rounded-2xl p-6 !bg-transparent` cards with icon, h6 title, body, and a **text button** ("Find a location", "Find a time", "Find a watch party", "Find a pop-up"). Cards: Physical Campus · Live Streams · Watch Party · Pop-Up. (`MuiButton-text` large, primary.)
6. **"Discover more ways to connect"** — `section aria-label="Marketing cards"`, slick carousel of `<article>` cards: `aspect-video` image, h6 title, `line-clamp-2` body, caption CTA line ("Learn more", "Purchase your tickets today", "Young adults, RSVP", "Start our new devotional"). Prev/Next `MuiFab` circular buttons, custom dots. Slides `px-2 min-[600px]:px-3`, `min-h-[115px] min-[600px]:min-h-[126px]` text area.
7. **"A place for you and your family"** — paper-grey band (`bg-light-background-paper`), `max-w-[1200px] !py-20`, **`grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-4 md:gap-6`**; 7 ministry tiles each `h-[366px] rounded-2xl px-4 py-6 md:px-6 bg-light-secondary-light` (#E0E0E0) with background photo, logo image, h6 tagline, caption name and a **contained "Learn more"** button. Tiles span `lg:col-span-3` (4 tiles, 2 per row) then `lg:col-span-2` (3 tiles, 3 per row) — a 2+2+3 mosaic. The Worship tile uses a looping muted `<video>` instead of a photo.
8. **"How to get involved"** — three stacked/side-by-side feature cards (Volunteer / Lead / Opportunities): `aspect-[16/9]` image with `bg-home-card-gradient-involved` scrim, `rounded-t-2xl rounded-b-none`, text card beneath `!-mt-[68px] !pt-6` (overlapping the image), contained "Learn more".
9. **Footer**: there is **no traditional footer** on the homepage. Address, legal links and socials live at the bottom of the **left navigation Drawer** (`MuiDrawer-anchorLeft`, 320px wide: `transform:translateX(-320px)` when closed). Drawer sections: Get Involved (9 items with one-line descriptions) · Discover · Ministries · "Notice an issue?" mailto · Opportunities · About · MyElevation card · address/phone · © · Contact · Cookies · Terms · Privacy · Manage Cookies · 4 social circles (`h-[36px] w-[36px] rounded-full bg-black text-white transition hover:bg-text-greyHover`).

### Grid / flex habits
- `flex` ×143 vs `grid` ×8: layout is overwhelmingly flexbox; CSS grid appears only for the ministry mosaic and `col-span-12 sm:col-span-6` two-up pairs.
- `aspect-*` everywhere (`aspect-video` ×10, `aspect-[16/9]`, `aspect-[4/3.5]`, `aspect-[24/9]`, `aspect-[21/9]`) with `absolute inset-0 object-cover` images — all media boxes are ratio-locked.
- `whitespace-nowrap` on 20 buttons; `!w-fit` on 14 — buttons hug content, never stretch.

---

## 5. Navigation & header behavior

- **Persistent hamburger on all breakpoints**; the drawer is the real site map. Top-bar links are a curated 5 (Give, Groups, Serve, Events, About). The drawer items each carry a **two-line label** (title + 8-word description), e.g. "Salvation — Receive God's grace", "Baptism — Celebrate new beginnings", "Need Prayer? — Support through faith".
- Header is `position: sticky` (not fixed); no shrink-on-scroll or transparency change is visible in CSS (inference: static height). `border-b-2` with 12% divider gives a hairline.
- **Search is first-class** in the header (`#header-input-search`, MUI Input with adornment).
- Mobile gets a **second sticky row** of icon tiles (`top-[64px]`, `z-[60]`, scroll-snap `snap-x snap-mandatory snap-start`), effectively an app tab bar at the top.
- Drawer: MUI Modal + Backdrop, `z-index: var(--mui-zIndex-drawer)` = 1200; slide transition is MUI's default (`transform 225ms cubic-bezier(0,0,0.2,1)` entering / `195ms cubic-bezier(0.4,0,0.6,1)` exiting — standard MUI values, inference since the inline CSS only shows `transform: translateX(-320px)` at rest). Contains its own "Skip to main content" link and a "Close navigation" button, plus a settings gear (theme / reduced-motion toggles, inference from `html.reduced-motion` + `class="light"`).
- Every nav anchor has a stable analytics id: `ec-nav-central-nav-bar-give`, `ec-mobile-central-sub-nav-sermons`, `ec-nav-central-get-involved-side-nav-baptism`, etc.
- Login icon leads to MyElevation (Salesforce Experience Cloud).

---

## 6. Hero treatment

- The hero is a **carousel of two "cards"**, not a full-viewport banner: constrained (`max-w-[1680px]`), rounded (`rounded-2xl` ≥720px), with a fixed aspect ratio (`24/9` desktop, `1.5` small, `4/3.5` phone portrait).
- **Slide 1 = video**. `<video class="absolute inset-0 w-full h-full object-cover object-center" playsinline preload="auto" src="blob:…">` with a `<img alt="Welcome to Elevation Church poster">` cover from `content.elevationchurch.org/images/ec_q1_header_2026.jpeg`. Overlaid controls: **Unmute** button (`absolute right-4 top-4 w-10 h-10 bg-[#00000066] backdrop-blur-[2.5px] hover:bg-[#212121]`) and a centred **Pause** button (`w-14 h-14`, same glass style). The whole frame is a `role="button" aria-label="Play video"` hit area. The cover `<div class="transition-all opacity-100" style="transition-duration:700ms; transition-timing-function:ease-in-out; transition-property:opacity,filter; filter:blur(4px)">` fades/unblurs when playback starts.
- **Slide 2 = sermon art**: photo + separate title PNG (centred variant on mobile, left-aligned variant on desktop), name/subtitle, two CTAs.
- Text sits **bottom-left**, in a `max-w-[1200px]` inner frame aligned to the page content column, over `bg-home-card-gradient-header` (transparent until 61%, solid #1A1A1A by 93.5%). `pointer-events-none` on the overlay wrapper, `pointer-events-auto` restored on the CTA group.
- Copy: `<h1>` "Welcome to Elevation Church" + one-line promise "See what God can do through you." — short, visitor-addressed, no church jargon.
- CTA pair: primary contained black "Get connected" + second contained "Learn more" (both contained, both primary; the hierarchy is positional, not stylistic).
- Below-image duplicate CTA bar for mobile keeps buttons off the photo on small screens.
- Dots: custom `slick-dots` — 18px hit targets, `opacity .32` inactive, active dot stretches to a **16px-wide pill** (`width:16px; border-radius:6px`), `rgb(147,197,253)` focus outline. One `MuiFab` "Next" arrow (default grey, `hover:bg grey-300`).

---

## 7. Video usage

1. **Hero welcome video** — first-party, streamed via MSE (`blob:` URL) with cue-point and chapter text tracks (`data-removeondestroy`), `playsinline`, `preload="auto"`, no `autoplay`/`muted` attributes in markup (JS starts it muted; an explicit Unmute control is provided). Poster image preloaded. Treated as **ambient brand video with opt-in sound**.
2. **Worship ministry tile** — `<video loop playsinline preload="none">` with `<source src="https://www.datocms-assets.com/60661/1729023769-tig-trim.mp4" type="video/mp4">`, `<track kind="captions">`, server props `{"autoPlayVideo":true,"muted":true,"coverUrl":"/ew-avatar-dark.png"}`. Looping muted MP4 as a **card background**, with a static fallback image and the same 700ms blur-fade cover.
3. **Sermon pages** — `youtube.com/embed/<id>?playsinline=1&origin=…` in a `rounded-2xl overflow-hidden aspect-video` box via the IFrame API (`#youtube-player-<id>`); the sermon list and "More sermons" use static thumbnails `aspect-[16/9] rounded-2xl` + title + speaker.
4. **Live stream** lives off-site at `live.elevationchurch.online` ("Watch full experience").
5. No Vimeo, Wistia, Mux-branded player or background-video sections elsewhere on scraped pages. Video is confined to **cards**, never full-bleed behind text sections.

---

## 8. Animations & transitions

What moves, concretely:

| Element | Motion | Trigger | Duration / easing | Mechanism |
|---|---|---|---|---|
| Video cover (poster over video) | opacity + `filter: blur(4px) → blur(0)` | playback starts | **700ms ease-in-out**, `transition-property: opacity, filter` | inline style, React state |
| Hero / marketing carousels | horizontal `translate3d` of `.slick-track` | arrow, dot, swipe (and probably autoplay — not provable) | slick default **500ms ease** (inference; no custom speed in payload) | react-slick |
| Carousel dot | width 0 → 16px pill, opacity .32 → 1 | slide change | MUI default transition (inference) | Emotion |
| Contained buttons | `background-color, box-shadow, border-color` | hover/focus/active | **250ms cubic-bezier(0.4,0,0.2,1)**; hover bg `#1D1D1D` | MUI Button |
| Icon buttons / Fab | background-color | hover | **150ms cubic-bezier(0.4,0,0.2,1)** | MUI IconButton |
| Paper / AppBar / Card | box-shadow | elevation change | **300ms cubic-bezier(0.4,0,0.2,1)** | MUI Paper |
| SVG icons | fill | colour change | 300ms cubic-bezier(0.4,0,0.2,1) | MuiSvgIcon |
| Generic MUI (Collapse, Drawer, Modal) | transform/opacity | open/close | 200ms cubic-bezier(0.4,0,0.2,1) (9 rules); `width 250ms cubic-bezier(0.4,0,0.6,1)` for the search field | MUI transitions |
| Tailwind `transition` / `transition-all` | colours, opacity, shadow, transform, filter | hover | **150ms cubic-bezier(0.4,0,0.2,1)**; `duration-200`, `duration-300`, `ease-out = cubic-bezier(0,0,.2,1)` available | Tailwind |
| Social circle buttons | background black → greyHover | hover | 150ms | `transition` utility |
| Row links in drawer | background → `gray-light3` (#F5F5F5) | hover | none declared (instant) | `hover:bg-gray-light3` |
| Skeletons | `@keyframes animation-c7515d {0%{opacity:1}50%{opacity:.4}100%{opacity:1}}` | loading | MUI Skeleton default **1.5s ease-in-out infinite** | Emotion |
| `animate-pulse` | opacity .5 at 50% | loading | 2s cubic-bezier(.4,0,.6,1) infinite | Tailwind |
| `animate-spin`, `animate-spin-reverse` | rotate 1turn | loading | 1s / 1.5s linear infinite | Tailwind + custom |
| Page anchors | `html{scroll-behavior:smooth}` | hash links | browser default | global CSS |
| Image blur-up | LQIP base64 background under the img | load | react-datocms default fade (inference ~500ms) | react-datocms |

Only **one** keyframe set is custom (`spin-reverse`); there are **no scroll-triggered reveals, no parallax, no staggered entrances, no hover scale/translate utilities** (`hover:scale-*`, `hover:-translate-y-*`, `group-hover:*` all absent). Cards do not lift on hover; they rely on cursor change and underline/background shifts.

Reduced motion:
- Global: `html.reduced-motion * { animation:none!important; transition:none!important; scroll-behavior:auto!important }` and `--animation-duration:0s` — triggered by a **user setting**, not only the OS query.
- OS query: `@media (prefers-reduced-motion:no-preference)` gates `motion-safe:animate-pulse`; `@media (prefers-reduced-motion:reduce)` provides `motion-reduce:hidden` and `motion-reduce:transition-none`.
- `html{max-width:100vw}` and `body{overflow-x:hidden}` guard against carousel overflow.

---

## 9. Interaction patterns

### Buttons (MUI `Button`, themed)
- **Primary contained**: black `#000` bg, white text, `rounded` (4px MUI radius; Tailwind `rounded` 0.25rem also applied), `normal-case`, `whitespace-nowrap`, `!w-fit`, size "medium" `!px-[22px] !py-2` or "large" `px-[24px] py-2`; hover bg `#1D1D1D` (`hover:bg-light-primary-dark`), **no shadow at rest or hover** (`shadow-none hover:shadow-none` beat MUI's elevation 2/4/8 ramp); focus-visible `outline: 2px solid rgb(147,197,253)`; transition 250ms standard-ease.
- **Secondary pill**: `bg-light-secondary-button` (#EEEEEE) text black, `hover:bg-light-secondary-light` (#E0E0E0), dark: `#424242`.
- **Text button** (`MuiButton-text` large): black label, used for the four "Find a…" links; hover bg `rgba(0,0,0,.04)`.
- **Icon buttons / Fab**: circular, 36–56px, `bg-[#00000066] backdrop-blur-[2.5px]` glass on media; Fab arrows grey with `hover:bg rgb(97,97,97)` in some variants.
- Text links in header: plain, `hover:underline`.
- Labels are verbs: "Get connected", "Watch sermon", "Find a location", "Sign up to serve", "Access MyElevation", "Give Now", "Load more".

### Cards
- Three recurring card recipes:
  1. **Media card** — ratio-locked image, `rounded-2xl overflow-hidden`, scrim gradient, text anchored bottom-left, CTAs inside (desktop) and repeated below (mobile).
  2. **Icon info card** — transparent bg, `p-6 gap-6`, icon, h6, body2, text-button; no border, no shadow.
  3. **Tinted tile** — `#E0E0E0` bg, fixed `h-[366px]`, photo/video behind, logo, tagline, contained button.
- Whole card is wrapped in a single `<a>` when it's a link (`<a class="block w-full"><article>…</article></a>`), with `line-clamp-2` text and reserved min-heights so rows align.
- Hover feedback on list rows: `hover:bg-gray-light3 rounded px-3 py-2` (drawer items) — the "app list" look.

### Carousels
- react-slick, `slick-cloned` slides for infinite loop, custom dots (18px targets, pill active state), MUI Fab arrows positioned outside the track on desktop; mobile relies on swipe (`touch-action: pan-y`).
- Native **scroll-snap** for the mobile sub-nav and some rails (`snap-x snap-mandatory snap-start`, `[scrollbar-width:none] [&::-webkit-scrollbar]:hidden`).
- Edge fades: `from-light-background-default to-transparent` gradient masks (inference for rails).

### Forms / inputs
- MUI Input (standard variant) for search with leading icon adornment; autocorrect/autocapitalize/spellcheck off.
- Locations page: pill toggle "All / Campus / Watch Party", distance-sorted list with "Find My Location" geolocation button.
- Giving: segmented controls (Tithes & Offerings / Trust in God Offering; Electronic / Crypto / Stocks), then a single **"Give Now"** button that hands off to Pushpay. FAQ is an accordion list.

---

## 10. Content & CTA strategy

- **Visitor-first framing.** H1 "Welcome to Elevation Church"; page title "Welcome Home"; meta "Find the right experience for you…". The first content block after the hero is literally "Find the right experience for you" with four modes of attending (Physical Campus, Live Streams, Watch Party, Pop-Up) — **location/format choice before anything about the church itself**.
- **"Find a ___" verb pattern** for every attendance CTA: Find a location / Find a time / Find a watch party / Find a pop-up / Find a group / Find an experience / Find My Location.
- **Three-tier pathway** repeated across pages: Connect (locations, streams, groups) → Grow (sermons, study guides, devotional) → Serve/Give (eTeams, Outreach, Giving). Sermon detail ends with "Take your next step of faith": Make a decision for Christ / Go public with your faith (baptism) / Find your people (groups).
- **Give** is in the top nav as the first link but is not shouted on the homepage body; the giving page leads with impact copy ("See what God can do through your generosity"), then options, then "There are many ways to give" (app, text-to-give 77977, in person, mail, non-cash), then accountability (ECFA badge, annual report, audited financials) and FAQs.
- **Watch** is the second hero slide and the first drawer "Discover" item; sermons page has a hero card for the latest message, then a searchable/filterable grid with "Load more".
- **Serve** appears as "Serve" nav link, "Serve Your Community" marketing card, "Volunteer" feature card, "Sign up to serve" on /about, and e101 volunteer orientation on /events.
- Taglines are short declaratives with a period: "Connecting people. Activating faith." / "Making an impact – locally and globally." / "Where calling meets college."
- Time-sensitive items (seasonal events, devotional, young-adult Chapel) are handled by the **marketing-card carousel**, not by altering the page skeleton.
- Alert banner pattern on /giving ("Your 2025 Giving Statement is ready. Click here to view.").
- Footer-equivalent includes a **"Notice an issue? Tell us so we can fix it."** mailto with pre-filled device/browser fields.

---

## 11. Secondary page templates

**/about ("About Us")** — long-scroll storytelling template:
1. Headline h2 "See What God Can Do Through You" + 2 paragraphs, full-width photo.
2. Mission statement band ("We exist so that people far from God will be raised to life in Christ.") with eyebrow "Who We Are" and two cards (Beliefs / Values → "Learn more").
3. "Find the right experience for you" — same four-mode module as home, each with photo + "Find a…" link.
4. Pastors section: eyebrow "Meet Our Pastors", portrait, bios, external links.
5. "What to Expect" — three alternating image/text rows (Sermons / Worship / Community) with a Spotify embed and two sub-cards (eGroups, Volunteer).
6. NextGen (Children / Youth) two-column cards with age ranges.
7. Young Adults (three-image strip).
8. Outreach with a stat ("300+ Outreach Partners") and "Sign up to serve".
9. Closing CTA band: "Ready to plan your visit? Make plans to join us this Sunday!" → **"Find an experience"**.

**/locations** — utility list template: filter pills (All / Campus / Watch Party), geolocated list sorted by distance ("18 miles · Watch Party"), each row = h4 name, address or "Hosted by Church member", distance+type chips, thumbnail; sticky bottom bar with the same filter + "Find My Location". No marketing copy at all.

**/giving** — form-first template: optional alert banner → eyebrow "Giving" → h2 impact headline → paragraph → segmented fund choice → segmented method choice → one-line explanation → **Give Now** → secondary links (Manage Pushpay, View FAQs) → "many ways to give" cards with app badges and text-giving steps (numbered 1/2 with example) → impact carousel (3 photo+story slides) → Resources (Annual Report, Budgeting tool, ECFA) → FAQ accordion.

**/sermons** — media library template: hero card for latest sermon (same component as homepage slide 2, with duplicated CTA row), `<h1>Sermons</h1>` + helper line, search input + "Filters", thumbnail grid (16:9, bold title, speaker), "Load more".

**/sermons/[slug]** — detail: 16:9 YouTube embed in rounded card, h1 title, "Sermon Discussion" section with "View Discussion Questions" button, "Give" and "Subscribe" buttons, "Take your next step of faith" 3-card CTA module, "More sermons" grid of 8.

**/events** — hero card (Outreach) with "View Events / Learn more", then location-aware list "Happening at Elevation Online" with fallback copy ("Nothing within 100 mi of {city}… here is what is happening online"), event cards: image, "VIRTUAL EVENT" tag, title, campus, date/time, language/platform/time range.

Shared chrome on every page: same sticky header, same drawer-as-footer, same skip links, same `max-w-[1200px]` content column, same `rounded-2xl` media cards.

---

## 12. Accessibility notes

Good:
- Two skip links (content and nav), visible on focus; drawer has its own skip link.
- `lang="en"`, `dir="ltr"`, `<main id="main-content">`, `<nav>`, `<section aria-label="Marketing cards">`, `<article>` for cards, `<next-route-announcer>` live region.
- All icon buttons have `aria-label` ("menu", "Unmute", "Pause", "Next", "Previous", "Login to your account", "Close navigation", "Open settings modal").
- Visible focus style: `outline: 2px solid rgb(147,197,253)` on buttons, dots, Fabs; `focus:border-2 focus:border-[#1D1D1D]` on inputs.
- Long descriptive alt text on content photos; decorative card images use `alt=""`.
- Captions track on the looping video; chapters/cuepoints tracks on hero video.
- User-controllable reduced motion and dark mode, plus OS `prefers-reduced-motion` support.
- Hit targets: 36–56px icon buttons, 18–24px dot `<li>` (small but above slick's 6px default).
- Buttons are sentence-case (better readability than all-caps).

Weak:
- Hero video autoplays (muted) with no `autoplay`/`muted` attributes in markup — relies on JS; if JS fails the poster shows, which is fine, but autoplay still runs for users without reduced-motion set.
- The `<h1>` lives inside a carousel slide; heading order jumps (h1 → h2 "Pastor Steven Furtick" inside slide 2 → h2 sections). Slick clones duplicate headings (`slick-cloned` h3s appear 3× in the DOM), which screen readers may read repeatedly unless `aria-hidden` is set (not visible in the HTML dump).
- Grey-on-white secondary text at `rgba(0,0,0,.6)` passes AA for body (≈4.6:1) but captions at 12px are borderline; dark-mode secondary `rgba(255,255,255,.7)` on `#0A0A0A` is fine.
- No `<footer>` landmark — footer content is inside a modal drawer, invisible to landmark navigation until opened.
- Giving FAQ headings render literal "###" prefixes in text (CMS markdown leaking: "### How do I edit my giving?").
- Slick's focus/keyboard handling is mediocre by default; the site adds focus outlines on dots but arrows sit outside the track order.

---

## 13. Weaknesses to avoid

1. **Hidden footer.** Burying address, legal and socials inside the hamburger drawer confuses users who scroll to the bottom expecting a footer; it also removes an SEO/landmark block. Keep a real `<footer>`.
2. **Three font families shipped, one used.** Inter and EB Garamond add ~10 woff2 requests of unused weight. Load only what you render.
3. **Oversized MUI theme in inline CSS** — 75 KB of Emotion CSS plus 235 KB Tailwind. Fine on their CDN, heavy for a parish site; pick one system.
4. **H1 inside a carousel** and duplicated cloned slides — heading semantics and SR verbosity suffer. If you carousel the hero, put the h1 outside the track or mark clones `aria-hidden`.
5. **Autoplaying hero video** without honouring OS reduced-motion by default (only the custom toggle disables it). Gate autoplay on `matchMedia('(prefers-reduced-motion: no-preference)')` and `saveData`.
6. **Two identical contained CTAs** in the hero — no visual hierarchy between "Get connected" and "Learn more". Make the second one a text/outline button.
7. **Duplicated CTA rows** (inside image + below image) create duplicate links in the accessibility tree and tab order. Use one row that repositions with CSS.
8. **Analytics IDs leaking into markup** (`ec-nav-central-get-involved-side-nav-baptism`) are harmless but noisy; prefer `data-` attributes.
9. **Markdown artefacts** ("###") in FAQ headings — sanitize CMS rich text.
10. **Mobile sub-nav + header = 144px of sticky chrome** on a phone; acceptable for an app-like megachurch, too much for a small parish. Keep sticky chrome ≤ 64px on mobile.
11. **Very small display type** (section titles 18→24px, hero copy modest). It reads "app", not "sanctuary". A parish wanting warmth should run larger, more generous headlines.
12. Flat monochrome palette depends entirely on strong photography; without a steady supply of high-quality photos it will look grey.

---

## 14. Reusable patterns (codeable rules)

### Tokens
```css
:root{
  --space: 8px;
  --radius-card: 16px;          /* rounded-2xl: the signature shape */
  --radius-panel: 24px;
  --radius-btn: 4px;
  --header-h-mobile: 64px;
  --header-h-desktop: 80px;
  --content-max: 1200px;        /* text/content column */
  --media-max: 1680px;          /* hero/media cards */
  --page-pad-mobile: 16px;      /* px-4 */
  --page-pad-desktop: 24px;     /* md:px-6 */
  --section-gap: 80px;          /* py-20 between bands */
  --color-ink: #000;
  --color-ink-hover: #1D1D1D;
  --color-text: rgba(0,0,0,.87);
  --color-text-2: rgba(0,0,0,.60);
  --color-text-3: rgba(0,0,0,.38);
  --color-divider: rgba(0,0,0,.12);
  --color-surface: #FFF;
  --color-surface-2: #F4F4F4;
  --color-tile: #E0E0E0;
  --color-chip: #EEEEEE;
  --color-hover-row: #F5F5F5;
  --color-focus: rgb(147,197,253);
  --scrim-dark: #1A1A1A;
  --ease-standard: cubic-bezier(.4,0,.2,1);
  --ease-out: cubic-bezier(0,0,.2,1);
  --dur-fast: 150ms;  --dur-base: 250ms;  --dur-slow: 300ms;  --dur-cover: 700ms;
}
```

### Type rules
- One sans (DM Sans or similar geometric humanist), weights 400/500/700 only. Self-host with `font-display: swap` and a size-adjusted local fallback (`size-adjust: 104.5%` for Arial vs DM Sans).
- Body 16px/1.5, tracking 0.15px; small 14px/1.43; caption 12px/1.66 tracking 0.4px.
- Section title: 700, **18px mobile → 24px ≥600px**, line-height 1.334. Card title: 700, 16px → 20px, line-height 1.33. (Scale these up 1.25–1.5× for a warmer parish feel.)
- Buttons: 500 weight, 14–16px, **sentence case**, `white-space: nowrap`, width fits content.
- Clamp card copy to 2 lines and reserve `min-height: 3rem`.

### Media card
```css
.media-card{position:relative;overflow:hidden;border-radius:var(--radius-card);aspect-ratio:16/9}
@media (min-width:600px){.media-card.hero{aspect-ratio:24/9}}
.media-card>img,.media-card>video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.media-card::after{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(26,26,26,0) 61%,#1a1a1a 93.5%,#1a1a1a)}
.media-card .copy{position:absolute;inset:0;display:flex;align-items:flex-end;gap:16px;
  max-width:var(--content-max);margin:auto;padding:16px;color:#fff;z-index:2}
```
Below 720px: `border-radius:0` (full-bleed) and move the CTA row out of the image into a plain card with `margin-top:-4px; padding:16px 16px 24px`.

### Video cover fade
```css
.cover{transition:opacity var(--dur-cover) ease-in-out, filter var(--dur-cover) ease-in-out}
.is-playing .cover{opacity:0;filter:blur(4px)}
```
Autoplay only when `matchMedia('(prefers-reduced-motion: no-preference)').matches && !navigator.connection?.saveData`; always `muted playsinline loop preload="none|metadata"`; give an Unmute (top-right, 40px) and Pause (centre, 56px) glass button: `background:#00000066; backdrop-filter:blur(2.5px); border-radius:50%`.

### Buttons
```css
.btn{display:inline-flex;align-items:center;gap:8px;padding:8px 22px;border-radius:4px;font:500 15px/1.75 inherit;
  text-transform:none;white-space:nowrap;width:fit-content;border:0;cursor:pointer;
  transition:background-color var(--dur-base) var(--ease-standard),border-color var(--dur-base) var(--ease-standard)}
.btn-primary{background:#000;color:#fff}.btn-primary:hover{background:#1D1D1D}
.btn-secondary{background:#EEE;color:#000}.btn-secondary:hover{background:#E0E0E0}
.btn-text{background:transparent;color:#000}.btn-text:hover{background:rgba(0,0,0,.04)}
.btn:focus-visible{outline:2px solid var(--color-focus);outline-offset:2px}
```
No box-shadow on buttons at any state.

### Section skeleton
```html
<section class="band">            <!-- optional background: #F4F4F4 -->
  <div class="container">         <!-- max-width:1200px; padding:0 16px (24px ≥900px) -->
    <h2 class="title">…</h2>      <!-- 18→24px bold -->
    <p class="lede">…</p>         <!-- 16px, 60% ink, max-width ~600px -->
    <div class="cards">…</div>    <!-- flex, gap 16px (24px ≥900px) -->
  </div>
</section>
```
Vertical rhythm: 80px between bands (`py-20`), 40px after the hero on mobile / 80px desktop.

### Ministry mosaic grid
`display:grid; grid-template-columns:repeat(6,1fr); gap:24px;` tiles `height:366px; border-radius:16px; padding:24px; background:#E0E0E0` with `grid-column: span 3` for the first four and `span 2` for the last three (2 + 2 + 3). Collapse to `repeat(2,1fr)` at ≥600px and 1 column below.

### Carousel
- Dots: 18px square hit targets, dot 6–8px, inactive opacity .32, active becomes a 16×6px pill (`border-radius:6px`), transition 200ms.
- Arrows: 40–48px circular Fab outside the track on desktop, hidden on touch; swipe + `scroll-snap-type:x mandatory` for simple rails.
- Mark cloned slides `aria-hidden="true"` and keep the h1 outside the track.

### Navigation
- Sticky header 64/80px, white, 1px bottom divider at 12% ink; logo left, curated 5 links right, search in the middle, account icon last.
- Drawer (320px, slide 225ms ease-out) is the complete site map; every item = **title + one-line benefit** ("Baptism — Celebrate new beginnings").
- Mobile: horizontally scroll-snapping icon tiles 72×80px for the 6–9 most-used destinations.
- Two skip links, visible on focus.

### Content rules
- Lead with the visitor's decision: four ways to attend, each with a "Find a …" CTA.
- Use short declarative taglines ending in a period for ministries.
- Repeat the Connect → Grow → Serve/Give ladder on every template; end detail pages with a 3-card "next step" module (decision / baptism / groups).
- Put seasonal items in a card carousel so the page skeleton never changes.
- Keep giving copy impact-first, then options, then accountability (annual report, audited financials, accreditation badge), then FAQs.

### Reduced motion
```css
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
html.reduced-motion *{animation:none!important;transition:none!important}   /* user toggle */
```
