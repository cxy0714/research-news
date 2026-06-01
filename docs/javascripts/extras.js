// Personal-account layer on top of the static mkdocs-material site.
//
// There is no server: a personal GitHub token (gist scope) entered once in the
// browser acts as the "login", and per-user state — which papers are read, and
// which are starred (collected) along with per-paper comments — lives in a
// single private GitHub Gist on that account, synced across every signed-in
// device. Signing in is required; without a token only the login button shows.
//
// Features:
//   1) Account button (bottom-right): paste a GitHub token to sign in / out.
//   2) Per-paper read / unread + ☆ 收藏 badges on daily / journals / deep-read
//      pages. Starring a paper drops it into the 收藏 page automatically.
//   3) The 收藏 page (docs/favorites.md) renders all starred papers, with a
//      view toggle: 总收藏 (grouped by category → date) and 按周 (by ISO week).
//      Each paper can carry an inline comment, edited right on the page.

(function () {
  "use strict";

  // ── storage keys ────────────────────────────────────────────────────────
  const READ_PREFIX = "rn-paper-read:";     // legacy per-paper read keys
  const TOKEN_KEY = "rn-gh-token";
  const GIST_ID_KEY = "rn-gist-id";
  const STATE_CACHE_KEY = "rn-state";       // local mirror of gist state
  const VIEW_KEY = "rn-collection-view";    // "total" | "week"

  const STATE_FILE = "research-news-state.json";
  const GIST_DESC = "research-news · 已读与收藏状态（请勿删除）";
  const GH_API = "https://api.github.com";

  // ── in-memory state ───────────────────────────────────────────────────────
  // { version, read: {paperId: isoTime}, favorites: {paperId: {...}} }
  let state = emptyState();
  let gistReady = false;     // true once the gist has been located/created
  let _synced = false;       // true once we've pulled from the gist this session
  let _deepReadsCache = null;
  let _topicLabelsCache = null;
  let _publicCache = null;

  function emptyState() {
    return { version: 1, read: {}, favorites: {} };
  }

  // ── tiny localStorage helpers (never throw) ────────────────────────────────
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function lsDel(k) { try { localStorage.removeItem(k); } catch (e) {} }

  function getToken() { return lsGet(TOKEN_KEY) || ""; }
  function getGistId() { return lsGet(GIST_ID_KEY) || ""; }
  function loggedIn() { return !!getToken() && gistReady; }

  // Read / favorite badges and the collection page require signing in: state
  // lives in the user's gist, so there is nowhere to persist without a token.
  function active() { return !!getToken(); }

  // ── ISO week, e.g. "2026-W22" ──────────────────────────────────────────────
  function isoWeek(d) {
    const date = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
    const day = date.getUTCDay() || 7;
    date.setUTCDate(date.getUTCDate() + 4 - day);
    const yearStart = new Date(Date.UTC(date.getUTCFullYear(), 0, 1));
    const week = Math.ceil((((date - yearStart) / 86400000) + 1) / 7);
    return date.getUTCFullYear() + "-W" + String(week).padStart(2, "0");
  }

  // ── local persistence + legacy migration ───────────────────────────────────
  function loadLocal() {
    try {
      const raw = lsGet(STATE_CACHE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        state = Object.assign(emptyState(), parsed);
        state.read = state.read || {};
        state.favorites = state.favorites || {};
      }
    } catch (e) { state = emptyState(); }
    migrateLegacyReads();
  }

  function migrateLegacyReads() {
    try {
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith(READ_PREFIX) && localStorage.getItem(k) === "1") {
          const id = k.slice(READ_PREFIX.length);
          if (!state.read[id]) state.read[id] = new Date().toISOString();
        }
      }
    } catch (e) {}
  }

  function saveLocal() { lsSet(STATE_CACHE_KEY, JSON.stringify(state)); }

  // ── GitHub Gist sync ────────────────────────────────────────────────────────
  function ghHeaders() {
    return {
      "Authorization": "Bearer " + getToken(),
      "Accept": "application/vnd.github+json",
    };
  }

  // Locate (or create) the state gist. Stores its id in localStorage.
  async function ensureGist() {
    if (!getToken()) return false;
    if (getGistId()) { gistReady = true; return true; }
    try {
      // Look for an existing state gist on this account first.
      const res = await fetch(GH_API + "/gists?per_page=100", { headers: ghHeaders() });
      if (!res.ok) throw new Error("list gists: " + res.status);
      const gists = await res.json();
      const found = gists.find((g) => g.description === GIST_DESC ||
        (g.files && g.files[STATE_FILE]));
      if (found) { lsSet(GIST_ID_KEY, found.id); gistReady = true; return true; }
      // None yet — create one, seeded from whatever is in local state.
      const created = await fetch(GH_API + "/gists", {
        method: "POST",
        headers: ghHeaders(),
        body: JSON.stringify({
          description: GIST_DESC,
          public: false,
          files: { [STATE_FILE]: { content: JSON.stringify(state, null, 2) } },
        }),
      });
      if (!created.ok) throw new Error("create gist: " + created.status);
      const g = await created.json();
      lsSet(GIST_ID_KEY, g.id);
      gistReady = true;
      return true;
    } catch (e) {
      console.warn("[research-news] gist setup failed:", e);
      return false;
    }
  }

  // Pull authoritative state from the gist (gist wins over local cache).
  async function pullGist() {
    if (!getToken() || !getGistId()) return false;
    try {
      const res = await fetch(GH_API + "/gists/" + getGistId(), { headers: ghHeaders() });
      if (!res.ok) throw new Error("get gist: " + res.status);
      const g = await res.json();
      const file = g.files && g.files[STATE_FILE];
      if (file && typeof file.content === "string" && file.content.trim()) {
        const remote = JSON.parse(file.content);
        state = Object.assign(emptyState(), remote);
        state.read = state.read || {};
        state.favorites = state.favorites || {};
        saveLocal();
      }
      return true;
    } catch (e) {
      console.warn("[research-news] gist pull failed:", e);
      return false;
    }
  }

  let _saveTimer = null;
  function scheduleSync() {
    saveLocal();
    if (!loggedIn()) return;
    if (_saveTimer) clearTimeout(_saveTimer);
    _saveTimer = setTimeout(pushGist, 800);
  }

  async function pushGist() {
    if (!loggedIn()) return;
    try {
      const res = await fetch(GH_API + "/gists/" + getGistId(), {
        method: "PATCH",
        headers: ghHeaders(),
        body: JSON.stringify({
          files: { [STATE_FILE]: { content: JSON.stringify(state, null, 2) } },
        }),
      });
      if (!res.ok) throw new Error("patch gist: " + res.status);
    } catch (e) {
      console.warn("[research-news] gist push failed:", e);
    }
  }

  // ── mutations ───────────────────────────────────────────────────────────────
  function isRead(id) { return !!state.read[id]; }
  function toggleRead(id) {
    if (state.read[id]) delete state.read[id];
    else state.read[id] = new Date().toISOString();
    scheduleSync();
  }

  function isFav(id) { return !!state.favorites[id]; }
  function toggleFav(info) {
    const id = info.paperId;
    if (state.favorites[id]) {
      delete state.favorites[id];
    } else {
      state.favorites[id] = {
        paper_id: id,
        title: info.title || id,
        url: info.url || "",
        deep_read_url: info.deepReadUrl || "",
        source: info.source || "",
        source_url: info.sourceUrl || location.pathname,
        category: info.category || UNCATEGORIZED,
        date: info.date || pageDate(),
        week: isoWeek(new Date()),
        added: new Date().toISOString(),
        note: "",
      };
    }
    scheduleSync();
    document.dispatchEvent(new CustomEvent("rn:favchange"));
  }

  function removeFav(id) {
    delete state.favorites[id];
    scheduleSync();
    document.dispatchEvent(new CustomEvent("rn:favchange"));
  }

  function setNote(id, text) {
    if (state.favorites[id]) {
      state.favorites[id].note = text;
      scheduleSync();
    }
  }

  // ── page / paper helpers ────────────────────────────────────────────────────
  // Absolute site root, derived from this script's own URL so it is correct on
  // any page depth and under any GitHub Pages base path.
  let _siteRoot = null;
  function siteRoot() {
    if (_siteRoot) return _siteRoot;
    const s = document.querySelector('script[src*="javascripts/extras.js"]');
    if (s) {
      const u = new URL(s.src, location.href);
      _siteRoot = u.pathname.replace(/javascripts\/extras\.js.*$/, "");
    } else {
      _siteRoot = "/";
    }
    return _siteRoot;
  }

  function getRoot() {
    const p = location.pathname;
    for (const d of ["/daily/", "/journals/", "/deep_reads/"]) {
      const idx = p.indexOf(d);
      if (idx >= 0) return p.slice(0, idx + 1);
    }
    return p.replace(/[^\/]*$/, "");
  }

  // YYYY-MM-DD from the page path (daily / journal / deep-read all carry it).
  function pageDate() {
    const m = location.pathname.match(/(\d{4}-\d{2}-\d{2})/);
    return m ? m[1] : new Date().toISOString().slice(0, 10);
  }

  function isOverviewPage() {
    const p = location.pathname;
    return p.includes("/daily/") || p.includes("/journals/");
  }

  function isDeepReadPage() {
    return location.pathname.includes("/deep_reads/");
  }

  function pageLabel() {
    const h1 = document.querySelector("article h1, .md-content h1");
    return h1 ? (h1.textContent || "").replace(/¶/g, "").trim() : document.title;
  }

  // On overview pages each paper heading is:  "N. <a>paper_id</a> — Title".
  // Capture id / url / title BEFORE we inject any badges (which would otherwise
  // pollute heading.textContent).
  function findPaperLinks() {
    const out = [];
    document.querySelectorAll("h2, h3, h4, h5, h6").forEach((h) => {
      const a = Array.from(h.querySelectorAll("a")).find(
        (x) => !x.classList.contains("headerlink")
      );
      if (!a) return;
      const id = (a.textContent || "").trim();
      if (!id) return;
      // Cache the title on first sight: later re-runs (e.g. after login) would
      // otherwise read injected badge text back out of heading.textContent.
      let title = a.dataset.rnTitle;
      if (title === undefined) {
        title = (h.textContent || "").replace(/¶/g, "").trim();
        const numMatch = title.match(/^\s*\d+\.\s*/);
        if (numMatch) title = title.slice(numMatch[0].length);
        if (title.startsWith(id)) title = title.slice(id.length);
        title = title.replace(/^[\s—–\-:]+/, "").trim();
        a.dataset.rnTitle = title;
      }
      out.push({ heading: h, link: a, paperId: id, title: title, url: a.href });
    });
    return out;
  }

  // ── deep-read index (for "🔍 精读" links + deep_read_url on favorites) ───────
  function loadDeepReads() {
    if (_deepReadsCache) return Promise.resolve(_deepReadsCache);
    const url = siteRoot() + "data/deep_reads_index.json";
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

  function deepReadHref(entry) {
    return siteRoot() + entry.doc_path.replace(/\.md$/i, "/");
  }

  // ── topic taxonomy (for grouping favorites by category) ───────────────────────
  // { order: [keys...], labels: {key: zh}, orderedLabels: [zh...] }
  function loadTopicLabels() {
    if (_topicLabelsCache) return Promise.resolve(_topicLabelsCache);
    const url = siteRoot() + "data/topic_labels.json";
    return fetch(url, { cache: "no-cache" })
      .then((r) => (r.ok ? r.json() : { order: [], labels: {} }))
      .then((j) => {
        const order = j.order || [];
        const labels = j.labels || {};
        _topicLabelsCache = {
          order: order,
          labels: labels,
          orderedLabels: order.map((k) => labels[k] || k),
        };
        return _topicLabelsCache;
      })
      .catch(() => ({ order: [], labels: {}, orderedLabels: [] }));
  }

  // Public favorites snapshot, refreshed nightly by a GitHub Action.
  function loadPublicFavs() {
    if (_publicCache) return Promise.resolve(_publicCache);
    return fetch(siteRoot() + "data/favorites_public.json", { cache: "no-cache" })
      .then((r) => (r.ok ? r.json() : []))
      .then((arr) => { _publicCache = Array.isArray(arr) ? arr : []; return _publicCache; })
      .catch(() => []);
  }

  const UNCATEGORIZED = "未分类";

  // Category label for a paper. Overview pages: nearest preceding section
  // heading (the topic group). Stripped of the trailing "(causal, N 篇)".
  function categoryFromHeading(h) {
    if (!h) return UNCATEGORIZED;
    const level = parseInt(h.tagName.slice(1), 10);
    const all = Array.from(document.querySelectorAll("h1,h2,h3,h4,h5,h6"));
    let idx = all.indexOf(h);
    for (let i = idx - 1; i >= 0; i--) {
      const lv = parseInt(all[i].tagName.slice(1), 10);
      if (lv < level) {
        let t = (all[i].textContent || "").replace(/¶/g, "").trim();
        t = t.split(/\s*[\(（*]/)[0].trim();
        // Skip the daily wrapper headings ("⭐ 高相关论文 …").
        if (/高相关|中相关|会议|Seminar/.test(t)) continue;
        return t || UNCATEGORIZED;
      }
    }
    return UNCATEGORIZED;
  }

  // ── badges (read + favorite) ────────────────────────────────────────────────
  function makeBadge(cls, role) {
    const b = document.createElement("span");
    b.className = cls;
    if (role) b.setAttribute("role", "button");
    return b;
  }

  function addReadBadge(pl) {
    const link = pl.link;
    if (link.dataset.rnReadBadge) return;
    link.dataset.rnReadBadge = "1";
    const badge = makeBadge("rn-read-badge", "button");
    badge.title = "点击切换已读 / 未读";
    function refresh() {
      const read = isRead(pl.paperId);
      badge.textContent = read ? "✓ 已读" : "○ 未读";
      badge.classList.toggle("rn-read", read);
      badge.classList.toggle("rn-unread", !read);
    }
    badge.addEventListener("click", (e) => {
      e.preventDefault(); e.stopPropagation();
      toggleRead(pl.paperId); refresh();
    });
    refresh();
    link.insertAdjacentElement("afterend", badge);
  }

  function addFavBadge(pl, byId) {
    const link = pl.link;
    if (link.dataset.rnFavBadge) return;
    link.dataset.rnFavBadge = "1";
    const badge = makeBadge("rn-fav-badge", "button");
    const drEntry = byId && byId.get(pl.paperId);
    function refresh() {
      const fav = isFav(pl.paperId);
      badge.textContent = fav ? "★ 已收藏" : "☆ 收藏";
      badge.title = fav ? "已收藏，点击移除" : "加入收藏";
      badge.classList.toggle("rn-fav-on", fav);
    }
    badge.addEventListener("click", (e) => {
      e.preventDefault(); e.stopPropagation();
      toggleFav({
        paperId: pl.paperId,
        title: pl.title,
        url: pl.url,
        deepReadUrl: drEntry ? deepReadHref(drEntry) : "",
        source: pageLabel(),
        sourceUrl: location.pathname,
        category: categoryFromHeading(pl.heading),
        date: pageDate(),
      });
      refresh();
    });
    refresh();
    // Put the star last so it sits after the "🔍 精读" link when present.
    link.parentElement.appendChild(badge);
  }

  function addDeepReadLink(pl, byId) {
    const link = pl.link;
    if (link.dataset.rnDeepLink) return;
    if (!byId.has(pl.paperId)) return;
    link.dataset.rnDeepLink = "1";
    const entry = byId.get(pl.paperId);
    const a = document.createElement("a");
    a.href = deepReadHref(entry);
    a.className = "rn-deep-link";
    a.textContent = "🔍 精读";
    a.title = entry.title || "Deep-read report";
    link.insertAdjacentElement("afterend", a);
  }

  // Deep-read pages have no paper-link heading; star the page as a whole.
  function addDeepReadPageBadge(byId, labels) {
    const h1 = document.querySelector("article h1, .md-content h1");
    if (!h1 || h1.dataset.rnFavBadge) return;
    // Resolve paper_id/title/topic from the deep-reads index via the page path.
    let paperId = null, title = (h1.textContent || "").replace(/¶/g, "").trim();
    let category = UNCATEGORIZED, dateStr = pageDate();
    // Page slug, e.g. "2026-06-01-2605.31130" (DOI-based ids keep their slug).
    const slug = location.pathname.replace(/\/$/, "").split("/").pop() || "";
    if (byId) {
      for (const e of byId.values()) {
        const base = e.doc_path.replace(/^.*\//, "").replace(/\.md$/i, "");
        if (base === slug) {
          paperId = e.paper_id;
          title = e.title || title;
          if (e.date) dateStr = e.date;
          if (labels && e.topic) category = labels.labels[e.topic] || e.topic;
          break;
        }
      }
    }
    if (!paperId) {
      // Fallback: strip the leading date prefix off the slug.
      const m = slug.match(/^\d{4}-\d{2}-\d{2}-(.+)$/);
      paperId = m ? m[1] : slug;
    }
    h1.dataset.rnFavBadge = "1";

    // Read / unread toggle for the paper as a whole.
    const readBadge = makeBadge("rn-read-badge", "button");
    readBadge.title = "点击切换已读 / 未读";
    function refreshRead() {
      const read = isRead(paperId);
      readBadge.textContent = read ? "✓ 已读" : "○ 未读";
      readBadge.classList.toggle("rn-read", read);
      readBadge.classList.toggle("rn-unread", !read);
    }
    readBadge.addEventListener("click", (e) => {
      e.preventDefault(); e.stopPropagation();
      toggleRead(paperId); refreshRead();
    });
    refreshRead();
    h1.appendChild(readBadge);

    const badge = makeBadge("rn-fav-badge", "button");
    function refresh() {
      const fav = isFav(paperId);
      badge.textContent = fav ? "★ 已收藏" : "☆ 收藏";
      badge.title = fav ? "已收藏，点击移除" : "加入收藏";
      badge.classList.toggle("rn-fav-on", fav);
    }
    badge.addEventListener("click", (e) => {
      e.preventDefault(); e.stopPropagation();
      toggleFav({
        paperId: paperId,
        title: title,
        url: location.pathname,
        deepReadUrl: location.pathname,
        source: "精读 · " + title,
        sourceUrl: location.pathname,
        category: category,
        date: dateStr,
      });
      refresh();
    });
    refresh();
    h1.appendChild(badge);
  }

  // ── account panel (bottom-right) ──────────────────────────────────────────
  function buildAccountUI() {
    if (document.getElementById("rn-account-btn")) return;

    const btn = document.createElement("button");
    btn.id = "rn-account-btn";
    btn.type = "button";

    const panel = document.createElement("div");
    panel.id = "rn-account-panel";
    panel.hidden = true;

    function refreshBtn() {
      btn.textContent = loggedIn() ? "👤 已登录" : (getToken() ? "👤 连接中…" : "👤 登录");
    }

    function renderPanel() {
      const favCount = Object.keys(state.favorites).length;
      const readCount = Object.keys(state.read).length;
      const favHref = siteRoot() + "favorites/";
      if (loggedIn()) {
        panel.innerHTML =
          '<div class="rn-ap-row"><strong>已登录</strong> · gist <code>' +
          getGistId().slice(0, 8) + '…</code></div>' +
          '<div class="rn-ap-row">收藏 <b>' + favCount + '</b> 篇 · 已读 <b>' +
          readCount + '</b> 篇</div>' +
          '<div class="rn-ap-row"><a href="' + favHref + '">→ 打开收藏</a></div>' +
          '<div class="rn-ap-row"><button id="rn-logout" type="button">退出登录</button></div>';
        const out = panel.querySelector("#rn-logout");
        if (out) out.addEventListener("click", () => {
          lsDel(TOKEN_KEY); lsDel(GIST_ID_KEY); gistReady = false; _synced = false;
          refreshBtn(); renderPanel();
        });
      } else {
        panel.innerHTML =
          '<div class="rn-ap-row"><strong>用 GitHub Token 登录</strong></div>' +
          '<div class="rn-ap-hint">需要一个带 <code>gist</code> 权限的 ' +
          'Personal Access Token（classic）。已读状态与周报收藏会存进你账号下的一个' +
          '私密 Gist，多设备同步。<a href="https://github.com/settings/tokens/new?scopes=gist&description=research-news" ' +
          'target="_blank" rel="noopener">→ 点此创建 Token</a></div>' +
          '<div class="rn-ap-row"><input id="rn-token-in" type="password" ' +
          'placeholder="ghp_… 粘贴 token" autocomplete="off"></div>' +
          '<div class="rn-ap-row"><button id="rn-login" type="button">登录</button></div>';
        const inp = panel.querySelector("#rn-token-in");
        const go = panel.querySelector("#rn-login");
        go.addEventListener("click", async () => {
          const t = (inp.value || "").trim();
          if (!t) return;
          lsSet(TOKEN_KEY, t);
          go.textContent = "登录中…"; go.disabled = true;
          const ok = await ensureGist();
          if (ok) { await pullGist(); await pushGist(); _synced = true; }
          else { lsDel(TOKEN_KEY); alert("登录失败：token 无效或没有 gist 权限。"); }
          refreshBtn(); renderPanel(); refreshAllBadges();
        });
        inp.addEventListener("keydown", (e) => { if (e.key === "Enter") go.click(); });
      }
    }

    btn.addEventListener("click", () => {
      panel.hidden = !panel.hidden;
      if (!panel.hidden) renderPanel();
    });

    refreshBtn();
    document.body.appendChild(btn);
    document.body.appendChild(panel);
  }

  // ── collection page (收藏) ───────────────────────────────────────────────────
  function getView() { return lsGet(VIEW_KEY) === "week" ? "week" : "total"; }
  function setView(v) { lsSet(VIEW_KEY, v); }

  function dateDesc(a, b) {
    const d = (b.date || "").localeCompare(a.date || "");
    return d !== 0 ? d : (b.added || "").localeCompare(a.added || "");
  }

  // Order categories by the report taxonomy, with unknown ones last.
  function orderedCategories(present, ordering) {
    const seen = new Set(present);
    const out = [];
    (ordering || []).forEach((c) => { if (seen.has(c)) { out.push(c); seen.delete(c); } });
    Array.from(seen).sort().forEach((c) => out.push(c));
    // Always sink "未分类" to the very end.
    return out.filter((c) => c !== UNCATEGORIZED)
      .concat(out.includes(UNCATEGORIZED) ? [UNCATEGORIZED] : []);
  }

  function groupBy(favs, key) {
    const g = {};
    favs.forEach((f) => { const k = f[key] || UNCATEGORIZED; (g[k] = g[k] || []).push(f); });
    return g;
  }

  function favItemHtml(f, readonly) {
    const read = (!readonly && isRead(f.paper_id))
      ? '<span class="rn-c-read">✓ 已读</span>' : '';
    const dr = f.deep_read_url ? ' · <a href="' + f.deep_read_url + '" target="_blank" rel="noopener noreferrer">🔍 精读</a>' : '';
    const metaBits = [f.date || "", f.venue || f.source || ""];
    if (f.score != null) metaBits.push("相关性 " + Math.round(f.score) + "/10");
    const meta = metaBits.filter(Boolean).map(escapeHtml).join(" · ");
    const summary = f.summary
      ? '<div class="rn-c-summary">' + escapeHtml(f.summary) + '</div>' : '';
    const note = f.note
      ? '<div class="rn-c-note" data-id="' + escapeHtml(f.paper_id) + '">' +
        '💬 ' + escapeHtml(f.note) + '</div>'
      : '';
    const rm = readonly ? '' :
      '<button class="rn-c-rm" title="移除收藏" type="button">✕</button>';
    const editBtn = readonly ? '' :
      ' · <button class="rn-c-edit" type="button">✎ ' + (f.note ? '改评论' : '评论') + '</button>';
    return (
      '<li data-id="' + escapeHtml(f.paper_id) + '">' +
      '<a class="rn-c-title" href="' + (f.url || "#") + '">' + escapeHtml(f.title) + '</a> ' +
      read + dr + rm +
      '<div class="rn-c-meta">' + meta + editBtn + '</div>' +
      summary + note +
      '</li>'
    );
  }

  function renderCollection() {
    const host = document.getElementById("rn-collection");
    if (!host) return;
    if (active()) {
      renderFavs(host, Object.values(state.favorites), false);
    } else {
      loadPublicFavs().then((favs) => {
        if (favs && favs.length) renderFavs(host, favs, true);
        else host.innerHTML = '<p class="rn-c-empty">还没有公开的收藏。' +
          '点右下角 <b>👤 登录</b> 可管理你自己的收藏。</p>';
      });
    }
  }

  function renderFavs(host, favs, readonly) {
    loadTopicLabels().then((labels) => {
      const view = getView();
      const parts = [];
      parts.push(
        '<div class="rn-c-bar">' +
        '<span class="rn-c-views">' +
        '<button data-view="total" class="' + (view === "total" ? "on" : "") + '" type="button">总收藏</button>' +
        '<button data-view="week" class="' + (view === "week" ? "on" : "") + '" type="button">按周</button>' +
        '</span>' +
        '<button id="rn-c-md" type="button">复制为 Markdown</button>' +
        '</div>'
      );
      if (readonly) {
        parts.push('<p class="rn-c-pubnote">📖 这是公开收藏快照（每日自动刷新）。' +
          '登录后可在此管理你自己的收藏。</p>');
      }

      const itemsHtml = (arr) =>
        '<ul class="rn-c-list">' +
        arr.slice().sort(dateDesc).map((f) => favItemHtml(f, readonly)).join("") +
        '</ul>';

      if (!favs.length) {
        parts.push('<p class="rn-c-empty">还没有收藏。去日报 / 期刊 / 精读页面，' +
          '点论文旁的 <b>☆ 收藏</b> 把它加进来。</p>');
      } else if (view === "total") {
        const byCat = groupBy(favs, "category");
        orderedCategories(Object.keys(byCat), labels.orderedLabels).forEach((cat) => {
          parts.push('<h2>' + escapeHtml(cat) + ' <small>(' + byCat[cat].length + ' 篇)</small></h2>');
          parts.push(itemsHtml(byCat[cat]));
        });
      } else {
        const byWeek = groupBy(favs, "week");
        Object.keys(byWeek).sort().reverse().forEach((w) => {
          parts.push('<h2>' + escapeHtml(w || "未归周") + ' <small>(' + byWeek[w].length + ' 篇)</small></h2>');
          const byCat = groupBy(byWeek[w], "category");
          orderedCategories(Object.keys(byCat), labels.orderedLabels).forEach((cat) => {
            parts.push('<h3>' + escapeHtml(cat) + '</h3>');
            parts.push(itemsHtml(byCat[cat]));
          });
        });
      }
      host.innerHTML = parts.join("");
      wireCollection(host, favs, labels, readonly);
    });
  }

  function wireCollection(host, favs, labels, readonly) {
    host.querySelectorAll(".rn-c-views button").forEach((b) => {
      b.addEventListener("click", () => { setView(b.getAttribute("data-view")); renderCollection(); });
    });
    const mdBtn = host.querySelector("#rn-c-md");
    if (mdBtn) mdBtn.addEventListener("click", () => copyCollectionMarkdown(favs, labels));
    if (readonly) return;
    host.querySelectorAll(".rn-c-rm").forEach((b) => {
      b.addEventListener("click", () => {
        const li = b.closest("li");
        if (li) removeFav(li.getAttribute("data-id"));
      });
    });
    host.querySelectorAll(".rn-c-edit").forEach((b) => {
      b.addEventListener("click", () => {
        const li = b.closest("li");
        if (li) openNoteEditor(li);
      });
    });
  }

  function openNoteEditor(li) {
    if (li.querySelector(".rn-c-note-edit")) return;
    const id = li.getAttribute("data-id");
    const fav = state.favorites[id];
    if (!fav) return;
    const box = document.createElement("div");
    box.className = "rn-c-note-edit";
    const ta = document.createElement("textarea");
    ta.value = fav.note || "";
    ta.placeholder = "写点评论 / 笔记…";
    const save = document.createElement("button");
    save.type = "button"; save.textContent = "保存";
    save.addEventListener("click", () => { setNote(id, ta.value.trim()); renderCollection(); });
    box.appendChild(ta);
    box.appendChild(save);
    li.appendChild(box);
    ta.focus();
  }

  function copyCollectionMarkdown(favs, labels) {
    const lines = ["# 收藏", ""];
    if (getView() === "week") {
      const byWeek = groupBy(favs, "week");
      Object.keys(byWeek).sort().reverse().forEach((w) => {
        lines.push("## " + w, "");
        const byCat = groupBy(byWeek[w], "category");
        orderedCategories(Object.keys(byCat), labels.orderedLabels).forEach((cat) => {
          lines.push("### " + cat, "");
          byCat[cat].slice().sort(dateDesc).forEach((f) => lines.push(mdLine(f)));
          lines.push("");
        });
      });
    } else {
      const byCat = groupBy(favs, "category");
      orderedCategories(Object.keys(byCat), labels.orderedLabels).forEach((cat) => {
        lines.push("## " + cat, "");
        byCat[cat].slice().sort(dateDesc).forEach((f) => lines.push(mdLine(f)));
        lines.push("");
      });
    }
    const text = lines.join("\n");
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(
      () => alert("已复制为 Markdown。"), () => prompt("复制以下内容：", text));
    else prompt("复制以下内容：", text);
  }

  function mdLine(f) {
    const link = f.deep_read_url || f.url || "";
    let s = "- [" + f.title + "](" + link + ")";
    if (f.date) s += "  · " + f.date;
    if (f.note) s += "  — " + f.note;
    return s;
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    }[c]));
  }

  // ── styles ──────────────────────────────────────────────────────────────────
  function ensureStyles() {
    if (document.getElementById("rn-extras-style")) return;
    const css = `
      .rn-read-badge, .rn-fav-badge {
        display: inline-block; margin-left: 0.4em; padding: 0 0.4em;
        font-size: 0.7em; line-height: 1.5; border-radius: 0.25em;
        cursor: pointer; user-select: none; vertical-align: middle;
        border: 1px solid transparent; font-weight: normal;
      }
      .rn-read-badge.rn-read   { color: #5a5a5a; background: #eee; border-color: #ddd; }
      .rn-read-badge.rn-unread { color: #b06b00; background: #fff3d6; border-color: #f0d28a; }
      .rn-fav-badge            { color: #8a6500; background: #fff7d6; border-color: #e6c200; }
      .rn-fav-badge.rn-fav-on  { color: #fff; background: #e0a800; border-color: #c79100; }
      [data-md-color-scheme="slate"] .rn-read-badge.rn-read   { color: #aaa; background: #2a2a2a; border-color: #444; }
      [data-md-color-scheme="slate"] .rn-read-badge.rn-unread { color: #ffc34d; background: #3a2f10; border-color: #6a5310; }
      [data-md-color-scheme="slate"] .rn-fav-badge            { color: #ffd966; background: #3a2f10; border-color: #806000; }
      [data-md-color-scheme="slate"] .rn-fav-badge.rn-fav-on  { color: #1a1400; background: #ffce3a; border-color: #ffce3a; }

      .rn-deep-link {
        display: inline-block; margin-left: 0.5em; padding: 0 0.45em;
        font-size: 0.75em; line-height: 1.6; border-radius: 0.3em;
        background: #fff7d6; color: #8a6500 !important; border: 1px solid #e6c200;
        text-decoration: none !important; vertical-align: middle; font-weight: normal;
      }
      .rn-deep-link:hover { background: #ffeaa3; }
      [data-md-color-scheme="slate"] .rn-deep-link {
        background: #3a2f10; color: #ffd966 !important; border-color: #806000;
      }

      #rn-account-btn {
        position: fixed; right: 1rem; bottom: 1rem; z-index: 30;
        padding: 0.45em 0.8em; border-radius: 2em; border: 1px solid #c79100;
        background: #ffce3a; color: #1a1400; font-size: 0.78rem; cursor: pointer;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
      }
      #rn-account-panel {
        position: fixed; right: 1rem; bottom: 3.4rem; z-index: 30; width: 19rem;
        max-width: calc(100vw - 2rem); padding: 0.9em 1em; border-radius: 0.5em;
        background: var(--md-default-bg-color, #fff); color: var(--md-default-fg-color, #222);
        border: 1px solid rgba(0,0,0,0.18); box-shadow: 0 4px 18px rgba(0,0,0,0.22);
        font-size: 0.82rem;
      }
      #rn-account-panel .rn-ap-row { margin: 0.5em 0; }
      #rn-account-panel .rn-ap-hint { font-size: 0.74rem; opacity: 0.85; line-height: 1.5; }
      #rn-account-panel input { width: 100%; padding: 0.4em; box-sizing: border-box;
        border: 1px solid rgba(0,0,0,0.25); border-radius: 0.3em;
        background: var(--md-default-bg-color, #fff); color: var(--md-default-fg-color, #222); }
      #rn-account-panel button { padding: 0.35em 0.9em; border-radius: 0.3em;
        border: 1px solid #c79100; background: #ffce3a; color: #1a1400; cursor: pointer; }
      #rn-account-panel a { color: var(--md-primary-fg-color, #3f51b5); }

      .rn-c-bar { display: flex; gap: 0.6em; align-items: center; flex-wrap: wrap;
        margin: 0.5em 0 1em; }
      .rn-c-bar button { padding: 0.3em 0.8em; border-radius: 0.3em; cursor: pointer;
        border: 1px solid #c79100; background: #fff7d6; color: #8a6500; }
      .rn-c-views { display: inline-flex; }
      .rn-c-views button { border-radius: 0; }
      .rn-c-views button:first-child { border-radius: 0.3em 0 0 0.3em; }
      .rn-c-views button:last-child { border-radius: 0 0.3em 0.3em 0; border-left: none; }
      .rn-c-views button.on { background: #ffce3a; color: #1a1400; font-weight: 600; }
      .rn-c-list { list-style: none; padding-left: 0; }
      .rn-c-list li { margin: 0.5em 0; padding: 0.4em 0; border-bottom: 1px dashed rgba(0,0,0,0.12); }
      .rn-c-title { font-weight: 600; }
      .rn-c-read { font-size: 0.75em; color: #5a5a5a; background: #eee;
        border-radius: 0.25em; padding: 0 0.4em; margin-left: 0.3em; }
      .rn-c-meta { font-size: 0.78em; opacity: 0.75; margin-top: 0.15em; }
      .rn-c-meta .rn-c-edit { border: none; background: transparent; cursor: pointer;
        color: var(--md-primary-fg-color, #3f51b5); font-size: 1em; padding: 0; }
      .rn-c-summary { font-size: 0.88em; margin-top: 0.3em; opacity: 0.92; line-height: 1.6; }
      .rn-c-note { font-size: 0.86em; margin-top: 0.3em; padding: 0.35em 0.6em;
        border-left: 3px solid #e6c200; background: rgba(230,194,0,0.08); white-space: pre-wrap; }
      .rn-c-pubnote { font-size: 0.82em; opacity: 0.8; margin: 0.2em 0 1em;
        padding: 0.4em 0.6em; border-left: 3px solid var(--md-primary-fg-color, #3f51b5);
        background: rgba(63,81,181,0.06); }
      .rn-c-note-edit { margin-top: 0.3em; }
      .rn-c-note-edit textarea { width: 100%; min-height: 3.5em; box-sizing: border-box;
        padding: 0.4em; border: 1px solid rgba(0,0,0,0.25); border-radius: 0.3em;
        background: var(--md-default-bg-color, #fff); color: var(--md-default-fg-color, #222); }
      .rn-c-note-edit button { margin-top: 0.3em; padding: 0.25em 0.8em; border-radius: 0.3em;
        border: 1px solid #c79100; background: #ffce3a; color: #1a1400; cursor: pointer; }
      .rn-c-rm { float: right; border: none; background: transparent; cursor: pointer;
        color: #b00; font-size: 0.9em; }
      .rn-c-empty { opacity: 0.8; }
    `;
    const style = document.createElement("style");
    style.id = "rn-extras-style";
    style.textContent = css;
    document.head.appendChild(style);
  }

  // ── lifecycle ────────────────────────────────────────────────────────────────
  function refreshAllBadges() {
    // Re-run badge attachment + collection render after state changes (login).
    decoratePage();
    renderCollection();
  }

  function decoratePage() {
    if (isDeepReadPage()) {
      Promise.all([loadDeepReads(), loadTopicLabels()]).then(([byId, labels]) => {
        if (active()) addDeepReadPageBadge(byId, labels);
      });
      return;
    }
    if (!isOverviewPage()) return;
    const paperLinks = findPaperLinks();
    if (!paperLinks.length) return;
    loadDeepReads().then((byId) => {
      paperLinks.forEach((pl) => addDeepReadLink(pl, byId));
      if (active()) {
        paperLinks.forEach((pl) => {
          addReadBadge(pl);
          addFavBadge(pl, byId);
        });
      }
    });
  }

  async function init() {
    ensureStyles();
    loadLocal();
    buildAccountUI();
    decoratePage();
    renderCollection();
    // Bring in remote state (gist) once per session if signed in, then redraw.
    // Instant-navigation re-runs skip this to avoid clobbering pending edits.
    if (getToken() && !_synced) {
      _synced = true;
      const ok = await ensureGist();
      if (ok) { await pullGist(); refreshAllBadges(); }
    }
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(() => init());
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
