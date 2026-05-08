# Uncertainty Log: ESP32_CSI_WIFI_NODE Strict Visual Readability Re-Audit

Date: 2026-05-06

## Uncertainties

| Item | Confidence | Human Review Required | Notes |
|---|---|---:|---|
| Exact severity of every visible overlap in KiCad GUI | MEDIUM | YES | The audit inspected exported rendered crops. LJ should still inspect the KiCad GUI directly before approval. |
| Whether some dense labels are acceptable to LJ | MEDIUM | YES | The strict rule treats touching/crowded labels as visual fail. LJ can confirm design-style expectations. |
| Whether crop framing issues are tooling-only or schematic-layout issues | MEDIUM | YES | Some crops include adjacent blocks or clipping; next repair should improve both schematic spacing and block crop definitions if needed. |

## Final Uncertainty Status

The schematic is not approved. Remaining uncertainty does not justify passing the visual gate; it reinforces the need for another repair and LJ inspection.
