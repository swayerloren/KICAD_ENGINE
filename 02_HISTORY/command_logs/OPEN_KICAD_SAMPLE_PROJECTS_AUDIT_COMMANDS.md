# Open KiCad Sample Projects Audit Commands

Date: `2026-05-03`

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

Status: `COMMAND_LOG_COMPLETE`

## Safety

- Scope was limited to `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/`.
- No repairs were made.
- No KiCad source files were intentionally modified.
- No Gerbers, drill files, pick-and-place files, or fabrication packages were generated.
- Generated audit outputs were written under `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/`.

## Tool Version

`kicad-cli --version`

Observed result:

`9.0.7`

## Discovery And Help Checks

Commands used to confirm read-only KiCad CLI capabilities:

```powershell
kicad-cli sch erc --help
kicad-cli pcb drc --help
kicad-cli sch export svg --help
kicad-cli pcb export svg --help
kicad-cli pcb export pdf --help
```

## Audit Runner

A local Python audit pass was used to:

- locate `.kicad_pro`, `.kicad_sch`, and `.kicad_pcb` files
- inventory files
- parse placed schematic symbols and footprint fields
- resolve project-local footprint library tables where present
- run `kicad-cli` ERC and DRC
- export schematic SVG and PCB top/bottom SVG views
- summarize annotation, missing-footprint, missing-3D-model, and generated-output findings
- create per-sample reports and a master report

The first static parser pass was corrected because it overcounted schematic library symbol templates as placed duplicate references and did not resolve project-local `fp-lib-table` entries. The corrected pass generated the final reports now referenced by this log.

## KiCad CLI Commands Captured

The complete generated command summary is stored at:

`32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/sample_engineering_audit_command_summary.json`

Representative commands:

```powershell
kicad-cli sch erc --format report --severity-all --exit-code-violations --output <sample>_erc.rpt <sample>.kicad_sch
kicad-cli pcb drc --format report --severity-all --schematic-parity --exit-code-violations --output <sample>_drc.rpt <sample>.kicad_pcb
kicad-cli sch export svg --black-and-white --output schematic_svg <sample>.kicad_sch
kicad-cli pcb export svg --mode-single --page-size-mode 2 --fit-page-to-board --layers F.Cu,F.Mask,F.SilkS,Edge.Cuts --output <sample>_pcb_top.svg <sample>.kicad_pcb
kicad-cli pcb export svg --mode-single --page-size-mode 2 --fit-page-to-board --mirror --layers B.Cu,B.Mask,B.SilkS,Edge.Cuts --output <sample>_pcb_bottom.svg <sample>.kicad_pcb
```

## Results Summary

| sample | ERC command | DRC command | visual export |
| --- | --- | --- | --- |
| `esp_rs_esp_rust_board` | exit code 5, violations present | exit code 5, violations present | schematic/top/bottom SVG export passed |
| `m4a1x_tps5430` | exit code 5, warnings present | exit code 5, violations present | schematic/top/bottom SVG export passed |
| `tomasr8_attiny85_dev_board` | exit code 5, violations present | exit code 5, violations present | schematic/top/bottom SVG export passed |

## Documentation Updates

Updated files:

- `32_OPEN_KICAD_SAMPLE_INTAKE/INDEX.md`
- `15_BENCHMARKS/README.md`
- `15_BENCHMARKS/tasks/OPEN_SAMPLE_IMPORT_BENCHMARK_CANDIDATES.md`
- `12_REFERENCE_DESIGN_LIBRARY/00_INDEX/REFERENCE_DESIGN_INDEX.md`
- `FOR CHAT GPT.MD`

Created files:

- `02_HISTORY/design_reviews/OPEN_KICAD_SAMPLE_PROJECTS_MASTER_AUDIT.md`
- `02_HISTORY/sessions/OPEN_KICAD_SAMPLE_PROJECTS_AUDITED.md`
- `02_HISTORY/issue_logs/OPEN_KICAD_SAMPLE_PROJECTS_AUDIT_BLOCKERS.md`
- `02_HISTORY/quality_gate_failures/OPEN_KICAD_SAMPLE_PROJECTS_NOT_PROMOTION_READY.md`
- AI-quality closeout records under `02_HISTORY/ai_self_reviews`, `ai_scorecards`, `claim_evidence_matrices`, `uncertainty_logs`, and `hallucination_risk_logs`

## Closeout Validation Commands

Report-presence validation:

```powershell
$required = @(
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/SAMPLE_PROJECTS_MASTER_AUDIT.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_ENGINEERING_AUDIT.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_ERC_DRC_REPORT.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_VISUAL_AUDIT.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_GATE_STATUS.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_ENGINEERING_AUDIT.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_ERC_DRC_REPORT.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_VISUAL_AUDIT.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_GATE_STATUS.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_ENGINEERING_AUDIT.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_ERC_DRC_REPORT.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_VISUAL_AUDIT.md',
  '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_GATE_STATUS.md',
  '02_HISTORY/design_reviews/OPEN_KICAD_SAMPLE_PROJECTS_MASTER_AUDIT.md',
  '02_HISTORY/sessions/OPEN_KICAD_SAMPLE_PROJECTS_AUDITED.md',
  '02_HISTORY/command_logs/OPEN_KICAD_SAMPLE_PROJECTS_AUDIT_COMMANDS.md'
)
$required | ForEach-Object { [pscustomobject]@{Path=$_; Exists=(Test-Path $_)} }
```

Result: all required paths existed.

Generated-output check:

```powershell
Get-ChildItem -Path '32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/engineering_audit_artifacts' -Recurse -File |
  Where-Object { $_.Extension -match '\.(gbr|drl|zip|pos|csv)$' -or $_.Name -match 'gerber|drill|fabrication|production' }
```

Result: no generated Gerber, drill, package zip, pick-and-place, or fabrication-style output was found in the audit artifact folder.

Index rebuilds:

```powershell
python '03_TOOLS/scripts/indexing/build_repo_index.py'
python '03_TOOLS/scripts/indexing/build_memory_index.py'
python '03_TOOLS/scripts/indexing/build_history_index.py'
python '03_TOOLS/scripts/indexing/build_known_problems.py'
python '03_TOOLS/scripts/ai_quality/build_ai_quality_index.py'
python '32_OPEN_KICAD_SAMPLE_INTAKE/scripts/build_sample_index.py'
```

Results:

- repo, memory, history, known-problems, and AI-quality indexes rebuilt successfully.
- sample index script wrote a dry-run report at `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/sample_index_dry_run.md`.
- `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md` now references the open sample audit issue, uncertainty, hallucination-risk, and quality-gate failure records.

Additional validation:

```powershell
git status --short
```

Result: unavailable in this checkout because no `.git` metadata was present.

```powershell
$cutoff=(Get-Date).AddMinutes(-45)
Get-ChildItem -Path '32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples' -Recurse -Include *.kicad_pro,*.kicad_sch,*.kicad_pcb |
  Where-Object { $_.LastWriteTime -gt $cutoff }
```

Result: no recently modified KiCad project, schematic, or PCB source files were reported during closeout validation.
