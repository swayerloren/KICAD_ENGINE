# Project Quality Gate Rules

Status: `ACTIVE_PROJECT_MEMORY`

Quality-gate rules for `ESP32_CSI_WIFI_NODE`.

## Blocked Until Human Review

Mark work blocked if:

- exact connector footprint is unverified,
- connector orientation is unverified,
- ESP32 module source/footprint/keepout is unresolved,
- USB power path is uncertain,
- ERC was required but not run,
- DRC was required but not run,
- manufacturing-style output exists without review.

