# Failed Attempt - Git Status Unavailable During Golden Path Sample Promotion

Date: `2026-05-03`

Status: `NON_BLOCKING`

## Attempt

Command:

```powershell
git status --short
```

## Result

The command failed because this checkout is not a Git repository:

```text
fatal: not a git repository (or any of the parent directories): .git
```

## Impact

This did not block the promotion task. File-level validation was performed directly instead.

## Lesson

Do not depend on Git metadata in this checkout. Use file inventories and generated indexes when `.git` is unavailable.

