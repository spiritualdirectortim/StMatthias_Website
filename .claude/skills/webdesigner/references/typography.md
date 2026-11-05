# Typography

Zeldman: "the easiest, fastest path to authoritative, branded design is through
typography." iA's framing: web design is 95% typography because text is the interface.
Get this layer right before color or motion, and most of the "premium" feeling arrives on
its own.

## 1. Pairing models (choose one)

| Model | Seen at | Why it works | Watch out |
|---|---|---|---|
| One family, three or four weights | Elevation (DM Sans 400/500/700), Austin Stone (Proxima Nova), Anchor (Metropolis 400 to 700), River Valley (Realist) | Hierarchy from size, weight and case; one font request; always coherent | Can feel corporate; needs strong photography or scale contrast |
| Display + body | Church of the City (Inter Display + Inter); this repository (serif display, sans body) | Display face gives personality in headlines and pull quotes; body stays neutral | Keep the display face out of body copy and buttons |
| Display + body + mono or small-caps for metadata | VOUS (Inter Tight, Inter, Spline Sans Mono) | Dates, times, addresses, eyebrows and buttons in a third voice feel designed | Three families cost load time; mono must still pass contrast at 12 to 14px |

For a parish or nonprofit, display + body is the sweet spot: a serif or humanist display
for warmth and tradition, a clean sans for wayfinding.

## 2. Scale

Two approaches, both valid:

**Fixed steps** (VOUS: 12 / 14 / 16 / 20 / 22 / 24 / 28 / 36 / 48 / 64 / 80; COTC: 14 / 16 /
22 / 28 / 40 / 64) with per-breakpoint overrides. Predictable; needs three or four media
queries.

**Fluid steps** with `clamp()`, `rem` in the preferred value so browser zoom still works
(Coyier):

```css
:root {
  --step--1: clamp(.8rem, .78rem + .1vw, .875rem);     /* 12.8 to 14 */
  --step-0:  clamp(1rem, .95rem + .25vw, 1.125rem);    /* 16 to 18 */
  --step-1:  clamp(1.2rem, 1.1rem + .5vw, 1.4rem);
  --step-2:  clamp(1.44rem, 1.25rem + .9vw, 1.9rem);
  --step-3:  clamp(1.8rem, 1.4rem + 1.8vw, 2.6rem);
  --step-4:  clamp(2.2rem, 1.5rem + 3vw, 3.6rem);
  --step-5:  clamp(2.8rem, 1.6rem + 5vw, 5rem);
  --display: clamp(3rem, 1.5rem + 8vw, 7.5rem);
}
```

Anchor's alternative is a fluid root: `html { font-size: calc(.3987rem + .6682vw) }` under
1440px with three more formulas per breakpoint, so every `rem` scales. Elegant, but it
shrinks body text below 16px on small phones; if you use it, clamp body separately.

Minimums that the inspiration sites broke and you should not: body 16px on phones (COTC
shipped 12.8px, Anchor 13px card copy), labels 12px, nothing interactive under 14px.

## 3. Headline rules

- Line-height 1.0 to 1.2 for headings, 1.5 to 1.6 for body, 1.3 to 1.4 for card copy.
- Tracking: slightly negative (-0.01 to -0.02em) above about 40px; none at text sizes;
  positive (0.08 to 0.2em) only on small uppercase labels. Never positive-track large caps.
- Weight inversion (COTC): headings up to 40px at 700, display moments above 48px at 400.
  Big and light reads calm and expensive; big and bold reads loud.
- Case: sentence case for headlines and buttons reads more human; COTC ends statement
  headlines with a period ("Practicing the Way of Jesus."). Uppercase works for labels and
  for one giant wordmark (Anchor), typed in lowercase in the HTML and uppercased in CSS so
  screen readers do not spell it out.
- Measure: `max-width: 65ch` for prose, 20 to 30ch for headlines, 32rem for subtitles.
- Two-tone headline (COTC): `strong` at full ink, the rest at 60% opacity, for a value
  word plus its description.
- Pull quotes and scripture: display family at 56 to 64px, weight 400, line-height 1.1,
  reference row below at 60 to 80% opacity with a small filled dot.

## 4. Label systems

Pick one and use it for every eyebrow, date, time, nav item and button label:

- **Tracked caps** (Austin Stone, River Valley): 12 to 14px, 500 to 700, uppercase,
  letter-spacing .1 to .2em, muted ink or the accent color.
- **Monospace** (VOUS): 12 to 14px, 400 to 500, uppercase, 1px tracking; overlines 12px
  with 4px tracking in the accent.
- **Bordered chips** (COTC): 14px, sentence or caps, `padding: 4px 8px; border: 1px solid
  currentColor; border-radius: 5px`. Keep opacity at 1 (COTC's .25 fails contrast).

Elevation shows the opposite choice: no labels at all, sentence case everywhere, buttons
`normal-case`. It reads as an app rather than a sanctuary; choose it only if that is the
brief.

## 5. Loading and performance

- Self-host `woff2`; subset to Latin if the content allows. Two families, at most four
  weights total. The inspiration sites loaded 18 to 55 files for one or two families.
- `font-display: swap` for body, `optional` for a display face if a flash of fallback is
  worse than losing it on slow connections.
- Provide a metric-compatible fallback with `size-adjust`, `ascent-override` and
  `descent-override` to kill layout shift (Elevation: Arial with `size-adjust: 104.53%` for
  DM Sans). Tools: Fontaine, Capsize, or measure once in DevTools.
- `preload` only the one or two files used above the fold.
- Gate load-time text animations on `document.fonts.ready` with a timeout fallback so
  words do not jump mid-animation.

## 6. Quick type audit

1. Is there exactly one `h1`, and are heading levels in order?
2. Body at least 16px on a 375px phone, line-height 1.5, measure under 75ch?
3. At most two families, at most four weights, all self-hosted?
4. Every uppercase run under 15px with positive tracking; every big headline with none or
   slight negative tracking?
5. Does the display face appear only in headlines, pull quotes and statement bands?
6. Do labels (dates, times, eyebrows, buttons) share one treatment across the site?
7. Does all text pass 4.5:1, including grey metadata and hover colors?
