# Claim Evidence Matrix: ESP32_CSI_WIFI_NODE GUI Native Annotation

Date: `2026-05-06`

| Claim | Status | Evidence |
|---|---|---|
| The active Eeschema window matched the target schematic path. | `VERIFIED_BY_COMMAND` | `detect_unsaved_kicad_state.ps1` output recorded in `KICAD_GUI_NATIVE_ANNOTATION_RUN_REPORT.md`. |
| A backup was created before GUI annotation. | `VERIFIED_BY_FILE` | `99_BACKUPS/pre_codex_edits/20260506_210316_ESP32_CSI_WIFI_NODE_before_native_gui_annotation`. |
| KiCad native Annotate Schematic dialog opened. | `VERIFIED_BY_GUI_EVIDENCE` | UIA dump and screenshot `native_annotation_dialog_after_apply_20260506_210316.bmp`. |
| Annotation was applied and schematic was saved from GUI. | `VERIFIED_BY_GUI_EVIDENCE` | GUI title cleared `*`; KiCad status text reported schematic saved. |
| GUI ERC was run and showed zero violations. | `VERIFIED_BY_GUI_EVIDENCE` | UIA reported `Violations (0)` after `Run ERC`. |
| CLI ERC passed after GUI save. | `VERIFIED_BY_COMMAND` | `KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.raw.txt`. |
| Saved schematic has no unresolved or duplicate references. | `VERIFIED_BY_FILE` | `KICAD_GUI_NATIVE_ANNOTATION_REFERENCE_TABLE.md/json`. |
| PCB update remains blocked. | `VERIFIED_BY_REPO_RULE` | Annotation-only task did not clear visual, footprint, electrical, or schematic-to-PCB gates. |

