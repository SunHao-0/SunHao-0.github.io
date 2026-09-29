/* Theme toggle (light/dark, remembered) + section highlighting in the nav. */
(function () {
  "use strict";

  var root = document.documentElement;

  function currentTheme() {
    if (root.dataset.theme) return root.dataset.theme;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  var toggle = document.getElementById("theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      try { localStorage.setItem("theme", next); } catch (e) { /* private mode */ }
      toggle.setAttribute("aria-label", "Switch to " + (next === "dark" ? "light" : "dark") + " theme");
    });
  }

  /* On phones the nav scrolls horizontally; make sure the current page's
     link is visible rather than hidden past the right edge. */
  var current = document.querySelector('.topnav a.is-active');
  if (current && current.scrollIntoView) {
    current.scrollIntoView({ block: 'nearest', inline: 'nearest' });
  }

  /* Highlight the section currently in view. */
  var links = Array.prototype.slice.call(document.querySelectorAll('.topnav a[href^="#"]'));
  if (!links.length || !("IntersectionObserver" in window)) return;

  var byId = {};
  var sections = [];
  links.forEach(function (a) {
    var el = document.getElementById(a.hash.slice(1));
    if (el) { byId[el.id] = a; sections.push(el); }
  });

  var visible = new Set();
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) visible.add(entry.target.id);
      else visible.delete(entry.target.id);
    });
    var active = sections.filter(function (s) { return visible.has(s.id); })[0];
    links.forEach(function (a) { a.classList.remove("is-active"); });
    if (active && byId[active.id]) byId[active.id].classList.add("is-active");
  }, { rootMargin: "-20% 0px -70% 0px", threshold: 0 });

  sections.forEach(function (s) { observer.observe(s); });
})();
