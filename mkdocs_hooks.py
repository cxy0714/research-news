"""MkDocs build hooks.

Display-math robustness
-----------------------
``pymdownx.arithmatex`` only recognises *display* math (``\\[ ... \\]`` and
``$$ ... $$``) when the delimiters sit in their own Markdown block — i.e. with
a blank line before and after, and (inside a list) at a 4-space-multiple
indent. A great deal of the LLM-generated content writes display math glued
directly under a line of text or inside a list item without that separation,
e.g.

    **定理1**：
    \\[
    \\liminf_n (\\tilde\\theta-\\theta_0)^2 \\ge c
    \\]
    即 ...

Markdown then treats ``\\[``/``\\]`` as escaped brackets (``\\[`` → ``[``),
collapses the newlines, and even turns ``_`` inside the formula into ``<em>``.
The equation renders as raw text like ``[ \\liminf_n ... ]``.

Fixing this in the source would mean reflowing ~1700 list-embedded blocks to
exact Markdown indentation — fragile and version-dependent. Instead we protect
display math *before* Markdown sees it and restore it *after*:

* ``on_page_markdown`` swaps every display-math block for an inert, alnum-only
  placeholder token (skipping fenced/inline code so literal ``$``/``\\[`` in
  code spans are left alone). Placeholders survive Markdown untouched and work
  in any context — list item, mid-paragraph, any indent.
* ``on_page_content`` swaps the placeholders back in as
  ``<div class="arithmatex">\\[ ... \\]</div>``, exactly the markup
  ``arithmatex`` (generic) emits, so the existing MathJax config renders them.

Inline math (``\\( ... \\)`` / ``$ ... $``) still works everywhere, so it is
left to ``arithmatex`` and not touched here.
"""
from __future__ import annotations

import re

# Placeholder must be alnum-only so Markdown never escapes, emphasises or
# line-breaks it, and distinctive enough never to occur in real prose.
_PH = "xARITHMATEXDISPLAYx{}xENDx"
_PH_RE = re.compile(r"xARITHMATEXDISPLAYx(\d+)xENDx")

# Ordered alternation: a fenced code block or inline code span is matched
# *before* any math delimiter, so ``$$``/``\[`` living inside code is consumed
# as code and never mistaken for a formula. Only the math groups are rewritten.
_SCAN = re.compile(
    r"(?P<fence>^[ \t]*(?P<f>`{3,}|~{3,})[^\n]*\n.*?^[ \t]*(?P=f)[ \t]*$)"
    r"|(?P<icode>`+[^`\n]*?`+)"
    r"|(?P<bracket>\\\[.*?\\\])"
    r"|(?P<dollar>\$\$.+?\$\$)",
    re.S | re.M,
)

# Per-page stash of extracted formulas, keyed by id(page).
_STORE: dict[int, list[str]] = {}


def _inner(token: str) -> str:
    """Strip the outer display delimiters, returning just the LaTeX body."""
    s = token.strip()
    if s.startswith("\\[") and s.endswith("\\]"):
        return s[2:-2].strip()
    if s.startswith("$$") and s.endswith("$$"):
        return s[2:-2].strip()
    return s


def on_page_markdown(markdown: str, *, page=None, **__) -> str:
    formulas: list[str] = []

    def repl(m: re.Match) -> str:
        if m.lastgroup in ("fence", "icode"):
            return m.group(0)  # leave code exactly as-is
        formulas.append(_inner(m.group(0)))
        return _PH.format(len(formulas) - 1)

    out = _SCAN.sub(repl, markdown)
    if page is not None:
        _STORE[id(page)] = formulas
    return out


def on_page_content(html: str, *, page=None, **__) -> str:
    formulas = _STORE.pop(id(page), None) if page is not None else None
    if not formulas:
        return html

    def div(i: int) -> str:
        return f'<div class="arithmatex">\\[{formulas[i]}\\]</div>'

    # If a placeholder is the whole paragraph, replace the <p> wrapper too so we
    # don't nest a <div> inside a <p>.
    html = re.sub(
        r"<p>\s*" + _PH_RE.pattern + r"\s*</p>",
        lambda m: div(int(m.group(1))),
        html,
    )
    # Any remaining placeholders (inside <li>, mixed with text, etc.).
    html = _PH_RE.sub(lambda m: div(int(m.group(1))), html)
    return html
