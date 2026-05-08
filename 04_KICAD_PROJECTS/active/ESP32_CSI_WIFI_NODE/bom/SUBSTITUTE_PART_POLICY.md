# ESP32_CSI_WIFI_NODE Substitute Part Policy

Date: 2026-05-07

Mode: `READ_ONLY`

Final classification: `BOM_BLOCKED`

## Global Rules

- Substitutes are not allowed for high-risk parts unless exact drawing, pinout, package, electrical, thermal, mechanical, and orientation evidence is reviewed.
- Supplier package names, JLC/LCSC category text, and generic KiCad footprint names are not substitute approval.
- Any substitute that changes package, pinout, height, polarity marking, current rating, RF behavior, USB capacitance, thermal behavior, or mechanical fit requires human review.
- Stock-driven substitutions must be reviewed at order time with source date and source URL or user-provided supplier CSV.

## Substitute Policy By Part Class

| Part class | Refs | Substitute allowed | Required review |
|---|---|---:|---|
| ESP32-S3-WROOM-1U module | `U2` | `NO_BY_DEFAULT` | Exact Espressif order code, flash/PSRAM config, footprint, keepout, U.FL/pigtail mechanical clearance. |
| USB-C connector | `J2` | `NO_BY_DEFAULT` | Exact drawing, pin numbering, shell tabs, board-edge geometry, mating plug/enclosure clearance. |
| Barrel jack | `J1` | `NO_BY_DEFAULT` | Exact drawing, pin numbering, switched contacts, current rating, edge direction, plug clearance. |
| PMOS reverse polarity | `Q1` | `NO_BY_DEFAULT` | Source/gate/drain mapping, Vgs/Vds/Rds(on), body diode direction, SOT-23 pad numbering. |
| Buck regulator | `U1` | `NO_BY_DEFAULT` | Pinout, package, thermal behavior, switching frequency/control mode, compensation/stability requirements. |
| Buck inductor | `L1` | `CONDITIONAL` | Inductance, saturation current, RMS current, DCR, shielded type, size, height, thermal behavior. |
| USB ESD array | `U3` | `NO_BY_DEFAULT` | Pinout, flow-through orientation, capacitance, IEC rating, package, USB routing constraints. |
| TVS diode | `D1` | `CONDITIONAL_STRICT` | Standoff voltage, clamp voltage, unidirectional/bidirectional choice, polarity, package, surge rating. |
| PTC fuse | `F1` | `CONDITIONAL` | Hold/trip current, voltage rating, resistance, temperature derating, package, fault behavior. |
| LEDs | `D2`, `D3` | `CONDITIONAL` | Color, forward voltage, brightness, polarity mark, package, resistor current, enclosure visibility. |
| Switches | `SW1`, `SW2` | `NO_BY_DEFAULT` | Footprint drawing, actuator direction, height, force, enclosure access. |
| USB CC / series resistors | `R4-R7` | `CONDITIONAL` | Value, tolerance, package, placement; CC resistors should be correct USB-C Rd value. |
| General resistors | `R1`, `R2`, `R8`, `R9` | `YES_WITH_CONSTRAINTS` | Value, tolerance, power rating, package, assembly availability. |
| MLCC capacitors | `C2-C8` | `YES_WITH_CONSTRAINTS` | Capacitance after DC bias, voltage rating, dielectric, package, regulator stability or reset timing impact. |
| Bulk input capacitor | `C1` | `CONDITIONAL_STRICT` | Capacitance, voltage, ESR, ripple/inrush, polarity if applicable, package/height. |
| Test pads | `TP1-TP9` | `YES_WITH_LAYOUT_REVIEW` | Pad size, probe access, no USB stub harm for `TP8/TP9`. |
| Mounting holes | `MH1-MH4` | `NO_WITHOUT_MECHANICAL_REVIEW` | Screw size, NPTH/PTH intent, standoff/washer/copper keepout, enclosure fit. |

## Current Substitute Decision

No production substitutions are approved.

Reason: exact part and package evidence is incomplete, no PCB exists, and the high-risk footprint/orientation review is still open.
