# How To Create A Project

KiCad Engine can help plan a project workspace, but KiCad remains the design tool.

## Recommended Workflow

1. Define project goals, constraints, interfaces, and manufacturing assumptions.
2. Create or copy a KiCad project in a controlled folder.
3. Document the active project path.
4. Confirm backups before AI-assisted edits.
5. Research major components and footprints before schematic entry.
6. Run ERC after schematic changes.
7. Run DRC after PCB changes.
8. Keep outputs `NOT_FINAL` until review is complete.

## Ask The Agent To Plan First

Use:

- `.prompts/codex/05_PLAN_SCHEMATIC.md`
- `.prompts/claude/05_PLAN_SCHEMATIC.md`

The planning step should identify:

- Main blocks.
- Power domains.
- Interfaces.
- Component research required.
- Datasheets needed.
- Footprint risks.
- Verification plan.

## Do Not Skip Footprint Review

Before layout, verify footprints against exact manufacturer drawings, especially for connectors, modules, regulators, crystals, RF parts, and exposed-pad packages.
