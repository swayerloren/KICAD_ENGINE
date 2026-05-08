# Test Projects

Status: `SAFE_TEST_AND_SAMPLE_FIXTURE_AREA`

## Purpose

`19_TEST_PROJECTS/` holds disposable examples, controlled sample projects, and
test fixtures used to exercise KiCad Engine workflows without risking active
user projects.

This folder is where users can see how KiCad Engine handles real KiCad files,
gate reports, attribution, and known blockers. It is not a place for production
projects or final fabrication packages.

## What Belongs Here

- Planning-only workflow examples.
- Public-safe copied sample projects after license and attribution review.
- Broken or partial fixtures for validator tests.
- Expected report shapes for regression checks.
- Documentation that explains how to run and interpret sample gates.

## What Does Not Belong Here

- Active private user projects.
- Unreviewed raw imports from the web.
- Edited copies of `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/`.
- Final fabrication outputs.
- Secrets, API keys, credentials, or private supplier exports.

## Current Sample Projects

| Sample | Path | Status | Purpose |
| --- | --- | --- | --- |
| ATtiny85 development board | `sample_kicad_projects/tomasr8_attiny85_dev_board/` | `CONTROLLED_DEMO_FIXTURE_BLOCKED_UNTIL_HUMAN_REVIEW` | Demonstrates honest gate reporting on a small real KiCad project. |

The ATtiny85 fixture is not a clean passing design. It is blocked by remaining
ERC, DRC, footprint, connector-orientation, polarity, and human-review issues.
That blocked status is intentional and useful: it proves the gate system refuses
to call a design ready when evidence is incomplete or failing.

## Run The Sample Gate

From the repo root:

```powershell
.\03_TOOLS\scripts\project_gate\run_project_gate.ps1 -ProjectPath "19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board"
```

The one-command runner writes:

```text
05_OUTPUTS/gate_runs/<timestamp>/PROJECT_GATE_REPORT.md
05_OUTPUTS/gate_runs/<timestamp>/PROJECT_GATE_REPORT.json
```

Expected current result:

```text
BLOCKED_UNTIL_HUMAN_REVIEW
```

## Inspect Sample Reports

Start with:

- `sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md`
- `sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_GATE_REPORT.md`
- `sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_FINAL_AUDIT.md`
- latest `05_OUTPUTS/gate_runs/<timestamp>/PROJECT_GATE_REPORT.md`

Visual review artifacts live under:

- `sample_kicad_projects/tomasr8_attiny85_dev_board/_verification/schematic_visual/`
- `sample_kicad_projects/tomasr8_attiny85_dev_board/_verification/pcb_visual/`

## Attribution And License

Imported sample projects must preserve source, license, and attribution records.
For the current ATtiny85 fixture, read:

- `sample_kicad_projects/tomasr8_attiny85_dev_board/ORIGINAL_SOURCE_ATTRIBUTION.md`
- `sample_kicad_projects/tomasr8_attiny85_dev_board/LICENSE`

Public bundling remains subject to final human release review even when a source
license appears compatible.

## NOT_FINAL Rule

All sample outputs are review evidence only. They are not fabrication approval.
No Gerber, drill, pick-and-place, STEP, BOM, image, PDF, or gate report in this
folder should be treated as final manufacturing data.

## More Docs

- `SAMPLE_PROJECTS_INDEX.md`
- `HOW_TO_RUN_SAMPLE_PROJECTS.md`
- `HOW_TO_INTERPRET_GATE_RESULTS.md`
- `18_PUBLIC_DOCS/HOW_TO_RUN_GOLDEN_PATH_DEMO.md`
- `18_PUBLIC_DOCS/HOW_TO_VERIFY_PROJECT.md`
