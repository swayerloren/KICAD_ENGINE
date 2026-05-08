# NOT_FINAL Fab Export Select-String Quoting Failure

Date: 2026-05-03

Status: `RESOLVED_WITH_SIMPLER_VALIDATION_COMMAND`

## What Failed

A final validation `Select-String` command failed with:

`The string is missing the terminator: ".`

## Cause

The command used a backtick-heavy search pattern while validating Markdown content.

## Resolution

The validation was rerun with simpler single-quoted patterns.

## Impact

No KiCad design files were edited. No manufacturing outputs were generated.

