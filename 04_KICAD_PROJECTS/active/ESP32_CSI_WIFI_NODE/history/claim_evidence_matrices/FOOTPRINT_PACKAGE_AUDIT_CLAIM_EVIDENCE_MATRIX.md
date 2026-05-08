# FOOTPRINT_PACKAGE_AUDIT_CLAIM_EVIDENCE_MATRIX

Status: `COMPLETED`

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

| Claim | Status | Evidence | Human review required |
| --- | --- | --- | --- |
| Active KiCad project and schematic were located. | `VERIFIED_BY_FILE` | `kicad/ESP32_CSI_WIFI_NODE.kicad_pro`; `kicad/ESP32_CSI_WIFI_NODE.kicad_sch` | No |
| The schematic has 43 physical symbols. | `VERIFIED_BY_COMMAND` | Read-only Python parse using `schematic_check_common` | No |
| The schematic has 0 assigned physical footprints. | `VERIFIED_BY_COMMAND` | Read-only Python parse output `with_footprints=0` | No |
| The schematic has 0 populated physical datasheet fields. | `VERIFIED_BY_COMMAND` | Read-only Python parse output `with_datasheets=0` | No |
| Every current component footprint verification fails. | `VERIFIED_BY_COMMAND` | No physical symbol has a footprint assignment; package-to-footprint evidence cannot exist in schematic assignments. | Yes |
| USB-C connector orientation and pin numbering are unresolved. | `PARTIALLY_VERIFIED` | `J2` has USB-C symbol/value but no exact MPN, footprint, drawing, or datasheet field. | Yes |
| AO3401A-class PMOS pin/footprint mapping is blocked. | `VERIFIED_BY_FILE` | `SCHEMATIC_ELECTRICAL_AUDIT.md`; Q1 value includes `PINMAP_BLOCKED_NEEDS_REVIEW`. | Yes |
| 3D model checks cannot be performed meaningfully. | `VERIFIED_BY_COMMAND` | No footprints are assigned, so no footprint-linked model references exist to inspect. | Yes |
| Schematic-to-PCB gate remains FAIL. | `VERIFIED_BY_FILE` | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` updated with footprint audit blocker. | Yes |

