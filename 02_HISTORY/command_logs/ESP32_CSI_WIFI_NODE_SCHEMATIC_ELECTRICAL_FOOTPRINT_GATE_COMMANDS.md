# ESP32_CSI_WIFI_NODE Schematic Electrical Footprint Gate Commands

Date: 2026-05-06  
Working directory: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Read And Inspect Commands

```powershell
Get-Content -LiteralPath '09_ACCURACY_ENGINE\verification_rules\FOOTPRINT_DATASHEET_MATCH_RULES.md'
Get-Content -LiteralPath '09_ACCURACY_ENGINE\workflows\SCHEMATIC_TO_PCB_GATE_WORKFLOW.md'
Get-ChildItem -LiteralPath '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE' -Force
Get-ChildItem -LiteralPath '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports' -Force
```

Checked requested optional project files:

```powershell
Test-Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\PRE_SCHEMATIC_BOM_LOCK.md'
Test-Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\SCHEMATIC_READY_PARTS_LIST.md'
Test-Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\NEEDS_REVIEW_BEFORE_SCHEMATIC.md'
```

Result: all three requested optional files were missing.

## KiCad / ERC

```powershell
Get-Command kicad-cli -ErrorAction SilentlyContinue
kicad-cli sch erc --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_ERC.rpt' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Result: ERC passed with 0 errors and 0 warnings.

## Schematic Parse

```powershell
python - <<equivalent inline script using 03_TOOLS\scripts\kicad_schematic_checks\schematic_check_common.py
```

Output:

- `reports/SCHEMATIC_ELECTRICAL_FOOTPRINT_GATE_PARSE.json`
- 43 physical schematic symbols.
- 43 blank footprints.
- 43 placeholder datasheet/source fields.
- 0 duplicate physical references.

## Checker Commands

The first checker invocation used unsupported option names (`--report-md` and `--report-json`) and failed. The commands were rerun with the actual local script arguments.

Corrected commands:

```powershell
python '03_TOOLS\scripts\kicad_schematic_checks\check_schematic_annotation.py' --schematic '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_ANNOTATION_CHECK.md' --json-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_ANNOTATION_CHECK.json' --no-fail
python '03_TOOLS\scripts\kicad_schematic_checks\check_schematic_completeness.py' --schematic '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' --project-root '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_COMPLETENESS_CHECK.md' --json-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_COMPLETENESS_CHECK.json' --no-fail
python '03_TOOLS\scripts\kicad_schematic_checks\check_bom_lock_alignment.py' --schematic '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_BOM_LOCK_ALIGNMENT_CHECK.md' --json-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_BOM_LOCK_ALIGNMENT_CHECK.json' --no-fail
python '03_TOOLS\scripts\kicad_schematic_checks\check_needs_review_markers.py' --schematic '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_NEEDS_REVIEW_MARKER_CHECK.md' --json-output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_NEEDS_REVIEW_MARKER_CHECK.json' --no-fail
```

Results:

- Annotation checker: `FAIL`, 43 fail, 158 pass, 0 warn.
- Completeness checker: `WARN`, 10 pass, 1 warn.
- BOM lock alignment checker: `FAIL`, 1 fail.
- NEEDS_REVIEW marker checker: `FAIL`, 26 fail, 1 warn.

## AI Quality Commands

Created project-scoped AI self-review, scorecard, claim/evidence matrix, uncertainty log, hallucination-risk log, and quality-gate failure using:

```powershell
python '03_TOOLS\scripts\ai_quality\create_ai_self_review.py' ...
python '03_TOOLS\scripts\ai_quality\create_response_scorecard.py' ...
python '03_TOOLS\scripts\ai_quality\create_claim_evidence_matrix.py' ...
python '03_TOOLS\scripts\ai_quality\create_uncertainty_log.py' ...
python '03_TOOLS\scripts\ai_quality\create_hallucination_risk_log.py' ...
python '03_TOOLS\scripts\ai_quality\create_quality_gate_failure.py' ...
```

## Index Rebuild Commands

```powershell
python '03_TOOLS\scripts\indexing\build_memory_index.py' --repo-root .
python '03_TOOLS\scripts\indexing\build_history_index.py' --repo-root .
python '03_TOOLS\scripts\ai_quality\build_ai_quality_index.py' --repo-root .
python '03_TOOLS\scripts\indexing\build_known_problems.py' --repo-root .
```

Result: indexes and `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md` rebuilt without command errors.

## Final Inspection Commands

```powershell
git status --short
Get-Content '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_TO_PCB_GATE_STATUS.md' -TotalCount 80
Get-ChildItem '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\history\ai_self_reviews','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\history\ai_scorecards','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\history\claim_evidence_matrices','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\history\uncertainty_logs','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\history\hallucination_risk_logs','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\history\quality_gate_failures'
Get-Item '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro'
Test-Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb'
Select-String -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_REPORT.md','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FOOTPRINT_PACKAGE_GATE_REPORT.md','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_TO_PCB_GATE_STATUS.md' -Pattern 'Final classification|Gate result|PCB update allowed|Footprint/package gate result|Electrical gate result'
```

Result:

- `git status --short` failed because this checkout does not expose `.git` metadata to the current shell context.
- Gate status file inspection confirmed `Gate result: FAIL` and `PCB update allowed: NO`.
- Project AI quality files were present under active project history folders.
- `.kicad_sch` and `.kicad_pro` timestamps were inspected; no `.kicad_pcb` file is present.

## Manual Report/Memory Edits

Report, memory, issue-log, session-log, command-log, failed-attempt, and handoff files were edited with `apply_patch`.

## Design File Safety

No `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbol library, footprint library, or manufacturing output files were edited.
