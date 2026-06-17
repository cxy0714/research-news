# Register (or update) the research-news Task Scheduler jobs. Run ONCE from the
# repo root in PowerShell:
#   .\scripts\register-task.ps1                 # daily weekdays 09:10 + catch-up at logon
#   .\scripts\register-task.ps1 -Time "08:30"
#   .\scripts\register-task.ps1 -NoCatchUp      # only the daily task
# Re-running updates the existing tasks. If it complains about permissions, run
# from an elevated (Admin) PowerShell.

param(
    [datetime]$Time = "09:10",
    [string]$TaskName = "research-news-daily",
    [string]$CatchUpTaskName = "research-news-catchup",
    [switch]$NoCatchUp
)

$repo = Split-Path -Parent $PSScriptRoot          # repo root (script is in scripts\)

# Shared settings: catch up a missed start, never run two at once, ignore battery.
$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -MultipleInstances IgnoreNew `
    -ExecutionTimeLimit (New-TimeSpan -Hours 6) `
    -DontStopIfGoingOnBatteries -AllowStartIfOnBatteries

function Register-RnTask([string]$name, [string]$scriptFile, $trigger, [string]$desc) {
    $path = Join-Path $repo $scriptFile
    if (-not (Test-Path $path)) { throw "$scriptFile not found at $path" }
    $action = New-ScheduledTaskAction -Execute "powershell.exe" `
        -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$path`"" `
        -WorkingDirectory $repo
    # Current user, "run only when logged on" (no stored password).
    Register-ScheduledTask -TaskName $name -Action $action -Trigger $trigger `
        -Settings $settings -Description $desc -Force | Out-Null
}

# Daily report — weekdays at $Time.
$dailyTrigger = New-ScheduledTaskTrigger -Weekly `
    -DaysOfWeek Monday, Tuesday, Wednesday, Thursday, Friday -At $Time
Register-RnTask $TaskName "run_daily.ps1" $dailyTrigger "research-news daily pipeline"
Write-Host "Registered '$TaskName' for weekdays at $($Time.ToString('HH:mm'))."

# Catch-up — at logon (covers a boot after a few days off), 3-min delay so the
# desktop settles first. It only fills missing past weekdays; today stays the
# daily task's job.
if (-not $NoCatchUp) {
    $logon = New-ScheduledTaskTrigger -AtLogOn
    $logon.Delay = "PT3M"
    Register-RnTask $CatchUpTaskName "scripts\catch-up.ps1" $logon "research-news catch-up missed days"
    Write-Host "Registered '$CatchUpTaskName' to run at logon (+3 min)."
}

Write-Host ""
Write-Host "Test now:  Start-ScheduledTask -TaskName '$TaskName'"
Write-Host "Watch:     Get-ScheduledTaskInfo -TaskName '$TaskName'"
