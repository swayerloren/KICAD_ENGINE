# Failed Attempt: rg Dollar Pattern Quoting

Date: 2026-05-03
Status: `RESOLVED`

## What Failed

An `rg` command intended to search for `$rel`, `$name`, and related marker strings in the generator source returned no matches because the dollar-sign pattern was awkward under PowerShell quoting.

## Impact

No files were modified by the failed command.

## Resolution

Used `Select-String` for the source file and `rg --fixed-strings` for the target datasheet tree.

## Lesson

For literal dollar-sign markers in PowerShell, prefer `rg --fixed-strings` or `Select-String -SimpleMatch` style searches.
