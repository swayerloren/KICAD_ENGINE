# PCB Layout Sandbox Gate Added Audit

Date: `2026-05-07`

## Scope

Repo startup rules, PCB workflow gates, project-local sandbox gate reporting, and handoff only. No KiCad schematic, PCB, or manufacturing files were edited.

## Files Updated

- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `00_CODEX_START/START_HERE.md`
- `09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`
- `09_ACCURACY_ENGINE/workflows/CREATE_PCB_WORKFLOW.md`
- `09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md`
- `01_MEMORY/DESIGN_RULES_MEMORY.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_BLOCKERS.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_PROJECT_STATE.md`

## Files Created

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`

## Rule Change Summary

- Real PCB update from schematic is now blocked until both `SCHEMATIC_TO_PCB_GATE_STATUS.md` and `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` are exactly `PASS`.
- Real PCB placement is now blocked by the same two-gate rule.
- The sandbox gate now requires:
  - at least three layout variants
  - a variant scorecard
  - a selected layout plan
  - connector-orientation planning
  - antenna-keepout planning
  - board-shape/dimension planning
  - recorded LJ approval of the selected layout plan
- The project-local `ESP32_CSI_WIFI_NODE` sandbox gate is currently `BLOCKED`.

## Validation

- Readback confirmed the startup and workflow docs now reference the new project-local sandbox gate.
- The active project's new gate file was created and records the current blocked state without touching any KiCad design file.
- Final no-design-file hash recheck is required in session closeout.

## Residual Risk

- `ESP32_CSI_WIFI_NODE` still has stale and conflicting older gate history in some reports; future work should continue to trust the newest evidence files and explicitly supersede older blocked wording where appropriate.
- LJ approval remains a human gate; this patch intentionally does not try to infer it from prior variant-selection work.
