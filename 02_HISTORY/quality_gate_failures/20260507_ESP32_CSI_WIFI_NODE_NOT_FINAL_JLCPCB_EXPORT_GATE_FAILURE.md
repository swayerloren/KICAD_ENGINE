# Quality Gate Failure: ESP32_CSI_WIFI_NODE NOT_FINAL JLCPCB Export

Date: 2026-05-07

Gate: `NOT_FINAL_JLCPCB_EXPORT_PRECONDITIONS`

Result: `FAIL`

## Failed Requirements

- DRC pass or accepted nonblocking DRC violations: `FAIL_NOT_RUN_NO_PCB`
- No unrouted nets: `FAIL_UNKNOWN_NO_PCB`
- JLCPCB DFM/DFA review pass or accepted: `FAIL_JLCPCB_REVIEW_BLOCKED`
- BOM review pass or accepted: `FAIL_BOM_BLOCKED`

## Required Action

Do not export or upload a JLCPCB package until the schematic-to-PCB gate passes, a PCB exists, DRC/unrouted checks are current, and JLCPCB/BOM blockers are closed or explicitly accepted by LJ as nonblocking review risks.

