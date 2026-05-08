# COMMAND_LINK_VERIFIED_REFERENCE Project Memory

## Project Identity

- Project name: `COMMAND_LINK_VERIFIED_REFERENCE`
- Project path: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\COMMAND_LINK_VERIFIED_REFERENCE`
- Source finished PCB path: `C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK`
- Status: copied finished reference project for read-only review and learning.

## Durable Rules

- The original finished PCB folder must remain unchanged.
- This copied reference is not a design revision workspace.
- Read-only review comes first.
- Any design changes must be made in a new revision copy.
- Any generated outputs are `NOT_FINAL` unless LJ explicitly approves a verified release workflow.
- Do not store secrets in project memory or history.

## Known Context

- User described the source as a finished Fiverr-verified PCB project.
- Previous inventory report: `02_HISTORY\design_reviews\COMMAND_LINK_FINISHED_PCB_INVENTORY.md`
- Reference copy session log: `02_HISTORY\sessions\COMMAND_LINK_REFERENCE_COPY_CREATED.md`
- Read-only review report: `02_HISTORY\design_reviews\COMMAND_LINK_READ_ONLY_REVIEW.md`
- ERC/DRC review report: `02_HISTORY\erc_drc_reports\COMMAND_LINK_ERC_DRC_REVIEW.md`

## Durable Factual Findings

- The copied reference contains 1 `.kicad_pro`, 1 `.kicad_sch`, and 1 `.kicad_pcb`.
- The visible BOM has 32 rows, quantity sum 46, and 46 unique expanded designators.
- No duplicate BOM designators, missing BOM designators, missing BOM values, or missing BOM footprints were found in the visible BOM CSV.
- Pick-and-place CSVs contain 43 top-side rows and 0 bottom-side rows.
- BOM references not present in the parsed placement CSVs: `J2`, `J3`, `J4`.
- Visible fabrication files include 4 copper layers, front/back solder mask, front/back silkscreen, front/back paste, board outline, Gerber job file, and PTH/NPTH drill-related Gerbers.
- ERC completed with KiCad CLI exit code 5: 0 errors and 2 warnings.
- DRC completed with KiCad CLI exit code 5: 46 violations, 0 unconnected pads/items, and 0 footprint errors in the DRC summary.
- The current local KiCad environment does not include footprint library `ULN2803ADW`.
- Script outputs for the read-only review are under `review_outputs\NOT_FINAL_read_only_review_20260430_180511`.

## Reusable Lessons

- TBD. Add only durable lessons that are confirmed useful beyond this reference project.
