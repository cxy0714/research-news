# Windows runner for the journal back-catalog backfill — a LOOP that does units
# back-to-back until the queue (ops\journal-backfill.md) is empty, releasing the
# lock between units and yielding to the daily run. Meant to start at logon on a
# mostly-always-on desktop; it exits on its own when the queue is done.
#
#   -Max N           : stop after N units (default 0 = run until the queue is empty)
#   -DailyHour H     : the daily run's hour (default 9). The loop pauses during
#                      H:00–(H+5):00 until today's report exists, so daily gets the
#                      lock first. (run_daily.ps1 also waits for the lock, so daily
#                      is never skipped even if a unit straddles the window; and a
#                      rare skipped daily self-heals via catch-up the next day.)
#   -CommitMinutes N : push at most once every N minutes (default 120; 0 = push
#                      after every unit, the old behaviour). Units are written back
#                      to back and each push costs a ~7-min Pages build, so the
#                      batch is only pushed when it is this old — plus always on
#                      exit. `git pull --rebase --autostash` before each unit keeps
#                      the unpushed batch safe.

param(
    [int]$Max = 0,
    [int]$DailyHour = 9,
    [int]$CommitMinutes = 120
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

# Commit + push the batch, self-healing a non-fast-forward push.
function Push-Batch([string]$msg) {
    if (-not (git status --porcelain)) { return }
    git add -A
    git commit -m $msg | Out-Null
    for ($i = 1; $i -le 4; $i++) {
        git push
        if ($LASTEXITCODE -eq 0) { return }
        Start-Sleep -Seconds ([math]::Pow(2, $i))
        git pull --rebase --autostash
    }
    Log "push FAILED after 4 attempts - batch stays local-only"
}

Log "journal backfill loop start (Max=$Max, CommitMinutes=$CommitMinutes)"
$done = 0
$lastPush = Get-Date
while ($Max -le 0 -or $done -lt $Max) {
    # Yield to the daily run: while today's report isn't out yet and we're in the
    # daily window, pause (don't take the lock) so daily runs first. A wide window
    # (H..H+5) so even a longer unit that straddled 09:10 ends up yielding once it
    # finishes, letting the waiting daily grab the lock.
    #
    # Weekday gate (2026-10-11): the daily task only runs Mon-Fri, so on Sat/Sun
    # docs\daily\<today>.md never appears and the old check made the loop idle the
    # whole 09:00-14:00 window for a report that was never coming (10h/week of
    # queue-grinding lost on weekends). Weekdays keep the exact old behaviour.
    $today = Get-Date -Format "yyyy-MM-dd"
    $hour = (Get-Date).Hour
    $isWeekday = (Get-Date).DayOfWeek -ne [System.DayOfWeek]::Saturday -and
                 (Get-Date).DayOfWeek -ne [System.DayOfWeek]::Sunday
    if ($isWeekday -and
        $hour -ge $DailyHour -and $hour -lt ($DailyHour + 5) -and
        -not (Test-Path "docs\daily\$today.md")) {
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

    # Commit + push whatever the units so far produced (journal pages, data, the
    # ticked queue, the logs) — but only once the batch is CommitMinutes old, so
    # the Pages deploy isn't retriggered every few minutes.
    $due = ($CommitMinutes -le 0) -or
           (((Get-Date) - $lastPush).TotalMinutes -ge $CommitMinutes)
    if ($due) {
        Push-Batch "journal backfill $today"
        $lastPush = Get-Date
    }

    # Non-zero = no unit to do (queue empty) or the unit failed → stop the loop.
    if ($code -ne 0) {
        Log "no more units (or unit failed, exit $code) - stopping"
        break
    }
    $done++
    Start-Sleep -Seconds 10   # brief gap so a pending daily can grab the lock
}
Push-Batch "journal backfill $today"   # never leave finished units unpushed
Log "journal backfill loop done ($done unit(s) this run)"
