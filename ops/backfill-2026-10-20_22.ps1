# ops\backfill-2026-10-20_22.ps1 — one-off backfill for the 2026-10-20..22 gap.
#
# Why these dates:
#   * 2026-10-20 (Tue), 2026-10-21 (Wed) — no docs\daily\<date>.md at all and no
#     rows in data\llm_scores.jsonl, i.e. the daily run never happened (the
#     2026-10-21 log on disk is the *catch-up for 10-19*, not a 10-21 run).
#   * 2026-10-22 (Thu) — the page exists but is a 248-byte garbled stub with
#     0 papers (arXiv RSS died with SSL errors at 09:10 that morning), so it
#     needs a full --force regeneration.
#   (2026-10-24/25 are the weekend — arXiv announces on weekdays only.)
#
# It mirrors run_daily.ps1/scripts\catch-up.ps1: same single-instance mutex, same
# venv, same daily -> rerun -> retry-stubs sequence, and it commits+pushes after
# each date so partial progress survives a failure on a later date.
#
# Run it detached (this is what the "start now" scheduler hook does):
#   powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\ops\backfill-2026-10-20_22.ps1
#
# Progress: logs\backfill-<stamp>-<host>.log (transcript) + tmp\backfill-status.json.

param(
    [string[]]$Dates = @("2026-10-20", "2026-10-21", "2026-10-22"),
    # --force = regenerate even though a page may exist (needed for the empty
    # 2026-10-22 stub; also skips seen-set dedup so the re-render is complete).
    [string[]]$ForceDates = @("2026-10-22"),
    # Render the pages first, skip the long PDF/deep-read pass. Needed when the
    # deep-read model (deepseek-reasoner) blows the 300s per-request timeout on
    # 35k-char full texts: every paper then burns 3 x 5 min and 28 papers would
    # hold the daily mutex for ~6h. Deep reads are backfilled separately later.
    [switch]$SkipDeepReads
)

$repo = Split-Path -Parent $PSScriptRoot          # ops\ -> repo root
Set-Location -LiteralPath $repo

$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$hostTag = $env:COMPUTERNAME
if (-not $hostTag) { $hostTag = "host" }
$hostTag = ($hostTag -replace '[^A-Za-z0-9._-]', '-').ToLower()

New-Item -ItemType Directory -Force -Path "logs", "tmp" | Out-Null
$transcript = "logs\backfill-$stamp-$hostTag.log"
Start-Transcript -Path $transcript -Append -ErrorAction SilentlyContinue | Out-Null

$env:PYTHONIOENCODING = "utf-8"
$py = Join-Path $repo ".venv\Scripts\python.exe"
if (-not (Test-Path $py)) { $py = "python" }

$statusPath = Join-Path $repo "tmp\backfill-status.json"
function Write-Status([string]$state, [string]$detail) {
    $payload = [ordered]@{
        state     = $state
        detail    = $detail
        dates     = $Dates
        updated   = (Get-Date -Format o)
        pid       = $PID
        transcript = $transcript
    }
    try {
        $payload | ConvertTo-Json | Set-Content -LiteralPath $statusPath -Encoding UTF8
    } catch { }
}

Write-Host "=== research-news backfill $($Dates -join ', ') (forced: $($ForceDates -join ', ')) ==="
Write-Host "repo=$repo python=$py"
Write-Status "starting" "acquiring lock"

# Same lock as the daily / catch-up / journal tasks; WAIT rather than bail so we
# queue behind a running unit instead of skipping the backfill.
$mutex = New-Object System.Threading.Mutex($false, "Global\research-news-daily")
if (-not $mutex.WaitOne([TimeSpan]::FromHours(3))) {
    Write-Host "could not acquire the run lock within 3h - aborting backfill"
    Write-Status "failed" "lock timeout"
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
    exit 1
}

function Push-Commit([string]$message) {
    if (-not (git status --porcelain)) {
        Write-Host "nothing to commit for '$message'"
        return $true
    }
    git add -A
    git commit -m $message | Out-Host
    for ($i = 1; $i -le 4; $i++) {
        git push 2>&1 | Out-Host
        if ($LASTEXITCODE -eq 0) {
            Write-Host "push OK, HEAD = $(git rev-parse --short HEAD)"
            return $true
        }
        Start-Sleep -Seconds ([math]::Pow(2, $i))
        git pull --rebase --autostash 2>&1 | Out-Host
    }
    Write-Host "!!! PUSH FAILED after 4 attempts - commit '$message' stays local-only"
    return $false
}

$results = [ordered]@{}
try {
    # Pull first so this machine is not behind another machine's reports/code.
    git pull --rebase --autostash 2>&1 | Out-Host

    foreach ($iso in $Dates) {
        $page = "docs\daily\$iso.md"
        $force = $ForceDates -contains $iso
        $argsList = @("-m", "research_news.daily", "--date", $iso)
        if ($force) { $argsList += "--force" }
        if ($SkipDeepReads) { $argsList += "--skip-deep-reads" }

        Write-Host ""
        Write-Host "=== [$iso] python $($argsList -join ' ') ==="
        Write-Status "running" "daily --date $iso"
        $sw = [Diagnostics.Stopwatch]::StartNew()
        & $py @argsList 2>&1 | Out-Host
        $code = $LASTEXITCODE
        $sw.Stop()
        Write-Host "=== [$iso] daily exit=$code in $([int]$sw.Elapsed.TotalMinutes) min ==="

        if ($code -ne 0) {
            $results[$iso] = "daily FAILED (exit $code)"
            Write-Status "running" "daily failed for $iso"
            continue
        }
        # Same post-steps run_daily.ps1 does for today's page.
        & $py -m research_news.rerun --date $iso 2>&1 | Out-Host
        if ($SkipDeepReads) {
            Write-Host "=== [$iso] --skip-deep-reads: not retrying deep-read stubs ==="
        } else {
            & $py -m research_news.backfill_deep_reads --retry-stubs --date $iso 2>&1 | Out-Host
        }

        if (Test-Path $page) {
            $size = (Get-Item $page).Length
            $results[$iso] = "wrote $page ($size bytes)"
        } else {
            $results[$iso] = "daily exit 0 but NO page written"
        }
        Push-Commit "daily report $iso (backfill)" | Out-Null
        Write-Status "running" "done $iso; $(($results.GetEnumerator() | ForEach-Object { "$($_.Key)=$($_.Value)" }) -join '; ')"
    }
}
finally {
    $mutex.ReleaseMutex()
    $mutex.Dispose()
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
}

Write-Host ""
Write-Host "=== backfill summary ==="
$results.GetEnumerator() | ForEach-Object { Write-Host ("{0}: {1}" -f $_.Key, $_.Value) }
Write-Status "finished" (($results.GetEnumerator() | ForEach-Object { "$($_.Key)=$($_.Value)" }) -join '; ')

# Final sweep: push anything left over (e.g. index/all_daily.md touched after the
# last per-date commit).
Push-Commit "backfill 2026-10-20..22: docs index" | Out-Null
Write-Host "transcript: $transcript"