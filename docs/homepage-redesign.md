# St. Matthias Parish — Homepage and Navigation Redesign (Concept)

Date: 2026-09-10
Status: concept for review. Not launched. No payment processing is built.
Scope: **homepage and site navigation only.** The section pages (Plan a Visit, Worship & Sacraments, Community, Preschool, About, Give) are described here as notes and intro copy. They are not built.

**What is built:** `index.html`, `css/tokens.css`, `css/site.css`, `js/nav.js`, `js/motion.js`, `images/logo-badge.svg`, `images/logo-lockup.svg`, `images/placeholders/*.svg`, and `images/Congregation-v3.png`. Earlier hero versions are retained but are no longer used by the visible hero.

**How to view:** open the "St. Matthias preview" server from `.claude/launch.json` (it runs `node .claude/serve.js 8787`) and go to `http://localhost:8787`. The three visual directions switch from the "Concept" control at the bottom-left of the page (see section 10).

Everything marked `[NEEDS PARISH CONFIRMATION]` on the page and in these notes is listed in `docs/needs-parish-confirmation.md`.

---

## 1. Audit of the current site

Reviewed on 2026-09-10: the homepage, New to St. Matthias, Our Parish, Staff Directory, Parish Leadership, History, Shaping Our Future, Parish Registration, Online Donations, the sacrament pages (Baptism, Reconciliation, Eucharist, Confirmation, Marriage, Anointing of the Sick), Becoming Catholic (RCIA), GIFT, Youth Ministry, the Ministries Index and the Prayer and Worship, Justice and Charity, and Community Building pages, and About the Preschool. The event calendar page was not reviewed in this pass.

### What gets in the way

1. **The navigation is built for insiders.** Seven top-level items with five dropdowns and about 45 links. Several labels come from the parish's internal pastoral-plan categories ("Catechesis", "Stewardship", "Evangelization", "Ministries Index", "Shaping Our Future"). A visitor has to already know the parish's vocabulary to find things.
2. **A first-time visitor has no clear path.** "New to St. Matthias?" is the eighth item inside the Parish dropdown. The page is a checklist for registering and enrolling, not a welcome. Nothing on the site says what to expect at Mass, where to park, or how accessible the building is.
3. **The St. Charles schedule is shown next to the St. Matthias schedule with no explanation.** On every page, "St. Charles: Mon–Fri 5:00 pm, Saturday 5:00 pm, Sunday 8:30 and 11:00 am" sits under the St. Matthias Mass times. A newcomer can drive to the wrong church.
4. **Office hours conflict.** "Mon, Tues and Thurs 9AM–4PM" (New to St. Matthias, Staff Directory, Parish Leadership) versus "Monday–Thursday 10:00 am–4:00 pm" (Baptism, Marriage, Reconciliation, RCIA, ministry pages).
5. **Giving is one sentence.** "Support Us" leads to `/online-donations/`. The visible text is a statement about PCI security. The page text does not name the giving provider, and there are no bank-transfer, check, or mailing instructions and no note on what gifts support.
6. **Dated content.** COVID-19 pandemic references (Our Parish, History); the 60th anniversary (2021); "RCIA is scheduled to begin on Sunday, September 17, 2023"; pastoral-plan process dates from 2014–2016; a pastor succession list; the footer reads "© 2017 – 2026". The homepage events list includes "Church in Latin America Spec Coll", an internal collection label.
7. **Acronyms are used as labels.** GIFT, RCIA, RCIC, MSYM, HSYM.
8. **Two registration paths.** A Household Registration Form on the site (needs JavaScript; does not say what happens after you submit) and a Flocknote link.
9. **The homepage has no first action.** It is an image slider (greeters, the church interior, a priest portrait, the car-show flyer), the mission statement, a preschool promo, an events list, and a bulletin list. There is no clear next step for a newcomer and no giving entry point outside the menu.
10. **Footer social links include channels that are not the parish's own.** Facebook, YouTube, and the youth Instagram are parish channels. The Pinterest board and the @Pontifex Twitter link are not, or are not current.

### What is strong and should carry into the redesign

- **Welcome Weekend.** A real, monthly, well-described hospitality event with a blessing for newcomers. This is the best proof of the "close-knit" message.
- **About 400 families.** A real number that supports "people will know your name."
- **A livestream on YouTube**, so people can watch before they visit.
- **A weekly email through Flocknote**, which is also the registration path.
- **A complete ministries index** and sacrament pages with real process detail (contacts, requirements, timing).
- **The preschool** has its own website and its own phone number.
- **A clear pastoral relationship with St. Charles** (shared pastor, weekday Mass and Saturday confessions there). It only needs to be explained, not hidden.

---

## 2. Keep, combine, move, or remove

| Current site content | Recommendation | Where it goes |
|---|---|---|
| Home slider, mission statement, preschool promo, events list, bulletin list | **Replace** with the new homepage (section 5) | Home |
| New to St. Matthias? | **Keep, rewrite** as a warm welcome with what to expect | Plan a Visit |
| Mass times (both parishes on every page) | **Keep St. Matthias times everywhere.** Move the St. Charles weekday Mass and Saturday confession times into one explained note | Home (Mass times card), Plan a Visit, Worship & Sacraments |
| Parish Registration form + Flocknote link | **Combine** into one "Register" action that uses Flocknote | Plan a Visit; footer |
| Sacraments (8 pages) | **Keep**, one page per sacrament, plain-language titles | Worship & Sacraments |
| Prayer and Worship ministries (music, readers, ushers, altar servers, Eucharistic ministers, Rosary for Peace, Prayer Tree, liturgical environment) | **Keep**, grouped as "Ways to pray and serve at Mass" | Worship & Sacraments |
| Faith Formation: Adult Faith Formation, Breaking Open the Word, Becoming Catholic (RCIA) | **Keep**, spell out RCIA as "Becoming Catholic" | Community → Learn |
| GIFT, Children's Liturgy of the Word, Youth Ministry (middle and high school) | **Keep**, spell out GIFT ("Generations in Faith Together") on first use | Community → Families & Young People |
| Justice & Charity: St. Vincent de Paul, Maple Street Shelter dinner, Justice and Charity Commission, Anti-Racism Book Club, Ecuador pilgrimage | **Keep** | Community → Serve (book club under Learn) |
| Community Building: Welcome Weekend, Greeters, Welcome Ambassadors | **Keep**, merge into one "Meet people" area | Community → Meet People; Plan a Visit |
| Family & Pastoral Care: sick and homebound, funeral support, prayer shawl | **Keep** as "Care and support" | Community |
| Ministries Index | **Keep** as a single alphabetical list, but not in the main menu | Community → All ministries |
| Catechesis, Stewardship, Evangelization (pastoral-plan categories) | **Remove as navigation labels.** The ministries inside them move to the groups above | — |
| Shaping Our Future (2014–2016 pastoral plan) | **Move** to About, shortened to what still applies | About |
| Our Parish, History, Staff Directory, Parish Leadership (councils) | **Keep**, shortened; remove pandemic and anniversary references | About |
| Parish Bulletin Archive | **Keep** as a utility page (footer link) | About → Bulletins |
| Event Calendar | **Keep** as the single calendar; feature 3–4 public events on Home | Community → Calendar |
| Preschool (7 subpages + external site) | **Combine** into one overview page that links to `stmatthiaspreschool.org` for details, staff, calendar, and payments | Preschool |
| Online Donations ("Support Us") | **Rebuild** as Give: online, bank transfer, other ways, questions | Give |
| Pinterest and @Pontifex links | **Remove** unless the parish confirms they are active | — |
| "Church in Latin America Spec Coll" and other internal collection labels | **Remove** from public event lists (keep in the bulletin) | — |

---

## 3. Simplified sitemap

```
Home
Plan a Visit
  What to expect · Mass times and livestream · Directions and parking [NEEDS PARISH CONFIRMATION]
  Welcome Weekend · Watch a Mass online · Register with the parish (Flocknote)
Worship & Sacraments
  Mass times · Livestream · Confession
  Baptism · First Communion · Confirmation · Marriage · Anointing of the Sick · Vocations
  Ways to pray and serve at Mass: music ministry, readers, ushers, altar servers,
    Eucharistic ministers, Rosary for Peace, Prayer Tree
Community
  Learn: adult faith formation, Breaking Open the Word, Anti-Racism Book Club, Becoming Catholic (RCIA)
  Serve: St. Vincent de Paul, Maple Street Shelter dinner, Justice and Charity Commission, Ecuador pilgrimage
  Families & Young People: GIFT (K–8), Children's Liturgy of the Word, middle and high school youth ministry
  Meet People: Welcome Weekend, Sunday music fellowship, greeters and welcome ambassadors
  Care and support: the sick and homebound, funeral support, prayer shawl ministry
  Calendar · All ministries (A–Z)
Preschool
  Overview → stmatthiaspreschool.org
About
  Our parish and mission · Clergy and staff · Councils · History · Bulletins · Pastoral plan · Contact
Give
  Give online · Give by bank transfer · Other ways to give · Questions

Footer only: Register, Bulletins, Calendar, Privacy policy [NEEDS PARISH CONFIRMATION]
```

---

## 4. Navigation

Six labels and one button. No mega-menu. Built in `index.html` (header and drawer) and `js/nav.js`.

| Label | Link | Purpose |
|---|---|---|
| Plan a Visit | `/plan-a-visit/` | The newcomer path |
| Worship & Sacraments | `/worship-and-sacraments/` | Mass, prayer, sacraments |
| Community | `/community/` | Learn, serve, families, meet people, calendar |
| Preschool | `/preschool/` | Overview and link to the preschool site |
| About | `/about/` | Who we are, staff, history, bulletins, contact |
| **Give** | `/give/` | Terracotta button, always visible |

"Home" is the logo. The drawer also lists Home as its first item.

### Desktop (1024 px and wider)

- Fixed header, 4.5 rem tall on desktop (4 rem on smaller screens). Logo lockup on the left (round mark + "St. Matthias Parish" + "Responding to the Call of Jesus"). Five text links and the Give button on the right.
- Over the hero image the header is transparent with light text. After 40 px of scroll it gets a frosted parchment background (`.is-solid`), and the text turns navy.
- Links show a short underline on hover and focus. The Give button is the only filled element in the header.
- The header is 100% of the width; content stays inside the 1200 px container.

### Mobile and tablet (below 1024 px)

- Header shows the logo lockup and a "Menu" button (`.nav-toggle`, `aria-expanded`).
- Tapping Menu opens a full-screen drawer (`#drawer`, `role="dialog"`) from the right with a scrim behind it. The list (Home + the five sections) fades in one item at a time. Below it: a full-width Give button, the two Mass-time pills, the address, and the phone number.
- Close with the X button, the scrim, the Escape key, or by tapping any link. Focus moves to the close button on open and back to the Menu button on close. Tab is trapped inside the drawer while it is open. The page behind does not scroll.
- If the window grows past 1024 px while the drawer is open, it closes on its own.

### Where the nav links go today

The section pages are not built, so the primary navigation stays within the homepage: Plan a Visit, Worship & Sacraments, Community, About, and Give scroll to the corresponding homepage sections; Preschool opens the existing preschool website. Any remaining link to an unfinished internal page is intercepted and displays a brief “coming soon” message instead of leaving the homepage or returning a 404. External links continue to work normally.

---

## 5. Homepage wireframe (as built)

Order follows the brief. One idea per section. Every section has a heading, at most two paragraphs, and one clear action.

```
┌──────────────────────────────────────────────────────────────────┐
│ HEADER  [mark] St. Matthias Parish   Plan a Visit · Worship &     │
│         Responding to the Call…      Sacraments · Community ·     │
│                                      Preschool · About  [ Give ]  │
├──────────────────────────────────────────────────────────────────┤
│ 1  HERO  (100vh, congregation photo, navy overlay)                │
│    overline · H1 (two lines, italic ending) · one-sentence lede   │
│    [Plan Your Visit] [View Mass Times]                            │
│    right: "Mass this weekend" card — Sat 5:00 · Sun 9:45 · Live   │
│    bottom: SCROLL cue · address                                   │
├──────────────────────────────────────────────────────────────────┤
│ 2  MASS TIMES & LOCATION                                          │
│    left: heading, one paragraph, two time pills, livestream link  │
│          [Get Directions] [What to Expect]                        │
│    right: "Find us" card — address, phone, email, office hours*,  │
│          parking*, and the St. Charles note                       │
├──────────────────────────────────────────────────────────────────┤
│ 3  WHY PEOPLE COME  (scroll collage, 280vh on desktop)            │
│    centered heading + one paragraph stays pinned while five       │
│    photo tiles fly in from the edges and settle around it;        │
│    captions appear once each tile lands. Below 1024px: a          │
│    two-column photo grid under the heading.                       │
├──────────────────────────────────────────────────────────────────┤
│ 4  NEW HERE?  (alt background)                                    │
│    left: arched photo · right: heading, two paragraphs,           │
│    three check items, [Plan Your Visit]  Watch a Mass online →    │
├──────────────────────────────────────────────────────────────────┤
│ 5  WHAT'S HAPPENING                      See All Events →         │
│    three event cards: date block, title, meta line, one           │
│    paragraph, one link                                            │
├──────────────────────────────────────────────────────────────────┤
│ 6  FIND YOUR PLACE  (alt background)                              │
│    heading + one line, then five cards:                           │
│    Pray · Learn · Serve · Families & Young People · Meet People   │
├──────────────────────────────────────────────────────────────────┤
│ 7  NEWSLETTER BAND  (navy)                                        │
│    heading, one line, [Sign up on Flocknote], cadence note*       │
├──────────────────────────────────────────────────────────────────┤
│ 8  GIVING                                                         │
│    left: heading, two paragraphs, [Give Online] [Give by Bank     │
│          Transfer]                                                │
│    right: "About your gift" trust card — security, provider*,     │
│          bank transfer*, questions                                │
├──────────────────────────────────────────────────────────────────┤
│ 9  FOOTER  (navy)                                                 │
│    badge + name + address/phone/email · Mass times · Parish life  │
│    · Connect · copyright · St. Charles relationship line          │
└──────────────────────────────────────────────────────────────────┘
* = [NEEDS PARISH CONFIRMATION]
```

### Motion notes

- **Page load:** the hero headline slides up word by word out of a mask; the overline, lede, buttons, and Mass card follow in order. Nothing animates until the web fonts are ready (800 ms fallback).
- **Hero:** the opening carousel occupies 84% of the viewport so a 16% preview of the next section is always visible. The first image pans continuously from its far-left framing to its far-right framing over fifteen seconds, beginning with the priest in white-and-gold visible and ending with the priest in black fully visible. The second and third carousel images remain on screen for five seconds each. Later narrative sections retain their scroll-linked transitions.
- **Mission statement:** every word remains dim until the first line enters the viewport. The words then illuminate in reading order, with the first line complete before the third line appears and the full statement complete when the last line is 100 px above the bottom edge. The section uses normal page flow rather than a pinned scroll hold, so visitors can continue downward without an animation-imposed delay.
- **Find your place:** the ministry cards occupy one viewport in normal page flow. The former extra 80% sticky hold has been removed so the events section follows immediately when visitors continue scrolling.
- **Sections:** headings and cards fade and rise 24 px when they enter the viewport (IntersectionObserver). Card grids stagger by 90 ms.
- **Collage:** on desktop only, the section is 280 vh tall with a sticky 100 vh stage. Scroll progress (0–1) drives each tile's own slice of the timeline. Tiles start off-canvas with a rotation, then settle into fixed rest positions with a small resting tilt. Captions fade in at 78% of each tile's travel. Below 1024 px there is no scrub; the tiles are a static grid.
- **Reduced motion:** all reveals are shown, the collage is shown in its settled state, and transitions are off.

---

## 6. Homepage headlines and copy (as built)

Source facts: the current parish site, 2026-09-10. Nothing below is invented. Missing facts are marked.

**Page title:** St. Matthias Catholic Church | Catholic Parish in Emerald Hills, Redwood City
**Meta description:** St. Matthias is a welcoming Catholic parish of about 400 families in Emerald Hills, Redwood City. Mass Saturday 5:00 p.m. and Sunday 9:45 a.m. at 1685 Cordilleras Road. Come as you are.

### 1. Hero
- Overline: A Catholic parish in Emerald Hills, Redwood City
- H1: Come worship with a parish where people *know your name.*
- Lede: St. Matthias is a Roman Catholic parish of about 400 families in the Emerald Hills of Redwood City. Come as you are.
- Buttons: **Plan Your Visit** · View Mass Times
- Mass card: Mass this weekend — Saturday 5:00 p.m. · Sunday 9:45 a.m. — Livestream available
- Bottom bar: Scroll · 1685 Cordilleras Road · Emerald Hills

### 2. Mass times and location
- Overline: Mass times
- H2: Join us this weekend.
- Copy: Two Masses every weekend at St. Matthias. Newcomers are blessed at both on Welcome Weekend, the second full weekend of each month.
- Pills: Saturday 5:00 p.m. · Sunday 9:45 a.m.
- Link: Livestream available on YouTube
- Buttons: **Get Directions** · What to Expect
- Find us card: 1685 Cordilleras Road, Redwood City, CA 94062 · Phone (650) 366-9544 · Email info@stmatthiasparish.org · Office `[NEEDS PARISH CONFIRMATION] Office hours` · Parking `[NEEDS PARISH CONFIRMATION] Parking and accessibility`
- Note: St. Matthias shares its pastor, Fr. Roy Remo, with St. Charles Parish in San Carlos. Weekday Mass (Monday to Friday, 5:00 p.m.) and Saturday confessions (3:30 to 4:30 p.m.) are at St. Charles, 880 Tamarack Avenue. Confessions at St. Matthias are by appointment through the parish office.

### 3. Why people come (collage)
- Overline: Why people come
- H2: You will not be anonymous here.
- Copy: Every month we bless newcomers at Mass, then share a meal. Families learn together in GIFT on Sunday mornings. Neighbors serve neighbors through St. Vincent de Paul. At about 400 families, St. Matthias is small enough that people notice when you arrive, and when you are missing.
- Captions: A blessing for newcomers on Welcome Weekend · Coffee, donuts, and juice after the 9:45 Mass · Appetizers and a saint's story on Saturday nights · Families learning together in GIFT · Neighbors serving with St. Vincent de Paul

### 4. New here?
- Overline: New here?
- H2: Visiting for the first time? We are glad you are here.
- Copy: Come as you are. Sit anywhere you like. If you have questions, the people around you will be glad to help.
- Copy: On the second full weekend of each month we hold Welcome Weekend. First-time visitors and visiting parishioners receive a special blessing at both Masses.
- Checks: Saturday after the 5:00 p.m. Mass: appetizers and a movie about a saint. Bring a dish to share if you like. · Sunday after the 9:45 a.m. Mass: donuts, coffee, and juice in Fr. Lacey Hall. · Not ready to visit in person? Watch a Mass on our YouTube livestream first.
- Actions: **Plan Your Visit** · Watch a Mass online →

### 5. What's happening
- Overline: What's happening
- H2: Come to something this month.
- Link: See All Events →
- Card: 12–13 Sep — Welcome Weekend — After the 5:00 p.m. and 9:45 a.m. Masses — Newcomers receive a special blessing. Saturday brings appetizers and a movie about a saint. Sunday brings donuts, coffee, and juice in Fr. Lacey Hall. — Plan Your Visit →
- Card: 17 Oct · Saturday — Car Show with the Highlands Community Club — 9:00 a.m. to 3:00 p.m. · Free admission — Classic cars and trophies, music and food, raffles, and fun for the whole family at 1685 Cordilleras Road. All are welcome. — `[NEEDS PARISH CONFIRMATION] Car registration link`
- Card: Thu · Every week — Rosary for Peace — 10:00 a.m. in the church — Parishioners gather each week to pray the rosary for peace. Open to all. Come once or come every week. — Ways to pray →

### 6. Find your place
- Overline: Find your place
- H2: There is a place for you here.
- Copy: Start with what draws you. Someone will be glad to help you get started.
- Pray — Worship and prayer — Sing with the music ministry (no experience needed; rehearsals Saturday 4:00 p.m. and Sunday 8:45 a.m.), serve as a reader, usher, altar server, or Eucharistic minister, or join the Rosary for Peace on Thursdays. → Worship & Sacraments
- Learn — Grow in faith — Adult faith formation, Breaking Open the Word, the Anti-Racism Book Club, and RCIA for adults who want to become Catholic. → Faith formation
- Serve — Care for neighbors — St. Vincent de Paul food collections, the annual Maple Street Shelter dinner, the Justice and Charity Commission, and care for the sick, the grieving, and the homebound. → Service ministries
- Families & young people — Room to grow up here — GIFT, our Sunday morning family formation program for kindergarten through eighth grade, Children's Liturgy of the Word, middle and high school youth ministry, and a preschool for ages 2 to 5. → Families and youth
- Meet people — Get to know us — Welcome Weekend hospitality, Sunday morning music fellowship at 8:15 a.m., Saturday saint films, and the greeters and welcome ambassadors who meet you at the door. → Community life

### 7. Newsletter
- Overline: Stay in touch
- H2: Get the weekly parish email.
- Copy: Parish news and upcoming events, sent through Flocknote, the same place you can register with the parish.
- Button: **Sign up on Flocknote** · `[NEEDS PARISH CONFIRMATION] Email cadence and contents`

### 8. Giving
- Overline: Giving
- H2: Keep St. Matthias a welcoming place.
- Copy: Your generosity helps St. Matthias remain a welcoming parish, support our ministries, care for our neighbors, and maintain our church home in Emerald Hills.
- Copy: Every amount matters, and every gift is handled with care.
- Buttons: **Give Online** · Give by Bank Transfer
- Trust card "About your gift": Secure online giving — Online donations are secured with the highest level of PCI (Payment Card Industry) security standards. · Online giving provider `[NEEDS PARISH CONFIRMATION] Provider name and link` · Bank transfer `[NEEDS PARISH CONFIRMATION] Bank name, account details, and instructions` · Questions — Call the parish office at (650) 366-9544 or email info@stmatthiasparish.org. · Concept only. No payment processing is built into this design.

### 9. Footer
- St. Matthias Catholic Church · 1685 Cordilleras Road, Redwood City, CA 94062 · (650) 366-9544 · info@stmatthiasparish.org
- Mass times: Saturday 5:00 p.m. · Sunday 9:45 a.m. · Get directions · Watch the livestream
- Parish life: Full calendar · Weekly bulletins · Register as a parishioner · Give · St. Matthias Preschool · (650) 367-1320
- Connect: Weekly email (Flocknote) · YouTube · Facebook · Youth ministry on Instagram · `[NEEDS PARISH CONFIRMATION] Privacy policy`
- © 2026 St. Matthias Parish · Archdiocese of San Francisco · St. Matthias shares its pastor, Fr. Roy Remo, with St. Charles Parish in San Carlos.

---

## 7. Section pages: titles and intro copy (notes only, not built)

Each page opens with the same pattern as the homepage: overline, one headline, one or two short paragraphs, one primary action. Facts below come from the current site. Details still to confirm are marked.

### Plan a Visit
- Title: Plan a Visit | St. Matthias Catholic Church, Redwood City
- H1: Your first visit, made easy.
- Intro: You do not need to know anyone, or anything, to come to Mass at St. Matthias. Sit where you like, follow along, and stay for coffee if you can. Mass is Saturday at 5:00 p.m. and Sunday at 9:45 a.m. at 1685 Cordilleras Road in Emerald Hills. If you would rather watch first, our Masses are livestreamed on YouTube.
- Primary action: Get Directions. Secondary: Register with the parish (Flocknote).
- Contents: what to expect at Mass `[NEEDS PARISH CONFIRMATION] — length, children, dress, communion guidance in the parish's own words`; directions and parking `[NEEDS PARISH CONFIRMATION]`; accessibility `[NEEDS PARISH CONFIRMATION]`; Welcome Weekend; office hours `[NEEDS PARISH CONFIRMATION]`; the St. Charles note.

### Worship & Sacraments
- Title: Worship & Sacraments | St. Matthias Catholic Church
- H1: Pray with us.
- Intro: Mass at St. Matthias is Saturday at 5:00 p.m. and Sunday at 9:45 a.m., with a livestream for those who cannot be here. This page has everything else about the sacramental life of the parish: confession, baptism, first communion, confirmation, marriage, anointing of the sick, and the ministries that serve at Mass.
- Primary action: View Mass Times (anchor). Secondary: Contact the parish office.
- Contents: Mass times and livestream; confession (Saturday 3:30–4:30 p.m. at St. Charles, 880 Tamarack Avenue, San Carlos; by appointment at St. Matthias through the office); Baptism (contact Deacon Rich Foley through the office; baptisms at weekend Masses; preparation class); First Communion (through GIFT; celebrated late April or early May); Confirmation (two-year high school program); Marriage (speak with the clergy at least six months ahead); Anointing of the Sick and communion for the homebound (call the office); Vocations; ways to serve at Mass — music ministry (rehearsals Saturday 4:00 p.m., Sunday 8:45 a.m.), readers, ushers, altar servers, Eucharistic ministers, Rosary for Peace (Thursdays 10:00 a.m.), Prayer Tree.

### Community
- Title: Community | St. Matthias Catholic Church
- H1: Find your people.
- Intro: At about 400 families, St. Matthias is small enough to know you and big enough to have a place for you. Learn, serve, bring your family, or simply meet people. Start anywhere.
- Primary action: See the Calendar. Secondary: All ministries (A–Z).
- Contents by group: **Learn** — adult faith formation, Breaking Open the Word, Anti-Racism Book Club, Becoming Catholic (RCIA). **Serve** — St. Vincent de Paul (food collections at Sunday Mass), the annual Maple Street Shelter dinner, the Justice and Charity Commission, the Ecuador pilgrimage. **Families & Young People** — GIFT (Generations in Faith Together, kindergarten through eighth grade, Sunday mornings September to May), Children's Liturgy of the Word, middle school and high school youth ministry. **Meet People** — Welcome Weekend, Sunday music fellowship at 8:15 a.m., greeters and welcome ambassadors. **Care and support** — the sick and homebound, funeral support team, prayer shawl ministry. Program fees, dates, and contacts: `[NEEDS PARISH CONFIRMATION] — confirm current-year details before publishing`.

### Preschool
- Title: St. Matthias Preschool | Redwood City
- H1: A place for fun. A place for learning.
- Intro: St. Matthias Preschool is a licensed, play-based Catholic preschool for children ages 2 through 5, open Monday to Friday. It has served Redwood City families since 1977. Visit the preschool website for programs, staff, the calendar, enrollment, and payments.
- Primary action: Visit the Preschool Website (stmatthiaspreschool.org). Secondary: Call (650) 367-1320.
- Note: the parish site lists the preschool at 533 Canyon Road and hours of 7:30 a.m. to 5:30 p.m. `[NEEDS PARISH CONFIRMATION] — confirm address, hours, and licensing text with the preschool director before publishing`.

### About
- Title: About St. Matthias | Catholic Parish in Emerald Hills, Redwood City
- H1: A Roman Catholic community in Emerald Hills since 1961.
- Intro: St. Matthias is a parish of the Archdiocese of San Francisco, founded on June 24, 1961, in the Emerald Hills of Redwood City. We strive to respond to the call of Jesus through worship and sacraments, faith formation, service, and social opportunities. Our pastor, Fr. Roy Remo, also serves St. Charles Parish in San Carlos.
- Primary action: Contact us. Secondary: Read this week's bulletin.
- Contents: mission; clergy and staff (from the current directory; `[NEEDS PARISH CONFIRMATION] — confirm the roster is current`); Pastoral and Finance Councils; history (keep founding, Fr. Lacey, the church dedication in 1963, the hall; drop the pandemic and anniversary passages); the pastoral plan, shortened to what still applies; bulletins; contact and office hours `[NEEDS PARISH CONFIRMATION]`.

### Give
- Title: Give | St. Matthias Catholic Church
- H1: Keep St. Matthias a welcoming place.
- Intro: Your gift keeps the lights on, the doors open, and the coffee hot. It supports our ministries, our care for neighbors in need, and the upkeep of our church home in Emerald Hills. Give in the way that is easiest for you.
- Primary action: Give Online. Secondary: Give by Bank Transfer.
- Contents: Give online `[NEEDS PARISH CONFIRMATION] — provider name and link`; Give by bank transfer `[NEEDS PARISH CONFIRMATION] — bank name, account details, reference format, and instructions`; other ways to give `[NEEDS PARISH CONFIRMATION] — checks, mail, in-person, stock or planned gifts, if offered`; security statement (PCI); questions — parish office (650) 366-9544, info@stmatthiasparish.org. Note for build: no live payment form in the concept.

---

## 8. Call-to-action strategy

One primary action per screen. Terracotta filled button = primary. Outlined button = secondary. Arrow link = tertiary.

| Placement | Primary | Secondary | Goal served |
|---|---|---|---|
| Header (every page) | **Give** (button) | Section links | Giving is one tap from anywhere |
| Hero | **Plan Your Visit** | View Mass Times (anchor) | Bring new people in |
| Mass times | **Get Directions** (Google Maps) | What to Expect | Remove the last barrier to showing up |
| Collage | none (read) | — | Prove the community message |
| New here? | **Plan Your Visit** | Watch a Mass online (YouTube) | Lower the bar for the hesitant |
| Events | See All Events | one arrow link per card | Existing parishioners find things to join |
| Find your place | one arrow link per card | — | Existing parishioners discover ministries |
| Newsletter band | **Sign up on Flocknote** | — | Keep people connected; registration path |
| Giving | **Give Online** | Give by Bank Transfer | Simple, trustworthy giving |
| Footer | Give, Register, Directions, Livestream | Calendar, Bulletins, social | Utility |
| Mobile drawer | **Give** (full width) | Mass pills, address, phone | Same priorities, one thumb |

Rules: never two primary buttons side by side; every section ends with a way forward; phone and email are always plain links; external links open in a new tab with `rel="noopener"`.

---

## 9. Information that needs parish confirmation

Full list with sources: `docs/needs-parish-confirmation.md`. On the homepage today:

1. Office hours (the current site shows two different schedules)
2. Parking and accessibility
3. Car Show registration link
4. Weekly email cadence and contents
5. Online giving provider name and link
6. Bank transfer details and instructions
7. Privacy policy link
8. Photos for every remaining placeholder tile

---

## 10. Three visual homepage directions

All three are built as CSS skins on the same markup (`css/site.css`, "Visual directions" block). Switch with the "Concept" control at the bottom-left of the page. The choice is saved in `localStorage` under `stm-direction` so it survives reloads. The control and the skins are for review only and should be removed before launch, keeping only the chosen direction.

| | Warm Neighborhood Parish (`warm`, default) | Quiet Sacred Editorial (`quiet`) | Modern Community Hub (`hub`) |
|---|---|---|---|
| Feel | A parish that knows your name | A place to be still | A busy, friendly campus |
| Surface | Sanctuary parchment `#fbf9f4` | Lighter parchment `#FAF8F5`, more air | Same base, more colored panels |
| Section padding | default | largest (up to 7 rem) | tightest (up to 4.5 rem) |
| Headings | Newsreader 500 | Newsreader 400, tighter tracking, no overline rule | Newsreader 600, dot overlines |
| Cards | linen border, lifts on hover | flat, hairline navy-soft border, no hover lift | pill radius, no border, alternating navy-soft / sage-wash / terracotta-soft fills |
| Mass pills | terracotta-soft | navy-soft | terracotta-soft |
| Newsletter band | navy | linen with navy text, terracotta overline | sage-moss with parchment text |
| Hero overlay | navy-deep 62% → 18% | navy-deep 74% → 30% | navy 66% → sage 16% |
| Collage tiles | resting tilt ±2° | no tilt, soft float shadow, slightly desaturated | more tilt (×1.4), slightly more saturated |
| Buttons | rounded | small radius | full pill |

Recommendation: **Warm** for launch. It carries the "know your name" message best and reads as the most welcoming to a first-time visitor. Quiet is the strongest alternative if the parish wants a calmer, more contemplative tone.

---

## Logo

- `images/logo-badge.svg` — the primary logo. A round navy ring with the words "ST. MATTHIAS PARISH" on top and "Responding to the Call of Jesus" below. Inside: a simple line drawing of the St. Matthias church with its tall cross, redwoods on both sides, and a row of people of every color holding hands along the ground line. Colors are the Sanctuary Editorial navy, terracotta, sage, and parchment.
- `images/logo-lockup.svg` — the horizontal header version: the same disc mark at small size next to the name and tagline.
- The wording from the current logo is kept. The church building is kept. The open, welcoming reading comes from the row of people, not from any slogan.
- `[NEEDS PARISH CONFIRMATION]` the parish should approve the mark before it is used on print or social.

---

## Implementation notes

- **No dependencies.** Plain HTML, CSS custom properties, and two small scripts. Fonts load from Google Fonts (Newsreader, Source Sans 3) with system fallbacks.
- **Tokens** (`css/tokens.css`) follow `DESIGN.md` "Sanctuary Editorial": colors, type scale, spacing, radii, shadows, motion timings, and the component knobs the three skins override.
- **Accessibility:** skip link, landmark roles, `aria-labelledby` on every section, visible focus rings, drawer focus trap and Escape, `prefers-reduced-motion` honored everywhere, alt text on every image (placeholders say what photo should go there), color contrast checked against navy and parchment.
- **Performance:** the hero uses the exact supplied PNG with explicit dimensions. Images below the fold use `loading="lazy"`.
- **SEO:** title and description name "Catholic parish" and "Emerald Hills, Redwood City" once each; JSON-LD `Church` schema with address, phone, email, and social profiles; one H1; sections use H2.
- **Placeholders:** every photo tile and the New here arch remain placeholders. The hero is an AI-generated concept based on the real church-interior photo and should be parish-approved or replaced with an authentic photograph before launch.
- **Remove before launch:** the concept switcher (`.concept-switch` in `index.html`, its block in `css/site.css`, and the switcher section of `js/motion.js`), the `stm-direction` pre-script in the head, and the two unused skins.
- **Not built:** the six section pages, the calendar, the bulletin archive, search, any form, and any payment or bank-transfer flow. Unfinished internal links are prevented from navigating and display a “coming soon” message.
