# User Manual

KiCad Engine is a VS Code workspace for AI-assisted KiCad engineering. It gives Codex, Claude, and similar agents a safer way to inspect your installed KiCad app, read project context, run checks, and produce review reports.

## Basic Workflow

1. Install or clone KiCad Engine.
2. Open the `KICAD_ENGINE` folder in VS Code.
3. Run the health check.
4. Log in to your AI tool yourself.
5. Start the agent with the matching prompt pack.
6. Ask for planning, review, validation, research, or controlled output generation.
7. Review the agent's work and verification reports.

## Folders You Will Use

- `.prompts/`: prompts for Codex, Claude, and shared standards.
- `.vscode/`: tasks, settings, launch config, and extension recommendations.
- `00_CODEX_START/`: startup rules and agent operating context.
- `01_MEMORY/`: durable project decisions.
- `02_HISTORY/`: sessions, command logs, audits, and review reports.
- `03_TOOLS/`: scripts and KiCad intelligence tooling.
- `04_KICAD_PROJECTS/`: optional place for local KiCad projects.
- `05_OUTPUTS/`: generated reports and review outputs.
- `06_DATASHEETS/`: datasheet metadata, source links, summaries, and policies.
- `08_COMPONENT_DATABASE/`: structured component records and design-rule notes.

## Working With AI Agents

Use the prompt pack instead of starting from a blank chat. The prompt pack tells the agent:

- What files to read first.
- What not to modify.
- How to handle backups and logs.
- How to avoid fake datasheet claims.
- How to avoid unverified footprint selections.
- How to label outputs `NOT_FINAL`.

## Working With KiCad Projects

Before an agent edits a KiCad project, require:

- Active project name and path.
- Exact files likely to change.
- Backup path.
- Rollback plan.
- Verification plan.
- Human approval.

For review-only work, prefer:

- Project validation script.
- ERC through `kicad-cli`.
- DRC through `kicad-cli`.
- Datasheet and component database checks.
- Footprint and connector review notes.

## Reports And Outputs

Reports normally go under:

- `02_HISTORY/`
- `05_OUTPUTS/`

Manufacturing-style files such as Gerbers, drills, pick-and-place, and STEP exports must remain `NOT_FINAL` until the full verification gate passes.

## Deeper Guides

- `docs/WHAT_IS_KICAD_ENGINE.md`
- `docs/USING_WITH_CODEX.md`
- `docs/USING_WITH_CLAUDE.md`
- `docs/USING_WITH_KICAD.md`
- `docs/HOW_TO_CREATE_A_PROJECT.md`
- `docs/HOW_TO_REVIEW_A_PROJECT.md`
- `docs/HOW_TO_VERIFY_A_FOOTPRINT.md`
- `docs/SAFETY_AND_LIMITATIONS.md`
