# STM32F1 Pilot Bad rg Quoting

Date: 2026-05-03
Status: `RESOLVED`

## What Failed

A read-only `rg` command attempted to search for multiple KiCad symbol properties using escaped double quotes inside a PowerShell command. PowerShell split part of the pattern into an invalid path, and `rg` reported a filename/directory syntax error.

## Impact

No files were modified. The command was read-only and non-destructive.

## Resolution

The search was rerun with simpler single-quoted patterns:

- `rg -n 'STM32F103C8Tx' ...`
- `rg -n 'LQFP-48_7x7mm_P0.5mm' ...`

## Lesson

Use simple single-quoted regex patterns in PowerShell for `rg` when matching KiCad S-expression strings.
