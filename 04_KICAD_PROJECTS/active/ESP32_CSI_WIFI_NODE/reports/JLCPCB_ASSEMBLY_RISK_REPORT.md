# ESP32_CSI_WIFI_NODE JLCPCB Assembly Risk Report

Date: 2026-05-07

Mode: `READ_ONLY`

Assembly package generated: `NO`

Final assembly classification: `ASSEMBLY_BLOCKED`

## Assembly Strategy Status

| Item | Status | Finding |
|---|---:|---|
| JLCPCB assembly strategy selected | `NO` | No PCB-only versus JLC assembly versus mixed manual-solder strategy is recorded. |
| Side selection known | `NO` | No PCB placement exists, so top/bottom component side is unknown. |
| BOM complete for JLCPCB | `NO` | Current BOM lock is planning-only and exact MPN/package evidence is incomplete. |
| CPL complete for JLCPCB | `NO` | No PCB exists, so no X/Y/rotation/side data exists. |
| LCSC/JLC part availability verified | `NO` | No exact JLC/LCSC part-number review was performed; availability is time-sensitive. |
| DNP/manual-solder parts identified | `NO` | No final assembly scope exists. |
| Polarity/orientation marks verified | `NO` | No placement/silkscreen exists; high-risk parts remain review-blocked. |

## High-Risk Assembly Items

| Ref/Group | Risk | Status | Required action |
|---|---|---:|---|
| `J1` barrel jack | Exact part and edge/mechanical orientation unknown; likely not standard SMT assembly. | `BLOCKED` | Select exact MPN, verify footprint drawing, decide manual solder or assembly handling. |
| `J2` USB-C | Connector suffix, footprint, shell tabs, edge alignment, and rotation risk. | `BLOCKED` | Verify exact GCT USB4105 suffix or replacement; check JLCPCB assembly availability and preview. |
| `Q1` PMOS | SOT-23 pin-1/source-drain orientation can silently fail protection. | `BLOCKED` | Verify symbol/footprint/datasheet mapping and assembly rotation before production. |
| `D1` TVS | Polarity/package/marking risk. | `BLOCKED` | Verify unidirectional/bidirectional selection, cathode marking, and footprint. |
| `U1` regulator | TSOT-23-6/TSOT26 orientation and support layout risk. | `BLOCKED` | Verify exact package and JLC part availability; inspect assembly preview. |
| `L1` inductor | Exact MPN/package/height/current rating missing. | `BLOCKED` | Select shielded inductor and decide JLC assembly or manual placement. |
| `U2` ESP32-S3-WROOM-1U | Module package/land-pattern equivalence and RF connector clearance risk. | `BLOCKED` | Verify footprint and assembly handling; confirm whether JLCPCB can assemble selected module. |
| `U3` USB ESD | Exact package/pinout not selected; rotation can swap or short USB lines. | `BLOCKED` | Select exact ESD array and verify symbol, footprint, and JLC preview. |
| `SW1/SW2` | Exact tactile switch MPN and actuation orientation unknown. | `BLOCKED` | Select switches; verify footprint and enclosure access. |
| `D2/D3` LEDs | Exact LEDs missing; polarity and brightness unknown. | `BLOCKED` | Select LED MPN/color; verify footprint polarity and resistor current. |
| `C1/C2/C3/C4/C6/C8` | Package/voltage/derating decisions missing. | `BLOCKED` | Select package/voltage ratings and confirm JLC/LCSC availability if assembled. |
| `TP1-TP9` | Test pads may be non-assembly parts; USB stubs risky. | `BLOCKED` | Exclude from assembly BOM/CPL or mark correctly; review USB test pad policy. |
| `MH1-MH4` | Mounting holes are mechanical, not SMT placement parts. | `BLOCKED` | Ensure they are excluded from assembly BOM/CPL; define NPTH/PTH intent. |

## JLCPCB Assembly File Risks

| Risk | Status | Closure |
|---|---:|---|
| BOM/CPL reference mismatch | `BLOCKED_NO_FILES` | Generate BOM/CPL after PCB exists and ensure reference designators match exactly. |
| Duplicate BOM references | `BLOCKED_NO_FINAL_BOM` | Check final BOM for duplicate reference designators before upload. |
| Incorrect rotation/origin | `BLOCKED_NO_CPL` | Verify every polarized/asymmetric component in JLCPCB preview. |
| Bottom-side assembly cost/process surprise | `BLOCKED_NO_PLACEMENT` | Decide one-side or two-side assembly after placement. |
| Parts unavailable at order time | `BLOCKED_NO_LCSC_CHECK` | Verify JLC/LCSC stock and lifecycle immediately before order. |
| Manual-solder parts accidentally included | `BLOCKED_NO_ASSEMBLY_SCOPE` | Mark all manual/DNP parts explicitly and keep BOM/CPL consistent. |

## Assembly Recommendation

Do not use JLCPCB assembly yet. The safest next assembly-path decision, after the schematic and PCB gates are repaired, is:

1. Prefer top-side-only JLC assembly for small passives, regulator, USB ESD, PMOS, TVS, and LEDs only if exact JLC/LCSC parts and rotations are verified.
2. Treat barrel jack, ESP32 module, USB-C connector, switches, and any uncommon/mechanical parts as `NEEDS_JLC_AVAILABILITY_REVIEW` before deciding assembly versus manual solder.
3. Exclude mounting holes and non-assembled test pads from assembly BOM/CPL.
4. Verify JLCPCB online preview before approving production.

Final result: `ASSEMBLY_BLOCKED`
