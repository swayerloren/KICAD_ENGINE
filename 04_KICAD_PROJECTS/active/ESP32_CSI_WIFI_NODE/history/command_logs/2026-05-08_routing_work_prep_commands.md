# Routing Work Prep Commands

Date: `2026-05-08`

- checked prompt counter and maintenance-due state
- recorded live PCB timestamp and SHA256
- created backup and routing-work snapshot folder
- ran `kicad-cli pcb drc --format json` for the baseline
- extracted live placement, net status, ratsnest grouping, and raw trace snapshot
- checked phase 8 gate output to confirm live evidence controls the block
- cleaned the timed-out zero-byte trace CSV stub after stopping session-owned orphan KiCad Python processes
- incremented the project prompt counter for this task
- ran the canonical maintenance cycle and reset the prompt counter to `0`
