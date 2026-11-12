# Windows runner for the two AI-track daily radars — invoked by Task Scheduler
# (research-news-ai-radar / research-news-autoresearch) and safe to run by hand.
#
#   .\run_ai_radar.ps1                        # AI 评测雷达 (benchmarks daily)
#   .\run_ai_radar.ps1 -Radar autoresearch    # AI auto-research 雷达
#   .\run_ai_radar.ps1 -Date 2026-11-11       # backfill one missed day
#   .\run_ai_radar.ps1 -Force                 # re-render even if the page exists
#
# Why this exists separately from run_daily.ps1: the radars used to be the last
# step of the daily chain, so when daily died early (11-11) the radar silently
# skipped and no page was ever produced — nothing in Task Scheduler showed it.
# Now each radar has its own task, its own log and its own exit code, and both
# sides pass --if-missing so whichever runs first wins without double LLM spend.
#
# Locking: the radars take the SAME named mutex as the daily run / journal and
# deep-read loops, so they queue behind a running unit instead of racing it for
# the LLM rate limit (9 req/min is global).
param(
    [ValidateSet("ai-eval", "autoresearch")] [string]$Radar = "ai-eval",
    [string]$Date = "",
    [switch]$Force
)

$ErrorActionPreference = "Continue"
Set-Location -LiteralPath $PSScriptRoot

$hostTag = $env:COMPUTERNAME
if (-not $hostTag) { $hostTag = "host" }
$hostTag = ($hostTag -replace '[^A-Za-z0-9._-]', '-').ToLower()
New-Item -ItemType Directory -Force -Path "logs" | Out-Null

$day = if ($Date) { $Date } else { Get-Date -Format "yyyy-MM-dd" }
$logFile = "logs\radar-$Radar-$day-$hostTag.log"

function Log($msg) {
    $line = "[$(Get-Date -Format o)] $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -ErrorAction SilentlyContinue
}

function Push-Changes([string]$msg) {
    if (-not (git status --porcelain)) {
        Log "nothing to commit"
        return
    }
    git add -A
    git commit -m $msg | Out-Null
    for ($i = 1; $i -le 4; $i++) {
        git push
        if ($LASTEXITCODE -eq 0) {
            Log "push OK, HEAD = $(git rev-parse --short HEAD)"
            return
        }
        Start-Sleep -Seconds ([math]::Pow(2, $i))
        git pull --rebase --autostash
    }
    Log "!!! push FAILED after 4 attempts - $Radar $day stays local-only"
}

# ── map the track to its python entry point ──────────────────────────────────
switch ($Radar) {
    "ai-eval" {
        $module = "research_news.benchmarks"
        $args_ = @("daily")
    }
    "autoresearch" {
        $module = "research_news.autoresearch"
        $args_ = @("daily")
    }
}
if ($Date) { $args_ += @("--date", $Date) }
if (-not $Force) { $args_ += "--if-missing" }

$venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) { . $venvActivate }

# ── one lock hold around fetch + score + render ─────────────────────────────
$mutex = New-Object System.Threading.Mutex($false, "Global\research-news-daily")
if (-not $mutex.WaitOne([TimeSpan]::FromMinutes(60))) {
    Log "$Radar $day : lock held >60 min - giving up this run"
    $mutex.Dispose()
    exit 1
}

$code = 1
try {
    Log "$Radar $day : start ($module $($args_ -join ' '))"
    git pull --rebase --autostash
    python -m $module $args_
    $code = $LASTEXITCODE
}
finally {
    $mutex.ReleaseMutex()
    $mutex.Dispose()
}

if ($code -eq 0) {
    Log "$Radar $day : OK (exit 0)"
    Push-Changes "ai radar $Radar $day"
} else {
    Log "$Radar $day : FAILED (exit $code)"
}
exit $code
