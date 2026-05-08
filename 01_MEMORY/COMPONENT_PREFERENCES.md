# Component Preferences

Durable component preferences and placeholder lists for KiCad projects. Add parts only after footprint, datasheet, sourcing, and lifecycle checks are complete.

## Preferred MCUs
- TBD.
- Record: part number, package, voltage, clocking, programming interface, lifecycle status, and verified footprint.

## Preferred CAN Transceivers
- TBD.
- Record: part number, supply voltage, bus fault rating, standby mode behavior, ESD rating, package, and verified footprint.

## Preferred Voltage Regulators
- TBD.
- Record: topology, input range, output voltage/current, thermal limits, efficiency, package, and verified footprint.

## Preferred Connectors
- TBD.
- Record: family, pitch, current rating, mating part, crimp/contact details, keying, retention, and verified footprint.

## Preferred Protection Parts
- TBD.
- Record: TVS diodes, fuses, resettable fuses, reverse-polarity devices, ESD arrays, filters, and verified footprints.

## Parts To Avoid
- TBD.
- Record: part number, reason to avoid, affected projects, and acceptable alternatives.

## Verified Footprints
- TBD.
- Record: symbol, footprint, part number, datasheet revision, verification date, and reviewer.

## Unverified Footprints
- TBD.
- Record: symbol, footprint, part number, concern, required check, and status.

## Components Observed In COMMAND LINK Reference

The following parts and footprints were observed in the read-only `COMMAND_LINK_VERIFIED_REFERENCE` review on 2026-04-30. They are not approved preferences yet. Promote any item only after datasheet, footprint, sourcing, lifecycle, and project-fit checks are complete.

- MCU observed: `STM32F103C8Tx` with `Package_QFP:LQFP-48_7x7mm_P0.5mm`.
- CAN transceiver observed: `SN65HVD230` with `Package_SO:SOIC-8_3.9x4.9mm_P1.27mm`.
- Low-side driver observed: `ULN2803A` with project footprint `IC_ULN2803ADW`; local review reported missing footprint library `ULN2803ADW`, so this footprint remains unverified in this workspace.
- Voltage regulator observed: `LMR16006YQ` with `Package_TO_SOT_SMD:SOT-23-6`.
- Protection/diode parts observed: `NUP2105L` with `Package_TO_SOT_SMD:SOT-23`, `D_Schottky` with `Diode_SMD:D_SMA`, `D_TVS` with `Diode_SMD:D_SMB`, and `15V` with `Diode_SMD:D_SMA`.
- Switching/power parts observed: `Q_PMOS_GDS` with `Package_TO_SOT_SMD:SOT-23` and `22uH` with `Inductor:L_6.3x6.3_H3`.
- Connector footprints observed: `Connector_PinHeader_1.27mm:PinHeader_1x06_P1.27mm_Vertical`, `TerminalBlock:TerminalBlock_Bornier-2_P5.08mm`, `Wire_2mm:SolderWire-2sqmm_1x06_P7.8mm_D2mm_OD3.9mm`, and `Wire_2mm:SolderWire-2sqmm_1x04_P7.8mm_D2mm_OD3.9mm`.
- Passive footprints observed: `Resistor_SMD:R_0805_2012Metric`, `Capacitor_SMD:C_0805_2012Metric`, `Capacitor_SMD:C_1210_3225Metric`, and `Capacitor_SMD:C_1206_3216Metric`.

## COMMAND LINK Unverified Footprint Notes

- `IC_ULN2803ADW` / `ULN2803ADW`: missing from the local library environment during ERC/DRC review. Do not reuse until the footprint source, dimensions, pin mapping, courtyard, and fabrication suitability are verified.
- Multiple footprints in the copied reference reported library footprint mismatches in local DRC. Treat those as review items before reuse; they may reflect library version drift or project-local footprint changes.
