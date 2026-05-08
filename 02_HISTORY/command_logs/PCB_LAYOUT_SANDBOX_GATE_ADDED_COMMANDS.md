# PCB Layout Sandbox Gate Added Commands

Date: `2026-05-07`

## Commands Run

1. Read-first and startup-context inspection:

```powershell
Get-Content AGENTS.md
Get-Content README_GPT.md
Get-Content "FOR CHAT GPT.MD"
Get-Content 00_CODEX_START\START_HERE.md
Get-Content 09_ACCURACY_ENGINE\workflows\SCHEMATIC_TO_PCB_GATE_WORKFLOW.md
Get-Content 09_ACCURACY_ENGINE\workflows\CREATE_PCB_WORKFLOW.md
Get-Content 09_ACCURACY_ENGINE\checklists\FULL_PIPELINE_GATE_CHECKLIST.md
Get-Content 34_PCB_LAYOUT_SANDBOX\PCB_VARIANT_WORKFLOW.md
```

2. Active-project and prompt-counter checks:

```powershell
Get-Content 00_CODEX_START\CURRENT_PROJECT.md
Get-Content 00_CODEX_START\PROMPT_COUNTER_RULES.md
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
```

Result:

- Prompt counter incremented from `0` to `1`.
- Maintenance due: `NO`.

3. Project evidence inspection:

```powershell
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox\SELECTED_LAYOUT_PLAN.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox\VARIANT_COMPARISON_SCORECARD.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_TO_PCB_GATE_STATUS.md
Get-ChildItem 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox | Select-Object -ExpandProperty Name
rg -n "KICAD_NATIVE_ANNOTATION|GUI ERC|Violations \\(0\\)|annotation" 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports 33_KICAD_GUI_AUTOMATION
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FOOTPRINT_PACKAGE_GATE_REPORT.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FOOTPRINT_ASSIGNMENT_PLAN.md
Get-ChildItem 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports -Filter 'KICAD_GUI_NATIVE_ANNOTATION*' | Select-Object -ExpandProperty Name
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_BLOCKERS.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_PROJECT_STATE.md
```

4. No-design-file hash checks:

```powershell
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
Test-Path 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_LAYOUT_SANDBOX_GATE_STATUS.md
```

5. Validation:

```powershell
rg -n "PCB_LAYOUT_SANDBOX_GATE_STATUS|LJ approved|both .*PASS|selected layout plan" AGENTS.md README_GPT.md "FOR CHAT GPT.MD" 00_CODEX_START/START_HERE.md 09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md 09_ACCURACY_ENGINE/workflows/CREATE_PCB_WORKFLOW.md 09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md 01_MEMORY/DESIGN_RULES_MEMORY.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_LAYOUT_SANDBOX_GATE_STATUS.md
```

6. AI-quality closeout and index rebuild:

```powershell
python 03_TOOLS/scripts/ai_quality/create_ai_self_review.py --repo-root . --scope global --title "PCB Layout Sandbox Gate Added Self Review" --summary "Added a mandatory sandbox-and-LJ-approval gate before PCB update from schematic or real PCB placement, without touching KiCad design files." --details "The task stayed in startup-rule, workflow-gate, checklist, handoff, project-report, and project-memory scope. The new logic requires both SCHEMATIC_TO_PCB_GATE_STATUS.md and PCB_LAYOUT_SANDBOX_GATE_STATUS.md to be exact PASS before real PCB update from schematic or real placement may begin. The ESP32_CSI_WIFI_NODE project-local sandbox gate was created and correctly records the current blocked state." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Updated AGENTS.md, README_GPT.md, FOR CHAT GPT.MD, 00_CODEX_START/START_HERE.md, 09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md, CREATE_PCB_WORKFLOW.md, FULL_PIPELINE_GATE_CHECKLIST.md, 01_MEMORY/DESIGN_RULES_MEMORY.md, and project memory files; created 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md; readback confirmed the new gate references; final KiCad hash recheck matched the baseline." --issue "LJ approval and footprint assignment remain open blockers for ESP32_CSI_WIFI_NODE."
python 03_TOOLS/scripts/ai_quality/create_response_scorecard.py --repo-root . --scope global --title "PCB Layout Sandbox Gate Added AI Response Scorecard" --summary "Startup and PCB workflow rules now enforce a second exact-PASS gate for sandbox completion and LJ approval before PCB update or placement." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Direct file reads, patch results, rg validation, project gate report readback, and pre/post KiCad hash checks." --issue "The active project remains blocked until LJ approval and footprint assignment are resolved." --overall-score 97 --evidence-support 19 --kicad-correctness 20 --datasheet-accuracy 15 --safety-compliance 15 --memory-routing 10 --uncertainty-disclosure 8 --usefulness 10
python 03_TOOLS/scripts/ai_quality/create_claim_evidence_matrix.py --repo-root . --scope global --title "PCB Layout Sandbox Gate Added Claim Evidence Matrix" --summary "KiCad Engine now blocks real PCB update from schematic and real placement until the sandbox workflow is complete and LJ approved the selected layout plan." --details "The patch updated startup rules, PCB workflows, the full pipeline checklist, durable memory, and handoff context, and created a project-local sandbox gate report for ESP32_CSI_WIFI_NODE." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "AGENTS.md, README_GPT.md, FOR CHAT GPT.MD, 00_CODEX_START/START_HERE.md, 09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md, 09_ACCURACY_ENGINE/workflows/CREATE_PCB_WORKFLOW.md, 09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md, 01_MEMORY/DESIGN_RULES_MEMORY.md, 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md, and project memory updates." --issue "ESP32_CSI_WIFI_NODE still lacks LJ approval and assigned footprints, so the new project-local gate remains blocked."
python 03_TOOLS/scripts/ai_quality/create_uncertainty_log.py --repo-root . --scope global --title "PCB Layout Sandbox Gate Added Uncertainty Log" --summary "The new sandbox gate rules and project-local gate report are implemented, but some older project reports still contain stale or conflicting historical wording." --details "The main uncertainty is historical consistency rather than the new rule itself. The new gate report uses the newest explicit evidence: native GUI annotation success, the footprint package gate, the sandbox scorecard, and the selected layout plan. Older project reports may still contain superseded blocked-state wording, so future work should continue to privilege the newest evidence files and explicit gate reports." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label LOW_RISK --gate-result PASS_WITH_WARNINGS --human-review-required NO --evidence "Readback of current project gate files, layout sandbox files, footprint package gate, native annotation reports, and rg validation of the new startup/workflow references." --issue "Historical project report consistency still needs ongoing maintenance discipline."
python 03_TOOLS/scripts/ai_quality/create_hallucination_risk_log.py --repo-root . --scope global --title "PCB Layout Sandbox Gate Added Hallucination Risk Log" --summary "This task had low hallucination risk because it relied on local workflow files, explicit project reports, and direct readback validation." --details "The main risk was overstating current project readiness. That was controlled by creating a new project-local gate file that explicitly records BLOCKED status and cites the actual evidence files showing missing LJ approval and missing footprint assignment. A second risk was implying KiCad design-file changes; that was controlled by pre/post hash checks on the active project's .kicad_pcb, .kicad_sch, and .kicad_pro files." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_COMMAND --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Local file patches, direct report reads, rg validation, and final KiCad hash recheck." --issue "No unresolved hallucination blocker was identified."
python 03_TOOLS/scripts/memory_maintenance/rebuild_history_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/memory_maintenance/rebuild_memory_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_known_problems.py --repo-root .
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
```

Result:

- AI-quality records created.
- History, memory, repo, AI-quality, and known-problem indexes rebuilt.
- Final KiCad design-file hashes matched the baseline.
