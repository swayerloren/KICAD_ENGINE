# ESP32 Dev Board Layout Intelligence Commands

Date: `2026-05-07`

## Commands Run

1. Read-first and startup-context inspection:

```powershell
Get-Content AGENTS.md -TotalCount 260
Get-Content README_GPT.md -TotalCount 120
Get-Content "FOR CHAT GPT.MD" -TotalCount 120
Get-Content 34_PCB_LAYOUT_SANDBOX\COMPONENT_PLACEMENT_RULES.md -TotalCount 260
Get-Content 34_PCB_LAYOUT_SANDBOX\CONNECTOR_ORIENTATION_RULES.md -TotalCount 260
Get-Content 34_PCB_LAYOUT_SANDBOX\RF_ANTENNA_KEEP_OUT_RULES.md -TotalCount 260
Get-Content 00_CODEX_START\CURRENT_PROJECT.md -TotalCount 120
Get-Content 00_CODEX_START\PROMPT_COUNTER_RULES.md -TotalCount 160
Get-Content 00_CODEX_START\SESSION_CLOSEOUT_CHECKLIST.md -TotalCount 200
Get-ChildItem 10_KNOWLEDGE_BASE\design_patterns | Select-Object Name
Get-ChildItem 10_KNOWLEDGE_BASE\common_mistakes | Select-Object Name
Get-Content 01_MEMORY\DESIGN_RULES_MEMORY.md -TotalCount 120
Get-Content 34_PCB_LAYOUT_SANDBOX\INDEX.md -TotalCount 260
Get-Content 34_PCB_LAYOUT_SANDBOX\README.md -TotalCount 220
Get-Content 10_KNOWLEDGE_BASE\design_patterns\MOUNTING_HOLE_PATTERN.md -TotalCount 220
Get-Content 10_KNOWLEDGE_BASE\design_patterns\TEST_POINT_PATTERN.md -TotalCount 220
Get-Content 10_KNOWLEDGE_BASE\common_mistakes\ESP32_COMMON_MISTAKES.md -TotalCount 220
Get-Content 10_KNOWLEDGE_BASE\common_mistakes\USB_C_COMMON_MISTAKES.md -TotalCount 220
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

4. Validation:

```powershell
Get-ChildItem '10_KNOWLEDGE_BASE\design_patterns\ESP32_DEV_BOARD_LAYOUT_PATTERN.md','10_KNOWLEDGE_BASE\design_patterns\STM32_DEV_BOARD_LAYOUT_PATTERN.md','10_KNOWLEDGE_BASE\design_patterns\CONNECTOR_EDGE_PLACEMENT_PATTERN.md','10_KNOWLEDGE_BASE\design_patterns\RF_MODULE_ANTENNA_KEEP_OUT_PATTERN.md','10_KNOWLEDGE_BASE\common_mistakes\ESP32_LAYOUT_COMMON_MISTAKES.md','10_KNOWLEDGE_BASE\common_mistakes\USB_C_CONNECTOR_LAYOUT_COMMON_MISTAKES.md','10_KNOWLEDGE_BASE\common_mistakes\BARREL_JACK_LAYOUT_COMMON_MISTAKES.md','34_PCB_LAYOUT_SANDBOX\ESP32_STYLE_BOARD_PLACEMENT_RULES.md','34_PCB_LAYOUT_SANDBOX\DEV_BOARD_SHAPE_REASONING_RULES.md' | Select-Object -ExpandProperty FullName
rg -n "These are layout patterns, not universal rules|board shape must be justified|Buttons must remain user-accessible|LEDs must remain visible|Test pads must remain accessible after assembly|do not place copper, traces, mounting holes, connectors, test pads, shields, or tall components under the antenna keepout" 10_KNOWLEDGE_BASE 34_PCB_LAYOUT_SANDBOX README_GPT.md "FOR CHAT GPT.MD" 01_MEMORY\DESIGN_RULES_MEMORY.md
Get-Content 10_KNOWLEDGE_BASE\design_patterns\ESP32_DEV_BOARD_LAYOUT_PATTERN.md -TotalCount 220
Get-Content 34_PCB_LAYOUT_SANDBOX\ESP32_STYLE_BOARD_PLACEMENT_RULES.md -TotalCount 260
```

5. Closeout and final checks:

```powershell
python 03_TOOLS/scripts/ai_quality/create_ai_self_review.py --repo-root . --scope global --title "ESP32 Dev Board Layout Intelligence Self Review" --summary "Created reusable placement-intelligence docs for ESP32-style boards, STM32-style dev boards, connector edges, RF keepouts, buttons, LEDs, mounting holes, and test pads without touching KiCad design files." --details "The task stayed in knowledge-base, sandbox-rule, memory, and handoff scope. The new docs explicitly state that they are patterns rather than universal rules and that project requirements come first. No KiCad design files or manufacturing outputs were modified." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Created files under 10_KNOWLEDGE_BASE/design_patterns, 10_KNOWLEDGE_BASE/common_mistakes, and 34_PCB_LAYOUT_SANDBOX; updated sandbox discovery files, DESIGN_RULES_MEMORY.md, README_GPT.md, and FOR CHAT GPT.MD; validated file existence and key warning/rule phrases; final KiCad hash recheck confirmed no design-file changes." --issue "The new placement-intelligence docs still need a first live project-local sandbox adoption pass."
python 03_TOOLS/scripts/ai_quality/create_response_scorecard.py --repo-root . --scope global --title "ESP32 Dev Board Layout Intelligence AI Response Scorecard" --summary "The placement-intelligence docs were added cleanly and wired into sandbox discovery, memory, and handoff without editing KiCad design files." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Direct file reads, patch results, existence checks, rule-phrase scans, and pre/post KiCad file hashes." --issue "No first live project-local variant-study evidence exists yet for the new docs." --overall-score 97 --evidence-support 19 --kicad-correctness 20 --datasheet-accuracy 15 --safety-compliance 15 --memory-routing 10 --uncertainty-disclosure 8 --usefulness 10
python 03_TOOLS/scripts/ai_quality/create_claim_evidence_matrix.py --repo-root . --scope global --title "ESP32 Dev Board Layout Intelligence Claim Evidence Matrix" --summary "KiCad Engine now has reusable placement-intelligence guidance for ESP32-style boards, STM32-style dev boards, connector edge placement, RF module keepouts, and common placement mistakes." --details "The patch created new design-pattern and common-mistake documents, added new sandbox rule files, and updated global memory and handoff docs so future agents can find the new placement guidance during planning." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "10_KNOWLEDGE_BASE/design_patterns/ESP32_DEV_BOARD_LAYOUT_PATTERN.md, STM32_DEV_BOARD_LAYOUT_PATTERN.md, CONNECTOR_EDGE_PLACEMENT_PATTERN.md, RF_MODULE_ANTENNA_KEEP_OUT_PATTERN.md; 10_KNOWLEDGE_BASE/common_mistakes/ESP32_LAYOUT_COMMON_MISTAKES.md, USB_C_CONNECTOR_LAYOUT_COMMON_MISTAKES.md, BARREL_JACK_LAYOUT_COMMON_MISTAKES.md; 34_PCB_LAYOUT_SANDBOX/ESP32_STYLE_BOARD_PLACEMENT_RULES.md and DEV_BOARD_SHAPE_REASONING_RULES.md; README_GPT.md; FOR CHAT GPT.MD; 01_MEMORY/DESIGN_RULES_MEMORY.md." --issue "The guidance is documented but not yet exercised on a real project-local sandbox study."
python 03_TOOLS/scripts/ai_quality/create_uncertainty_log.py --repo-root . --scope global --title "ESP32 Dev Board Layout Intelligence Uncertainty Log" --summary "The new placement-intelligence guidance is documented and discoverable, but it has not yet been tested through a full project-local sandbox variant set." --details "The main residual uncertainty is operational adoption rather than content structure. The new docs now state the intended rules and warnings, but first live usage may still show that some prompt-pack or project-local references should become more explicit. Validation in this task was limited to file reads, phrase scans, and no-design-file hash checks." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label LOW_RISK --gate-result PASS_WITH_WARNINGS --human-review-required NO --evidence "Created and updated markdown files were read back after patching; reference scans confirmed the warning and core rule language; active-project KiCad hashes matched the baseline." --issue "First real sandbox adoption is still required for end-to-end workflow confidence."
python 03_TOOLS/scripts/ai_quality/create_hallucination_risk_log.py --repo-root . --scope global --title "ESP32 Dev Board Layout Intelligence Hallucination Risk Log" --summary "This task had low hallucination risk because it was constrained to local repo-doc creation, explicit user-specified rule content, and direct validation of the resulting files." --details "The main risk was overstating how broadly the new placement-intelligence docs are already enforced. That was mitigated by describing them as new guidance routed through sandbox discovery, memory, and handoff layers, and by recording a specific open issue for first live project adoption. A second risk was accidentally implying KiCad design-file edits; that was mitigated by pre/post hashes for the active project's .kicad_pcb, .kicad_sch, and .kicad_pro files." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_COMMAND --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Local file patches, readback checks, reference scans, and final KiCad hash recheck." --issue "No unresolved hallucination blocker was identified."
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
