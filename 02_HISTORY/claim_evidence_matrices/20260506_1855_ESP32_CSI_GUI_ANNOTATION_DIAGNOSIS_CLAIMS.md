# Claim/Evidence Matrix: ESP32 CSI GUI Annotation Diagnosis

Date: `2026-05-06`

| Claim | Status | Evidence | Notes |
| --- | --- | --- | --- |
| Eeschema is open on the exact active schematic path. | `VERIFIED_BY_COMMAND` | `Get-CimInstance Win32_Process` command log | Command line includes the exact target path. |
| The KiCad GUI document is modified/unsaved. | `VERIFIED_BY_COMMAND` | `Get-Process` main window title starts with `*` | In KiCad window titles, leading `*` conventionally indicates modified/unsaved document state. |
| The saved active disk file has zero bad placed-symbol refs. | `VERIFIED_BY_COMMAND` | Structured Python parser output in command log | Parsed actual placed-symbol blocks, not only general text search. |
| The saved active disk file passes local CLI ERC. | `VERIFIED_BY_COMMAND` | `GUI_MISMATCH_DIAGNOSIS_ERC_FROM_REPO_ROOT.rpt`, `GUI_MISMATCH_DIAGNOSIS_ERC_FROM_PROJECT_DIR.rpt` | Both report 0 errors and 0 warnings. |
| The GUI still shows `?` refs. | `VERIFIED_BY_USER` | LJ task statement | Codex did not independently inspect GUI symbol graphics. |
| CLI and GUI are showing different states. | `PARTIALLY_VERIFIED` | User observation plus saved-file parse/ERC plus unsaved GUI title | Strong inference; exact GUI object table was not extracted. |
| KiCad-native annotation was run by Codex. | `CONTRADICTED` | `KICAD_NATIVE_ANNOTATION_RESULT.md` | Codex did not run it. |
| Manual KiCad-native annotation is required next. | `REQUIRES_HUMAN_REVIEW` | GUI state is unsaved and unsafe for automation | LJ must use KiCad GUI annotation and save. |
| Visual cleanup may resume now. | `CONTRADICTED` | `KICAD_NATIVE_ANNOTATION_RESULT.md` | Visual cleanup remains blocked. |
| PCB update is allowed. | `CONTRADICTED` | `SCHEMATIC_TO_PCB_GATE_STATUS.md` remains fail | PCB update remains blocked. |
