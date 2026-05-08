# Quality Gate Failure - Open KiCad Samples Not Promotion Ready

Date: `2026-05-03`

Gate: `SAMPLE_PROMOTION_GATE`

Status: `FAILED`

Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`

## Gate Result

No imported normalized sample currently passes the gate for golden-path demo, clean benchmark baseline, reference-grade design, or public payload promotion.

## Blocking Evidence

| sample | blocking evidence |
| --- | --- |
| `esp_rs_esp_rust_board` | ERC failed with 73 messages, DRC failed with 81 DRC violations and 95 footprint/parity errors |
| `m4a1x_tps5430` | ERC failed with 36 warnings, DRC failed with 87 DRC violations and 30 footprint/parity errors |
| `tomasr8_attiny85_dev_board` | ERC failed with 7 messages, DRC failed with 16 DRC violations and 13 footprint/parity errors |

## Required Before Promotion

1. Separate approved repair/enrichment task.
2. Preserve `imported_originals` unchanged.
3. Repair only normalized copies.
4. Rerun ERC and DRC.
5. Complete close-up visual review.
6. Resolve missing libraries, footprint mismatches, DRC violations, and gate blockers.
7. Record license/public-payload status before public distribution.

