# scripts/catch-up.ps1 — fill in daily reports missed while this machine was off.
#
# Finds the newest docs\daily\<date>.md, then runs `daily --date <X>` for every
# missing WEEKDAY from there up to *yesterday* (today is left to the scheduled
# 09:10 task / its "run if missed" catch-up). arXiv only announces on weekdays,
# so weekends are skipped. Safe + idempotent: the daily re-run guard skips any
# date that already has a report, and it shares the daily lock so it never runs
# in parallel with the scheduled run (it waits for it instead).
#
# Run it at logon/startup (register-task.ps1 sets this up), or by hand:
#   powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\catch-up.ps1
#   .\scripts\catch-up.ps1 -MaxDays 30      # look further back

param(
    [int]$MaxDays = 14   # don't catch up further back than this many calendar days
)

Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)   # repo root
$repo = (Get-Location).Path
$today = (Get-Date).Date

# Per-day, per-machine transcript (same scheme as run_daily.ps1).
New-Item -ItemType Directory -Force -Path "logs" | Out-Null
$hostTag = $env:COMPUTERNAME
if (-not $hostTag) { $hostTag = "host" }
$hostTag = ($hostTag -replace '[^A-Za-z0-9._-]', '-').ToLower()
Start-Transcript -Path "logs\catchup-$($today.ToString('yyyy-MM-dd'))-$hostTag.log" -Append -ErrorAction SilentlyContinue | Out-Null

$venvActivate = Join-Path $repo ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) { . $venvActivate }

# Same lock as the daily run. WAIT (don't bail) so we queue behind a running
# daily/scheduled task instead of skipping the catch-up entirely.
$mutex = New-Object System.Threading.Mutex($false, "Global\research-news-daily")
if (-not $mutex.WaitOne([TimeSpan]::FromMinutes(90))) {
    Write-Host "could not acquire the run lock within 90 min - will catch up next boot"
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
    return
}

$missing = @()
try {
    # Pull first so another machine's reports (and the latest code) are counted.
    git pull --rebase --autostash

    $reports = Get-ChildItem "docs\daily\*.md" -ErrorAction SilentlyContinue |
        ForEach-Object {
            if ($_.BaseName -match '^\d{4}-\d{2}-\d{2}$') {
                [datetime]::ParseExact($_.BaseName, 'yyyy-MM-dd', [System.Globalization.CultureInfo]::InvariantCulture)
            }
        } | Sort-Object
    if (-not $reports) {
        Write-Host "no existing daily reports - run daily once to bootstrap; nothing to catch up"
        return
    }

    $last = $reports[-1]
    $yesterday = $today.AddDays(-1)
    $start = $last.AddDays(1)
    $floor = $today.AddDays(-$MaxDays)
    if ($start -lt $floor) {
        Write-Host "gap exceeds -MaxDays ($MaxDays days): catching up only from $($floor.ToString('yyyy-MM-dd'))"
        $start = $floor
    }

    for ($d = $start; $d -le $yesterday; $d = $d.AddDays(1)) {
        if ($d.DayOfWeek -eq 'Saturday' -or $d.DayOfWeek -eq 'Sunday') { continue }
        $iso = $d.ToString('yyyy-MM-dd')
        if (-not (Test-Path "docs\daily\$iso.md")) { $missing += $iso }
    }

    if ($missing.Count -eq 0) {
        Write-Host "up to date - no missing weekdays through $($yesterday.ToString('yyyy-MM-dd'))"
        return
    }

    Write-Host "catching up $($missing.Count) missing weekday(s): $($missing -join ', ')"
    foreach ($iso in $missing) {
        Write-Host "=== daily --date $iso ==="
        python -m research_news.daily --date $iso
    }
}
finally {
    $mutex.ReleaseMutex()
    $mutex.Dispose()
    # Close the transcript before git stages it (avoid a Windows file lock).
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
}

# Commit + push all caught-up days together (transcript now closed + unlocked).
if ($missing.Count -gt 0 -and (git status --porcelain)) {
    git add -A
    git commit -m "catch-up: $($missing -join ', ')"
    for ($i = 1; $i -le 4; $i++) {
        git push
        if ($LASTEXITCODE -eq 0) { break }
        Start-Sleep -Seconds ([math]::Pow(2, $i))
    }
}
