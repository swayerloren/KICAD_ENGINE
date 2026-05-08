# Gate Status - esp_rs_esp_rust_board

Generated: `2026-05-03T18:36:21Z`

Gate result: `FAIL_NEEDS_REVIEW`

Classification: `BROKEN_TEST_PROJECT`

## Gate Checks

- Project files found: yes
- License present: yes
- ERC result: `FAIL`
- DRC result: `FAIL`
- Annotation result: PASS
- Footprint static library check: FAIL
- Embedded/no-library-prefix footprint review: REVIEW_REQUIRED
- 3D model check: WARN_OR_FAIL
- Visual exports: schematic `PASS`, top `PASS`, bottom `PASS`

## Blockers / Review Items

- ERC did not pass cleanly: ERC_MESSAGES_73_ERRORS_6_WARNINGS_67.
- DRC did not pass cleanly: DRC_VIOLATIONS_81; FOOTPRINT_ERRORS_95; UNCONNECTED_0.
- Some footprint assignments are missing or unresolved against installed/project libraries.
- Some board footprints are embedded/no-library-prefix and need human review before reuse.
- Some 3D models are missing after known variable resolution.

## Promotion Decision

Do not promote this sample to a public payload or scored benchmark until the blockers above are closed or explicitly accepted with human review.
