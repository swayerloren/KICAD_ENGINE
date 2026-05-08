# ESP32_CSI_WIFI_NODE Schematic-Only Audit Report

Generated: 2026-05-06
Mode: strict read-only schematic audit
Schematic: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
Project: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro`

## Final Result

Result: `FAIL`

The schematic is not ready for PCB update. ERC is clean, but the schematic remains blocked by missing footprint assignments, missing datasheet fields, unresolved `NEEDS_REVIEW` markers, missing BOM-lock evidence, and incomplete close-up visual review.

PCB update status: `BLOCKED`

## Evidence Files

- Annotation check: `reports/SCHEMATIC_AUDIT_ONLY_ANNOTATION_CHECK.md`
- Completeness check: `reports/SCHEMATIC_AUDIT_ONLY_COMPLETENESS_CHECK.md`
- BOM alignment check: `reports/SCHEMATIC_AUDIT_ONLY_BOM_LOCK_ALIGNMENT_CHECK.md`
- NEEDS_REVIEW marker check: `reports/SCHEMATIC_AUDIT_ONLY_NEEDS_REVIEW_MARKER_CHECK.md`
- ERC report: `reports/SCHEMATIC_AUDIT_ONLY_ERC.rpt`
- Full-page SVG: `_verification/schematic_audit_only/full_page/ESP32_CSI_WIFI_NODE.svg`
- Full-page PDF: `_verification/schematic_audit_only/full_page/ESP32_CSI_WIFI_NODE.pdf`
- Close-up review: `reports/SCHEMATIC_AUDIT_ONLY_CLOSE_UP_REVIEW.md`
- Close-up crops: `_verification/schematic_audit_only/crops/`

## Annotation Result

Annotation result: `PASS_WITH_BLOCKERS`

The schematic parser found 79 symbol instances and 43 physical symbols. No actual symbol instance references ending in `?` were found for the requested prefixes `C`, `R`, `U`, `D`, `SW`, `J`, `TP`, `MH`, `F`, `Q`, `L`, or `Y`.

Automated annotation checker result: `FAIL`

Reason: annotation itself is complete, but the same gate also checks layout-critical fields. It reported:

- 158 pass findings.
- 43 warnings for physical symbols missing `Datasheet` fields.
- 43 failures for physical symbols with no footprint assigned.
- 1 failure for high-risk regulator `U1` lacking an explicit verification marker.

## Duplicate Reference Result

Duplicate reference result: `PASS`

Using the shared schematic checker parser, actual symbol instances had no duplicate references. A raw text search of the `.kicad_sch` overcounts library-symbol definitions and is not used as the authoritative duplicate-reference result.

## Reference Prefix Result

Reference prefix result: `PASS`

No category mismatch candidates were reported by the schematic checker for physical symbols. Physical references found:

`J1, F1, Q1, D1, C1, U1, L1, C2, C3, C4, C5, U2, C6, C7, R1, C8, SW1, R2, SW2, J2, R3, R4, R5, U3, R6, R7, R8, D2, R9, D3, TP1, TP2, TP3, TP4, TP5, TP6, TP7, TP8, TP9, MH1, MH2, MH3, MH4`

## Value / MPN Result

Value/MPN result: `FAIL`

The schematic has no blank values, but many values intentionally remain non-final or review-marked because the required project BOM-lock files are missing from the expected root paths:

- `PRE_SCHEMATIC_BOM_LOCK.md`: missing.
- `SCHEMATIC_READY_PARTS_LIST.md`: missing.
- `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`: missing.

The BOM alignment checker result is `FAIL` because no BOM lock path was available. Values that remain explicitly unresolved include:

- `J1`: `5.5x2.1_CENTER_POSITIVE_NEEDS_REVIEW`
- `F1`: `PTC_HOLD_CURRENT_NEEDS_REVIEW`
- `Q1`: `AO3401A_CLASS_PMOS_PINMAP_BLOCKED_NEEDS_REVIEW`
- `D1`: `5V_TVS_NEEDS_REVIEW`
- `C1`: `47uF_>=16V_BULK_NEEDS_REVIEW`
- `L1`: `3.9uH_NEEDS_REVIEW_MPN`
- `J2`: `USB_C_RECEPTACLE_USB2_NEEDS_REVIEW`
- `R3`: `0R_DNI_SHIELD_BLOCKED_NEEDS_REVIEW`
- `U3`: `TPD2EUSB30_OR_EQ_NEEDS_REVIEW`
- `R6`: `22R_USB_D-_NEEDS_REVIEW`
- `R7`: `22R_USB_D+_NEEDS_REVIEW`
- `MH1` through `MH4`: `M2.5_NPTH_2.7mm_NEEDS_REVIEW`
- `STATUS_LED_GPIO_NEEDS_REVIEW` net label/text note.
- USB VBUS and shield policy notes marked `BLOCKED_NEEDS_REVIEW`.

## Footprint Assignment Result

Footprint assignment result: `FAIL`

All 43 physical schematic symbols have blank footprint fields. This blocks PCB update from schematic. No footprint is accepted as package-verified by this audit.

High-risk footprint blockers:

- `J1` barrel jack: exact manufacturer part and mechanical drawing required.
- `Q1` AO3401A-class PMOS: source/gate/drain symbol-to-footprint mapping and package orientation are blocked.
- `D1` 5 V TVS: exact package and polarity/orientation require verification.
- `U1` AP63203WU regulator: exact package footprint, thermal notes, and verification status required.
- `U2` ESP32-S3-WROOM-1U-N16R8: exact module footprint and 1 vs 1U equivalence require verification.
- `J2` USB-C receptacle: exact connector MPN, footprint drawing, shell pins, and orientation require verification.
- `U3` USB ESD: exact MPN/package/pin mapping require verification.
- `MH1` through `MH4`: final mounting-hole drill, plated status, and mechanical placement require review.

## ERC Result

ERC result: `PASS`

Command:

`kicad-cli sch erc --output 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_AUDIT_ONLY_ERC.rpt --format report --severity-all 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

Result:

- `Found 0 violations`
- Report summary: `0 Errors 0 Warnings`

This ERC pass does not clear footprint, BOM, visual, connector, polarity, or human-review blockers.

## Completeness Result

Completeness result: `WARN`

The completeness checker found required schematic blocks present:

- Power input.
- Protection.
- Regulator.
- MCU/module.
- USB-C section.
- ESD.
- Boot/reset.
- Test pads.
- Mounting holes.
- Project/mechanical notes.

Warning: no BOM lock was provided, so completeness cannot prove all intended BOM items are present.

## Visual Export Result

Full-page export result: `PASS_WITH_LIMITATIONS`

Generated:

- `_verification/schematic_audit_only/full_page/ESP32_CSI_WIFI_NODE.svg`
- `_verification/schematic_audit_only/full_page/ESP32_CSI_WIFI_NODE.pdf`

The close-up generator produced 13 SVG crops and 13 PNG crops. The close-up review report still shows `Full-page PNG: NOT_AVAILABLE`; the SVG/PDF full-page exports exist, and PNG crops exist.

## Close-Up Visual Result By Block

Close-up visual review result: `FAIL`

| Block | Result | Notes |
| --- | --- | --- |
| 5V input / barrel jack / fuse | `FAIL` | Visible `Datasheet` and footprint/library-field risks detected. Human visual result still `NOT_REVIEWED`. |
| Reverse polarity PMOS | `FAIL` | Visible `Datasheet` and footprint/library-field risks detected. Human visual result still `NOT_REVIEWED`. |
| TVS / input capacitor | `PASS_NEEDS_HUMAN_REVIEW` | No visible unannotated refs or field risks detected, but human visual result is still `NOT_REVIEWED`. |
| Buck regulator | `PASS_NEEDS_HUMAN_REVIEW` | No visible unannotated refs or field risks detected, but human visual result is still `NOT_REVIEWED`. |
| ESP32 module | `PASS_NEEDS_HUMAN_REVIEW` | No visible unannotated refs or field risks detected, but human visual result is still `NOT_REVIEWED`. |
| USB-C connector | `FAIL` | Visible footprint field risk detected. Human visual result still `NOT_REVIEWED`. |
| USB ESD diode | `PASS_NEEDS_HUMAN_REVIEW` | No visible unannotated refs or field risks detected, but human visual result is still `NOT_REVIEWED`. |
| CC resistors | `WARN` | Crop generated, but text extraction found no visible text; crop coordinates likely need adjustment. |
| Reset / boot | `WARN` | Crop generated, but text extraction found no visible text; crop coordinates likely need adjustment. |
| LEDs | `WARN` | Crop generated, but text extraction found no visible text; crop coordinates likely need adjustment. |
| Test pads | `WARN` | Crop generated, but text extraction found no visible text; crop coordinates likely need adjustment. |
| Mounting holes / mechanical | `PASS_NEEDS_HUMAN_REVIEW` | No visible unannotated refs or field risks detected, but human visual result is still `NOT_REVIEWED`. |
| Mechanical notes | `PASS_NEEDS_HUMAN_REVIEW` | No visible unannotated refs or field risks detected, but human visual result is still `NOT_REVIEWED`. |

## Text / Value / Reference / Net-Label Overlap Result

Overlap result: `NEEDS_HUMAN_REVIEW`

Automated SVG text heuristic found 78 near-coordinate text collisions. Several are expected KiCad symbol/power-label render overlaps or repeated rendered text, but some indicate likely readability problems. Examples include:

- `#PWR39` overlapping `3V3`.
- `2.2k_PWR_LED` near `#PWR35`.
- `#PWR28` near `10k_BOOT_PULLUP`.
- `GND` near `#PWR20`.

Because this is a heuristic, it is not a final visual judgment. The generated close-up crops must be inspected manually or with a stronger visual workflow before schematic freeze.

## Power Rail Naming Result

Power rail naming result: `PASS_RELATIVE_TO_CURRENT_PROJECT_NOTES`

The schematic labels include `+5V_IN`, `+5V_FUSED`, and `+5V_PROTECTED`. The previous mismatch using `/5V_RAW`, `/5V_FUSED`, and `+5V` was not present in the current parsed label set.

## Unresolved NEEDS_REVIEW Items

Needs-review result: `FAIL`

Automated unresolved marker check:

- 15 unresolved review markers on symbols.
- 10 unresolved review markers in schematic text notes.
- 1 high-risk symbol without explicit review marker (`U1` regulator).
- 1 warning that unresolved review markers must block schematic-to-PCB gate.

Primary blockers:

- Exact MPNs and source links are not locked for multiple physical parts.
- All physical footprints are blank.
- Datasheet fields are missing on all physical parts.
- AO3401A-class PMOS pin mapping and footprint orientation remain blocked.
- USB VBUS/backfeed policy remains blocked.
- USB shield/EMC policy remains blocked.
- USB-C connector exact MPN/footprint/orientation remains unresolved.
- ESP32-S3-WROOM-1U module footprint equivalence remains unresolved.
- Regulator passives and inductor MPN/derating remain unresolved.
- Mounting-hole and enclosure-dependent mechanical details remain unresolved.
- Status LED GPIO selection remains unresolved.
- Optional USB D+/D- test stub policy remains unresolved.

## Safe Automatic Repair Assessment

Safe to repair automatically: `PARTIAL`

Safe low-risk schematic repairs, after a backup and explicit edit task:

- Add explicit `Verification_Status` fields where the value already states `NEEDS_REVIEW` or `BLOCKED`.
- Hide visible `Footprint` and `Datasheet` fields from normal schematic view without assigning footprints.
- Improve crop block coordinates in `visual_blocks.json`.
- Add or update report notes to carry unresolved blockers.

Not safe to repair automatically without source/human review:

- Assigning footprints.
- Selecting exact connector MPNs.
- Resolving AO3401A pin mapping.
- Resolving USB VBUS/backfeed policy.
- Resolving USB shield/EMC policy.
- Declaring ESP32-S3-WROOM-1U footprint equivalence.
- Declaring mounting-hole size/position final.
- Locking BOM values and supplier/MPN choices.

## PCB Update Gate

PCB update is blocked.

Do not update PCB from schematic until:

- Annotation gate passes without field/footprint blockers.
- BOM lock exists and alignment passes.
- All physical footprints are assigned and package-verified or explicitly human-approved.
- Datasheet/source fields exist or are explicitly link-only/unverified.
- ERC remains clean.
- Close-up visual review passes with human or AI visual evidence.
- All high-risk `NEEDS_REVIEW`/`BLOCKED` items are resolved or formally accepted by human review.
