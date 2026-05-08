# Footprint Capture Schema

Status: `SCHEMA_DRAFT`

| Field | Required | Notes |
| --- | --- | --- |
| `manufacturer` | Yes | Manufacturer or generic target. |
| `manufacturer_part_number` | Yes | MPN or generic target label. |
| `package_name_from_source` | No | Candidate package text only. |
| `package_drawing_source_url` | No | Required for drawing-level verification. |
| `kicad_symbol_candidates` | No | Candidate symbols only. |
| `kicad_footprint_candidates` | No | Candidate footprints only. |
| `kicad_3d_model_candidates` | No | Candidate 3D models only. |
| `footprint_match_status` | Yes | Default `UNVERIFIED`. |
| `pinout_status` | Yes | Default `UNVERIFIED`. |
| `connector_orientation_status` | Yes | Default `UNVERIFIED` or `NOT_APPLICABLE`. |
| `human_review_required` | Yes | Default `true`. |
| `notes` | No | Include high-risk warnings. |

## High-Risk Rule

Connector, RF connector, PMOS/MOSFET, ESD array, MCU module, regulator, mounting-hole, and test-pad records must remain human-review-required unless exact package/mechanical drawing and orientation evidence exists.

