// Header scroll state + mobile drawer. No dependencies.
(function () {
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  var drawer = document.getElementById("drawer");
  if (!header) return;

  // Keep the header light over the cinematic hero, then settle into parchment.
  var solid = false;
  function onScroll() {
    var hero = document.querySelector(".scroll-hero");
    var threshold = hero ? Math.max(40, hero.offsetHeight - window.innerHeight - 24) : 40;
    var next = window.scrollY > threshold;
    if (next !== solid) {
      solid = next;
      header.classList.toggle("is-solid", solid);
    }
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  onScroll();

  if (!toggle || !drawer) return;

  var closeBtn = drawer.querySelector(".drawer-close");
  var scrim = drawer.querySelector(".drawer-scrim");
  var focusable = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])';
  var lastFocus = null;
  var open = false;

  drawer.querySelectorAll(".drawer-nav li").forEach(function (li, i) {
    li.style.setProperty("--i", i);
  });

  function setOpen(next) {
    if (next === open) return;
    open = next;
    drawer.classList.toggle("is-open", open);
    drawer.setAttribute("aria-hidden", String(!open));
    toggle.setAttribute("aria-expanded", String(open));
    document.documentElement.classList.toggle("drawer-open", open);
    if (open) {
      lastFocus = document.activeElement;
      window.setTimeout(function () { closeBtn && closeBtn.focus(); }, 60);
    } else if (lastFocus) {
      lastFocus.focus();
    }
  }

  // Keep unfinished internal pages from navigating away from this concept.
  var pendingRoutes = [
    "/plan-a-visit/",
    "/worship-and-sacraments/",
    "/community/",
    "/community/calendar/",
    "/preschool/",
    "/about/",
    "/about/bulletins/",
    "/give/"
  ];
  var toast = document.getElementById("coming-soon-toast");
  var toastTimer = null;

  function pendingRouteFor(href) {
    if (!href || href.charAt(0) !== "/") return null;
    var path = href.split("#")[0];
    return pendingRoutes.indexOf(path) !== -1 ? path : null;
  }

  document.querySelectorAll('a[href^="/"]').forEach(function (link) {
    if (!pendingRouteFor(link.getAttribute("href"))) return;
    link.classList.add("is-coming-soon");
    link.setAttribute("title", "This page is coming soon");
  });

  document.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest("a[href]");
    if (!link || !pendingRouteFor(link.getAttribute("href"))) return;
    event.preventDefault();
    setOpen(false);
    if (!toast) return;
    var label = (link.textContent || "This page").replace(/\s+/g, " ").trim();
    toast.textContent = label + " is coming soon. You are still on the homepage.";
    toast.classList.add("is-visible");
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(function () {
      toast.classList.remove("is-visible");
    }, 3600);
  });

  toggle.addEventListener("click", function () { setOpen(!open); });
  closeBtn && closeBtn.addEventListener("click", function () { setOpen(false); });
  scrim && scrim.addEventListener("click", function () { setOpen(false); });
  drawer.querySelectorAll("a[href]").forEach(function (a) {
    a.addEventListener("click", function () { setOpen(false); });
  });

  document.addEventListener("keydown", function (e) {
    if (!open) return;
    if (e.key === "Escape") { setOpen(false); return; }
    if (e.key !== "Tab") return;
    var items = drawer.querySelectorAll(focusable);
    var first = items[0], last = items[items.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });

  var mq = window.matchMedia("(min-width: 1024px)");
  var onChange = function (e) { if (e.matches) setOpen(false); };
  mq.addEventListener ? mq.addEventListener("change", onChange) : mq.addListener(onChange);
})();
