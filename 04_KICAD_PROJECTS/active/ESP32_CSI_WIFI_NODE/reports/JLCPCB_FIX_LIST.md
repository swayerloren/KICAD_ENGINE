# ESP32_CSI_WIFI_NODE JLCPCB Fix List

Date: 2026-05-07

Mode: `READ_ONLY`

Final classification: `JLCPCB_REVIEW_BLOCKED`

## P0 - Must Fix Before Any JLCPCB Output

| ID | Fix | Evidence | Done |
|---|---|---|---:|
| JLC-P0-001 | Resolve schematic-to-PCB gate to exact `PASS`. | Current gate is `FAIL`; PCB update allowed is `NO`. | `NO` |
| JLC-P0-002 | Create/update PCB only after gate passes. | No `.kicad_pcb` exists. | `NO` |
| JLC-P0-003 | Verify exact package drawings and pin/orientation for all high-risk parts. | BOM lock has 0 exact verified footprints. | `NO` |
| JLC-P0-004 | Select exact MPN/package for blocked parts. | J1, L1, SW1, SW2, U3, D2, D3 are missing exact part selections; C1/C2/C3/C4/C6/C8 lack package decisions. | `NO` |
| JLC-P0-005 | Define JLCPCB order path: PCB-only, Economic PCBA, Standard PCBA, or mixed manual solder. | Assembly strategy is not recorded. | `NO` |

## P1 - Must Fix Before JLCPCB DFM/DFA Can Pass

| ID | Fix | Evidence | Done |
|---|---|---|---:|
| JLC-P1-001 | Create closed board outline on `Edge.Cuts`. | No board outline exists. | `NO` |
| JLC-P1-002 | Set JLCPCB-aware design rules for selected layer count and copper weight. | No PCB constraints exist. | `NO` |
| JLC-P1-003 | Add mounting holes with explicit NPTH/PTH intent and copper keepouts. | MH1-MH4 review remains open. | `NO` |
| JLC-P1-004 | Place USB-C and barrel jack using exact drawings and edge overhang clearance. | J1/J2 drawings and edge alignment unresolved. | `NO` |
| JLC-P1-005 | Route, refill zones, and run DRC. | DRC is `NOT_RUN_NO_PCB`; routing is blocked. | `NO` |
| JLC-P1-006 | Verify silkscreen over pads, solder-mask slivers, courtyards, copper-to-edge, annular rings, drills, and slots. | No PCB geometry exists. | `NO` |

## P2 - Must Fix Before JLCPCB Assembly

| ID | Fix | Evidence | Done |
|---|---|---|---:|
| JLC-P2-001 | Complete final BOM with exact MPNs and JLC/LCSC part numbers if assembly is planned. | Current BOM lock is planning-only. | `NO` |
| JLC-P2-002 | Generate CPL after placement and verify X/Y/side/rotation. | No PCB placement exists. | `NO` |
| JLC-P2-003 | Mark DNP/manual-solder parts and exclude non-assembly items from BOM/CPL. | Manual/JLC assembly scope is undecided. | `NO` |
| JLC-P2-004 | Verify orientation marks for PMOS, TVS, USB ESD, LEDs, USB-C, switches, regulator, ESP32 module. | Orientation risks remain open. | `NO` |
| JLC-P2-005 | Decide fiducials, edge rails, tooling holes, and panelization based on JLCPCB assembly type. | Assembly type and board outline are unknown. | `NO` |
| JLC-P2-006 | Review JLCPCB online assembly preview and resolve every rotation/origin warning. | No BOM/CPL package exists. | `NO` |

## Current Release Decision

JLCPCB review result: `JLCPCB_REVIEW_BLOCKED`

Gerbers may be generated now: `NO`

JLCPCB order may be placed now: `NO`
