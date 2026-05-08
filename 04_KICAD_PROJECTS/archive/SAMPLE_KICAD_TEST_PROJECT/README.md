# SAMPLE_KICAD_TEST_PROJECT

Standard KiCad project workspace.

## Status

- Project name: `SAMPLE_KICAD_TEST_PROJECT`
- Project path: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT`
- Active project: not selected by template creation alone
- Fabrication status: not final

## Folder Map

- `kicad/`: KiCad project source files.
- `datasheets/`: component datasheets and reference documents.
- `bom/`: BOM exports, sourcing notes, and assembly review files.
- `fabrication/`: Gerber, drill, pick/place, STEP, and fabrication package drafts.
- `renders/`: board renders and visual review images.
- `reports/`: ERC, DRC, design review, and verification reports.
- `notes/`: project notes that are not durable memory.
- `scripts/`: project-local helper scripts.
- `memory/`: project-local durable design memory.
- `history/`: project-local session and review history.

## Startup Rule

Before editing this project, read the root `KICAD_ENGINE/AGENTS.md`, root startup files, this project's `AGENTS.md`, and relevant memory/history.

## Fabrication Rule

Do not treat any output as final until the verify-before-fab workflow passes, including ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, power/protection, mechanical, and visual review gates.

## Next Steps

1. Create or copy KiCad project files into `kicad/`.
2. Add component datasheets to `datasheets/`.
3. Update root `00_CODEX_START/CURRENT_PROJECT.md` only when this project should become active.
4. Record durable design decisions in project memory.
5. Record session work and command results in project history.

