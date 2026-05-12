# ERC DRC Required Rules

## Purpose

Define when KiCad Engine agents must run, request, or explicitly defer ERC and DRC.

## ERC Is Required When

- A schematic file is created or changed.
- Symbols, pins, power nets, labels, hierarchical sheets, or net ties are changed.
- A component is added, removed, or replaced.
- A schematic is being reviewed for readiness.
- A BOM, PCB sync, or manufacturing workflow depends on schematic correctness.

## DRC Is Required When

- A PCB file is created or changed.
- A footprint is assigned, changed, moved, or replaced.
- Tracks, zones, vias, board outline, mounting holes, or copper clearances are changed.
- Gerbers, drills, pick-and-place, STEP, or other manufacturing-style outputs are generated.
- A PCB is being reviewed for readiness.

## Evidence Requirement

An agent must not claim ERC or DRC passed unless it has actual command output or report evidence from `kicad-cli`, KiCad, KiBot, or another documented verification workflow.

Board-aware scripts must use a KiCad-compatible Python context when `pcbnew`
object access is required. Normal repo Python is not proof that `pcbnew` is
available.

Saved-file parsing and third-party extraction are allowed for audit and
triage, but native KiCad validation remains stronger evidence than parser-only
results.

Acceptable statuses:

- `ERC_RUN_PASS`
- `ERC_RUN_WARNINGS`
- `ERC_RUN_FAIL`
- `ERC_NOT_RUN_EXPLAINED`
- `DRC_RUN_PASS`
- `DRC_RUN_WARNINGS`
- `DRC_RUN_FAIL`
- `DRC_NOT_RUN_EXPLAINED`

## Blocking Rule

If ERC/DRC is required but not run, mark the work:

`BLOCKED_UNTIL_VERIFICATION`

If manufacturing-style outputs are involved, also mark:

`NOT_FINAL`

## KiCad-Specific Interpretation

- prefer `kicad-cli sch erc` for saved-file ERC evidence
- prefer `kicad-cli pcb drc --schematic-parity --severity-all --format report`
  when parity-aware PCB gate evidence is required
- use native KiCad GUI workflows for annotation and disputed live GUI state
  because CLI alone cannot prove those states
