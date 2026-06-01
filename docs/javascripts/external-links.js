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

(function () {
  "use strict";

  function externalize() {
    const content = document.querySelector(".md-content");
    if (!content) return;
    content.querySelectorAll('a[href]').forEach((a) => {
      const href = a.getAttribute("href") || "";
      // Skip in-page anchors (e.g. toc permalinks) and mailto:.
      if (href.startsWith("#") || /^mailto:/i.test(href)) return;
      const external =
        /^https?:\/\//i.test(href) && a.hostname !== window.location.hostname;
      // a.pathname resolves both relative and absolute hrefs.
      const deepRead = a.pathname.includes("/deep_reads/");
      if (!external && !deepRead) return;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
    });
  }

  // Re-run on every instant-navigation page load; fall back to plain load.
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(externalize);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", externalize);
  } else {
    externalize();
  }
})();
