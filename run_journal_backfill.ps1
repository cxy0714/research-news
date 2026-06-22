# Windows runner for the journal back-catalog backfill — a LOOP that does units
# back-to-back until the queue (ops\journal-backfill.md) is empty, releasing the
# lock between units and yielding to the daily run. Meant to start at logon on a
# mostly-always-on desktop; it exits on its own when the queue is done.
#
#   -Max N       : stop after N units (default 0 = run until the queue is empty)
#   -DailyHour H : the daily run's hour (default 9). The loop pauses during
#                  H:00–(H+5):00 until today's report exists, so daily gets the
#                  lock first. (run_daily.ps1 also waits for the lock, so daily
#                  is never skipped even if a unit straddles the window; and a
#                  rare skipped daily self-heals via catch-up the next day.)

param(
    [int]$Max = 0,
    [int]$DailyHour = 9
)

$ErrorActionPreference = "Continue"
Set-Location -LiteralPath $PSScriptRoot

$hostTag = $env:COMPUTERNAME
if (-not $hostTag) { $hostTag = "host" }
$hostTag = ($hostTag -replace '[^A-Za-z0-9._-]', '-').ToLower()
New-Item -ItemType Directory -Force -Path "logs" | Out-Null

# Append-only loop log (Add-Content closes the handle each call, so git can add
# it; the per-unit journals subprocess writes its own logs\journals-<date>-…log).
function Log($msg) {
    $line = "[$(Get-Date -Format o)] $msg"
    Write-Host $line
    Add-Content -Path "logs\journal-loop-$(Get-Date -Format yyyy-MM-dd)-$hostTag.log" `
        -Value $line -ErrorAction SilentlyContinue
}

$venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) { . $venvActivate }

Log "journal backfill loop start (Max=$Max)"
$done = 0
while ($Max -le 0 -or $done -lt $Max) {
    # Yield to the daily run: while today's report isn't out yet and we're in the
    # daily window, pause (don't take the lock) so daily runs first. A wide window
    # (H..H+5) so even a longer unit that straddled 09:10 ends up yielding once it
    # finishes, letting the waiting daily grab the lock.
    $today = Get-Date -Format "yyyy-MM-dd"
    $hour = (Get-Date).Hour
    if ($hour -ge $DailyHour -and $hour -lt ($DailyHour + 5) -and -not (Test-Path "docs\daily\$today.md")) {
        Log "daily not out yet - yielding 5 min"
        Start-Sleep -Seconds 300
        continue
    }

    # Take the lock for ONE unit (wait up to 60 min behind a running daily/unit).
    $mutex = New-Object System.Threading.Mutex($false, "Global\research-news-daily")
    if (-not $mutex.WaitOne([TimeSpan]::FromMinutes(60))) {
        $mutex.Dispose()
        continue
    }
    $code = 0
    try {
        git pull --rebase --autostash
        python -m research_news.journal_backfill --max 1
        $code = $LASTEXITCODE
    }
    finally {
        $mutex.ReleaseMutex()
        $mutex.Dispose()
    }

    # Commit + push whatever the unit produced (journal pages, data, the ticked
    # queue, the logs), self-healing a non-fast-forward push.
    if (git status --porcelain) {
        git add -A
        git commit -m "journal backfill $today" | Out-Null
        for ($i = 1; $i -le 4; $i++) {
            git push
            if ($LASTEXITCODE -eq 0) { break }
            Start-Sleep -Seconds ([math]::Pow(2, $i))
            git pull --rebase --autostash
        }
    }

    # Non-zero = no unit to do (queue empty) or the unit failed → stop the loop.
    if ($code -ne 0) {
        Log "no more units (or unit failed, exit $code) - stopping"
        break
    }
    $done++
    Start-Sleep -Seconds 10   # brief gap so a pending daily can grab the lock
}
Log "journal backfill loop done ($done unit(s) this run)"
