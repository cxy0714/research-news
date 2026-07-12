// Pagefind-backed on-site search, mounted on the dedicated /search/ page.
//
// Why not the Material header search box: the built-in lunr search downloads
// the whole corpus and builds the index in the browser, which no longer scales
// past a few thousand pages. Pagefind ships a sharded index (built at deploy
// time by `pagefind --site site`) and fetches only the fragments a query needs.
//
// This file only does the front-end wiring: on the search page it lazy-loads
// Pagefind's own UI bundle and mounts it into #pagefind-search. Everything is
// hung off Material's `document$` observable so it re-runs correctly under
// `navigation.instant` (client-side page swaps don't re-execute inline script).

(function () {
  "use strict";

  var CSS_HREF = "../pagefind/pagefind-ui.css";
  var JS_SRC = "../pagefind/pagefind-ui.js";
  var BUNDLE_PATH = "../pagefind/";

  var cssLoaded = false;
  var jsLoading = null; // Promise, so concurrent mounts share one load.

  function loadCss() {
    if (cssLoaded) return;
    var link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = CSS_HREF;
    document.head.appendChild(link);
    cssLoaded = true;
  }

  function loadJs() {
    if (jsLoading) return jsLoading;
    jsLoading = new Promise(function (resolve, reject) {
      // PagefindUI is a global registered by the UMD bundle.
      if (window.PagefindUI) {
        resolve();
        return;
      }
      var s = document.createElement("script");
      s.src = JS_SRC;
      s.onload = function () { resolve(); };
      s.onerror = function () {
        jsLoading = null; // allow a later retry on re-navigation
        reject(new Error("failed to load pagefind-ui.js"));
      };
      document.head.appendChild(s);
    });
    return jsLoading;
  }

  function mount() {
    var host = document.getElementById("pagefind-search");
    if (!host) return; // not the search page
    if (host.dataset.pagefindMounted === "1") return; // already mounted on this node
    host.dataset.pagefindMounted = "1";

    loadCss();
    loadJs()
      .then(function () {
        host.innerHTML = ""; // drop the loading placeholder
        // eslint-disable-next-line no-new
        new window.PagefindUI({
          element: "#pagefind-search",
          bundlePath: BUNDLE_PATH,
          showSubResults: true,
          showImages: false,
          pageSize: 10,
          translations: {
            placeholder: "搜索站内内容……",
            clear_search: "清除",
            load_more: "加载更多结果",
            search_label: "站内搜索",
            zero_results: "没有找到与「[SEARCH_TERM]」相关的结果",
            many_results: "找到 [COUNT] 条与「[SEARCH_TERM]」相关的结果",
            one_result: "找到 [COUNT] 条与「[SEARCH_TERM]」相关的结果",
            searching: "正在搜索「[SEARCH_TERM]」……"
          }
        });
      })
      .catch(function (err) {
        host.dataset.pagefindMounted = ""; // permit retry
        host.innerHTML =
          '<p class="pagefind-loading">搜索暂不可用：' +
          (err && err.message ? err.message : "加载失败") +
          "。（本地预览需先运行 Pagefind 构建脚本。）</p>";
      });
  }

  // Material emits `document$` on first load and after every instant-nav swap.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(mount);
  } else if (document.readyState !== "loading") {
    mount();
  } else {
    document.addEventListener("DOMContentLoaded", mount);
  }
})();
