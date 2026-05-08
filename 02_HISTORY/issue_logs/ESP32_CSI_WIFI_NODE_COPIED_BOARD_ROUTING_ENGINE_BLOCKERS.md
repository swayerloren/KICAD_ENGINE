# ESP32_CSI_WIFI_NODE_COPIED_BOARD_ROUTING_ENGINE_BLOCKERS

Date: `2026-05-07`

Status: `OPEN`

## Summary

The copied-board routing-engine live test succeeded as a bridge test, but the project remains blocked for real routing.

## Exact Blockers

- `16` unrouted nets remain
- `3` trace audit entries are flagged
- GND strategy is missing in routing-score evaluation
- critical power net missing in routing-score evaluation
- routing plan did not pass
- unrouted critical net exists
- upstream placement/mechanical project gates still block active-project routing

## Evidence

- `14_LAYOUT_AUTOMATION/real_board_tests/reports/ESP32_CSI_WIFI_NODE_COPIED_BOARD_EXTRACTION_REPORT.md`
- `14_LAYOUT_AUTOMATION/real_board_tests/reports/ESP32_CSI_WIFI_NODE_COPIED_BOARD_ROUTING_AUDIT.md`
- `14_LAYOUT_AUTOMATION/real_board_tests/reports/ESP32_CSI_WIFI_NODE_COPIED_BOARD_ROUTING_AUDIT.json`
