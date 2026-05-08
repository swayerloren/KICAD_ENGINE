# Auto Sandbox Approval System Audit

Date: `2026-05-07`

Scope: replace manual-only sandbox approval language with an evidence-based auto-approval gate for real PCB work.

## What Changed

- added sandbox auto-approval rules, decision engine, status codes, and start rules
- added auto-approval and auto-blocked templates
- updated startup, workflow, checklist, and memory docs to require objective sandbox approval instead of generic LJ approval
- updated the active `ESP32_CSI_WIFI_NODE` sandbox gate to use exact auto-block reasons

## Key Review Result

The repo no longer requires generic LJ approval before PCB update or placement when the sandbox can prove objective readiness.

The new rule is:

- `AUTO_APPROVED_FOR_PCB_WORK` -> sandbox may support real PCB work
- any `AUTO_BLOCKED_*` status -> sandbox remains blocked and must list exact missing evidence

## Active Project Result

`ESP32_CSI_WIFI_NODE` remains blocked.

Primary reason:

- `AUTO_BLOCKED_DRC_PRECHECK_FAIL`

Additional blockers:

- upstream schematic-to-PCB gate still `FAIL`
- all physical footprints still blank
- board dimensions still assumption-only

## No-KiCad-Edit Check

This task changed workflow, memory, and report markdown only.
