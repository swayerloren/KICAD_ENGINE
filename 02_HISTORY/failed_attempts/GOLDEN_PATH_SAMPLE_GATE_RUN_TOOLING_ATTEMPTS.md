# Failed Attempts - Golden Path Sample Gate Run

Date: `2026-05-03`

## Attempt 1 - Optional Git Status Check

Command:

```powershell
git status --short -- 19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board 03_TOOLS/scripts/project_validation/validate_kicad_project.py
```

Result:

`fatal: not a git repository (or any of the parent directories): .git`

Impact:

No source files were reverted or changed because of this failure. The checkout appears to lack Git metadata from the command's perspective, so final file-change accounting is based on command output and direct file paths.

## Attempt 2 - Nonexistent Common Parser Filename

An earlier inspection attempted to open `03_TOOLS/scripts/kicad_schematic_checks/kicad_schematic_common.py`. The actual helper module is `schematic_check_common.py`.

Impact:

No code or KiCad design files were changed. The correct module was later used through the existing checker scripts.
