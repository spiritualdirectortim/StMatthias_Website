# Needs Parish Confirmation

Updated: 2026-11-04
Who should answer: the parish office, Fr. Roy Remo, or the staff member named for each area.
This file is private working documentation. `.vercelignore` keeps `docs/` off the published site.

**Rule for the website:** nothing is invented. Every public fact comes from the current parish website (stmatthiasparish.org), the parish's public Google Calendar feed, or the parish's Vanco giving portal, all checked on 2026-11-04. Anything unconfirmed is **left off the public site** (no `[TODO]` markers, no placeholders in text) and listed here instead. To publish an item once it is confirmed, edit the data file named and run `python3 scripts/build.py`.

---

## A. Required before the Google for Nonprofits / Ad Grants application

| # | Item | Status | How to publish |
|---|---|---|---|
| A1 | **Exact legal nonprofit name** | Unknown. Not shown. | `data/site.json` → `legal.legalName`. Appears in the footer and in About Us → Contact & Nonprofit Information. |
| A2 | **EIN or applicable nonprofit identification** | Unknown. Not shown. U.S. Catholic parishes are often covered by a group exemption through their diocese; confirm with the Archdiocese of San Francisco what identifier the parish should publish and use for Google for Nonprofits validation. | `legal.ein` and/or `legal.nonprofitStatus` in `data/site.json`. |
| A3 | **Parish-owned custom domain** | The Vercel domain (stmatthiaswebsite.vercel.app) is a development preview only. Confirm the domain the parish owns and controls (presumably www.stmatthiasparish.org) and who manages DNS. The application must use that domain, and it must serve the site directly (no automatic redirect to another site, a donation portal, or social media). | Hosting decision; no code change needed. |
| A4 | **Real photography** for every colored placeholder | All non-logo media are solid-color placeholders. See section F. | Replace placeholders before nonprofit review. |
| A5 | **Privacy Policy approval** | `/privacy/` describes only what this website actually does (no forms, cookies, analytics, or ads; fonts from Google Fonts; links to Vanco, Flocknote, YouTube, Google Maps, Facebook, Instagram, preschool site). The parish (and the Archdiocese, if it has a required policy) should review and approve the wording. | Edit `privacy/index.html`; update the "Last updated" date. |
| A6 | **Office hours** | The current site shows two schedules: "Mon, Tues and Thurs 9AM–4PM" (New to St. Matthias, Staff Directory, Parish Leadership) and "Monday–Thursday, 10:00 am–4:00 pm" (several sacrament and ministry pages). Not shown on the new site. | `data/site.json` → `parish.officeHours`. Appears in the footer. |

---

## B. Giving (`data/giving.json`)

Online giving goes through the parish's Vanco portal, which the current parish site embeds on `/online-donations/`. Every link below returned the correct secure (HTTPS) Vanco giving form on 2026-11-04.

| Option | Published? | Notes to confirm |
|---|---|---|
| **Regular Collection** — https://secure.myvanco.com/L-ZAJ1/campaign/C-13RZH | **Yes, primary** | Wording is adapted from Vanco ("primary source of funds for the parish… operational and programming expenses"). Confirm. |
| **St. Matthias Roofing Fund** — https://secure.myvanco.com/L-ZAJ1/campaign/C-16KPV | **Yes**, as the active parish campaign | Live on Vanco. Wording from Vanco: the Parish and Finance Councils anticipate replacing the church's composite roof in the next 3–5 years. No goal, total, or deadline is shown. Confirm the campaign is active; set `active: false` when it ends. |
| **Archdiocesan Annual Appeal** — https://secure.myvanco.com/L-ZAJ1/campaign/C-13RZN | **No** | The Vanco text still says "St. Matthias Church met our goal for 2025." Confirm the current appeal year and wording, then set `active: true`. It then appears on the homepage, on `/support-us/#annual-appeal`, and in the Support Us menu automatically. |
| Building Fund (C-13RZJ), St. Vincent de Paul (C-13RZP) | No | "Other verified ways to give" are published only after parish confirmation. Both are prepared in `giving.json` with `active: false`. |
| Other Vanco items: Mass Stipend, Flower Offering, Holy Days offering, World Mission Sunday, St. Patrick's Seminary, Campaign for Human Development, Preschool funds, "Donate with Stock & Crypto" (The Giving Block) | No | Decide which, if any, belong on the public Support Us page. |
| Faith Formation fees — https://secure.myvanco.com/L-ZAJ1/campaign/C-13RZX | Linked from Faith Formation as "Pay program fees online" | Confirm. Fee amounts from the old pages (GIFT $200/family, First Communion $80, MSYM $120/$60, Confirmation $80/$120) are **not** published. |
| PCI statement | Shown on `/support-us/` | From the current parish site: "Online Donations are secured with the highest level of PCI security standards." Keep, or use Vanco's wording. |
| Giving questions | Parish office phone and email | Confirm who answers giving questions. |
| Checks, mail, in-person, bank transfer, planned giving | Not shown | Offered? If so, provide instructions. |

---

## C. Events (`data/events.json`)

Source: the parish's public Google Calendar feed ("ST. M FACILITIES CALENDAR," the calendar embedded on the current parish site), read on 2026-11-04. Times were converted to Pacific time. Events disappear from the site automatically after they end (at build time, and again in the browser via `js/events.js`).

### Published

| Event | Date and time | Confirm |
|---|---|---|
| Masses of Remembrance (featured) | Sat Nov 7, 5:00 p.m.; Sun Nov 8, 9:45 a.m. (livestreamed) | Description written from Catholic practice for November ("the Church remembers and prays for all who have died"). Confirm wording. |
| Caroling, Cookies & Cocoa (featured) | Sat Dec 12, 2:30–5:00 p.m. | **The calendar gives no location or description.** The site says "St. Matthias Parish." Confirm the location (church, hall, or neighborhood) and any details. |
| Christmas Eve Masses (featured) | Thu Dec 24, 4:00 p.m. and 9:00 p.m. | Calendar entries have no location; the site says St. Matthias Church. Confirm both times. Is there a Christmas Day Mass? |
| Thanksgiving Day Mass | Thu Nov 26, 10:00 a.m. | Location inferred (St. Matthias Church). |
| Solemnity of the Immaculate Conception | Tue Dec 8, 7:00 p.m. | Location inferred. Description calls it a holy day of obligation (true in the U.S. for Dec 8, 2026). |
| Solemnity of Mary, Mother of God | Fri Jan 1, 2027, 10:00 a.m. | Location inferred. |
| Ash Wednesday Masses | Wed Feb 10, 2027, noon and 7:00 p.m. | Location inferred. |
| Welcome Weekend (recurring) | "Second full weekend of each month," after both weekend Masses | From the parish homepage. **The calendar is inconsistent for November 2026:** one Welcome Weekend series excludes Nov 14, a duplicate series includes it, and Donut Sunday is excluded on Nov 8. The site shows only the recurrence, no specific date. Confirm the November and December dates. |
| Rosary for Peace (recurring) | Thursdays, 10:00 a.m., in the church | From the calendar and the Prayer and Worship page. |

### Not published (need details or are not public)

- **Holy Week and Easter 2027:** the calendar shows Palm Sunday (Mar 21, 9:45 a.m.), Holy Thursday (Mar 25, 7:00 p.m.), Stations of the Cross (Good Friday, Mar 26, 6:00 p.m.), and **two conflicting Easter Sunday entries** (an 8:00 a.m. "Sunday Mass" and a 10:30 a.m. "Easter Sunday Mass" carrying a Google Meet link). No Easter Vigil entry. Confirm the full Holy Week schedule.
- **First Communion,** Sun May 2, 2027 (no time; a family celebration).
- **Costigan/Kerns Concert,** Feb 21, 2027 (no time or description).
- **Preschool Christmas Show,** Wed Dec 2, 7:00 p.m., in the church. Public, or for preschool families?
- **"Sunday Mass, Bethlehem AD Angels,"** Dec 13. Meaning unclear.
- **Training for Eucharistic Ministers and Readers,** Sat Nov 14, 10:00 a.m.–noon (internal ministry training).
- Excluded by policy (administrative or internal): special collections (Campaign for Human Development Nov 14, St. Vincent de Paul Nov 28, Retirement for Religious Dec 12, Building Fund Dec 19), "Parish Office Closed," staff, council, and committee meetings, funerals, baptisms, and preschool closures.

### Process

- Who will keep `data/events.json` current after launch, and how often?
- Should the hero always feature three events, or fewer during quiet seasons? (The site shows as many as are marked `featured: true`, up to three, and falls back to a "Mass at St. Matthias" slide if none remain.)

---

## D. About Us, staff, and contact

- **Staff roster** (from the Staff Directory, 2026-11-04). Confirm names, titles, and each person's consent to be listed: Fr. Roy Remo (Pastor), Fr. Alner "Al" Nambatac (Parochial Vicar), Deacon Rich Foley (Adult Faith Formation Coordinator), Deacon David Rolandelli (listed as "RCIA Coordinator"; shown as "Becoming Catholic Coordinator"), Carmen Perlas, Lisa Bamford (Administrative Assistant), Melanie Dresbach (Music Director), Rosemary Juarez (Preschool Director).
- **Carmen Perlas's title:** the Staff Directory says "Religious Education Coordinator"; the Faith Formation page signs her as "Pastoral Associate." The site uses Religious Education Coordinator.
- **Sabrina Harper** is the named contact on several old pages (Baptism for older children, First Communion, Confirmation, Catechesis, and adult studies) but is **not** in the current Staff Directory. The new site names Carmen Perlas for children's and youth programs instead. Confirm.
- Named volunteer contacts on old pages were replaced with "the parish office": Joey Gutierrez (Eucharistic Ministers) and Joe Yanacek (ushers). Confirm whether to name them.
- Staff bios were shortened, and all references to the other parish Fr. Roy and Fr. Al also serve were removed. Confirm.
- **Finance Council members** (Colton Daine, Chair; Lynda Brouchoud; Marybelle Ang; Paul Imbordino; Anne Campbell; Eilish McCaffrey; John McAfee; Nina Yang). Confirm the list is current and members agree to be listed.
- **Pastoral Council:** members are not listed. List them?
- "About four hundred registered families" and "served this neighborhood since 1961" (from Our Parish). Confirm.
- **Registration destination:** the site uses Flocknote (https://stmatthias.flocknote.com/), the registration link already used by the concept site. The current parish site also has a PDS "Household Registration Form" at `/parish-registration/`, and its homepage presents Flocknote as the newsletter. Which is the official way to register? If both, which should the button use?
- **Parking and accessibility:** nothing is published anywhere. Add to the New Here? FAQ once confirmed (where to park, step-free entrance, accessible restroom, hearing assistance, seating).
- Mailing address: Vanco lists ZIP+4 94062-3209. Use it anywhere?
- Social channels kept: Facebook, YouTube, and the youth ministry Instagram. Removed: Pinterest (smff2013) and @Pontifex. Is there a parish-wide Instagram?

---

## E. Sacraments, Faith Formation, and Ministries details to confirm

Content was migrated from the current pages and edited for plain language. Items below were either left out because they may be out of date or kept but need a second look.

**Sacraments**
- Baptism: suggested donation ($50–100) not published. Baptism preparation class schedule?
- Reconciliation: the site says weekday confession is by appointment through the office. The Saturday confession times on the old site are at another parish and were removed. Does St. Matthias offer any scheduled confession time?
- First Communion: process as described on the Eucharist page (second grade, family retreats in November and February/March, first Reconciliation in January, First Communion late April or early May). Still accurate for 2026–27?
- Confirmation: the registration Google Form required a Google sign-in (HTTP 401) on 2026-11-04, so it is **not linked**; the site says to contact the parish office. Confirm the form and whether it should be public. Collaboration details with the other parish's coordinators were removed. Is the Archdiocese's adult Confirmation preparation (Friday–Saturday session; Pentecost at the Cathedral) still offered?
- Anointing of the Sick: communal celebration during Holy Week. Still held?
- Vocations: links to the Archdiocese homepage (sfarch.org). Is there a better Office of Vocations URL?

**Faith Formation**
- GIFT: published as Sundays September–May, about twice a month, 11:00 a.m.–12:15 p.m. in Fr. Lacey Hall. The 2026–27 calendar shows first Sundays in Fr. Lacey Hall and third Sundays with a Google Meet link. Are third-Sunday sessions online? Is the *Faith Stories* curriculum still in use?
- Promise (Children's Liturgy of the Word, ages 3–6): published as depending on volunteers. Is it running in 2026–27? Its 2023 registration form is not linked.
- Middle School Youth Ministry: no schedule or location published (the last published schedule was 2024–25, Wednesdays 5:00–6:00 p.m., mostly held at the other parish's hall). Confirm the current schedule and location.
- High School Youth Ministry: the Peninsula Multifaith Coalition collaboration is mentioned. Still current?
- Adult Bible study: published as seasonal series on Mondays at 10:00 a.m., repeated at 7:00 p.m., in Fr. Lacey Hall (the fall 2026 series ended Nov 2). When is the next series?
- Becoming Catholic (OCIA): no session day, time, or location is published (the last published start date was Sept 2023). The calendar shows children's sessions ("OCIA-C") on select Sundays at 1:00 p.m. in Fr. Lacey Hall. Confirm the adult schedule.
- Safe-environment text (Protecting God's Children, Empowering God's Children) is kept from the current pages.

**Ministries**
- Music: the old page gives two Sunday rehearsal times ("8:45am for the Sunday 9:45am liturgy" and "rehearsal continues in the sanctuary at 0915"). The site shows 8:45 a.m.
- St. Vincent de Paul: the calendar shows a monthly meeting (second Tuesday, 7:00 p.m., Fr. Lacey Hall); not published. The old page mentions fifth-Sunday collections and Vanco mentions second collections; the site says "special collections."
- Justice and Charity Commission: published without a meeting time (the old page said third Thursday, in the Rectory). Still active?
- Maple Street Shelter dinner: published as an annual event. Still planned for 2027?
- Prayer Tree Network: the site says to share requests through the parish office. Confirm how requests should be submitted.
- Prayer Shawl Ministry: published as third Tuesday, 3:00 p.m., Fr. Lacey Hall (from the calendar).
- Not migrated; confirm they can stay off: Ecuador pilgrimage, ChristLife, past anti-racism book-club series (2020–2022), The Chosen watch party (2024), Breaking Open the Word (listed in the old index, no current page), Liturgical Environment, Shaping Our Future, parish history page, bulletin archive.
- The hall is called "Fr. Lacey Hall" throughout (the history page says "Fr. Lacey Memorial Hall").

---

## F. Photography to create (placeholder slots)

Every non-logo image is a solid-color placeholder (`.media-ph`) with a `data-image-slot` label naming the photo it is waiting for. All are decorative (`aria-hidden`), so surrounding text carries the meaning. Placeholders keep each container's original size and aspect ratio. **Replace all of them before nonprofit review.**

| Slot | Where | Photo needed |
|---|---|---|
| `featured-event-1`, `featured-event-2`, `featured-event-3` | Homepage hero slides, in order | A wide image for each featured event (Masses of Remembrance, Caroling, Christmas Eve), or a seasonal parish image per slide |
| `featured-event-fallback` | Hero, shown only if no featured events remain | The church during weekend Mass |
| `support-the-parish` | Hero Support Us card | Parishioners supporting the parish (16:9) |
| `mission-worship`, `mission-faith-formation`, `mission-service`, `mission-welcome`, `mission-community` | "A life shared in Christ" floating tiles (4:3). These same tiles fly into the Upcoming cards. | Mass, families learning together, service to neighbors, greeters at the door, parish fellowship |
| `event-welcome-weekend`, `event-rosary-for-peace`, `event-thanksgiving-mass`, `event-immaculate-conception`, `event-mary-mother-of-god`, `event-ash-wednesday`, `event-masses-of-remembrance`, `event-caroling-cookies-cocoa`, `event-christmas-eve-masses` | Homepage Upcoming cards and the Events page | One image per event |
| `support-regular-collection`, `support-roofing-fund` (and `support-annual-appeal`, `support-building-fund`, `support-st-vincent-de-paul` if activated) | Homepage giving posters and Support Us page | The church and parish life; the church roof or building exterior |
| `support-hero` | Support Us page hero | Parishioners at the offertory or a welcoming church interior (4:5 on desktop, 16:9 on phones) |
| `about-hero`, `sacraments-hero`, `faith-formation-hero`, `ministries-hero`, `events-hero` | Inner-page heroes, beside the headline (4:5 on desktop, 16:9 on phones) | The church in its Emerald Hills setting; a sacramental moment at the altar or font; families learning together; volunteers serving; a parish gathering |
| `about-church-exterior` | About Us, Our Parish & Mission (4:3 desktop, 16:9 phones; same for every section photo below) | St. Matthias Church exterior |
| `staff-fr-roy-remo`, `staff-fr-alner-nambatac`, `staff-deacon-rich-foley`, `staff-deacon-david-rolandelli`, `staff-carmen-perlas`, `staff-lisa-bamford`, `staff-melanie-dresbach`, `staff-rosemary-juarez` | About Us, Staff & Leadership (square, shown as a circle) | A head-and-shoulders portrait of each person |
| `sacrament-baptism`, `sacrament-reconciliation`, `sacrament-eucharist`, `sacrament-confirmation`, `sacrament-marriage`, `sacrament-anointing`, `sacrament-holy-orders` | Sacraments page, one per section | The font, the confessional, First Communion, a Confirmation, a wedding, the oils or a visit to the sick, an ordination or a priest at the altar |
| `formation-children-families`, `formation-youth`, `formation-adults`, `formation-becoming-catholic` | Faith Formation page, one per section | GIFT families, youth ministry, adult Bible study, an RCIA/Easter Vigil moment |
| `ministry-worship`, `ministry-service`, `ministry-welcome`, `ministry-care`, `ministry-parish-support` | Ministries page, one per section | Music ministry or readers, St. Vincent de Paul volunteers, greeters, Communion to the homebound, parish volunteers at work |
| `events-weekend-mass` | Events page, "Mass at St. Matthias" | The church during weekend Mass |

Technical note for when photos arrive: add an optional `image` field to each event and giving option and render it in `scripts/build.py`. The homepage flight animation pairs mission tile *n* with Upcoming card *n*, so keep their images visually related, and export WebP files with explicit width and height for page speed.

Other image questions:
- These files are no longer used by any page and can be archived: `images/Congregation*.png`, `images/generated/*`, `images/church-interior.jpg`, `images/placeholders/*.svg`, and `videos/*`. `Congregation-v3.png` is an AI-generated scene with likenesses of real parishioners; it must not be presented as documentary photography.
- Photo releases: anyone recognizable, especially children, needs consent on file.
- Logo: approve `images/LogoFinal.png` (shown in the header, footer, and favicon as the 256 px copy `images/logo-icon.png`, and used as the homepage share image). `NewLogo*.png` are earlier drafts and can be archived.

---

## G. Launch and platform decisions

- **Deployment exclusions:** `.vercelignore` (added 2026-11-04) keeps `docs/`, `data/`, `scripts/`, `.claude/`, and `videos/` off future deployments. Until the next deployment, these files are still publicly reachable on the Vercel preview (for example `/docs/needs-parish-confirmation.md`). After redeploying, confirm those URLs return 404.
- **Search indexing of the preview:** consider sending `X-Robots-Tag: noindex` only for `*.vercel.app` hosts once the custom domain is live, so search engines index only the parish domain. Decision needed; not implemented.
- **Who runs the build:** after editing `data/*.json`, someone must run `python3 scripts/build.py` and redeploy. Expired events also disappear on their own in the browser, but new events require a rebuild.
- **Page speed:** run Google PageSpeed Insights on the custom domain after real photos are added.
