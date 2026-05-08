# Auto Approval Status Codes

## Purpose

Define the exact status codes used by the PCB Layout Sandbox auto-approval gate.

The project-level gate file still uses a top-level gate result such as `PASS` or `BLOCKED`.
These status codes provide the exact reason underneath that gate result.

## Rule

`AUTO_APPROVED_FOR_PCB_WORK` is the only status that may support a sandbox gate result of `PASS`.

Every `AUTO_BLOCKED_*` status forces the sandbox gate result to remain `BLOCKED` and requires an auto-blocked report with exact missing items or failing evidence.

## Status Codes

### `AUTO_APPROVED_FOR_PCB_WORK`

Use only when every required sandbox precondition has objective evidence and the selected variant is safe to carry into real PCB work.

### `AUTO_BLOCKED_MISSING_DATA`

Use when required sandbox evidence is missing, stale, incomplete, or still assumption-only.

Examples:

- board dimensions are still guessed
- routing-feasibility evidence was never produced
- the selected-layout auto-approval report does not exist

### `AUTO_BLOCKED_BAD_LAYOUT`

Use when the selected variant is objectively poor even if the evidence set is complete.

Examples:

- selected variant has hard fails
- projected pathing is implausible
- score is too low

### `AUTO_BLOCKED_ROUTING_FEASIBILITY_FAIL`

Use when routing-feasibility evidence shows congestion, impossible placement, unrouted critical path risk, or another objective routing-feasibility failure.

### `AUTO_BLOCKED_HIGH_RISK_FOOTPRINT_UNVERIFIED`

Use when high-risk footprints are not backed by exact package evidence or an explicitly documented safe-candidate source path.

Examples:

- USB-C footprint not tied to exact package drawing
- barrel jack footprint not mechanically verified
- RF module footprint not verified to exact module/keepout requirements

### `AUTO_BLOCKED_MECHANICAL_CONFLICT`

Use when board shape, edge placement, mounting, enclosure, service access, or connector overhang assumptions conflict with each other.

### `AUTO_BLOCKED_ANTENNA_KEEPOUT_VIOLATION`

Use when the selected variant blocks or crosses the RF keepout or antenna service zone.

### `AUTO_BLOCKED_CONNECTOR_ORIENTATION_UNKNOWN`

Use when a connector's intended edge, facing direction, or mating direction is still unknown, contradictory, or not mechanically defensible.

### `AUTO_BLOCKED_DRC_PRECHECK_FAIL`

Use when a required precheck or gate-level blocker already proves that PCB work must not start.

Examples:

- schematic-to-PCB gate is not `PASS`
- ERC is not `PASS`
- KiCad-native annotation evidence is missing

## Precedence

When multiple block conditions exist, use the most specific highest-risk code first:

1. `AUTO_BLOCKED_DRC_PRECHECK_FAIL`
2. `AUTO_BLOCKED_HIGH_RISK_FOOTPRINT_UNVERIFIED`
3. `AUTO_BLOCKED_ANTENNA_KEEPOUT_VIOLATION`
4. `AUTO_BLOCKED_CONNECTOR_ORIENTATION_UNKNOWN`
5. `AUTO_BLOCKED_MECHANICAL_CONFLICT`
6. `AUTO_BLOCKED_ROUTING_FEASIBILITY_FAIL`
7. `AUTO_BLOCKED_BAD_LAYOUT`
8. `AUTO_BLOCKED_MISSING_DATA`

The blocked report must still list every additional blocker, not only the primary status code.

