# Portability Remaining Gaps

Record kind: `issue_log`
Status: `OPEN`
Created: `2026-05-08T18:37:00`
Scope: `global`
Project: `N/A`

## Summary

The repo is now better documented and tooled for ZIP-first portability, but some older tracked artifacts still weaken the self-contained story.

## Details

1. `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work` is still a large tracked historical scratch payload that includes copied `.kicad_pcb`, `.kicad_pro`, `.kicad_prl`, and DRC scratch files.
2. `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/*.json` still contain machine-local library URIs from earlier indexing work.
3. `00_CODEX_START/TOOL_INDEX.md` still carries machine-specific inventory content by design. It is now labeled, but it is not a portable source of assumptions.
4. `CURRENT_STATUS.md` remains time-sensitive and can drift quickly after new commits or engineering work.

## Source Or Evidence

- `05_OUTPUTS/release_readiness/PORTABILITY_TOOLCHAIN_AUDIT_REPORT.md`
- `05_OUTPUTS/release_readiness/HARDCODED_PATH_PORTABILITY_AUDIT.md`
- git inventory commands
- hardcoded-path scan results

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
