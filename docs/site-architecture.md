# St. Matthias Parish Website: Architecture and Maintenance

Updated: 2026-11-04
Status: development preview at https://stmatthiaswebsite.vercel.app/ (not the parish domain; not deployed from this revision).
Replaces the September 2026 homepage concept notes (see git history for `docs/homepage-redesign.md`).
Open questions and unconfirmed facts: `docs/needs-parish-confirmation.md`.

---

## 1. Site map

| Route | Purpose | Sections (anchor ids) |
|---|---|---|
| `/` | Homepage | Hero (featured events + Support card) · `#mission` · `#join-us` · `#upcoming` · `#support` |
| `/about-us/` | Who we are | `#mission` Our Parish & Mission · `#staff-leadership` Staff & Leadership (clergy, staff, Pastoral and Finance Councils) · `#faq` New Here? FAQ · `#contact` Contact & Nonprofit Information |
| `/sacraments/` | All seven sacraments on one page | `#baptism` · `#reconciliation` · `#first-communion` · `#confirmation` · `#marriage` · `#anointing-of-the-sick` · `#holy-orders` |
| `/faith-formation/` | Learning at every age | `#children-families` (GIFT, Promise, safe environment) · `#youth` · `#adults` · `#becoming-catholic` |
| `/ministries/` | Ways to serve | `#worship` · `#service` · `#welcome` · `#care` · `#parish-support` |
| `/events/` | Current and future public events only | One `<article id="event-id">` per event, then recurring gatherings |
| `/support-us/` | Giving | Hero with jump links · `#start` (featured gifts as large cards) · `#ways` (every other active option, grouped: `#give-parish`, `#give-worship`, `#give-neighbors`) · `#questions` (trust facts, FAQ, office contact) · closing "Give your time, too" band. Every option card has its own anchor (`#regular-collection`, `#flower-offering`, …) and is highlighted when targeted. |
| `/privacy/` | Privacy Policy | Linked from the footer |
| Preschool | External only | https://stmatthiaspreschool.org/ (no parish-hosted page) |

Every sacrament section answers the same five questions: what it is, who it is for, how preparation works, the next step, and the contact. Sections are always expanded (no accordion), so all content is in the HTML and works without JavaScript.

Not migrated: Shaping Our Future, parish history, bulletin archive, St. Charles information, old schedules and handouts, past events, and the separate ministry category pages.

## 2. Navigation

Desktop (1200 px and wider): logo (Home) · About Us ▾ · Sacraments ▾ · Faith Formation ▾ · Ministries ▾ · Events · Support Us ▾ (a plain link like the others) · **Preschool** (last; the only boxed item, an outline-only button).

- Each dropdown is a disclosure: the label is a normal link to the page, and the chevron is a `<button aria-expanded aria-controls>`. Clicking or tapping the chevron toggles the menu; mouse hover opens it on devices with a fine pointer; ArrowDown opens it and focuses the first link; ArrowUp and ArrowDown move through links; Escape closes it and returns focus to the chevron; moving focus away closes it. Without JavaScript, menus open on hover and focus via CSS.
- Below 1200 px a full-screen drawer replaces the bar. It has the same items in the same order, and each dropdown becomes an expandable sub-list (`aria-expanded`). Focus is trapped while it is open, and Escape, the close button, or the scrim closes it.
- The header and drawer are both generated from `data/site.json → nav`, so they cannot drift apart. The Support Us sub-items list every active entry in `data/giving.json` and link to that gift's card on `/support-us/`, so visitors stay on the parish site. Give buttons open Vanco in the same tab (Back returns to the site); no giving link opens a new tab. Links carry no decorative arrows.
- The breakpoint moved from 1024 px to 1200 px because the seven labels plus the logo do not fit at 1024 px.

## 3. Homepage (layout, order, and motion unchanged)

1. **Hero carousel** shows up to three featured events (`featured: true`). Each slide has a category overline, title, date and time, location, a one-sentence description, and a "View Event" button that links to `/events/#id`. A translucent **Support St. Matthias** card sits at the right on screens 1024 px and wider. Its right edge is set clear of the next arrow, it sits above the slide counter and progress bar, and event copy is narrowed so it never runs under the card. Below 1024 px the card sits directly under the carousel. On phones the arrows move to the bottom-right corner so they never cover event text.
2. **A life shared in Christ** shows the parish mission statement (word-by-word light-up kept), supporting copy, and links to About Us, Faith Formation, and Ministries.
3. **Join us this Sunday** shows Saturday 5:00 p.m. and Sunday 9:45 a.m., the address with directions, Watch Mass Online, Register with the Parish, and a "New here?" link to `/about-us/#faq`.
4. **Upcoming at St. Matthias** ("Come together in faith and community.") shows the next five non-featured events in the original five-card layout. With fewer events it shows fewer cards; the grid adapts, and spare flight tiles stay hidden.
5. **Support St. Matthias** ("Help our parish worship, form, serve, and welcome.") turns the stacked-poster fan into giving cards from `data/giving.json`. The fan spreads to however many options are active (two today), and the section button links to `/support-us/`.
6. **Footer** has four groups: Contact, Mass, Explore, and Take Action. Below them: copyright, an empty legal-identity slot (filled from `data/site.json → legal`), and verified social links.

The hero headline animation, crossfades, scroll-linked mission and flight motion, poster fan, and reduced-motion fallbacks all keep the original code paths (`js/motion.js`). The only motion changes adapt them to placeholders and variable card counts.

## 4. One source for each kind of content

| Content | Edit here | Rendered into |
|---|---|---|
| Parish facts, Mass times, navigation, footer, legal identity | `data/site.json` | Header and drawer (all pages), footer (all pages), About Us legal rows |
| Events | `data/events.json` | Homepage hero, homepage Upcoming cards, `/events/` |
| Giving options | `data/giving.json` | Homepage giving fan, `/support-us/`, Support Us menu |

`scripts/build.py` (Python 3, standard library only) replaces the regions between `<!-- build:NAME -->` and `<!-- /build:NAME -->` in each page. Never hand-edit inside those markers.

```bash
python3 scripts/build.py           # regenerate pages
python3 scripts/build.py --check   # fail if any page is out of date
```

Build rules:
- Only events with `"status": "verified"` are published. The build stops if any other status is present, so placeholder events can never go live.
- Events whose last session has ended are dropped at build time. `js/events.js` also removes them in the browser and promotes the next event, so a past event never shows even if nobody has rebuilt.
- Only giving options with `"active": true` and an `https://` URL are published, and the Regular Collection must be the active primary option.
- Legal name, EIN, nonprofit status, and office hours stay hidden until they are set (null means not shown).

### Common updates

- **Add an event:** copy an entry in `data/events.json`, give it a unique `id`, set `sessions` with Pacific offsets (`-08:00` in winter, `-07:00` in summer), set `featured: true` for up to three hero events, then rebuild.
- **Activate the Annual Appeal:** set `"active": true` in `data/giving.json` after confirming the wording, then rebuild. The homepage, Support Us page, and menu all update.
- **Publish the legal name and EIN:** fill `legal` in `data/site.json`, then rebuild.

## 5. Placeholders

Every non-logo image slot carries the `media-ph` class and a `data-image-slot="…"` name. An empty slot is a `<div>` in a token color (terracotta, sage, slate, sand, taupe, navy, moss, clay) with `aria-hidden="true"`. A filled slot is a decorative `<img alt="">` with the same classes, so it keeps the box's size and shows the color while loading (`img.media-ph` uses `object-fit: cover`). The slots and the photos they need are listed in `docs/needs-parish-confirmation.md`, section F.

The homepage is filled with AI-generated stand-in photos (2026-11-05) from `images/GeminiGeneratedImages/web/`; that folder's README maps each file to its slot. `scripts/build.py` fills the generated regions automatically through `photo()`. The hero uses `hero-<event id>-1200/2400.webp`, an Upcoming card uses `event-<event id>-960.webp`, a giving poster uses `<imageSlot>-800.webp`, and a slot with no matching file falls back to its placeholder. The Support Us card, mission tiles, and flight tiles are fixed `<img>` tags in `index.html`.

The inner pages use the same set. `photo()` also fills the Events-page event rows and the Support Us giving cards. Page heroes (`<slot>-960.webp`, 4:5) and section photos (`<slot>-1200.webp`, 4:3) are fixed `<img>` tags in each page. Staff portraits are real headshots in `images/staff/staff-<name>.jpg` (256 px squares, shown as circles). Still placeholders: `staff-deacon-david-rolandelli`, `staff-carmen-perlas`, and `ministry-worship`, `ministry-care` and `ministry-parish-support`.

## 6. Preview locally

```bash
node .claude/serve.js 8787
```

If Node is not installed, from the project folder:

```bash
python3 -m http.server 8787
```

Then open http://localhost:8787/. Every route is a folder with an `index.html`, so both servers resolve `/about-us/` and the other routes.

## 7. Accessibility and technical notes

- One `<h1>` per page (visually hidden on the homepage, because the hero is now an events carousel), landmarks, a skip link, and `aria-labelledby` on sections.
- Dropdowns and drawer: see section 2. The carousel controls have labels, inactive slides are `aria-hidden`, and the Support card is a normal link in tab order.
- External links open in a new tab with `rel="noopener"` and a visually hidden "(opens in a new tab)".
- `prefers-reduced-motion` keeps the existing static fallbacks, and the new dropdown and drawer transitions are disabled under it too.
- No framework and no new dependencies. Fonts load from Google Fonts. No analytics, cookies, ads, or affiliate links.
- `[hidden]` is forced to `display: none` so data-driven cards held in reserve stay hidden.

## 8. Content decisions

- **No St. Charles information anywhere:** shared-pastor notes, St. Charles Mass and confession times, the St. Charles link, and youth-meeting locations at St. Charles were all removed. Staff bios mention only St. Matthias.
- **No bulletins,** bulletin archive, or "coming soon" links. The old coming-soon interception script is gone, because every route now exists.
- **Plain-language labels:** "Becoming Catholic" (Order of Christian Initiation of Adults, formerly RCIA), "First Communion & Eucharist," and "Support Us." GIFT (Generations in Faith Together) and other acronyms are spelled out on first use.
- **Dated content removed:** pandemic language, anniversaries, past Bible-study archives and handouts, past book clubs, and old program start dates.
- **Fees and amounts** from the old pages are not published, pending confirmation.

## 9. Google for Nonprofits website policy review (2026-11-04)

Reviewed against https://support.google.com/nonprofits/answer/1657899.

| Requirement | Status |
|---|---|
| Domain ownership; no redirects | **Pending.** Must use the parish-owned domain (A3). The Vercel URL is a preview only. No redirects are configured. |
| Substantial, unique content | Met in draft. About Us, Sacraments, Faith Formation, and Ministries are full HTML pages with original, edited text. No PDFs are relied on and no page is "under construction." |
| Clear mission and activities | Met on the homepage (mission is the second section) and About Us. Physical address is in the footer and About Us. **EIN or tax ID still pending** (A1, A2). |
| Navigation and working links | Met. An automated audit found 0 broken internal links or anchors; all 11 external destinations, including both donation links, returned working pages. No empty pages or placeholder social icons. |
| Fast loading | Likely met (static HTML, small CSS and JS, no images yet). **Re-test with PageSpeed Insights after real photos are added.** |
| Mobile-friendly | Met. Tested at 375, 1024, 1200, and 1440 px wide with no horizontal scrolling. |
| HTTPS | Every link and asset uses HTTPS; Vercel serves HTTPS. Confirm on the custom domain. |
| Commercial activity, ads, affiliates | Met. No ads, AdSense, affiliate links, or store. Donation links go to the parish's dedicated secure Vanco pages. |
| Placeholder content | **Pending.** Colored image placeholders must be replaced before review (A4). |

## 10. Files

- Pages: `index.html`, `about-us/`, `sacraments/`, `faith-formation/`, `ministries/`, `events/`, `support-us/`, `privacy/` (each an `index.html`)
- Styles: `css/tokens.css` (unchanged) and `css/site.css` (navigation, placeholders, Support card, and secondary-page styles added)
- Scripts: `js/nav.js` (header, dropdowns, drawer), `js/motion.js` (existing motion, adapted), `js/events.js` (expiry of past events)
- Data and tooling: `data/*.json`, `scripts/build.py`
- Deployment: `.vercelignore` keeps `docs/`, `data/`, `scripts/`, `.claude/`, and `videos/` off the public site
