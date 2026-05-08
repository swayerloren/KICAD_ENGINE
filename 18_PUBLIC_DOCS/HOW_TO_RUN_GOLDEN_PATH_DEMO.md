# How To Run The Golden-Path Demo

Status: `PUBLIC_DEMO_GUIDE`

## What The Demo Is

The current golden-path demo fixture is:

```text
19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board
```

It is a controlled copy of an open-source ATtiny85 KiCad project. KiCad Engine
uses it to demonstrate local-first, KiCad-native, AI-assisted project review
from VS Code with Codex, Claude, or a similar agent.

## Honest Status

The fixture is not a clean passing design.

Current status:

- `CONTROLLED_DEMO_FIXTURE`
- `GOLDEN_PATH_PARTIAL`
- `BLOCKED_UNTIL_HUMAN_REVIEW`

Known blockers include ERC, DRC, footprint/package, connector orientation,
polarity, visual-review, and fab-readiness issues.

## Run The Demo Gate

From the repo root:

```powershell
.\03_TOOLS\scripts\project_gate\run_project_gate.ps1 -ProjectPath "19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board"
```

Expected result:

```text
BLOCKED_UNTIL_HUMAN_REVIEW
```

This result means the runner is working. The demo is designed to show that KiCad
Engine refuses to call a project ready when evidence is failing or incomplete.

## Open The Reports

After running the command, open the newest folder under:

```text
05_OUTPUTS/gate_runs/
```

Read:

- `PROJECT_GATE_REPORT.md`
- `PROJECT_GATE_REPORT.json`

Then inspect the controlled sample status:

- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_GATE_REPORT.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_FINAL_AUDIT.md`

## What The Demo Proves

- KiCad Engine can preserve attribution for an imported open KiCad project.
- KiCad Engine can maintain a controlled test copy separate from raw imports.
- KiCad Engine can aggregate ERC, DRC, visual, footprint, sync, unrouted, and
  fabrication-readiness evidence.
- KiCad Engine can block a sample honestly instead of claiming a false pass.

## What The Demo Does Not Prove

- It does not prove ERC passes.
- It does not prove DRC passes.
- It does not prove the PCB is electrically correct.
- It does not prove footprints or connector orientation are verified.
- It does not prove manufacturing readiness.
- It does not prove KiCad Engine is better than any cloud PCB AI tool.

## Attribution

Read:

```text
19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/ORIGINAL_SOURCE_ATTRIBUTION.md
```

The sample preserves MIT license evidence, but public payload inclusion still
requires final human release review.

## Safety

Do not generate fabrication outputs from this demo while it is blocked. If a
future task generates review outputs, they must be clearly labeled `NOT_FINAL`.
