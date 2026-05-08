# Failed Attempt - README Link Validation False Negative

- Date: `2026-05-08`
- Task: GitHub README workflow rewrite

## What Failed

The first local Markdown-link validation helper reported `README.md: missing FOR%20CHAT%20GPT.MD`.

## Root Cause

The validator treated the URL-encoded path literally and did not decode the encoded space in the filename.

## Resolution

- Changed the README link target to angle-bracket syntax for the file with spaces.
- Reran validation with a helper that understands angle-bracket paths.
- Final result: `LINK_CHECK_PASS`
