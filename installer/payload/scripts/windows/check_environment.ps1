[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$tools = @("kicad-cli", "git", "python", "node", "npm", "code", "winget")
foreach ($tool in $tools) {
    $found = Get-Command $tool -ErrorAction SilentlyContinue
    if ($found) {
        Write-Output "FOUND $tool $($found.Source)"
    } else {
        Write-Output "MISSING $tool"
    }
}
