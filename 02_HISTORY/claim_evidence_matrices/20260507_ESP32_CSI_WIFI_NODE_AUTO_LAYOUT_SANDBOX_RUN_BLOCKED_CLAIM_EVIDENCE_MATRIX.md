# Claim Evidence Matrix

Session: `ESP32_CSI_WIFI_NODE_AUTO_LAYOUT_SANDBOX_RUN_BLOCKED`

Date: `2026-05-07`

| Claim | Evidence |
| --- | --- |
| The automatic sandbox run was blocked before variant generation. | User precondition in this session; `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`; `layout_sandbox/AUTO_APPROVAL_REPORT.md` |
| The schematic gate is not exact `PASS`. | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` -> `Gate result: FAIL` |
| Physical footprints are still missing. | `reports/FOOTPRINT_PACKAGE_GATE_REPORT.md` -> `Physical symbols with assigned footprints: 0`; `Physical symbols with blank footprint fields: 43` |
| No KiCad design files changed in this session. | Post-session `Get-FileHash` results recorded in the command log |
