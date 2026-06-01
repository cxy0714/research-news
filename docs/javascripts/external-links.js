// Make external links in the page content open in a new browser tab.
//
// Article links (arXiv, journal pages, etc.) point off-site; by default they
// replace the current page, which loses your place in the archive. Here we
// rewrite every external link inside the main content to open in a new tab,
// while leaving internal navigation links alone — the site uses
// mkdocs-material's `navigation.instant` SPA routing, and forcing those into
// new tabs would break it.

(function () {
  "use strict";

  function externalize() {
    const content = document.querySelector(".md-content");
    if (!content) return;
    content.querySelectorAll('a[href]').forEach((a) => {
      const href = a.getAttribute("href") || "";
      // Skip in-page anchors, mailto:, and relative/internal links.
      if (!/^https?:\/\//i.test(href)) return;
      if (a.hostname === window.location.hostname) return;
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
