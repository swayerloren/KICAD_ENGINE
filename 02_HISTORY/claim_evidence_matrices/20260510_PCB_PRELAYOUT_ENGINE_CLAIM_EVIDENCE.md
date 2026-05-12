# Claim Evidence Matrix - PCB Prelayout Engine

Date: `2026-05-10`
Task type: `DOCS_ONLY`

| Claim | Evidence |
| --- | --- |
| The repo now has a dedicated prelayout engine folder with docs and schemas. | New files under `33_PCB_PRELAYOUT_ENGINE/` and `33_PCB_PRELAYOUT_ENGINE/schemas/`. |
| The repo now has supporting read-only prelayout scripts. | New files under `03_TOOLS/scripts/pcb_prelayout/`; `python -m py_compile ...` passed. |
| Real PCB placement and routing now have an added mandatory prelayout rule in the main startup/handoff docs. | Updated `AGENTS.md`, `START_HERE_FOR_AI_AGENTS.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, `00_CODEX_START/START_HERE.md`, `00_CODEX_START/FOLDER_ROUTING_RULES.md`, `00_CODEX_START/REPO_STRUCTURE_INDEX.md`, and `00_CODEX_START/REPO_MAP.md`. |
| The dry-run on `ESP32_CSI_WIFI_NODE` generated three variants and one passing variant. | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/prelayout_engine/20260510_083835/prelayout_gate_result.json`. |
| The engine blocks wrong connector direction. | `scores/variant_02.score.json` records `CONNECTOR_DIRECTION_FAIL` and `status = FAIL`. |
| The engine blocks projected open nets and overlap-driven bad layouts. | `scores/variant_02.score.json` and `scores/variant_03.score.json` record `PROJECTED_OPEN_NETS_PRESENT`; `variant_03.score.json` also records `MECHANICAL_COMPONENT_OVERLAP`. |
| The dry-run blocks routing continuation when the live board still has open nets even with zero geometry violations. | `prelayout_gate_result.json` records `routing_gate_status = BLOCKED`, `13` unconnected items, `3` detectable unrouted nets, and `0` DRC violations. |
| No tracked KiCad schematic or PCB source file changed in this task. | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'` returned no files; `git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb'` returned no tracked modifications. |
