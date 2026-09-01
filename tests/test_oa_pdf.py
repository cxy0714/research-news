"""Offline tests for the open-access PDF resolver (no network).

Covers: URL / DOI extraction, landing-URL derivation, the host-rule table,
citation meta-tag parsing, and the magic-byte check that keeps a paywall page
from ever being stored as a "PDF".
"""
from __future__ import annotations

from pathlib import Path

from research_news import oa_pdf


# ── extraction helpers ────────────────────────────────────────────────────────

def test_extract_url_and_doi():
    text = ("Hettinger et al. Beyond No Unmeasured Confounding. "
            "Observational Studies 12(2). https://muse.jhu.edu/article/999750, "
            "doi:10.1353/obs.2026.a999750.")
    assert oa_pdf.extract_url(text) == "https://muse.jhu.edu/article/999750"
    assert oa_pdf.extract_doi(text) == "10.1353/obs.2026.a999750"
    assert oa_pdf.extract_url("no link here") == ""
    assert oa_pdf.extract_doi("no doi here") == ""


def test_extract_url_strips_trailing_punctuation():
    assert oa_pdf.extract_url("see (https://example.org/a/b).") == \
        "https://example.org/a/b"


def test_landing_url_strips_pdf_marker():
    assert oa_pdf.landing_url("https://muse.jhu.edu/pub/56/article/999750/pdf") == \
        "https://muse.jhu.edu/pub/56/article/999750"
    assert oa_pdf.landing_url("https://www.biorxiv.org/content/10.1101/x.full.pdf") == \
        "https://www.biorxiv.org/content/10.1101/x.full"
    # A bare .pdf file name has no derivable landing page — left alone.
    assert oa_pdf.landing_url("https://www.jmlr.org/papers/volume27/23-0535/23-0535.pdf") \
        == "https://www.jmlr.org/papers/volume27/23-0535/23-0535.pdf"


# ── host rules ────────────────────────────────────────────────────────────────

def test_host_rules():
    r = oa_pdf.host_rule_pdf
    assert r("https://arxiv.org/abs/2405.08525") == "https://arxiv.org/pdf/2405.08525"
    # The JMLR path that actually serves the PDF (/papers/v27/<stem>.pdf is a 404).
    assert r("https://www.jmlr.org/papers/v27/23-0535.html") == \
        "https://www.jmlr.org/papers/volume27/23-0535/23-0535.pdf"
    assert r("https://proceedings.mlr.press/v139/agarwal21c.html") == \
        "https://proceedings.mlr.press/v139/agarwal21c/agarwal21c.pdf"
    assert r("https://muse.jhu.edu/article/999750") == \
        "https://muse.jhu.edu/article/999750/pdf"
    assert r("https://openreview.net/forum?id=7Bywt2mQsCe") == \
        "https://openreview.net/pdf?id=7Bywt2mQsCe"
    assert r("https://www.nature.com/articles/s41467-023-40566-6") == \
        "https://www.nature.com/articles/s41467-023-40566-6.pdf"
    assert r("https://journals.plos.org/plosone/article?id=10.1371/journal.pone.01") == \
        "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.01&type=printable"
    # www. prefix must not be mangled when matching the host (removeprefix, not lstrip).
    assert r("https://onlinelibrary.wiley.com/doi/full/10.1111/rssb.12453") == \
        "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/rssb.12453"


def test_host_rules_unknown_host_is_none():
    # Unknown publishers are handled by the meta-tag layer, not this table.
    assert oa_pdf.host_rule_pdf("https://example.org/some/article") is None
    assert oa_pdf.host_rule_pdf("") is None


# ── citation meta tags (layer 1) ──────────────────────────────────────────────

# Trimmed from the real Project MUSE page for Observational Studies 12(2).
_MUSE_HTML = """<html><head>
<meta name="citation_publisher" content="University of Pennsylvania Press">
<meta name="citation_journal_title" content="Observational Studies">
<meta name="citation_title" content="Beyond &quot;No Unmeasured Confounding&quot;">
<meta name="citation_author" content="Gary C. N. Hettinger">
<meta name="citation_author" content="Renson, Audrey">
<meta name="citation_volume" content="12">
<meta name="citation_issue" content="2">
<meta name="citation_online_date" content="2026/08/27">
<meta name="citation_pdf_url" content="https://muse.jhu.edu/pub/56/article/999750/pdf">
<meta name="og:description" content="A long enough abstract to be kept by the
parser, describing Cornfield-style reasoning in modern causal inference.">
</head><body></body></html>"""


def test_parse_meta_muse():
    m = oa_pdf.parse_meta(_MUSE_HTML)
    assert m["pdf_url"] == "https://muse.jhu.edu/pub/56/article/999750/pdf"
    assert m["title"] == 'Beyond "No Unmeasured Confounding"'
    # "Family, Given" is flipped; already-natural names are left alone.
    assert m["authors"] == ["Gary C. N. Hettinger", "Audrey Renson"]
    assert m["venue"] == "Observational Studies"
    assert m["published"] == "2026-08-27"
    assert (m["volume"], m["issue"]) == ("12", "2")
    assert "Cornfield" in m["abstract"]
    assert "doi" not in m          # MUSE emits none here


def test_parse_meta_dublin_core_and_doi():
    html = ('<html><head>'
            '<meta name="DC.title" content="A Dublin Core Paper">'
            '<meta name="DC.creator" content="Roe, John">'
            '<meta name="citation_doi" content="doi:10.1214/25-AOS2537">'
            '</head></html>')
    m = oa_pdf.parse_meta(html)
    assert m["title"] == "A Dublin Core Paper"
    assert m["authors"] == ["John Roe"]
    assert m["doi"] == "10.1214/25-AOS2537"
    assert "pdf_url" not in m


def test_parse_meta_empty():
    assert oa_pdf.parse_meta("") == {}
    assert oa_pdf.parse_meta("<html><body>no meta</body></html>") == {}


# ── download + magic-byte verification ────────────────────────────────────────

class _FakeStream:
    def __init__(self, body: bytes, ctype: str, status: int = 200):
        self._body, self.headers, self._status = body, {"content-type": ctype}, status

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def raise_for_status(self):
        if self._status >= 400:
            raise RuntimeError(f"HTTP {self._status}")

    def iter_bytes(self, chunk_size=65536):
        for i in range(0, len(self._body), chunk_size):
            yield self._body[i:i + chunk_size]


def _fake_httpx(responses: dict):
    """A stand-in httpx.Client whose .stream() serves ``{url: _FakeStream}``."""
    class _Client:
        def __init__(self, *a, **k):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def stream(self, method, url):
            if url not in responses:
                raise RuntimeError("connection refused")
            return responses[url]
    return _Client


_REAL_PDF = b"%PDF-1.7\n" + b"x" * 4000
_PAYWALL_HTML = b"<!DOCTYPE html><html>Sign in to continue</html>"


def test_fetch_pdf_accepts_real_pdf(tmp_path, monkeypatch):
    monkeypatch.setattr(oa_pdf.httpx, "Client", _fake_httpx(
        {"https://x/ok.pdf": _FakeStream(_REAL_PDF, "application/pdf")}))
    dest = tmp_path / "a.pdf"
    assert oa_pdf.fetch_pdf("https://x/ok.pdf", dest) == dest
    assert dest.read_bytes().startswith(b"%PDF")


def test_fetch_pdf_rejects_html_paywall(tmp_path, monkeypatch):
    monkeypatch.setattr(oa_pdf.httpx, "Client", _fake_httpx(
        {"https://x/wall": _FakeStream(_PAYWALL_HTML, "text/html")}))
    dest = tmp_path / "a.pdf"
    assert oa_pdf.fetch_pdf("https://x/wall", dest) is None
    assert not dest.exists()                       # nothing written
    assert not list(tmp_path.glob("*.part"))       # temp file cleaned up


def test_fetch_pdf_rejects_truncated_pdf(tmp_path, monkeypatch):
    monkeypatch.setattr(oa_pdf.httpx, "Client", _fake_httpx(
        {"https://x/stub.pdf": _FakeStream(b"%PDF-1.4 tiny", "application/pdf")}))
    assert oa_pdf.fetch_pdf("https://x/stub.pdf", tmp_path / "a.pdf") is None


def test_download_falls_through_to_second_candidate(tmp_path, monkeypatch):
    monkeypatch.setattr(oa_pdf.httpx, "Client", _fake_httpx({
        "https://x/wall": _FakeStream(_PAYWALL_HTML, "text/html"),
        "https://x/ok.pdf": _FakeStream(_REAL_PDF, "application/pdf"),
    }))
    src = oa_pdf.PdfSource(landing_url="https://x/a",
                           pdf_candidates=["https://x/wall", "https://x/ok.pdf"])
    dest = tmp_path / "a.pdf"
    assert oa_pdf.download(src, dest) == dest


def test_download_returns_none_when_all_candidates_fail(tmp_path, monkeypatch):
    monkeypatch.setattr(oa_pdf.httpx, "Client", _fake_httpx(
        {"https://x/wall": _FakeStream(_PAYWALL_HTML, "text/html")}))
    src = oa_pdf.PdfSource(landing_url="https://x/a", pdf_candidates=["https://x/wall"])
    assert oa_pdf.download(src, tmp_path / "a.pdf") is None


# ── resolve() orchestration ───────────────────────────────────────────────────

def test_resolve_from_pasted_pdf_link_uses_meta_tags(monkeypatch):
    seen = {}

    def fake_get_html(url, timeout=30, **kw):
        seen["url"] = url
        return _MUSE_HTML, url
    monkeypatch.setattr(oa_pdf, "_get_html", fake_get_html)

    src = oa_pdf.resolve("https://muse.jhu.edu/pub/56/article/999750/pdf",
                         use_openalex=False)
    # The landing page (not the PDF) is what gets fetched for metadata.
    assert seen["url"] == "https://muse.jhu.edu/pub/56/article/999750"
    assert src.title == 'Beyond "No Unmeasured Confounding"'
    assert src.venue == "Observational Studies"
    assert src.authors == ["Gary C. N. Hettinger", "Audrey Renson"]
    # Pasted link first (known-good), then the one the page advertises.
    assert src.pdf_url == "https://muse.jhu.edu/pub/56/article/999750/pdf"
    assert len(src.pdf_candidates) == 1     # both URLs are the same here


def test_resolve_from_doi_only_adds_openalex_candidates(monkeypatch):
    monkeypatch.setattr(oa_pdf, "_get_html", lambda url, timeout=30, **kw: ("", url))
    from research_news.scrapers import openalex
    monkeypatch.setattr(openalex, "work_oa_info", lambda doi: {
        "pdf_urls": ["https://repo.example.org/paper.pdf"],
        "title": "An OpenAlex Title", "authors": ["Jane Doe"],
        "venue": "Journal of Things", "published": "2026-01-02",
        "abstract": "", "arxiv_id": "2405.08525",
    })
    src = oa_pdf.resolve("10.1353/obs.2026.a999750")
    assert src.doi == "10.1353/obs.2026.a999750"
    assert src.pdf_candidates == ["https://repo.example.org/paper.pdf"]
    assert src.title == "An OpenAlex Title"
    assert src.arxiv_id == "2405.08525"


def test_resolve_uses_host_rule_when_page_is_blocked(monkeypatch):
    # Bot wall / JS app: no meta tags, so the host rule is the only candidate.
    monkeypatch.setattr(oa_pdf, "_get_html", lambda url, timeout=30, **kw: ("", url))
    src = oa_pdf.resolve("https://www.jmlr.org/papers/v27/23-0535.html",
                         use_openalex=False)
    assert src.pdf_candidates == [
        "https://www.jmlr.org/papers/volume27/23-0535/23-0535.pdf"]


_BOT_WALL = '<html><head><title>Verify</title></head><body>checking…</body></html>'


def test_fetch_meta_retries_direct_when_page_is_a_bot_wall(monkeypatch):
    # A verification interstitial is still text/html, so "got HTML" isn't enough:
    # the proxied route must be discarded in favour of the direct one.
    monkeypatch.setattr(oa_pdf, "_proxy_modes", lambda: [True, False])
    calls = []

    def fake_get_html(url, timeout=30, *, trust_env=True):
        calls.append(trust_env)
        if trust_env:
            return _BOT_WALL, "https://muse.jhu.edu/verify?url=%2Farticle%2F999750"
        return _MUSE_HTML, url
    monkeypatch.setattr(oa_pdf, "_get_html", fake_get_html)

    meta, final = oa_pdf._fetch_meta("https://muse.jhu.edu/article/999750")
    assert calls == [True, False]
    assert meta["venue"] == "Observational Studies"
    assert final == "https://muse.jhu.edu/article/999750"   # not the /verify URL


def test_fetch_meta_keeps_requested_url_when_nothing_usable(monkeypatch):
    monkeypatch.setattr(oa_pdf, "_proxy_modes", lambda: [True])
    monkeypatch.setattr(oa_pdf, "_get_html",
                        lambda url, timeout=30, **kw: (_BOT_WALL, "https://x/verify"))
    meta, final = oa_pdf._fetch_meta("https://x/article/1")
    assert meta == {}
    assert final == "https://x/article/1"


def test_norm_date():
    n = oa_pdf._norm_date
    assert n("2026/08/27") == "2026-08-27"
    assert n("2021/7/1") == "2021-07-01"
    assert n("Dec 13, 2023") == "2023-12-13"
    assert n("2026") == "2026"          # year-only is left as-is
    assert n("forthcoming") == "forthcoming"


def test_resolve_returns_none_without_url_or_doi(monkeypatch):
    monkeypatch.setattr(oa_pdf, "_get_html",
                        lambda *a, **k: (_ for _ in ()).throw(
                            AssertionError("fetched for a bare title")))
    assert oa_pdf.resolve("Just a paper title with no link at all") is None


def test_resolve_returns_none_when_no_candidate(monkeypatch):
    monkeypatch.setattr(oa_pdf, "_get_html", lambda url, timeout=30, **kw: ("", url))
    assert oa_pdf.resolve("https://example.org/article/1", use_openalex=False) is None
