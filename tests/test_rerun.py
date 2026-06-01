"""Tests for the garbled-summary detection / salvage / rerun logic.

These cover the offline paths only — no LLM is called."""
from __future__ import annotations

from pathlib import Path

from research_news.llm.pipeline import (
    _strip_code_fence,
    salvage_summary_fields,
    summary_looks_garbled,
)
from research_news.render.markdown import RERUN_MARKER
from research_news import rerun


# ── pipeline helpers ──────────────────────────────────────────────────────────

def test_strip_code_fence():
    assert _strip_code_fence("```json\n{\"a\": 1}\n```") == '{"a": 1}'
    # Truncated output keeps only the opening fence.
    assert _strip_code_fence("```json\n{\"a\": 1") == '{"a": 1'
    assert _strip_code_fence('{"a": 1}') == '{"a": 1}'


def test_summary_looks_garbled():
    assert summary_looks_garbled("```json\n{...")
    assert summary_looks_garbled('{\n  "topic": "x"')
    assert summary_looks_garbled('{"summary_zh": "...')
    assert not summary_looks_garbled("在观察性研究中，未观测混杂是核心难题。")
    assert not summary_looks_garbled("")
    assert not summary_looks_garbled(None)


def test_salvage_complete_prose_with_inner_quotes_and_truncated_array():
    # summary_zh has unescaped inner quotes; key_techniques is cut off.
    blob = (
        "```json\n{\n"
        '  "topic": "econ_theory",\n'
        '  "summary_zh": "构建"非伪造模型集"，得到 markup 的区间。",\n'
        '  "key_techniques": [\n'
        '    "markup estimation",\n'
        '    "production func'
    )
    out = salvage_summary_fields(blob)
    assert out["topic"] == "econ_theory"
    assert "非伪造模型集" in out["summary_zh"]
    # Only the complete array item survives; the truncated tail is dropped.
    assert out["key_techniques"] == ["markup estimation"]


def test_salvage_drops_truncated_summary():
    # summary_zh itself was cut off mid-sentence — nothing safe to recover.
    blob = '{\n "topic": "causal_inference",\n "summary_zh": "在模型下，直接连接您 primary i'
    out = salvage_summary_fields(blob)
    assert "summary_zh" not in out


def test_salvage_summary_as_last_field():
    blob = '{"topic": "x", "summary_zh": "完整的中文摘要。"}'
    out = salvage_summary_fields(blob)
    assert out["summary_zh"] == "完整的中文摘要。"


# ── markdown block driver ─────────────────────────────────────────────────────

_GARBLED_MD = """# 2026-06-01 每日 arXiv 资讯

## ⭐ 高相关论文（按主题分组）

### 因果推断  *(causal_inference, 1 篇)*

#### 1. [2605.99999](https://arxiv.org/abs/2605.99999) — Some clean paper
- **作者**: Jane Doe
- **分类**: stat.ME
- 相关性 8/10
- **摘要**: 这是一个干净的摘要，不应被改动。
- **关键技术**: `method a`

#### 2. [2605.30493](https://arxiv.org/abs/2605.30493) — A garbled paper
- **作者**: John Roe
- **分类**: econ.EM
- 相关性 5/10
- **摘要**: ```json
{
  "topic": "econ_theory",
  "summary_zh": "构建"非伪造模型集"，得到 markup 的区间。",
  "key_techniques": [
    "markup estimation",
    "production func

---

Maintained by 陈星宇
"""


def test_rerun_file_offline_salvages_only_garbled_block(tmp_path: Path):
    md = tmp_path / "2026-06-01.md"
    md.write_text(_GARBLED_MD, encoding="utf-8")

    found, fixed = rerun.rerun_file(
        md,
        offline=True,
        client=None,
        score_index={},          # salvage path doesn't need the score log
        interests_text="",
        model=None,
        dry_run=False,
    )
    assert (found, fixed) == (1, 1)

    text = md.read_text(encoding="utf-8")
    assert "```json" not in text
    assert RERUN_MARKER not in text
    # Clean block is untouched.
    assert "这是一个干净的摘要，不应被改动。" in text
    # Garbled block is salvaged into prose + a complete technique list.
    assert "- **摘要**: 构建" in text
    assert "`markup estimation`" in text
    assert "production func" not in text  # truncated item dropped


def test_rerun_file_dry_run_writes_nothing(tmp_path: Path):
    md = tmp_path / "2026-06-01.md"
    md.write_text(_GARBLED_MD, encoding="utf-8")
    before = md.read_text(encoding="utf-8")

    found, fixed = rerun.rerun_file(
        md, offline=True, client=None, score_index={},
        interests_text="", model=None, dry_run=True,
    )
    assert (found, fixed) == (1, 1)
    assert md.read_text(encoding="utf-8") == before
