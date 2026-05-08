# ESP32_CSI_WIFI_NODE Human-Readable Schematic Repair Commands

Date: 2026-05-06

## Commands Run

Startup/context reads:

```powershell
Get-Content AGENTS.md
Get-Content README_GPT.md
Get-Content 'FOR CHAT GPT.MD'
Get-Content '00_CODEX_START/START_HERE.md'
Get-Content '09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md'
Get-Content '09_ACCURACY_ENGINE/verification_rules/VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md'
Get-Content '09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md'
```

Backup:

```powershell
Copy-Item '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch' '99_BACKUPS/pre_codex_edits/20260506_170404_ESP32_CSI_WIFI_NODE_human_readable_schematic_relayout/'
Copy-Item '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro' '99_BACKUPS/pre_codex_edits/20260506_170404_ESP32_CSI_WIFI_NODE_human_readable_schematic_relayout/'
```

ERC:

```powershell
kicad-cli sch erc '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch' --output '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_HUMAN_READABILITY_REPAIR_ERC.rpt'
```

Schematic checks:

```powershell
python '03_TOOLS/scripts/kicad_schematic_checks/check_schematic_annotation.py' --schematic '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch' --output '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_HUMAN_READABILITY_REPAIR_ANNOTATION_CHECK.md'
python '03_TOOLS/scripts/kicad_schematic_checks/check_schematic_completeness.py' --project-root '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE' --schematic '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch' --output '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_HUMAN_READABILITY_REPAIR_COMPLETENESS_CHECK.md'
python '03_TOOLS/scripts/kicad_schematic_checks/check_bom_lock_alignment.py' --schematic '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch' --bom-lock '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/PRE_SCHEMATIC_BOM_LOCK.md' --output '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_HUMAN_READABILITY_REPAIR_BOM_LOCK_ALIGNMENT_CHECK.md' --no-fail
python '03_TOOLS/scripts/kicad_schematic_checks/check_needs_review_markers.py' --schematic '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch' --bom-lock '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/PRE_SCHEMATIC_BOM_LOCK.md' --output '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_HUMAN_READABILITY_REPAIR_NEEDS_REVIEW_CHECK.md' --no-fail
```

Visual export/crops:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '03_TOOLS/kicad/run_schematic_visual_check.ps1' -ProjectRoot '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE' -SchematicPath '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch' -NoFailOnFindings
```

## Notable Failed Attempt

An initial broad regex relayout produced 33 ERC violations. The schematic was restored from the pre-edit backup before continuing with narrower exact edits. The final ERC result after the later repair pass is 0 violations.

## AI Quality Closeout Commands

```powershell
python '03_TOOLS/scripts/memory_history/create_failed_attempt.py' --repo-root . --scope project --project-name ESP32_CSI_WIFI_NODE --project-path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE' --title 'Failed broad regex schematic relayout attempt' ...
python '03_TOOLS/scripts/ai_quality/create_ai_self_review.py' --repo-root . --scope project --project-name ESP32_CSI_WIFI_NODE --project-path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE' --title 'Human-readable schematic repair self-review' ...
python '03_TOOLS/scripts/ai_quality/create_response_scorecard.py' --repo-root . --scope project --project-name ESP32_CSI_WIFI_NODE --project-path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE' --title 'Human-readable schematic repair response scorecard' ...
python '03_TOOLS/scripts/ai_quality/create_claim_evidence_matrix.py' --repo-root . --scope project --project-name ESP32_CSI_WIFI_NODE --project-path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE' --title 'Human-readable schematic repair claim evidence matrix' ...
python '03_TOOLS/scripts/ai_quality/create_uncertainty_log.py' --repo-root . --scope project --project-name ESP32_CSI_WIFI_NODE --project-path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE' --title 'Human-readable schematic repair uncertainty log' ...
python '03_TOOLS/scripts/ai_quality/create_hallucination_risk_log.py' --repo-root . --scope project --project-name ESP32_CSI_WIFI_NODE --project-path '04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE' --title 'Human-readable visual pass risk log' ...
python '03_TOOLS/scripts/indexing/build_memory_index.py' --repo-root .
python '03_TOOLS/scripts/indexing/build_history_index.py' --repo-root .
python '03_TOOLS/scripts/ai_quality/build_ai_quality_index.py' --repo-root .
python '03_TOOLS/scripts/indexing/build_known_problems.py' --repo-root .
```
