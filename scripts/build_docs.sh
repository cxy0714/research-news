#!/usr/bin/env bash
# Build the MkDocs site AND the Pagefind search index locally.
#
# `mkdocs serve` alone does NOT run Pagefind, so search will not work under it.
# To preview search, run this script then serve the built site/ directory:
#
#   ./scripts/build_docs.sh
#   python -m http.server -d site 8000
#   # open http://localhost:8000/research-news/search/  (or /search/ if no base)
#
# Requires: mkdocs + mkdocs-material (pip), and Node/npm on PATH (for npx).
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo"

echo "==> mkdocs build --strict"
mkdocs build --strict

echo "==> pagefind --site site"
npx -y "pagefind@^1" --site site

echo "==> done. Serve with: python -m http.server -d site 8000"
