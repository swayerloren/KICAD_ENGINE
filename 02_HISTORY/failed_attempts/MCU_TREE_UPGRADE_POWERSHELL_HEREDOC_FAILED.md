# Failed Attempt: PowerShell Heredoc Syntax

Date: 2026-05-03
Status: `RESOLVED`

## What Failed

A summary command used Bash-style heredoc syntax:

```text
python - <<'PY'
```

PowerShell rejected it with a missing file specification / reserved operator parse error.

## Impact

No files were modified by the failed command.

## Resolution

The command was rerun using a PowerShell here-string piped to Python:

```text
@'
...
'@ | python -
```

## Lesson

Use PowerShell-compatible here-strings or `python -c` in this workspace.
