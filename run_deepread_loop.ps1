# Windows runner for the resident deep-read loop — one unit (default: one paper)
# per iteration, back to back, until nothing is pending. Priority order inside
# `backfill_deep_reads --pending`: data/highlights.json backlog (papers daily
# selected but never deep-read — incl. green-lit / popsci ones) -> failed stubs
# past their cooldown -> score-threshold leftovers.
#
# It releases the lock between units, yields to the daily run's window, and
# commits/pushes every few units so the site picks pages up as they land. Starts
# at logon on a mostly-always-on desktop; a daily trigger restarts it if it had
# stopped. It exits on its own when nothing is pending.
#
#   -Max N         : stop after N units (default 0 = run until the queue is empty)
#   -Limit N       : papers per unit (default 1 — one ~5-min deep read per lock hold)
#   -CommitEvery N : commit + push every N units (default 5)
#   -DailyHour H   : the daily run's hour (default 9). The loop pauses during
#                    H:00–(H+5):00 until today's report exists, so daily gets the
#                    lock first. (run_daily.ps1 also waits for the lock, so daily
#                    is never skipped even if a unit straddles the window.)
#
# The python unit's exit code drives the loop: 0 = did work, 7 = nothing pending
# (stop), anything else = the unit failed (stop, logged).

param(
    [int]$Max = 0,
    [int]$Limit = 1,
    [int]$CommitEvery = 5,
    [int]$DailyHour = 9
)

$ErrorActionPreference = "Continue"
Set-Location -LiteralPath $PSScriptRoot

$hostTag = $env:COMPUTERNAME
if (-not $hostTag) { $hostTag = "host" }
$hostTag = ($hostTag -replace '[^A-Za-z0-9._-]', '-').ToLower()
New-Item -ItemType Directory -Force -Path "logs" | Out-Null

# Append-only loop log (Add-Content closes the handle each call so git can add
# it; each unit's python process writes its own logs\<date>-<host>.log).
function Log($msg) {
    $line = "[$(Get-Date -Format o)] $msg"
    Write-Host $line
    Add-Content -Path "logs\deepread-loop-$(Get-Date -Format yyyy-MM-dd)-$hostTag.log" `
        -Value $line -ErrorAction SilentlyContinue
}

# Commit + push whatever the finished units produced; self-heal a push that lost
# the race with another machine.
function Push-Changes([string]$msg) {
    if (-not (git status --porcelain)) { return }
    git add -A
    git commit -m $msg | Out-Null
    for ($i = 1; $i -le 4; $i++) {
        git push
        if ($LASTEXITCODE -eq 0) { return }
        Start-Sleep -Seconds ([math]::Pow(2, $i))
        git pull --rebase --autostash
    }
    Log "push FAILED after 4 attempts - commit stays local-only"
}

$venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) { . $venvActivate }

Log "deep-read loop start (Max=$Max, Limit=$Limit, CommitEvery=$CommitEvery)"
$done = 0
$uncommitted = 0
while ($Max -le 0 -or $done -lt $Max) {
    # Yield to the daily run: while today's report isn't out yet and we're in the
    # daily window, pause (don't take the lock) so daily runs first. Weekday gate
    # matters because daily only runs Mon-Fri.
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
        python -m research_news.backfill_deep_reads --pending --limit $Limit
        $code = $LASTEXITCODE
    }
    finally {
        $mutex.ReleaseMutex()
        $mutex.Dispose()
    }

    # Non-zero: 7 = nothing pending (queue empty), anything else = unit failed.
    if ($code -eq 7) {
        Log "nothing pending - stopping"
        break
    }
    if ($code -ne 0) {
        Log "unit failed (exit $code) - stopping"
        break
    }

    $done++
    $uncommitted++
    if ($CommitEvery -gt 0 -and $uncommitted -ge $CommitEvery) {
        Push-Changes "deep reads $(Get-Date -Format yyyy-MM-dd)"
        $uncommitted = 0
    }
    Start-Sleep -Seconds 10   # brief gap so a pending daily can grab the lock
}
if ($uncommitted -gt 0) {
    Push-Changes "deep reads $(Get-Date -Format yyyy-MM-dd)"
}
Log "deep-read loop done ($done unit(s) this run)"
