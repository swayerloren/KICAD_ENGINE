# Claim Evidence Matrix

Session: `ESP32_CSI_WIFI_NODE_AUTO_PCB_START_BLOCKED`

Date: `2026-05-07`

| Claim | Evidence |
| --- | --- |
| Automatic PCB start is blocked. | `reports/AUTO_PCB_START_REPORT.md`; `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`; `layout_sandbox/AUTO_APPROVAL_REPORT.md` |
| The schematic-to-PCB gate is exact `FAIL`. | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` |
| The sandbox auto-approval report is not `AUTO_APPROVED_FOR_PCB_WORK`. | `layout_sandbox/AUTO_APPROVAL_REPORT.md` |
| No PCB update, placement, DRC, or visual export occurred in this run. | `reports/AUTO_PCB_START_REPORT.md`; command log for this session |
