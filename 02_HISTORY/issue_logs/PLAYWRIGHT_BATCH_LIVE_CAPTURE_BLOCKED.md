# Issue Log: Playwright Batch Live Capture Blocked

Date: 2026-05-03

Status: `OPEN`

## Issue

Live Playwright browser capture cannot run because the local Node environment does not have the `playwright` package installed.

## Impact

- Batch expansion is dry-run-only.
- No screenshot evidence was captured.
- Source URLs remain source-link metadata, not live-captured evidence.
- All records remain `UNVERIFIED`.

## Required Resolution

Install Playwright only through an approved setup/tooling task, then rerun a small live pilot before expanding live captures.

