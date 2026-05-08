# ESP32_CSI_WIFI_NODE BOM Production Blockers

Date: 2026-05-07

Mode: `READ_ONLY`

Final classification: `BOM_BLOCKED`

## Blocking Summary

| Blocker | Severity | Evidence |
|---|---:|---|
| No exact verified footprints | `CRITICAL` | `PRE_SCHEMATIC_BOM_LOCK.md` has `Exact drawing verified footprints: 0`. |
| Missing exact part selections | `CRITICAL` | `J1`, `L1`, `SW1`, `SW2`, `U3`, `D2`, `D3` are `BLOCKED_NO_EXACT_PART`. |
| Missing package decisions | `CRITICAL` | `C1`, `C2`, `C3`, `C4`, `C6`, `C8` are `BLOCKED_NO_PACKAGE`. |
| No JLC/LCSC part numbers | `HIGH` | No JLC/LCSC fields are locked for any purchased part. |
| No current stock/lifecycle evidence | `HIGH` | Supplier policy requires source date/source URL or user CSV for stock/lifecycle; none was reviewed. |
| High-risk orientation unresolved | `CRITICAL` | PMOS, TVS, USB ESD, USB-C, barrel jack, LEDs, switches, regulator, and ESP32 module require human review. |
| Assembly strategy not selected | `HIGH` | JLCPCB assembly versus manual-solder/DNP scope is open. |
| PCB does not exist | `CRITICAL` | No CPL, placement side, rotation, or footprint-on-board evidence can exist without PCB. |

## Minimum Fix List

1. Select exact orderable MPNs for all `BLOCKED_NO_EXACT_PART` rows.
2. Select package/voltage/height/derating for all `BLOCKED_NO_PACKAGE` rows.
3. Verify exact package drawings against candidate KiCad footprints.
4. Record official datasheet/source links and source dates for every production part.
5. Decide supplier path and add supplier SKUs.
6. If JLCPCB assembly is planned, add current JLC/LCSC part numbers and verify availability close to order time.
7. Decide DNP/DNI/manual-solder scope, especially `R3`, `TP8`, `TP9`, connectors, module, switches, test pads, and mounting holes.
8. Resolve polarity/orientation review for all high-risk parts.
9. Create PCB only after schematic-to-PCB gate passes, then generate CPL and verify placement rotations.

## Final Classification

`BOM_BLOCKED`
