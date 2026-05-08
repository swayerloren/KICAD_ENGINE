# KiCad Agent Task Map

Date: 2026-05-02

Audience: Codex, Claude, and similar AI agents using KiCad from VS Code.

Status: Safe workflow map. This file does not grant permission to edit KiCad project files.

## How To Use This Map

For each user request:

1. Classify the task.
2. Choose the safest workflow.
3. Confirm whether the task is read-only, output-generating, or source-editing.
4. Apply the active project, backup, verification, and rollback gates when needed.
5. Record reports, outputs, and remaining risk.

Default control-plane order:

1. Read files and library metadata.
2. Use existing scripts.
3. Use `kicad-cli`.
4. Use read-only `pcbnew` Python.
5. Use GUI screenshots only for visual discovery.
6. Avoid GUI control unless explicitly approved.

## Create New Project

Safe workflow:

1. Clarify project name, purpose, board constraints, target KiCad version, and whether this is a template or active design.
2. Check `00_CODEX_START/CURRENT_PROJECT.md` and project indexes.
3. If source creation is requested, confirm the active project path and backup/rollback plan.
4. Prefer creating from an approved template under `04_KICAD_PROJECTS/templates`.
5. Create project-local folders for libraries, datasheets, reports, and outputs if approved.
6. Do not create placeholder schematic or PCB files unless the user explicitly asks for source generation.

Primary tools:

- Repo templates.
- Direct file operations after approval.
- `kicad-cli` only if needed for validation.

Stop if:

- Board requirements are too incomplete to create meaningful source.
- Active project scope is ambiguous.

## Add MCU

Safe workflow:

1. Identify exact MCU part number and package.
2. Locate datasheet and reference manual in `06_DATASHEETS` or request/download approval.
3. Inspect existing component preferences in `01_MEMORY`.
4. Resolve symbol candidates from project-local, global, then stock libraries.
5. Resolve footprint candidates and compare to the package drawing.
6. Check required power rails, decoupling, boot straps, reset, clock, USB/JTAG/UART, antenna/RF constraints, and programming path.
7. If source edits are requested, require active project approval and backup before adding anything.
8. After edits, run ERC; after layout placement/routing, run DRC.

Primary tools:

- Datasheet inspection.
- Library discovery guide.
- Direct `.kicad_sym` and `.kicad_mod` inspection.
- ERC/DRC wrappers after approved edits.

High risks:

- Wrong package variant.
- Boot strap pins.
- Hidden power pins.
- RF layout rules.
- Incomplete decoupling.

## Add USB-C

Safe workflow:

1. Clarify role: power-only, USB 2.0 device, host, dual-role, or USB-PD.
2. Identify connector part number and orientation.
3. Verify CC resistors, ESD protection, shield/chassis treatment, VBUS protection, and differential-pair needs.
4. Inspect symbol pin mapping and footprint pad numbering against datasheet.
5. Check connector mechanical orientation, board edge, keepout, shell pads, and 3D model.
6. Require source-edit approval before changing schematic or PCB.
7. Run ERC after schematic changes and DRC after layout changes.

Primary tools:

- Datasheet and package drawing.
- Footprint inspection.
- `pcbnew` Python for board-edge/orientation reports if needed.
- GUI screenshot for final visual orientation only.

High risks:

- Flipped connector orientation.
- Incorrect CC pull-up/pull-down role.
- Shell grounding assumptions.
- Missing ESD or VBUS protection.

## Add CAN Transceiver

Safe workflow:

1. Confirm CAN voltage domain, MCU I/O voltage, bus speed, connector, and whether isolation is required.
2. Identify exact transceiver and package.
3. Verify TXD/RXD pin mapping, standby/silent pins, VIO pin if present, termination, common-mode choke, TVS, and connector pinout.
4. Inspect symbol and footprint against datasheet.
5. Require source-edit approval before changes.
6. Run ERC after schematic changes and DRC after layout changes.

Primary tools:

- Datasheet inspection.
- Symbol/footprint library inspection.
- ERC/DRC wrappers.

High risks:

- 3.3 V versus 5 V logic mismatch.
- Missing bus protection.
- Incorrect connector pinout.
- Termination placed incorrectly.

## Add Regulator

Safe workflow:

1. Confirm input range, output voltage, load current, thermal constraints, noise constraints, and topology.
2. Identify exact regulator part number and package.
3. Inspect datasheet for required capacitors, inductor, diode, feedback divider, compensation, enable pins, exposed pad, and layout notes.
4. Resolve symbol and footprint.
5. Check thermal pad and copper requirements.
6. Require source-edit approval before changes.
7. Run ERC after schematic changes and DRC after layout changes.

Primary tools:

- Datasheet and application circuit.
- Footprint inspection.
- `pcbnew` geometry checks for thermal pad/via layout after placement.

High risks:

- Wrong capacitor ESR or value.
- Incorrect feedback divider.
- Missing thermal relief or copper.
- Package mismatch.

## Add Connector

Safe workflow:

1. Confirm connector family, pitch, pin count, gender/mating side, shrouding/keying, orientation, current rating, and board placement.
2. Inspect datasheet or drawing.
3. Verify symbol pin order and footprint pad order.
4. Check pin 1 marking, silkscreen, fab outline, courtyard, and 3D model.
5. For edge or panel connectors, verify mechanical side and mating direction visually.
6. Require source-edit approval before changes.
7. Run ERC and DRC after approved edits.

Primary tools:

- Footprint inspection.
- `pcbnew` Python for orientation and placement reports.
- GUI screenshot for visual confirmation.

High risks:

- Mirrored pin order.
- Wrong gender.
- Mating direction reversed.
- Silkscreen pin-1 ambiguity.

## Check Footprints

Safe workflow:

1. Extract schematic footprint assignments and PCB footprint references.
2. Resolve project-local libraries first, then global, then stock.
3. Inspect `.kicad_mod` files read-only.
4. Compare pad count, numbering, dimensions, orientation, courtyard, 3D model, and pin-1 marking to datasheets.
5. Report unresolved or unverifiable footprints.
6. Do not change assignments without active project approval.

Primary tools:

- Direct file parsing.
- Library discovery guide.
- Datasheets.
- `pcbnew` Python for board-level placement checks.

Output:

- Footprint review report in `02_HISTORY/design_reviews` or approved project history.

## Validate Project

Safe workflow:

1. Confirm this is read-only validation, not automatic repair.
2. Identify the target project folder or `.kicad_pro` file.
3. Run the project validation wrapper and keep outputs outside the project folder by default.
4. Review the Markdown and JSON report for `PASS`, `WARN`, and `FAIL` checks.
5. Treat missing libraries, missing footprints, missing 3D models, missing datasheet records, and high-risk review flags as unresolved work.
6. Do not auto-fix symbols, footprints, library tables, or project files from the report.
7. Escalate connector orientation, polarity, RF, USB, CAN, LIN, and automotive findings to human review.

Primary command:

```powershell
& ".\03_TOOLS\scripts\project_validation\validate_kicad_project.ps1" -ProjectPath "C:\path\to\project"
```

Focused commands:

```powershell
python ".\03_TOOLS\scripts\project_validation\check_missing_footprints.py" "C:\path\to\project"
python ".\03_TOOLS\scripts\project_validation\check_missing_3d_models.py" "C:\path\to\project"
python ".\03_TOOLS\scripts\project_validation\check_connector_orientation_review_needed.py" "C:\path\to\project"
```

Outputs:

- `05_OUTPUTS/project_validation/<timestamp>_<project>/project_validation_report.md`
- `05_OUTPUTS/project_validation/<timestamp>_<project>/project_validation_report.json`

High risks:

- False confidence from static parsing.
- Treating a candidate footprint as verified.
- Ignoring project-local library tables.
- Treating `PASS` as release approval.

## Run ERC

Safe workflow:

1. Confirm active project and schematic path.
2. Confirm whether this follows edits or is read-only verification.
3. Use `03_TOOLS/scripts/run_erc.ps1`.
4. Save report and summary under `02_HISTORY/erc_drc_reports` or approved output root.
5. Report exit code and key violations.
6. State remaining schematic risks beyond ERC.

Primary command:

```powershell
& ".\03_TOOLS\scripts\run_erc.ps1" -ProjectPath "C:\path\to\project"
```

Stop if:

- No schematic exists.
- Target project is not the active-approved project for the task.

## Run DRC

Safe workflow:

1. Confirm active project and board path.
2. Confirm whether this follows edits or is read-only verification.
3. Use `03_TOOLS/scripts/run_drc.ps1`.
4. Save report and summary under `02_HISTORY/erc_drc_reports` or approved output root.
5. Report exit code and key violations.
6. State remaining board risks beyond DRC.

Primary command:

```powershell
& ".\03_TOOLS\scripts\run_drc.ps1" -ProjectPath "C:\path\to\project"
```

Stop if:

- No PCB exists.
- Target project is not the active-approved project for the task.

## Export Gerbers

Safe workflow:

1. Confirm active project and board path.
2. Confirm ERC and DRC status, or state that export is review-only despite missing gates.
3. Use `03_TOOLS/scripts/export_gerbers.ps1`.
4. Write into timestamped `NOT_FINAL` output folder.
5. Include command log and summary.
6. Do not call the result fabrication-ready.

Primary command:

```powershell
& ".\03_TOOLS\scripts\export_gerbers.ps1" -ProjectPath "C:\path\to\project"
```

High risks:

- Export settings not matching fab requirements.
- Board house layer naming expectations.
- Generated files not visually reviewed.

## Export BOM

Safe workflow:

1. Confirm active project and schematic path.
2. Use `03_TOOLS/scripts/export_bom.ps1`.
3. Review generated CSV for references, values, footprints, MPNs, DNP status, and quantities.
4. Cross-check critical parts against datasheets and sourcing requirements.
5. Mark as review-only until approved.

Primary command:

```powershell
& ".\03_TOOLS\scripts\export_bom.ps1" -ProjectPath "C:\path\to\project"
```

High risks:

- Missing manufacturer part numbers.
- DNP parts not encoded.
- Footprint variants hidden by generic values.

## Review Finished PCB

Safe workflow:

1. Treat original finished PCB folders as read-only unless the user explicitly approves direct edits.
2. Prefer a copied review workspace.
3. Inventory source files, libraries, outputs, reports, and package manifests.
4. Run ERC and DRC only when project scope is approved.
5. Compare existing fabrication outputs to source when possible.
6. Produce a design review report in `02_HISTORY/design_reviews`.
7. Classify result as review-only, `HUMAN_REVIEW_REQUIRED`, or user-approved.

Primary tools:

- Direct parsing.
- ERC/DRC wrappers.
- Gerber/drill/BOM parsers if available.
- GUI screenshots only for visual confirmation.

High risks:

- Original reference folders accidentally edited.
- Existing outputs treated as final without source verification.

## Compare Schematic To PCB

Safe workflow:

1. Confirm active project and source files.
2. Parse schematic references, values, footprints, and nets.
3. Parse PCB footprints, nets, pads, and missing/unconnected items.
4. Use KiCad netlist/ERC/DRC outputs where available.
5. Report mismatches: missing references, extra footprints, footprint changes, no-connect differences, and net inconsistencies.
6. Do not auto-fix mismatches without explicit approval.

Primary tools:

- Direct file parsing.
- `kicad-cli` ERC/DRC.
- `pcbnew` Python for board-side net and footprint inspection.

High risks:

- Hierarchical sheets.
- Excluded-from-BOM/board fields.
- Intentional mechanical or mounting footprints.

## Check Datasheets

Safe workflow:

1. Identify exact component part numbers.
2. Check whether datasheets exist in `06_DATASHEETS`.
3. Do not download datasheets unless the user approves.
4. Extract package, pinout, recommended circuit, layout, thermal, electrical limits, and orientation evidence.
5. Compare symbol pins and footprint pads to datasheet.
6. Record unknowns and source gaps.

Primary tools:

- Local datasheets.
- Component memory.
- Symbol and footprint inspection.

High risks:

- Datasheet copyright and redistribution.
- Wrong revision.
- Similar part number with different package or pinout.

## Generate Manufacturing Package

Safe workflow:

1. Confirm active project, backup state, and output folder.
2. Run ERC and DRC or cite recent clean reports.
3. Export BOM, Gerbers, drills, pick-and-place if available, assembly drawings, STEP, and reports.
4. Create a manifest.
5. Mark package `NOT_FINAL` unless all release gates are complete.
6. Review connector orientation, polarity, footprint accuracy, and fab requirements before any final claim.

Primary tools:

- `full_verify_project.ps1` when appropriate.
- Individual export scripts.
- Direct package manifest generation.

High risks:

- False finality.
- Missing assembly data.
- Unreviewed connector/polarity assumptions.
- Board house option mismatch.

## Prepare JLCPCB Package

Safe workflow:

1. Confirm the user wants a JLCPCB-oriented review package.
2. Check current JLCPCB requirements from trusted current sources if exact formatting is needed.
3. Generate Gerbers, drills, BOM, and pick-and-place into `NOT_FINAL` output.
4. Review BOM fields for MPN/LCSC part numbers if assembly is intended.
5. Review pick-and-place side, rotation, X/Y origin, and package fields.
6. Include a manifest of unresolved JLCPCB-specific questions.
7. Do not claim upload readiness until human review confirms requirements.

Primary tools:

- KiCad export scripts.
- BOM/PNP parsers.
- Current fab requirement lookup when requested.

High risks:

- Changing JLCPCB format requirements.
- Rotation conventions.
- LCSC part mapping.
- DNP and manually assembled parts.

## Prepare PCBWay Package

Safe workflow:

1. Confirm the user wants a PCBWay-oriented review package.
2. Check current PCBWay requirements from trusted current sources if exact formatting is needed.
3. Generate Gerbers, drills, BOM, pick-and-place, assembly drawings, and STEP as needed into `NOT_FINAL` output.
4. Review layer names, drill files, board outline, stackup, solder mask, silkscreen, and assembly data.
5. Include a manifest of unresolved PCBWay-specific questions.
6. Do not claim upload readiness until human review confirms requirements.

Primary tools:

- KiCad export scripts.
- BOM/PNP parsers.
- Current fab requirement lookup when requested.

High risks:

- Board house file naming expectations.
- Assembly rotation conventions.
- Missing mechanical drawing or panelization requirements.
- Unverified stackup and impedance assumptions.
