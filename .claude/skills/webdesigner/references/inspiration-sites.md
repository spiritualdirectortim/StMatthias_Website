# Inspiration sites: what to borrow, what to avoid

Six contemporary church websites were studied in depth (raw HTML, first-party CSS,
interaction bundles, secondary pages, screenshots) in November 2026. This file is the
comparative digest. The full per-site studies, with measured values and codeable
patterns, are in `sites/<name>.md`; read one when you want to reproduce a specific feel.

## At a glance

| Site | Stack | Fonts | Palette | Hero | Motion engine | Reduced motion |
|---|---|---|---|---|---|---|
| Elevation (`sites/elevationchurch.md`) | Next.js, Tailwind, MUI, DatoCMS | DM Sans only | Black/white/greys, orange logo only | Rounded carousel card with muted video | CSS transitions only | Yes, plus user toggle |
| Austin Stone (`sites/austinstone.md`) | Webflow, IX2, Finsweet | Proxima Nova only | #282828 / white / #f4f4f4, one blue #00a3e1 | 100vh photo, bottom-left copy, word cycler | Webflow IX2 | Marquee only |
| VOUS (`sites/vouschurch.md`) | Webflow, GSAP + ScrollTrigger | Inter Tight, Inter, Spline Sans Mono | Greige #e8e6e3, ink #131212, gold #c6beab | 100svh silent sermon video, no headline | GSAP | Yes |
| River Valley (`sites/rivervalley.md`) | Webflow, IX2, Swiper | Realist, Realist Wide | Near-black #231f20, gold #d3b975 | 100svh video, small wordmark, two gold pills | Webflow IX2 | None |
| Church of the City (`sites/cotc.md`) | Webflow, Splide, Lottie | Inter Display + Inter | #fafafa / #252525, red live dot | 85vh video, headline with period, two CTAs | CSS + Splide | None |
| Anchor Tacoma (`sites/anchortacoma.md`) | Webflow, IX2, Lottie | Metropolis only | #272727 ink on cream #fbf8f3 | Dark band with rounded photo card, 200px wordmark straddling it | Webflow IX2 | Menu only |

## What all six agree on (treat as the baseline)

- **Near-monochrome palette with one accent.** Warmth and color come from photography
  of real people, not from the UI. Accents are used sparingly: links, one button, eyebrows.
- **One or two families, heavy use of weight and case for hierarchy.** Uppercase tracked
  labels (eyebrows, nav, buttons) at 12 to 14px against sentence-case headlines.
- **Visitor-first content.** Nav of five or six verbs (Visit, Watch, Give, About, Events).
  "Visit" or "Plan a visit" is the persistent primary CTA; Give is distinct but secondary.
- **Service times and locations on the homepage**, usually right after the hero.
- **A "next steps" rail of cards at the end of every page** (visit, groups, kids,
  students, watch, serve, give).
- **Large radii and no drop shadows.** Depth from 1px borders at 10 to 12% ink, backdrop
  blur on glass chrome, and gradients. Radii 12 to 50px on cards and sheets.
- **Section rhythm of 60 to 120px desktop, 40 to 64px phone**, alternating light, photo,
  dark, light, dark footer.
- **Motion vocabulary:** 200 to 300ms hovers, 300 to 500ms panels, 500 to 1000ms reveals,
  800 to 1500ms hero entrances; strong ease-out curves; distances of 4 to 8px for hovers
  and 16 to 72px for reveals; nothing bounces.
- **Peeking carousels** (track narrower than the viewport, overflow visible, arrows in the
  section header rather than over slides).
- **Outsource transactions** (giving to Pushpay or Church Center, registration to Planning
  Center, video to YouTube or Vimeo) and keep on-site pages short and explanatory.

## Where they diverge (choose deliberately)

| Decision | Options seen | Guidance |
|---|---|---|
| Hero | Full-viewport video (VOUS, River Valley, COTC); full-viewport photo with word cycler (Austin Stone); contained rounded media card (Elevation); photo card with giant wordmark overlap (Anchor) | Video only if you have calm, well-shot footage and will add poster, pause and reduced-motion fallback. Otherwise the contained card or photo hero reads just as premium and loads faster. |
| Header | Fixed solid white (VOUS); transparent over hero then solid on scroll (Austin Stone, COTC); transparent and never sticky (River Valley, Anchor); sticky with hamburger everywhere (Elevation) | Transparent over hero, solid after ~80px scroll, hide on scroll down and return on scroll up on long pages. Keep text links visible on desktop. |
| Navigation menu | Right drawer (River Valley); left drawer that is also the footer (Elevation); slide-down mega menu (VOUS); full-screen overlay with giant links (COTC, Anchor); fixed inset panel (Austin Stone) | Any works if it has dialog semantics, focus trap, Escape and staggered reveal. Full-screen overlays with four or five giant verbs are the most distinctive. |
| Headline scale | Giant caps (Anchor 200px wordmark, Austin Stone 112px); modest (Elevation 24px section titles, River Valley 27px uppercase hero) | Giant type needs few words and perfect kerning. Modest type needs excellent photography. Both work; mixing a giant display with long copy does not. |
| Scroll reveals | Everywhere (Anchor, River Valley, VOUS); none at all (COTC, Elevation) | Both read as premium. If you reveal, do it once, under 1s, and never leave content hidden without JS. |
| Button style | Pill with lift and shadow (VOUS); pill with fill-and-text-roll (Anchor); frosted glass with trailing arrow (COTC); dark pill to accent on hover (Austin Stone); flat 4px (Elevation) | Pick one primary and one ghost/outline variant and use them everywhere. Trailing arrow on every CTA (COTC) is a cheap consistency win. |
| Labels | Uppercase tracked sans (most); monospace (VOUS); bordered chips (COTC) | Mono or chips are distinctive; tracked caps are safe. |

## Per-site: signature, borrow, avoid

### Elevation Church
- **Signature:** flat, app-like, monochrome; `rounded-2xl` (16px) on everything; a
  320px drawer that is the whole site map; "Title plus one-line benefit" on every menu
  item ("Baptism: Celebrate new beginnings").
- **Borrow:** menu items with benefit lines; detail pages ending with a 3-card "Take your
  next step"; giving page order (impact, options, Give Now, accountability, FAQ); glass
  Unmute/Pause controls on hero video (`#00000066`, `backdrop-filter: blur(2.5px)`);
  hero copy repeated below the media on mobile; `html.reduced-motion` user toggle.
- **Avoid:** footer hidden in a drawer with no landmark; `h1` inside a carousel with
  cloned slides; autoplay not gated on reduced motion; identical twin CTAs; 144px of
  sticky chrome on mobile.
- **Values:** DM Sans 400/500/700; body 16/1.5; section titles 18 to 24px/700; container
  1200px with 16/24px gutters; header 64/80px; bands 80px apart; MUI button transition
  `250ms cubic-bezier(.4,0,.2,1)`; video cover fade `700ms ease-in-out`.

### Austin Stone
- **Signature:** confident monochrome with one blue accent; hero word cycler in an
  8rem mask; header that hides on scroll down and returns on scroll up; eyebrow labels on
  every section; a single "VISIT" pill repeated on every page.
- **Borrow:** navbar hide/show (`translateY(-100%) 700ms outCubic`, hide after 24%
  scroll down, return on 12% scroll up); transparent-over-hero then
  `rgba(255,255,255,.64) + blur(5px)`; mega-menu tile hover that slides a label stack in a
  mask; card hover image scale 1.05 over 300ms plus arrow nudge 6px; a 40s CSS marquee
  that pauses on hover and respects reduced motion; closing band pattern (question
  headline, one button, follow, contact).
- **Avoid:** 380KB CSS and 923KB interaction bundle; two nav systems; hidden tabs that
  pre-render 18 cards; hard-coded 120px tracks tied to header height.
- **Values:** Proxima Nova; display 7rem/7.6rem 700 tracking -1px; h2 2.4rem; eyebrow
  1rem/500 caps tracking 2px; buttons .8rem/600 caps tracking 2px, pill 16px 32px,
  `transition: all .48s cubic-bezier(.509,-.005,.111,1.007)`; section padding 120/80/64px.

### VOUS Church
- **Signature:** greige canvas, white square cards with no radius or shadow, monospace
  for all metadata, a silent 4K sermon loop as the hero with no headline, GSAP scroll
  reveals with scrub on desktop.
- **Borrow:** mono labels and numerals ("01") on cards; pill button with 4px lift and
  `0 2px 5px rgba(0,0,0,.2)`; native overflow rows as carousels with pager arrows below
  and a left-edge blur fade; the reveal recipe (section `y 72, scale .985, .95s power3.out`,
  children `y 34, .7s, stagger .06`); hover gated on `(hover:hover) and (pointer:fine)`;
  hero ink wash that fades out on `canplay` with a 4s keyframe fallback.
- **Avoid:** no headline or CTA in the hero; multiple `h1`s; 4K video without poster;
  three drag rows on one page; a persistent frosted popup.
- **Values:** Inter Tight 500/600 headings, Inter body 20px/300, Spline Sans Mono labels
  14px caps tracking 1px; scale 12/14/16/20/22/24/28/36/48/64/80; section padding 60/40;
  gutters 10% (15% at 1440+); house easing `cubic-bezier(.33,1,.68,1)`.

### River Valley
- **Signature:** warm near-black and gold two-color system; everything label-like is
  uppercase at 0.2em tracking; deliberately small hero title so video and buttons
  dominate; glass cards (`#00000069`, `blur(20px)`, `#474747` border).
- **Borrow:** two-color discipline where gold is the only accent and every hover goes
  gold; the card hover choreography (image rests at 1.1 and settles to 1, gold arrow rises
  from `translateY(101%)`, 2px underline wipes from `translateX(-101%)` over 500ms
  `cubic-bezier(.19,1,.22,1)`); right drawer with search on top and a 2-column link grid;
  Swiper with fractional slides per view (1.1 / 1.5 / 2.25 / 3.25 / 4.25).
- **Avoid:** 55 font faces loaded; "Learn More" everywhere; `alt=""` everywhere;
  div buttons and `a11y: false`; autoplay with no pause; placeholder staff text shipped.
- **Values:** Realist 300/500/700; body 1.1rem/1.5/500; h1 4rem, h2 3rem, h3 2rem;
  labels .9rem caps 0.2em; pills `.8rem 1.75rem`, radius 4rem; reveal `translateY 1.5rem,
  500ms ease, 150ms delay`; section padding 4rem/8rem; cards radius 1.25rem.

### Church of the City
- **Signature:** sticky frosted pill nav that is transparent at the very top; headline
  with a period ("Practicing the Way of Jesus."); frosted-glass buttons with a trailing
  arrow; portrait ministry cards with a blurred-duplicate scrim; no scroll reveals at all.
- **Borrow:** the pill nav and `.is-top` transparent state; exactly two hero CTAs (light
  primary "Join us in person", glass secondary "Join us online"); the blurred-duplicate
  scrim technique; "small and bold, big and light" weight inversion; events carousel with
  7s dwell and 1s travel; click-to-load video posters; `data-show-at` live-now scheduling;
  dismissible announcement bar keyed by message slug; footer "sheet" edge.
- **Avoid:** 12.8px mobile body; eyebrows at opacity .25; no hover state on primary
  buttons; empty overlay anchors; 18 static font files; stale copyright.
- **Values:** h1 40/1.1, h2 28/1.0, h3 22/1.2, body 16/1.4, pull quote 64/1.1 at -0.02em;
  container 1480px, gutter 24px; radii 12/5/16; glass button `17px 30px`, `blur(7.5px)`,
  inset highlight `0 -2px 8px 1px rgba(255,255,255,.15)`; image hover `scale(1.1) .8s
  cubic-bezier(.515,.012,.316,1.001)`.

### Anchor Tacoma
- **Signature:** cream paper, one bold uppercase family, enormous wordmark straddling a
  rounded photo card, sticky "sheet" sections that park while the next slides over, footer
  that reveals like a curtain, pill buttons with a fill-and-text-roll hover.
- **Borrow:** hero overlap composition; sticky sheet and curtain footer (CSS only);
  fluid root font size formula so every rem scales; two-easing discipline
  (`cubic-bezier(.19,1,.22,1)` at 500ms for color/opacity, `cubic-bezier(.785,.135,.15,.86)`
  at 400ms for choreography); mega menu with dialog semantics, inert background, focus
  trap, Escape and staggered groups; nav reduced to Vision, logo, Give, "Visit Us".
- **Avoid:** no sticky nav; sections hidden until JS; 1.5s entrances with no opt-out;
  `#7e7e7e` hover text failing contrast at 13px; `loading="eager"` on everything;
  clickable divs over invisible anchors.
- **Values:** Metropolis 700 caps tracking -0.02em, line-height .9 to 1; hero 12.5rem,
  h1 7.8rem, h2 3.5rem, h3 2.75rem; body 1rem/1.5; radii 35/25/50px and 2.5rem pills;
  containers 80/64/48rem; `padding-inline: 5%`; section padding 7/5/3rem.

## How to use this when a user says "make it feel like..."

1. Open the matching `sites/<name>.md` and read sections 2 (typography), 4 (layout),
   8 (animations) and 14 (reusable patterns).
2. Borrow the composition and the motion values, not the brand: swap in the project's
   own tokens, fonts and photography.
3. Fix the site's listed weaknesses as you go; the user is asking for the feel, not the
   bugs.
4. Say which site informed which decision so the user can push back.
