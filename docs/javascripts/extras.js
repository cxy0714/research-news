// Two enhancements layered on top of mkdocs-material:
//   1) Read / unread tracker for daily / journals / deep_reads pages
//      (state in localStorage, badge next to every link, auto-mark on visit).
//   2) Inline "🔍 精读" link injection on daily / journals overview pages,
//      driven by docs/data/deep_reads_index.json.

(function () {
  const STORAGE_PREFIX = "rn-read:";
  const TRACKED_DIRS = ["/daily/", "/journals/", "/deep_reads/"];

  // ── helpers ────────────────────────────────────────────────────────────────

  function normalizePath(pathname) {
    // Drop trailing index.html, ensure trailing slash, lowercase.
    let p = pathname.replace(/index\.html$/i, "");
    if (!p.endsWith("/") && !/\.[a-z0-9]+$/i.test(p)) p += "/";
    return p.toLowerCase();
  }

  function isTrackedPath(pathname) {
    return TRACKED_DIRS.some((d) => pathname.includes(d));
  }

  function getRoot() {
    // Strip the deepest tracked-dir segment to find the docs root URL.
    const p = location.pathname;
    for (const d of TRACKED_DIRS) {
      const idx = p.indexOf(d);
      if (idx >= 0) return p.slice(0, idx + 1);
    }
    // Fallback: directory of current page.
    return p.replace(/[^\/]*$/, "");
  }

  // ── 1) read / unread tracker ───────────────────────────────────────────────

  function markCurrentAsRead() {
    const path = normalizePath(location.pathname);
    if (isTrackedPath(path)) {
      try { localStorage.setItem(STORAGE_PREFIX + path, "1"); } catch (e) {}
    }
  }

  function decorateLinks() {
    document.querySelectorAll("a[href]").forEach((a) => {
      if (a.dataset.rnRead) return;
      let url;
      try { url = new URL(a.href, location.href); } catch (e) { return; }
      if (url.origin !== location.origin) return;
      const path = normalizePath(url.pathname);
      if (!isTrackedPath(path)) return;
      a.dataset.rnRead = "1";

      const key = STORAGE_PREFIX + path;
      const badge = document.createElement("span");
      badge.className = "rn-read-badge";
      badge.setAttribute("role", "button");
      badge.title = "点击切换已读 / 未读";

      function refresh() {
        const isRead = (() => {
          try { return localStorage.getItem(key) === "1"; } catch (e) { return false; }
        })();
        badge.textContent = isRead ? "✓ 已读" : "○ 未读";
        badge.classList.toggle("rn-read", isRead);
        badge.classList.toggle("rn-unread", !isRead);
      }
      badge.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        try {
          if (localStorage.getItem(key) === "1") localStorage.removeItem(key);
          else localStorage.setItem(key, "1");
        } catch (err) {}
        refresh();
      });
      refresh();
      a.insertAdjacentElement("afterend", badge);
    });
  }

  // ── 2) deep-read link injection ────────────────────────────────────────────

  let _deepReadsCache = null;

  function loadDeepReads() {
    if (_deepReadsCache) return Promise.resolve(_deepReadsCache);
    const url = getRoot() + "data/deep_reads_index.json";
    return fetch(url, { cache: "no-cache" })
      .then((r) => (r.ok ? r.json() : []))
      .then((arr) => {
        const byId = new Map();
        for (const e of arr) {
          if (!e || !e.paper_id || !e.doc_path) continue;
          // Keep newest entry per paper (array is already sorted desc by date).
          if (!byId.has(e.paper_id)) byId.set(e.paper_id, e);
        }
        _deepReadsCache = byId;
        return byId;
      })
      .catch(() => new Map());
  }

  function injectDeepReadLinks() {
    const p = location.pathname;
    if (!p.includes("/daily/") && !p.includes("/journals/")) return;

    loadDeepReads().then((byId) => {
      if (!byId.size) return;
      const root = getRoot();
      document.querySelectorAll("a").forEach((a) => {
        const id = (a.textContent || "").trim();
        if (!byId.has(id)) return;
        // Avoid duplicate injection.
        const next = a.nextElementSibling;
        if (next && next.classList && next.classList.contains("rn-deep-link")) return;

        const entry = byId.get(id);
        // doc_path is "deep_reads/<stem>.md"; mkdocs serves it as ".../"
        let href = entry.doc_path.replace(/\.md$/i, "/");
        href = root + href;

        const link = document.createElement("a");
        link.href = href;
        link.className = "rn-deep-link";
        link.textContent = "🔍 精读";
        link.title = entry.title || "Deep-read report";
        a.insertAdjacentElement("afterend", link);
      });
      // Newly injected links should also get the read/unread badge.
      decorateLinks();
    });
  }

  // ── styles ─────────────────────────────────────────────────────────────────

  function ensureStyles() {
    if (document.getElementById("rn-extras-style")) return;
    const css = `
      .rn-read-badge {
        display: inline-block;
        margin-left: 0.4em;
        padding: 0 0.4em;
        font-size: 0.75em;
        line-height: 1.4;
        border-radius: 0.25em;
        cursor: pointer;
        user-select: none;
        vertical-align: middle;
        border: 1px solid transparent;
      }
      .rn-read-badge.rn-read   { color: #5a5a5a; background: #eee; border-color: #ddd; }
      .rn-read-badge.rn-unread { color: #b06b00; background: #fff3d6; border-color: #f0d28a; }
      [data-md-color-scheme="slate"] .rn-read-badge.rn-read   { color: #aaa; background: #2a2a2a; border-color: #444; }
      [data-md-color-scheme="slate"] .rn-read-badge.rn-unread { color: #ffc34d; background: #3a2f10; border-color: #6a5310; }

      .rn-deep-link {
        display: inline-block;
        margin-left: 0.5em;
        padding: 0 0.45em;
        font-size: 0.8em;
        line-height: 1.5;
        border-radius: 0.3em;
        background: #fff7d6;
        color: #8a6500 !important;
        border: 1px solid #e6c200;
        text-decoration: none !important;
        vertical-align: middle;
      }
      .rn-deep-link:hover { background: #ffeaa3; }
      [data-md-color-scheme="slate"] .rn-deep-link {
        background: #3a2f10; color: #ffd966 !important; border-color: #806000;
      }
    `;
    const style = document.createElement("style");
    style.id = "rn-extras-style";
    style.textContent = css;
    document.head.appendChild(style);
  }

  // ── lifecycle ──────────────────────────────────────────────────────────────

  function init() {
    ensureStyles();
    markCurrentAsRead();
    injectDeepReadLinks();
    decorateLinks();
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    // mkdocs-material instant navigation: re-run on every page swap.
    document$.subscribe(() => init());
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
