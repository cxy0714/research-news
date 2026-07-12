"""LLM deep-read for one conference talk -> per-talk JSON dict.

Reuses the project's SJTU client and PDF text extraction. When the matched
candidate has an arXiv id we download+read the PDF; otherwise we deep-read from
the abstract (OpenAlex/arXiv). Produces the schema the topic-page generator
consumes: {no, title, speaker, paper_title, arxiv_id, url, abstract, found,
deep_read}.
"""
from __future__ import annotations

import logging
import os
from pathlib import Path

import httpx

from ..deep_read import extract_pdf_text
from ..llm.sjtu_client import SJTUClient
from .match import MatchResult

log = logging.getLogger(__name__)

DEEP_READ_MODEL = os.environ.get("DEEP_READ_MODEL") or os.environ.get("SJTU_MODEL_DEEP")
MAX_PDF_CHARS = 90_000
DEEP_READ_MAX_TOKENS = 2_000
PDF_DIR = Path("data/conferences/jcsds2026/pdfs")

SYSTEM = """你是一位严谨的统计学教授，专精因果推断、数理统计、高维统计、机器学习理论。\
你在为一份中文会议导览为某场学术报告写一段 300-500 字的**精读**，读者是找研究问题的统计方向研究者。

要求：
- 结构：问题 / 核心方法 / 与已有工作关系 / 贡献 四个要点（用 Markdown 加粗小标题分段）。
- 讲清"这场报告解决什么问题、方法本质是什么、相比已有工作新在哪、主要贡献"。
- 行内公式用 $...$。中文写作，术语可保留英文。
- 若我告诉你"未找到对应论文"，则基于题目与讲者研究方向做**合理推断**，并在开头明确注明"未检索到公开论文，以下为基于题目与讲者方向的推断"。
- 只输出这段精读正文，不要额外前言或标题。"""


def _download_pdf(arxiv_id: str) -> str:
    """Download an arXiv PDF into PDF_DIR, return extracted text ('' on failure)."""
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    dest = PDF_DIR / f"{arxiv_id.replace('/', '_')}.pdf"
    if not (dest.exists() and dest.stat().st_size > 1024):
        url = f"https://arxiv.org/pdf/{arxiv_id}"
        try:
            with httpx.Client(timeout=120, follow_redirects=True,
                              headers={"User-Agent": "research-news/1.0"}) as c:
                r = c.get(url)
                r.raise_for_status()
                dest.write_bytes(r.content)
        except Exception as e:  # noqa: BLE001
            log.warning("PDF download failed for %s: %s", arxiv_id, e)
            return ""
    return extract_pdf_text(dest, max_chars=MAX_PDF_CHARS)


def _build_user(title, speaker, m: MatchResult, pdf_text: str) -> str:
    lines = [f"报告题目：{title}", f"讲者：{speaker}"]
    if m.found and m.candidate:
        c = m.candidate
        lines.append(f"对应论文：{c.title}")
        if c.authors:
            lines.append(f"论文作者：{', '.join(c.authors[:8])}")
        if pdf_text:
            lines.append(f"\n## 论文全文（截断）\n{pdf_text}")
        elif c.abstract:
            lines.append(f"\n## 摘要\n{c.abstract}")
    else:
        lines.append("未找到对应论文，请基于题目与讲者方向合理推断，并在开头注明。")
    return "\n".join(lines)


def read_talk(client: SJTUClient, no: int, title: str, speaker: str,
              m: MatchResult, *, download: bool = True) -> dict:
    c = m.candidate if m.found else None
    pdf_text = ""
    if m.found and c and c.arxiv_id and download:
        pdf_text = _download_pdf(c.arxiv_id)

    user = _build_user(title, speaker, m, pdf_text)
    try:
        deep_read = client.chat(
            [{"role": "system", "content": SYSTEM},
             {"role": "user", "content": user}],
            model=DEEP_READ_MODEL, max_tokens=DEEP_READ_MAX_TOKENS,
        ).strip()
    except Exception as e:  # noqa: BLE001
        log.error("deep-read LLM failed for talk %s %r: %s", no, title[:50], e)
        deep_read = "（精读生成失败，请稍后重试）"

    return {
        "no": int(no),
        "title": title,
        "speaker": speaker,
        "paper_title": c.title if c else None,
        "arxiv_id": c.arxiv_id if c else None,
        "url": c.url if c else None,
        "abstract": c.abstract if (c and c.abstract) else None,
        "found": bool(m.found),
        "deep_read": deep_read,
    }
