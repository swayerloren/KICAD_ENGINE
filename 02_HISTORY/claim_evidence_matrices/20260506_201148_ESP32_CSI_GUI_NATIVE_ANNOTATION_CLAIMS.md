# Claim Evidence Matrix: ESP32_CSI_WIFI_NODE GUI Native Annotation Attempt

Date: `2026-05-06`

| Claim | Status | Evidence |
|---|---|---|
| No Eeschema window was detected. | `VERIFIED_BY_COMMAND` | `detect_unsaved_kicad_state.ps1` returned `NO_EESCHEMA_WINDOW` twice. |
| Backup was created before possible GUI action. | `VERIFIED_BY_COMMAND` | Backup copy command and SHA256 output. |
| Native GUI annotation did not run. | `VERIFIED_BY_COMMAND` | No Eeschema window existed; no GUI action commands were run. |
| CLI ERC passes on the saved file. | `VERIFIED_BY_COMMAND` | `KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.rpt` reports 0 errors and 0 warnings. |
| Saved file has no unresolved question patterns. | `VERIFIED_BY_COMMAND` | `rg` scan returned no unresolved question patterns. |
| PCB update remains blocked. | `VERIFIED_BY_FILE` | `SCHEMATIC_TO_PCB_GATE_STATUS.md` gate result is `FAIL`. |
