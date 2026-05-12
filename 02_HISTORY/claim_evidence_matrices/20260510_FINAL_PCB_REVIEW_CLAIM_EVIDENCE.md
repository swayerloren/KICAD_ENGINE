# Claim Evidence Matrix

Date: `2026-05-10`

| Claim | Evidence | Confidence |
|---|---|---|
| Final classification is `BLOCKED_BEFORE_NOT_FINAL_EXPORT`. | `reports/FINAL_ROUTED_PCB_REVIEW.md`; `pcb_quality_gate_result.json` fail codes | High |
| ERC evidence passes. | `reports/SCHEMATIC_ERC_AFTER_VISUAL_CLEANUP.md` | High |
| Live board still has `22` parity issues, `13` unconnected items, and `3` detectable unrouted nets. | `reports/pcb_quality_gate/20260510_quality_gate_creation_v2/pcb_quality_gate_result.json` | High |
| J2 passes orientation and U2 passes antenna-direction proof. | `reports/mechanical_orientation/20260510_usb_c_orientation_audit.json`; `reports/mechanical_orientation/20260510_esp32_antenna_orientation_audit.json` | High |
| J1 still needs human review. | `reports/mechanical_orientation/20260510_barrel_jack_orientation_audit.json` | High |
| Existing final visual assets are stale against the live PCB hash. | `_verification/pcb_visual/FINAL_PCB_REVIEW_PACKAGE.md`; live hash from current `.kicad_pcb` | High |
