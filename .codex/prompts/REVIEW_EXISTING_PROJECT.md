# Review Existing KiCad Project

Use this prompt when the user asks Codex to review an existing KiCad project.

## Startup Requirements
Before inspecting project files:
1. Read root `AGENTS.md`.
2. Read all `00_CODEX_START/` files in the required order.
3. Confirm the active project name and path.
4. Load relevant project memory and history.
5. State the review scope and verification plan.

## Project Structure Inspection
Inspect the existing project structure and identify:
- `.kicad_pro`
- `.kicad_sch`
- `.kicad_pcb`
- Symbol libraries
- Footprint libraries
- Datasheets
- BOM files
- Reports
- Manufacturing outputs
- Renders or visual references
- Project notes

## Review Scope
Check:
- Library references.
- Symbol availability.
- Footprint assignments.
- Datasheet coverage for critical parts.
- BOM completeness.
- Existing ERC/DRC reports.
- Manufacturing outputs and whether they are current.
- Connector pinouts and orientation.
- Power input, protection, rails, and net labels.
- Mechanical constraints, mounting holes, and board outline.

## ERC And DRC
- Run ERC and DRC when local tooling is available and the user has authorized checks.
- If tooling is missing or checks cannot run, prepare the exact intended ERC/DRC commands or manual check plan and explain the limitation.

## Output
Produce a review report in `02_HISTORY\design_reviews\` or the project-specific history folder.

Do not edit project files unless the user explicitly requests fixes.
