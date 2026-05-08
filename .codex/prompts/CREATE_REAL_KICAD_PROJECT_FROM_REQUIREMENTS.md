# Create Real KiCad Project From Requirements

Use this prompt when the user wants to create a real KiCad project, but the project name and engineering requirements still need to be gathered or confirmed.

## Startup Requirements

Before creating or editing anything, Codex must:

1. Read `AGENTS.md` from the current checkout.
2. Read every required startup file in `00_CODEX_START/` in the order required by `AGENTS.md`.
3. Confirm the current checkout root and read `00_CODEX_START/PATH_PORTABILITY_RULES.md` before acting on absolute paths.
4. Read relevant workspace memory and history.
5. Confirm that no real project should be created until the user provides a project name and requirements.

## Required User Inputs

Ask for or confirm all of the following before creating a real project:

- Project name
- Board purpose
- Input voltage
- Output voltages
- Max current
- MCU/processor requirements
- Communication buses, such as CAN, LIN, UART, I2C, SPI, USB
- Connectors
- Enclosure/mechanical limits
- Mounting hole requirements
- Environment, such as vehicle, outdoor, waterproof, vibration
- Preferred parts
- Parts to avoid
- Fab house
- Layer count
- Board size
- Special DFM rules
- Whether the task is schematic-only, PCB-only, or full design

If any requirement is unknown, ask a concise follow-up instead of guessing. Use `04_KICAD_PROJECTS\templates\REAL_PROJECT_REQUIREMENTS_TEMPLATE.md` as the intake checklist.

## Confirmation Gate

Before creating the project workspace, Codex must restate:

- Project name
- Project path that will be created under `04_KICAD_PROJECTS\active`
- Design scope: schematic-only, PCB-only, or full design
- Files/folders likely to be created
- Initial verification plan
- Rollback plan
- Open requirements still marked unknown

Proceed only after the user confirms.

## Project Creation Rules

When confirmed, create the real project using the standard workspace flow:

1. Create the project under `04_KICAD_PROJECTS\active\<project-id>`.
2. Use `03_TOOLS\scripts\new_kicad_project_workspace.ps1` unless there is a clear reason to create manually.
3. Create or update project requirements notes from the confirmed requirements.
4. Create project memory under `01_MEMORY\projects\<project-id>`.
5. Create project history under `02_HISTORY\project_history\<project-id>`.
6. Update `00_CODEX_START\PROJECT_INDEX.md`.
7. Update `00_CODEX_START\CURRENT_PROJECT.md` only if the user explicitly asks to make the project active.

## Safety Rules

- Do not create a real project without a project name.
- Do not create a real project without at least board purpose, input voltage, design scope, and mechanical/environment assumptions confirmed.
- Do not edit `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, symbol libraries, footprint libraries, or manufacturing outputs until the active project and backup plan are confirmed.
- Do not install tools.
- Do not clone repositories.
- Do not configure MCP unless explicitly requested.
- Do not generate fabrication-ready outputs during project creation.
- Never store secrets in memory, history, requirements, or project notes.

## Output

After project creation, summarize:

- Project created
- Project path
- Requirements captured
- Unknowns remaining
- Files changed
- Memory/history updated
- Next recommended engineering step
