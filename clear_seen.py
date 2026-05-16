"""Clear the seen-papers cache so today's papers can be reprocessed.

Usage:  python clear_seen.py
"""
from pathlib import Path
import json

p = Path("data/seen_papers.json")
if p.exists():
    data = json.loads(p.read_text(encoding="utf-8"))
    print(f"Cleared {len(data)} entries from {p}")
    p.write_text("[]", encoding="utf-8")
else:
    print("No cache file found — nothing to clear")
