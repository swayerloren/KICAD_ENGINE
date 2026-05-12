# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| The saved schematic has `0` blank footprint fields. | `reports/footprint_assignment_blank_footprints.json` |
| ERC still passes after the lock-file run. | `reports/erc_after_footprint_lock.raw.txt` |
| The footprint package gate is `NEEDS_HUMAN_REVIEW`. | `reports/footprint_package/20260510_footprint_lock_apply/FOOTPRINT_PACKAGE_GATE_REPORT.md` |
| `U2` is mismatched between value and saved footprint. | `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`, `reports/FOOTPRINT_PACKAGE_PROOF_REPORT.md`, Espressif `1U` official product page and datasheet |
| `U3` package evidence points to TI `Texas_DRT-3`, not the saved `SOT-23-6`. | `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`, installed KiCad symbol library `TPD2EUSB30`, TI product page and datasheet, `reports/FOOTPRINT_PACKAGE_PROOF_REPORT.md` |
| PCB update may not begin. | `reports/SCHEMATIC_READY_FOR_PCB_UPDATE_GATE.md`, footprint gate report, schematic quality report |
