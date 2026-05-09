# Routing Work Git Cleanup Commands

Record kind: `workflow_run`
Status: `UNVERIFIED`
Created: `2026-05-09T07:46:38`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`

## Summary

Commands used to audit and remove the tracked `routing_work` scratch payload from Git while preserving the local files and the placeholder README.

## Details

- `git status --short --ignored`
- `git ls-files 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work`
- `Get-ChildItem 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/20260508_091428 -Recurse -File`
- `git check-ignore -v --no-index 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/20260508_091428 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/README.md`
- `git rm -r --cached -- 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/20260508_091428`
- validation commands for staged removals, on-disk existence, and tracked placeholder behavior

## Source Or Evidence

Command outputs established:

- `3300` tracked paths existed under `routing_work`
- `3299` tracked paths belonged to the timestamped scratch payload
- tracked payload size was about `278.02 MiB`
- the timestamped folder remained on disk after `git rm --cached`
- the cleanup did not touch the live project design files

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
