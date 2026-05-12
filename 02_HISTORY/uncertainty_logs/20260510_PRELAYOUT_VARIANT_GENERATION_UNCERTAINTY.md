# Uncertainty Log - Prelayout Variant Generation

- Uncertain item: Final mechanical proof for `J1`.
- Why uncertain: The barrel-jack orientation audit found the correct geometric opening direction, but the exact 3D model file is unresolved on this machine.
- Risk level: `HIGH`
- Required evidence: Resolved exact 3D model or equivalent approved human proof for the exact barrel-jack part and footprint.
- Human review required: `YES`
- Tracking: `02_HISTORY/issue_logs/20260510_ESP32_CSI_WIFI_NODE_PRELAYOUT_VARIANT_PACKET_BLOCKED.md`

- Uncertain item: Whether the live board can be repaired to match the winning routing-first plan without placement edits.
- Why uncertain: The current run was planning-only and did not modify the real PCB.
- Risk level: `MEDIUM`
- Required evidence: A future approved PCB-edit run plus fresh DRC and geometry evidence.
- Human review required: `YES`
- Tracking: same issue log above.
