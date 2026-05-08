# ESP32_CSI_WIFI_NODE JLCPCB Assembly BOM Status

Date: 2026-05-07

Mode: `READ_ONLY`

Final classification: `BOM_BLOCKED`

## JLCPCB Assembly Status

| Gate | Status | Evidence |
|---|---:|---|
| Assembly strategy selected | `NO` | No PCB-only/JLC assembly/mixed manual strategy is locked. |
| JLC/LCSC part numbers assigned | `NO` | Production BOM review has `UNKNOWN` JLC/LCSC for every purchased part. |
| BOM complete for upload | `NO` | Exact MPNs and packages are missing for multiple parts. |
| CPL/pick-place available | `NO` | No PCB exists, so no placement/side/rotation/origin data exists. |
| DNP/manual-solder scope complete | `NO` | R3/TP8/TP9 are policy candidates, but final DNP/DNI and manual-solder scope is not locked. |
| High-risk orientation ready | `NO` | PMOS, TVS, USB ESD, connectors, LEDs, switches, regulator, and module remain review-required. |
| JLCPCB assembly ready | `NO` | BOM and PCB are blocked. |

## JLC/LCSC Status By Group

| Group | Refs | JLC/LCSC status | Assembly risk |
|---|---|---:|---|
| MCU/RF module | `U2` | `UNKNOWN` | High; module availability, footprint, RF/mechanical clearance, and assembly handling need review. |
| USB-C connector | `J2` | `UNKNOWN` | High; exact suffix, footprint, orientation, and edge alignment need review. |
| Barrel jack | `J1` | `UNKNOWN` | High; likely manual/through-hole or special assembly review. |
| Power protection | `F1`, `Q1`, `D1`, `C1` | `UNKNOWN` | High; exact MPN/package/polarity/pinout incomplete. |
| Buck regulator group | `U1`, `L1`, `C2-C5` | `UNKNOWN` | High; regulator exact package, inductor, and capacitor derating/stability incomplete. |
| ESP32 support | `C6`, `C7`, `R1`, `C8`, `R2`, `SW1`, `SW2` | `UNKNOWN` | High for switches and C8; medium for passives after package lock. |
| USB support | `R3-R7`, `U3`, `TP8`, `TP9` | `UNKNOWN` | High for U3 and TP8/TP9 USB stubs; R3 DNI policy open. |
| LEDs | `D2`, `D3`, `R8`, `R9` | `UNKNOWN` | Medium/high; exact LED MPN/color/polarity and current not locked. |
| Test pads | `TP1-TP9` | `NOT_ASSEMBLY_PART` | Exclude from assembly BOM/CPL unless a specific assembly note requires otherwise. |
| Mounting holes | `MH1-MH4` | `NOT_ASSEMBLY_PART` | Exclude from assembly BOM/CPL; define mechanical drill intent in PCB files. |

## Assembly BOM Requirements Before Upload

1. Decide assembly mode: PCB-only, JLC top-side assembly, JLC two-side assembly, or mixed manual-solder.
2. Select exact MPN and package for all purchased parts.
3. Add JLC/LCSC part numbers from an official/current source or user-provided CSV.
4. Mark manual-solder and DNP/DNI parts explicitly.
5. Exclude test pads and mounting holes from assembly BOM/CPL.
6. Generate CPL only after actual PCB placement exists.
7. Verify every polarized/asymmetric part in the JLCPCB assembly preview.

Final result: `BOM_BLOCKED`
