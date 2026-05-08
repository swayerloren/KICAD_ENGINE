param(
    [Parameter(Mandatory = $true)]
    [string]$BoardPath,

    [Parameter(Mandatory = $true)]
    [string]$OutputDsnPath,

    [string]$ManualDsnPath,

    [switch]$Force
)

$ErrorActionPreference = "Stop"

function Resolve-FullPath {
    param([Parameter(Mandatory = $true)][string]$PathValue)
    $item = Resolve-Path -LiteralPath $PathValue
    return $item.Path
}

$board = Resolve-FullPath -PathValue $BoardPath

if ([System.IO.Path]::GetExtension($board).ToLowerInvariant() -ne ".kicad_pcb") {
    throw "BoardPath must point to a .kicad_pcb file."
}

$outputFull = [System.IO.Path]::GetFullPath($OutputDsnPath)
$outputDir = Split-Path -Parent $outputFull
if (-not [string]::IsNullOrWhiteSpace($outputDir)) {
    New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
}

if ((Test-Path -LiteralPath $outputFull) -and (-not $Force)) {
    throw "Output DSN already exists. Use -Force to replace it."
}

$result = [ordered]@{
    review_status = "REVIEW_ONLY"
    action = $null
    board_path = $board
    output_dsn_path = $outputFull
    source_dsn_path = $null
    notes = @()
}

if ($ManualDsnPath) {
    $manual = Resolve-FullPath -PathValue $ManualDsnPath
    if ([System.IO.Path]::GetExtension($manual).ToLowerInvariant() -ne ".dsn") {
        throw "ManualDsnPath must point to a .dsn file."
    }
    Copy-Item -LiteralPath $manual -Destination $outputFull -Force
    $result.action = "COPIED_MANUAL_DSN"
    $result.source_dsn_path = $manual
    $result.notes += "No KiCad PCB file was modified."
    $result.notes += "This staged DSN is review-only input for routing feasibility."
    $result | ConvertTo-Json -Depth 6
    exit 0
}

$siblingDsn = [System.IO.Path]::ChangeExtension($board, ".dsn")
if (Test-Path -LiteralPath $siblingDsn) {
    Copy-Item -LiteralPath $siblingDsn -Destination $outputFull -Force
    $result.action = "COPIED_EXISTING_SIBLING_DSN"
    $result.source_dsn_path = $siblingDsn
    $result.notes += "No KiCad PCB file was modified."
    $result.notes += "This staged DSN is review-only input for routing feasibility."
    $result | ConvertTo-Json -Depth 6
    exit 0
}

$kicadCli = Get-Command kicad-cli -ErrorAction SilentlyContinue
if ($kicadCli) {
    $helpText = (& $kicadCli.Source pcb export --help 2>&1 | Out-String)
    if ($helpText -match "specctra|dsn") {
        throw "Specctra export may exist in this KiCad build, but this script does not drive it yet. Export the DSN manually from a copied or sandbox board, then rerun with -ManualDsnPath."
    }
}

throw "No existing DSN was found and no verified headless DSN export path is wired here. Export a .dsn manually from KiCad PCB Editor on a copied or sandbox board, then rerun with -ManualDsnPath."
