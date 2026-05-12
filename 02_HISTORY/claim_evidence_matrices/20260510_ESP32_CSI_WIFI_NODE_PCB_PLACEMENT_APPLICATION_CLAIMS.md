# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| The prelayout placement precondition failed. | `reports/PCB_PRELAYOUT_RECOMMENDED_VARIANT.md` |
| No real PCB placement was applied in this task. | unchanged PCB hash, blocked-state reports, and absence of `.kicad_pcb` diff |
| `J2` is placement-proven for the bottom edge. | `reports/PCB_PRELAYOUT_CONNECTOR_ORIENTATION_AUDIT.md` |
| `U2` antenna keepout direction is placement-proven for the top edge. | `reports/PCB_PRELAYOUT_CONNECTOR_ORIENTATION_AUDIT.md` |
| `J1` remains unresolved for real placement approval. | `reports/PCB_PRELAYOUT_CONNECTOR_ORIENTATION_AUDIT.md` |
| Routing rehearsal may not begin from this request. | `reports/PCB_PLACEMENT_APPLICATION_REPORT.md`, `memory/CURRENT_PROJECT_STATE.md` |
