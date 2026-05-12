# PCB Variant Scoring Rules

## Purpose

Score placement variants from objective prelayout evidence before real board edits.

## Categories

Use a `0-100` total with these category ranges:

- mechanical correctness: `0-20`
- connector truth correctness: `0-20`
- RF keepout correctness: `0-15`
- power-path logic: `0-15`
- USB/data-path logic: `0-10`
- component grouping: `0-10`
- route feasibility: `0-10`

## Hard Fails

Any one of these forces `FAIL`:

- wrong connector mating direction
- unknown connector truth for a required connector
- connector truth still marked `NEEDS_HUMAN_REVIEW`
- route projection crosses RF keepout
- projected route uses non-45-degree acute geometry
- projected route cannot close a required net
- required component group has no feasible channel
- board dimensions are guessed

Connector orientation is not proven by XY position or rotation alone. A connector with a missing 3D model or unresolved front/back proof remains blocking even if its edge position looks correct.

## Status Thresholds

- `PASS`: score `80+`, no hard fail, projected open-net count `0`
- `AUTO_BLOCKED_BAD_LAYOUT`: score `<80`, evidence complete, no missing-data blocker
- `AUTO_BLOCKED_MISSING_DATA`: required fields or connector truth evidence missing
- `FAIL`: one or more hard fails

## Selection Rule

The selected variant must be the highest-ranked non-failed candidate.

The selector must never choose:

- a hard-failed variant
- a variant with projected open nets
- a variant with connector truth marked unknown
- a variant with connector truth marked `NEEDS_HUMAN_REVIEW`

## Reference Sample Comparison

Reviewed open-source PCB samples may be used as supporting comparison evidence
for grouping quality, connector edge placement patterns, and projected routing
compactness.

They do not override connector truth, RF keepout, projected open-net, or
geometry hard-fail rules. Human-made samples can still be wrong.

## Canonical Rule Links

- `09_ACCURACY_ENGINE/pcb_rules/USB_C_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/BUCK_REGULATOR_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/ESP32_RF_ANTENNA_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/MOUNTING_HOLE_MECHANICAL_RULES.md`
