# Uncertainty Log - ESP32_CSI_WIFI_NODE Schematic Electrical Blockers

## Session

- Date: 2026-05-03
- Scope: Schematic electrical repair and gate update.

| Item | Severity | Confidence | Human review required | Status |
|---|---|---|---|---|
| AO3401A exact symbol pin mapping and footprint orientation | HIGH | HIGH | Yes | `BLOCKED_NEEDS_REVIEW` |
| USB VBUS/backfeed/power-sense policy | HIGH | HIGH | Yes | `BLOCKED_NEEDS_REVIEW` |
| USB shield EMC strategy | HIGH | HIGH | Yes | `BLOCKED_NEEDS_REVIEW` |
| Missing `PRE_SCHEMATIC_BOM_LOCK.md` | HIGH | HIGH | Yes | Missing input |
| Missing `SCHEMATIC_READY_PARTS_LIST.md` | HIGH | HIGH | Yes | Missing input |
| Missing `NEEDS_REVIEW_BEFORE_SCHEMATIC.md` | HIGH | HIGH | Yes | Missing input |
| Exact footprints and package drawings | HIGH | HIGH | Yes | Not verified |
| Connector orientation | HIGH | HIGH | Yes | Not verified |
| Polarity-sensitive part review | HIGH | HIGH | Yes | Not complete |
| Regulator passive MPNs/derating/layout | HIGH | HIGH | Yes | Not verified |
| USB-C connector/ESD/series resistor source review | HIGH | HIGH | Yes | Not complete |
| ESP32 EN/BOOT source verification | MEDIUM | MEDIUM | Yes | Not complete |
| Close-up visual review method | MEDIUM | HIGH | Yes if strict GUI screenshot review is required | SVG/source based, not GUI screenshot based |

## Outcome

Schematic-to-PCB gate remains `FAIL`.
