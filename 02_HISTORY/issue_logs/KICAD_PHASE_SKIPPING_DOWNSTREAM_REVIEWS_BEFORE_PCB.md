# Issue Log - KiCad Phase Skipping Downstream Reviews Before PCB

Status: `OPEN_RISK_MITIGATED_BY_PHASE_GATE`

Date: `2026-05-07`

## Problem

Agents previously created or attempted downstream JLCPCB, mechanical/3D, BOM production, production-fix, NOT_FINAL export, upload feedback, and final signoff review artifacts for `ESP32_CSI_WIFI_NODE` before `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb` existed.

## Impact

This is a high-risk workflow failure because later reports can appear to imply engineering progress even when the required PCB artifact and earlier evidence do not exist.

## Mitigation Added

- Mandatory phase order added at `00_CODEX_START/KICAD_PHASE_ORDER.md`.
- Phase-gate workflow added at `09_ACCURACY_ENGINE/workflows/MANDATORY_KICAD_PHASE_GATE.md`.
- No-phase-skipping rule added at `09_ACCURACY_ENGINE/verification_rules/NO_PHASE_SKIPPING_RULES.md`.
- PCB phase checklist added at `09_ACCURACY_ENGINE/checklists/PCB_PHASE_GATE_CHECKLIST.md`.
- Read-only checker added at `03_TOOLS/scripts/project_gate/check_phase_allowed.py`.

## Current ESP32_CSI_WIFI_NODE State

`ESP32_CSI_WIFI_NODE.kicad_pcb` is still missing. The next allowed project phase is Phase 2, PCB Creation / Update From Schematic, when LJ approval and schematic evidence are in scope.

