# KiCad GUI Automation

## Purpose

This folder defines the safe GUI control layer for KiCad/Eeschema actions that cannot be proven through raw file edits or `kicad-cli`.

It exists because the `ESP32_CSI_WIFI_NODE` schematic showed question-mark references in the KiCad GUI even after saved-file and CLI checks claimed annotation was clean. Future agents must treat KiCad's live GUI/native workflow as a separate evidence source.

## What Belongs Here

- Windows KiCad/Eeschema window discovery.
- Unsaved GUI state detection.
- Exact open schematic path checks.
- Screenshot helpers.
- Safety-gated wrappers for native annotation, save, and GUI ERC workflows.
- Reports about GUI automation readiness and failure modes.

## What Does Not Belong Here

- KiCad design source files.
- PCB layout, routing, zones, or manufacturing automation.
- Random coordinate-click scripts.
- Secrets or credentials.
- Claims that GUI annotation is automated before it is tested on a copied project.

## Current Status

Status: `GUI_NATIVE_ANNOTATION_VERIFIED_ON_ESP32_CSI_WIFI_NODE`

Available:

- PowerShell process/window discovery.
- Unsaved `*` title detection.
- Exact path matching against the expected active schematic.
- Screenshot helper script when run through the existing `windows_gui` Python environment.
- Dry-run/manual fallback helpers for annotation, save, and GUI ERC.
- Verified live native annotation workflow on `ESP32_CSI_WIFI_NODE` with dialog open, annotation apply, GUI save, GUI ERC `Violations (0)`, post-save `kicad-cli` ERC pass, 0 unresolved `?` references, and 0 duplicate references.
- Dry-run-first auto-open workflow for launching the exact target `.kicad_pro`, opening/focusing Eeschema, confirming the target `.kicad_sch`, and then handing off to native annotation.

Still limited:

- The verified live flow is approved only for schematic annotation/save/ERC under the documented gates.
- It does not approve schematic visual cleanup, footprint assignment, PCB update, layout, routing, zones, or manufacturing outputs.
- New projects must still pass exact path, backup, screenshot, unsaved-state, and UI-control gates before any GUI action.
- Auto-open from closed state is implemented in dry-run mode and requires explicit `--live` for any launch. Live open-from-closed-state has not been tested in this setup task.

Success record:

- `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`

## Mandatory Rule

For annotation tasks, Codex/Claude must use KiCad-native annotation through verified GUI automation or stop and tell LJ exactly how to run KiCad's Annotate Schematic tool manually. Raw `.kicad_sch` text edits are not sufficient proof of annotation success.

The accepted proof is the full annotation gate: native annotation applied, schematic saved from KiCad GUI, GUI ERC 0 violations when safely automatable, `kicad-cli` ERC pass after GUI save, saved schematic scan with 0 unresolved `?` references, and duplicate-reference scan pass.

## First Safe Command

```powershell
.\33_KICAD_GUI_AUTOMATION\scripts\windows\detect_unsaved_kicad_state.ps1 `
  -ExpectedSchematicPath "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch" `
  -Json
```
