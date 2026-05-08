# Failed Attempt: Playwright Live Artifact Scan Quoting

Date: 2026-05-03
Status: `RESOLVED`

## What Failed

An `rg` command intended to search for live-mode evidence markers used a pattern with pipe characters and embedded quotes that PowerShell split incorrectly. A follow-up `Select-String -Recurse` attempt failed because this PowerShell version does not support the `-Recurse` parameter on `Select-String`.

## Resolution

The check was rerun with:

```powershell
Get-ChildItem -LiteralPath '31_PLAYWRIGHT_RESEARCH_PIPELINE\output','31_PLAYWRIGHT_RESEARCH_PIPELINE\evidence','31_PLAYWRIGHT_RESEARCH_PIPELINE\reports' -Recurse -File | Select-String -Pattern 'LIVE_PUBLIC_PAGE','live_web_used\": true','pdfs_downloaded\": true','BLOCKED_OR_LOGIN_REQUIRED'
```

No live-mode artifacts were found.

## Lesson

For recursive text searches in PowerShell with complex patterns, prefer piping `Get-ChildItem -Recurse -File` into `Select-String`.

