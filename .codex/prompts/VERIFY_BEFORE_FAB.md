# Verify Before Fabrication

Use this prompt before any KiCad manufacturing package is treated as ready for fabrication.

## Startup Requirements
Before verification:
1. Read root `AGENTS.md`.
2. Read all `00_CODEX_START/` files in the required order.
3. Confirm the active project name and path.
4. Load relevant memory and history.
5. Confirm outputs will be written only to approved output folders.

## Required Verification
Run or complete:
- ERC.
- DRC.
- BOM export.
- Footprint checks.
- Datasheet checks.
- Connector checks.
- Polarity and orientation checks.
- Power input and protection checks.
- Mounting hole checks.
- Board edge clearance checks.

## Fabrication Outputs
Export fabrication files only into:
- `05_OUTPUTS`
- The active project's `fabrication` folder

Allowed fabrication exports include:
- Gerber files.
- Drill files.
- STEP files.

Do not overwrite prior release outputs without creating a dated or versioned output folder.

## Finality Rule
Mark the output `NOT FINAL` if any verification is incomplete, blocked, stale, or unreviewed.

Manufacturing output is not final until ERC, DRC, BOM, footprint, netlist, datasheet, and visual review are complete.

## Reports
Save verification reports in:
- `02_HISTORY\erc_drc_reports\`
- `02_HISTORY\fabrication_reviews\`
- The project-specific history folder when appropriate
