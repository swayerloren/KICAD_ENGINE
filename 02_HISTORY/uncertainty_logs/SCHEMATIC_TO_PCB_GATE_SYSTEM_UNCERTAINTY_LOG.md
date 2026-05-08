# Uncertainty Log - Schematic To PCB Gate System

## Session

- Date: 2026-05-03
- Scope: Schematic-to-PCB gate setup.

## Uncertainties

| Item | Severity | Confidence | Human review required | Notes |
|---|---|---|---|---|
| Actual schematic annotation status | HIGH | LOW | Yes | The gate system was created, but annotation was not audited. |
| ERC status | HIGH | HIGH | Yes | ERC was not run in this session; gate remains blocked. |
| Visual full-page and close-up review status | HIGH | HIGH | Yes | No visual exports or close-up review reports were created. |
| Electrical audit status | HIGH | HIGH | Yes | No electrical audit was run. |
| BOM lock status | HIGH | HIGH | Yes | No BOM lock audit was run. |
| Footprint/package drawing verification | HIGH | HIGH | Yes | No footprint audit was run. |
| Connector orientation status | HIGH | HIGH | Yes | No connector orientation review was run. |
| AO3401A pin mapping | HIGH | HIGH | Yes | Project-specific blocker remains unresolved. |
| USB VBUS/shield policy | HIGH | HIGH | Yes | Project-specific blocker remains unresolved. |
| ESP32 EN/BOOT verification | HIGH | HIGH | Yes | Not audited in this session. |
| Git-based no-design-file-change verification | MEDIUM | HIGH | No | Git metadata is absent, so `git status` and `git diff` cannot be used in this workspace. |
| Visual verification workflow file | MEDIUM | HIGH | No | `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md` was requested if present, but it is missing. |

## Required Resolution

The active project must stay blocked from PCB update until the missing evidence is created and the gate file is changed to `PASS`.
