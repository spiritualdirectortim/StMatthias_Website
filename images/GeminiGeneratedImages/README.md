# Gemini-generated homepage photos

AI-generated with Gemini (Nano Banana Pro, Google AI Pro account), 2026-11-05.
Brief: photorealistic, candid documentary style, people aged 25–35 doing things,
no recognizable church architecture. These are illustrations, not photos of real
parishioners. Replace them with real parish photography when it exists.

- `*.jpg` are the full-size originals (2752×1536 for 16:9, 2400×1792 or 1200×896 for 4:3).
- `web/*.webp` are the site-ready exports (cover-cropped, quality 0.82).
- `contact-sheet.jpg` shows all 30 at a glance.

| Homepage slot (`data-image-slot`) | Web file(s) | Original |
|---|---|---|
| `featured-event-*` for Masses of Remembrance | `hero-masses-of-remembrance-2400/1200.webp` | `hero-remembrance-v3.jpg` |
| `featured-event-*` for Caroling, Cookies & Cocoa | `hero-caroling-cookies-cocoa-2400/1200.webp` | `hero-caroling-v2.jpg` |
| `featured-event-*` for Christmas Eve Masses | `hero-christmas-eve-masses-2400/1200.webp` | `hero-christmas-eve.jpg` |
| `featured-event-fallback` | `hero-weekend-mass-2400/1200.webp` | `hero-fallback-mass.jpg` |
| `support-the-parish` (16:9) | `support-the-parish-800.webp` | `support-the-parish.jpg`: a couple giving an envelope and cash at an offering box (replaced 2026-11-05). The earlier volunteers image is kept as `support-the-parish-volunteers.jpg` and is unused. |
| `mission-worship`, `-faith-formation`, `-service`, `-welcome`, `-community` (4:3) | `mission-*-900.webp` | `mission-*.jpg` |
| `event-<id>` Upcoming cards | `event-<id>-960.webp` (960×540) | `event-<id>.jpg` |
| `event-masses-of-remembrance`, `event-caroling-cookies-cocoa`, `event-christmas-eve-masses` | `event-<id>-960.webp` | cropped from the matching hero |
| `support-<fund>` giving posters (4:3) | `support-<fund>-800.webp` (800×600) | `support-<fund>.jpg` |

Hero images keep the people right of center and darker space on the left for the headline.

## Inner pages (generated and wired in 2026-11-05)

`scripts/build.py` fills the Events-page event photos and the Support Us giving cards. The heroes and section photos are fixed `<img>` tags in each page's HTML; to swap one, replace the file in `web/` with the same name.

People reflect the parish: mostly white, Asian and Filipino, with some Latino families.
`contact-sheet-inner-pages.jpg` shows this set.

| Page slot | Web file | Notes |
|---|---|---|
| `about-hero`, `sacraments-hero`, `faith-formation-hero`, `ministries-hero`, `events-hero`, `support-hero` | `<slot>-960.webp` (960×1200, 4:5) | Subjects centered, so the 16:9 phone crop works too |
| `sacrament-baptism`, `-reconciliation`, `-eucharist`, `-confirmation`, `-marriage`, `-anointing`, `-holy-orders` | `<slot>-1200.webp` (1200×900, 4:3) | |
| `formation-children-families`, `-youth`, `-adults`, `-becoming-catholic` | `<slot>-1200.webp` | |
| `ministry-welcome`, `ministry-service` | `<slot>-1200.webp` | |
| `events-weekend-mass` | `events-weekend-mass-1200.webp` | |
| Events page `event-*` and Support Us page `support-*` | reuse the homepage files above | |

The remaining ministry images—`ministry-worship` (music rehearsal), `ministry-care` (Communion to the homebound), and `ministry-parish-support` (grounds work day)—are now stored in `images/generated/` and used on the Ministries page. All three use the parish's chosen `*-final.webp` images.
Not generated on purpose: the `staff-*` portraits. Those are real photos in `images/staff/`, taken from the current Staff Directory (Timothy Valderrama's is his own).

Generated but not wired in: `about-mission.jpg` / `web/about-mission-1200.webp` (parishioners over coffee under oak trees after Mass), made for the About Us mission section. Unused: the parish chose its own image for that slot, `images/generated/about-church-exterior-welcome-final.webp` (families arriving at the church with the priests greeting them at the door).
