# No-Progress Detector

## Purpose

Stop routing loops where Codex keeps producing reports, retries, or small
reroute attempts without real engineering progress.

## Trigger Rule

If two consecutive edit-required runs show any of these, the detector must
raise `BLOCKED_REPAIR_MODE`:

- no PCB hash change
- no unrouted or unconnected reduction
- DRC worsens
- the same blocker repeats

## Required `BLOCKED_REPAIR_MODE` Behavior

When blocked repair mode triggers, the workflow must:

1. stop broad routing
2. identify the exact repeated blocker
3. recommend one targeted repair
4. prevent another report-only loop

## Evidence Inputs

The detector should inspect:

- edit-required routing reports
- before/after PCB hashes
- unconnected and unrouted counts
- DRC trend
- repeated deferred or remaining blocker nets

## Output

The detector should emit:

- overall status
- edit-required run count
- no-progress event count
- exact repeated blocker
- recommended target stage
- recommended targeted repair

## Command

```powershell
python 14_LAYOUT_AUTOMATION\scripts\detect_no_progress.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE `
  --output-json 05_OUTPUTS\reliability\no_progress.json `
  --markdown 05_OUTPUTS\reliability\no_progress.md
```
