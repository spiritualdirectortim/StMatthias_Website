// Progressive motion for the St. Matthias narrative homepage.
// Every section has a static fallback and respects reduced-motion preferences.
(function () {
  var doc = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var desktop = window.matchMedia("(min-width: 768px)");
  doc.classList.add("js");

  function splitWords(el, className) {
    var n = 0;
    function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (child) {
        if (child.nodeType === 3) {
          var frag = document.createDocumentFragment();
          child.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) {
              frag.appendChild(document.createTextNode(" "));
              return;
            }
            var outer = document.createElement("span");
            outer.className = className;
            var inner = document.createElement("span");
            inner.textContent = part;
            inner.style.setProperty("--i", n++);
            outer.appendChild(inner);
            frag.appendChild(outer);
          });
          node.replaceChild(frag, child);
        } else if (child.nodeType === 1) {
          walk(child);
        }
      });
    }
    walk(el);
    return n;
  }

  document.querySelectorAll("[data-split]").forEach(function (el) {
    splitWords(el, "w");
    el.classList.add("split");
  });

  var missionWords = [];
  document.querySelectorAll("[data-word-light] h2").forEach(function (el) {
    splitWords(el, "lit-word");
    missionWords = missionWords.concat(Array.prototype.slice.call(el.querySelectorAll(".lit-word")));
  });

  var ready = false;
  function markReady() {
    if (ready) return;
    ready = true;
    doc.classList.add("is-ready");
  }
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { window.setTimeout(markReady, 40); });
  }
  window.setTimeout(markReady, 800);

  document.querySelectorAll("[data-reveal-stagger]").forEach(function (group) {
    Array.prototype.forEach.call(group.children, function (child, i) {
      child.style.setProperty("--i", i);
    });
  });
  var revealTargets = document.querySelectorAll("[data-reveal], [data-reveal-stagger]");
  if ("IntersectionObserver" in window && !reduce.matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: .07 });
    revealTargets.forEach(function (target) { io.observe(target); });
  } else {
    revealTargets.forEach(function (target) { target.classList.add("is-in"); });
  }

  var hero = document.querySelector("[data-scroll-scene]");
  var scenes = hero ? Array.prototype.slice.call(hero.querySelectorAll("[data-scene]")) : [];
  var sceneCurrent = hero ? hero.querySelector("[data-scene-current]") : null;
  var heroPrev = hero ? hero.querySelector("[data-hero-prev]") : null;
  var heroNext = hero ? hero.querySelector("[data-hero-next]") : null;
  var carouselIndex = 0;
  var carouselTimer = 0;
  var carouselInterval = 5000;
  var openingCarouselInterval = 15000;
  var heroCrossfadeDuration = 1200;
  var heroLeavingTimers = [];
  var syncHeroToScroll = true;
  var scrubs = Array.prototype.slice.call(document.querySelectorAll("[data-scrub]"));
  var missionSection = document.querySelector(".mission-scroll");
  var missionImages = missionSection ? Array.prototype.slice.call(missionSection.querySelectorAll(".mission-image")) : [];
  var sundaySection = document.querySelector(".sunday");
  var ministrySection = document.querySelector(".ministry-scroll");
  var ministrySticky = ministrySection ? ministrySection.querySelector(".ministry-sticky") : null;
  var flightLayer = document.querySelector("[data-ministry-flight]");
  var flightImages = flightLayer ? Array.prototype.slice.call(flightLayer.querySelectorAll("[data-flight-image]")) : [];
  var ministryTargets = ministrySection ? Array.prototype.slice.call(ministrySection.querySelectorAll(".ministry-card img")) : [];
  var ticking = false;

  function progressFor(el, viewportHeight) {
    var rect = el.getBoundingClientRect();
    var travel = rect.height - viewportHeight;
    if (travel <= 0) return 1;
    return Math.min(1, Math.max(0, -rect.top / travel));
  }

  function clamp01(value) {
    return Math.min(1, Math.max(0, value));
  }

  function lerp(from, to, amount) {
    return from + (to - from) * amount;
  }

  function ease(amount) {
    amount = clamp01(amount);
    return amount * amount * (3 - 2 * amount);
  }

  function renderHeroScene() {
    if (!hero || !scenes.length) return;
    carouselIndex = (carouselIndex + scenes.length) % scenes.length;
    scenes.forEach(function (scene, index) {
      var isActive = index === carouselIndex;
      var wasActive = scene.classList.contains("is-active");
      window.clearTimeout(heroLeavingTimers[index]);
      if (isActive) {
        scene.classList.remove("is-leaving");
      } else if (wasActive) {
        scene.classList.add("is-leaving");
        heroLeavingTimers[index] = window.setTimeout(function () {
          if (!scene.classList.contains("is-active")) scene.classList.remove("is-leaving");
        }, heroCrossfadeDuration);
      }
      scene.classList.toggle("is-active", isActive);
      scene.setAttribute("aria-hidden", String(!isActive));
    });
    hero.style.setProperty("--hero-p", ((carouselIndex + 1) / scenes.length).toFixed(4));
    if (sceneCurrent) sceneCurrent.textContent = String(carouselIndex + 1).padStart(2, "0");
  }

  function scheduleCarousel() {
    window.clearTimeout(carouselTimer);
    if (!hero || scenes.length < 2 || reduce.matches) return;
    var sceneInterval = carouselIndex === 0 ? openingCarouselInterval : carouselInterval;
    carouselTimer = window.setTimeout(function () {
      var rect = hero.getBoundingClientRect();
      var isVisible = rect.top < window.innerHeight && rect.bottom > 0;
      if (!document.hidden && isVisible && !hero.contains(document.activeElement)) {
        carouselIndex += 1;
        renderHeroScene();
      }
      scheduleCarousel();
    }, sceneInterval);
  }

  function moveCarousel(direction) {
    carouselIndex += direction;
    syncHeroToScroll = false;
    renderHeroScene();
    scheduleCarousel();
  }

  if (heroPrev) heroPrev.addEventListener("click", function () { moveCarousel(-1); });
  if (heroNext) heroNext.addEventListener("click", function () { moveCarousel(1); });

  function flightStartRects(viewportWidth, viewportHeight) {
    var width = Math.min(240, Math.max(136, viewportWidth * .17));
    var height = width * .75;
    return [
      { x: viewportWidth * .03 + 20, y: viewportHeight * .15 - 20, w: width, h: height, r: -5 },
      { x: (viewportWidth - width) / 2, y: viewportHeight * .035, w: width, h: height, r: 1 },
      { x: viewportWidth - width - viewportWidth * .02, y: viewportHeight * .91 - height, w: width, h: height, r: -4 },
      { x: viewportWidth * .10 - 40, y: viewportHeight * .82 - height + 20, w: width, h: height, r: 3 },
      { x: viewportWidth - width - Math.max(0, viewportWidth * .05 - 20), y: viewportHeight * .12, w: width, h: height, r: 4 }
    ];
  }

  function flightWaypoints(viewportWidth, viewportHeight, starts) {
    var sideWidth = Math.min(viewportWidth * .29, starts[0].w * 1.55);
    var sideHeight = sideWidth * .66;
    var smallWidth = starts[0].w * .92;
    var smallHeight = smallWidth * .75;
    return [
      { x: -sideWidth * .20, y: viewportHeight * .50, w: sideWidth, h: sideHeight, r: 2 },
      { x: (viewportWidth - smallWidth) / 2, y: viewportHeight * .08, w: smallWidth, h: smallHeight, r: 1 },
      { x: viewportWidth - sideWidth * .80, y: viewportHeight * .47, w: sideWidth, h: sideHeight, r: -2 },
      { x: viewportWidth * .08, y: viewportHeight * .66, w: smallWidth, h: smallHeight, r: -3 },
      { x: viewportWidth - smallWidth - viewportWidth * .08, y: viewportHeight * .66, w: smallWidth, h: smallHeight, r: 3 }
    ];
  }

  function updateMinistryFlight(viewportWidth, viewportHeight) {
    if (!flightLayer || !missionSection || !sundaySection || !ministrySection || !ministrySticky || flightImages.length !== ministryTargets.length) return;

    var scrollY = window.scrollY || window.pageYOffset;
    var missionRect = missionSection.getBoundingClientRect();
    var ministryRect = ministrySection.getBoundingClientRect();
    var missionTop = scrollY + missionRect.top;
    var ministryTop = scrollY + ministryRect.top;
    var missionTravel = Math.max(1, missionRect.height - viewportHeight);
    var motionStart = missionTop + missionTravel;
    var motionEnd = ministryTop - viewportHeight * .32;
    var raw = clamp01((scrollY - motionStart) / Math.max(1, motionEnd - motionStart));
    var isInJourney = scrollY >= motionStart && scrollY < ministryTop + viewportHeight * .08;
    var starts = flightStartRects(viewportWidth, viewportHeight);
    var waypoints = flightWaypoints(viewportWidth, viewportHeight, starts);
    var firstLeg = ease(raw / .70);
    var secondLeg = ease((raw - .70) / .30);
    var crossfade = ease((raw - .975) / .025);

    flightLayer.style.visibility = isInJourney ? "visible" : "hidden";
    missionImages.forEach(function (image) {
      image.style.visibility = isInJourney ? "hidden" : "visible";
    });

    flightImages.forEach(function (image, index) {
      var start = starts[index];
      var waypoint = waypoints[index];
      var targetRect = ministryTargets[index].getBoundingClientRect();
      var target = {
        x: targetRect.left,
        y: Math.min(targetRect.top, viewportHeight - Math.min(targetRect.height, waypoint.h) * .45),
        w: targetRect.width,
        h: targetRect.height,
        r: 0
      };
      var from = raw < .70 ? start : waypoint;
      var to = raw < .70 ? waypoint : target;
      var amount = raw < .70 ? firstLeg : secondLeg;
      var x = lerp(from.x, to.x, amount);
      var y = lerp(from.y, to.y, amount);
      var width = lerp(from.w, to.w, amount);
      var height = lerp(from.h, to.h, amount);
      var rotation = lerp(from.r, to.r, amount);
      var opacity = 1 - crossfade;

      image.style.left = x + "px";
      image.style.top = y + "px";
      image.style.width = width + "px";
      image.style.height = height + "px";
      image.style.opacity = String(opacity);
      image.style.filter = "none";
      image.style.transform = "rotate(" + rotation + "deg)";
      image.style.borderRadius = lerp(24, 16, raw) + "px";
      ministryTargets[index].style.opacity = String(crossfade);
    });

    if (!isInJourney && scrollY >= ministryTop) {
      ministryTargets.forEach(function (target) { target.style.opacity = "1"; });
    }
  }

  function animateEvents(el, p) {
    var settings = [
      { delay: 0, x: 28, startRotation: -15, endRotation: -8 },
      { delay: .05, x: 15, startRotation: -9, endRotation: -4 },
      { delay: .10, x: 0, startRotation: 2, endRotation: 0 },
      { delay: .15, x: -15, startRotation: 9, endRotation: 4 },
      { delay: .20, x: -28, startRotation: 15, endRotation: 8 }
    ];
    el.querySelectorAll(".event-poster").forEach(function (poster, index) {
      var s = settings[index];
      if (!s) return;
      var ep = ease((p - s.delay) / .58);
      var q = 1 - ep;
      var rotation = lerp(s.startRotation, s.endRotation, ep);
      poster.style.opacity = String(clamp01((p - s.delay) * 7));
      poster.style.transform = "translate3d(" + (s.x * q) + "vw," + (q * 62) + "vh,0) rotate(" + rotation + "deg) scale(" + (.78 + .22 * ep) + ")";
    });
  }

  function entryProgress(el, viewportHeight) {
    var rect = el.getBoundingClientRect();
    return clamp01((viewportHeight - rect.top) / (viewportHeight * .78));
  }

  function wordLightProgress(el, viewportHeight) {
    var heading = el.querySelector("h2");
    if (!heading) return 1;
    var rect = heading.getBoundingClientRect();
    var finishOffset = 100;
    return clamp01((viewportHeight - rect.top) / (rect.height + finishOffset));
  }

  function eventTriggerProgress(el, viewportHeight) {
    var intro = el.querySelector(".events-intro");
    var button = el.querySelector(".events-intro .btn");
    if (!intro || !button) return entryProgress(el, viewportHeight);
    var sectionTop = el.getBoundingClientRect().top;
    var buttonTop = button.getBoundingClientRect().top;
    var sectionEntry = clamp01((viewportHeight - sectionTop) / (viewportHeight * .72)) * .78;
    var buttonEntry = clamp01((viewportHeight - 150 - buttonTop) / (viewportHeight * .34));
    return Math.max(sectionEntry, buttonEntry);
  }

  function update() {
    ticking = false;
    var viewportHeight = window.innerHeight;

    if (!desktop.matches || reduce.matches) {
      renderHeroScene();
      scrubs.forEach(function (el) { el.style.setProperty("--p", 1); });
      missionWords.forEach(function (word) {
        word.style.removeProperty("--word-light");
        word.classList.add("is-lit");
      });
      if (flightLayer) flightLayer.style.visibility = "hidden";
      missionImages.forEach(function (image) { image.style.visibility = "visible"; });
      document.querySelectorAll(".mission-image, .flight-image, .ministry-card img, .ministry-card > div, .event-poster").forEach(function (el) {
        el.style.opacity = "";
        el.style.transform = "";
      });
      return;
    }

    if (hero) {
      var heroRect = hero.getBoundingClientRect();
      if (syncHeroToScroll && heroRect.height > viewportHeight) {
        var heroProgress = progressFor(hero, viewportHeight);
        carouselIndex = Math.min(scenes.length - 1, Math.floor(heroProgress * scenes.length));
      }
      renderHeroScene();
      syncHeroToScroll = false;
    }

    scrubs.forEach(function (el) {
      var p = progressFor(el, viewportHeight);
      if (el.hasAttribute("data-word-light")) {
        p = wordLightProgress(el, viewportHeight);
        el.style.setProperty("--p", p.toFixed(4));
        var wordPosition = p * missionWords.length;
        missionWords.forEach(function (word, index) {
          var wordProgress = clamp01(wordPosition - index);
          word.style.setProperty("--word-light", (.18 + .82 * wordProgress).toFixed(3));
          word.classList.toggle("is-lit", wordProgress >= 1);
        });
      }
      if (el.classList.contains("ministry-scroll")) {
        p = entryProgress(el, viewportHeight);
        el.style.setProperty("--p", p.toFixed(4));
      }
      if (el.classList.contains("events-scroll")) {
        p = eventTriggerProgress(el, viewportHeight);
        el.style.setProperty("--p", p.toFixed(4));
        animateEvents(el, p);
      }
    });

    updateMinistryFlight(window.innerWidth, viewportHeight);
  }

  function requestUpdate() {
    if (!ticking) {
      ticking = true;
      window.requestAnimationFrame(update);
    }
  }

  window.addEventListener("scroll", function () {
    syncHeroToScroll = true;
    scheduleCarousel();
    requestUpdate();
  }, { passive: true });
  window.addEventListener("resize", requestUpdate);
  window.addEventListener("load", requestUpdate);
  window.addEventListener("pageshow", requestUpdate);
  if (desktop.addEventListener) desktop.addEventListener("change", requestUpdate);
  if (reduce.addEventListener) reduce.addEventListener("change", requestUpdate);
  document.addEventListener("visibilitychange", scheduleCarousel);
  update();
  scheduleCarousel();
  window.setTimeout(requestUpdate, 160);
})();
