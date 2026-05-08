# PCB Update Blocked Claim Evidence Matrix

Date: `2026-05-06 22:07:44 -04:00`

| Claim | Evidence | Status |
| --- | --- | --- |
| Native KiCad GUI annotation completed successfully | `reports/KICAD_GUI_NATIVE_ANNOTATION_RUN_REPORT.md` | `SUPPORTED` |
| ERC passes after native annotation | `reports/KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.md` | `SUPPORTED` |
| Stored unresolved reference tokens are not present | `reports/KICAD_GUI_NATIVE_ANNOTATION_REFERENCE_TABLE.md`; direct `rg` scan found only `ki_fp_filters` wildcard strings | `SUPPORTED_FOR_REFERENCE_TOKENS` |
| PCB update may proceed | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` says `Gate result: FAIL` and `PCB update allowed: NO` | `REFUTED` |
| PCB file exists | `Test-Path kicad/ESP32_CSI_WIFI_NODE.kicad_pcb` returned `False` | `REFUTED` |
| Footprints were imported | PCB update was not run | `REFUTED` |
| DRC result is available | DRC was not run because no PCB exists | `REFUTED` |
| Placement planning may begin | Gate is `FAIL`; PCB does not exist | `REFUTED` |
