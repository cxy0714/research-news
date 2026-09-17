from research_news.dedup import filter_new
from research_news.models import Paper


def _paper(paper_id: str) -> Paper:
    return Paper(
        source="arxiv",
        paper_id=paper_id,
        title=paper_id,
        authors=[],
        abstract="",
        url=f"https://arxiv.org/abs/{paper_id}",
    )


def test_filter_new_removes_seen_and_same_batch_duplicates():
    papers = [_paper("1"), _paper("1"), _paper("2"), _paper("3")]

    assert [p.paper_id for p in filter_new(papers, {"arxiv:3"})] == ["1", "2"]
