@echo off
REM Simple batch wrapper. Prefer run_daily.ps1 for richer error handling.
cd /d "%~dp0"
if exist ".venv\Scripts\activate.bat" call ".venv\Scripts\activate.bat"
python -m research_news.daily
git add docs/ data/
git diff --cached --quiet || (
    git commit -m "daily report %date%"
    git push
)
