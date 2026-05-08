# Failed Attempts - Open KiCad Sample Import

Date: `2026-05-03`

Status: `RECOVERED`

## Context

Task: import only approved open-license KiCad sample projects from `32_OPEN_KICAD_SAMPLE_INTAKE/candidates/CANDIDATE_INDEX.md`.

Approved first batch:

- `tomasr8/attiny85-dev-board`
- `M4a1x/TPS5430`
- `esp-rs/esp-rust-board`

## Failed Attempt 1 - PowerShell Boolean Expression

Command class: import guard command.

Problem:

- Used `Test-Path $original -or Test-Path $normalized`.
- PowerShell parsed `-or` as a `Test-Path` parameter and stopped before download/import.

Result:

- No repository was downloaded before this failure.
- A staging folder existed at `05_OUTPUTS/open_sample_import_staging/20260503_first_batch`.
- The command was corrected by evaluating each `Test-Path` call separately.

Lesson:

- In PowerShell, wrap boolean expressions around complete expressions: `(Test-Path $a) -or (Test-Path $b)`.

## Failed Attempt 2 - Empty Copy From Extracted ZIP

Command class: copy imported archive contents into sample folders.

Problem:

- Used `Copy-Item -LiteralPath (Join-Path $root.FullName '*')`.
- `-LiteralPath` did not expand the wildcard and produced empty destination folders.

Result:

- Empty `imported_originals` and `normalized_samples` folders were created.
- Initial audit reports at `20260503T181513Z` and `20260503T181514Z` describe the empty-copy state and are stale.

Recovery:

- Verified destinations were empty.
- Re-copied from staging extracts with `Get-ChildItem -LiteralPath $root.FullName -Force | Copy-Item -Destination ... -Recurse -Force`.
- Re-ran populated file audits with `_populated_20260503T181554Z` / `_populated_20260503T181555Z` names.

Lesson:

- For PowerShell archive extraction copy operations, enumerate children explicitly before `Copy-Item` when using `-LiteralPath`.

## Current Status

The import was recovered. Populated originals and normalized copies exist for all three approved samples. Do not delete the stale audit reports; they are retained as evidence of the failed attempt.
