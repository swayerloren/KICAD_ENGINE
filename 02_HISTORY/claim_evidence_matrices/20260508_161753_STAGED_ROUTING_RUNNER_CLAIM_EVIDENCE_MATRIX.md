# Claim Evidence Matrix

| Claim | Evidence |
| --- | --- |
| Ten routing stages are defined. | `14_LAYOUT_AUTOMATION/scripts/routing_stage_contracts.py` |
| The runner blocks broad routing when repair mode is active. | `14_LAYOUT_AUTOMATION/scripts/staged_routing_runner.py` |
| The detector can replay ESP32 routing history. | `14_LAYOUT_AUTOMATION/scripts/detect_no_progress.py` and `05_OUTPUTS/reliability/NO_PROGRESS_DETECTOR.json` |
| The current history contains a real stalled handoff between Batch 04 and Batch 05. | `05_OUTPUTS/reliability/NO_PROGRESS_DETECTOR.md` |
| No KiCad design files were edited in this task. | `git status`, file scope, and absence of `.kicad_*` changes |
