# Knowledge Base Reference Design Setup Failed Attempts

Date: 2026-05-02

## Failed Attempt 1

Type: command syntax error

What happened:

- A PowerShell required-file verification command initially used a pipeline after a `foreach` construct in a way PowerShell rejected.

Observed result:

- Error: `An empty pipe element is not allowed.`

Correction:

- Re-ran the check inside an `& { ... }` script block.

Lesson:

- For multi-line PowerShell verification commands, wrap collection logic in an explicit script block before piping.

## Failed Attempt 2

Type: patch context mismatch

What happened:

- A large patch for reference-design index/schema/template files failed because the expected context in `REFERENCE_RECORD_TEMPLATE.md` did not match the current file.

Correction:

- Inspected the current file content and reapplied smaller, targeted patches.

Lesson:

- For generated or frequently edited docs, inspect exact current context before applying multi-file patches.

