# Issue: Playwright Research Pipeline Live Mode Untested

Date opened: 2026-05-03
Status: `OPEN`
Severity: `MEDIUM`

## Issue

`31_PLAYWRIGHT_RESEARCH_PIPELINE` has dry-run and guarded live-mode scripts, but live browser capture has not been run or validated.

## Reason

The setup task explicitly avoided live web browsing unless explicitly safe and approved. No approval was given for live browser runs.

## Required Closure Criteria

- User explicitly approves a small public-page live-mode pilot.
- Source profile is reviewed before the run.
- Page is public and does not require login.
- Script stops on CAPTCHA, blocking, or unclear terms.
- Evidence output confirms `LIVE_PUBLIC_PAGE` only for allowed public pages.
- No credentials, cookies, PDFs, or private page data are stored.

