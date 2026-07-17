"""Route outbound HTTP(S) through a local proxy for GFW-blocked sources.

arXiv / OpenAlex / Crossref sit behind the GFW and fail intermittently from the
campus network with `SSL: UNEXPECTED_EOF_WHILE_READING` or TLS-handshake
timeouts when reached directly. We funnel traffic through the local Clash proxy
(default 127.0.0.1:7897) by exporting the standard proxy env vars, which both
httpx (this project's HTTP client) and urllib honour automatically — so no call
site needs changing. Domestic / direct-only hosts (the SJTU LLM gateway and any
*.cn host) are listed in NO_PROXY so they keep going direct.

Override via .env (all optional):
    PROXY_URL=http://127.0.0.1:7897   # empty string disables proxying entirely
    NO_PROXY_EXTRA=host1,host2        # extra direct-connect hosts (appended)
"""
from __future__ import annotations

import os

_DEFAULT_PROXY = "http://127.0.0.1:7897"
# Must stay direct: domestic LLM gateway + China-side sources. Proxied traffic
# to these either can't route or is needless.
_DEFAULT_NO_PROXY = [
    "localhost", "127.0.0.1", "::1",
    "models.sjtu.edu.cn",   # SJTU LLM gateway (domestic)
    ".cn",                  # any *.cn host
]


def setup_proxy() -> None:
    """Idempotently export proxy env vars from PROXY_URL (default Clash)."""
    proxy = os.environ.get("PROXY_URL", _DEFAULT_PROXY).strip()
    if not proxy:  # explicitly disabled via empty PROXY_URL
        return

    no_proxy = list(_DEFAULT_NO_PROXY)
    extra = os.environ.get("NO_PROXY_EXTRA", "").strip()
    if extra:
        no_proxy += [h.strip() for h in extra.split(",") if h.strip()]
    no_proxy_str = ",".join(no_proxy)

    # httpx reads *_PROXY / ALL_PROXY; urllib prefers the lower-case names.
    # setdefault → an externally-set proxy still wins.
    for key in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"):
        os.environ.setdefault(key, proxy)
        os.environ.setdefault(key.lower(), proxy)
    # Overwrite NO_PROXY so our domestic allowlist always applies.
    os.environ["NO_PROXY"] = no_proxy_str
    os.environ["no_proxy"] = no_proxy_str
