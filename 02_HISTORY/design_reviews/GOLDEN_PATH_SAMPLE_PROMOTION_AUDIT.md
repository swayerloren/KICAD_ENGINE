# Golden Path Sample Promotion Audit

Date: `2026-05-03`

Status: `PROMOTED_AS_CONTROLLED_FIXTURE_WITH_KNOWN_FAILURES`

## Selected Sample

Selected sample: `tomasr8_attiny85_dev_board`

Destination:

`19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/`

## Selection Rationale

This sample was selected as the best available imported sample because:

- it is small and beginner-friendly
- it contains `.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`
- the import records identify MIT license evidence
- attribution, source URL, and imported commit are recorded
- it has the fewest ERC/DRC issues among the imported samples
- it is useful for demonstrating honest gate behavior on a real project

## License And Attribution Evidence

- Source URL: `https://github.com/tomasr8/attiny85-dev-board`
- Source owner: `tomasr8`
- Imported commit: `488b99063b6bdbafa0f367ecc25901b55c4c7144`
- License: MIT License
- Attribution record: `32_OPEN_KICAD_SAMPLE_INTAKE/attribution/tomasr8_attiny85_dev_board_ATTRIBUTION.md`
- Import report: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_IMPORT_REPORT.md`
- Public bundle status: `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`

## Copy Scope

Copied into the controlled fixture:

- `attiny85.kicad_pro`
- `attiny85.kicad_sch`
- `attiny85.kicad_pcb`
- `custom_footprints/MOLEX_48037-0001.kicad_mod`
- `LICENSE`
- `.gitignore`
- `ORIGINAL_UPSTREAM_README.md`
- KiCad Engine sample metadata files

Excluded from the controlled fixture:

- upstream `gerbers/`
- upstream drill files
- upstream PDFs
- bootloader files
- large upstream media assets

## Engineering Status

The sample remains blocked from clean golden-path claims.

| Check | Result |
| --- | --- |
| ERC | `FAIL`, `ERC_MESSAGES_7_ERRORS_1_WARNINGS_6` |
| DRC | `FAIL`, `DRC_VIOLATIONS_16; FOOTPRINT_ERRORS_13; UNCONNECTED_0` |
| Annotation | `PASS`, no unannotated refs detected in prior audit |
| Schematic visual export | `PASS`, full-page SVG in prior audit |
| PCB visual export | `PASS`, top/bottom SVG in prior audit |
| Close-up visual review | `NOT_GENERATED_AUTOMATICALLY` |
| Footprint/library status | `FAIL`, unresolved `My footprints:MOLEX_48037-0001` |
| Fabrication readiness | `BLOCKED` |

## Files Created

- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/KICAD_ENGINE_SAMPLE_README.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/ORIGINAL_SOURCE_ATTRIBUTION.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md`
- `15_BENCHMARKS/tasks/TASK_GOLDEN_PATH_tomasr8_attiny85_dev_board.md`
- `15_BENCHMARKS/results/tomasr8_attiny85_dev_board_BASELINE_RESULT.md`

## Files Updated

- `19_TEST_PROJECTS/sample_kicad_projects/README.md`
- `15_BENCHMARKS/README.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/INDEX.md`
- `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`
- `FOR CHAT GPT.MD`

## Validation

- Destination fixture exists.
- Required KiCad source files are present.
- Upstream generated Gerber/drill/PDF/fabrication-style files are absent from the controlled copy.
- Git status could not be checked because this checkout has no `.git` metadata.

## Final Promotion Status

`CONTROLLED_GOLDEN_PATH_DEMO_FIXTURE_WITH_KNOWN_FAILURES`

This is a valid controlled sample fixture for demonstrating the review workflow, not a passing demo board.

