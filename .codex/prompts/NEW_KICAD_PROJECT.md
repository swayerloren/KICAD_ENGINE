# New KiCad Project

Use this prompt when the user asks Codex to create a new KiCad project workspace.

## Required Inputs
Ask for a filesystem-safe project ID if it is not provided. Use uppercase letters, numbers, and underscores where possible.

## Startup Requirements
Before creating anything:
1. Read root `AGENTS.md`.
2. Read all `00_CODEX_START/` files in the required order.
3. Review relevant memory and history.
4. Confirm no existing project folder will be overwritten.

## Create Project Structure
Create the new project under:

`04_KICAD_PROJECTS\active\<project-id>`

Create these folders inside the project:
- `kicad`
- `datasheets`
- `bom`
- `fabrication`
- `renders`
- `reports`
- `notes`

## Create Project Files
Create:
- `04_KICAD_PROJECTS\active\<project-id>\AGENTS.md`
- `04_KICAD_PROJECTS\active\<project-id>\README.md`

The project `AGENTS.md` must inherit the root workspace rules and define project-specific boundaries.

The project `README.md` must include the project purpose, current status, folder map, verification status, and next actions.

## Create Memory And History
Create the project memory folder:

`01_MEMORY\projects\<project-id>`

Create:

`01_MEMORY\projects\<project-id>\PROJECT_MEMORY.md`

Create the project history folder:

`02_HISTORY\project_history\<project-id>`

## Update Indexes
- Update `00_CODEX_START\PROJECT_INDEX.md` with the new project record.
- Update `00_CODEX_START\CURRENT_PROJECT.md` only when the user explicitly asks to make the new project active.

## Restrictions
- Do not install tools.
- Do not clone repositories.
- Do not configure MCP.
- Do not create manufacturing outputs during project setup.
