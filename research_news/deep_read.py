"""Deep-read high-relevance papers via LLM using their downloaded PDFs.

For each paper with a downloaded PDF, extract the full text and ask the LLM
to produce a structured Chinese research note.  Results are written as
Markdown to docs/deep_reads/<date>-<run_type>.md.
"""
from __future__ import annotations

import logging
from datetime import date
from pathlib import Path

from pypdf import PdfReader

from .llm.prompts import DEEP_READ_SYSTEM, TOPIC_LABELS_ZH
from .llm.sjtu_client import SJTUClient
from .models import Paper

log = logging.getLogger(__name__)

DEEP_READS_DIR = Path("docs/deep_reads")
# ~30 k chars ≈ 7-8 k tokens; covers the bulk of most stat theory papers.
MAX_PDF_CHARS = 30_000


def extract_pdf_text(pdf_path: str | Path, max_chars: int = MAX_PDF_CHARS) -> str:
    """Return up to max_chars of extracted text from a PDF file."""
    try:
        reader = PdfReader(str(pdf_path))
        parts: list[str] = []
        total = 0
        for page in reader.pages:
            chunk = page.extract_text() or ""
            parts.append(chunk)
            total += len(chunk)
            if total >= max_chars:
                break
        return "\n".join(parts)[:max_chars]
    except Exception as e:
        log.warning("PDF text extraction failed for %s: %s", pdf_path, e)
        return ""


def deep_read_paper(
    client: SJTUClient,
    paper: Paper,
    interests_yaml: str,
    *,
    model: str | None = None,
) -> str:
    """Return a Markdown deep-read section for one paper (empty string on failure)."""
    pdf_text = ""
    if paper.pdf_path and Path(paper.pdf_path).exists():
        pdf_text = extract_pdf_text(paper.pdf_path)

    if not pdf_text:
        log.info("no PDF text for %s — falling back to abstract", paper.paper_id)
        pdf_text = f"Abstract:\n{paper.abstract}"

    user = (
        f"## Researcher interests\n{interests_yaml}\n\n"
        f"## Paper metadata\n"
        f"Title: {paper.title}\n"
        f"Authors: {', '.join(paper.authors)}\n"
        f"Venue: {paper.venue or paper.source}\n"
        f"Score: {paper.score}\n"
        f"Topic: {paper.topic}\n\n"
        f"## Full text\n{pdf_text}\n"
    )
    try:
        return client.chat(
            [
                {"role": "system", "content": DEEP_READ_SYSTEM},
                {"role": "user", "content": user},
            ],
            model=model,
            max_tokens=4000,
        )
    except Exception as e:
        log.warning("deep read LLM call failed for %s: %s", paper.paper_id, e)
        return ""


def generate_deep_read_report(
    papers: list[Paper],
    client: SJTUClient,
    interests_yaml: str,
    run_date: date,
    run_type: str = "daily",
    *,
    model: str | None = None,
    output_dir: Path = DEEP_READS_DIR,
) -> Path | None:
    """Generate a deep-read Markdown report for high-relevance papers.

    Uses downloaded PDFs when available; falls back to abstract.  Writes to
    output_dir/<date>-<run_type>.md and returns the path, or None if the list
    is empty.
    """
    if not papers:
        log.info("deep_read: no papers — skipping report")
        return None

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{run_date.isoformat()}-{run_type}.md"

    type_label = {"daily": "每日 arXiv", "journals": "期刊"}.get(run_type, run_type)
    lines: list[str] = [
        f"# 精读报告 · {type_label} · {run_date.isoformat()}\n",
        f"共 {len(papers)} 篇高相关性论文（评分 ≥ 阈值）。\n",
    ]

    for i, paper in enumerate(papers, 1):
        log.info("deep reading %d/%d: %s", i, len(papers), paper.paper_id)
        report = deep_read_paper(client, paper, interests_yaml, model=model)
        topic_label = TOPIC_LABELS_ZH.get(paper.topic or "other", paper.topic or "other")
        authors_str = ", ".join(paper.authors[:5]) + (" et al." if len(paper.authors) > 5 else "")
        lines.append(f"\n---\n\n## {i}. {paper.title}")
        lines.append(f"**作者**: {authors_str}  ")
        if paper.venue:
            lines.append(f"**来源**: {paper.venue}  ")
        lines.append(f"**主题**: {topic_label}  ")
        lines.append(f"**相关性**: {paper.score:.0f}/10  ")
        lines.append(f"**链接**: <{paper.url}>\n")
        lines.append(report if report else "*（精读失败，请查看日志）*")

    lines.append(
        "\n---\n\n"
        "Maintained by 陈星宇 · "
        "[Homepage](https://cxy0714.github.io/) · "
        "[Source on GitHub](https://github.com/cxy0714/research-news)\n"
    )

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log.info("deep read report written to %s", out_path)
    return out_path
