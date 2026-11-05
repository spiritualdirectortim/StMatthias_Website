#!/usr/bin/env python3
"""Regenerate the shared and data-driven regions of the St. Matthias site.

The site is plain static HTML. Shared pieces (header, mobile drawer, footer) and
data-driven pieces (events, giving options) live between marker comments:

    <!-- build:NAME -->  ...generated...  <!-- /build:NAME -->

Sources (edit these, never the generated HTML):
    data/site.json     parish facts, navigation, footer
    data/events.json   every event on the site
    data/giving.json   every giving option on the site

Usage:
    python3 scripts/build.py           rewrite the pages
    python3 scripts/build.py --check   exit 1 if any page is out of date
    python3 scripts/build.py --today 2026-11-04   build as of a given date

Standard library only. Python 3.8+.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# page file -> nav id used for aria-current (None for none)
PAGES = {
    "index.html": None,
    "about-us/index.html": "about-us",
    "sacraments/index.html": "sacraments",
    "faith-formation/index.html": "faith-formation",
    "ministries/index.html": "ministries",
    "events/index.html": "events",
    "support-us/index.html": "support-us",
    "privacy/index.html": None,
}

HERO_LIMIT = 3          # slides shown in the homepage hero
HERO_CANDIDATES = 5     # slides rendered so expired ones can be replaced at runtime
UPCOMING_LIMIT = 5      # cards shown in "Upcoming at St. Matthias"
UPCOMING_CANDIDATES = 10

HERO_COLORS = ["ph-navy", "ph-moss", "ph-clay", "ph-navy", "ph-moss"]

CHEVRON = (
    '<svg class="chev" viewBox="0 0 12 12" width="12" height="12" aria-hidden="true" focusable="false">'
    '<path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)
NEW_TAB = '<span class="visually-hidden"> (opens in a new tab)</span>'


def e(text):
    return escape(str(text), quote=True)


# ---------------------------------------------------------------- photos

# Web-ready photos, named by image slot: <name>-<width>.webp (see that folder's README).
# A slot with no matching file keeps its solid-colour placeholder.
PHOTO_DIR = "images/GeminiGeneratedImages/web"
PHOTO_SIZES = {          # file widths available per kind, and their height at the largest width
    "hero": ([1200, 2400], 1340),
    "event": ([960], 540),
    "giving": ([800], 600),
}


def photo(cls, slot, name, kind, sizes="100vw", eager=False):
    """An <img> for `name` if its files exist, else the original placeholder <div>."""
    widths, height = PHOTO_SIZES[kind]
    files = [(w, "%s/%s-%d.webp" % (PHOTO_DIR, name, w)) for w in widths]
    if not all((ROOT / f).exists() for _, f in files):
        return '<div class="%s" data-image-slot="%s" aria-hidden="true"></div>' % (cls, e(slot))
    srcset = ""
    if len(files) > 1:
        srcset = ' srcset="%s" sizes="%s"' % (", ".join("/%s %dw" % (f, w) for w, f in files), sizes)
    loading = ' fetchpriority="high"' if eager else ' loading="lazy"'
    return ('<img class="%s" data-image-slot="%s" src="/%s"%s width="%d" height="%d" alt="" decoding="async"%s>'
            % (cls, e(slot), files[-1][1], srcset, files[-1][0], height, loading))


def load(name):
    with open(DATA / name, encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------- dates

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def parse(ts):
    return datetime.fromisoformat(ts)


def fmt_time(dt):
    if dt.hour == 12 and dt.minute == 0:
        return "noon"
    hour = dt.hour % 12 or 12
    return "%d:%02d %s" % (hour, dt.minute, "a.m." if dt.hour < 12 else "p.m.")


def fmt_range(start, end):
    same_half = (start.hour < 12) == (end.hour < 12)
    if same_half and not (end.hour == 12 and end.minute == 0):
        return "%s–%s" % (fmt_time(start).rsplit(" ", 1)[0], fmt_time(end))
    return "%s–%s" % (fmt_time(start), fmt_time(end))


def fmt_date(dt, year):
    text = "%s, %s %d" % (DAYS[dt.weekday()], MONTHS[dt.month - 1], dt.day)
    if dt.year != year:
        text += ", %d" % dt.year
    return text


def when(event, year):
    """Return (date_label, time_label, iso_start or None, iso_end or None)."""
    if event.get("recurrence"):
        return event["recurrence"], event.get("time", ""), None, None
    sessions = [(parse(s["start"]), parse(s["end"]) if s.get("end") else None, s.get("showEnd"))
                for s in event["sessions"]]
    first, last = sessions[0], sessions[-1]
    end = last[1] or last[0] + timedelta(hours=1)
    dates = {s[0].date() for s in sessions}

    def t(s):
        return fmt_range(s[0], s[1]) if (s[2] and s[1]) else fmt_time(s[0])

    if len(dates) == 1:
        date_label = fmt_date(first[0], year)
        times = [t(s) for s in sessions]
        time_label = times[0] if len(times) == 1 else ", ".join(times[:-1]) + " and " + times[-1]
    else:
        a, b = first[0], last[0]
        if a.month == b.month and a.year == b.year:
            date_label = "%s %d–%d" % (MONTHS[a.month - 1], a.day, b.day)
        else:
            date_label = "%s %d – %s %d" % (MONTHS[a.month - 1], a.day, MONTHS[b.month - 1], b.day)
        if a.year != year:
            date_label += ", %d" % a.year
        # Repeating weekly sessions (e.g. two weekends of Masses) list each weekday-time once.
        labels = []
        for s in sessions:
            label = "%s %s" % (DAYS[s[0].weekday()], t(s))
            if label not in labels:
                labels.append(label)
        time_label = " · ".join(labels)
    return date_label, time_label, first[0].isoformat(), end.isoformat()


def event_end(event):
    if event.get("recurrence"):
        return None
    last = event["sessions"][-1]
    return parse(last["end"]) if last.get("end") else parse(last["start"]) + timedelta(hours=1)


def event_start(event):
    return None if event.get("recurrence") else parse(event["sessions"][0]["start"])


def upcoming(events, now):
    """Published events that have not ended, recurring first, then by date."""
    out = []
    for ev in events:
        if ev.get("status") != "verified":
            raise SystemExit("events.json: '%s' is not verified; only verified events are published." % ev.get("id"))
        end = event_end(ev)
        if end is not None and end < now:
            continue
        out.append(ev)
    recurring = [ev for ev in out if ev.get("recurrence")]
    dated = sorted((ev for ev in out if not ev.get("recurrence")), key=event_start)
    return recurring + dated


def end_attr(ev):
    end = event_end(ev)
    return ' data-event-end="%s"' % e(end.isoformat()) if end else ""


def event_href(ev):
    return "/events/#%s" % ev["id"]


def time_html(date_label, iso):
    if iso:
        return '<time datetime="%s">%s</time>' % (e(iso), e(date_label))
    return e(date_label)


# ---------------------------------------------------------------- navigation

def nav_children(item, giving):
    if item.get("childrenFrom") == "giving":
        # Every active giving option, linked to its card on the Support Us page so visitors
        # stay on the parish site until they choose to give.
        return [{"label": opt["name"], "href": "/support-us/#%s" % opt["id"]} for opt in active_giving(giving)]
    return item.get("children", [])


def is_external(href):
    return href.startswith("http")


def render_header(site, giving, current):
    p = site["parish"]
    items = []
    for item in site["nav"]:
        kids = nav_children(item, giving)
        cls = ["nav-item"]
        if kids:
            cls.append("has-sub")
        if item.get("style"):
            cls.append("nav-item-" + item["style"])
        current_attr = ' aria-current="page"' if current == item["id"] else ""
        if item.get("style") == "external":
            link = ('<a class="nav-link nav-external" href="%s" target="_blank" rel="noopener">%s%s</a>'
                    % (e(item["href"]), e(item["label"]), NEW_TAB))
        else:
            link = '<a class="nav-link" href="%s"%s>%s</a>' % (e(item["href"]), current_attr, e(item["label"]))
        parts = ['<li class="%s">' % " ".join(cls), link]
        if kids:
            sub_id = "sub-" + item["id"]
            parts.append('<button class="sub-toggle" type="button" aria-expanded="false" aria-controls="%s">'
                         '<span class="visually-hidden">%s menu</span>%s</button>' % (sub_id, e(item["label"]), CHEVRON))
            parts.append('<ul class="subnav" id="%s">' % sub_id)
            for kid in kids:
                parts.append("<li>%s</li>" % ext_link(kid["label"], kid["href"]))
            parts.append("</ul>")
        parts.append("</li>")
        items.append("".join(parts))

    drawer_items = []
    for i, item in enumerate(site["nav"]):
        kids = nav_children(item, giving)
        cls = ["drawer-item"]
        if item.get("style"):
            cls.append("drawer-item-" + item["style"])
        current_attr = ' aria-current="page"' if current == item["id"] else ""
        if item.get("style") == "external":
            link = ('<a href="%s" target="_blank" rel="noopener">%s%s</a>'
                    % (e(item["href"]), e(item["label"]), NEW_TAB))
        else:
            link = '<a href="%s"%s>%s</a>' % (e(item["href"]), current_attr, e(item["label"]))
        row = ['<li class="%s"><div class="drawer-row">' % " ".join(cls), link]
        if kids:
            sub_id = "dsub-" + item["id"]
            row.append('<button class="drawer-sub-toggle" type="button" aria-expanded="false" aria-controls="%s">'
                       '<span class="visually-hidden">Show %s links</span>%s</button>' % (sub_id, e(item["label"]), CHEVRON))
        row.append("</div>")
        if kids:
            row.append('<ul class="drawer-sub" id="dsub-%s" hidden>' % item["id"])
            for kid in kids:
                row.append("<li>%s</li>" % ext_link(kid["label"], kid["href"]))
            row.append("</ul>")
        row.append("</li>")
        drawer_items.append("".join(row))

    pills = "".join(
        '<span class="pill"><span class="pill-day">%s</span><span class="pill-time">%s</span></span>'
        % (e(m["day"]), e(m["time"])) for m in p["massTimes"])

    return "\n".join([
        '<header class="site-header">',
        '  <div class="container header-inner">',
        '    <a class="brand" href="/" aria-label="%s home" data-load style="--d:0ms">' % e(p["shortName"]),
        '      <img class="brand-mark" src="/images/logo-icon.png" width="256" height="256" alt="">',
        '      <span class="brand-text"><span class="brand-name">%s</span><span class="brand-tag">%s</span></span>'
        % (e(p["shortName"]), e(p["tagline"])),
        "    </a>",
        '    <nav class="nav-primary" aria-label="Primary" data-load style="--d:120ms">',
        '      <ul class="nav-list">',
        "\n".join("        " + li for li in items),
        "      </ul>",
        "    </nav>",
        '    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Open menu" data-load style="--d:120ms">',
        "      <span></span><span></span><span></span>",
        "    </button>",
        "  </div>",
        "</header>",
        "",
        '<div class="drawer" id="drawer" aria-hidden="true">',
        '  <div class="drawer-scrim"></div>',
        '  <div class="drawer-panel" role="dialog" aria-modal="true" aria-label="Menu">',
        '    <div class="drawer-top">',
        '      <a class="drawer-title" href="/">%s</a>' % e(p["shortName"]),
        '      <button class="drawer-close" type="button" aria-label="Close menu">',
        '        <svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 4l12 12M16 4L4 16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
        "      </button>",
        "    </div>",
        '    <nav class="drawer-nav" aria-label="Mobile">',
        "      <ul>",
        "\n".join("        " + li for li in drawer_items),
        "      </ul>",
        "    </nav>",
        '    <div class="drawer-meta">',
        "      <strong>Mass this weekend</strong>",
        '      <div class="pills">%s</div>' % pills,
        '      <address>%s<br>%s, %s %s<br><a href="%s">%s</a></address>'
        % (e(p["street"]), e(p["city"]), e(p["region"]), e(p["postalCode"]), e(p["phoneHref"]), e(p["phone"])),
        "    </div>",
        "  </div>",
        "</div>",
    ])


def ext_link(label, href, cls=None):
    c = ' class="%s"' % cls if cls else ""
    if is_external(href):
        return '<a%s href="%s" target="_blank" rel="noopener">%s%s</a>' % (c, e(href), e(label), NEW_TAB)
    return '<a%s href="%s">%s</a>' % (c, e(href), e(label))


def render_footer(site, year):
    p = site["parish"]
    legal = site.get("legal", {})
    nav_by_id = {item["id"]: item for item in site["nav"]}
    explore = "".join('<li><a href="%s">%s</a></li>' % (e(nav_by_id[i]["href"]), e(nav_by_id[i]["label"]))
                      for i in site["footer"]["explore"])
    action = "".join("<li>%s</li>" % ext_link(a["label"], a["href"]) for a in site["footer"]["takeAction"])
    times = "".join("<li><span>%s</span><strong>%s</strong></li>" % (e(m["day"]), e(m["time"])) for m in p["massTimes"])
    hours = ""
    if p.get("officeHours"):
        hours = "<br>Office hours: %s" % e(p["officeHours"])
    social = " &middot; ".join(ext_link(s["label"], s["url"]) for s in site["social"])

    identity = []
    if legal.get("legalName"):
        identity.append("<span>%s</span>" % e(legal["legalName"]))
    if legal.get("nonprofitStatus"):
        identity.append("<span>%s</span>" % e(legal["nonprofitStatus"]))
    if legal.get("ein"):
        identity.append("<span>EIN %s</span>" % e(legal["ein"]))
    identity_html = ('<p class="footer-legal">%s</p>' % " &middot; ".join(identity)) if identity else \
        "<!-- Legal identity: set legalName, nonprofitStatus, and ein in data/site.json once confirmed. -->"

    return "\n".join([
        '<footer class="site-footer on-dark">',
        '  <div class="container">',
        '    <div class="footer-grid">',
        '      <div class="footer-brand">',
        '        <img class="footer-badge" src="/images/logo-icon.png" width="256" height="256" alt="St. Matthias Parish logo" loading="lazy">',
        "        <div>",
        '          <h2>Contact</h2>',
        "          <strong>%s</strong>" % e(p["name"]),
        "          <address>%s<br>%s, %s %s<br>" % (e(p["street"]), e(p["city"]), e(p["region"]), e(p["postalCode"])),
        '            <a href="%s">%s</a><br>' % (e(p["phoneHref"]), e(p["phone"])),
        '            <a href="mailto:%s">%s</a>%s</address>' % (e(p["email"]), e(p["email"]), hours),
        "        </div>",
        "      </div>",
        "      <div>",
        "        <h2>Mass</h2>",
        '        <ul class="footer-times">%s</ul>' % times,
        '        <ul class="footer-links footer-links-tight">',
        "          <li>%s</li>" % ext_link("Get directions", p["directionsUrl"]),
        "          <li>%s</li>" % ext_link("Watch the livestream", p["livestreamUrl"]),
        "        </ul>",
        "      </div>",
        "      <div>",
        "        <h2>Explore</h2>",
        '        <ul class="footer-links">%s</ul>' % explore,
        "      </div>",
        "      <div>",
        "        <h2>Take Action</h2>",
        '        <ul class="footer-links">%s</ul>' % action,
        "      </div>",
        "    </div>",
        '    <div class="footer-bottom">',
        '      <div class="footer-identity">',
        "        <p>&copy; %d %s &middot; %s</p>" % (year, e(p["shortName"]), e(p["archdiocese"])),
        "        " + identity_html,
        "      </div>",
        '      <p class="footer-social">%s</p>' % social,
        "    </div>",
        "  </div>",
        "</footer>",
    ])


# ---------------------------------------------------------------- events

def render_hero(events, year):
    featured = [ev for ev in events if ev.get("featured") and not ev.get("recurrence")][:HERO_CANDIDATES]
    out = []
    for i, ev in enumerate(featured):
        date_label, time_label, iso, _ = when(ev, year)
        first = i == 0
        load = (lambda d: ' data-load style="--d:%dms"' % d) if first else (lambda d: "")
        attrs = ' data-hero-motion="%s"' % ("pan" if first else "zoom")
        cls = "hero-scene is-active" if first else "hero-scene"
        hidden = "" if first else ' aria-hidden="true"'
        if i >= HERO_LIMIT:
            hidden += " hidden"
        title_attr = ' data-split style="--d:320ms"' if first else ""
        out.append("\n".join([
            '<article class="%s" data-scene%s%s%s aria-labelledby="hero-event-%s">' % (cls, attrs, end_attr(ev), hidden, e(ev["id"])),
            "  " + photo("hero-scene-media media-ph %s" % HERO_COLORS[i % len(HERO_COLORS)],
                         "featured-event-%d" % (i + 1), "hero-%s" % ev["id"], "hero", eager=first),
            '  <div class="hero-scene-shade"></div>',
            '  <div class="container hero-scene-copy">',
            '    <p class="overline"%s>%s</p>' % (load(200), e(ev["category"])),
            '    <h2 class="display" id="hero-event-%s"%s>%s</h2>' % (e(ev["id"]), title_attr, e(ev["title"])),
            '    <p class="hero-event-meta"%s><strong>%s</strong><span>%s</span><span>%s</span></p>'
            % (load(760), time_html(date_label, iso), e(time_label), e(ev["location"])),
            '    <p class="lede"%s>%s</p>' % (load(900), e(ev["description"])),
            '    <div class="btn-row"%s><a class="btn btn-primary" href="%s">View Event<span class="visually-hidden">: %s</span></a></div>'
            % (load(1050), e(event_href(ev)), e(ev["title"])),
            "  </div>",
            "</article>",
        ]))
    fallback_hidden = " hidden" if featured else ""
    out.append("\n".join([
        '<article class="hero-scene%s" data-scene-fallback%s aria-labelledby="hero-fallback-title">' % ("" if featured else " is-active", fallback_hidden),
        "  " + photo("hero-scene-media media-ph ph-navy", "featured-event-fallback", "hero-weekend-mass", "hero",
                     eager=not featured),
        '  <div class="hero-scene-shade"></div>',
        '  <div class="container hero-scene-copy">',
        '    <p class="overline">Join us this weekend</p>',
        '    <h2 class="display" id="hero-fallback-title">Mass at St. Matthias</h2>',
        '    <p class="hero-event-meta"><strong>Saturday 5:00 p.m.</strong><span>Sunday 9:45 a.m.</span><span>St. Matthias Church</span></p>',
        '    <div class="btn-row"><a class="btn btn-primary" href="/events/">See Upcoming Events</a></div>',
        "  </div>",
        "</article>",
    ]))
    return "\n".join(out), min(len(featured), HERO_LIMIT)


def render_upcoming(events, year):
    rest = [ev for ev in events if not ev.get("featured")][:UPCOMING_CANDIDATES]
    cards = []
    for i, ev in enumerate(rest):
        date_label, time_label, iso, _ = when(ev, year)
        hidden = " hidden" if i >= UPCOMING_LIMIT else ""
        cards.append("\n".join([
            '<article class="ministry-card"%s%s>' % (end_attr(ev), hidden),
            "  " + photo("card-media media-ph", "event-%s" % ev["id"], "event-%s" % ev["id"], "event"),
            "  <div>",
            "    <span>%s</span>" % e(ev["category"]),
            '    <h3><a class="card-link" href="%s">%s</a></h3>' % (e(event_href(ev)), e(ev["title"])),
            '    <p class="card-when">%s &middot; %s</p>' % (time_html(date_label, iso), e(time_label)),
            '    <p class="card-desc">%s</p>' % e(ev["description"]),
            "  </div>",
            "</article>",
        ]))
    count = min(len(rest), UPCOMING_LIMIT)
    empty_hidden = "" if count == 0 else " hidden"
    grid = '<div class="container ministry-grid" data-upcoming data-count="%d">\n%s\n</div>' % (count, "\n".join(cards))
    empty = ('<p class="container upcoming-empty" data-upcoming-empty%s>New events are added regularly. '
             '<a class="link" href="/events/">See all upcoming events</a> or call the parish office.</p>' % empty_hidden)
    return grid + "\n" + empty


def render_events_page(events, year, parish):
    dated = [ev for ev in events if not ev.get("recurrence")]
    recurring = [ev for ev in events if ev.get("recurrence")]

    def item(ev):
        date_label, time_label, iso, _ = when(ev, year)
        action = ""
        if ev.get("action"):
            a = ev["action"]
            action = '<p class="event-action">%s</p>' % ext_link(a["label"], a["url"], cls="link-arrow")
        if ev.get("registration"):
            r = ev["registration"]
            action += '<p class="event-action">%s</p>' % ext_link(r["label"], r["url"], cls="link-arrow")
        return "\n".join([
            '<article class="event-item" id="%s"%s>' % (e(ev["id"]), end_attr(ev)),
            "  " + photo("event-item-media media-ph", "event-%s" % ev["id"], "event-%s" % ev["id"], "event"),
            '  <div class="event-item-body">',
            '    <p class="eyebrow">%s</p>' % e(ev["category"]),
            "    <h3>%s</h3>" % e(ev["title"]),
            '    <dl class="event-facts">',
            "      <div><dt>When</dt><dd>%s &middot; %s</dd></div>" % (time_html(date_label, iso), e(time_label)),
            "      <div><dt>Where</dt><dd>%s</dd></div>" % e(ev["location"]),
            "    </dl>",
            "    <p>%s</p>" % e(ev["description"]),
            "    " + action if action else "",
            "  </div>",
            "</article>",
        ])

    parts = ['<section class="section" aria-labelledby="coming-up-title">', '<div class="container">',
             '<div class="section-head"><p class="overline">Coming up</p><h2 class="h-xl" id="coming-up-title">Mark your calendar.</h2></div>',
             '<div class="event-list" data-event-list>']
    parts += [item(ev) for ev in dated]
    parts.append("</div>")
    parts.append('<p class="event-empty" data-events-empty%s>New events are being scheduled. Call the parish office at '
                 '<a href="%s">%s</a> or check back soon.</p>'
                 % (" hidden" if dated else "", e(parish["phoneHref"]), e(parish["phone"])))
    parts += ["</div>", "</section>"]
    if recurring:
        parts += ['<section class="section section-alt" aria-labelledby="regular-title">', '<div class="container">',
                  '<div class="section-head"><p class="overline">Every week and every month</p><h2 class="h-xl" id="regular-title">Regular gatherings.</h2></div>',
                  '<div class="event-list">']
        parts += [item(ev) for ev in recurring]
        parts += ["</div>", "</div>", "</section>"]
    return "\n".join(p for p in parts if p != "")


# ---------------------------------------------------------------- giving

def active_giving(giving):
    opts = [o for o in giving["options"] if o.get("active")]
    for o in opts:
        if not o["url"].startswith("https://"):
            raise SystemExit("giving.json: '%s' must use an HTTPS donation URL." % o["id"])
    opts.sort(key=lambda o: (not o.get("primary"), giving["options"].index(o)))
    if not opts or not opts[0].get("primary"):
        raise SystemExit("giving.json: the Regular Collection must be active and primary.")
    return opts


def fan(count):
    """Fan layout for the stacked giving posters (matches the original five-card fan)."""
    odd_rise = [0, 0.8, 2.4, 3.6]      # rem; five cards reproduce the original 0 / .8 / 2.4 fan
    even_rise = [0.4, 1.6, 3.0]
    spacing = 21.5 if count >= 4 else 24
    out = []
    for i in range(count):
        offset = i - (count - 1) / 2
        step = int(abs(offset))
        y = (even_rise if count % 2 == 0 else odd_rise)[min(step, 2)]
        out.append({
            "x": "%.2f%%" % (50 + offset * spacing),
            "y": "%grem" % y,
            "z": count - step,
            "tilt": "%gdeg" % (offset * 4),
        })
    return out


def render_home_giving(giving):
    opts = active_giving(giving)
    fallback_layout = fan(min(len(opts), 5))
    posters = []
    for i, opt in enumerate(opts):
        fallback = fallback_layout[min(i, len(fallback_layout) - 1)]
        hidden = " hidden" if i >= 5 else ""
        posters.append("\n".join([
            '<article class="event-poster" data-carousel-card%s style="--fan-x:%s;--fan-y:%s;--fan-z:%d;--fan-tilt:%s">'
            % (hidden, fallback["x"], fallback["y"], fallback["z"], fallback["tilt"]),
            "  " + photo("card-media media-ph %s" % ("ph-clay" if i % 2 == 0 else "ph-slate"),
                         opt["imageSlot"], opt["imageSlot"], "giving"),
            '  <div class="poster-body">',
            '    <span class="poster-label">%s</span>' % e(opt["label"]),
            "    <h3>%s</h3>" % e(opt["name"]),
            "    <p>%s</p>" % e(opt["summary"]),
            "    %s" % give_link(opt, "poster-action"),
            "  </div>",
            "</article>",
        ]))
    dots = "".join(
        '<button type="button" data-support-dot data-index="%d" aria-label="Show %s"%s></button>'
        % (i, e(opt["name"]), ' aria-current="true"' if i == 0 else "")
        for i, opt in enumerate(opts)
    )
    return "\n".join([
        '<div class="event-stack" data-support-carousel data-count="%d" tabindex="0" aria-label="Giving options carousel">' % len(opts),
        "\n".join(posters),
        '  <div class="support-carousel-controls">',
        '    <button class="support-carousel-arrow support-carousel-prev" type="button" data-support-prev aria-label="Show previous giving option"><span aria-hidden="true">&#8592;</span></button>',
        '    <div class="support-carousel-pagination" aria-label="Choose a giving option">%s</div>' % dots,
        '    <button class="support-carousel-arrow support-carousel-next" type="button" data-support-next aria-label="Show next giving option"><span aria-hidden="true">&#8594;</span></button>',
        "  </div>",
        '  <p class="visually-hidden" data-support-status aria-live="polite">%s, 1 of %d</p>' % (e(opts[0]["name"]), len(opts)),
        "</div>",
    ])


def give_link(opt, cls):
    """A giving button. Opens the Vanco page in the same tab so the site never vanishes
    behind a new tab; Back returns to the parish site."""
    return '<a class="%s" href="%s">%s</a>' % (cls, e(opt["url"]), e(opt["actionLabel"]))


GROUP_PH = ["ph-1", "ph-2", "ph-3", "ph-5", "ph-moss", "ph-clay"]


def support_groups(giving):
    """Non-featured active options, bucketed by data/giving.json -> groups, in data order."""
    rest = [opt for opt in active_giving(giving) if not opt.get("featured")]
    groups = []
    for g in giving.get("groups", []):
        items = [opt for opt in rest if opt.get("group") == g["id"]]
        if items:
            groups.append(dict(g, items=items))
    known = {g["id"] for g in giving.get("groups", [])}
    loose = [opt for opt in rest if opt.get("group") not in known]
    if loose:
        groups.append({"id": "more", "title": "More collections", "intro": "", "items": loose})
    return groups


def render_support_jump(giving):
    links = [("#start", "Where to start")]
    links += [("#give-%s" % g["id"], g["title"]) for g in support_groups(giving)]
    links.append(("#questions", "Questions"))
    return "\n".join('          <a href="%s">%s</a>' % (e(h), e(t)) for h, t in links)


def render_support_options(giving, parish):
    opts = active_giving(giving)
    featured = [opt for opt in opts if opt.get("featured")] or opts[:1]
    provider = e(giving["provider"]["name"])
    out = [
        '<section class="page-section give-start" id="start" aria-labelledby="start-title">',
        '  <div class="container">',
        '    <div class="section-head">',
        '      <p class="overline">Where to start</p>',
        '      <h2 class="h-xl" id="start-title">The gifts that keep our doors open.</h2>',
        '      <p class="copy">Not sure where to give? Start here. Every gift is processed securely by %s, the parish&rsquo;s online giving provider.</p>' % provider,
        "    </div>",
        '    <div class="give-feature-grid">',
    ]
    for i, opt in enumerate(featured):
        details = "\n".join("          <p>%s</p>" % e(d) for d in opt["details"])
        out += [
            '      <article class="give-feature%s" id="%s" aria-labelledby="%s-title">'
            % (" is-primary" if opt.get("primary") else "", e(opt["id"]), e(opt["id"])),
            "        " + photo("give-feature-media media-ph %s" % ("ph-clay" if i % 2 == 0 else "ph-slate"),
                                 opt["imageSlot"], opt["imageSlot"], "giving"),
            '        <div class="give-feature-body">',
            '          <p class="eyebrow">%s</p>' % e(opt["label"]),
            '          <h3 id="%s-title">%s</h3>' % (e(opt["id"]), e(opt["name"])),
            details,
            '          <div class="btn-row">%s</div>' % give_link(opt, "btn btn-primary"),
            "        </div>",
            "      </article>",
        ]
    out += ["    </div>", "  </div>", "</section>"]

    groups = support_groups(giving)
    count = sum(len(g["items"]) for g in groups)
    if groups:
        out += [
            '<section class="page-section section-alt give-ways" id="ways" aria-labelledby="ways-title">',
            '  <div class="container">',
            '    <div class="section-head">',
            '      <p class="overline">More ways to give</p>',
            '      <h2 class="h-xl" id="ways-title">Give where it means the most to you.</h2>',
            '      <p class="copy">%s more collections and offerings, from Mass intentions to missionaries abroad. Each button opens that gift&rsquo;s secure %s page.</p>'
            % (NUMBER_WORDS.get(count, str(count)).capitalize(), provider),
            "    </div>",
        ]
        n = 0
        for g in groups:
            out += [
                '    <div class="give-group" id="give-%s" aria-labelledby="give-%s-title">' % (e(g["id"]), e(g["id"])),
                '      <div class="give-group-head">',
                '        <h3 id="give-%s-title">%s</h3>' % (e(g["id"]), e(g["title"])),
            ]
            if g.get("intro"):
                out.append("        <p>%s</p>" % e(g["intro"]))
            out += ["      </div>", '      <ul class="give-cards" role="list">']
            for opt in g["items"]:
                out += [
                    '        <li class="give-card" id="%s">' % e(opt["id"]),
                    "          " + photo("give-card-media media-ph %s" % GROUP_PH[n % len(GROUP_PH)],
                                         opt["imageSlot"], opt["imageSlot"], "giving"),
                    '          <div class="give-card-body">',
                    '            <p class="eyebrow">%s</p>' % e(opt["label"]),
                    "            <h4>%s</h4>" % e(opt["name"]),
                    "            <p>%s</p>" % e(opt["summary"]),
                    "            %s" % give_link(opt, "btn btn-secondary btn-sm"),
                    "          </div>",
                    "        </li>",
                ]
                n += 1
            out += ["      </ul>", "    </div>"]
        out += ["  </div>", "</section>"]
    return "\n".join(out)


NUMBER_WORDS = {2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                9: "nine", 10: "ten", 11: "eleven", 12: "twelve"}


def render_legal(site):
    legal = site.get("legal", {})
    rows = []
    if legal.get("legalName"):
        rows.append("<div><dt>Legal name</dt><dd>%s</dd></div>" % e(legal["legalName"]))
    if legal.get("nonprofitStatus"):
        rows.append("<div><dt>Nonprofit status</dt><dd>%s</dd></div>" % e(legal["nonprofitStatus"]))
    if legal.get("ein"):
        rows.append("<div><dt>EIN</dt><dd>%s</dd></div>" % e(legal["ein"]))
    if not rows:
        return "<!-- Legal identity rows appear here once legalName, nonprofitStatus, and ein are set in data/site.json. -->"
    return "\n".join(rows)


# ---------------------------------------------------------------- main

def replace_region(text, name, content, path):
    pattern = re.compile(r"(<!-- build:%s -->)(.*?)(<!-- /build:%s -->)" % (re.escape(name), re.escape(name)), re.S)
    if not pattern.search(text):
        raise SystemExit("%s: missing <!-- build:%s --> region" % (path, name))
    return pattern.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(3), text, count=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--today", help="YYYY-MM-DD (defaults to now)")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    if args.today:
        now = datetime.fromisoformat(args.today + "T00:00:00-08:00")
    year = now.astimezone(timezone(timedelta(hours=-8))).year

    site, events_doc, giving = load("site.json"), load("events.json"), load("giving.json")
    events = upcoming(events_doc["events"], now)

    hero_html, hero_count = render_hero(events, year)
    shared = {
        "footer": render_footer(site, year),
    }
    regions_by_page = {
        "index.html": {
            "home-hero": hero_html,
            "home-hero-count": '<span data-scene-total>%02d</span>' % max(hero_count, 1),
            "home-upcoming": render_upcoming(events, year),
            "home-giving": render_home_giving(giving),
        },
        "events/index.html": {"events-list": render_events_page(events, year, site["parish"])},
        "support-us/index.html": {
            "support-jump": render_support_jump(giving),
            "support-options": render_support_options(giving, site["parish"]),
        },
        "about-us/index.html": {"legal": render_legal(site)},
    }

    stale = []
    for rel, current in PAGES.items():
        path = ROOT / rel
        if not path.exists():
            raise SystemExit("missing page: %s" % rel)
        original = path.read_text(encoding="utf-8")
        text = replace_region(original, "header", render_header(site, giving, current), rel)
        for name, content in shared.items():
            text = replace_region(text, name, content, rel)
        for name, content in regions_by_page.get(rel, {}).items():
            text = replace_region(text, name, content, rel)
        if text != original:
            stale.append(rel)
            if not args.check:
                path.write_text(text, encoding="utf-8")

    if args.check:
        if stale:
            print("Out of date: " + ", ".join(stale))
            return 1
        print("All pages are up to date.")
        return 0
    print("Updated: " + (", ".join(stale) if stale else "nothing (already current)"))
    print("Published events: %d (hero %d). Active giving options: %d."
          % (len(events), hero_count, len(active_giving(giving))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
