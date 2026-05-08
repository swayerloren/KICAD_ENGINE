# Open KiCad Sample Import Audit

Date: `2026-05-03`

Status: `IMPORT_COMPLETED_REVIEW_REQUIRED`

## Executive Summary

Three approved open-license KiCad sample projects were imported into the controlled sample-intake area. Each sample now has a preserved original copy, a normalized working copy, attribution record, and import report.

The import is useful for future benchmark and workflow testing, but the samples are not verified reference designs. Public payload inclusion and benchmark scoring remain blocked until human license review and technical review are complete.

## Imported Samples

| Sample | Source | License | Original files | Normalized copy | Status |
| --- | --- | --- | ---: | --- | --- |
| `tomasr8_attiny85_dev_board` | https://github.com/tomasr8/attiny85-dev-board | MIT | 32 | yes | `IMPORTED_NEEDS_REVIEW` |
| `m4a1x_tps5430` | https://github.com/M4a1x/TPS5430 | CERN-OHL-S-2.0 | 39 | yes | `IMPORTED_NEEDS_REVIEW` |
| `esp_rs_esp_rust_board` | https://github.com/esp-rs/esp-rust-board | CERN-OHL-P-2.0 | 52 | yes | `IMPORTED_NEEDS_REVIEW` |

## Rules Check

| Rule | Result | Evidence |
| --- | --- | --- |
| Import only approved/public-bundle candidates | PASS | Candidate index marked these three as `PUBLIC_BUNDLE_ALLOWED` pending attribution/human review. |
| Keep unclear-license candidates link-only | PASS | No second-wave or official KiCad demo candidates imported. |
| Preserve license and attribution | PASS | Attribution records and local source license files exist for each sample. |
| Store original under `imported_originals` | PASS | Three source copies exist under `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/`. |
| Create normalized copy | PASS | Three normalized copies exist under `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/`. |
| Do not edit imported originals | PASS_WITH_CAVEAT | Originals were populated during import only. No analysis/repair edits were made after population. |
| Do not merge into active projects | PASS | No `04_KICAD_PROJECTS/active` paths were targeted. |
| Do not generate manufacturing outputs | PASS | No KiCad exports were run. Imported upstream Gerbers/outputs are source artifacts only. |
| Do not import huge repos without reporting size | PASS | Repository sizes were reported before import. |

## Warnings

- Imported samples include upstream fabrication-style files. These are not KiCad Engine outputs and must not be relabeled as generated `NOT_FINAL` packages.
- KiCad compatibility was not verified beyond detecting project files.
- ERC, DRC, visual review, footprint/package audit, BOM review, and public payload review have not been run.
- Human license review is still required before public bundle release.

## Failed Attempts Captured

- `02_HISTORY/failed_attempts/OPEN_KICAD_SAMPLE_IMPORT_FAILED_ATTEMPTS.md`

## Closeout Validation

| Check | Result |
| --- | --- |
| Original and normalized folders exist for all three samples | PASS |
| License file exists in each original and normalized copy | PASS |
| `.kicad_pro` exists in each original and normalized copy | PASS |
| `.git` folders imported | PASS, none found |
| Targeted obvious-secret scan | PASS, no matches |
| Active project modified | PASS, no active-project paths targeted |
| Generated indexes rebuilt | PASS |

## Next Review Gate

Run `32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_REVIEW_WORKFLOW.md` against normalized copies only. Start with the smallest sample, `tomasr8_attiny85_dev_board`, before attempting ESP32/USB-C/battery review complexity.
