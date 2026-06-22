"""Tests for the display-math build hook (mkdocs_hooks.py).

The hook protects display math (``\\[ ... \\]`` / ``$$ ... $$``) from Markdown's
block/indent rules by swapping it for inert placeholders before parsing and
restoring it as ``<div class="arithmatex">`` afterwards. The core protect /
restore logic is tested without any Markdown dependency; an end-to-end render
test runs only when ``markdown`` + ``pymdownx`` are installed (the docs env).
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_HOOK_PATH = Path(__file__).resolve().parent.parent / "mkdocs_hooks.py"
_spec = importlib.util.spec_from_file_location("mkdocs_hooks", _HOOK_PATH)
hooks = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hooks)


class _Page:  # unique identity per render, mimics an mkdocs Page
    pass


# ── protect step (on_page_markdown) ──────────────────────────────────────────

def test_display_block_replaced_by_placeholder():
    md = "**定理**：\n\\[\na = b\n\\]\n即如此。"
    out = hooks.on_page_markdown(md, page=_Page())
    assert "\\[" not in out and "\\]" not in out  # delimiters removed
    assert hooks._PH_RE.search(out)               # placeholder injected


def test_dollar_display_replaced():
    out = hooks.on_page_markdown("文字\n$$x=y$$\n更多", page=_Page())
    assert "$$" not in out
    assert hooks._PH_RE.search(out)


def test_inline_math_is_left_for_arithmatex():
    # Inline \( \) and single $ ... $ must NOT be captured (arithmatex owns them).
    md = r"取 \( n^{1/2} \) 与 $x^2$ 显著。"
    out = hooks.on_page_markdown(md, page=_Page())
    assert out == md


def test_code_with_dollars_is_not_treated_as_math():
    md = "- `$N$`：总人口。\n\n```\n$$not math$$\n```\n"
    out = hooks.on_page_markdown(md, page=_Page())
    assert "`$N$`" in out          # inline code untouched
    assert "$$not math$$" in out   # fenced code untouched
    assert not hooks._PH_RE.search(out)


def test_citation_brackets_are_not_math():
    # \[22, 23] is an escaped citation bracket (no closing \]) — leave it alone.
    md = "见 Gross & Taylor \\[22, 23]: 基石工作。"
    out = hooks.on_page_markdown(md, page=_Page())
    assert out == md


# ── restore step (on_page_content) ───────────────────────────────────────────

def test_restore_wraps_in_arithmatex_div():
    page = _Page()
    md = "前言\n\\[\n\\alpha + \\beta\n\\]\n后语"
    hooks.on_page_markdown(md, page=page)
    # Simulate a placeholder that markdown wrapped in its own <p>.
    html = f"<p>前言</p>\n<p>{hooks._PH.format(0)}</p>\n<p>后语</p>"
    restored = hooks.on_page_content(html, page=page)
    assert '<div class="arithmatex">\\[\\alpha + \\beta\\]</div>' in restored
    assert hooks._PH_RE.search(restored) is None  # no placeholder left


def test_dollar_display_normalised_to_bracket_delimiters():
    # MathJax here only recognises \[ \] for display, so $$ must become \[ \].
    page = _Page()
    hooks.on_page_markdown("$$E = mc^2$$", page=page)
    restored = hooks.on_page_content(f"<p>{hooks._PH.format(0)}</p>", page=page)
    assert restored == '<div class="arithmatex">\\[E = mc^2\\]</div>'


def test_page_without_math_is_untouched():
    page = _Page()
    md = "纯文本，没有公式。"
    assert hooks.on_page_markdown(md, page=page) == md
    assert hooks.on_page_content("<p>纯文本</p>", page=page) == "<p>纯文本</p>"


# ── end-to-end through Markdown + arithmatex (docs env only) ──────────────────

def _render(md_text: str) -> str:
    markdown = pytest.importorskip("markdown")
    pytest.importorskip("pymdownx")
    page = _Page()
    md_text = hooks.on_page_markdown(md_text, page=page)
    html = markdown.Markdown(
        extensions=["pymdownx.arithmatex"],
        extension_configs={"pymdownx.arithmatex": {"generic": True}},
    ).convert(md_text)
    return hooks.on_page_content(html, page=page)


def test_e2e_reported_theorem_case_renders():
    # The exact failure the user reported: a \[ \] block glued under a text line.
    md = (
        "**定理1**（下界）：  \n"
        "\\[\n"
        "\\liminf_{n} (\\tilde{\\theta} - \\theta_0)^2 \\ge c > 0.\n"
        "\\]\n"
        "即 minimax 不好于 \\( n^{-s} \\)。"
    )
    html = _render(md)
    assert '<div class="arithmatex">' in html
    assert "\\liminf" in html
    # the inline \( \) is still handled by arithmatex
    assert '<span class="arithmatex">' in html


def test_e2e_ordered_list_numbering_preserved():
    md = (
        "1. **步骤一**：得到\n"
        "   \\[\n   y = x\n   \\]\n"
        "   然后：\n"
        "   \\[\n   z = w\n   \\]\n"
        "2. **步骤二**。\n"
        "3. **步骤三**。"
    )
    html = _render(md)
    assert html.count('<div class="arithmatex">') == 2  # both equations render
    assert html.count("<ol>") == 1                      # numbering not split
    assert html.count("<li>") == 3
