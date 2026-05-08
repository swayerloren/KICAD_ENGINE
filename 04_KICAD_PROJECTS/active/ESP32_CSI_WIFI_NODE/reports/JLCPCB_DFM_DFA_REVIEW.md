# ESP32_CSI_WIFI_NODE JLCPCB DFM/DFA Review

Date: 2026-05-07

Mode: `READ_ONLY`

Gerbers generated: `NO`

Drills generated: `NO`

BOM/CPL generated: `NO`

Final classification: `JLCPCB_REVIEW_BLOCKED`

## Evidence Reviewed

- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `24_FAB_PROFILES/JLCPCB/README.md`: `MISSING`
- `24_FAB_PROFILES/00_INDEX/FAB_PROFILE_SCHEMA.md`
- `reports/FINAL_PCB_AUDIT_BEFORE_FAB.md`
- `reports/PRODUCTION_RISK_REGISTER.md`
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `Test-Path kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`: `False`

## JLCPCB Reference Points Used

Because the local JLCPCB profile README is missing, this review used current official JLCPCB help/capability pages as external reference evidence:

- JLCPCB copper-weight guide: 1 oz 1-2 layer FR4 minimum trace/space is 0.10 mm; 2 oz FR4 minimum trace/space is 0.16 mm; heavier copper requires wider rules.
- JLCPCB ordering guide: solder-mask bridges usually need at least 0.2 mm pad/pin spacing on 1-2 layer boards and 0.1 mm on multilayer boards.
- JLCPCB tooling-hole guide: Economic PCBA tooling holes are required; JLCPCB specifies 1.152 mm round NPTH tooling holes with solder-mask expansion guidance.
- JLCPCB edge-rail/fiducial guide: Standard PCB Assembly requires edge rails and fiducials; edge rails are at least 5 mm; fiducials use exposed copper with solder-mask opening around it.
- JLCPCB BOM/CPL preparation guidance: reference designators must match exactly between BOM and CPL; only references present in both files are recognized for assembly.

## Review Result

No PCB source file exists, so this review cannot measure geometry, DRC rules, component placement, silk, mask, drills, annular rings, board outline, CPL origins, rotations, or bottom-side assembly content. All geometry-dependent DFM checks are therefore `BLOCKED_NO_PCB`, not `PASS`.

## DFM/DFA Checklist

| # | Check | Status | Evidence | Required closure |
|---:|---|---:|---|---|
| 1 | Board outline closed and valid | `BLOCKED_NO_PCB` | Final PCB audit says no `.kicad_pcb`; no board outline exists. | Create PCB only after schematic-to-PCB gate passes; verify closed `Edge.Cuts` with DRC and visual review. |
| 2 | Minimum track width meets JLCPCB capability | `BLOCKED_NO_PCB` | No traces exist; JLCPCB baseline depends on copper weight/layer count. | Set net classes at or above selected JLCPCB capability, preferably with margin, then DRC. |
| 3 | Minimum clearance meets JLCPCB capability | `BLOCKED_NO_PCB` | No copper exists; no clearance report exists. | Set clearance rules for selected copper weight/layer count; verify DRC. |
| 4 | Minimum drill size meets JLCPCB capability | `BLOCKED_NO_PCB` | No PCB holes/vias exist. | Define vias, PTH, NPTH, slots, and mounting/tooling holes; verify against current JLCPCB order page. |
| 5 | Annular rings acceptable | `BLOCKED_NO_PCB` | No plated holes/vias exist. | Verify pad/via sizes against drill tolerances and JLCPCB DRC. |
| 6 | Copper-to-edge clearance acceptable | `BLOCKED_NO_PCB` | No outline or copper exists. | Define copper keepouts around board edge, slots, mounting holes, and connector cutouts. |
| 7 | Silkscreen not over pads | `BLOCKED_NO_PCB` | No PCB silkscreen exists. | Run DRC and visual review; move references/values away from pads and component bodies. |
| 8 | Solder mask slivers acceptable | `BLOCKED_NO_PCB` | No pads or mask openings exist. | Check fine-pitch parts, USB-C, ESD, regulator, and LED pads; confirm mask bridge feasibility. |
| 9 | Courtyards/component spacing acceptable | `BLOCKED_NO_PCB` | No placement exists; placement audit is blocked. | Place parts, run courtyard DRC, and compare to JLCPCB SMD spacing guidance. |
| 10 | Via tenting expectations documented | `BLOCKED_POLICY_OPEN` | No vias exist; no fab note/profile exists. | Decide tented/open via policy before Gerber generation; document in fab notes if needed. |
| 11 | Mounting holes plated/non-plated intent clear | `BLOCKED_NO_PCB` | MH1-MH4 still require screw, NPTH/plated, copper keepout, standoff review. | Define NPTH/PTH intent and keepouts; add assembly tooling holes separately if JLCPCB assembly is used. |
| 12 | Edge connectors/USB/barrel jack overhang clear | `BLOCKED_NO_PCB` | J1/J2 exact drawings and board-edge alignment are unresolved; no outline/placement exists. | Verify exact connector drawings, edge overhang, insertion clearance, and enclosure openings. |
| 13 | Component rotation/origin risk for assembly | `BLOCKED_NO_CPL` | No PCB placement or CPL exists; many exact package drawings are not verified. | Generate CPL after placement; verify JLCPCB preview and orientation for all polarized/asymmetric parts. |
| 14 | Bottom-side components present yes/no | `BLOCKED_NO_PCB` | No PCB placement exists. | Decide one-side versus two-side assembly after placement; record side for every part. |
| 15 | Hand-solder vs JLC assembly strategy | `BLOCKED_POLICY_OPEN` | Production risk register says exact parts and assembly policy are unresolved. | Decide PCB-only, JLC top-side assembly, two-side assembly, or mixed manual-solder strategy. |
| 16 | Part availability in JLC/LCSC if assembly planned | `BLOCKED_NO_PART_SELECTION` | Exact MPNs missing for J1, L1, SW1, SW2, U3, D2, D3; packages missing for capacitors. | Select exact orderable parts and verify JLCPCB/LCSC availability close to order time. |
| 17 | Parts not in JLC library marked DNP/manual-solder | `BLOCKED_NO_BOM_STRATEGY` | No assembly BOM exists; exact source/library strategy unresolved. | Mark non-assembled parts DNP/manual-solder or remove from assembly BOM/CPL. |
| 18 | BOM fields complete | `BLOCKED_NO_FINAL_BOM` | BOM lock is planning-only; no exact verified footprints; no final JLC part fields. | Complete MPN, LCSC/JLC part numbers, quantity, value, footprint, side, DNP/manual status. |
| 19 | CPL/pick-place fields complete | `BLOCKED_NO_CPL` | No PCB exists; no positions, layers, or rotations exist. | Generate CPL after placement; verify designator, X/Y, side, and rotation in JLCPCB preview. |
| 20 | Polarity/orientation marks clear | `BLOCKED_NO_PCB` | Polarity/orientation risks remain open for PMOS, TVS, USB ESD, LEDs, connectors, switches, ESP32 module. | Add clear pin-1/cathode/polarity/orientation marks and verify against datasheets and assembly preview. |
| 21 | Fiducials needed yes/no | `NEEDS_DECISION` | If JLCPCB Standard PCBA is used, edge rails/fiducials are required by JLCPCB guidance; no assembly plan exists. | For Standard PCBA, include rails and fiducials or accept JLCPCB-added panel features; for PCB-only, document not required. |
| 22 | Tooling holes needed yes/no | `NEEDS_DECISION` | Economic PCBA guidance requires tooling holes; Standard/process-edge guidance differs; no assembly plan exists. | Decide Economic versus Standard PCBA; add appropriate tooling-hole/panel features if assembly is ordered. |
| 23 | Panelization needed yes/no | `NEEDS_DECISION` | Board size/outline does not exist; assembly strategy unresolved. | Decide single-board order versus panelized/rails after board outline, connector overhang, and assembly side are known. |

## Blocking Findings

1. There is no PCB file to review for JLCPCB DFM/DFA.
2. No Gerber/drill/BOM/CPL package exists and none was generated in this task.
3. JLCPCB-specific manufacturing checks cannot pass without a board outline, DRC, drills, copper, silkscreen, solder mask, placement, and assembly data.
4. JLCPCB assembly cannot be planned from the current BOM because exact MPNs, package drawings, JLC/LCSC availability, DNP/manual-solder status, and CPL rotations/origins are absent.
5. Production remains blocked by `PRODUCTION_RISK_REGISTER.md` and final PCB audit evidence.

## Final Classification

`JLCPCB_REVIEW_BLOCKED`

Reason: the design has no PCB, no DRC, no routing, no board outline, no BOM/CPL assembly package, and unresolved exact-part/package/orientation risks.
