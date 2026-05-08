# COPPER_ZONE_STRATEGY_BLOCKED_UNCERTAINTY_LOG

Date: 2026-05-03

## Uncertainties

| Item | Confidence | Blocking | Notes |
|---|---|---|---|
| Top/bottom GND zone geometry | `HIGH_UNCERTAINTY` | Yes | No PCB outline exists. |
| Zone priority and orphan policy | `HIGH_UNCERTAINTY` | Yes | No zones, stackup, or constraints exist. |
| Thermal relief policy | `HIGH_UNCERTAINTY` | Yes | No footprints, pad current roles, or power copper exist. |
| ESP32 antenna keepout | `HIGH_UNCERTAINTY` | Yes | No module placement or source-backed keepout exists. |
| USB keepout and return path | `HIGH_UNCERTAINTY` | Yes | No connector/ESD placement or USB layout evidence exists. |
| Regulator/power copper | `HIGH_UNCERTAINTY` | Yes | No regulator placement, current/thermal evidence, or source layout evidence exists. |
| GND islands/orphans | `UNKNOWN` | Yes | No zones exist to inspect. |

## Required Future Evidence

- `.kicad_pcb` file.
- Board outline and stackup.
- Placement pass reports.
- Hole/test-pad/via strategy pass.
- Source-backed ESP32 antenna keepout.
- USB and regulator placement/layout evidence.
- DRC and visual outputs after zone setup.

