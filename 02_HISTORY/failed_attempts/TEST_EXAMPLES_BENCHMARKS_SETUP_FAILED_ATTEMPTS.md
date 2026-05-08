# Test Examples Benchmarks Setup Failed Attempts

Date: 2026-05-03

## Failed Attempt 1

Type: patch context mismatch

What happened:

- A multi-file patch expected `15_BENCHMARKS/INDEX.md` to contain `Status: SCAFFOLD`, but the current file used `Status: METHODOLOGY_ONLY`.

Correction:

- Inspected the exact current index files and reapplied smaller targeted patches.

Lesson:

- Inspect generated/index files before applying broad multi-file patches.

## Failed Attempt 2

Type: noisy verification command

What happened:

- A PowerShell artifact scan used `-Include` with literal folder paths and returned Markdown files even though the intended scan was for KiCad/fab artifacts.

Correction:

- Re-ran the scan using an explicit extension filter in `Where-Object`.

Lesson:

- For extension-sensitive scans over literal directories, filter extensions explicitly instead of relying on `-Include`.

