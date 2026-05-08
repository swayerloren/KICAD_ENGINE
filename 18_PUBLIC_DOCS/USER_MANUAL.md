# User Manual

Status: `PUBLIC_DRAFT`

## Core Workflow

1. Open the workspace in VS Code.
2. Run the health check.
3. Start an AI session with `.prompts/codex/00_START_SESSION.md` or `.prompts/claude/00_START_SESSION.md`.
4. Ask the agent to inspect, plan, validate, or document before requesting KiCad edits.
5. Require backups before any KiCad source edit.
6. Run ERC after schematic changes and DRC after PCB changes.
7. Keep manufacturing-style outputs `NOT_FINAL` until human review.

## Main Areas

- `00_CODEX_START/`: startup and safety rules.
- `03_TOOLS/`: scripts and tool guidance.
- `06_DATASHEETS/`: datasheet metadata and source-link library.
- `08_COMPONENT_DATABASE/`: structured part records.
- `09_ACCURACY_ENGINE/`: anti-guessing rules.
- `10_KNOWLEDGE_BASE/`: reusable circuit and review guidance.
- `11_LIBRARY_FACTORY/`: symbol and footprint standards.
- `12_REFERENCE_DESIGN_LIBRARY/`: link-first reference design records.

## What Users Must Verify

- Datasheet values.
- Pinouts.
- Symbols.
- Footprints.
- Connector orientation.
- Mechanical fit.
- BOM.
- ERC/DRC results.
- Gerber/drill/PNP/STEP outputs.

