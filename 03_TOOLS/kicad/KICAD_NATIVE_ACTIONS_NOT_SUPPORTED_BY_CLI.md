# KiCad Native Actions Not Supported By CLI

Status: `MANDATORY_REFERENCE`

## Purpose

This file records KiCad actions that should use the native GUI workflow or a verified GUI automation layer instead of raw text edits.

## Native GUI Required Or Preferred

| Action | Why CLI/text edit is not enough | Required handling |
| --- | --- | --- |
| Annotate Schematic | `kicad-cli` does not expose schematic annotation in this environment, and text edits may not update the live GUI state. | Use verified GUI automation or tell LJ to run `Tools -> Annotate Schematic -> Re-annotate all symbols -> Save`. |
| Save active schematic GUI state | The GUI may contain unsaved changes not present on disk. | Detect `*` title, confirm path, create backup, get explicit approval before saving. |
| Clear/update ERC markers | GUI-visible ERC markers may reflect unsaved or stale state. | Run ERC in GUI when validating what LJ sees. |
| Run GUI ERC | CLI ERC checks the saved file; GUI ERC checks the live project state. | Use GUI ERC or manual LJ ERC when GUI state is disputed. |
| Screenshot actual schematic view | CLI exports may not match the open modified GUI view. | Capture Eeschema screenshot when LJ reports GUI-visible problems. |
| Interactively verify rendered layout | Human readability depends on what is visible. | Inspect rendered PNG/crops or GUI screenshots; do not infer from file scans. |

## Mandatory Annotation Rule

For annotation tasks, Codex/Claude must use KiCad-native annotation via verified GUI automation or stop and instruct LJ to run KiCad's Annotate Schematic tool manually.

Raw `.kicad_sch` text edits are not sufficient proof of annotation success.

Cross-reference: `10_KNOWLEDGE_BASE/kicad_core/KICAD_GUI_VS_CLI_ACTIONS.md`.

## Verified Native Annotation Success

`ESP32_CSI_WIFI_NODE` proved the required native GUI workflow on `2026-05-06`:

- Eeschema was detected on the exact active schematic path.
- A backup was created before GUI action.
- The KiCad native `Annotate Schematic` dialog opened.
- Annotation was applied.
- The schematic was saved from KiCad GUI.
- GUI ERC showed `Violations (0)`.
- `kicad-cli` ERC passed after GUI save.
- Saved schematic scan showed 0 unresolved `?` references.
- Duplicate-reference scan passed.

Evidence: `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md`.

## Auto-Open Project Support

If Eeschema is not open, future agents should not fail immediately with `NO_EESCHEMA_WINDOW`. They may use the dry-run-first workflow in `33_KICAD_GUI_AUTOMATION/KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md` to launch the exact target `.kicad_pro`, open/focus the schematic editor, verify the exact target `.kicad_sch`, and then run native actions.

Hard stops still apply:

- stop if Eeschema is open for a different project
- stop if the title starts with `*` unless LJ explicitly approves preserving/saving that GUI state
- stop if schematic editor controls are ambiguous
- never open PCB editor, route, update PCB, or generate manufacturing outputs from this workflow
