# Windows runner for the journal back-catalog backfill — invoke from Task
# Scheduler (separate from the daily task). Does the next unit(s) of the queue
# in ops\journal-backfill.md, one journal at a time. Shares the daily lock so it
# never runs in parallel with the daily run (it waits behind it).
#
# Register it with:  .\scripts\register-task.ps1   (adds research-news-journals)
# Pace: -Max units per run (default 1). Tokens aren't the constraint (the weekly
# quota dwarfs a unit); wall-clock + the PC being on is — one journal at
# --n-issues 2-4 is ~30-90 min, so 1/day is a safe default.

param(
    [int]$Max = 1
)

$ErrorActionPreference = "Continue"
Set-Location -LiteralPath $PSScriptRoot
$today = Get-Date -Format "yyyy-MM-dd"

New-Item -ItemType Directory -Force -Path "logs" | Out-Null
$hostTag = $env:COMPUTERNAME
if (-not $hostTag) { $hostTag = "host" }
$hostTag = ($hostTag -replace '[^A-Za-z0-9._-]', '-').ToLower()
Start-Transcript -Path "logs\journal-$today-$hostTag.log" -Append -ErrorAction SilentlyContinue | Out-Null

$venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) { . $venvActivate }

# Same lock as run_daily.ps1. WAIT (don't bail) so the journal run queues behind
# a running daily run instead of being skipped.
$mutex = New-Object System.Threading.Mutex($false, "Global\research-news-daily")
if (-not $mutex.WaitOne([TimeSpan]::FromMinutes(90))) {
    Write-Host "[$(Get-Date -Format o)] daily still running after 90 min - skipping journal backfill"
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
    return
}

try {
    git pull --rebase --autostash
    python -m research_news.journal_backfill --max $Max
}
finally {
    $mutex.ReleaseMutex()
    $mutex.Dispose()
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
}

# Commit + push (the journal pages, their data, the ticked-off queue, the logs).
if (git status --porcelain) {
    git add -A
    git commit -m "journal backfill $today"
    for ($i = 1; $i -le 4; $i++) {
        git push
        if ($LASTEXITCODE -eq 0) { break }
        # Rebase onto the remote before retrying (non-fast-forward self-heal).
        Start-Sleep -Seconds ([math]::Pow(2, $i))
        git pull --rebase --autostash
    }
}
