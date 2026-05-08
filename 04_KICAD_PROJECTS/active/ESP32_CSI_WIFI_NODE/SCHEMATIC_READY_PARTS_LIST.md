# Schematic Ready Parts List

Project: `ESP32_CSI_WIFI_NODE`  
Date: `2026-05-06`  
Status: `NOT_READY_FOR_AUTOMATIC_FOOTPRINT_ASSIGNMENT`

This file summarizes whether each schematic physical component has enough evidence to be safely assigned a footprint in a future schematic edit pass.

## Result

- Physical parts parsed: `43`
- Ready for exact footprint assignment without human review: `0`
- Candidate available but human review required: `30`
- Blocked by no exact part: `7`
- Blocked by no package: `6`

## Ready Rules

A part is only `SCHEMATIC_READY_FOR_FOOTPRINT_ASSIGNMENT` when:

1. Exact MPN or accepted generic package decision is recorded.
2. Package/pad orientation is understood.
3. Candidate KiCad footprint is recorded.
4. High-risk review is either complete or explicitly accepted by LJ.

No current row meets all four conditions.

## Candidate But Human Review Required

These rows have plausible KiCad footprint candidates, but footprint assignment is not approved until LJ reviews package/orientation/policy details:

- `F1` - `Fuse:Fuse_1206_3216Metric`
- `Q1` - `Package_TO_SOT_SMD:SOT-23`
- `D1` - `Diode_SMD:D_SMA`
- `U1` - `Package_TO_SOT_SMD:TSOT-23-6`
- `C5` - `Capacitor_SMD:C_0603_1608Metric`
- `U2` - `RF_Module:ESP32-S3-WROOM-1`
- `C7` - `Capacitor_SMD:C_0603_1608Metric`
- `R1` - `Resistor_SMD:R_0603_1608Metric`
- `R2` - `Resistor_SMD:R_0603_1608Metric`
- `J2` - `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal`
- `R3` - `Resistor_SMD:R_0603_1608Metric`
- `R4` - `Resistor_SMD:R_0603_1608Metric`
- `R5` - `Resistor_SMD:R_0603_1608Metric`
- `R6` - `Resistor_SMD:R_0603_1608Metric`
- `R7` - `Resistor_SMD:R_0603_1608Metric`
- `R8` - `Resistor_SMD:R_0603_1608Metric`
- `R9` - `Resistor_SMD:R_0603_1608Metric`
- `TP1` through `TP9` - `TestPoint:TestPoint_Pad_D1.5mm`
- `MH1` through `MH4` - `MountingHole:MountingHole_2.7mm_M2.5`

## Blocked By Missing Exact Part

These rows need exact MPN or accepted final part selection before footprint assignment:

- `J1` - final 5.5 mm x 2.1 mm right-angle barrel jack not selected.
- `L1` - final 3.9 uH shielded inductor not selected.
- `SW1` - final reset tactile switch not selected.
- `SW2` - final boot tactile switch not selected.
- `U3` - final USB ESD orderable/package not selected.
- `D2` - final power LED color/package/MPN not selected.
- `D3` - final status LED color/package/MPN not selected.

## Blocked By Missing Package

These rows have values but no locked package/size:

- `C1` - 47 uF >=16 V bulk capacitor.
- `C2` - 10 uF buck input capacitor.
- `C3` - 22 uF buck output capacitor.
- `C4` - 22 uF buck output capacitor.
- `C6` - 10 uF ESP32 module bulk decoupling.
- `C8` - 1 uF EN delay capacitor.

## Human Review Required Before Schematic Edit

Human review is required before footprint assignment for:

- All connectors.
- All high-current/power path parts.
- All polarity-sensitive parts.
- PMOS source/gate/drain mapping.
- USB ESD package and pinout.
- ESP32 module package and WROOM-1U footprint equivalence.
- USB D+/D- optional test pads.
- Mounting holes and mechanical clearances.

## Decision

Schematic footprint assignment can safely proceed now: `NO`.

Recommended next action: LJ reviews `PRE_SCHEMATIC_BOM_LOCK.md` and chooses exact parts or accepts package defaults for blocked rows.
