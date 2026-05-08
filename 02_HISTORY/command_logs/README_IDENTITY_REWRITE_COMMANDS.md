# README Identity Rewrite Commands

Record kind: `workflow_run`
Status: `UNVERIFIED`
Created: `2026-05-08T21:06:00`
Scope: `global`
Project: `N/A`

## Summary

Major commands used for the GitHub-facing KiCad Engine identity rewrite.

## Details

- `git status --short`
- `Get-Content README.md`
- `Get-Content START_HERE.md`
- `Get-Content CURRENT_STATUS.md`
- `Get-Content PROJECTS_INDEX.md`
- `Get-Content WORKFLOWS_INDEX.md`
- `Get-Content TOOLS_INDEX.md`
- `Get-Content ONE_PROMPT_START.md`
- `Get-Content DOWNLOAD_ZIP_START_HERE.md`
- `Get-Content AGENT_STARTER_PROMPTS.md`
- `Get-Content .github/README.md`
- grep/readback scans against the rewritten docs
- changed-file scan confirming no `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files were modified

## Source Or Evidence

Command outputs were used to validate:

- README identity no longer leads with `ESP32_CSI_WIFI_NODE`
- ZIP -> VS Code -> prompt startup is explicit
- `04_KICAD_PROJECTS/active`, `archive`, and `templates` are explained
- the repo is presented as Codex/Claude + local KiCad workflow infrastructure

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
