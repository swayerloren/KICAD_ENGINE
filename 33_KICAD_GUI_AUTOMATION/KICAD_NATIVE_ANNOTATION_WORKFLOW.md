# KiCad Native Annotation Workflow

## Purpose

Use this workflow when schematic annotation must be proven in the KiCad GUI, not only in the saved `.kicad_sch` file.

Verified success model: `ESP32_CSI_WIFI_NODE` on `2026-05-06`. Evidence is recorded in `KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md` and project reports under `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/`.

## Mandatory Startup

1. Read `AGENTS.md`.
2. Read `33_KICAD_GUI_AUTOMATION/KICAD_GUI_AUTOMATION_RULES.md`.
3. Read `33_KICAD_GUI_AUTOMATION/KICAD_WINDOW_STATE_RULES.md`.
4. Read the active project's current annotation/gate reports.

## Safe Workflow

1. Detect Eeschema:

```powershell
.\33_KICAD_GUI_AUTOMATION\scripts\windows\detect_eeschema_window.ps1 -ExpectedSchematicPath "<active .kicad_sch>" -Json
```

2. Detect unsaved state:

```powershell
.\33_KICAD_GUI_AUTOMATION\scripts\windows\detect_unsaved_kicad_state.ps1 -ExpectedSchematicPath "<active .kicad_sch>" -Json
```

3. If no Eeschema window is open, use `KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md` and `ensure_eeschema_open.py`. Auto-open must launch only the exact target `.kicad_pro`, open/focus the schematic editor, and verify the exact target `.kicad_sch` before annotation. If Eeschema is open with a different project, stop.
4. If the title starts with `*`, stop and ask LJ whether the unsaved GUI state should be kept.
5. Create or confirm backup.
6. Capture before screenshot.
7. Run KiCad native annotation only through verified GUI automation or manually:

```text
Tools -> Annotate Schematic... -> Re-annotate all symbols -> Confirm
```

8. Save only after LJ approval if the GUI state was dirty.
9. Run ERC in the same GUI state, or have LJ run it manually if GUI automation is not verified.
10. Capture after screenshot.
11. Re-run saved-file parse and CLI ERC after saving.

## Closed-State Workflow

If Eeschema is closed and the task explicitly allows opening KiCad:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py --project "<active .kicad_pro>" --schematic "<active .kicad_sch>" --live --allow-annotation --allow-save --allow-gui-erc
```

This command remains dry-run unless `--live` is present. Annotation remains blocked unless `--allow-annotation` is present. Save remains blocked unless `--allow-save` is present.

## Manual Fallback

If automation is unsafe or not selector-verified, tell LJ:

```text
In KiCad: Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC.
Then confirm the GUI no longer shows question-mark references.
```

## Pass Criteria

The annotation gate can pass only when:

- KiCad native `Annotate Schematic` was applied through verified GUI automation or LJ-confirmed manual action.
- The schematic was saved from KiCad GUI.
- GUI ERC shows 0 violations when safely automatable.
- `kicad-cli` ERC passes after GUI save.
- Saved schematic scan shows 0 unresolved `?` references.
- Duplicate-reference scan passes.
- The project report records screenshots, backup path, command log, and reference table.

Passing annotation does not pass visual readability, footprint/package, electrical, or schematic-to-PCB gates.

## Failure Criteria

Fail if:

- GUI path does not match the expected schematic.
- the GUI is unsaved and LJ has not approved save/overwrite.
- native annotation cannot be run safely.
- the GUI still shows question-mark references.
