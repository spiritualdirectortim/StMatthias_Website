# Layout patterns and section recipes

Each recipe below was observed on at least one of the six inspiration sites and rewritten
to satisfy the UX and craft rules in `SKILL.md`. Copy the markup and CSS, then swap in the
project's tokens. Build mobile-first; the breakpoints are where the content breaks
(Marcotte), not where devices are.

Contents
1. Tokens and foundations
2. Header and navigation (three variants)
3. Heroes (four variants)
4. Visit block (times, locations, what to expect)
5. Statement band
6. Events and card rows
7. Next-steps rail
8. Ministry or portrait card grid
9. Give page
10. Footer
11. Page templates
12. Responsive navigation and content choreography

## 1. Tokens and foundations

```css
:root {
  /* color: near-monochrome plus one accent; warmth from photography */
  --paper: #faf8f5; --paper-2: #f1ede6; --ink: #1e1e1e; --ink-2: #4a4a4a; --line: rgba(30,30,30,.12);
  --accent: #b8562f; --accent-deep: #8f3f20; --on-dark: #f5f2ec;
  /* spacing (8px base) and rhythm */
  --s-1: .5rem; --s-2: 1rem; --s-3: 1.5rem; --s-4: 2rem; --s-5: 3rem; --s-6: 4rem; --s-7: 6rem;
  --section: clamp(3.5rem, 3rem + 3vw, 7.5rem);
  --gutter: clamp(1rem, 5vw, 4rem);
  --container: 80rem; --container-prose: 65ch; --container-narrow: 48rem;
  /* shape */
  --r-sm: 6px; --r: 12px; --r-lg: 20px; --r-xl: 32px; --r-pill: 999px;
  --shadow: 0 4px 20px rgba(0,0,0,.08);
  /* motion: see motion.md */
  --ease: cubic-bezier(.33,1,.68,1); --ease-expo: cubic-bezier(.19,1,.22,1);
  --dur-fast: 200ms; --dur: 300ms; --dur-panel: 420ms; --dur-reveal: 700ms;
}
html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--paper); color: var(--ink); font: 400 var(--step-0)/1.55 var(--font-body); }
img, video { max-width: 100%; height: auto; display: block; }
.container { width: min(100% - 2 * var(--gutter), var(--container)); margin-inline: auto; }
.section { padding-block: var(--section); }
.section--dark { background: var(--ink); color: var(--on-dark); }
.flow > * + * { margin-block-start: var(--flow, 1em); }
:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }
.visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
```

Observed containers: 1200px (Elevation), 1280px / 80rem (Anchor), 1440px cap (Austin
Stone), 1480px (COTC), 120rem (River Valley). Observed gutters: 16/24px (Elevation), 5%
(Anchor), 10% (VOUS), 2.5rem (River Valley). Observed section padding: 60/40 (VOUS), 80
(Elevation), 112/80/48 (Anchor), 120/80/64 (Austin Stone), 128/64 (River Valley).

## 2. Header and navigation

Rules first: text links visible on desktop; at most five or six verbs; "Give" styled as a
button; a skip link; sticky on long pages; the menu button is a real `button` with
`aria-expanded` and `aria-controls`.

### 2a. Transparent over hero, solid on scroll (Austin Stone, COTC)

```html
<a class="skip" href="#main">Skip to content</a>
<header class="site-header is-top" data-header>
  <div class="container site-header__bar">
    <a class="brand" href="/" aria-label="Home"><img src="/images/logo.svg" alt="" width="140" height="36"></a>
    <nav class="nav" aria-label="Primary">
      <ul><li><a href="/visit/">Visit</a></li><li><a href="/mass-times/">Mass times</a></li><li><a href="/events/">Events</a></li><li><a href="/ministries/">Ministries</a></li><li><a href="/about-us/">About</a></li></ul>
    </nav>
    <a class="btn btn--primary btn--sm" href="/support-us/">Give</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
  </div>
</header>
```

```css
.site-header { position: sticky; top: 0; z-index: 100; transition: background-color var(--dur), color var(--dur), transform 600ms var(--ease-expo); }
.site-header__bar { display: flex; align-items: center; gap: var(--s-4); min-height: 72px; }
.nav { margin-inline-start: auto; } .nav ul { display: flex; gap: var(--s-3); list-style: none; margin: 0; padding: 0; }
.nav a { text-decoration: none; color: inherit; padding-block: .5rem; position: relative; }
.nav a::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 2px; background: currentColor; transform: scaleX(0); transform-origin: left; transition: transform var(--dur-fast) var(--ease); }
.nav a:hover::after, .nav a[aria-current="page"]::after { transform: scaleX(1); }
.site-header.is-top { background: transparent; color: #fff; }
.site-header:not(.is-top) { background: rgba(250,248,245,.78); color: var(--ink); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }
.site-header.is-hidden { transform: translateY(-100%); }
@media (max-width: 47.99em) { .nav { display: none; } }   /* hidden links repeated inside the menu and in the footer */
```

### 2b. Centered frosted pill (COTC)

Same markup; the bar becomes a centered pill: `padding: 6px 6px 6px 16px; border-radius:
8px; background: rgba(255,255,255,.9); border: 1px solid rgba(123,123,123,.2);
backdrop-filter: blur(7px)`. `.is-top` makes it transparent with inverted logo and an
outlined menu button. Give the header `margin-bottom: calc(-1 * var(--nav-h))` so the hero
runs beneath it.

### 2c. Full-screen menu with giant verbs (COTC, Anchor)

```html
<div class="menu" id="menu" role="dialog" aria-modal="true" aria-label="Site menu" hidden>
  <div class="menu__primary"><a href="/visit/">Plan a visit</a><a href="/watch/">Watch</a><a href="/support-us/">Give</a><a href="/events/">Events</a></div>
  <div class="menu__groups">
    <section><h2>New here</h2><ul>…</ul></section>
    <section><h2>Grow</h2><ul>…</ul></section>
    <section><h2>Serve</h2><ul>…</ul></section>
  </div>
  <address class="menu__contact">…</address>
</div>
```

`position: fixed; inset: 0; background: rgba(20,20,20,.92); backdrop-filter: blur(10px);
overflow: auto; max-height: 100dvh; padding: calc(var(--nav-h) + var(--s-5)) var(--gutter)
var(--s-6)`. Primary links at `clamp(2rem, 5vw, 3rem)` weight 600 with `translateX(4px)`
hover; groups in `grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr))`; group
reveal delays of 100ms steps. Script: toggle `hidden`, set `inert` on `header`, `main`
and `footer`, move focus in, trap it, Escape closes, return focus to the button, lock body
scroll. Elevation's trick is worth copying: each item is "Title plus one-line benefit".

## 3. Heroes

Common rules: one `h1` with one idea; one or two CTAs (primary filled, secondary ghost or
glass); copy bottom-left or centered, never both; scrim strong enough for 4.5:1 on white
text; CTAs repeated below the media on phones if the media is tall; `min-height` in `svh`.

### 3a. Full-bleed photo or video, copy bottom-left (Austin Stone, COTC, River Valley)

```html
<section class="hero" aria-labelledby="hero-title">
  <picture class="hero__media"><source media="(min-width: 48em)" srcset="/images/hero-wide.avif" type="image/avif"><img src="/images/hero.jpg" alt="" width="1600" height="1000" fetchpriority="high"></picture>
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="container hero__content">
    <p class="eyebrow" data-enter style="--i:0">A Catholic parish in Redondo Beach</p>
    <h1 id="hero-title" data-enter style="--i:1">You are welcome here.</h1>
    <p class="hero__lede" data-enter style="--i:2">Sunday Mass at 8, 10 and 12. Doors open twenty minutes early.</p>
    <div class="cluster" data-enter style="--i:3"><a class="btn btn--primary" href="/visit/">Plan a visit</a><a class="btn btn--ghost" href="/mass-times/">Mass times</a></div>
  </div>
</section>
```

```css
.hero { position: relative; isolation: isolate; min-height: min(85svh, 56rem); display: grid; align-items: end; color: #fff; padding-block: calc(var(--nav-h, 72px) + var(--s-5)) var(--s-6); }
.hero__media, .hero__scrim { position: absolute; inset: 0; z-index: -1; }
.hero__media img { width: 100%; height: 100%; object-fit: cover; object-position: var(--focal, 50% 40%); }
.hero__scrim { background: linear-gradient(180deg, rgba(0,0,0,.18) 0%, rgba(0,0,0,.08) 40%, rgba(0,0,0,.62) 100%); }
.hero__content { max-width: 40rem; }
.hero h1 { font: var(--heading-weight, 400) var(--display)/1.02 var(--font-display); letter-spacing: -.02em; margin: 0 0 var(--s-3); text-wrap: balance; }
.hero__lede { font-size: var(--step-1); max-width: 32rem; }
@media (max-width: 47.99em) { .hero { min-height: 70svh; } }
```

For video, see `motion.md` section 3.8.

### 3b. Contained rounded media card (Elevation)

The hero is a card inside the container, not a full-bleed banner: `aspect-ratio: 4/3.5`
on phones, `3/2` on tablets, `24/9` on desktop; `border-radius: var(--r-xl); overflow:
hidden`; copy bottom-left over `linear-gradient(180deg, transparent 60%, rgba(26,26,26,.95)
100%)`; the same CTAs repeated as a row below the card on phones. Pair with a solid header.
Fastest to load and easiest to make accessible.

### 3c. Band plus overlapping card with giant wordmark (Anchor)

A dark band (`height: 43.5rem`) holds a rounded photo card (`min-height: 37.5rem;
border-radius: 35px`) that hangs below the band onto the cream canvas; the title block is
pulled up (`margin-top: -31rem`) so a 200px wordmark straddles the card's top edge.
Needs a one-word or two-word title. See `sites/anchortacoma.md` section 14.

### 3d. Statement hero (no media)

Display headline at `--display`, one sentence, one CTA, on paper or ink, with the photo
band following as section two. Use when photography is weak; type carries it.

## 4. Visit block

Put it right after the hero. Visitors come for when and where.

```html
<section class="section visit" aria-labelledby="visit-title">
  <div class="container visit__grid">
    <div class="flow">
      <p class="eyebrow">Join us</p>
      <h2 id="visit-title">Mass times</h2>
      <ul class="times">
        <li><strong>Saturday</strong> 5:00 pm Vigil</li>
        <li><strong>Sunday</strong> 8:00, 10:00 am, 12:00 pm</li>
        <li><strong>Weekdays</strong> 8:00 am</li>
      </ul>
      <address>123 Example Ave, Redondo Beach, CA 90277 · <a href="https://maps…">Directions</a></address>
      <a class="btn btn--primary" href="/visit/">What to expect</a>
    </div>
    <img src="/images/church-front.jpg" alt="The front steps and open doors of St. Matthias" width="1200" height="900" loading="lazy">
  </div>
</section>
```

```css
.visit__grid { display: grid; gap: var(--s-5); align-items: center; grid-template-columns: repeat(auto-fit, minmax(min(100%, 22rem), 1fr)); }
.times { list-style: none; padding: 0; margin: 0; display: grid; gap: var(--s-1); }
.times li { display: flex; gap: var(--s-2); justify-content: space-between; padding-block: var(--s-1); border-bottom: 1px solid var(--line); }
.times strong { font-family: var(--font-display); font-weight: 500; }
```

Multi-location variant (COTC, River Valley): white cards `border-radius: var(--r-lg);
padding: var(--s-3); box-shadow: var(--shadow)` with a dot plus name, grey address, times
on the right, and a small outlined "More info" link, in an auto-fit grid of `minmax(18rem,
1fr)`.

## 5. Statement band

One photo inside the gutters or full-bleed, dark wash, a centered 36 to 48px light
headline in two lines, no button (VOUS). Or a scripture pull quote on paper: eyebrow chip,
quote at 56 to 64px weight 400, reference row with a dot (COTC). One per page.

```css
.band { position: relative; isolation: isolate; color: var(--on-dark); padding-block: var(--s-7); text-align: center; }
.band__img { position: absolute; inset: 0; z-index: -1; width: 100%; height: 100%; object-fit: cover; filter: brightness(.55) saturate(.85); }
.band h2 { font: 400 var(--step-4)/1.15 var(--font-display); max-width: 24ch; margin-inline: auto; text-wrap: balance; }
```

## 6. Events and card rows

Section head with headline left and "All events" link right (COTC):

```css
.sec-head { display: flex; flex-wrap: wrap; align-items: end; justify-content: space-between; gap: var(--s-3); margin-bottom: var(--s-5); }
```

Event card: date block (display face, day numeral 2.5rem, month as small caps), title,
time and place line, one arrow link. Rows as native overflow carousels (motion.md 3.7) or a
responsive grid `repeat(auto-fit, minmax(min(100%, 18rem), 1fr))`. Keep "Learn more" out;
the title is the link.

## 7. Next-steps rail

Five of six sites end every page with the same rail. Make it one include.

```html
<section class="section next-steps" aria-labelledby="next-title">
  <div class="container">
    <h2 id="next-title">Take your next step</h2>
    <ul class="steps">
      <li><a href="/visit/"><img …><span>Plan a visit</span><small>What to expect on Sunday</small></a></li>
      <li><a href="/faith-formation/"><img …><span>Faith formation</span><small>For kids, teens and adults</small></a></li>
      <li><a href="/ministries/"><img …><span>Serve</span><small>Find a place to help</small></a></li>
      <li><a href="/support-us/"><img …><span>Give</span><small>Support the parish</small></a></li>
    </ul>
  </div>
</section>
```

```css
.steps { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--s-3); grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr)); }
.steps a { display: grid; gap: var(--s-2); text-decoration: none; color: inherit; border-radius: var(--r-lg); overflow: hidden; background: var(--paper-2); padding-bottom: var(--s-3); }
.steps img { aspect-ratio: 4/3; object-fit: cover; }
.steps span { font: 500 var(--step-2)/1.2 var(--font-display); padding-inline: var(--s-3); }
.steps small { padding-inline: var(--s-3); color: var(--ink-2); }
```

## 8. Ministry or portrait card grid

COTC's portrait card with a blurred-duplicate scrim is the best-looking variant: a second
copy of the same image, `filter: brightness(25%) blur(50px)`, masked with
`linear-gradient(0deg, #000 5%, transparent 70%)`, under the title and chips. Elevation's
2+2+3 mosaic (`grid-template-columns: repeat(6, 1fr)`; first row spans 3+3, second 3+3,
third 2+2+2) breaks the monotony of equal cards. Always: `aspect-ratio: 2/3` or `4/5`,
`border-radius: var(--r-lg)`, title at `--step-2`, one real link per card.

## 9. Give page

The convergent structure (Elevation, Austin Stone, River Valley): a short statement of why
giving matters and what it funds; two or three ways to give (online button to the provider,
bank/ACH recommended with fees disclosed, mail or legacy giving); accountability
(financial statements, council, audited reports); FAQ in an accordion; contact. Keep the
provider's embed below the fold or on its own page; do not open it in the hero. Never make
"Give" the hero CTA on the homepage.

## 10. Footer

A real `footer` landmark with: brand and one-line identity; address, phone, email;
service times again; three link columns mirroring the nav plus the hidden mobile links;
"Need care?" or "Contact a priest" pill; newsletter if you actually send one; socials as
32 to 40px circular icon links with accessible names; legal line with a current year
generated at build time. Dark background, `--on-dark` text, headings as 12 to 14px tracked
labels at 60% opacity. COTC's "sheet" edge (the page canvas gets a rounded bottom floating
over the footer) and Anchor's curtain footer (`.footer-wrap { margin-top: -100vh }` with a
sticky footer) are optional flourishes; the content is not optional.

## 11. Page templates

| Template | Order | Source |
|---|---|---|
| Homepage | header, hero, visit block, statement band, what's happening, next-steps rail, story or leadership, values or photo wall, footer | consensus of six |
| Visit / New here | hero with one promise, what to expect (parking, kids, length, dress), times and map, FAQ accordion, "we'll save you a seat" CTA, rail | Austin Stone, COTC, Elevation |
| Location or campus | hero, welcome info columns, latest message, campus-filtered calendar, ministries, what-to-expect FAQ, rail | COTC |
| Ministry | hero, who it is for, when and where, leader card, how to join (form or contact), related events, rail | COTC, Elevation |
| Events list | section head with filters, grid or rows of event cards, calendar embed if any, rail | all |
| Event detail | title, date/time/place block, add-to-calendar, body, register CTA, contact, rail | Elevation, River Valley |
| Watch / Sermons | latest with click-to-load player, series grid, filters, podcast links | Elevation, Austin Stone |
| Give | why, ways, accountability, FAQ, contact | section 9 |
| About / Story | statement hero, timeline or history, beliefs, leadership grid, rail | all |

## 12. Responsive navigation and content choreography

- Mobile-first order is the content priority order (Marcotte). Decide it in the HTML;
  do not rely on `order` to fix it later, because `order` breaks keyboard sequence.
- Use intrinsic layouts first (`auto-fit` grids, `flex-wrap`, `min()`); add a media or
  container query only when a component visibly breaks.
- Container queries for components that live in sidebars and main columns alike:

```css
.card-list { container-type: inline-size; }
@container (min-width: 40rem) { .card { grid-template-columns: 2fr 3fr; } }
```

- Side-by-side pairs collapse with Every Layout's switcher instead of a breakpoint:

```css
.switcher { display: flex; flex-wrap: wrap; gap: var(--s-4); }
.switcher > * { flex: 1 1 calc((40rem - 100%) * 999); }
```

- Keep 44px targets and 16px text at every width; check that the sticky header plus any
  announcement bar never exceeds about 120px of phone chrome (Elevation's 144px is too much).
