"""Per-machine tagging for log filenames.

When more than one machine runs the pipeline against the same repo (e.g. a cloud
server in the morning and a desktop later), they otherwise both write
``logs/<date>.log`` — the file collides, the two runs interleave/overwrite, and
you can't tell which machine produced what. Stamping the hostname into the
filename keeps them separate: ``logs/<date>-<host>.log``.
"""
from __future__ import annotations

import re
import socket


def host_tag() -> str:
    """A short, filesystem-safe, lowercase hostname for log filenames."""
    try:
        host = socket.gethostname()
    except Exception:  # noqa: BLE001 — never let logging setup fail
        host = ""
    host = re.sub(r"[^A-Za-z0-9._-]+", "-", host or "").strip("-._").lower()
    return host[:24] or "host"
