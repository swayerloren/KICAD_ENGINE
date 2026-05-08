# Task-Type Execution Contract

This folder defines the KiCad Engine execution contract for meaningful Codex runs.

The contract exists to stop false completion of KiCad engineering tasks that only
update reports or Markdown while claiming PCB work happened.

## Purpose

Every meaningful run must declare exactly one task type.

The declared task type determines whether KiCad design files are allowed to
change, and what proof is required before the run may be treated as complete.

## Task Types

- `DOCS_ONLY`
- `AUDIT_ONLY`
- `LIVE_STATE_RECONCILE`
- `PLACEMENT_EDIT_REQUIRED`
- `ROUTING_EDIT_REQUIRED`
- `PCB_EDIT_REQUIRED`
- `GITHUB_DOCS_ONLY`

## Hard Rules

- `DOCS_ONLY` cannot edit KiCad design files.
- `AUDIT_ONLY` cannot edit KiCad design files.
- `LIVE_STATE_RECONCILE` cannot edit KiCad design files.
- `GITHUB_DOCS_ONLY` cannot edit KiCad design files.
- `PLACEMENT_EDIT_REQUIRED` must prove a real `.kicad_pcb` change.
- `ROUTING_EDIT_REQUIRED` must prove a real `.kicad_pcb` change.
- `PCB_EDIT_REQUIRED` must prove a real `.kicad_pcb` change or explicit
  `NO_DESIGN_CHANGE_NEEDED`.
- If an `*_EDIT_REQUIRED` run ends with only report or Markdown changes, the
  required final status is:
  `EDIT_REQUIRED_FAILED_NO_ENGINEERING_ARTIFACT_CHANGE`

## Canonical Files

- `task_contract.schema.json`
  - JSON schema reference for contract shape.
- `validate_task_contract.py`
  - Validates a contract and returns pass/fail plus a recommended final status.
- `enforce_edit_required.py`
  - Hard-fails edit-required contracts that do not prove engineering artifact
    change.
- `write_task_contract_report.py`
  - Writes a Markdown report from the contract plus validation result.
- `examples/`
  - Minimal example contracts for the supported task types.

## Contract Shape

The contract JSON is intentionally simple:

- `task_type`
- `task_summary`
- `project_path`
- `target_pcb`
- `changed_files`
- `declared_final_status`
- `notes`
- `evidence`

Common `evidence` fields:

- `backup_created`
- `backup_path`
- `pcb_hash_before`
- `pcb_hash_after`
- `no_design_change_needed`
- `drc_run`
- `drc_report_path`
- `visual_export_attempted`
- `visual_paths`
- `unconnected_before`
- `unconnected_after`
- `unrouted_before`
- `unrouted_after`
- `trace_change_log_updated`
- `placement_report_updated`

## Examples

Validate an example contract:

```powershell
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 03_TOOLS\scripts\execution_contract\examples\docs_only.json
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 03_TOOLS\scripts\execution_contract\examples\routing_edit_required.json
```

Enforce edit-required proof:

```powershell
python 03_TOOLS\scripts\execution_contract\enforce_edit_required.py --contract 03_TOOLS\scripts\execution_contract\examples\pcb_edit_required.json
```

Write a Markdown execution report:

```powershell
python 03_TOOLS\scripts\execution_contract\write_task_contract_report.py `
  --contract 03_TOOLS\scripts\execution_contract\examples\routing_edit_required.json `
  --output 05_OUTPUTS\execution_contract_example_report.md
```

## Result Expectations

For non-edit task types, validation fails if any changed file is a KiCad design
file such as:

- `.kicad_sch`
- `.kicad_pcb`
- `.kicad_pro`

For edit-required task types, validation fails if the contract does not prove
the required engineering artifact change and evidence set.

The validator and enforcer both return non-zero when the contract is invalid.
