# Project Hallucination Risks

Status: `ACTIVE_PROJECT_MEMORY`

Known hallucination risks for `ESP32_CSI_WIFI_NODE`.

## Risks

- Generic USB-C connector footprint selection.
- Generic RF connector or U.FL pigtail assumptions.
- ESP32-S3 module keepout and pinout assumptions without exact module source.
- Regulator layout and thermal assumptions without datasheet review.
- USB power/backfeed assumptions without a reviewed power-path decision.

## Required Mitigation

Create project hallucination-risk logs for any guessed or weakly sourced high-risk claim.

