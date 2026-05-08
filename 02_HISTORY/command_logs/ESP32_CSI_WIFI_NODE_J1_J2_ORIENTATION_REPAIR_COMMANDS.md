# ESP32_CSI_WIFI_NODE J1/J2 Orientation Repair Commands

Status: `ACTIVE_EVIDENCE`

Date: `2026-05-07`

## Key Commands And Results

| Command | Result |
|---|---|
| `python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply` | Counter `2 -> 3`; maintenance due `NO`. |
| `python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 5` | Returned `BLOCKED`; stale conflict logged because current project state allows placement/mechanical repair. |
| `Copy-Item -Recurse ...` | Backup created at `99_BACKUPS\pre_codex_edits\20260507_132053_ESP32_CSI_WIFI_NODE_pre_J1_J2_orientation_repair`. |
| `kicad-cli pcb drc ... --schematic-parity` | Final result: `13` DRC violations, `78` unconnected items, `0` schematic parity issues. |
| `kicad-cli pcb export svg ... j1_j2_orientation_repair_top.svg` | Top 2D SVG created. |
| `kicad-cli pcb export svg ... j1_j2_orientation_repair_bottom.svg --mirror` | Bottom 2D SVG created. |
| `kicad-cli pcb render ... j1_j2_orientation_repair_3d_full_top.png` | Full top 3D render created. |
| `kicad-cli pcb render ... j1_j2_orientation_repair_3d_bottom_edge_front.png --side front` | Bottom-edge 3D front view created. |
| `kicad-cli pcb render ... j2_orientation_repair_3d_closeup.png` | J2 close-up 3D render created. |
| `kicad-cli pcb render ... j1_orientation_repair_3d_blocker_closeup.png` | J1 blocker-evidence render created; barrel-jack 3D body absent because model is missing. |

## Failed Or Noisy Attempts

- PowerShell rejected a Bash-style Python heredoc probe.
- `git diff` was unavailable because this checkout is not detected as a Git repository by `git`.
- `kicad-cli pcb render --pivot` does not accept a negative first vector component as a separate option value; a broader bottom-edge pivot was used for J1 blocker evidence.
- Some `kicad-cli` commands emitted a project lock parse warning for an empty `.kicad_pro`, but the requested export/render files were still created.

## Generated Evidence

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\J1_J2_FOOTPRINT_GEOMETRY_ORIENTATION_AUDIT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\J1_J2_BOTTOM_EDGE_ORIENTATION_REPAIR_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\J1_J2_CONNECTOR_ORIENTATION_PROOF.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\BOTTOM_EDGE_CONNECTOR_DRC_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\J1_J2_ORIENTATION_REPAIR_REVIEW.md`
