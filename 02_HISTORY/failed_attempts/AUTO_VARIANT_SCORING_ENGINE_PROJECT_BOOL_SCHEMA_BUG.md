# Failed Attempt - Auto Variant Scoring Engine Project Bool Schema Bug

Date: `2026-05-07`

## What Failed

`auto_approve_selected_variant.py` incorrectly treated `project` as a required boolean field inside the approval-context schema.

## Symptom

The approval result returned:

- `AUTO_BLOCKED_MISSING_DATA`
- `Invalid context fields: project`

even though the context file was valid.

## Resolution

Removed `project` from the required boolean-field tuple and reran syntax-check plus dry-run approval.

