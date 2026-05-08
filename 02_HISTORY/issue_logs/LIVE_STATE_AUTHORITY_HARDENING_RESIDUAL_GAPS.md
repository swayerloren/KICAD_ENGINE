# Live State Authority Hardening Residual Gaps

Date: `2026-05-08`
Status: `OPEN`

## Residual Gap

`TASK_CONTRACT_FAILURE` is available in the canonical live-state gate wrapper,
but not every existing caller injects a task contract yet.

## Risk

Some workflows may still omit `--task-contract`, which means the gate checker
cannot emit `TASK_CONTRACT_FAILURE` for that run even though the support exists.

## Recommended Follow-Up

- Add a top-level launcher or CI check that always passes the declared contract
  file into gate decisions for meaningful project runs.
