"""JCSDS-2026 conference deep-read pipeline (script-based, no subagents).

Modules:
  match    — find each talk's arXiv paper by title/author search
  fetch    — download matched PDFs
  read     — LLM deep-read from PDF (or abstract fallback) -> per-talk JSON
  run      — orchestrate match -> fetch -> read for a set of sessions
"""
