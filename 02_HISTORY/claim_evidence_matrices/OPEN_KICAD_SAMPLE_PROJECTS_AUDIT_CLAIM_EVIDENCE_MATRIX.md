# Claim Evidence Matrix - Open KiCad Sample Projects Audit

Date: `2026-05-03`

## Claims

| claim | status | evidence | human review required |
| --- | --- | --- | --- |
| Three normalized samples were audited. | `VERIFIED_BY_FILE` | `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/SAMPLE_PROJECTS_MASTER_AUDIT.md` | No |
| `esp_rs_esp_rust_board` fails ERC and DRC under local KiCad CLI. | `VERIFIED_BY_COMMAND` | `esp_rs_esp_rust_board_ERC_DRC_REPORT.md`, command summary JSON | Yes before promotion |
| `m4a1x_tps5430` fails ERC and DRC under local KiCad CLI. | `VERIFIED_BY_COMMAND` | `m4a1x_tps5430_ERC_DRC_REPORT.md`, command summary JSON | Yes before promotion |
| `tomasr8_attiny85_dev_board` fails ERC and DRC under local KiCad CLI. | `VERIFIED_BY_COMMAND` | `tomasr8_attiny85_dev_board_ERC_DRC_REPORT.md`, command summary JSON | Yes before promotion |
| All three samples have no visible unannotated references according to the parser. | `VERIFIED_BY_FILE` | Per-sample engineering audit reports | Yes if used for a benchmark claim |
| Full-page schematic and PCB SVG exports were generated for all samples. | `VERIFIED_BY_COMMAND` | Per-sample visual audit reports and artifact folders | Yes before visual-quality claims |
| Close-up crop review was not completed. | `VERIFIED_BY_FILE` | Per-sample visual audit reports; no visual block configs present | Yes |
| All three samples are `BROKEN_TEST_PROJECT` candidates. | `PARTIALLY_VERIFIED` | ERC/DRC failures and gate reports | Yes before any public-facing classification beyond internal audit |
| No new fabrication outputs were generated. | `VERIFIED_BY_COMMAND` | Command summary contains ERC/DRC/SVG export commands only | Yes before public release packaging |

