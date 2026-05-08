# Issue Log: Schematic Safe Repair Blockers Remain Open

Date: 2026-05-06
Project: `ESP32_CSI_WIFI_NODE`
Status: `OPEN`
Severity: `BLOCKS_PCB_UPDATE`

## Summary

Safe schematic cleanup was completed and verified. ERC remains clean and automated schematic visual crops now pass, but the schematic remains blocked before PCB update.

## Evidence

- `reports/SCHEMATIC_VERIFICATION_REPORT.md`
- `_verification/VISUAL_CHECK_REPORT.md`
- `_verification/schematic_visual/CLOSE_UP_REVIEW.md`
- `reports/SCHEMATIC_SAFE_REPAIR_ERC.rpt`
- `reports/SCHEMATIC_SAFE_REPAIR_ANNOTATION_CHECK.md`
- `reports/SCHEMATIC_SAFE_REPAIR_BOM_LOCK_ALIGNMENT_CHECK.md`
- `reports/SCHEMATIC_SAFE_REPAIR_NEEDS_REVIEW_MARKER_CHECK.md`

## Open Blockers

- 43 physical symbols still have blank footprint fields.
- BOM lock input is still missing.
- `NEEDS_REVIEW` and `BLOCKED` markers remain on high-risk parts and schematic notes.
- Footprint/package drawings, connector orientation, polarity review, USB policy, and human review are incomplete.

## Required Resolution

Do not update PCB from schematic until the schematic-to-PCB gate is explicitly `PASS`.
