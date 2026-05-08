# Post Sample Project Blockers

Date: `2026-05-06`

Status: `OPEN_BLOCKERS`

## Blocking Public Release

1. `tomasr8_attiny85_dev_board` remains `BLOCKED_UNTIL_HUMAN_REVIEW`.
2. Latest gate run: `05_OUTPUTS/gate_runs/20260506_145808/PROJECT_GATE_REPORT.md`.
3. ERC fails on `J1` shield pin.
4. DRC fails with 15 violations.
5. PCB sync/parity fails with 13 schematic/footprint issues.
6. Footprint/package/orientation review remains open for `J1`, `J2`, and `U2`.
7. Schematic and PCB visual close-up reviews still require human review.
8. Final PCB verification before fab is missing.
9. NOT_FINAL fab package audit is missing because fab export is blocked.
10. Public bundle status remains
    `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`.
11. `17_RELEASE_BUILD/build_public_payload.py` is missing.
12. `21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md` still says
    `REQUIRES_HUMAN_REVIEW`.
13. Broad repo public release must exclude local virtual environments,
    third-party tool repos, backups, generated outputs, and secret-named files.

## Not Blockers, But Important

- The sample is still useful as a blocked-gate demo fixture.
- The gate runner is working as intended when it refuses to pass the sample.
- Imported originals and normalized copies are separate and documented.
- No sample fabrication folder was found in the controlled fixture.
- No credential files were found in the audited sample/release/public areas.
