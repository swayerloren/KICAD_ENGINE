# ESP32_CSI_WIFI_NODE Layout Sandbox Variants Commands

Date: `2026-05-07`

## Commands Run

1. Read-first and startup/project-context inspection:

```powershell
Get-Content AGENTS.md -TotalCount 260
Get-Content README_GPT.md -TotalCount 120
Get-Content "FOR CHAT GPT.MD" -TotalCount 120
Get-Content 34_PCB_LAYOUT_SANDBOX\PCB_VARIANT_WORKFLOW.md -TotalCount 260
Get-Content 34_PCB_LAYOUT_SANDBOX\VARIANT_SCORING_RULES.md -TotalCount 260
Get-Content 34_PCB_LAYOUT_SANDBOX\ESP32_STYLE_BOARD_PLACEMENT_RULES.md -TotalCount 260
Get-Content 10_KNOWLEDGE_BASE\design_patterns\ESP32_DEV_BOARD_LAYOUT_PATTERN.md -TotalCount 220
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_TO_PCB_GATE_STATUS.md -TotalCount 260
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FOOTPRINT_PACKAGE_GATE_REPORT.md -TotalCount 260
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_SYNC_STATUS.md -TotalCount 260
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_PROJECT_STATE.md -TotalCount 220
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_BLOCKERS.md -TotalCount 220
rg -n "J1|J2|U1|U2|U3|F1|Q1|D3|R8|R9|button|LED|TP|mounting hole|Edge.Cuts|antenna|USB-C|barrel jack" 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

2. Prompt-counter maintenance gate:

```powershell
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
```

Result:

- Prompt counter incremented.
- Maintenance due: `NO`.

3. Baseline KiCad no-edit hash capture:

```powershell
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
```

4. Sandbox planning validation:

```powershell
New-Item -ItemType Directory -Force 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox
python 34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/VARIANT_A_COMPACT_DEV_BOARD_STYLE.md --format json
python 34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/VARIANT_B_CONNECTOR_MECHANICAL_OPTIMIZED.md --format json
python 34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/VARIANT_C_ROUTING_POWER_RF_OPTIMIZED.md --format json
python 34_PCB_LAYOUT_SANDBOX/scripts/compare_layout_variants.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/VARIANT_A_COMPACT_DEV_BOARD_STYLE.md 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/VARIANT_B_CONNECTOR_MECHANICAL_OPTIMIZED.md 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/VARIANT_C_ROUTING_POWER_RF_OPTIMIZED.md --format json
```

Result:

- All three variants scored successfully.
- `VARIANT_C` ranked highest.
- Real PCB edit readiness remained `false`.

5. Closeout and final checks:

```powershell
python 03_TOOLS/scripts/ai_quality/create_ai_self_review.py --repo-root . --scope global --title "ESP32_CSI_WIFI_NODE Layout Sandbox Variants Self Review" --summary "Created three project-local PCB layout sandbox variants, scored them, and recorded a provisional front-runner without editing the real KiCad PCB." --details "The task stayed in planning, sandbox, project-memory, and history scope. The variant docs capture board-shape assumptions, connector placement, power and USB path projections, RF connector clearance for the WROOM-1U module, buttons, LEDs, test pads, mounting holes, via strategy, and risks. The selected variant is explicitly marked as NEEDS_HUMAN_REVIEW and not placement-approved." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Created layout_sandbox/VARIANT_A_COMPACT_DEV_BOARD_STYLE.md, VARIANT_B_CONNECTOR_MECHANICAL_OPTIMIZED.md, VARIANT_C_ROUTING_POWER_RF_OPTIMIZED.md, VARIANT_COMPARISON_SCORECARD.md, and SELECTED_LAYOUT_PLAN.md; ran score_layout_variant.py on all three files and compare_layout_variants.py on the full set; updated CURRENT_PROJECT_STATE.md, CURRENT_BLOCKERS.md, and FOR CHAT GPT.MD; final KiCad hash recheck confirmed no design-file changes." --issue "The selected sandbox front-runner still needs LJ review, exact dimension confirmation, and unresolved upstream gate resolution before any real PCB placement work."
python 03_TOOLS/scripts/ai_quality/create_response_scorecard.py --repo-root . --scope global --title "ESP32_CSI_WIFI_NODE Layout Sandbox Variants AI Response Scorecard" --summary "The project-local sandbox variants were created cleanly, scored with the repo's comparison scripts, and documented without editing KiCad design files." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Direct file reads, compare script outputs, project-memory updates, and pre/post KiCad file hashes." --issue "The selected plan is still blocked for execution because LJ review and upstream project gates remain unresolved." --overall-score 98 --evidence-support 20 --kicad-correctness 20 --datasheet-accuracy 15 --safety-compliance 15 --memory-routing 10 --uncertainty-disclosure 8 --usefulness 10
python 03_TOOLS/scripts/ai_quality/create_claim_evidence_matrix.py --repo-root . --scope global --title "ESP32_CSI_WIFI_NODE Layout Sandbox Variants Claim Evidence Matrix" --summary "Three project-local layout sandbox variants now exist for ESP32_CSI_WIFI_NODE, and Variant C is the highest-scoring non-failed sandbox front-runner." --details "The patch created the three requested variant plans plus a comparison scorecard and selected-plan document. The scoring scripts reported Variant C as the highest-scoring non-failed option with status NEEDS_HUMAN_REVIEW and ready_for_real_pcb_edit false." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_COMMAND --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/*.md files; score_layout_variant.py JSON outputs for A/B/C; compare_layout_variants.py JSON output selecting VARIANT_C; project memory updates and final KiCad hash recheck." --issue "Variant C is only a provisional sandbox front-runner and is not a placement approval."
python 03_TOOLS/scripts/ai_quality/create_uncertainty_log.py --repo-root . --scope global --title "ESP32_CSI_WIFI_NODE Layout Sandbox Variants Uncertainty Log" --summary "The sandbox variants are documented and scored, but exact board dimensions, exact connector/package lock, and LJ mechanical approval remain unresolved." --details "The main uncertainty is mechanical closure rather than document completeness. The project uses an ESP32-S3-WROOM-1U external-antenna module, so the RF planning is based on reserved RF connector and pigtail clearance rather than a fully proven final enclosure path. Board dimensions are still assumptions in all three variants, which keeps every variant in NEEDS_HUMAN_REVIEW even though Variant C scores highest." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label LOW_RISK --gate-result PASS_WITH_WARNINGS --human-review-required NO --evidence "SCHEMATIC_TO_PCB_GATE_STATUS.md, FOOTPRINT_PACKAGE_GATE_REPORT.md, PCB_SYNC_STATUS.md, current project memory, the three variant docs, and compare_layout_variants.py output." --issue "LJ must still approve the selected plan before any real PCB placement or edit work."
python 03_TOOLS/scripts/ai_quality/create_hallucination_risk_log.py --repo-root . --scope global --title "ESP32_CSI_WIFI_NODE Layout Sandbox Variants Hallucination Risk Log" --summary "This task had low hallucination risk because it stayed inside local project reports, sandbox rules, and direct script-validated comparison outputs." --details "The main risk was overcommitting to a board shape or antenna interpretation without respecting the exact project data. That was mitigated by reading the project gate reports and capturing that U2 is the ESP32-S3-WROOM-1U external-antenna module, so the RF planning is framed as connector/pigtail clearance rather than a generic PCB-antenna rule. A second risk was overstating readiness; that was mitigated by preserving NEEDS_HUMAN_REVIEW status and ready_for_real_pcb_edit false in the comparison docs." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_COMMAND --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Local report reads, sandbox variant markdown files, compare script output, project-memory updates, and final KiCad hash recheck." --issue "No unresolved hallucination blocker was identified."
python 03_TOOLS/scripts/memory_maintenance/rebuild_history_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/memory_maintenance/rebuild_memory_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_known_problems.py --repo-root .
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
```

Result:

- AI-quality records and indexes rebuilt.
- Final KiCad design-file hashes matched the baseline.
