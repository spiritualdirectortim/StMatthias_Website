// WebDesigner starter motion script. Pairs with starter.css.
// - Adds html.js so CSS can opt motion in (content is visible without this script).
// - Adds html.is-ready after fonts load so hero entrances do not jump mid-animation.
// - Reveals [data-reveal] sections once, when ~10% in view, staggering .reveal-child.
// - Toggles header .is-top / .is-hidden (transparent over hero; hide on scroll down, show on scroll up).
// - Does none of the above when the visitor prefers reduced motion.
(function () {
  var doc = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  doc.classList.add('js');
  if (reduce.matches) doc.classList.add('reduce');

  // hero entrance after fonts are ready (800ms safety timeout)
  var ready = false;
  function markReady() { if (ready) return; ready = true; doc.classList.add('is-ready'); }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { setTimeout(markReady, 40); });
  setTimeout(markReady, 800);

  // scroll reveals
  var sections = Array.prototype.slice.call(document.querySelectorAll('[data-reveal]'));
  sections.forEach(function (el) {
    Array.prototype.forEach.call(el.querySelectorAll('.reveal-child'), function (c, i) { c.style.setProperty('--i', i); });
  });
  if (reduce.matches || !('IntersectionObserver' in window)) {
    sections.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.1 });
    sections.forEach(function (el) { io.observe(el); });
  }

  // header state
  var header = document.querySelector('[data-header]');
  if (header) {
    var lastY = window.scrollY, hideAfter = 120, threshold = 80;
    function onScroll() {
      var y = window.scrollY;
      header.classList.toggle('is-top', y < threshold);
      if (header.getAttribute('data-menu-open') === 'true' || header.contains(document.activeElement)) { header.classList.remove('is-hidden'); lastY = y; return; }
      if (y > hideAfter && y - lastY > 8) header.classList.add('is-hidden');
      else if (lastY - y > 2) header.classList.remove('is-hidden');
      lastY = y;
    }
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  reduce.addEventListener && reduce.addEventListener('change', function () { window.location.reload(); });
})();
