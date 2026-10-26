# ops\backfill-deepreads-2026-10-20_22.ps1 — fill the deep reads (精读) for the
# three backfilled daily pages, using a model that actually finishes inside the
# 300s request budget.
#
# Why: the pages for 2026-10-20/21/22 were rendered with --skip-deep-reads
# because DEEP_READ_MODEL=deepseek-reasoner blows SJTU_TIMEOUT (300s x 3 retries
# = 15 min per paper) on these 35k-char full texts. deepseek-chat is the same
# fallback the XAGI long-read phase uses (run_xagi_backfill.ps1 -LongModel).
#
# Two passes:
#   1. threshold backfill — deep-read every >=threshold paper in the range that
#      has no deep-read page yet (10-21 and 10-22 have none at all);
#   2. --retry-stubs — regenerate the three deep reads that FAILED on 10-20
#      before the switch to --skip-deep-reads.
#
# Run detached (harness background job):
#   powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\ops\backfill-deepreads-2026-10-20_22.ps1

param(
    [string]$Since = "2026-10-20",
    [string]$Until = "2026-10-22",
    [string]$Model = "deepseek-chat"
)

$repo = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repo

$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$hostTag = $env:COMPUTERNAME
if (-not $hostTag) { $hostTag = "host" }
$hostTag = ($hostTag -replace '[^A-Za-z0-9._-]', '-').ToLower()

New-Item -ItemType Directory -Force -Path "logs", "tmp" | Out-Null
$transcript = "logs\deepreads-$stamp-$hostTag.log"
Start-Transcript -Path $transcript -Append -ErrorAction SilentlyContinue | Out-Null

$env:PYTHONIOENCODING = "utf-8"
$py = Join-Path $repo ".venv\Scripts\python.exe"
if (-not (Test-Path $py)) { $py = "python" }

$statusPath = Join-Path $repo "tmp\deepreads-status.json"
function Write-Status([string]$state, [string]$detail) {
    try {
        [ordered]@{
            state = $state; detail = $detail; since = $Since; until = $Until
            model = $Model; updated = (Get-Date -Format o); pid = $PID
            transcript = $transcript
        } | ConvertTo-Json | Set-Content -LiteralPath $statusPath -Encoding UTF8
    } catch { }
}

Write-Host "=== deep-read backfill $Since..$Until (model=$Model) ==="
Write-Status "running" "waiting for lock"

$mutex = New-Object System.Threading.Mutex($false, "Global\research-news-daily")
if (-not $mutex.WaitOne([TimeSpan]::FromHours(3))) {
    Write-Host "could not acquire the run lock within 3h - aborting"
    Write-Status "failed" "lock timeout"
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
    exit 1
}

try {
    git pull --rebase --autostash 2>&1 | Out-Host

    Write-Host "=== pass 1/2: threshold backfill ==="
    Write-Status "running" "threshold backfill"
    & $py -m research_news.backfill_deep_reads --since $Since --until $Until --model $Model 2>&1 | Out-Host
    $pass1 = $LASTEXITCODE

    Write-Host "=== pass 2/2: retry failed stubs ==="
    Write-Status "running" "retry-stubs"
    & $py -m research_news.backfill_deep_reads --retry-stubs --since $Since --until $Until --model $Model 2>&1 | Out-Host
    $pass2 = $LASTEXITCODE
}
finally {
    $mutex.ReleaseMutex()
    $mutex.Dispose()
    Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
}

# Commit + push whatever changed (docs\deep_reads\, index, daily pages).
if (git status --porcelain) {
    git add -A
    git commit -m "deep reads $Since..$Until (backfill, model=$Model)" | Out-Host
    $pushed = $false
    for ($i = 1; $i -le 4; $i++) {
        git push 2>&1 | Out-Host
        if ($LASTEXITCODE -eq 0) { $pushed = $true; break }
        Start-Sleep -Seconds ([math]::Pow(2, $i))
        git pull --rebase --autostash 2>&1 | Out-Host
    }
    if (-not $pushed) { Write-Host "!!! PUSH FAILED - deep reads stay local-only" }
} else {
    Write-Host "nothing to commit after deep-read backfill"
}

$n = (Get-ChildItem "docs\deep_reads" -Filter "$Since-*.md" -ErrorAction SilentlyContinue |
      Where-Object { $_.BaseName -match "^$([regex]::Escape($Since))-" } | Measure-Object).Count
Write-Status "finished" "pass1=$pass1 pass2=$pass2; deep-read files on $Since = $n"
Write-Host "transcript: $transcript"