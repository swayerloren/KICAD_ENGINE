# Claim Evidence Matrix: KiCad Native Annotation Workflow Documentation Update

Date: `2026-05-06`

| Claim | Status | Evidence |
|---|---|---|
| Native GUI annotation succeeded for `ESP32_CSI_WIFI_NODE`. | `VERIFIED_BY_FILE` | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/KICAD_GUI_NATIVE_ANNOTATION_RUN_REPORT.md` |
| GUI ERC showed 0 violations. | `VERIFIED_BY_FILE` | `KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.md` |
| `kicad-cli` ERC passed after GUI save. | `VERIFIED_BY_FILE` | `KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.md` |
| Saved schematic had 0 unresolved `?` references and 0 duplicates. | `VERIFIED_BY_FILE` | `KICAD_GUI_NATIVE_ANNOTATION_REFERENCE_TABLE.md` |
| Future annotation tasks should not rely on raw text edits as proof. | `VERIFIED_BY_RULE` | `AGENTS.md`, `START_HERE.md`, `KICAD_ANNOTATION_DO_AND_DO_NOT.md` |
| PCB update remains blocked. | `VERIFIED_BY_RULE` | Schematic-to-PCB gate rules and updated docs. |

