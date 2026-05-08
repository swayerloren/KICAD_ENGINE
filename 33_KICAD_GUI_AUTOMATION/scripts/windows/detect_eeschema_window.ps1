param(
    [string]$ExpectedSchematicPath = "",
    [switch]$Json
)

$ErrorActionPreference = "Stop"

function Normalize-PathText {
    param([string]$PathText)
    if ([string]::IsNullOrWhiteSpace($PathText)) { return "" }
    try { return [System.IO.Path]::GetFullPath($PathText).TrimEnd('\').ToLowerInvariant() }
    catch { return $PathText.TrimEnd('\').ToLowerInvariant() }
}

$expected = Normalize-PathText $ExpectedSchematicPath
$windows = Get-CimInstance Win32_Process |
    Where-Object { $_.Name -eq 'eeschema.exe' } |
    ForEach-Object {
        $proc = Get-Process -Id $_.ProcessId -ErrorAction SilentlyContinue
        $cmd = $_.CommandLine
        $openPath = ""
        if ($cmd -match '"([^"]+\.kicad_sch)"') { $openPath = $Matches[1] }
        $openNorm = Normalize-PathText $openPath
        $title = if ($proc) { $proc.MainWindowTitle } else { "" }
        [PSCustomObject]@{
            process_id = $_.ProcessId
            title = $title
            command_line = $cmd
            open_schematic_path = $openPath
            expected_schematic_path = $ExpectedSchematicPath
            path_match = if ($expected -and $openNorm) { $openNorm -eq $expected } else { $false }
            unsaved_gui_state = if ($title) { $title.StartsWith("*") } else { $false }
            safe_for_read_only_discovery = [bool]$openPath
            safe_for_gui_save = $false
            reason_save_blocked = "Saving through automation requires explicit backup, path-match, screenshot evidence, and user approval."
        }
    }

if ($Json) { $windows | ConvertTo-Json -Depth 5 } else { $windows | Format-List }
