# ESP32_CSI_WIFI_NODE Schematic Audit-Only Commands

Date: 2026-05-06
Working directory: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Commands Run

### Startup and file inspection

Read required startup, workflow, checklist, and project memory/history files with `Get-Content`.

### Tool help and version checks

```powershell
python 03_TOOLS\scripts\kicad_schematic_checks\check_schematic_annotation.py --help
python 03_TOOLS\scripts\kicad_schematic_checks\check_schematic_completeness.py --help
python 03_TOOLS\scripts\kicad_schematic_checks\check_bom_lock_alignment.py --help
python 03_TOOLS\scripts\kicad_schematic_checks\check_needs_review_markers.py --help
kicad-cli version
kicad-cli sch erc --help
kicad-cli sch export svg --help
kicad-cli sch export pdf --help
```

Result: `kicad-cli` version `9.0.7`.

### Annotation check

```powershell
python 03_TOOLS\scripts\kicad_schematic_checks\check_schematic_annotation.py --schematic 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_ANNOTATION_CHECK.md --json-output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_ANNOTATION_CHECK.json --no-fail
```

Result: `FAIL`; 158 pass, 43 warn, 44 fail.

### Completeness check

```powershell
python 03_TOOLS\scripts\kicad_schematic_checks\check_schematic_completeness.py --schematic 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch --project-root 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_COMPLETENESS_CHECK.md --json-output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_COMPLETENESS_CHECK.json --no-fail
```

Result: `WARN`; required blocks present, no BOM lock provided.

### BOM lock alignment check

```powershell
python 03_TOOLS\scripts\kicad_schematic_checks\check_bom_lock_alignment.py --schematic 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_BOM_LOCK_ALIGNMENT_CHECK.md --json-output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_BOM_LOCK_ALIGNMENT_CHECK.json --no-fail
```

Result: `FAIL`; BOM lock path required.

### NEEDS_REVIEW marker check

```powershell
python 03_TOOLS\scripts\kicad_schematic_checks\check_needs_review_markers.py --schematic 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_NEEDS_REVIEW_MARKER_CHECK.md --json-output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_NEEDS_REVIEW_MARKER_CHECK.json --no-fail
```

Result: `FAIL`; 26 fail, 1 warn.

### ERC

```powershell
kicad-cli sch erc --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_ERC.rpt --format report --severity-all 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch
```

Result: `Found 0 violations`; report summary `0 Errors 0 Warnings`.

### Schematic visual export

```powershell
kicad-cli sch export svg --black-and-white --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_audit_only\full_page 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch
kicad-cli sch export pdf --black-and-white --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_audit_only\full_page\ESP32_CSI_WIFI_NODE.pdf 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch
```

Result: SVG and PDF full-page exports created.

### Close-up crop generation

```powershell
python 03_TOOLS\scripts\visual\generate_schematic_closeups.py --source-svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_audit_only\full_page\ESP32_CSI_WIFI_NODE.svg --config 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\visual_blocks.json --crops-dir 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_audit_only\crops --review-output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_CLOSE_UP_REVIEW.md --json-output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_audit_only\SCHEMATIC_AUDIT_ONLY_CLOSE_UP_REVIEW.json --full-png-output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_audit_only\full_page\ESP32_CSI_WIFI_NODE.png --no-fail
```

Result: `FAIL`; 13 SVG crops and 13 PNG crops generated.

### Evidence summarization

Ran read-only Python snippets to parse generated JSON reports, schematic symbol instances, labels, and SVG text positions. These snippets wrote no KiCad files.

### Git status check

```powershell
git status --short
```

Result: failed because the current folder is not a Git repository: `fatal: not a git repository (or any of the parent directories): .git`.

### Closeout validation

```powershell
Get-ChildItem -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad' -Filter '*.kicad*' | Select-Object Name,LastWriteTime,Length
Get-Item '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_REPORT.md','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_REPAIR_PLAN.md','02_HISTORY\sessions\ESP32_CSI_WIFI_NODE_SCHEMATIC_AUDIT_ONLY_SESSION.md','02_HISTORY\command_logs\ESP32_CSI_WIFI_NODE_SCHEMATIC_AUDIT_ONLY_COMMANDS.md' | Select-Object FullName,Length
Get-Content -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_AUDIT_ONLY_ERC.rpt'
```

Result: required report/log files exist; KiCad project/schematic last-write timestamps remain earlier than this audit session.

## Design File Edits

None.
