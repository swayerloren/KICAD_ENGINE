# ESP32_CSI_WIFI_NODE Final PCB Visual Review Package Commands

Date: `2026-05-08`

Project: `ESP32_CSI_WIFI_NODE`

| Step | Command / Action | Purpose | Result |
| --- | --- | --- | --- |
| 1 | `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE` | Confirm maintenance gate before meaningful repo work | `PASS`; prompt count `1`, maintenance due `NO` |
| 2 | `Get-Content reports/FINAL_TRACE_BY_TRACE_AUDIT_REPORT.md` | Refresh routed-trace audit baseline | `PASS` |
| 3 | `Get-Content reports/FINAL_TRACE_REPAIR_LOG.md` | Refresh last accepted PCB repair details | `PASS` |
| 4 | `rg` on the live `.kicad_pcb` for key references and footprint positions | Recover render landmarks for USB, ESP32, power, test pads, and mounting holes | `PASS` |
| 5 | `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb render --help` | Confirm supported render options | `PASS` |
| 6 | `kicad-cli pcb render ... final_pcb_review_full_top.png` and `... final_pcb_review_full_bottom.png` | Generate fresh full-board top and bottom images | `PASS` |
| 7 | `kicad-cli pcb render ...` initial close-up batch using `--zoom` and `--pivot` | Attempt direct camera close-ups | `PARTIAL`; positive-pivot renders succeeded but some regions were misframed; negative-pivot values also hit PowerShell/KiCad argument parsing issues |
| 8 | `view_image` on fresh renders | Spot-check actual framing quality | `PASS`; confirmed the USB-area camera crop was not reliable enough |
| 9 | Inline Python/Pillow crop script over `final_pcb_review_full_top.png` and `final_pcb_review_full_bottom.png` | Create deterministic review crops for all requested regions | `PASS` |
| 10 | Additional `view_image` checks on the cropped outputs | Validate the final package imagery | `PASS` |
| 11 | `python 03_TOOLS/scripts/project_state/build_live_project_state.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply` | Refresh live-state packet references | `PASS`; confirmed live hash `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697` and `4` unrouted nets |
| 12 | `kicad-cli pcb drc --format json -o %TEMP%\\esp32_csi_final_pcb_visual_review_drc.json ...` | Run a fresh DRC for the packet | `PASS`; `0` violations, `17` unconnected items |
| 13 | `apply_patch` | Create packet, checklist, visual manifest, closeout logs, and memory/workflow updates | `PASS` |
| 14 | `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason \"final PCB visual review package\" --apply` | Increment project prompt counter | `PASS`; `1 -> 2`, maintenance due `NO` |
| 15 | `python 03_TOOLS/scripts/memory_history/build_memory_index.py --repo-root .` | Rebuild memory index | `PASS` |
| 16 | `python 03_TOOLS/scripts/memory_history/build_history_index.py --repo-root .` | Rebuild history index | `PASS` |
| 17 | `python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .` | Rebuild startup known-problems file | `PASS` |
