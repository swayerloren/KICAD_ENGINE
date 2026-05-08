# Open Sample Import Benchmark Candidates

Status: `CANDIDATE_ONLY_NOT_RUN`

This file records imported open KiCad projects that may become benchmark fixtures after review. It does not record benchmark results and must not be used as a scorecard.

## Imported Candidate Fixtures

| Sample | Category | Local normalized copy | Current status | Required before scoring |
| --- | --- | --- | --- | --- |
| ATtiny85 Development Board | Beginner MCU board | `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/tomasr8_attiny85_dev_board/` | `BROKEN_TEST_PROJECT` | ERC/DRC repair or intentional broken-fixture task definition; no scoring yet |
| TPS5430 DC-DC Buck Converter Module | Power/regulator board | `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/m4a1x_tps5430/` | `BROKEN_TEST_PROJECT` | ERC/DRC repair or intentional power-layout failure fixture; no scoring yet |
| ESP Rust Board | ESP32-C3 / USB-C / battery board | `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/esp_rs_esp_rust_board/` | `BROKEN_TEST_PROJECT` | ERC/DRC repair or intentional complex USB-C/ESP32 failure fixture; no scoring yet |

Latest read-only audit: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/SAMPLE_PROJECTS_MASTER_AUDIT.md`.

## Rules

- Do not score these samples until a dedicated benchmark run produces artifacts.
- Do not treat upstream Gerbers, BOMs, placement files, or STEP files as KiCad Engine outputs.
- Do not edit `imported_originals/`.
- Keep generated review outputs `NOT_FINAL`.
- Keep public release status separate from internal benchmark usefulness.
