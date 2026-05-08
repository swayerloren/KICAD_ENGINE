# KiCad Project Validation Scripts

Date: 2026-05-02

Purpose: provide read-only project validation reports that help Codex, Claude, and similar agents review KiCad projects without attempting unsafe automatic fixes.

## Scope

The validation system checks:

- Project file presence.
- Main schematic presence.
- PCB presence.
- Project-local library table presence.
- Missing symbol libraries.
- Missing footprint libraries and missing assigned footprint files.
- Missing 3D model references in the PCB.
- ERC, DRC, and BOM export availability through `kicad-cli`.
- Components with no datasheet evidence.
- Component database matches.
- Connectors requiring human orientation review.
- Polarity-sensitive parts requiring human review.
- RF components requiring layout review.
- USB/CAN/LIN/automotive topics requiring rule review.

## Safety

- Read-only project inspection only.
- No schematic, PCB, project, library, or manufacturing files are edited.
- No automatic fixes are attempted.
- Reports are written outside the project folder by default.
- The validator refuses to write reports inside the project folder unless `--allow-project-output` is explicitly supplied.
- A `PASS` result is not a fabrication-release approval.

## Main Command

PowerShell wrapper:

```powershell
& ".\03_TOOLS\scripts\project_validation\validate_kicad_project.ps1" -ProjectPath "C:\path\to\project"
```

Python directly:

```powershell
python ".\03_TOOLS\scripts\project_validation\validate_kicad_project.py" "C:\path\to\project"
```

Default reports:

```text
05_OUTPUTS/project_validation/<timestamp>_<project>/project_validation_report.md
05_OUTPUTS/project_validation/<timestamp>_<project>/project_validation_report.json
```

## Focused Checkers

Each focused checker uses the same report format and safety rules:

```powershell
python ".\03_TOOLS\scripts\project_validation\check_project_libraries.py" "C:\path\to\project"
python ".\03_TOOLS\scripts\project_validation\check_missing_footprints.py" "C:\path\to\project"
python ".\03_TOOLS\scripts\project_validation\check_missing_3d_models.py" "C:\path\to\project"
python ".\03_TOOLS\scripts\project_validation\check_unconnected_power.py" "C:\path\to\project"
python ".\03_TOOLS\scripts\project_validation\check_connector_orientation_review_needed.py" "C:\path\to\project"
python ".\03_TOOLS\scripts\project_validation\check_bom_has_datasheets.py" "C:\path\to\project"
python ".\03_TOOLS\scripts\project_validation\check_component_database_matches.py" "C:\path\to\project"
```

## Check IDs

Use `--checks` with the main validator for targeted reports:

```powershell
python ".\03_TOOLS\scripts\project_validation\validate_kicad_project.py" "C:\path\to\project" --checks project_files,missing_footprints,missing_3d_models
```

Available check IDs:

- `project_files`
- `project_libraries`
- `missing_footprints`
- `missing_3d_models`
- `cli_availability`
- `unconnected_power`
- `bom_datasheets`
- `component_database_matches`
- `connector_orientation`
- `polarity_review`
- `rf_layout_review`
- `interface_rule_review`

## Report Status

| Status | Meaning |
| --- | --- |
| `PASS` | The static check found no issue in its scope. |
| `WARN` | The check found unresolved review work or a static-analysis limit. |
| `FAIL` | Required source files, libraries, footprints, models, or tools are missing for that check. |

## Limits

- Static parsing does not replace KiCad ERC or DRC.
- Datasheet evidence is heuristic: symbol field, component database match, or local filename match.
- Connector, polarity, RF, USB, CAN, LIN, and automotive checks intentionally over-report for human review.
- Footprint correctness is never asserted unless an exact manufacturer drawing has been reviewed outside this script.
