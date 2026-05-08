# Claim/Evidence Matrix - ESP32_CSI_WIFI_NODE J1/J2 Orientation Repair

Status: `ACTIVE_EVIDENCE`

Date: `2026-05-07`

| Claim | Evidence | Status |
|---|---|---|
| J2 rotation is `0 deg` | PCB file, installed USB-C footprint, PCB Edge line transforms to bottom Edge.Cuts | `PROVEN` |
| J2 mouth faces downward/off-board | `j2_orientation_repair_3d_closeup.png`, `j1_j2_orientation_repair_3d_bottom_edge_front.png` | `PROVEN` |
| J1 rotation is `180 deg` | Barrel jack F.Fab/F.CrtYd front side local `-Y` transforms to bottom edge | `PROVEN_2D_ONLY` |
| J1 3D mouth proof exists | Referenced barrel-jack STEP model missing | `NOT_PROVEN` |
| No routing was performed | PCB edit scope and DRC still reports unconnected items | `PROVEN` |
| DRC schematic parity is clean | Final DRC reports `0` schematic parity issues | `PROVEN` |
