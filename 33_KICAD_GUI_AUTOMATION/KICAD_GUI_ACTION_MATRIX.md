# KiCad GUI Action Matrix

| Action | Default | Required Gates | Notes |
| --- | --- | --- | --- |
| Detect KiCad windows | `ALLOWED_READ_ONLY` | none | Uses PowerShell process/window inspection. |
| Detect Eeschema path | `ALLOWED_READ_ONLY` | none | Must be run before GUI control. |
| Detect unsaved state | `ALLOWED_READ_ONLY` | none | Title starting with `*` means dirty GUI state. |
| Screenshot Eeschema | `ALLOWED_WITH_CAPTURE_FLAG` | path match | Does not edit files. |
| Open exact KiCad project | `DRY_RUN_DEFAULT_LIVE_WITH_FLAG` | no conflicting Eeschema window, exact `.kicad_pro`, explicit `--live` | Launches only the requested project manager; no PCB or manufacturing actions. |
| Open/focus schematic editor | `DRY_RUN_DEFAULT_LIVE_WITH_FLAG` | exact project manager window, detectable schematic control, explicit `--live` | Prefer UIA-detected `Schematic` control; stop if ambiguous. |
| Ensure Eeschema open | `DRY_RUN_DEFAULT_LIVE_WITH_FLAG` | combines detection, exact project launch, schematic editor open, path verification | Stop on different project or dirty `*` title. |
| Annotate schematic | `ALLOWED_AFTER_GATES_FOR_NATIVE_ANNOTATION` | all gates | Verified on `ESP32_CSI_WIFI_NODE` on 2026-05-06. Use KiCad-native workflow or manual fallback. |
| Save schematic | `ALLOWED_AFTER_BACKUP_PATH_MATCH_AND_APPROVAL` | all gates plus user save approval if dirty | Can overwrite disk; never default on a dirty `*` title without explicit approval. |
| Run GUI ERC | `ALLOWED_AFTER_GATES_FOR_ANNOTATION_VALIDATION` | path match, screenshot | GUI ERC is preferred when validating the live state; CLI ERC remains saved-file evidence only. |
| Move symbols/text | `PROHIBITED_IN_THIS_LAYER` | N/A | Use explicit schematic visual repair task instead. |
| Edit values | `PROHIBITED_IN_THIS_LAYER` | N/A | Not GUI automation scope. |
| Assign footprints | `PROHIBITED_IN_THIS_LAYER` | N/A | Requires footprint/package gate. |
| PCB update/layout/routing/zones | `PROHIBITED` | N/A | Not allowed here. |
| Manufacturing output | `PROHIBITED` | N/A | Not allowed here. |
