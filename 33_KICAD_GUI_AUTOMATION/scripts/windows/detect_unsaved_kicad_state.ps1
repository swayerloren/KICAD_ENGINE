param(
    [string]$ExpectedSchematicPath = "",
    [switch]$Json
)

$ErrorActionPreference = "Stop"

$scriptPath = Join-Path $PSScriptRoot "detect_eeschema_window.ps1"
$raw = & $scriptPath -ExpectedSchematicPath $ExpectedSchematicPath -Json
$windows = @()
if ($raw) { $windows = $raw | ConvertFrom-Json }

$result = [PSCustomObject]@{
    checked_at = (Get-Date).ToString("s")
    expected_schematic_path = $ExpectedSchematicPath
    eeschema_windows = $windows
    unsaved_window_count = @($windows | Where-Object { $_.unsaved_gui_state }).Count
    path_mismatch_count = @($windows | Where-Object { $ExpectedSchematicPath -and -not $_.path_match }).Count
    overall_status = if (@($windows).Count -eq 0) {
        "NO_EESCHEMA_WINDOW"
    } elseif (@($windows | Where-Object { $_.unsaved_gui_state }).Count -gt 0) {
        "UNSAVED_GUI_STATE"
    } elseif ($ExpectedSchematicPath -and @($windows | Where-Object { -not $_.path_match }).Count -gt 0) {
        "PATH_MISMATCH"
    } else {
        "GUI_STATE_READ_ONLY_OK"
    }
}

if ($Json) { $result | ConvertTo-Json -Depth 8 } else { $result | Format-List }
