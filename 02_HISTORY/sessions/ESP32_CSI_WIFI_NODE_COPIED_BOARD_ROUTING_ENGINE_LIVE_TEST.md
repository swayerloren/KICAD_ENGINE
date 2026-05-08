# ESP32_CSI_WIFI_NODE_COPIED_BOARD_ROUTING_ENGINE_LIVE_TEST

Date: `2026-05-07`

## Summary

Ran the first live routing-engine test against a copied `ESP32_CSI_WIFI_NODE.kicad_pcb` only. The read-only bridge extracted routing-schema data, generated copied-board audit outputs, and confirmed that the engine works on a real copied board without touching the active project PCB.

## Results

- created copied-board test folder under `14_LAYOUT_AUTOMATION/real_board_tests/sample_inputs/`
- copied the active PCB into that folder
- verified source and copy SHA256 hashes match
- ran narrow extractors for nets/pads, tracks/vias, zones/keepouts, and net classes
- generated `ESP32_CSI_WIFI_NODE_ROUTING_SCHEMA.json`
- ran copied-board routing audit outputs including unrouted-net, keepout, trace-audit, and score reports
- confirmed the copied-board audit blocks for real routing reasons rather than bridge failure

## Key Outcome

The routing engine now works on a real copied board. Active-project routing is still blocked.

## Safety

No active-project KiCad design files were modified.
