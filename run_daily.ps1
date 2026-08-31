# Windows runner for the daily pipeline — invoke from Task Scheduler.
# Mirrors run_daily.sh: single-instance lock -> sync -> daily -> fix garbled
# summaries -> retry failed deep reads -> commit/push. A transcript of the whole
# run is written to logs\run-<date>.log and pushed with git add -A (alongside the
# pipeline's own logs\<date>.log).
#
# One-time setup (easiest): from the repo root in PowerShell, run
#   .\scripts\register-task.ps1
# or set it up by hand — see the steps at the bottom of this file / the README.
#
# -Force passes --force through to daily.py, for the rare re-run that must
# replace an already-rendered report (e.g. the first run only got part of the
# categories because arXiv 429'd). It OVERWRITES today's page — back it up first.
param(
    [switch]$Force
)

Set-Location -LiteralPath $PSScriptRoot
$today = Get-Date -Format "yyyy-MM-dd"

# Capture this run's console (wrapper + git + python) to a per-day, per-machine
# transcript, so logs from different machines pushing to the same repo don't
# collide.
New-Item -ItemType Directory -Force -Path "logs" | Out-Null
$hostTag = $env:COMPUTERNAME
if (-not $hostTag) { $hostTag = "host" }
$hostTag = ($hostTag -replace '[^A-Za-z0-9._-]', '-').ToLower()
Start-Transcript -Path "logs\run-$today-$hostTag.log" -Append -ErrorAction SilentlyContinue | Out-Null

# ── single-instance lock (Windows equivalent of flock) ────────────────────────
# A named mutex the OS releases automatically when this process exits, so the
# daily run never overlaps a journal-backfill unit. We WAIT (up to 3h) for it
# rather than bail, so daily is never skipped just because a journal unit is
# mid-flight — it queues behind the current unit and runs as soon as it frees
# the lock (the journal loop yields during the daily window, so the wait is
# usually zero). The re-run guard in daily.py still prevents clobbering.
$mutex = New-Object System.Threading.Mutex($false, "Global\research-news-daily")
if (-not $mutex.WaitOne([TimeSpan]::FromHours(3))) {
    Write-Host "[$(Get-Date -Format o)] lock held >3h - skipping this daily run"
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
    return
}

try {
    # Activate venv if present.
    $venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
    if (Test-Path $venvActivate) { . $venvActivate }

    # Sync first so the end-of-run push fast-forwards (changes may have been
    # merged via the web/agent). Best-effort.
    git pull --rebase --autostash

    if ($Force) {
        Write-Host "[$(Get-Date -Format o)] -Force: regenerating today's report from scratch"
        python -m research_news.daily --force
    } else {
        python -m research_news.daily
    }

    # Fix any garbled / truncated summaries in today's report.
    python -m research_news.rerun --date $today

    # Regenerate any deep reads whose LLM call failed today (the '精读失败' stubs).
    python -m research_news.backfill_deep_reads --retry-stubs --date $today

    # Deep-read papers the owner queued on the website (the gist 'queue': paste an
    # arXiv link -> default-favorite + queue). Fails open without GIST_TOKEN.
    python -m research_news.manual_requests --date $today
}
finally {
    $mutex.ReleaseMutex()
    $mutex.Dispose()
    # Close the transcript BEFORE git stages it, so the file isn't locked and the
    # committed logs\run-<date>.log is complete through the pipeline steps.
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
}

# Commit + push everything (docs/ + data/ + logs/) if anything changed.
if (git status --porcelain) {
    git add -A
    git commit -m "daily report $today"
    for ($i = 1; $i -le 4; $i++) {
        git push
        if ($LASTEXITCODE -eq 0) { break }
        # Push failed. Most often the remote moved on (another machine, or a
        # web/agent merge) → a plain retry won't fix a non-fast-forward; rebase
        # onto it, then retry (the backoff also rides out a transient network blip).
        Start-Sleep -Seconds ([math]::Pow(2, $i))
        git pull --rebase --autostash
    }
}

# ── Task Scheduler setup (manual alternative to register-task.ps1) ────────────
#   1. Task Scheduler -> Create Task (not Basic Task)
#   2. General  : name it; "Run only when user is logged on" is simplest (no
#                 stored password). Tick "Run with highest privileges" only if
#                 you hit permission issues.
#   3. Triggers : Weekly, Mon-Fri, 09:10.
#   4. Actions  : Start a program
#        Program/script : powershell.exe
#        Arguments      : -NoProfile -ExecutionPolicy Bypass -File "C:\path\to\research-news\run_daily.ps1"
#        Start in       : C:\path\to\research-news
#   5. Settings : tick "Run task as soon as possible after a scheduled start is
#                 missed" (catch up if the PC was off/asleep); set "If the task
#                 is already running" -> "Do not start a new instance".
#   6. Conditions: untick "Start only if on AC power" if it's a laptop; tick
#                 "Wake the computer to run this task" if you want it to wake.
#
# First run: do one manual `git push` in the repo so Git Credential Manager (or
# your SSH key) caches the credential — the scheduled push runs non-interactively.
