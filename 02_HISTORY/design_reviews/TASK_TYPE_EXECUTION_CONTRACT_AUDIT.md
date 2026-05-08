# Task-Type Execution Contract Audit

Date: `2026-05-08`

Branch: `hardening/execution-contract`

## Purpose

Audit the repo failure mode where PCB edit and routing tasks could appear
complete after producing only reports or Markdown without proving that the real
engineering artifact changed.

## Root Cause

The workspace already had strong phase gates, maintenance, and live-state
reconciliation, but it did not have a repo-wide execution contract that forced
each meaningful run to declare its task type and prove the required engineering
artifact changes.

That gap allowed this failure mode:

- the task request implied real PCB work
- reports and logs were created
- the final answer could look complete
- but there was no single formal contract requiring proof that the `.kicad_pcb`
  hash changed or that an allowed no-change outcome was explicit

## Changes Added In This Hardening Pass

### New execution-contract layer

Created under `03_TOOLS/scripts/execution_contract/`:

- `README.md`
- `task_contract.schema.json`
- `validate_task_contract.py`
- `enforce_edit_required.py`
- `write_task_contract_report.py`
- `examples/docs_only.json`
- `examples/audit_only.json`
- `examples/pcb_edit_required.json`
- `examples/routing_edit_required.json`

### Repo rule wiring

Updated:

- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `00_CODEX_START/START_HERE.md`
- `00_CODEX_START/SESSION_CLOSEOUT_CHECKLIST.md`
- `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_WORKFLOW.md`

## Contract Rules Now Enforced

- Every meaningful run must declare exactly one task type.
- `DOCS_ONLY`, `AUDIT_ONLY`, `LIVE_STATE_RECONCILE`, and `GITHUB_DOCS_ONLY`
  may not change KiCad design files.
- `PCB_EDIT_REQUIRED` must prove:
  - backup created
  - `.kicad_pcb` hash before
  - `.kicad_pcb` hash after
  - hash changed or explicit `NO_DESIGN_CHANGE_NEEDED`
  - DRC run
  - visual export attempted
- `ROUTING_EDIT_REQUIRED` must prove:
  - backup created
  - `.kicad_pcb` hash before
  - `.kicad_pcb` hash after
  - hash changed
  - DRC run
  - unrouted/unconnected before and after
  - trace-change log updated
  - visual export attempted
- `PLACEMENT_EDIT_REQUIRED` must prove:
  - backup created
  - `.kicad_pcb` hash before
  - `.kicad_pcb` hash after
  - hash changed
  - placement report updated
  - DRC run
  - visual export attempted
- If an `*_EDIT_REQUIRED` task ends with only docs or report changes, the
  required result is `EDIT_REQUIRED_FAILED_NO_ENGINEERING_ARTIFACT_CHANGE`.

## Validation Run

Python syntax check:

- `PASS`

Example contract validation:

- `docs_only.json`: `PASS`
- `audit_only.json`: `PASS`
- `pcb_edit_required.json`: `PASS`
- `routing_edit_required.json`: `PASS`

## Scope Safety

- No `.kicad_sch` files edited
- No `.kicad_pcb` files edited
- No routing performed
- No manufacturing outputs generated

## Remaining Gap

The execution contract is now documented, validated, and enforceable through the
new scripts, but runtime enforcement still depends on agents and workflows
calling the contract tools. A future wrapper or CI gate could make invocation
automatic.
