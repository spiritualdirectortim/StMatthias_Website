# Web design principles: Marcotte, Zeldman, Coyier

A working reference distilled from primary sources (read via Firecrawl on 2026-11-04).
Each section states the thinker's core principles with source URLs, gives short
attributed quotes, and ends with "How to apply it in code". A combined craft checklist
closes the document. Attribution note: where a CSS-Tricks article was written by a guest author rather than
Chris Coyier, the author is named. Quotes are verbatim from the pages read; paraphrases
are marked as such.

---

## 1. Ethan Marcotte: responsive, flexible, for everyone

### 1a. Core principles

**Responsive web design = fluid grids + flexible images + media queries, plus a change
of mindset.** The 2010 article names the three technical ingredients and immediately
insists that the real shift is philosophical: stop quarantining content into
device-specific sites and treat devices as "facets of the same experience."
Source: https://alistapart.com/article/responsive-web-design/ (A List Apart, 25 May 2010)

**The web's flexibility is an asset, not a bug.** Marcotte opens by quoting John
Allsopp's "A Dao of Web Design": print's control "is simply a function of the limitation
of the printed page"; the web should "accept the ebb and flow of things." Fifteen years
on he restates it: "We've stopped designing against a truly fluid design medium, and now
we see it as an asset."
Sources: https://alistapart.com/article/responsive-web-design/ ;
https://ethanmarcotte.com/wrote/responsive-design-at-15/ (2025)

**Proportions, not pixels: target ÷ context = result.** The "Fluid Grids" article (2009)
converts every width, margin and font-size into a ratio of its container. "Every aspect
of the grid—and the elements laid upon it—can be expressed as a proportion relative to
its container."
Source: https://alistapart.com/article/fluidgrids/

**Flexible foundation first, media queries layered on top.** From the book: "A truly
responsive design begins with a flexible layout, with media queries layered upon that
non-fixed foundation." Fluid layouts need fewer breakpoints and survive browsers that
ignore media queries.
Source: https://ethanmarcotte.com/books/responsive-web-design/full/chap04/

**Mobile first is a content-priority decision, not just a CSS order.** "If you design
mobile first, you create agreement on what matters most." Start with a small-screen-ready
layout and let each breakpoint build on the previous one with `min-width` queries; this
is progressive enhancement applied to layout.
Source: https://ethanmarcotte.com/books/responsive-web-design/full/chap05/

**Breakpoints come from the content, not from devices.** The 2010 article already applies
"resolution-specific spotfixes" where the design visibly breaks (600px, 400px, 1300px in
its demo), never at "iPhone width." Media queries are "conditional comments for the rest
of us" that let you "surgically correct issues in our layout as it scales."
Source: https://alistapart.com/article/responsive-web-design/

**Media queries do more than move boxes.** The same article lists what else a breakpoint
can tune: larger touch targets (Fitts's law), selectively revealing navigation, and
"responsive typesetting" that adjusts size and leading per display.

**Design a system of small layouts, not pages.** *Responsive Design: Patterns and
Principles* (2015) reframes the discipline: "we need to think of our responsive designs
as a network of small layout systems," each module "with its own rules for how it should
change, shift, and grow according to the needs of the content inside it." Design patterns
are "small, reusable modules" that help a layout "reach more devices (and people)."
Sources: https://ethanmarcotte.com/books/responsive-design-patterns-and-principles/ ;
https://ethanmarcotte.com/books/responsive-design-patterns-and-principles/full/chap01/

**Navigation: same access, different shapes; the hamburger is not a safe default.**
Chapter 2 surveys toggles, off-canvas panels, conditionally loaded menus and progressive
reveal. Navigation "does not need to look or work the same at every breakpoint" but must
give access to the same content. Start from a plain semantic list of links, identify the
critical links for small screens, and treat extra widescreen items as enhancements rather
than hiding a bloated desktop menu with CSS. (Paraphrase of chapter 2.)
Source: https://ethanmarcotte.com/books/responsive-design-patterns-and-principles/full/chap02/

**Content choreography (Trent Walton's term, adopted in the responsive canon).** As
columns collapse, don't just stack in source order; ask whether the hierarchy survives.
"Media queries can be used to do more than patch broken layouts." But don't redesign the
page per breakpoint either: "It's annoying—like someone rearranging the groceries in your
pantry every time you closed the door."
Source: https://trentwalton.com/2011/07/14/content-choreography/ (2011)

**Fit and finish: intrinsic ratios and flexible media.** The book's chapter on layout
shows the padding-top aspect-ratio box so embedded media "will resize proportionally."
Flexible images (`max-width: 100%`) were part of the 2010 recipe.
Source: https://ethanmarcotte.com/books/responsive-design-patterns-and-principles/full/chap03/

**Performance, accessibility and content strategy are preconditions, not polish.** "The
best responsive sites are founded upon a culture of performance"; "they plan for
accessibility and progressive enhancement from the outset"; they are "built upon a
well-researched and -executed content strategy."
Source: https://ethanmarcotte.com/wrote/responsive-design-workshop/

**The web is for everyone; accessibility is not a feature.** "'designing for the web'
means ensuring our work is accessible as broadly as possible." His own accessibility
statement commits to: semantic landmarks, a logical heading order from a single `h1`,
skip links, text equivalents for images and media, 300% zoom without breakage, sufficient
contrast, full mouse/keyboard/touch operability, and visible focus styles.
Sources: https://ethanmarcotte.com/wrote/accessibility-is-not-a-feature/ (2018) ;
https://ethanmarcotte.com/accessibility/

**Container queries are responsive design's natural evolution.** "As my designs have
become more component-based, media queries have felt like an increasingly creaky tool."
A flexible layout adapted by container queries is "absolutely a responsive layout"; today
he would list the ingredients as fluid grids, flexible images, and "some combination of
media queries and/or container queries."
Source: https://ethanmarcotte.com/wrote/responsive-design-at-11-container-queries/ (2021)

### 1b. Memorable quotes

- "Fluid grids, flexible images, and media queries are the three technical ingredients for responsive web design, but it also requires a different way of thinking." (ALA, 2010)
- "Rather than tailoring disconnected designs to each of an ever-increasing number of web devices, we can treat them as facets of the same experience." (ALA, 2010)
- "Every aspect of the grid—and the elements laid upon it—can be expressed as a proportion relative to its container." (Fluid Grids, 2009)
- "A truly responsive design begins with a flexible layout, with media queries layered upon that non-fixed foundation." (RWD, ch. 4)
- "If you design mobile first, you create agreement on what matters most." (RWD, ch. 5)
- "We need to think of our responsive designs as a network of small layout systems." (Patterns and Principles, ch. 1)
- "The best responsive sites are founded upon a culture of performance." (ethanmarcotte.com)
- "It's more than just another software feature." (on accessibility, 2018)
- "As my designs have become more component-based, media queries have felt like an increasingly creaky tool." (2021)

### 1c. The modern lineage (briefly)

- **Jen Simmons, Intrinsic Web Design (2018):** combine fixed, fluid (`fr`) and
  content-sized (`min-content`/`max-content`, `minmax()`) tracks so parts of a layout
  squish and stop "at separate moments"; embrace overlap and whitespace as shapes; "The
  fold doesn't exist."
  Source: https://zeldman.com/2018/05/02/transcript-intrinsic-web-design-with-jen-simmons-the-big-web-show/
- **Heydon Pickering and Andy Bell, Every Layout:** layout from composable primitives
  (Stack, Sidebar, Switcher, Grid, Cover, Cluster) governed by axioms such as a global
  measure. "Think of yourself as the browser's mentor, rather than its micro-manager."
  "Unless your design is founded on axioms, your output will be inconsistent and
  malformed."
  Source: https://every-layout.dev/rudiments/axioms/
- **Andy Bell, "Be the browser's mentor, not its micromanager" (2022):** fluid type and
  space scales, flexible composition instead of breakpoints, progressive enhancement:
  "set some base rules and hints, then getting out of its way." "We are all guilty of
  micromanaging the browser in some aspects, and in turn, are creating an inflexible and
  fragile user experience."
  Source: https://buildexcellentwebsit.es/

### 1d. How to apply it in code

Fluid foundation, then enhancement with content-out breakpoints (min-width):

```css
/* 1. Flexible by default: no fixed widths, proportions only */
.wrap { inline-size: min(100% - 2rem, 72rem); margin-inline: auto; }
img, video, svg { max-inline-size: 100%; block-size: auto; }

/* 2. Mobile-first: single column is the baseline, no query needed */
.layout { display: grid; gap: var(--space-m); }

/* 3. Add a breakpoint only where the content visibly breaks, in em/rem */
@media (min-width: 48em) {
  .layout { grid-template-columns: 2fr 1fr; }
}
```

Intrinsic grid that needs no breakpoints at all (Simmons/Every Layout lineage):

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(18rem, 100%), 1fr));
  gap: var(--space-m);
}
```

The Switcher (Every Layout): rows that become a column below a threshold measure:

```css
.switcher { display: flex; flex-wrap: wrap; gap: var(--space-s); }
.switcher > * { flex-grow: 1; flex-basis: calc((var(--measure, 60ch) - 100%) * 999); }
```

Container queries for component-level responsiveness:

```css
.card-list { container: cards / inline-size; }
.card { display: grid; gap: 1rem; }
@container cards (min-width: 40rem) {
  .card { grid-template-columns: 1fr 2fr; }
  .card h3 { font-size: clamp(1.25rem, 3cqi, 2rem); }
}
```

Intrinsic aspect ratio for media (modern form of the padding-top hack):

```css
.player { aspect-ratio: 16 / 9; inline-size: 100%; }
.player > iframe { inline-size: 100%; block-size: 100%; }
```

Responsive navigation that starts as a list and is enhanced, not hidden:

```html
<nav aria-label="Primary">
  <ul class="cluster">
    <li><a href="/mass-times">Mass Times</a></li>
    <li><a href="/events">Events</a></li>
    <li><a href="/about-us">About</a></li>
    <li><a href="/support-us">Give</a></li>
  </ul>
</nav>
```

```css
/* Keep the most important links visible; only collapse overflow */
.cluster { display: flex; flex-wrap: wrap; gap: var(--space-s) var(--space-m); }
@media (max-width: 40em) {
  .cluster li:nth-child(n+3) { display: none; }  /* only if a JS "More" toggle exists */
}
```

Accessibility baseline (from Marcotte's own statement):

```html
<a class="skip-link" href="#main">Skip to content</a>
<header>…</header>
<nav aria-label="Primary">…</nav>
<main id="main"><h1>Page title</h1>…</main>
<footer>…</footer>
```

```css
.skip-link { position: absolute; inset-block-start: -100%; }
.skip-link:focus { inset-block-start: 0; }
html { font-size: 100%; }           /* never block zoom; test at 300% */
```

Rules of thumb:
- Set breakpoints in `em`/`rem`, from the content's own failure points, `min-width` first.
- Prefer `fr`, `minmax()`, `auto-fit` and `clamp()` to additional breakpoints.
- Use container queries for components that appear in several contexts; media queries for
  page-level choreography.
- Every image: `max-inline-size: 100%`, intrinsic `width`/`height` attributes, `srcset` or
  `<picture>` so small screens don't download desktop bytes.
- Decide content priority before layout; the small-screen order is the canonical order.

---

## 2. Jeffrey Zeldman: standards, structure, content, readability

### 2a. Core principles

**Separate structure, presentation and behavior.** The founding argument of web standards:
semantic (X)HTML for structure, CSS for presentation, scripting for behavior. "This is not
about graphic design. It's about the separation of presentation from structure, which will
allow us to do amazing things."
Source: https://alistapart.com/article/tohell/ ("To Hell With Bad Browsers", ALA, Feb 2001)

**Forward compatibility over backward compatibility.** *Designing with Web Standards*
(2003; 3rd ed. 2009) is organised around "What Is Forward Compatibility?", with chapters
on Structure, Presentation, Behavior, "Marking Up Your Document for Sense Instead of
Style", "CSS and Accessibility Advantages" and "Accessibility Basics". Sites built on
hacks become "one more dung heap of bad code, one more web destination that will
eventually stop working as browsers and standards evolve."
Sources: https://books.google.com/books/about/Designing_with_Web_Standards.html?id=wUGTSdey6TwC ;
https://alistapart.com/article/tohell/

**Progressive enhancement, stated in 2001.** "The content of this site will be accessible
in any browser, but the design will only work in browsers that support CSS1." "It looks
better in CSS-compliant browsers, but the content is accessible to any browser or device."
Source: https://alistapart.com/article/tohell/

**Accessibility is a consequence of good markup.** Semantic structure "can help you comply
with these laws" and reaches screen readers and non-traditional devices without separate
builds.
Source: https://alistapart.com/article/tohell/

**Web design is environment design, not poster design.** "Web design is the creation of
digital environments that facilitate and encourage human activity; reflect or adapt to
individual voices and content; and change gracefully over time while always retaining
their identity." Typography and architecture are the apt comparisons: a design, like a
typeface, "is an environment for someone else's expression." Great sites accept headers,
columns and footers and win in "a hundred subtle details."
Source: https://alistapart.com/article/understandingwebdesign/ (ALA, Nov 2007)

**Style is not design.** The 2000 essay (republished 2005) argues "that trendy elements
are not the same as design," "that design is communication," "that most web design is
meant to be used" and "should therefore be usable."
Source: https://zeldman.com/2005/12/15/style-vs-design/

**Content precedes design.** "Content precedes design. Design in the absence of content is
not design, it's decoration." (Note: a Zeldman essay titled "Where's the content?" could
not be located; this 2008 post is the canonical statement of his content-first stance.)
Source: https://zeldman.com/2008/05/06/content-precedes-design/

**The readable web: big type, one column, whitespace, respect for the reader.** The 2012
redesign manifesto responded to Readability/Instapaper stripping designers out: "For a
certain kind of content, bigger type and a simpler layout just make sense, regardless of
screen size." "We can't focus so much on technology that we forget the web is often, and
quite gloriously, a transaction between reader and writer." "This design may be good,
bad, or indifferent but it is not accidental."
Source: https://zeldman.com/2012/05/18/web-design-manifesto-2012/

**Typography is the fastest route to authority and brand.** "The easiest, fastest, most
readily attainable path to clean, uncluttered, authoritative, branded design is through
typography." Large body type is "the kind you don't have to command-plus to read."
Source: https://zeldman.com/2017/02/06/readable-branded-design/ (Poynter report, 2017)

**The "95% typography" lineage (Oliver Reichenstein, iA, 2006).** "Web design is not about
picking great typefaces, it is how we use them." Macro-typography (format, grid,
hierarchy) is most of web design; "Correct leading, word and letter spacing, active white
space, and dosed use of color help readability." Treat text as a user interface.
Source: https://ia.net/topics/the-web-is-all-about-typography-period

**The Zeldman look (synthesis, not a single source):** a large, readable serif or
humanist body face; one dominant column; generous whitespace; a restricted palette with a
single strong accent (his own site's orange/red); strong personality in voice and
headlines; markup you could read without the stylesheet. The 2012 manifesto, the 2017
Poynter report and "Understanding Web Design" together describe it.

### 2b. Memorable quotes

- "This is not about graphic design. It's about the separation of presentation from structure, which will allow us to do amazing things." (2001)
- "The content of this site will be accessible in any browser, but the design will only work in browsers that support CSS1." (2001)
- "Web design is the creation of digital environments that facilitate and encourage human activity." (2007, abridged from the full definition)
- "Content precedes design. Design in the absence of content is not design, it's decoration." (2008)
- "For a certain kind of content, bigger type and a simpler layout just make sense, regardless of screen size." (2012)
- "This design may be good, bad, or indifferent but it is not accidental." (2012)
- "The easiest, fastest, most readily attainable path to clean, uncluttered, authoritative, branded design is through typography." (2017)
- "That design is communication." / "That most web design should therefore be usable." (Style vs. Design)
- Reichenstein: "Web design is not about picking great typefaces, it is how we use them." (2006)

### 2c. How to apply it in code

Structure first: a document that reads correctly with CSS off.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mass Times | St. Matthias Parish</title>
  <link rel="stylesheet" href="/css/site.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header>
    <a href="/" class="brand">St. Matthias</a>
    <nav aria-label="Primary"><ul>…</ul></nav>
  </header>
  <main id="main">
    <article>
      <h1>Mass Times</h1>
      <p class="lede">…</p>
      <section aria-labelledby="weekend"><h2 id="weekend">Weekend</h2>…</section>
    </article>
    <aside aria-label="Related">…</aside>
  </main>
  <footer><address>…</address></footer>
  <script src="/js/nav.js" type="module"></script>   <!-- behavior last, optional -->
</body>
</html>
```

Rules embodied above: one `h1`; headings in order; landmarks (`header`, `nav`, `main`,
`aside`, `footer`) labelled when repeated; `<button>` for actions, `<a href>` for
navigation; lists for lists, `<time datetime>` for dates, `<address>` for contact; no
`div`-only interfaces; presentation only in CSS; behavior loaded last and non-blocking.

Readable typography defaults ("Zeldman look" + iA macro-typography):

```css
:root {
  --measure: 65ch;                 /* 45–75 characters per line */
  --leading: 1.5;
  --step-0: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem);   /* 17–20px body */
  --step-1: clamp(1.25rem, 1.1rem + 0.8vw, 1.6rem);
  --step-2: clamp(1.6rem, 1.3rem + 1.6vw, 2.4rem);
  --step-3: clamp(2rem, 1.5rem + 2.8vw, 3.5rem);
  --ink: #1d1d1b; --paper: #fffdf8; --accent: #a23b1e;
}
html { font-size: 100%; -webkit-text-size-adjust: 100%; }
body {
  font-family: Georgia, "Iowan Old Style", "Source Serif 4", serif;
  font-size: var(--step-0); line-height: var(--leading);
  color: var(--ink); background: var(--paper);
  text-rendering: optimizeLegibility; font-kerning: normal;
}
h1, h2, h3 { line-height: 1.15; text-wrap: balance; letter-spacing: -0.01em; }
h1 { font-size: var(--step-3); } h2 { font-size: var(--step-2); } h3 { font-size: var(--step-1); }
p, li, blockquote, figcaption { max-inline-size: var(--measure); text-wrap: pretty; }
.prose > * + * { margin-block-start: 1em; }      /* rhythm by exception */
a { color: var(--accent); text-underline-offset: 0.15em; text-decoration-thickness: 1px; }
```

Limited palette with one accent and guaranteed contrast:

```css
:root {
  color-scheme: light dark;
  --ink: light-dark(#1d1d1b, #ece9e2);
  --paper: light-dark(#fffdf8, #15140f);
  --muted: light-dark(#5b5955, #b3afa6);   /* still ≥ 4.5:1 on paper */
  --accent: light-dark(#a23b1e, #e07a55);
}
```

Progressive enhancement in the Zeldman sense (content for everyone, design for capable
browsers) using feature queries rather than browser sniffing:

```css
.gallery { display: flex; flex-wrap: wrap; gap: 1rem; }      /* baseline */
@supports (grid-template-rows: subgrid) {
  .gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr)); }
  .gallery > figure { display: grid; grid-row: span 2; grid-template-rows: subgrid; }
}
```

Rules of thumb:
- Write the content and headings before any layout; wireframe with real text.
- If removing the stylesheet makes the page nonsensical, the markup is wrong.
- Body type 17–20px on desktop, line-height ~1.5, measure 45–75ch, one column for prose.
- One accent colour; muted text still passes 4.5:1; links underlined in body copy.
- Personality lives in type choice, voice and a single colour, not in chrome.

---

## 3. Chris Coyier: pragmatic CSS, platform-first, playful craft

### 3a. Core principles

**HTML, CSS, accessibility and UX are a discipline, not a warm-up for JavaScript.** "The
Great Divide" (Jan 2019) names the split between JS-centric and "HTML, CSS, design,
interaction, patterns, accessibility" front-enders and insists neither side is lesser:
"Even if there is a divide, that doesn't absolve any of us from doing a good job." "Nobody
is allowed to do a bad job." Heavy toolchains are for big sites: "Sometimes it feels like
releasing cougars into the forest to handle your snake problem."
Source: https://css-tricks.com/the-great-divide/

**Choose technology by need, not by label.** On "website vs web app": "There are a lot of
technological choices to make, but they can be made based on actual needs, not because a
site happens to fall into a lexical bucket." Content sites output HTML whatever builds them.
Source: https://chriscoyier.net/2022/10/12/stanford-website-experiment/ (2022)

**Progressive enhancement, in practice since 2008.** Start with semantic markup that works
without JavaScript ("We'll take advantage of definition lists"), style it, then let JS
enhance: "we should take care to do our hiding with JavaScript, so that when JavaScript
is off, the answers are not hidden."
Source: https://css-tricks.com/dynamic-faq-page/ (Dec 2008)

**Don't invent what the platform gives you.** Use real attributes and hooks: "If JavaScript
needs to discover this element, use an data-js attribute. Just don't make up attributes."
(The spirit of "don't fight the browser": defer to native elements, native focus, native
scrolling, native form controls; this is a theme across CSS-Tricks rather than a single
essay.)
Source: https://chriscoyier.net/2023/01/19/html-attributes-for-very-specific-third-party-reasons/

**Flexbox for one-dimensional components; Grid for two-dimensional layout.** "Flexbox
layout is most appropriate to the components of an application, and small-scale layouts,
while the CSS Grid layout is intended for larger scale layouts." Practical rules from the
guide: use the `flex` shorthand (default `0 1 auto`; `flex: 1` means `1 1 0%`), use `gap`
rather than margins, `flex-wrap: wrap` for multi-line, `margin: auto` to centre a child,
and remember `order` changes only visual order, which "is bad for accessibility."
Source: https://css-tricks.com/snippets/css/a-guide-to-flexbox/ (Coyier)

**Grid vocabulary that removes breakpoints.** `fr` means "portion of the remaining space";
`auto-fit` fits "whatever columns there are into the space" while `auto-fill` keeps empty
tracks; `grid-template-areas` gives "a visualization of the structure of the grid";
`dense` reorders visually and is "bad for accessibility." The canonical fluid snippet:
`grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));`
Source: https://css-tricks.com/snippets/css/complete-guide-grid/ (Chris House, maintained by CSS-Tricks)

**Fluid typography with `clamp()`.** "Fluid typography is the idea that font-size (and
perhaps other attributes of type, like line-height) change depending on the screen size."
Pure viewport units swing too far; clamp a minimum and maximum, and mix `rem` into the
preferred value so user zoom still works: `font-size: clamp(100%, 1.5rem + 2vw, 24px);`
Source: https://css-tricks.com/simplified-fluid-typography/ (Coyier, Nov 2019)

**Custom properties are the design-token layer.** Define on `:root`, override in
components and media queries because "the fact that custom properties use the cascade is
one of the most useful things about them"; use fallbacks `var(--x, 1.2)`; wrap maths in
`calc()`; split colours into channels for theming; don't over-abstract.
Source: https://css-tricks.com/a-complete-guide-to-custom-properties/ (Coyier with Miriam Suzanne)

**Respect `prefers-reduced-motion`.** Eric Bailey's CSS-Tricks article: motion can
trigger vestibular disorders; parallax, zooming and large movement are the worst
offenders; animation "when used with discretion and restraint" communicates relationships
and state. "Remember: we're all just temporarily-abled."
Source: https://css-tricks.com/introduction-reduced-motion-media-query/ (Eric Bailey, 2017)

**Animate `transform` and `opacity`; avoid layout properties.** "The GPU is highly
optimized for tasks like moving pixels around and applying transform matrices and
opacity," while `top/left/width/height` trigger layout and paint, which "eat up the most
processing resources (by FAR)."
Source: https://css-tricks.com/myth-busting-css-animations-vs-javascript/ (Jack Doyle, 2014)

**Easing: ease-out to enter, ease-in to exit, never linear for UI.** Linear motion "tends
to feel unnatural or even robotic"; ease-out starts fast and settles, ease-in accelerates
away. "The purpose of an easing function is to get non-linear values from linear value
inputs."
Source: https://css-tricks.com/ease-y-breezy-a-primer-on-easing-functions/ (Pavithra Kodmad, 2018)

**Never remove focus without replacing it; use `:focus-visible`.** The almanac warns that
`outline: none` on `:focus` means keyboard users "can't see where they've tabbed," and
`:focus-visible` "only applies when you actually want a visual indicator." Standardise the
ring with custom properties: `:is(a, button, input, textarea, summary):focus-visible { outline: … }`.
Sources: https://css-tricks.com/almanac/pseudo-selectors/f/focus-visible/ ;
https://css-tricks.com/standardizing-focus-styles-with-css-custom-properties/

**Container queries make components predictable and reusable.** They "allow us to define
all of the styles for a particular element in a more predictable way" and "are more
reusable than media queries in that they behave the same no matter where they are used."
Syntax: `container-type: inline-size; container-name: x; @container x (width > 60ch) {…}`;
`cqi` = 1% of the container's inline size.
Source: https://css-tricks.com/css-container-queries/ (Geoff Graham, 2024)

**Scroll-driven animations: progressive enhancement, reduced-motion aware.** "A
scroll-driven animation is an animation that responds to scrolling." Gate with
`@supports (animation-timeline: scroll())`, and "remember to use prefers-reduced-motion."
Source: https://css-tricks.com/unleash-the-power-of-scroll-driven-animations/ (Geoff Graham, 2024)

**Design systems are for people.** This is Jina Anne's line (2017 talk, Design Systems
Coalition), widely echoed on CSS-Tricks and ShopTalk; Coyier's own version is "Thoughts
on a Global Design System" (2024). The practical reading: a system exists to help the
humans who use and maintain it, so prefer fewer, clearer tokens over exhaustive ones.
Sources: https://publication.design.systems/distinct-design-systems-3c1ec8e69e5b ;
https://chriscoyier.net/2024/02/05/thoughts-on-a-global-design-system/

**The CodePen aesthetic (synthesis).** Coyier's demos and CSS-Tricks itself favour bold,
saturated accent colours on neutral grounds, chunky rounded buttons, visible hover and
focus states, one playful flourish per page, and copy written in a friendly first person.
The work is pragmatic first: a demo must function before it delights. (Observation of the
properties and demos read, not a quoted doctrine.)

### 3b. Memorable quotes

- "Even if there is a divide, that doesn't absolve any of us from doing a good job." (The Great Divide, 2019)
- "Nobody is allowed to do a bad job." (The Great Divide)
- "Sometimes it feels like releasing cougars into the forest to handle your snake problem." (The Great Divide)
- "There are a lot of technological choices to make, but they can be made based on actual needs." (2022)
- "Just don't make up attributes, that always makes me cringe." (2023)
- "Fluid typography is the idea that font-size … change[s] depending on the screen size." (2019)
- "The fact that custom properties use the cascade is one of the most useful things about them." (Custom Properties guide)
- Bailey: "Remember: we're all just temporarily-abled." (CSS-Tricks, 2017)
- Doyle: "The GPU is highly optimized for tasks like moving pixels around and applying transform matrices and opacity." (CSS-Tricks, 2014)
- Graham: "They are more reusable than media queries in that they behave the same no matter where they are used." (container queries, 2024)

### 3c. How to apply it in code

Fluid type and space scale with `clamp()` (rem in the preferred term keeps zoom working):

```css
:root {
  --step--1: clamp(0.875rem, 0.84rem + 0.2vw, 1rem);
  --step-0:  clamp(1rem, 0.95rem + 0.35vw, 1.25rem);
  --step-1:  clamp(1.25rem, 1.15rem + 0.6vw, 1.6rem);
  --step-2:  clamp(1.56rem, 1.35rem + 1.1vw, 2.2rem);
  --step-3:  clamp(1.95rem, 1.55rem + 2vw, 3rem);
  --space-s: clamp(0.75rem, 0.65rem + 0.5vw, 1rem);
  --space-m: clamp(1.25rem, 1rem + 1vw, 2rem);
  --space-l: clamp(2rem, 1.5rem + 2.5vw, 4rem);
  --space-xl: clamp(3rem, 2rem + 5vw, 7rem);
}
```

Tokens → components → exceptions (custom-property architecture):

```css
:root { --radius: 0.5rem; --ring: 3px; --ring-color: var(--accent); }
.button {
  --_bg: var(--button-bg, var(--accent));
  --_fg: var(--button-fg, white);
  background: var(--_bg); color: var(--_fg);
  padding: 0.6em 1.1em; border-radius: var(--radius); border: 0;
  font: inherit; cursor: pointer;
  transition: transform 150ms ease-out, background-color 150ms ease-out;
}
.button:hover { transform: translateY(-1px); }
.button:active { transform: translateY(0); }
.button.is-quiet { --button-bg: transparent; --button-fg: var(--accent); }
```

Transitions: transform/opacity only, short durations, asymmetric easing:

```css
:root {
  --dur-fast: 150ms;   /* hover, press, toggles */
  --dur-base: 250ms;   /* reveal, menus, cards */
  --dur-slow: 450ms;   /* page-level, large surfaces */
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);   /* entering: fast start, soft landing */
  --ease-in:  cubic-bezier(0.55, 0, 1, 0.45);   /* exiting: accelerate away */
  --ease-inout: cubic-bezier(0.65, 0, 0.35, 1); /* moving between on-screen states */
}
.menu { opacity: 0; transform: translateY(-0.5rem); pointer-events: none;
        transition: opacity var(--dur-base) var(--ease-out),
                    transform var(--dur-base) var(--ease-out); }
.menu[data-open] { opacity: 1; transform: none; pointer-events: auto; }
/* Never: transition: all; never animate height, top, left, width, margin */
```

Reduced motion, applied globally and then re-enabled selectively:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
/* Prefer opt-in motion: */
@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
  .reveal { animation: fade-up var(--dur-slow) var(--ease-out) both; }
}
@keyframes fade-up { from { opacity: 0; transform: translateY(1rem); } }
```

Scroll-driven animation as an enhancement:

```css
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .reveal {
      animation: fade-up linear both;
      animation-timeline: view();
      animation-range: entry 0% entry 40%;
    }
  }
}
```

Focus styles that are never removed:

```css
:root { --outline-size: max(2px, 0.125em); --outline-color: var(--accent); }
:focus { outline: var(--outline-size) solid var(--outline-color); outline-offset: 2px; }
:focus:not(:focus-visible) { outline: none; }          /* mouse users */
:focus-visible { outline: var(--outline-size) solid var(--outline-color); outline-offset: 2px; }
```

Logical properties so the layout survives RTL and vertical writing modes:

```css
.card { padding-block: var(--space-m); padding-inline: var(--space-s);
        margin-inline: auto; max-inline-size: var(--measure);
        border-inline-start: 4px solid var(--accent); }
```

Progressive enhancement for interactive components (platform first):

```html
<details class="faq">
  <summary>What time is Sunday Mass?</summary>
  <p>8:00, 10:00 and 12:00 noon.</p>
</details>
```

```css
.faq summary { cursor: pointer; }
.faq::details-content { /* animate open state where supported */
  opacity: 0; transition: opacity var(--dur-base) var(--ease-out), content-visibility var(--dur-base) allow-discrete;
}
.faq[open]::details-content { opacity: 1; }
```

Rules of thumb:
- Flexbox for rows of things; Grid for the page and for any two-axis alignment.
- `gap`, not margins, for spacing between siblings.
- `clamp()` for type and space; a breakpoint is a last resort.
- Animate `transform` and `opacity` only; 150–250ms for micro-interactions, under 500ms
  for anything larger; ease-out in, ease-in out; wrap every non-essential motion in
  `prefers-reduced-motion: no-preference`.
- Use `<details>`, `<dialog>`, `<button>`, native inputs before writing JS.
- Tokens on `:root`, component-scoped overrides, no magic numbers inline.

---

## 4. Craft checklist

Answer yes to each before shipping. Items are phrased so "no" is actionable.

### HTML semantics and structure
1. Does the page read correctly with CSS and JavaScript disabled? (Zeldman)
2. Is there exactly one `h1`, with headings in strict outline order below it? (Marcotte's statement)
3. Are `header`, `nav`, `main`, `aside`, `footer` used as landmarks, with `aria-label` where a landmark repeats?
4. Is there a skip link as the first focusable element?
5. Are actions `<button>` and navigation `<a href>`, never `div onclick`?
6. Are lists, tables, `<time>`, `<address>`, `<figure>`/`<figcaption>`, `<details>` used where the content is that thing?
7. Does every image have meaningful `alt` (or `alt=""` when decorative) and intrinsic `width`/`height`?
8. Are form fields labelled with `<label for>` and errors associated via `aria-describedby`?
9. Is `lang` set on `<html>` and the viewport meta present without `user-scalable=no`?

### Responsive and intrinsic layout
10. Is the layout fluid by default, with no fixed pixel widths on containers? (Marcotte)
11. Are breakpoints set where the content breaks, in `em`/`rem`, `min-width` first?
12. Could any breakpoint be replaced by `repeat(auto-fit, minmax())`, `flex-wrap`, or `clamp()`? If so, was it?
13. Do components that appear in several contexts use container queries rather than viewport queries?
14. Does the small-screen source order match the content's priority (content choreography)?
15. Does navigation keep the most important links visible at every size, built from a plain list?
16. Do images and embeds scale (`max-inline-size: 100%`, `aspect-ratio`) and serve responsive sources (`srcset`/`<picture>`)?
17. Does the page hold up at 320px wide, at 300% zoom, and at 2560px wide?
18. Are logical properties (`inline`/`block`) used instead of left/right/top/bottom for spacing and sizing?

### Typography and readability
19. Is body text at least 17–18px-equivalent on desktop with line-height around 1.5? (Zeldman)
20. Is prose measure capped between 45 and 75 characters (`max-inline-size: 65ch`)?
21. Is the type scale fluid via `clamp()` with `rem` in the preferred value so zoom works?
22. Is hierarchy carried by size, weight and space, using at most two type families?
23. Is vertical rhythm handled by a single spacing scale (`* + *`), not ad hoc margins?
24. Are headings balanced (`text-wrap: balance`) and paragraphs free of orphans where supported (`text-wrap: pretty`)?
25. Are links in body copy visibly distinguishable without relying on colour alone?

### Color and contrast
26. Does every text/background pair meet 4.5:1 (3:1 for large text) including muted and placeholder text?
27. Is the palette limited: neutrals plus one accent, with the accent reserved for action and emphasis?
28. Do focus rings and UI borders meet 3:1 against adjacent colours?
29. Is `color-scheme` declared and is a dark variant either designed or explicitly declined?
30. Is no meaning conveyed by colour alone (status, errors, required fields)?

### Motion and transitions
31. Are only `transform` and `opacity` animated (no `height`, `top`, `margin`, `box-shadow` on large surfaces)?
32. Are durations 150–250ms for micro-interactions and under ~500ms for larger moves?
33. Is easing asymmetric: ease-out on enter, ease-in on exit, never `linear` for UI motion?
34. Is every non-essential animation wrapped in `prefers-reduced-motion: no-preference` (or neutralised under `reduce`)?
35. Are scroll-driven or view-timeline effects behind `@supports` and reduced-motion checks?
36. Does no element auto-animate for more than 5 seconds without a pause control, and is parallax avoided or opt-in?

### Performance
37. Are images sized, lazy-loaded below the fold (`loading="lazy"`), and in modern formats?
38. Are fonts subset and loaded with `font-display: swap` (or `optional`), with a system fallback that matches metrics?
39. Is CSS small, single-file or layered, and free of unused frameworks?
40. Is JavaScript deferred or `type="module"`, non-blocking, and absent where HTML/CSS suffices?
41. Does layout not shift as fonts and images load (reserved space, `aspect-ratio`)?
42. Does the page work on a slow connection as a readable document before enhancements arrive? ("culture of performance")

### Progressive enhancement
43. Is the baseline experience HTML + CSS only, with JS adding behaviour on top?
44. Are new CSS features gated with `@supports` and given a sensible fallback?
45. Are native elements (`details`, `dialog`, `select`, `input type=date`) used before custom widgets?
46. Are JS hooks separate from styling hooks (`data-js`, not class names or invented attributes)?
47. If JS fails, is nothing hidden that should be visible, and nothing broken that worked before?

### CSS architecture
48. Are design tokens defined once on `:root` as custom properties and consumed everywhere else?
49. Are component overrides expressed as token overrides (`--button-bg`) rather than new selectors?
50. Is specificity flat (single-class selectors, `:is()`/`:where()`, optionally `@layer`) with no `!important` outside the reduced-motion reset?
51. Is `gap` used for sibling spacing and are magic numbers absent from component CSS?
52. Is the CSS organised so a newcomer can find tokens, base, layout primitives, components and utilities in that order? ("Design systems are for people.")

---

## Sources actually read (primary unless noted)

Marcotte
- https://alistapart.com/article/responsive-web-design/
- https://alistapart.com/article/fluidgrids/
- https://ethanmarcotte.com/books/responsive-web-design/full/chap04/
- https://ethanmarcotte.com/books/responsive-web-design/full/chap05/
- https://ethanmarcotte.com/books/responsive-design-patterns-and-principles/
- https://ethanmarcotte.com/books/responsive-design-patterns-and-principles/full/chap01/
- https://ethanmarcotte.com/books/responsive-design-patterns-and-principles/full/chap02/
- https://ethanmarcotte.com/wrote/responsive-design-at-11-container-queries/
- https://ethanmarcotte.com/wrote/responsive-design-at-15/
- https://ethanmarcotte.com/wrote/responsive-design-workshop/
- https://ethanmarcotte.com/wrote/accessibility-is-not-a-feature/
- https://ethanmarcotte.com/accessibility/
- https://trentwalton.com/2011/07/14/content-choreography/
- https://zeldman.com/2018/05/02/transcript-intrinsic-web-design-with-jen-simmons-the-big-web-show/
- https://every-layout.dev/rudiments/axioms/
- https://buildexcellentwebsit.es/

Zeldman
- https://alistapart.com/article/tohell/
- https://alistapart.com/article/understandingwebdesign/
- https://zeldman.com/2005/12/15/style-vs-design/
- https://zeldman.com/2008/05/06/content-precedes-design/
- https://zeldman.com/2012/05/18/web-design-manifesto-2012/
- https://zeldman.com/2017/02/06/readable-branded-design/
- https://books.google.com/books/about/Designing_with_Web_Standards.html?id=wUGTSdey6TwC (publisher page: chapter list)
- https://ia.net/topics/the-web-is-all-about-typography-period

Coyier / CSS-Tricks
- https://css-tricks.com/the-great-divide/
- https://css-tricks.com/snippets/css/a-guide-to-flexbox/
- https://css-tricks.com/snippets/css/complete-guide-grid/
- https://css-tricks.com/simplified-fluid-typography/
- https://css-tricks.com/a-complete-guide-to-custom-properties/
- https://css-tricks.com/introduction-reduced-motion-media-query/ (Eric Bailey)
- https://css-tricks.com/myth-busting-css-animations-vs-javascript/ (Jack Doyle)
- https://css-tricks.com/ease-y-breezy-a-primer-on-easing-functions/ (Pavithra Kodmad)
- https://css-tricks.com/almanac/pseudo-selectors/f/focus-visible/
- https://css-tricks.com/standardizing-focus-styles-with-css-custom-properties/ (search excerpt)
- https://css-tricks.com/css-container-queries/ (Geoff Graham)
- https://css-tricks.com/unleash-the-power-of-scroll-driven-animations/ (Geoff Graham)
- https://css-tricks.com/dynamic-faq-page/
- https://css-tricks.com/almanac/properties/t/transition/
- https://chriscoyier.net/2022/10/12/stanford-website-experiment/
- https://chriscoyier.net/2023/01/19/html-attributes-for-very-specific-third-party-reasons/ (search excerpt)
- https://chriscoyier.net/2024/02/05/thoughts-on-a-global-design-system/ (search excerpt)

Not located / caveats
- A Zeldman essay titled "Where's the content?" was not found; "Content precedes design" (2008) is used instead.
- abookapart.com product pages for Marcotte's books returned 404; the full text on ethanmarcotte.com was used.
- Transition duration ranges (150–500ms) are practical convention, not a quoted CSS-Tricks rule.
- "Design systems are for people" is Jina Anne's phrase, not Coyier's.
