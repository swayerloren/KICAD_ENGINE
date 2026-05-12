# KiCad Automation Index

Use this file to route automation work to the correct KiCad knowledge sources before touching a real project.

## Primary Sources

- `01_kicad_core/`
  - KiCad CLI behavior
  - editor workflows
  - DRC and ERC concepts
  - official KiCad usage documentation
- `02_kicad_python_api/`
  - Python automation
  - `pcbnew` scripting
  - bindings and IPC API references
- `03_kicad_file_formats/`
  - file-structure details for `.kicad_pcb`, `.kicad_sch`, and related files
  - safe parsing, generation, and diff-oriented automation
- `04_kicad_libraries_symbols_footprints/`
  - KLC and library rules
  - symbol and footprint policy

## Default Automation Workflow

1. Confirm the active project and backup plan before touching real design files.
2. Prove the intended change on non-production files, scratch copies, or deterministic transformations first.
3. Use the highest-trust docs from `01_` through `04_` to justify the edit.
4. Run or plan verification:
  - schema or format validation
  - KiCad CLI where applicable
  - DRC
  - ERC
  - visual diff or structural diff
5. Only then apply changes to a real PCB or schematic.

## What AI Should Prove Before Editing

- The file format and field names are understood.
- The automation path is deterministic, not guess-based.
- The edit can be checked by a script, CLI command, DRC/ERC, or file diff.
- Library or footprint changes still satisfy KLC or project-specific rules.

## Practical Routing

- Need scripting examples: start in `02_kicad_python_api/`.
- Need board or schematic file structure: start in `03_kicad_file_formats/`.
- Need library rule enforcement: start in `04_kicad_libraries_symbols_footprints/`.
- Need official KiCad user behavior or CLI docs: start in `01_kicad_core/`.

## Hard Rule

Do not touch a real PCB simply because an AI-generated edit looks plausible. The change must be backed by trusted sources and verified in the sandboxed workflow before it reaches a live design.
