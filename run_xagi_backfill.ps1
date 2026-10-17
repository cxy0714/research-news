# Windows runner for the XAGI 2026 conference deep-read queue — a LOOP that does
# one talk ("一格") at a time until the queue (ops\xagi2026-backfill.md) is empty,
# releasing the shared lock between units and yielding to the daily run. Same
# pattern as run_journal_backfill.ps1: start at logon on a mostly-always-on
# desktop; it exits on its own when both phases are done.
#
#   Phase 1 — the queue: one talk per lock hold, tick it, commit + push.
#   Phase 2 — long reads: papers whose long deep read timed out during phase 1
#             (the short per-talk read is already written) are retried one at a
#             time via `xagi long --max 1`, again committing each.
#
#   -Max N       : stop phase 1 after N units (default 0 = until the queue is empty)
#   -MaxLong N   : stop phase 2 after N long reads (default 0 = until none missing)
#   -LongModel M : model for phase 2 (default "" = the configured deep-read model;
#                  `deepseek-chat` is much faster when the reasoning model times out)
#   -DailyHour H : the daily run's hour (default 9). The loop pauses during
#                  H:00–(H+5):00 on weekdays until today's report exists, so the
#                  daily run gets the lock first (run_daily.ps1 also waits for
#                  the lock, so daily is never skipped).
#
# The queue itself (which cell is next, what is done) lives in git — see
# ops\xagi2026-backfill.md — so this script holds no state and is safe to stop /
# restart at any time.

param(
    [int]$Max = 0,
    [int]$MaxLong = 0,
    [string]$LongModel = "",
    [int]$DailyHour = 9
)

$ErrorActionPreference = "Continue"
Set-Location -LiteralPath $PSScriptRoot

$hostTag = $env:COMPUTERNAME
if (-not $hostTag) { $hostTag = "host" }
$hostTag = ($hostTag -replace '[^A-Za-z0-9._-]', '-').ToLower()
New-Item -ItemType Directory -Force -Path "logs" | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format o)] $msg"
    Write-Host $line
    Add-Content -Path "logs\xagi-loop-$(Get-Date -Format yyyy-MM-dd)-$hostTag.log" `
        -Value $line -ErrorAction SilentlyContinue
}

$venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) { . $venvActivate }

# During the weekday daily window, wait for today's report so daily runs first
# (a wider H..H+5 window so a unit straddling 09:10 still yields).
function Test-DailyWindow {
    $today = Get-Date -Format "yyyy-MM-dd"
    $hour = (Get-Date).Hour
    $isWeekday = (Get-Date).DayOfWeek -ne [System.DayOfWeek]::Saturday -and
                 (Get-Date).DayOfWeek -ne [System.DayOfWeek]::Sunday
    if ($isWeekday -and
        $hour -ge $DailyHour -and $hour -lt ($DailyHour + 5) -and
        -not (Test-Path "docs\daily\$today.md")) {
        Log "daily not out yet - yielding 5 min"
        Start-Sleep -Seconds 300
        return $true
    }
    return $false
}

# Run ONE unit under the shared lock, then commit + push whatever it produced
# (read JSON, conference pages, long read, ticked queue, logs), self-healing a
# non-fast-forward push. Returns the unit's exit code.
function Invoke-LockedUnit([scriptblock]$body) {
    # Same mutex name as run_daily.ps1 and run_journal_backfill.ps1 — that is
    # what makes "绝不并行" hold across daily / journals / XAGI.
    $mutex = New-Object System.Threading.Mutex($false, "Global\research-news-daily")
    if (-not $mutex.WaitOne([TimeSpan]::FromMinutes(60))) {
        $mutex.Dispose()
        return -1
    }
    $code = 0
    try {
        # Suppress git's stdout so the function's return value stays the exit
        # code (PowerShell functions return everything written to the pipeline).
        $null = git pull --rebase --autostash 2>&1
        & $body | Out-Host
        $code = $LASTEXITCODE
    }
    finally {
        $mutex.ReleaseMutex()
        $mutex.Dispose()
    }

    $changes = git status --porcelain
    if ($changes) {
        $null = git add -A 2>&1
        $null = git commit -m "xagi backfill $today" 2>&1
        for ($i = 1; $i -le 4; $i++) {
            $null = git push 2>&1
            if ($LASTEXITCODE -eq 0) { break }
            Start-Sleep -Seconds ([math]::Pow(2, $i))
            $null = git pull --rebase --autostash 2>&1
        }
    }
    return $code
}

$today = Get-Date -Format "yyyy-MM-dd"
Log "xagi backfill loop start (Max=$Max, MaxLong=$MaxLong)"

# ── phase 1: the per-talk queue ───────────────────────────────────────────────
$done = 0
while ($Max -le 0 -or $done -lt $Max) {
    if (Test-DailyWindow) { continue }
    $code = Invoke-LockedUnit { python -m research_news.xagi backfill --max 1 }
    if ($code -ne 0) {
        Log "no more queue units (or unit failed, exit $code) - phase 1 done"
        break
    }
    $done++
    Start-Sleep -Seconds 10   # brief gap so a pending daily can grab the lock
}
Log "phase 1 done ($done unit(s) this run)"

# ── phase 2: long reads that timed out earlier ────────────────────────────────
$longArgs = @("-m", "research_news.xagi", "long", "--max", "1")
if ($LongModel) { $longArgs += @("--model", $LongModel) }
$longDone = 0
while ($MaxLong -le 0 -or $longDone -lt $MaxLong) {
    if (Test-DailyWindow) { continue }
    $code = Invoke-LockedUnit { python @longArgs }
    if ($code -ne 0) {
        Log "no missing long reads (or one failed, exit $code) - phase 2 done"
        break
    }
    $longDone++
    Start-Sleep -Seconds 10
}
Log "xagi backfill loop done ($done unit(s), $longDone long read(s) this run)"
