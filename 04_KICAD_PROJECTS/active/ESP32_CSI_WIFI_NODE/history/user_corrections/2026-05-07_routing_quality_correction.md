# User Correction - Routing Quality

Date: `2026-05-07`

## Correction

LJ explicitly rejected the earlier first-pass scripted routing as not acceptable PCB routing quality.

Required correction:

- remove harsh 90-degree bends,
- remove awkward long/non-professional traces,
- use clean 45-degree or otherwise defensible geometry,
- keep power routes short/direct,
- do not keep bad tracks just because DRC is quiet.

## Applied To

- `ROUTING_STAGE_1_2_CLEANUP_*` reroute session on `ESP32_CSI_WIFI_NODE`

## Status

`CAPTURED_AND_APPLIED`
