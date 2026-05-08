# Footprint Gap Analysis Secret Scan False Positives

Date: 2026-05-03
Status: `RESOLVED`

## What Happened

An initial broad secret-scan pattern matched ordinary text such as `task-specific` and installed KiCad library metadata containing PDF source URLs.

## Impact

No secrets were found. The broad scan was too permissive for `sk-` tokens and produced false positives.

## Correction

The scan was rerun with a stricter token pattern:

```text
sk-[A-Za-z0-9_-]{20,}|api[_-]?key\s*=|token\s*=|password\s*=
```

The stricter scan returned `0` matches.

## Lesson

Use realistic token lengths for secret scans so normal words containing `sk-` do not become false positives.

