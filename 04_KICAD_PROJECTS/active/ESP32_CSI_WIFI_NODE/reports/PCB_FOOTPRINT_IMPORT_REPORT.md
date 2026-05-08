# PCB Footprint Import Report

Project: ESP32_CSI_WIFI_NODE  
Date: 2026-05-07  
Scope: Phase 2 footprint presence check after Q1 PMOS pin mapping repair.

## Summary

Footprints on PCB: `43`

Missing footprints: `0`

Stale footprints: `0`

## Expected Footprints

All expected schematic references are present on the PCB:

`C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3, F1, J1, J2, L1, MH1, MH2, MH3, MH4, Q1, R1, R2, R3, R4, R5, R6, R7, R8, R9, SW1, SW2, TP1, TP2, TP3, TP4, TP5, TP6, TP7, TP8, TP9, U1, U2, U3`

## Q1 Footprint

Q1 footprint:

`Package_TO_SOT_SMD:SOT-23`

Q1 pad/net mapping after repair:

| Pad | Function | Net |
|---|---|---|
| `1` | Gate | `GND` |
| `2` | Source | `/+5V_PROTECTED` |
| `3` | Drain | `/+5V_FUSED` |

## Import / Sync Method

The PCB was synced from the schematic netlist using KiCad-supported `pcbnew` APIs:

- loaded existing PCB
- exported schematic KiCad XML netlist
- updated footprint schematic paths from netlist timestamps
- updated footprint pad nets from netlist nodes
- saved PCB

No footprints were final-placed. No routing, zones, or fabrication outputs were created.

## Classification

`FOOTPRINT_IMPORT_COMPLETE`

PCB sync parity blocker for Q1 is resolved.
