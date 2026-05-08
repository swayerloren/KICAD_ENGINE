# KiCad Engine Sample - ATtiny85 Development Board

Status: `CONTROLLED_GOLDEN_PATH_DEMO_FIXTURE_WITH_KNOWN_FAILURES`

## Purpose

This folder is a controlled KiCad Engine sample fixture copied from the normalized imported open-source sample:

`32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/tomasr8_attiny85_dev_board/`

It is intended to demonstrate the KiCad Engine review workflow on a small real KiCad project:

- source/license/attribution tracking
- KiCad source inventory
- ERC/DRC execution
- schematic and PCB visual export
- missing library/footprint detection
- honest gate reporting
- benchmark baseline recording without fake pass claims

## What Was Copied

The controlled fixture includes:

- `attiny85.kicad_pro`
- `attiny85.kicad_sch`
- `attiny85.kicad_pcb`
- `custom_footprints/MOLEX_48037-0001.kicad_mod`
- `LICENSE`
- `.gitignore`
- `ORIGINAL_UPSTREAM_README.md`

## What Was Excluded

The controlled fixture intentionally excludes upstream generated or redistribution-sensitive artifacts:

- upstream `gerbers/`
- upstream drill files
- upstream PDFs under `assets/` and `bootloader/`
- large upstream photo/render media
- bootloader helper files

Those excluded files remain in the preserved import/normalized intake area for audit context only. They are not KiCad Engine outputs and must not be treated as final fabrication packages.

## Current Engineering Status

This fixture does not currently pass the KiCad Engine gate:

- ERC result: `FAIL`, 6 messages, 1 error, 5 warnings
- DRC result: `FAIL`, 15 DRC violations and 13 schematic parity/footprint issues
- annotation result: pass, no unannotated references detected by the audit parser
- schematic visual export: pass
- PCB top/bottom visual export: pass
- schematic and PCB close-up crops: generated, but human review remains required
- footprint audit status: custom footprint library mapping repaired; exact connector/regulator/header verification remains blocked
- latest one-command gate runner result: `BLOCKED_UNTIL_HUMAN_REVIEW`

Latest one-command gate report:

- `05_OUTPUTS/gate_runs/20260506_142924/PROJECT_GATE_REPORT.md`

## How Agents Should Use This Sample

Use this fixture to test review workflows, not design correctness:

1. Run inventory, ERC, DRC, annotation, footprint, and visual-export checks.
2. Confirm the known failures are detected.
3. Record reports under `02_HISTORY/`, `05_OUTPUTS/`, or `15_BENCHMARKS/results/` as appropriate.
4. Keep any generated outputs explicitly `NOT_FINAL`.
5. Do not silently repair the sample.

## What This Demo Proves

- KiCad Engine can preserve an open-source KiCad project as a controlled test fixture.
- KiCad Engine can run checks and surface real failures without overclaiming.
- KiCad Engine can distinguish source files from generated or excluded upstream artifacts.
- The review pipeline can classify a real sample as blocked instead of pretending it is ready.
- The one-command gate runner can aggregate existing evidence and surface exact blockers.

## What This Demo Does Not Prove

- It does not prove the board is electrically correct.
- It does not prove ERC or DRC passes.
- It does not prove the custom USB connector footprint is correct.
- It does not prove the sample is fabrication-ready.
- It does not prove KiCad Engine can automatically repair imported projects.
- It does not approve public payload inclusion without final human license/release review.

## Required Before Any Repair

Any future repair task must:

- use this controlled copy, not `imported_originals`
- create a backup before KiCad source edits
- document the intended repair plan
- preserve attribution
- run ERC, DRC, visual review, footprint review, and gate checks again
- keep generated outputs `NOT_FINAL`
