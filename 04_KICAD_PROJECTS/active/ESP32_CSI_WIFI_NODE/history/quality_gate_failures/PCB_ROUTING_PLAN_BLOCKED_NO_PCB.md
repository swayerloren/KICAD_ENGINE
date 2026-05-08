# PCB_ROUTING_PLAN_BLOCKED_NO_PCB

Status: `QUALITY_GATE_BLOCKED`

Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`

Date: 2026-05-03

## Gate

PCB routing gate.

## Failure

Routing is blocked because the active project does not meet the required PCB preconditions.

## Blocking Evidence

- Gate result is `FAIL`.
- No `.kicad_pcb` file exists.
- Placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`.
- Hole/test-pad/via strategy is `HOLE_PAD_VIA_FAIL`.
- Copper-zone strategy is `ZONE_SETUP_FAIL`.

## Required Human Review

Human review remains required for exact footprints, connector orientation, polarity-sensitive parts, USB VBUS/shield policy, ESP32 antenna keepout, board/mechanical constraints, and routing constraints.

