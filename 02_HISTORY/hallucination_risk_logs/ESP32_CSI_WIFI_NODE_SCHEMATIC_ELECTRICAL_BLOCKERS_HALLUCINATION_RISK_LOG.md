# Hallucination Risk Log - ESP32_CSI_WIFI_NODE Schematic Electrical Blockers

## Risk Label

`MEDIUM_RISK`

## Main Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Treating clean ERC as permission to start PCB layout. | HIGH | Gate status remains `FAIL`; no PCB update allowed. |
| Treating AO3401A as verified because its name appears in the schematic. | HIGH | Q1 explicitly says `PINMAP_BLOCKED_NEEDS_REVIEW`. |
| Treating USB VBUS/shield policy as selected. | HIGH | USB VBUS and shield strategy remain blocked in schematic notes, audit, and gate. |
| Treating C1 `>=16V` text as exact MPN approval. | MEDIUM | Audit states exact MPN/derating/footprint remain `NEEDS_REVIEW`. |
| Treating SVG/source visual review as full GUI visual signoff. | MEDIUM | Close-up review documents its limitation. |

## Outcome

No unverified footprint, policy, or manufacturing-readiness claim was promoted. Remaining high-risk items are documented blockers.
