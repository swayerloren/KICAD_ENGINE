# Reference Project Folder Standard

This standard applies when copying a finished PCB reference into `04_KICAD_PROJECTS\active` for read-only review and learning.

## Purpose

Reference project workspaces let Codex and ChatGPT inspect a finished PCB without modifying the original source folder under `99_01 Finished PCBs`.

## Naming

- Use `PROJECT_NAME_VERIFIED_REFERENCE` for the first copied review workspace.
- If that folder already exists, create `PROJECT_NAME_VERIFIED_REFERENCE_YYYYMMDD_HHMMSS`.
- Do not reuse a reference folder as an active design revision.

## Required Location

Copied reference workspaces belong under:

`04_KICAD_PROJECTS\active`

Original finished PCB references remain under:

`99_01 Finished PCBs`

## Required Files And Folders

Each copied reference workspace should include:

- A copy of the original finished PCB folder contents.
- `AGENTS.md` with reference-specific safety rules.
- `README.md` with source path, destination path, status, and review purpose.
- `reports` for project-local review summaries.
- `notes` for non-durable observations.
- `review_outputs` for generated review artifacts marked `NOT_FINAL`.
- `reference_original_inventory` for inventory snapshots copied from or linked to history reports.
- `learning` for extracted lessons that are candidates for memory updates.

Project memory belongs under:

`01_MEMORY\projects\PROJECT_NAME_VERIFIED_REFERENCE\PROJECT_MEMORY.md`

Project history belongs under:

`02_HISTORY\project_history\PROJECT_NAME_VERIFIED_REFERENCE`

## Safety Rules

- Do not edit the original finished PCB folder.
- Do not overwrite copied fabrication outputs inside the reference workspace.
- Do not generate final manufacturing outputs from a reference workspace.
- Run read-only review first.
- Generated review outputs must use timestamped `NOT_FINAL` folders.
- Any design changes must be made in a separate revision project, not in the finished original or the verified reference copy.

## Review Workflow

1. Read root `AGENTS.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, and the reference workspace `AGENTS.md`.
2. Inventory source files, outputs, backups, caches, and folders.
3. Run `find_kicad_project_files.ps1` against the copied workspace.
4. Create a backup snapshot before any scripted verification.
5. Run ERC and DRC only when safe and record results.
6. Review BOM, pick-and-place, fabrication files, drill files, board outline, PDF, and STL.
7. Save review reports in `02_HISTORY` and in the reference workspace `reports` folder.
8. Update project memory only with durable factual findings.
9. Promote lessons to global memory only when they are supported by evidence and useful beyond the reference project.
