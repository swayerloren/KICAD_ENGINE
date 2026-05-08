# User Correction: Automated Visual Pass Was Not Human Readability

Date: 2026-05-06  
Status: USER_CONFIRMED

## Correction

LJ identified that the ESP32_CSI_WIFI_NODE schematic was visually unacceptable in KiCad even though prior reports claimed visual/annotation improvements.

## Behavior Change Required

Codex and Claude must not treat automated crop generation, ERC pass, annotation pass, hidden footprint fields, populated footprint fields, or no `?` references as human-readable schematic approval.

## Evidence

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/EMERGENCY_CURRENT_SCHEMATIC_TRUTH_AUDIT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/STRICT_VISUAL_READABILITY_REAUDIT.md`
- `02_HISTORY/design_reviews/KICAD_ENGINE_SCHEMATIC_FAILURE_ROOT_CAUSE_AUDIT.md`

## Routing

This correction has been promoted to global memory because it applies to all KiCad schematic visual review workflows.
