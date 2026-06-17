@echo off
REM Thin wrapper — delegates to run_daily.ps1 so the date handling, lock, sync,
REM pipeline and push retry all live in one place (avoids %date% locale issues).
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_daily.ps1"
