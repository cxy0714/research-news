window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

if (typeof document$ !== "undefined" && document$.subscribe) {
  document$.subscribe(() => {
    if (window.MathJax && MathJax.startup && MathJax.typesetPromise) {
      MathJax.startup.document.state(0);
      MathJax.texReset && MathJax.texReset();
      MathJax.typesetPromise();
    }
  });
}
