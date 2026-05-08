# Pill-Style PCB Placement Rules Updated

Date: 2026-05-07

Task: Patch KiCad Engine placement rules after the `ESP32_CSI_WIFI_NODE` pill-style placement exposed connector, spacing, test-pad, and mechanical fit problems.

## Actions

- Read startup and handoff files.
- Confirmed target changes were docs/rules/prompts/history only.
- Created new PCB placement rule files under `09_ACCURACY_ENGINE/pcb_rules`.
- Created new pill-style placement checklist under `09_ACCURACY_ENGINE/checklists`.
- Updated pipeline placement prompts for pass 1 and pass 2 orientation audit.
- Updated `AGENTS.md`, `README_GPT.md`, and `FOR CHAT GPT.MD`.
- Created audit, session, and command-log records.

## KiCad Design Files

No KiCad design files were edited.

No routing, zones, or fabrication outputs were generated.

## Result

Rule patch status: `COMPLETE`

Current `ESP32_CSI_WIFI_NODE` placement status remains:

`BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

Routing remains blocked until a real placement repair is applied, audited, and visually approved by LJ.
