# PCB Quality Gate Creation Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-10T14:25:22`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Summary

The gate is authoritative for the implemented checks, but some layout quality aspects still depend on heuristics or external proof layers.

## Details

Trace geometry, TP topology, power width, and USB sanity use deterministic extraction plus configured thresholds. Connector orientation still depends on the mechanical truth layer, and barrel-jack proof remains incomplete when exact 3D evidence is missing. The gate therefore fails closed or marks NEEDS_HUMAN_REVIEW instead of guessing.

## Evidence

03_TOOLS/scripts/pcb_quality/_pcb_quality_common.py; 03_TOOLS/scripts/mechanical_orientation/; 08_COMPONENT_DATABASE/mechanical_orientation/; 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_quality_gate/20260510_quality_gate_creation_v2/connector_orientation.json

## Issue

Do not treat a connector as proven from edge XY plus rotation alone, and do not treat missing 3D/mechanical evidence as a pass.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
