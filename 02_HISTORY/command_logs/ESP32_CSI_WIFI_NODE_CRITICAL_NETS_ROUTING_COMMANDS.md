# ESP32_CSI_WIFI_NODE Critical Nets Routing Commands

Date: 2026-05-03

Status: `COMPLETED_BLOCKED`

## Scope

Commands and file inspections for the gated critical-net routing request.

## Commands Run

| Command | Purpose | Result |
|---|---|---|
| `Get-Content AGENTS.md` | Startup rules. | Read. |
| `Get-Content README_GPT.md` | Repo context. | Read. |
| `Get-Content "FOR CHAT GPT.MD"` | Handoff context. | Read. |
| `Get-Content 00_CODEX_START\START_HERE.md` | Startup flow. | Read. |
| `Get-Content 00_CODEX_START\SESSION_START_CHECKLIST.md` | Startup checklist. | Read. |
| `Get-Content 00_CODEX_START\STRUCTURE_STANDARD.md` | Structure rules. | Read. |
| `Get-Content 00_CODEX_START\FOLDER_ROUTING_RULES.md` | File routing rules. | Read. |
| `Get-Content 00_CODEX_START\CURRENT_KNOWN_PROBLEMS.md` | Known blockers. | Read. |
| `Get-Content 00_CODEX_START\MEMORY_INDEX.md` | Memory rules. | Read. |
| `Get-Content 00_CODEX_START\HISTORY_INDEX.md` | History rules. | Read. |
| `Get-Content 00_CODEX_START\CURRENT_PROJECT.md` | Active project. | Read. |
| `Get-Content 00_CODEX_START\CONTROL_PLANES.md` | Tool selection rules. | Read. |
| `Get-Content 00_CODEX_START\SESSION_CLOSEOUT_CHECKLIST.md` | Closeout requirements. | Read. |
| `Get-Content 00_CODEX_START\AI_RESPONSE_QUALITY_GATE.md` | AI quality gate. | Read. |
| `Get-Content 00_CODEX_START\AI_EVIDENCE_REQUIREMENTS.md` | Evidence rules. | Read. |
| `Get-Content 00_CODEX_START\AI_TRUTHFULNESS_SCORING.md` | Score rules. | Read. |
| `Get-Content reports\PCB_ROUTING_PLAN.md` | Routing readiness. | Read; final result `ROUTING_PLAN_BLOCKED`. |
| `Get-Content 09_ACCURACY_ENGINE\pcb_rules\USB_LAYOUT_RULES.md` | USB layout rules. | Read. |
| `Get-Content 09_ACCURACY_ENGINE\pcb_rules\POWER_LAYOUT_RULES.md` | Power layout rules. | Read. |
| `Get-Content 09_ACCURACY_ENGINE\pcb_rules\RF_LAYOUT_RULES.md` | RF layout rules. | Read. |
| `Get-Content 09_ACCURACY_ENGINE\workflows\SCHEMATIC_TO_PCB_GATE_WORKFLOW.md` | PCB work gate. | Read. |
| `Get-Content 09_ACCURACY_ENGINE\verification_rules\SCHEMATIC_TO_PCB_BLOCKERS.md` | Blocker rules. | Read. |
| `Get-Content 09_ACCURACY_ENGINE\verification_rules\NEEDS_REVIEW_BLOCKER_RULES.md` | Review blocker rules. | Read. |
| `Get-Content reports\SCHEMATIC_TO_PCB_GATE_STATUS.md` | Gate status. | Read; gate result `FAIL`. |
| `Get-Content reports\PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md` | Placement status. | Read; final result `PLACEMENT_ORIENTATION_FAIL`. |
| `Get-Content reports\COPPER_ZONE_STRATEGY_REPORT.md` | Zone status. | Read; final result `ZONE_SETUP_FAIL`. |
| `Get-Content reports\THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md` | Via strategy status. | Read; final result `HOLE_PAD_VIA_FAIL`. |
| `Get-ChildItem kicad` | Check active project KiCad files. | Found `.kicad_pro`, `.kicad_sch`, and `fp-info-cache`; no `.kicad_pcb`. |
| `Copy-Item kicad -> 99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_CRITICAL_ROUTING_BLOCKED_20260503_090215` | Create conservative pre-report backup. | Completed. |

## Validation

| Command | Purpose | Result |
|---|---|---|
| `python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .` | Rebuild memory indexes. | Completed. |
| `python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .` | Rebuild history indexes. | Completed. |
| `python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .` | Rebuild known-problems summary. | Completed. |
| `python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .` | Rebuild AI-quality indexes. | Completed. |
| `python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .` | Rebuild repo index. | Completed. |
| `Select-String reports\PCB_CRITICAL_NETS_ROUTING_REPORT.md ...` | Confirm blocked/fail status and DRC-not-run text. | Found `CRITICAL_ROUTING_FAIL`, `NOT_RUN_NO_PCB`, `No traces were routed`, and `DRC result`. |
| `Select-String _verification\pcb_visual\CRITICAL_NETS_CLOSEUP_REVIEW.md ...` | Confirm close-up review blocked status. | Found `NOT_RUN_NO_PCB` and `No close-up crops were generated`. |
| `Test-Path kicad\ESP32_CSI_WIFI_NODE.kicad_pcb` | Confirm PCB file absence. | Returned `False`. |
| `Test-Path backup\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` | Confirm backup was created. | Returned `True`. |
| `Get-ChildItem kicad` | Confirm KiCad source file set. | Found `.kicad_pro`, `.kicad_sch`, and `fp-info-cache`; no `.kicad_pcb`. |
| `Select-String ... secret patterns` | Check new records for obvious secret patterns. | No matches. |
| `Select-String CURRENT_KNOWN_PROBLEMS.md PCB_CRITICAL_NETS_ROUTING` | Confirm known-problems index includes new blocker. | Found new issue, quality-gate, and uncertainty records. |

## KiCad Design File Changes

None intentionally made. No `.kicad_pcb` exists and no schematic/PCB/source-library/manufacturing files were edited.

## Final Result

`CRITICAL_ROUTING_FAIL`
