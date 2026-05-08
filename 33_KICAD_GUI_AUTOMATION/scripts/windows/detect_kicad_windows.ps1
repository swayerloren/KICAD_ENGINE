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
$processes = Get-CimInstance Win32_Process |
    Where-Object { $_.Name -match '^(kicad|eeschema|pcbnew)\.exe$' } |
    ForEach-Object {
        $proc = Get-Process -Id $_.ProcessId -ErrorAction SilentlyContinue
        $cmd = $_.CommandLine
        $openPath = ""
        if ($cmd -match '"([^"]+\.kicad_sch)"') { $openPath = $Matches[1] }
        elseif ($cmd -match '"([^"]+\.kicad_pro)"') { $openPath = $Matches[1] }
        $openNorm = Normalize-PathText $openPath
        [PSCustomObject]@{
            process_id = $_.ProcessId
            process_name = $_.Name
            executable_path = $_.ExecutablePath
            window_title = if ($proc) { $proc.MainWindowTitle } else { "" }
            command_line = $cmd
            open_path = $openPath
            open_path_matches_expected = if ($expected -and $openNorm) { $openNorm -eq $expected } else { $null }
            unsaved_title_marker = if ($proc -and $proc.MainWindowTitle) { $proc.MainWindowTitle.StartsWith("*") } else { $false }
        }
    }

if ($Json) {
    $processes | ConvertTo-Json -Depth 5
} else {
    $processes | Format-List
}
