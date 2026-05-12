# Schematic Layout Engine Audit

Date: `2026-05-10`
Scope: `Repo tooling, rules, prompts, memory, and read-only validation`
Task type: `AUDIT_ONLY`
Active project used for dry-run: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

## Objective

Create a schematic visual cleanup and layout engine so future Codex/Claude
sessions can plan professional functional-block cleanup, prefer real wires over
local label spray, and score schematic readability before claiming schematic
readiness.

## Added Or Completed

- `03_TOOLS/scripts/schematic_layout/README.md`
- `03_TOOLS/scripts/schematic_layout/extract_schematic_layout.py`
- `03_TOOLS/scripts/schematic_layout/score_schematic_readability.py`
- `03_TOOLS/scripts/schematic_layout/plan_schematic_block_layout.py`
- `03_TOOLS/scripts/schematic_layout/rewrite_schematic_layout_safe.py`
- `03_TOOLS/scripts/schematic_layout/render_schematic_review_pages.py`
- `03_TOOLS/scripts/schematic_layout/audit_visual_flow.py`
- `03_TOOLS/scripts/schematic_layout/audit_local_wire_usage.py`
- `03_TOOLS/scripts/schematic_layout/schematic_layout_common.py`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md`
- `34_SCHEMATIC_QUALITY_ENGINE/FUNCTIONAL_BLOCK_TEMPLATES.md`
- `34_SCHEMATIC_QUALITY_ENGINE/LOCAL_WIRING_STYLE_GUIDE.md`
- `34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md`
- `.prompts/kicad_pipeline/02_schematic_visual_cleanup.md`
- `.prompts/kicad_pipeline/03_schematic_electrical_review.md`

## Updated

- `34_SCHEMATIC_QUALITY_ENGINE/README.md`
- `34_SCHEMATIC_QUALITY_ENGINE/README_FOR_CODEX_AND_CLAUDE.md`
- `09_ACCURACY_ENGINE/schematic_rules/READABLE_SCHEMATIC_FLOW_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/WIRE_VS_NET_LABEL_RULES.md`
- `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`
- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `START_HERE_FOR_AI_AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `01_MEMORY/DESIGN_RULES_MEMORY.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_BLOCKERS.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/PROJECT_MEMORY.md`

## Validation

- Python syntax: `PASS`
- Read-only review packet generation: `PASS`
- Dry-run result on active schematic: `FAIL` as intended
- No active KiCad design files changed: `PASS`

## Active Project Dry-Run Findings

- Review packet:
  `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_layout/20260510_113053/`
- Readability score: `39 / 100`
- Visual flow: `FAIL`
- Local wire usage: `FAIL`
- ERC category: `PASS`
- Annotation category: `FAIL`
- Footprint category: `FAIL`

## Main Failure Causes

- Disordered power flow between input, buck, and ESP32 blocks
- USB-C support path placed in the wrong visual region
- Repeated local labels inside ESP32, reset/boot, and test/debug blocks
- Label-heavy local USB signal presentation in the debug area

## Notes

- The safe rewrite wrapper remained dry-run only and wrote no schematic.
- This task did not edit `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files.
