# Windows runner for the daily pipeline. Invoke from Task Scheduler.
#
# Setup:
#   1. Open Task Scheduler -> Create Task
#   2. Trigger: Daily at e.g. 07:30
#   3. Action: Start a program
#        Program/script: powershell.exe
#        Arguments: -NoProfile -ExecutionPolicy Bypass -File "C:\path\to\research-news\run_daily.ps1"
#        Start in: C:\path\to\research-news
#   4. Settings -> "Run task as soon as possible after a scheduled start is missed"
#
# To bypass PowerShell execution policy without changing system settings, the
# Task Scheduler "Arguments" line above already does it.

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

# Activate venv if it exists.
$venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
    . $venvActivate
}

# Run the pipeline.
python -m research_news.daily

# Commit and push if there are changes under docs/ or data/.
$dirty = git status --porcelain docs/ data/
if ($dirty) {
    git add docs/ data/
    git commit -m ("daily report " + (Get-Date -Format "yyyy-MM-dd"))
    # Retry push on transient failures.
    for ($i = 1; $i -le 4; $i++) {
        git push
        if ($LASTEXITCODE -eq 0) { break }
        Start-Sleep -Seconds ([math]::Pow(2, $i))
    }
}
