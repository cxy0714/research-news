from datetime import date

from research_news.scrapers.arxiv import _date_window


def test_date_window_uses_only_requested_non_monday():
    assert _date_window(date(2026, 9, 16)) == (
        "202609160000",
        "202609162359",
    )


def test_date_window_reaches_back_to_friday_on_monday():
    assert _date_window(date(2026, 9, 14)) == (
        "202609110000",
        "202609142359",
    )
