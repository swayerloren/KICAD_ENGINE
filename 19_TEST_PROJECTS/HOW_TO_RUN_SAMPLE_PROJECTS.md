# How To Run Sample Projects

Status: `PUBLIC_SAMPLE_RUN_GUIDE`

## Before You Start

Install or confirm:

- KiCad, including `kicad-cli` for workflows that generate evidence.
- Python for KiCad Engine scripts.
- PowerShell on Windows.
- VS Code if you are using Codex, Claude, or another coding agent.

Run the repo health check first:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\health_check.ps1
```

or:

```powershell
python .\health_check.py
```

## Run The Golden-Path Fixture Gate

From the repo root:

```powershell
.\03_TOOLS\scripts\project_gate\run_project_gate.ps1 -ProjectPath "19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board"
```

The runner writes a timestamped report folder under:

```text
05_OUTPUTS/gate_runs/
```

Open:

- `PROJECT_GATE_REPORT.md` for the human-readable report.
- `PROJECT_GATE_REPORT.json` for machine-readable gate output.

## Expected Current Result

The current ATtiny85 sample should report:

```text
BLOCKED_UNTIL_HUMAN_REVIEW
```

That is not a tool failure. It reflects the current evidence: ERC, DRC,
footprint, connector-orientation, polarity, and human visual review blockers are
still unresolved.

## Inspect The Project Evidence

Start with:

```text
19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md
19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_GATE_REPORT.md
19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_FINAL_AUDIT.md
```

Then inspect the latest gate run under:

```text
05_OUTPUTS/gate_runs/<timestamp>/PROJECT_GATE_REPORT.md
```

## What Not To Do

- Do not edit the imported original project.
- Do not generate fabrication outputs from a blocked sample.
- Do not relabel review outputs as final.
- Do not treat a failed or blocked gate as manufacturing approval.
- Do not claim the sample proves KiCad Engine is better than any other PCB AI
  tool.

## If You Want To Repair A Sample Later

A repair task must:

1. Target only the controlled sample copy under `19_TEST_PROJECTS/`.
2. Create a backup under `99_BACKUPS/pre_codex_edits/`.
3. Preserve attribution and license files.
4. Document the repair plan before editing KiCad files.
5. Rerun ERC, DRC, visual review, footprint audit, and the gate runner.
6. Keep any generated outputs `NOT_FINAL`.
