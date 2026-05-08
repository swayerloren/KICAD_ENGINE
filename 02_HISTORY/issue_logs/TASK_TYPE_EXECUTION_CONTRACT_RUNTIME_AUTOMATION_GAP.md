# Task Type Execution Contract Runtime Automation Gap

Date: `2026-05-08`

Status: `OPEN`

## Issue

The task-type execution contract now exists as scripts plus repo rules, but
runtime enforcement still depends on agents or workflows calling the validator
and enforcer. There is not yet one unavoidable wrapper or CI gate that forces
contract invocation for every meaningful run.

## Risk

- agents can still ignore the contract if they bypass documented workflow
- false completion risk is reduced but not eliminated until invocation is more
  automatic

## Recommended Follow-Up

- integrate `validate_task_contract.py` or `enforce_edit_required.py` into a
  shared session wrapper, CI gate, or release-quality check
