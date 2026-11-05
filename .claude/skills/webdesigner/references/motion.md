# Motion: vocabulary, contract and recipes

Motion is the last layer, and the one most often overdone. Nielsen's test for any
animation: does it give feedback, show a state change, orient the visitor in space, or
strengthen a signifier? If none, cut it. Coyier's test for any implementation: does it
animate only `transform` and `opacity`, with an easing that is not linear? If not, fix it.

Contents
1. Vocabulary (measured across six sites)
2. The reduced-motion and no-JS contract
3. Recipes
   3.1 Scroll-in reveal
   3.2 Hero entrance stagger
   3.3 Button hovers (lift, fill and text roll, color, arrow)
   3.4 Card hovers (image zoom, arrow, underline wipe)
   3.5 Header: transparent to solid, hide on scroll down
   3.6 Menus and drawers with staggered groups
   3.7 Carousels and peeking rows
   3.8 Video hero done properly
   3.9 Accordion
   3.10 Marquee
   3.11 Scroll-driven CSS (sticky sheets, curtain footer, progress-linked)
   3.12 Word cycler and split-text headlines
4. Easing library

## 1. Vocabulary

| Layer | Observed values | Use |
|---|---|---|
| Micro hover (color, underline, opacity) | 150ms (Elevation icons), 200ms (VOUS, River Valley), 250ms (MUI buttons), 300ms | `200ms ease-out` |
| Hover transform (lift, nudge, scale) | 280ms `cubic-bezier(.33,1,.68,1)` (VOUS), 300ms outQuad (Austin Stone), 400ms in-out-circ (Anchor) | `300ms` strong ease-out |
| State change (hamburger morph, icon rotate, nav background) | 200 to 300ms, `cubic-bezier(.4,0,.2,1)` | `250ms` |
| Drawer or panel open | 225ms (MUI), 300ms (River Valley), 500ms (VOUS, Anchor) | `350 to 450ms` ease-out; close faster with ease-in |
| Scroll reveal | 500ms + 150ms delay (River Valley), 700 to 950ms power3.out (VOUS), 1000ms (Austin Stone), 1500ms (Anchor) | `600 to 900ms` ease-out, 16 to 40px rise |
| Hero entrance | 1000ms outCubic (Austin Stone), 1500ms with 250ms stagger (Anchor) | `900ms`, stagger 120ms |
| Image zoom | 300ms (Austin Stone), 400ms (Anchor), 800ms (COTC) | `500ms`, scale 1.04 to 1.06 |
| Carousel travel | 500ms (River Valley, Swiper), 1000ms (COTC) | `600ms` ease-out; autoplay dwell 7s if any |
| Video cover fade | 400ms (VOUS), 700ms (Elevation) | `500ms` |

Distances: 4px for hovers, 8px for popups and arrows, 16 to 40px for reveals (VOUS goes to
72px on desktop with scrub). Exits are faster than entrances and use ease-in.

## 2. The reduced-motion and no-JS contract

Three of the six sites ignored `prefers-reduced-motion` entirely and two left sections at
`opacity: 0` until JavaScript ran. Both are correctness bugs, not taste. The contract:

```css
/* 1. Content is visible by default. Motion is opt-in via a class the script adds. */
.reveal { opacity: 1; transform: none; }
html.js .reveal:not(.in) { opacity: 0; transform: translateY(24px); }
html.js .reveal { transition: opacity .7s cubic-bezier(.33,1,.68,1), transform .7s cubic-bezier(.33,1,.68,1); }

/* 2. Reduced motion removes movement everywhere, including hover transforms. */
@media (prefers-reduced-motion: reduce) {
  html.js .reveal:not(.in) { opacity: 1; transform: none; }
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; scroll-behavior: auto !important; }
}

/* 3. Hover transforms only for devices that can hover precisely. */
@media (hover: hover) and (pointer: fine) {
  .card:hover .card__img { transform: scale(1.05); }
}
```

In JavaScript, check once and bail:

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
if (reduce.matches) { /* mark everything .in, do not bind observers or timelines */ }
reduce.addEventListener('change', () => location.reload());
```

Video: under reduced motion show the poster (`video { display: none }` with the poster
as a background, or do not call `play()`), and always render a pause button.

## 3. Recipes

### 3.1 Scroll-in reveal (CSS + IntersectionObserver)

```html
<section class="reveal" data-reveal>
  <h2 class="reveal-child">What's happening</h2>
  <p class="reveal-child">…</p>
</section>
```

```css
html.js [data-reveal]:not(.in) .reveal-child { opacity: 0; transform: translateY(24px); }
html.js [data-reveal] .reveal-child { transition: opacity .7s cubic-bezier(.33,1,.68,1), transform .7s cubic-bezier(.33,1,.68,1); transition-delay: calc(var(--i, 0) * 80ms); }
```

```js
document.documentElement.classList.add('js');
if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.1 });
  document.querySelectorAll('[data-reveal]').forEach((el) => {
    el.querySelectorAll('.reveal-child').forEach((c, i) => c.style.setProperty('--i', i));
    io.observe(el);
  });
} else {
  document.querySelectorAll('[data-reveal]').forEach((el) => el.classList.add('in'));
}
```

Rules: trigger when the element is about 10 to 12% into the viewport; reveal once; stagger
children 60 to 80ms; cards in a horizontal row fade opacity-only (VOUS) so the row does
not jitter. A bundled version lives in `assets/reveal.js`.

Scroll-driven CSS alternative (no JS; progressively enhanced):

```css
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .reveal-child { animation: rise linear both; animation-timeline: view(); animation-range: entry 10% entry 45%; }
  }
}
@keyframes rise { from { opacity: 0; transform: translateY(24px); } }
```

### 3.2 Hero entrance stagger

On load, after fonts are ready (`document.fonts.ready`, with an 800ms timeout fallback),
add `is-ready` to `html`. Anchor's values: everything starts `opacity: 0;
translateY(2rem)` and rises over 1.5s with 0/250/500/750ms delays for title, media,
subtitle, buttons and nav. A tighter version that still reads as generous:

```css
.hero [data-enter] { opacity: 0; transform: translateY(28px); }
html.is-ready .hero [data-enter] { opacity: 1; transform: none; transition: opacity .9s cubic-bezier(.19,1,.22,1), transform .9s cubic-bezier(.19,1,.22,1); transition-delay: calc(var(--i) * 120ms); }
html:not(.js) .hero [data-enter], html.reduce .hero [data-enter] { opacity: 1; transform: none; }
```

Austin Stone's word cycler: an `8rem` tall `overflow: hidden` mask holding three stacked
words; `translateY(-8rem)` then `-16rem`, 1000ms outCubic, 3000ms dwell, desktop only.

### 3.3 Button hovers

Lift (VOUS): `transition: transform .2s, box-shadow .2s; :hover { transform:
translateY(-4px); box-shadow: 0 2px 5px rgba(0,0,0,.2); }`.

Color swap to accent (Austin Stone): dark pill fills with the accent color over
`.3 to .48s` strong ease-out. River Valley: gold pill turns white over `.3s`.

Fill and text roll (Anchor), the most distinctive:

```html
<a class="btn btn--roll" href="/visit"><span class="btn__label"><span>Visit us<br>Visit us</span></span><i class="btn__fill" aria-hidden="true"></i></a>
```

```css
.btn--roll { position: relative; overflow: hidden; isolation: isolate; border: 1px solid currentColor; border-radius: 999px; padding: .75rem 1.5rem; transition: color .4s cubic-bezier(.785,.135,.15,.86); }
.btn__fill { position: absolute; z-index: -1; inset: auto; width: 2rem; height: 1rem; border-radius: 999px; background: currentColor; transform: scale(0); transition: transform .4s cubic-bezier(.785,.135,.15,.86); }
.btn__label { display: block; height: 1.25em; line-height: 1.25; overflow: hidden; }
.btn__label span { display: block; transition: transform .4s cubic-bezier(.785,.135,.15,.86); }
@media (hover:hover) and (pointer:fine) {
  .btn--roll:hover { color: var(--paper); }
  .btn--roll:hover .btn__fill { transform: scale(13); background: var(--ink); }
  .btn--roll:hover .btn__label span { transform: translateY(-50%); }
}
```

Trailing arrow (COTC, VOUS): every CTA ends with a 20px arrow icon; on hover the arrow
moves `translateX(4px)` over 200ms. Cheap and consistent.

### 3.4 Card hovers

Image zoom + arrow nudge (Austin Stone, Anchor, COTC):

```css
.card__media { overflow: hidden; border-radius: var(--r-lg); }
.card__media img { transition: transform .5s cubic-bezier(.33,1,.68,1); }
.card__arrow { transition: transform .3s cubic-bezier(.19,1,.22,1); }
@media (hover:hover) and (pointer:fine) {
  .card:hover .card__media img { transform: scale(1.05); }
  .card:hover .card__arrow { transform: translate(4px, -4px); }
}
```

River Valley's choreography: the image rests at `scale(1.1)` and settles to `1` on hover
over 300ms; a gold arrow rises from `translateY(101%)`; a 2px underline wipes in from
`translateX(-101%)`, both 500ms `cubic-bezier(.19,1,.22,1)`; on leave the underline exits
to the right, then resets instantly.

Whole-card link: make the card an `article` with one real `a` inside the heading and
stretch it with `a::after { content:""; position:absolute; inset:0 }`. Never an empty
overlay anchor.

### 3.5 Header behaviors

Transparent over hero, solid after scroll (Austin Stone, COTC):

```css
.site-header { position: sticky; top: 0; z-index: 100; transition: background-color .25s, color .25s, backdrop-filter .25s; }
.site-header.is-top { background: transparent; color: #fff; }
.site-header:not(.is-top) { background: rgba(255,255,255,.72); color: var(--ink); backdrop-filter: blur(8px); border-bottom: 1px solid rgba(0,0,0,.08); }
```

Toggle `is-top` when `scrollY < 80`. Austin Stone also hides the bar on scroll down and
returns it on scroll up (`translateY(-100%)`, 700ms outCubic). Implement with a small
scroll delta check (`> 8px` down after 120px hides; any up shows). Never hide the header
while a menu is open or focus is inside it.

COTC's pill variant: a centered pill with `padding: 6px; border-radius: 6px;
background: rgba(255,255,255,.9); backdrop-filter: blur(7px)`, with `margin-bottom:
calc(-1 * var(--nav-h))` so the hero runs underneath; `.is-top` makes it transparent
and inverts the logo.

### 3.6 Menus and drawers

Panel: slide from its edge over 350 to 450ms strong ease-out; overlay fades 0 to .5 black.
Groups inside rise from `translateY(10%)` with delays of 100 to 150ms per group (Anchor:
150/250/450/550/650/750ms, 500ms out-sine). Hamburger bars morph over `.3s
cubic-bezier(.4,0,.2,1)`.

Semantics are part of the design: `role="dialog" aria-modal="true"`, `inert` on the rest of
the page, focus moved to the first link, focus trapped, Escape closes, focus returns to the
button, body scroll locked, `max-height: 100dvh; overflow: auto` on the panel. Under
reduced motion the panel appears instantly.

### 3.7 Carousels and peeking rows

Prefer a native overflow row (VOUS):

```css
.row { display: flex; gap: clamp(16px, 3vw, 50px); overflow-x: auto; overscroll-behavior-x: contain; scroll-snap-type: x mandatory; scrollbar-width: none; padding-inline: var(--gutter); scroll-padding-inline: var(--gutter); }
.row > * { flex: 0 0 min(85vw, 350px); scroll-snap-align: start; }
```

Arrows below the row scroll to the next card's `offsetLeft` with `scrollTo({behavior:
'smooth'})`; disabled arrows at `opacity: .25`. If a library is justified, copy River
Valley's fractional slides per view (1.1 / 1.5 / 2.25 / 3.25 / 4.25 at 0 / 480 / 767 / 990 /
1755px) and COTC's dwell (7000ms) and travel (1000ms, `cubic-bezier(.25,1,.5,1)`). Never
auto-advance a hero carousel; if a content carousel autoplays, pause on hover, focus and
reduced motion, and keep keyboard arrows working.

### 3.8 Video hero done properly

```html
<section class="hero">
  <video class="hero__video" autoplay muted loop playsinline poster="/images/hero-poster.jpg" preload="metadata" aria-hidden="true">
    <source src="/videos/hero.webm" type="video/webm">
    <source src="/videos/hero.mp4" type="video/mp4">
  </video>
  <div class="hero__scrim"></div>
  <div class="hero__content">…</div>
  <button class="hero__pause" type="button" aria-pressed="false">Pause video</button>
</section>
```

```css
.hero { position: relative; min-height: 85svh; display: grid; align-items: end; isolation: isolate; }
.hero__video, .hero__scrim { position: absolute; inset: 0; z-index: -1; }
.hero__video { width: 100%; height: 100%; object-fit: cover; }
.hero__scrim { background: linear-gradient(180deg, rgba(0,0,0,.15), rgba(0,0,0,.55)); }
.hero__pause { position: absolute; right: 1rem; bottom: 1rem; width: 44px; height: 44px; border-radius: 50%; background: rgba(0,0,0,.4); color: #fff; backdrop-filter: blur(2.5px); }
@media (prefers-reduced-motion: reduce) { .hero__video { display: none; } .hero { background: url(/images/hero-poster.jpg) center/cover; } }
```

Fade the poster or an ink wash out over 400 to 700ms on `canplay` (VOUS, Elevation), with a
keyframe fallback at 4s so a stalled video never leaves a black screen. Keep footage calm,
under 15 seconds, 1080p or less, with no faces talking; repeat the hero CTAs below the
media on phones (Elevation). Do not put the only `h1` in the video.

### 3.9 Accordion

Use `details`/`summary` for semantics. For smooth height, animate `grid-template-rows: 0fr
-> 1fr` on a wrapper (works without measuring), 350 to 500ms ease-out; COTC uses 1s
`cubic-bezier(.526,.012,.456,.995)` which is on the slow side. Rotate or scale the plus icon
over 200ms.

### 3.10 Marquee

Austin Stone's photo marquee is the right implementation: duplicate the track, `@keyframes
marquee { to { transform: translateX(-50%) } }` at 40s linear, `animation-play-state: paused`
on `:hover` and `:focus-within`, and disabled under reduced motion. Never put essential
content in it.

### 3.11 Scroll-driven CSS (sticky sheets, curtain footer)

Anchor's parking sheet and curtain footer need no JavaScript:

```css
.sheet { position: sticky; top: calc(-1 * var(--sheet-overflow, 60vh)); border-radius: 50px 50px 0 0; }
.footer-wrap { margin-top: -100vh; }
.site-footer { position: sticky; bottom: 0; }
```

Progress-linked effects (COTC's logo scrub over the first 7% of scroll, Anchor's footer
inner fade from 47 to 58% visibility) belong in `animation-timeline: scroll()` or `view()`
behind `@supports`, with the static end state as the default.

### 3.12 Split-text headlines

Split by word, not by character, wrap each word in a `span` with `--i`, and rise each by
`0.4em` with 40 to 60ms stagger. Keep the un-split text for assistive tech (`aria-label`
on the heading or split with `aria-hidden` spans plus a visually hidden copy). Only on the
hero and one statement band; everywhere else it is noise.

## 4. Easing library

```css
:root {
  --ease-standard: cubic-bezier(.4, 0, .2, 1);       /* state changes, MUI/Material */
  --ease-out-soft: cubic-bezier(.33, 1, .68, 1);     /* VOUS house easing; hovers, reveals */
  --ease-out-expo: cubic-bezier(.19, 1, .22, 1);     /* panels, underline wipes */
  --ease-out-quart: cubic-bezier(.25, 1, .5, 1);     /* carousel travel */
  --ease-in-out-circ: cubic-bezier(.785, .135, .15, .86); /* button choreography */
  --ease-in: cubic-bezier(.55, .055, .675, .19);     /* exits only */
  --dur-fast: 200ms; --dur-base: 300ms; --dur-panel: 420ms; --dur-reveal: 700ms; --dur-hero: 900ms;
}
```

Never `linear` for UI (only for marquees), never `ease-in` for entrances, never bounce or
elastic curves on a site whose job is calm and trust.
