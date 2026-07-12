# Build the MkDocs site AND the Pagefind search index locally.
#
# `mkdocs serve` alone does NOT run Pagefind, so search will not work under it.
# To preview search, run this script then serve the built site/ directory:
#
#   ./scripts/build_docs.ps1
#   python -m http.server -d site 8000
#   # open http://localhost:8000/research-news/search/  (or /search/ if no base)
#
# Requires: mkdocs + mkdocs-material (pip), and Node/npm on PATH (for npx).

$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot
Set-Location $repo

Write-Host "==> mkdocs build --strict"
mkdocs build --strict
if ($LASTEXITCODE -ne 0) { throw "mkdocs build failed" }

Write-Host "==> pagefind --site site"
npx -y "pagefind@^1" --site site
if ($LASTEXITCODE -ne 0) { throw "pagefind failed" }

Write-Host "==> done. Serve with: python -m http.server -d site 8000"
