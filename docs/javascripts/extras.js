// Two enhancements layered on top of mkdocs-material:
//   1) Per-paper read / unread badges on daily / journals pages.
//      Personal mode only: enable on a browser by visiting any page with
//      ?me=1 once; the badges are then shown there forever (until cleared).
//      State is keyed by paper_id and lives in localStorage — visible only
//      to that browser, never sent anywhere.
//   2) Inline "🔍 精读" link injection on daily / journals overview pages,
//      driven by docs/data/deep_reads_index.json. Always visible.

(function () {
  const MODE_KEY = "rn-personal-mode";
  const READ_PREFIX = "rn-paper-read:";

  // ── personal-mode toggle ───────────────────────────────────────────────────

  function syncPersonalMode() {
    try {
      const params = new URLSearchParams(location.search);
      if (params.has("me")) {
        const v = params.get("me");
        if (v === "0" || v === "off") {
          localStorage.removeItem(MODE_KEY);
        } else {
          localStorage.setItem(MODE_KEY, "1");
        }
      }
    } catch (e) {}
  }

  function personalModeOn() {
    try { return localStorage.getItem(MODE_KEY) === "1"; }
    catch (e) { return false; }
  }

  // ── helpers ────────────────────────────────────────────────────────────────

  function getRoot() {
    const p = location.pathname;
    for (const d of ["/daily/", "/journals/", "/deep_reads/"]) {
      const idx = p.indexOf(d);
      if (idx >= 0) return p.slice(0, idx + 1);
    }
    return p.replace(/[^\/]*$/, "");
  }

  function isOverviewPage() {
    const p = location.pathname;
    return p.includes("/daily/") || p.includes("/journals/");
  }

  // First non-headerlink <a> inside a heading is the paper-title link, and
  // its textContent is the paper_id (DOI / arxiv id / jmlr id).
  function findPaperLinks() {
    const out = [];
    document.querySelectorAll("h2, h3, h4, h5, h6").forEach((h) => {
      const a = Array.from(h.querySelectorAll("a")).find(
        (x) => !x.classList.contains("headerlink")
      );
      if (!a) return;
      const id = (a.textContent || "").trim();
      if (!id) return;
      out.push({ heading: h, link: a, paperId: id });
    });
    return out;
  }

  // ── per-paper read / unread badges ─────────────────────────────────────────

  function addReadBadge({ link, paperId }) {
    if (link.dataset.rnPaperBadge) return;
    link.dataset.rnPaperBadge = "1";

    const key = READ_PREFIX + paperId;
    const badge = document.createElement("span");
    badge.className = "rn-read-badge";
    badge.setAttribute("role", "button");
    badge.title = "点击切换已读 / 未读（仅在本浏览器生效）";

    function refresh() {
      const isRead = (() => {
        try { return localStorage.getItem(key) === "1"; }
        catch (e) { return false; }
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
    link.insertAdjacentElement("afterend", badge);
  }

  // ── deep-read link injection (always on) ───────────────────────────────────

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
          if (!byId.has(e.paper_id)) byId.set(e.paper_id, e);
        }
        _deepReadsCache = byId;
        return byId;
      })
      .catch(() => new Map());
  }

  function addDeepReadLink({ link, paperId }, byId) {
    if (link.dataset.rnDeepLink) return;
    if (!byId.has(paperId)) return;
    link.dataset.rnDeepLink = "1";

    const entry = byId.get(paperId);
    const href = getRoot() + entry.doc_path.replace(/\.md$/i, "/");

    const a = document.createElement("a");
    a.href = href;
    a.className = "rn-deep-link";
    a.textContent = "🔍 精读";
    a.title = entry.title || "Deep-read report";
    link.insertAdjacentElement("afterend", a);
  }

  // ── styles ─────────────────────────────────────────────────────────────────

  function ensureStyles() {
    if (document.getElementById("rn-extras-style")) return;
    const css = `
      .rn-read-badge {
        display: inline-block;
        margin-left: 0.4em;
        padding: 0 0.4em;
        font-size: 0.7em;
        line-height: 1.5;
        border-radius: 0.25em;
        cursor: pointer;
        user-select: none;
        vertical-align: middle;
        border: 1px solid transparent;
        font-weight: normal;
      }
      .rn-read-badge.rn-read   { color: #5a5a5a; background: #eee; border-color: #ddd; }
      .rn-read-badge.rn-unread { color: #b06b00; background: #fff3d6; border-color: #f0d28a; }
      [data-md-color-scheme="slate"] .rn-read-badge.rn-read   { color: #aaa; background: #2a2a2a; border-color: #444; }
      [data-md-color-scheme="slate"] .rn-read-badge.rn-unread { color: #ffc34d; background: #3a2f10; border-color: #6a5310; }

      .rn-deep-link {
        display: inline-block;
        margin-left: 0.5em;
        padding: 0 0.45em;
        font-size: 0.75em;
        line-height: 1.6;
        border-radius: 0.3em;
        background: #fff7d6;
        color: #8a6500 !important;
        border: 1px solid #e6c200;
        text-decoration: none !important;
        vertical-align: middle;
        font-weight: normal;
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
    syncPersonalMode();
    ensureStyles();
    if (!isOverviewPage()) return;

    const paperLinks = findPaperLinks();
    if (!paperLinks.length) return;

    const showBadges = personalModeOn();
    if (showBadges) {
      paperLinks.forEach(addReadBadge);
    }

    loadDeepReads().then((byId) => {
      if (!byId.size) return;
      paperLinks.forEach((pl) => addDeepReadLink(pl, byId));
    });
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(() => init());
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
