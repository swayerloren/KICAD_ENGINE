# Failed Attempt: Playwright Batch Markdown Report Generation Quoting

Date: 2026-05-03

Status: `RESOLVED`

## Attempt

Generate batch Markdown summaries from a large inline PowerShell command.

## Failure

PowerShell parsed part of a Markdown bullet string as an operator in a mixed quoted array and stopped before writing the intended Markdown files.

## Resolution

Created explicit report files and downstream summary files instead. No partial report files from the failed command were used.

## Lesson

For long generated Markdown with many interpolated strings, prefer a dedicated script, explicit file templates, or smaller apply-patch edits instead of a large inline PowerShell array.

