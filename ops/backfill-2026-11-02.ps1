# ops\backfill-2026-11-02.ps1 — one-off backfill for the 2026-11-02 (Mon) gap.
#
# Why this date:
#   * docs\daily\ has 2026-10-30, 2026-11-03 … 2026-11-06 but NO
#     2026-11-02.md: that Monday's daily run never produced a page (the machine
#     was off / the run was interrupted), and the catch-up path only walks to
#     *yesterday*, so it kept sliding past the gap.
#   * data\llm_scores.jsonl has no run_date = 2026-11-02 rows at all.
#   * --force is required: the 2026-11-03 run's 3-day Hexagon lookback already
#     absorbed 11-02's Hexagon batch (and a few late-announced arXiv ids) into
#     the seen-set, so a plain re-run would filter almost everything out and
#     render a near-empty page. --force skips seen-set dedup for a complete
#     re-render of that day.
#   * --skip-deep-reads: those same papers were already deep-read by the
#     11-03/11-04 runs. `backfill_deep_reads --date 2026-11-02 --dry-run`
#     reports "nothing to backfill (no new papers >= 6)", so the long PDF /
#     deep-read pass would only burn hours re-reading them under a new date.
#
# Mirrors run_daily.ps1 / scripts\catch-up.ps1 / ops\backfill-2026-10-20_22.ps1:
# same single-instance mutex, same venv, daily -> rerun -> commit/push.
#
# Run it detached:
#   powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\ops\backfill-2026-11-02.ps1
#
# Progress: logs\backfill-<stamp>-<host>.log (transcript) +
#           tmp\backfill-2026-11-02-status.json

param(
    [string]$Date = "2026-11-02",
    # Drop this switch if a future re-run should also (re)do PDF + deep reads.
    [switch]$WithDeepReads
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

$statusPath = Join-Path $repo "tmp\backfill-2026-11-02-status.json"
function Write-Status([string]$state, [string]$detail) {
    $payload = [ordered]@{
        state      = $state
        detail     = $detail
        date       = $Date
        updated    = (Get-Date -Format o)
        pid        = $PID
        transcript = $transcript
    }
    try {
        $payload | ConvertTo-Json | Set-Content -LiteralPath $statusPath -Encoding UTF8
    } catch { }
}

Write-Host "=== research-news backfill $Date (force; deep reads: $([bool]$WithDeepReads)) ==="
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

$page = "docs\daily\$Date.md"
try {
    # Pull first so this machine is not behind another machine's reports/code.
    git pull --rebase --autostash 2>&1 | Out-Host

    $argsList = @("-m", "research_news.daily", "--date", $Date, "--force")
    if (-not $WithDeepReads) { $argsList += "--skip-deep-reads" }

    Write-Host ""
    Write-Host "=== [$Date] python $($argsList -join ' ') ==="
    Write-Status "running" "daily --date $Date"
    $sw = [Diagnostics.Stopwatch]::StartNew()
    & $py @argsList 2>&1 | Out-Host
    $code = $LASTEXITCODE
    $sw.Stop()
    Write-Host "=== [$Date] daily exit=$code in $([int]$sw.Elapsed.TotalMinutes) min ==="

    if ($code -ne 0) {
        Write-Status "failed" "daily exit $code"
        throw "daily failed with exit $code"
    }

    # Same post-step run_daily.ps1 does for the day's page (garble/truncation fix).
    & $py -m research_news.rerun --date $Date 2>&1 | Out-Host

    if ($WithDeepReads) {
        & $py -m research_news.backfill_deep_reads --retry-stubs --date $Date 2>&1 | Out-Host
    } else {
        Write-Host "=== [$Date] --skip-deep-reads: deep reads already covered by the 11-03+ runs ==="
    }

    if (-not (Test-Path $page)) {
        Write-Status "failed" "daily exit 0 but no page written"
        throw "daily exit 0 but $page was not written"
    }
    $size = (Get-Item $page).Length
    $head = (Get-Content $page -TotalCount 3 -Encoding UTF8) -join ' | '
    Write-Host "=== [$Date] wrote $page ($size bytes) ==="
    Write-Host "=== [$Date] head: $head ==="

    Push-Commit "daily report $Date (backfill)" | Out-Null
    # update_index() runs inside daily; sweep any index/all_daily.md leftovers.
    Push-Commit "daily backfill $Date : docs index" | Out-Null

    Write-Status "finished" "wrote $page ($size bytes)"
}
catch {
    Write-Host "!!! backfill aborted: $($_.Exception.Message)"
    Write-Status "failed" "$($_.Exception.Message)"
}
finally {
    $mutex.ReleaseMutex()
    $mutex.Dispose()
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
}

Write-Host "transcript: $transcript"