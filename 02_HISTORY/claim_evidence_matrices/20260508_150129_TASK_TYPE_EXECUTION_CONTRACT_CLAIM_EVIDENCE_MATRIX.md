# Claim / Evidence Matrix

Date: `2026-05-08`

Task: `TASK_TYPE_EXECUTION_CONTRACT`

| Claim | Evidence |
| --- | --- |
| A new execution-contract layer was created. | Files added under `03_TOOLS/scripts/execution_contract/`. |
| Edit-required task types now have explicit proof rules. | `task_contract.schema.json`, `validate_task_contract.py`, `enforce_edit_required.py`, `AGENTS.md`, `START_HERE.md`, and `REAL_PROJECT_ROUTING_WORKFLOW.md`. |
| The new scripts are syntactically valid Python. | `python -m py_compile ...` run recorded in `TASK_TYPE_EXECUTION_CONTRACT_COMMANDS.md`. |
| The validator works on the requested examples. | Four successful validator runs recorded in `TASK_TYPE_EXECUTION_CONTRACT_COMMANDS.md`. |
| No KiCad design files were edited in this task. | `git status` scope and file-change list; all edited paths are docs, memory, history, and scripts only. |
