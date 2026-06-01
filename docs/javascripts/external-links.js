// Open external links — and internal deep-read links — in a new browser tab.
//
// Article links (arXiv, journal pages, etc.) point off-site; by default they
// replace the current page, which loses your place in the archive. The same
// goes for the "🔍 精读" / deep-read links scattered across the daily and
// journal overview pages: opening a deep read shouldn't throw away the
// overview you were scanning. So we new-tab both external links and any
// internal link into /deep_reads/, while leaving ordinary in-site navigation
// alone — the site uses mkdocs-material's `navigation.instant` SPA routing,
// and forcing those into new tabs would break it.
//
// We do this with a single capture-phase click delegate rather than by
// stamping target="_blank" onto each link. That makes it immune to timing:
// it works for links injected dynamically by extras.js (the 🔍 精读 badges,
// the 收藏 page re-renders) and it runs *before* Material's instant-navigation
// handler, so internal deep-read links genuinely open in a new tab instead of
// being intercepted as an SPA navigation.

(function () {
  "use strict";

  function qualifies(a) {
    const href = a.getAttribute("href") || "";
    // Leave in-page anchors (toc permalinks) and mailto: alone.
    if (href.startsWith("#") || /^mailto:/i.test(href)) return false;
    // a.hostname / a.pathname resolve both relative and absolute hrefs.
    const external =
      /^https?:\/\//i.test(href) && a.hostname !== window.location.hostname;
    const deepRead = a.pathname.includes("/deep_reads/");
    return external || deepRead;
  }

  document.addEventListener(
    "click",
    function (e) {
      // Respect default-prevented, non-primary buttons, and modifier clicks
      // (cmd/ctrl/shift/alt-click already do their own thing in the browser).
      if (e.defaultPrevented || e.button !== 0) return;
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      const a = e.target.closest ? e.target.closest("a[href]") : null;
      if (!a) return;
      // Only act on links inside the page content, never the chrome/nav.
      const content = document.querySelector(".md-content");
      if (!content || !content.contains(a)) return;
      if (!qualifies(a)) return;
      // Stop Material's instant-navigation handler and open a new tab.
      e.preventDefault();
      e.stopPropagation();
      window.open(a.href, "_blank", "noopener");
    },
    true // capture phase: run before mkdocs-material's click handler
  );
})();
