# STM32 Source Link Research Validation Command Failure

Date: 2026-05-03
Status: `RESOLVED`

## Scope

Global STM32 source-link indexing closeout validation.

## What Failed

The first CSV validation command used Bash heredoc syntax:

```text
python - <<'PY'
```

That syntax is invalid in the active PowerShell shell and failed before the Python validation could run.

## Impact

No repository files were modified by the failed command. The intended validation was rerun with a PowerShell-compatible here-string and passed.

## Correction

Use this PowerShell-compatible pattern for inline Python in this workspace:

```powershell
@'
print("validation")
'@ | python -
```

## Reusable Lesson

Match inline shell syntax to the active shell. This workspace uses PowerShell for local command execution in the current environment.

## Verification

The rerun validation confirmed:

- STM32 CSV headers matched the required schema.
- STM32 CSV row counts were generated as expected.
- All per-family source-link documents were present.
- No PDFs were found under the STM32 datasheet tree.
- Targeted secret scan returned no matches.
