# Register (or update) the research-news Task Scheduler jobs. Run ONCE from the
# repo root. Registering tasks can require admin — if you get "Access denied",
# re-run this from an ELEVATED PowerShell (Start menu -> Windows PowerShell ->
# Run as administrator; then `cd <repo>; .\scripts\register-task.ps1`).
#   .\scripts\register-task.ps1                       # daily 09:10 + catch-up + journals
#   .\scripts\register-task.ps1 -Time "08:30"
#   .\scripts\register-task.ps1 -NoCatchUp -NoJournals  # only the daily task
#   .\scripts\register-task.ps1 -JournalTime "14:00" -JournalMax 2

param(
    [datetime]$Time = "09:10",
    [datetime]$JournalTime = "10:30",
    [int]$JournalMax = 1,
    [string]$TaskName = "research-news-daily",
    [string]$CatchUpTaskName = "research-news-catchup",
    [string]$JournalTaskName = "research-news-journals",
    [switch]$NoCatchUp,
    [switch]$NoJournals
)

$repo = Split-Path -Parent $PSScriptRoot          # repo root (script is in scripts\)

$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Warning "Not elevated. If a task fails with 'Access denied (0x80070005)', re-run this from an elevated PowerShell (Run as administrator)."
}

# Shared settings: catch up a missed start, never run two at once, ignore battery.
$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -MultipleInstances IgnoreNew `
    -ExecutionTimeLimit (New-TimeSpan -Hours 6) `
    -DontStopIfGoingOnBatteries -AllowStartIfOnBatteries

function Register-RnTask([string]$name, [string]$scriptFile, $trigger, [string]$desc, [string]$extraArgs = "") {
    $path = Join-Path $repo $scriptFile
    if (-not (Test-Path $path)) { Write-Warning "$scriptFile not found at $path - skipped"; return $false }
    $argument = "-NoProfile -ExecutionPolicy Bypass -File `"$path`""
    if ($extraArgs) { $argument += " $extraArgs" }
    $action = New-ScheduledTaskAction -Execute "powershell.exe" `
        -Argument $argument -WorkingDirectory $repo
    try {
        # Current user, "run only when logged on" (no stored password).
        Register-ScheduledTask -TaskName $name -Action $action -Trigger $trigger `
            -Settings $settings -Description $desc -Force -ErrorAction Stop | Out-Null
        return $true
    } catch {
        Write-Warning "Failed to register '$name': $($_.Exception.Message)"
        if ("$($_.Exception.Message)" -match 'denied|0x80070005') {
            Write-Warning "  -> re-run this script in an ELEVATED PowerShell (Run as administrator)."
        }
        return $false
    }
}

# Daily report — weekdays at $Time.
$dailyTrigger = New-ScheduledTaskTrigger -Weekly `
    -DaysOfWeek Monday, Tuesday, Wednesday, Thursday, Friday -At $Time
if (Register-RnTask $TaskName "run_daily.ps1" $dailyTrigger "research-news daily pipeline") {
    Write-Host "OK: '$TaskName' - weekdays at $($Time.ToString('HH:mm'))."
}

# Catch-up — at logon (+10 min so the desktop settles). Only fills missing past
# weekdays; today stays the daily task's job.
if (-not $NoCatchUp) {
    $logon = New-ScheduledTaskTrigger -AtLogOn
    $logon.Delay = "PT10M"
    if (Register-RnTask $CatchUpTaskName "scripts\catch-up.ps1" $logon "research-news catch-up missed days") {
        Write-Host "OK: '$CatchUpTaskName' - at logon (+10 min)."
    }
}

# Journal back-catalog — weekdays at $JournalTime (after daily). Does the next
# $JournalMax unit(s) of ops\journal-backfill.md; shares the daily lock so it
# never overlaps the daily run.
if (-not $NoJournals) {
    $journalTrigger = New-ScheduledTaskTrigger -Weekly `
        -DaysOfWeek Monday, Tuesday, Wednesday, Thursday, Friday -At $JournalTime
    if (Register-RnTask $JournalTaskName "run_journal_backfill.ps1" $journalTrigger `
            "research-news journal back-catalog backfill" "-Max $JournalMax") {
        Write-Host "OK: '$JournalTaskName' - weekdays at $($JournalTime.ToString('HH:mm')) (max $JournalMax unit/run)."
    }
}

Write-Host ""
Write-Host "Test now:  Start-ScheduledTask -TaskName '$TaskName'"
Write-Host "List all:  Get-ScheduledTask -TaskName 'research-news-*'"
