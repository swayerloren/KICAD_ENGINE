# FOOTPRINT_PACKAGE_AUDIT

Status: `FOOTPRINT_AUDIT_FAIL`

Project: `ESP32_CSI_WIFI_NODE`

Audit date: 2026-05-03

Scope: strict footprint/package verification before any PCB update from schematic.

## Verdict

Final result: `FOOTPRINT_AUDIT_FAIL`

PCB update from schematic remains blocked.

Read-only schematic parsing found:

- Active project: `kicad/ESP32_CSI_WIFI_NODE.kicad_pro`
- Active schematic: `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
- Physical schematic symbols parsed: `43`
- Physical symbols with assigned footprint fields: `0`
- Physical symbols with populated datasheet fields: `0`
- Missing requested BOM lock file: `PRE_SCHEMATIC_BOM_LOCK.md`
- Missing requested ready-parts file: `SCHEMATIC_READY_PARTS_LIST.md`

Because no physical component has an assigned footprint and no schematic symbol has a populated datasheet field, no package-to-footprint match can be verified. Every component below is blocked as `UNASSIGNED_FOOTPRINT`.

## Rules Applied

- Every footprint must map to an exact part number and package drawing or land-pattern source.
- Connector footprints require exact manufacturer drawing, board-edge/mechanical orientation review, pin numbering review, and human review.
- Polarity-sensitive parts require symbol pin mapping, footprint pad mapping, and physical orientation review.
- A KiCad symbol name, default footprint name, clean ERC, or similar-looking part is not enough evidence.
- A 3D model can support mechanical review but cannot prove the footprint is correct.

## Component Footprint/Package Table

| Ref | Value | MPN | Symbol | Footprint | Package | Datasheet source | Footprint verification | Risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J1 | `5.5x2.1_CENTER_POSITIVE_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Connector:Barrel_Jack` | `UNASSIGNED` | `NEEDS_REVIEW exact barrel jack drawing` | `MISSING` | `FAIL - no footprint, package, or drawing evidence` | `HIGH mechanical/polarity` |
| F1 | `PTC_HOLD_CURRENT_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Device:Polyfuse` | `UNASSIGNED` | `NEEDS_REVIEW exact fuse package` | `MISSING` | `FAIL - no footprint, package, or rating evidence` | `HIGH protection/current` |
| Q1 | `AO3401A_CLASS_PMOS_PINMAP_BLOCKED_NEEDS_REVIEW` | `AO3401A-class, exact MPN NEEDS_REVIEW` | `Device:Q_PMOS` | `UNASSIGNED` | `NEEDS_REVIEW; do not assume SOT-23 without source` | `MISSING` | `FAIL - pin mapping and footprint orientation explicitly blocked` | `HIGH polarity/pinout` |
| D1 | `5V_TVS_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Device:D_TVS` | `UNASSIGNED` | `NEEDS_REVIEW exact TVS package` | `MISSING` | `FAIL - no polarity/package evidence` | `HIGH protection/polarity` |
| C1 | `47uF_>=16V_BULK_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Device:C` | `UNASSIGNED` | `NEEDS_REVIEW capacitor package and voltage rating` | `MISSING` | `FAIL - no footprint or derating evidence` | `MEDIUM polarity if electrolytic/tantalum selected` |
| U1 | `AP63203WU-7_3V3_2A` | `AP63203WU-7 from schematic value; source not verified` | `Regulator_Switching:AP63203WU` | `UNASSIGNED` | `NEEDS_REVIEW exact AP63203WU package/land pattern` | `MISSING` | `FAIL - no footprint or package drawing evidence` | `HIGH regulator/thermal/layout` |
| L1 | `3.9uH_NEEDS_REVIEW_MPN` | `NEEDS_REVIEW` | `Device:L` | `UNASSIGNED` | `NEEDS_REVIEW inductor package/current rating` | `MISSING` | `FAIL - no footprint or saturation-current evidence` | `HIGH power/thermal` |
| C2 | `10uF_CIN` | `NEEDS_REVIEW` | `Device:C` | `UNASSIGNED` | `NEEDS_REVIEW capacitor package/voltage` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM regulator input` |
| C3 | `22uF_COUT` | `NEEDS_REVIEW` | `Device:C` | `UNASSIGNED` | `NEEDS_REVIEW capacitor package/voltage` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM regulator output` |
| C4 | `22uF_COUT` | `NEEDS_REVIEW` | `Device:C` | `UNASSIGNED` | `NEEDS_REVIEW capacitor package/voltage` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM regulator output` |
| C5 | `100nF_CBST` | `NEEDS_REVIEW` | `Device:C` | `UNASSIGNED` | `NEEDS_REVIEW capacitor package/voltage` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM regulator bootstrap` |
| U2 | `ESP32-S3-WROOM-1U-N16R8` | `ESP32-S3-WROOM-1U-N16R8 from schematic value; source not verified` | `RF_Module:ESP32-S3-WROOM-1` | `UNASSIGNED` | `NEEDS_REVIEW Espressif module land pattern and 1 vs 1U equivalence` | `MISSING` | `FAIL - no module footprint, antenna/U.FL, or keepout evidence` | `HIGH RF/module/mechanical` |
| C6 | `10uF_MODULE_DECOUPLING` | `NEEDS_REVIEW` | `Device:C` | `UNASSIGNED` | `NEEDS_REVIEW capacitor package/voltage` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM module power` |
| C7 | `100nF_MODULE_DECOUPLING` | `NEEDS_REVIEW` | `Device:C` | `UNASSIGNED` | `NEEDS_REVIEW capacitor package/voltage` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM module power` |
| R1 | `10k_EN_PULLUP` | `NEEDS_REVIEW` | `Device:R` | `UNASSIGNED` | `NEEDS_REVIEW resistor package` | `MISSING` | `FAIL - no footprint evidence` | `LOW/MEDIUM boot/reset` |
| C8 | `1uF_EN_DELAY` | `NEEDS_REVIEW` | `Device:C` | `UNASSIGNED` | `NEEDS_REVIEW capacitor package/voltage` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM boot/reset` |
| SW1 | `RESET_EN` | `NEEDS_REVIEW` | `Switch:SW_Push` | `UNASSIGNED` | `NEEDS_REVIEW exact switch drawing` | `MISSING` | `FAIL - no footprint or actuator orientation evidence` | `HIGH mechanical/orientation` |
| R2 | `10k_BOOT_PULLUP` | `NEEDS_REVIEW` | `Device:R` | `UNASSIGNED` | `NEEDS_REVIEW resistor package` | `MISSING` | `FAIL - no footprint evidence` | `LOW/MEDIUM boot strap` |
| SW2 | `BOOT_GPIO0` | `NEEDS_REVIEW` | `Switch:SW_Push` | `UNASSIGNED` | `NEEDS_REVIEW exact switch drawing` | `MISSING` | `FAIL - no footprint or actuator orientation evidence` | `HIGH mechanical/orientation` |
| J2 | `USB_C_RECEPTACLE_USB2_NEEDS_REVIEW` | `NEEDS_REVIEW exact USB-C receptacle MPN` | `Connector:USB_C_Receptacle_USB2.0_14P` | `UNASSIGNED` | `NEEDS_REVIEW exact connector drawing and board-edge geometry` | `MISSING` | `FAIL - connector orientation and pin numbering cannot be verified` | `HIGH connector/mechanical/USB` |
| R3 | `0R_DNI_SHIELD_BLOCKED_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Device:R` | `UNASSIGNED` | `NEEDS_REVIEW resistor/jumper package` | `MISSING` | `FAIL - no footprint; shield policy blocked` | `HIGH EMC/USB shield` |
| R4 | `5.1k_CC1` | `NEEDS_REVIEW` | `Device:R` | `UNASSIGNED` | `NEEDS_REVIEW resistor package` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM USB-C CC` |
| R5 | `5.1k_CC2` | `NEEDS_REVIEW` | `Device:R` | `UNASSIGNED` | `NEEDS_REVIEW resistor package` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM USB-C CC` |
| U3 | `TPD2EUSB30_OR_EQ_NEEDS_REVIEW` | `TPD2EUSB30 or equivalent; exact suffix/package NEEDS_REVIEW` | `Power_Protection:TPD2EUSB30` | `UNASSIGNED` | `NEEDS_REVIEW exact ESD package and pinout` | `MISSING` | `FAIL - no ESD footprint, pin mapping, or placement evidence` | `HIGH USB ESD/pinout` |
| R6 | `22R_USB_D-_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Device:R` | `UNASSIGNED` | `NEEDS_REVIEW resistor package` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM USB signal placement` |
| R7 | `22R_USB_D+_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Device:R` | `UNASSIGNED` | `NEEDS_REVIEW resistor package` | `MISSING` | `FAIL - no footprint evidence` | `MEDIUM USB signal placement` |
| R8 | `2.2k_PWR_LED` | `NEEDS_REVIEW` | `Device:R` | `UNASSIGNED` | `NEEDS_REVIEW resistor package` | `MISSING` | `FAIL - no footprint evidence` | `LOW/MEDIUM LED current` |
| D2 | `PWR_LED` | `NEEDS_REVIEW` | `Device:LED` | `UNASSIGNED` | `NEEDS_REVIEW LED package and polarity` | `MISSING` | `FAIL - no footprint or polarity evidence` | `MEDIUM polarity/orientation` |
| R9 | `2.2k_STATUS_LED` | `NEEDS_REVIEW` | `Device:R` | `UNASSIGNED` | `NEEDS_REVIEW resistor package` | `MISSING` | `FAIL - no footprint evidence` | `LOW/MEDIUM LED current` |
| D3 | `STATUS_LED_SIMPLE` | `NEEDS_REVIEW` | `Device:LED` | `UNASSIGNED` | `NEEDS_REVIEW LED package and polarity` | `MISSING` | `FAIL - no footprint or polarity evidence` | `MEDIUM polarity/orientation` |
| TP1 | `+5V_PROTECTED` | `NEEDS_REVIEW` | `Connector:TestPoint` | `UNASSIGNED` | `NEEDS_REVIEW test pad style/size` | `MISSING` | `FAIL - no test pad footprint evidence` | `MEDIUM test access/mechanical` |
| TP2 | `3V3` | `NEEDS_REVIEW` | `Connector:TestPoint` | `UNASSIGNED` | `NEEDS_REVIEW test pad style/size` | `MISSING` | `FAIL - no test pad footprint evidence` | `MEDIUM test access/mechanical` |
| TP3 | `GND` | `NEEDS_REVIEW` | `Connector:TestPoint` | `UNASSIGNED` | `NEEDS_REVIEW test pad style/size` | `MISSING` | `FAIL - no test pad footprint evidence` | `MEDIUM test access/mechanical` |
| TP4 | `EN` | `NEEDS_REVIEW` | `Connector:TestPoint` | `UNASSIGNED` | `NEEDS_REVIEW test pad style/size` | `MISSING` | `FAIL - no test pad footprint evidence` | `MEDIUM test access/mechanical` |
| TP5 | `BOOT_GPIO0` | `NEEDS_REVIEW` | `Connector:TestPoint` | `UNASSIGNED` | `NEEDS_REVIEW test pad style/size` | `MISSING` | `FAIL - no test pad footprint evidence` | `MEDIUM test access/mechanical` |
| TP6 | `U0TXD_GPIO43` | `NEEDS_REVIEW` | `Connector:TestPoint` | `UNASSIGNED` | `NEEDS_REVIEW test pad style/size` | `MISSING` | `FAIL - no test pad footprint evidence` | `MEDIUM test access/mechanical` |
| TP7 | `U0RXD_GPIO44` | `NEEDS_REVIEW` | `Connector:TestPoint` | `UNASSIGNED` | `NEEDS_REVIEW test pad style/size` | `MISSING` | `FAIL - no test pad footprint evidence` | `MEDIUM test access/mechanical` |
| TP8 | `USB_D+_OPTIONAL_STUB_REVIEW` | `NEEDS_REVIEW` | `Connector:TestPoint` | `UNASSIGNED` | `NEEDS_REVIEW USB test pad/stub policy` | `MISSING` | `FAIL - no test pad footprint or USB stub evidence` | `MEDIUM USB signal integrity` |
| TP9 | `USB_D-_OPTIONAL_STUB_REVIEW` | `NEEDS_REVIEW` | `Connector:TestPoint` | `UNASSIGNED` | `NEEDS_REVIEW USB test pad/stub policy` | `MISSING` | `FAIL - no test pad footprint or USB stub evidence` | `MEDIUM USB signal integrity` |
| MH1 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Mechanical:MountingHole` | `UNASSIGNED` | `NEEDS_REVIEW mounting hole/mechanical stackup` | `MISSING` | `FAIL - no mounting-hole footprint evidence` | `HIGH mechanical fit` |
| MH2 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Mechanical:MountingHole` | `UNASSIGNED` | `NEEDS_REVIEW mounting hole/mechanical stackup` | `MISSING` | `FAIL - no mounting-hole footprint evidence` | `HIGH mechanical fit` |
| MH3 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Mechanical:MountingHole` | `UNASSIGNED` | `NEEDS_REVIEW mounting hole/mechanical stackup` | `MISSING` | `FAIL - no mounting-hole footprint evidence` | `HIGH mechanical fit` |
| MH4 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `NEEDS_REVIEW` | `Mechanical:MountingHole` | `UNASSIGNED` | `NEEDS_REVIEW mounting hole/mechanical stackup` | `MISSING` | `FAIL - no mounting-hole footprint evidence` | `HIGH mechanical fit` |

## Specific High-Risk Audit

### USB-C Connector

- Ref: `J2`
- Schematic symbol: `Connector:USB_C_Receptacle_USB2.0_14P`
- Exact manufacturer MPN: `NEEDS_REVIEW`
- Assigned footprint: `UNASSIGNED`
- Package drawing: `MISSING`
- Pin numbering/orientation review: `BLOCKED`
- 3D model check: `NOT_CHECKABLE_NO_FOOTPRINT`
- Result: `FAIL`

The USB-C connector cannot be approved until an exact connector part number, manufacturer mechanical drawing, KiCad footprint, shell-pad policy, board-edge location, pin numbering match, and human orientation review are complete.

### AO3401A PMOS

- Ref: `Q1`
- Schematic symbol: `Device:Q_PMOS`
- Exact MPN: `AO3401A-class, exact source not verified`
- Assigned footprint: `UNASSIGNED`
- Symbol pin mapping: `BLOCKED`
- Package drawing: `MISSING`
- 3D model check: `NOT_CHECKABLE_NO_FOOTPRINT`
- Result: `FAIL`

The PMOS cannot be approved until the exact device datasheet, pin numbering, body diode orientation, KiCad symbol pins, and footprint pads are matched.

### ESP32-S3 Module

- Ref: `U2`
- Schematic value: `ESP32-S3-WROOM-1U-N16R8`
- Schematic symbol: `RF_Module:ESP32-S3-WROOM-1`
- Assigned footprint: `UNASSIGNED`
- Espressif land pattern source: `MISSING`
- WROOM-1 vs WROOM-1U footprint equivalence: `NEEDS_REVIEW`
- Antenna/U.FL and keepout review: `NEEDS_REVIEW`
- 3D model check: `NOT_CHECKABLE_NO_FOOTPRINT`
- Result: `FAIL`

The module cannot be approved until the exact Espressif module drawing and KiCad footprint are matched. The `1U` external antenna variant also needs RF connector and mechanical review.

### USB ESD Diode

- Ref: `U3`
- Schematic value: `TPD2EUSB30_OR_EQ_NEEDS_REVIEW`
- Assigned footprint: `UNASSIGNED`
- Exact suffix/package: `NEEDS_REVIEW`
- Pin mapping: `NEEDS_REVIEW`
- Placement/orientation: `NEEDS_REVIEW`
- 3D model check: `NOT_CHECKABLE_NO_FOOTPRINT`
- Result: `FAIL`

### AP63203 Regulator

- Ref: `U1`
- Schematic value: `AP63203WU-7_3V3_2A`
- Assigned footprint: `UNASSIGNED`
- Package drawing: `MISSING`
- Thermal/layout review: `NEEDS_REVIEW`
- Inductor/capacitor footprint/derating: `NEEDS_REVIEW`
- 3D model check: `NOT_CHECKABLE_NO_FOOTPRINT`
- Result: `FAIL`

### Barrel Jack

- Ref: `J1`
- Assigned footprint: `UNASSIGNED`
- Exact connector MPN/drawing: `NEEDS_REVIEW`
- Center-positive polarity/mechanical orientation: `NEEDS_REVIEW`
- 3D model check: `NOT_CHECKABLE_NO_FOOTPRINT`
- Result: `FAIL`

### PTC Fuse

- Ref: `F1`
- Assigned footprint: `UNASSIGNED`
- Exact hold/trip/current/package source: `NEEDS_REVIEW`
- Result: `FAIL`

### TVS Diode

- Ref: `D1`
- Assigned footprint: `UNASSIGNED`
- Exact package/polarity/source: `NEEDS_REVIEW`
- Result: `FAIL`

### Test Pads

- Refs: `TP1` through `TP9`
- Assigned footprints: `UNASSIGNED`
- Pad size, soldermask, accessibility, and USB stub policy: `NEEDS_REVIEW`
- Result: `FAIL`

### Mounting Holes

- Refs: `MH1` through `MH4`
- Assigned footprints: `UNASSIGNED`
- Hole diameter, plating, clearance, screw hardware, enclosure fit, and keepout: `NEEDS_REVIEW`
- Result: `FAIL`

## Connector Orientation And Pin Numbering Risk

Connector-related items are blocked:

- `J1` barrel jack has no exact part number, footprint, polarity/mechanical drawing, or 3D model evidence.
- `J2` USB-C connector has no exact part number, footprint, pin numbering review, shell-pad strategy, board-edge placement, or 3D model evidence.
- `TP1`-`TP9` test pads have no selected pad footprint or placement/access policy.
- `MH1`-`MH4` mounting holes have no selected footprint or mechanical clearance review.

Result: `CONNECTOR_ORIENTATION_REVIEW_FAIL`

## Polarity/Orientation-Sensitive Parts

The following parts require source-backed orientation review before layout:

- `Q1` PMOS body diode, source/drain/gate pin mapping, and SOT/package orientation if selected.
- `D1` TVS diode polarity and package orientation.
- `D2` and `D3` LED polarity and footprint orientation.
- `U1` regulator pinout and exposed/thermal pad requirements if applicable.
- `U3` USB ESD diode pinout and USB line orientation.
- `J1` barrel jack center-positive polarity and switched/contact pin behavior if applicable.
- `J2` USB-C plug orientation, duplicate pins, shield tabs, and board-edge orientation.
- `C1` if a polarized capacitor technology is selected.

Result: `POLARITY_ORIENTATION_REVIEW_FAIL`

## 3D Model Check

3D model verification could not be meaningfully performed because no footprints are assigned. A 3D model review is useful for:

- `J1` barrel jack
- `J2` USB-C connector
- `U2` ESP32-S3 module and U.FL/mechanical antenna path
- `SW1` and `SW2` pushbuttons
- `MH1`-`MH4` mounting holes
- Any tall power components or connectors selected later

Result: `NOT_CHECKABLE_NO_FOOTPRINTS_ASSIGNED`

## Required Before Footprint Audit Can Pass

Before this audit may become `FOOTPRINT_AUDIT_PASS`, the project needs:

1. Recovered or recreated BOM lock with exact MPNs or explicit `NEEDS_REVIEW` markers.
2. Populated schematic footprint fields for every physical component.
3. Datasheet/source links for every exact MPN or package selection.
4. Package drawing evidence for every footprint.
5. KiCad footprint path/name for every component.
6. Symbol pin to footprint pad mapping evidence for every IC, module, diode, transistor, connector, and polarity-sensitive part.
7. Exact USB-C connector MPN, drawing, footprint, pin numbering, shell policy, board-edge placement, and human orientation review.
8. Exact AO3401A-class PMOS device, pin mapping, body diode orientation, and footprint verification.
9. Exact ESP32-S3 module land pattern and `WROOM-1U` variant review.
10. Exact AP63203 package and regulator layout/thermal review.
11. Exact USB ESD device suffix/package/pinout review.
12. Exact barrel jack, PTC fuse, TVS diode, test pad, mounting-hole, and switch footprint decisions.

## PCB Gate Impact

This audit keeps `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` at `FAIL`.

Do not update PCB from schematic, place parts, route traces, create zones, or generate PCB manufacturing outputs until this audit is replaced by a passing source-backed footprint/package audit and the schematic-to-PCB gate is exactly `PASS`.

