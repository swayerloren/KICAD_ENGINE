# Auto Layout Decision Engine

## Purpose

Define how Codex/Claude decides whether a selected layout variant is approved for real PCB work.

## Inputs

- active project's `SCHEMATIC_TO_PCB_GATE_STATUS.md`
- active project's `PCB_LAYOUT_SANDBOX_GATE_STATUS.md`
- sandbox variant files
- variant scorecard
- selected layout plan
- routing-feasibility evidence
- footprint and package evidence

## Decision Flow

1. Confirm the selected variant exists.
2. Confirm at least three variants exist.
3. Confirm the scorecard exists.
4. Confirm the selected variant has no hard fails.
5. Confirm the selected variant score is high enough and its risk is acceptable.
6. Confirm board shape, dimensions, connector orientation, and RF keepout are defined.
7. Confirm all physical parts have footprints.
8. Confirm all high-risk footprints are exact-verified or safe-candidate documented.
9. Confirm routing-feasibility evidence exists and passes.
10. Confirm no upstream precheck blocker exists.
11. Write one of:
   - auto-approval report
   - auto-blocked report
12. Update `PCB_LAYOUT_SANDBOX_GATE_STATUS.md`.

## Variant Acceptance Rule

The selected variant is acceptable only when:

- variant status is `PASS`
- no hard fail is present
- total score is `80+`
- risk is `NONE` or `LOW`
- routing-feasibility evidence is `PASS`

## Output Rule

- If every required condition passes, output `AUTO_APPROVED_FOR_PCB_WORK`.
- Otherwise output the most specific `AUTO_BLOCKED_*` status and list every blocker exactly.

## Compatibility Rule

Project gate files continue to use `PASS` or `BLOCKED` as the top-level gate result.

Map them like this:

- top-level gate `PASS` -> auto status `AUTO_APPROVED_FOR_PCB_WORK`
- top-level gate `BLOCKED` -> any `AUTO_BLOCKED_*`

