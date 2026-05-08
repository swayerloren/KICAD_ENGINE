# How To Verify A Project

Status: `PUBLIC_PROJECT_VERIFICATION_GUIDE`

## Verification Philosophy

KiCad Engine verification is evidence-based. A project is not ready because an
AI agent says it is ready. It is only ready for the next step when the required
reports, source evidence, visual checks, and human-review gates support that
claim.

## One-Command Gate Runner

Use the project gate runner to aggregate existing evidence:

```powershell
.\03_TOOLS\scripts\project_gate\run_project_gate.ps1 -ProjectPath "PATH\TO\PROJECT"
```

For the current sample:

```powershell
.\03_TOOLS\scripts\project_gate\run_project_gate.ps1 -ProjectPath "19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board"
```

The runner creates:

```text
05_OUTPUTS/gate_runs/<timestamp>/PROJECT_GATE_REPORT.md
05_OUTPUTS/gate_runs/<timestamp>/PROJECT_GATE_REPORT.json
```

## What The Runner Checks

- Schematic annotation evidence.
- ERC report evidence.
- Schematic visual export and close-up review evidence.
- Footprint/package audit evidence.
- PCB sync/parity evidence.
- DRC report evidence.
- PCB visual export and close-up review evidence.
- Unrouted-net evidence from DRC.
- Fabrication readiness gate evidence.

## Important Limit

The runner is read-only. It parses existing reports. If evidence is missing, it
returns `INCOMPLETE` or a blocker instead of pretending the project passed.

To create missing evidence, use the appropriate workflow under:

- `.prompts/kicad_pipeline/`
- `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
- `03_TOOLS/scripts/kicad_schematic_checks/`
- `03_TOOLS/kicad/run_schematic_visual_check.ps1`

## Result Labels

- `PASS`: evidence supports all gates, but human review is still required before fabrication.
- `FAIL`: a required gate failed or evidence is incomplete.
- `PARTIAL`: no hard failure, but warnings or limited evidence remain.
- `BLOCKED_UNTIL_HUMAN_REVIEW`: high-risk items require human review.

## Before Manufacturing Outputs

Do not generate Gerbers, drills, pick-and-place, STEP, or fab packages unless
the final PCB verification explicitly says:

```text
READY_FOR_NOT_FINAL_FAB_EXPORT
```

Even then, generated outputs must remain `NOT_FINAL` until final human review.
