# ESP32_CSI_WIFI_NODE Schematic Safe Repair Commands

Date: 2026-05-06
Working directory: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Read/Inspection Commands

Read required startup, audit, repair plan, project memory, project issue, and visual workflow files with `Get-Content`.

Located project files:

```powershell
Get-ChildItem -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad' -Filter '*.kicad*' | Select-Object FullName,LastWriteTime,Length
```

## Backup

```powershell
$timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$backup = "99_BACKUPS\pre_codex_edits\${timestamp}_ESP32_CSI_WIFI_NODE_schematic_safe_repair"
New-Item -ItemType Directory -Path $backup -Force
Copy-Item -LiteralPath '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' -Destination $backup
Copy-Item -LiteralPath '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' -Destination $backup
Copy-Item -LiteralPath '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\visual_blocks.json' -Destination $backup
```

Backup path: `99_BACKUPS\pre_codex_edits\20260506_152549_ESP32_CSI_WIFI_NODE_schematic_safe_repair`

## Edits

Applied safe schematic display/status cleanup to:

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\visual_blocks.json`

The first write attempt failed because this PowerShell host does not support `Set-Content -Encoding utf8NoBOM`. The file was then written with `.NET` UTF-8 no-BOM encoding.

## Validation Commands

```powershell
python -m json.tool '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\visual_blocks.json'
```

Result: `visual_blocks.json valid`.

```powershell
python - <<parser summary omitted>>
```

Result: schematic parsed successfully; 79 symbols, 43 physical symbols, 43 blank physical footprints, 43 physical datasheet placeholders, `U1` has `Verification_Status`.

## ERC

```powershell
kicad-cli sch erc --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_SAFE_REPAIR_ERC.rpt' --format report --severity-all '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Result: `Found 0 violations`.

## Schematic Checkers

```powershell
python '03_TOOLS\scripts\kicad_schematic_checks\check_schematic_annotation.py' --schematic '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_SAFE_REPAIR_ANNOTATION_CHECK.md' --json-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_SAFE_REPAIR_ANNOTATION_CHECK.json' --no-fail
python '03_TOOLS\scripts\kicad_schematic_checks\check_schematic_completeness.py' --schematic '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' --project-root '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_SAFE_REPAIR_COMPLETENESS_CHECK.md' --json-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_SAFE_REPAIR_COMPLETENESS_CHECK.json' --no-fail
python '03_TOOLS\scripts\kicad_schematic_checks\check_bom_lock_alignment.py' --schematic '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_SAFE_REPAIR_BOM_LOCK_ALIGNMENT_CHECK.md' --json-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_SAFE_REPAIR_BOM_LOCK_ALIGNMENT_CHECK.json' --no-fail
python '03_TOOLS\scripts\kicad_schematic_checks\check_needs_review_markers.py' --schematic '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_SAFE_REPAIR_NEEDS_REVIEW_MARKER_CHECK.md' --json-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_SAFE_REPAIR_NEEDS_REVIEW_MARKER_CHECK.json' --no-fail
```

Results:

- Annotation: `FAIL`, 43 blank-footprint failures, 0 warnings.
- Completeness: `WARN`, BOM lock missing.
- BOM lock alignment: `FAIL`, BOM lock input missing.
- NEEDS_REVIEW marker check: `FAIL`, 26 unresolved marker failures and 1 warning.

## Visual Export

```powershell
kicad-cli sch export svg --black-and-white --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\full_page' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
kicad-cli sch export pdf --black-and-white --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\full_page\ESP32_CSI_WIFI_NODE.pdf' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Result: SVG and PDF were generated. The PDF command also emitted a KiCad project-lock parse warning, but the project file was checked afterward and is not empty.

## Close-Up Visual Generation

```powershell
python '03_TOOLS\scripts\visual\generate_schematic_closeups.py' --source-svg '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\full_page\ESP32_CSI_WIFI_NODE.svg' --config '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\visual_blocks.json' --crops-dir '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\crops' --review-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\CLOSE_UP_REVIEW.md' --json-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\CLOSE_UP_REVIEW.json' --full-png-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\full_page\ESP32_CSI_WIFI_NODE.png' --no-fail
```

Result: `PASS`; 13 crops generated, 0 visible unannotated references, 0 visible footprint/library-field risks.

## Design File Boundaries

Edited: `.kicad_sch` only.

Not edited: `.kicad_pcb`, `.kicad_pro`, symbol libraries, footprint libraries, manufacturing outputs.

## Index And Closeout Commands

```powershell
python '03_TOOLS\scripts\indexing\build_memory_index.py' --repo-root .
python '03_TOOLS\scripts\indexing\build_history_index.py' --repo-root .
python '03_TOOLS\scripts\ai_quality\build_ai_quality_index.py' --repo-root .
python '03_TOOLS\scripts\indexing\build_known_problems.py' --repo-root .
python '03_TOOLS\scripts\indexing\build_repo_index.py' --repo-root .
```

Result: generated indexes were rebuilt.

## Final Validation Commands

```powershell
Get-Item '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | Select-Object FullName,Length,LastWriteTime
Get-Content '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_SAFE_REPAIR_ERC.rpt'
Get-Item '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_VERIFICATION_REPORT.md','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\VISUAL_CHECK_REPORT.md','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\CLOSE_UP_REVIEW.md','02_HISTORY\sessions\ESP32_CSI_WIFI_NODE_SCHEMATIC_SAFE_REPAIR_SESSION.md','02_HISTORY\command_logs\ESP32_CSI_WIFI_NODE_SCHEMATIC_SAFE_REPAIR_COMMANDS.md' | Select-Object FullName,Length
```

Result: required reports/logs exist. ERC report confirms 0 errors and 0 warnings.
