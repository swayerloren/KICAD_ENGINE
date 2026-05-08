# ESP32_CSI_WIFI_NODE GUI Annotation Diagnosis Commands

Date: `2026-05-06`

Working directory: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Required Reads

```powershell
Get-Content -Path 'AGENTS.md' -Raw
Get-Content -Path 'README_GPT.md' -Raw
Get-Content -Path 'FOR CHAT GPT.MD' -Raw
Get-Content -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md' -Raw
Get-Content -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ANNOTATION_REFERENCE_TABLE_FINAL.md' -Raw
Get-Content -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\EMERGENCY_ANNOTATION_REPAIR_REPORT.md' -Raw
Get-Content -Path '02_HISTORY\command_logs\ESP32_CSI_WIFI_NODE_ACTUAL_KICAD_ANNOTATION_REPAIR_COMMANDS.md' -Raw
```

## Active File Check

```powershell
Get-Item -LiteralPath 'C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
Get-FileHash -Algorithm SHA256 -LiteralPath 'C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Result:

- LastWriteTime: `2026-05-06 18:34:24`
- SHA256: `D0706DEDE551179DB96BF3CC5AE2F0072DF8CE15AE577EDADED4A7B0EB4DA15C`

## Duplicate File Search

```powershell
Get-ChildItem -Path . -Recurse -Filter 'ESP32_CSI_WIFI_NODE.kicad_sch' -File
```

Result: the active schematic plus backup copies under `99_BACKUPS/pre_codex_edits`.

## KiCad GUI Process Inspection

```powershell
Get-CimInstance Win32_Process | Where-Object { $_.Name -match 'kicad|eeschema' } | Select-Object ProcessId,Name,CommandLine
Get-Process | Where-Object { $_.ProcessName -match 'kicad|eeschema' } | Select-Object Id,ProcessName,MainWindowTitle,Path
```

Result:

```text
ProcessId: 3232
Name: eeschema.exe
CommandLine: "C:\Program Files\KiCad\9.0\bin\eeschema.exe" "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch"
MainWindowTitle: *ESP32_CSI_WIFI_NODE [ESP32_CSI_WIFI_NODE] - Schematic Editor
```

## Structured Placed-Symbol Parse

```powershell
# Inline Python parser extracted actual placed symbol blocks from the active .kicad_sch file.
```

Result:

- placed symbols: `79`
- bad refs in saved placed-symbol blocks: `0`
- duplicate refs in saved placed-symbol blocks: `0`

## ERC

```powershell
kicad-cli sch erc --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\GUI_MISMATCH_DIAGNOSIS_ERC_FROM_REPO_ROOT.rpt' 'C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Result: `Found 0 violations`

```powershell
kicad-cli sch erc --output '..\reports\GUI_MISMATCH_DIAGNOSIS_ERC_FROM_PROJECT_DIR.rpt' 'ESP32_CSI_WIFI_NODE.kicad_sch'
```

Run from:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad`

Result: `Found 0 violations`

## KiCad ERC Help

```powershell
kicad-cli sch erc --help
```

Result: command accepts one `INPUT_FILE` schematic argument. No separate `.kicad_pro` ERC argument or annotation command is exposed.

## Files Created

```text
04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\GUI_ANNOTATION_MISMATCH_DIAGNOSIS.md
04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\KICAD_NATIVE_ANNOTATION_RESULT.md
04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ANNOTATION_REFERENCE_TABLE_GUI_VERIFIED.md
02_HISTORY\sessions\ESP32_CSI_WIFI_NODE_GUI_ANNOTATION_DIAGNOSIS_SESSION.md
02_HISTORY\command_logs\ESP32_CSI_WIFI_NODE_GUI_ANNOTATION_DIAGNOSIS_COMMANDS.md
02_HISTORY\quality_gate_failures\ESP32_CSI_CODEX_TEXT_EDIT_ANNOTATION_FAILED.md
```

## Final Read-Only Recheck

```powershell
kicad-cli sch erc --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\GUI_MISMATCH_DIAGNOSIS_ERC_FINAL_RECHECK.rpt' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
Get-Item -LiteralPath '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
Get-FileHash -Algorithm SHA256 -LiteralPath '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
Get-Process | Where-Object { $_.ProcessName -match 'kicad|eeschema' } | Select-Object Id,ProcessName,MainWindowTitle,Path
```

Result:

- CLI ERC final recheck: `Found 0 violations`
- active schematic last write remained `2026-05-06 18:34:24`
- active schematic hash remained `D0706DEDE551179DB96BF3CC5AE2F0072DF8CE15AE577EDADED4A7B0EB4DA15C`
- Eeschema window title still began with `*`, so GUI state remained modified/unsaved.
