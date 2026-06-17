# Register (or update) the daily research-news task in Windows Task Scheduler.
# Run ONCE from the repo root in PowerShell:
#   .\scripts\register-task.ps1                 # weekdays at 09:10
#   .\scripts\register-task.ps1 -Time "08:30"
# Re-running with -Force updates the existing task. If it complains about
# permissions, run from an elevated (Admin) PowerShell.

param(
    [datetime]$Time = "09:10",
    [string]$TaskName = "research-news-daily"
)

$repo   = Split-Path -Parent $PSScriptRoot          # repo root (script is in scripts\)
$script = Join-Path $repo "run_daily.ps1"
if (-not (Test-Path $script)) { throw "run_daily.ps1 not found at $script" }

$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$script`"" `
    -WorkingDirectory $repo

$trigger = New-ScheduledTaskTrigger -Weekly `
    -DaysOfWeek Monday, Tuesday, Wednesday, Thursday, Friday -At $Time

# StartWhenAvailable: catch up a missed start (PC was off/asleep).
# MultipleInstances IgnoreNew: never run two at once.
# Battery flags: don't let a laptop's power state block the run.
$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -MultipleInstances IgnoreNew `
    -ExecutionTimeLimit (New-TimeSpan -Hours 6) `
    -DontStopIfGoingOnBatteries -AllowStartIfOnBatteries

# Registers for the current user, "run only when logged on" (no stored password).
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger `
    -Settings $settings -Description "research-news daily pipeline" -Force | Out-Null

Write-Host "Registered task '$TaskName' for weekdays at $($Time.ToString('HH:mm'))."
Write-Host "Run it now to test:  Start-ScheduledTask -TaskName '$TaskName'"
Write-Host "Watch it:            Get-ScheduledTaskInfo -TaskName '$TaskName'"
