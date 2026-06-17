# Register (or update) the research-news Task Scheduler jobs. Run ONCE from the
# repo root. Registering tasks can require admin — if you get "Access denied",
# re-run this from an ELEVATED PowerShell (Start menu -> Windows PowerShell ->
# Run as administrator; then `cd <repo>; .\scripts\register-task.ps1`).
#   .\scripts\register-task.ps1                 # daily weekdays 09:10 + catch-up at logon
#   .\scripts\register-task.ps1 -Time "08:30"
#   .\scripts\register-task.ps1 -NoCatchUp      # only the daily task

param(
    [datetime]$Time = "09:10",
    [string]$TaskName = "research-news-daily",
    [string]$CatchUpTaskName = "research-news-catchup",
    [switch]$NoCatchUp
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

function Register-RnTask([string]$name, [string]$scriptFile, $trigger, [string]$desc) {
    $path = Join-Path $repo $scriptFile
    if (-not (Test-Path $path)) { Write-Warning "$scriptFile not found at $path - skipped"; return $false }
    $action = New-ScheduledTaskAction -Execute "powershell.exe" `
        -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$path`"" `
        -WorkingDirectory $repo
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

Write-Host ""
Write-Host "Test now:  Start-ScheduledTask -TaskName '$TaskName'"
Write-Host "List both: Get-ScheduledTask -TaskName 'research-news-*'"
