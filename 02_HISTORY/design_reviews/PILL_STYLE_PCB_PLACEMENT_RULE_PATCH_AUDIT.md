# Pill-Style PCB Placement Rule Patch Audit

Date: 2026-05-07

Scope: KiCad Engine rule, checklist, prompt, and handoff patch. No KiCad schematic, PCB, routing, zone, or fabrication outputs were edited or generated.

## Problem Recorded

`ESP32_CSI_WIFI_NODE` exposed a placement quality failure:

1. Codex initially created an oversized board with a large dead area.
2. After correction, Codex created a better pill-style board.
3. The pill-style placement still had connector, spacing, test-pad, silkscreen, mounting-hole, RF keepout, and mechanical fit problems.
4. The workflow did not sufficiently enforce bottom-facing connector orientation, clean service rows, barrel-jack practicality, or LJ visual approval before routing.

## Files Created

- `09_ACCURACY_ENGINE/pcb_rules/PILL_STYLE_DEV_BOARD_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/CONNECTOR_EDGE_ORIENTATION_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/TEST_PAD_PLACEMENT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/ESP32_RF_KEEP_OUT_PLACEMENT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/PCB_MECHANICAL_CLEARANCE_RULES.md`
- `09_ACCURACY_ENGINE/checklists/PILL_STYLE_PLACEMENT_CHECKLIST.md`

## Files Updated

- `.prompts/kicad_pipeline/09_pcb_placement_pass_1.md`
- `.prompts/kicad_pipeline/10_pcb_placement_pass_2_orientation.md`
- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## New Hard Rules Added

- ESP32 module boards should place the module at the top edge with antenna/U.FL/RF keepout facing the top edge unless documented otherwise.
- USB-C on dev-board layouts should normally be bottom-edge, mouth off-board, and footprint edge-line aligned.
- Barrel jacks are usually not pill-board-friendly and require explicit mechanical review if retained.
- Test pads must be in clean service rows, not mixed into component clusters.
- Test pads must not be crowded behind USB-C shells or cable exits.
- Reset/boot buttons must be edge-accessible.
- LEDs must be visible.
- Mounting holes must not be placed in RF keepout or connector mechanical areas.
- Four mounting holes on narrow boards require proven clearance.
- Placement is not ready if any component/courtyard/text/pad overlap exists.
- Placement is not ready if connector ports do not face the intended edge.
- Placement is not ready if the board has giant dead areas without reason.
- Routing is blocked until LJ visually approves placement.

## Prevention Mechanism

The new rules prevent the `ESP32_CSI_WIFI_NODE` failure mode by changing placement review from "components are on a smaller board" to explicit mechanical pass/fail checks:

- Connector edge and mouth direction must be declared and verified.
- USB-C bottom-edge alignment is no longer implicit.
- Barrel jack retention on a pill board is a named review risk.
- Test pads must be treated as a service row with clearance, not as filler.
- RF keepout must be edge-facing and clear.
- Four-hole compact layouts must prove clearance before being accepted.
- Courtyard, silkscreen, text, pad, and mechanical overlaps block routing.
- LJ visual approval is required before routing.

## Current ESP32_CSI_WIFI_NODE Placement Status

Current status: `BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

Routing status: `BLOCKED`

Reason:

- Repaired placement was not actually applied.
- Current pill-style placement still has test-pad crowding, J1 mechanical risk, J2 edge review risk, four-hole strategy risk, U2 footprint/keepout risk, silkscreen issues, and DRC placement blockers.

Evidence:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_PILL_STYLE_PLACEMENT_REPAIR_AUDIT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/LJ_PILL_STYLE_REPAIRED_PLACEMENT_REVIEW_CHECKLIST.md`

## Classification

`RULE_PATCH_COMPLETE`
