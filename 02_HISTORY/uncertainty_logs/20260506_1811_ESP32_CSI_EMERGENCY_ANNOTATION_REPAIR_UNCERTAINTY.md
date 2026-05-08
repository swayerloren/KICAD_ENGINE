# Uncertainty Log: ESP32_CSI Emergency Annotation Repair

Date: `2026-05-06`

Risk label: `MEDIUM_RISK`

## Uncertainties

| Item | Status | Impact | Required Follow-Up |
| --- | --- | --- | --- |
| Live KiCad GUI state | `UNVERIFIED` | An already-open KiCad window may show stale annotation until the saved schematic is reloaded. | LJ should reload/reopen the schematic if the GUI still displays `?` references. |
| Human-readable schematic quality | `UNVERIFIED_AND_PREVIOUSLY_FAILED` | Annotation repair does not prove readability. | Run strict visual readability repair/re-audit before LJ visual approval. |
| Footprint/package verification | `UNVERIFIED` | PCB update remains unsafe. | Exact package drawings and human review required. |
| Connector orientation and PMOS/USB policy | `UNVERIFIED` | PCB update remains blocked. | Human/source-backed decisions required. |

## Non-Claims

- No claim was made that the schematic is visually acceptable.
- No claim was made that footprints are verified.
- No claim was made that PCB update is allowed.
- No claim was made that fabrication outputs are ready.
