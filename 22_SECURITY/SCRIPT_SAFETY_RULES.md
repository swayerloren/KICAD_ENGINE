# Script Safety Rules

Status: `ACTIVE_POLICY`

## Defaults

Scripts should be read-only unless their purpose and output path are explicit.

## Required Behavior

- Fail gracefully when tools are missing.
- Ask before installing anything.
- Avoid destructive operations.
- Avoid writing to Program Files, app bundles, or global KiCad library paths.
- Write reports to `02_HISTORY` or `05_OUTPUTS` unless another safe path is documented.

## Review Gate

Scripts that edit KiCad files require active project confirmation, backup, rollback plan, and verification plan.

