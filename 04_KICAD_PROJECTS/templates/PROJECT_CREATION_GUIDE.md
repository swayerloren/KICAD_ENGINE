# Project Creation Guide

Use this guide to create a standard KiCad project workspace under `04_KICAD_PROJECTS\active`.

## Rules

- Do not create a real project unless the user requests it.
- Do not modify installed KiCad application files.
- Do not update `00_CODEX_START\CURRENT_PROJECT.md` unless the user explicitly asks to make the new project active.
- Do not edit `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, symbol libraries, footprint libraries, or manufacturing files unless the active project gate is complete.

## Standard Template

Template folder:

```text
04_KICAD_PROJECTS\templates\STANDARD_KICAD_PROJECT_TEMPLATE
```

Template contents:

```text
AGENTS.md
README.md
kicad\
datasheets\
bom\
fabrication\
renders\
reports\
notes\
scripts\
memory\
history\
```

Reusable source templates:

```text
04_KICAD_PROJECTS\templates\STANDARD_PROJECT_AGENTS_TEMPLATE.md
04_KICAD_PROJECTS\templates\STANDARD_PROJECT_README_TEMPLATE.md
```

## Scripted Creation

Run from the workspace root:

```powershell
.\03_TOOLS\scripts\new_kicad_project_workspace.ps1 -ProjectName 'PROJECT_NAME'
```

The script will:

- Create `04_KICAD_PROJECTS\active\PROJECT_NAME`.
- Copy the standard project template.
- Create `01_MEMORY\projects\PROJECT_NAME`.
- Create `02_HISTORY\project_history\PROJECT_NAME`.
- Add a project record to `00_CODEX_START\PROJECT_INDEX.md`.
- Leave `00_CODEX_START\CURRENT_PROJECT.md` unchanged.

The script will fail if the active project folder already exists.

## Manual Creation

If creating manually:

1. Create `04_KICAD_PROJECTS\active\PROJECT_NAME`.
2. Copy contents from `04_KICAD_PROJECTS\templates\STANDARD_KICAD_PROJECT_TEMPLATE`.
3. Replace `PROJECT_NAME` and `PROJECT_PATH` placeholders in copied `README.md` and `AGENTS.md`.
4. Create `01_MEMORY\projects\PROJECT_NAME\PROJECT_MEMORY.md`.
5. Create `02_HISTORY\project_history\PROJECT_NAME`.
6. Update `00_CODEX_START\PROJECT_INDEX.md`.
7. Update `00_CODEX_START\CURRENT_PROJECT.md` only if the user asks to make the project active.

## After Creation

Next recommended steps:

1. Decide whether the new project should become active.
2. If active, update `00_CODEX_START\CURRENT_PROJECT.md`.
3. Create or import KiCad source files under the project `kicad\` folder.
4. Add datasheets before component verification.
5. Run ERC/DRC only after KiCad source files exist.
6. Keep manufacturing outputs marked not final until verify-before-fab passes.
