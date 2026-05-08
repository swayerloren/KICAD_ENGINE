# Pre-PCB Checklist

Status: `REQUIRED_BEFORE_PCB_EDITS`

Use this checklist before creating or editing KiCad PCB layout files. It does not authorize PCB update by itself; the schematic-to-PCB gate must also pass when moving from schematic to board.

## Required Before Layout

| Check | Required Result |
| --- | --- |
| Schematic gate | `SCHEMATIC_TO_PCB_GATE_STATUS.md` is `PASS`, or the task is explicitly planning-only. |
| ERC | Latest ERC pass report exists, or blocker is documented. |
| PCB sync | Update-from-schematic report exists for layout work. |
| Board outline | Known dimensions and mechanical constraints, or blocked for user review. |
| Stackup/design rules | Known fab profile or conservative project rules; no fake fab limits. |
| Backup | PCB backup created before board edits. |

## Component Evidence

| Evidence | Required Before Layout |
| --- | --- |
| Footprints | Every footprint has candidate and verification status. |
| High-risk footprints | Connector, PMOS, ESD, regulator, RF, module, and polarity parts have human-review status. |
| 3D models | Missing or unverified models are listed without blocking electrical layout unless mechanical fit depends on them. |
| Connectors | Exact drawing, board-edge direction, pin numbering, mating part, and orientation review are recorded or blocked. |
| Polarity | Diodes, LEDs, electrolytics/tantalums, polarized connectors, and MOSFETs are listed for orientation review. |
| Critical nets | USB, CAN, RF, clocks, high-current, switching regulator, and sensitive analog nets are identified. |

## Layout Planning

- Placement zones planned before moving parts.
- Power path order and current loops identified.
- Keepouts, courtyards, mounting holes, board edge, and antenna areas identified.
- Net classes, trace widths, clearances, and via strategy documented.
- Visual close-up checks listed for post-placement and post-routing review.

## Stop Conditions

Stop if connector drawings, package drawings, board outline, fab limits, antenna keepout, USB path constraints, regulator layout requirements, or critical mechanical constraints are unknown. Record `PCB_LAYOUT_BLOCKED` instead of guessing.
