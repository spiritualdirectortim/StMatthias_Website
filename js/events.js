// Removes events that have already ended, so the site never shows a past event
// even if nobody has re-run scripts/build.py since. Runs before motion.js.
// Event content itself lives in data/events.json and is rendered by the build.
(function () {
  var now = Date.now();

  Array.prototype.forEach.call(document.querySelectorAll("[data-event-end]"), function (el) {
    var end = Date.parse(el.getAttribute("data-event-end"));
    if (!isNaN(end) && end < now) el.parentNode.removeChild(el);
  });

  function pad(n) { return (n < 10 ? "0" : "") + n; }

  // Homepage hero: show up to three featured events, or the Mass-times fallback.
  var hero = document.querySelector("[data-scroll-scene]");
  if (hero) {
    var limit = 3;
    var scenes = Array.prototype.slice.call(hero.querySelectorAll("[data-scene]"));
    scenes.forEach(function (scene, i) {
      if (i >= limit) { scene.parentNode.removeChild(scene); return; }
      scene.hidden = false;
      scene.classList.toggle("is-active", i === 0);
      scene.setAttribute("aria-hidden", String(i !== 0));
    });
    scenes = scenes.slice(0, limit);
    var fallback = hero.querySelector("[data-scene-fallback]");
    if (!scenes.length && fallback) {
      fallback.hidden = false;
      fallback.setAttribute("data-scene", "");
      fallback.classList.add("is-active");
      scenes = [fallback];
    } else if (fallback) {
      fallback.parentNode.removeChild(fallback);
    }
    var total = hero.querySelector("[data-scene-total]");
    if (total) total.textContent = pad(Math.max(scenes.length, 1));
    hero.classList.toggle("is-single", scenes.length < 2);
  }

  // Homepage "Upcoming at St. Matthias": first five remaining events.
  var grid = document.querySelector("[data-upcoming]");
  if (grid) {
    var cards = Array.prototype.slice.call(grid.children);
    cards.forEach(function (card, i) {
      if (i >= 5) card.parentNode.removeChild(card);
      else card.hidden = false;
    });
    var count = Math.min(cards.length, 5);
    grid.setAttribute("data-count", String(count));
    var empty = document.querySelector("[data-upcoming-empty]");
    if (empty) empty.hidden = count > 0;
    if (!count) grid.parentNode.removeChild(grid);
  }

  // Events page: empty state if every dated event has passed.
  var list = document.querySelector("[data-event-list]");
  if (list) {
    var none = document.querySelector("[data-events-empty]");
    if (none) none.hidden = list.children.length > 0;
  }
})();
