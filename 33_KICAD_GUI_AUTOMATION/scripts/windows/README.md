# Windows KiCad GUI Scripts

These scripts provide a safety-gated Windows GUI layer for KiCad/Eeschema. They are designed to prevent future agents from treating raw `.kicad_sch` text edits as proof that KiCad's live GUI/native state has been updated.

## Current Capability

Available now:

- detect KiCad/Eeschema processes
- detect the open schematic path from process command lines
- detect unsaved GUI state from a leading `*` in the Eeschema title
- capture screenshots when run with `--capture` and the `windows_gui` Python environment
- provide manual fallback instructions for native annotation, GUI save, and GUI ERC
- run a gated live native annotation/save/GUI ERC workflow when the exact Eeschema target is detected and the task explicitly approves it
- run a gated full workflow that also captures before/after screenshots, creates a backup before live save, runs post-save `kicad-cli` ERC, and scans the saved schematic for unresolved `?` and duplicate references
- dry-run-first helpers to open the exact `.kicad_pro`, open/focus Eeschema, verify the `.kicad_sch`, and then hand off to native annotation

Verified live control:

- `ESP32_CSI_WIFI_NODE` on `2026-05-06`: KiCad native annotation dialog opened, annotation applied, schematic saved from GUI, GUI ERC reported `Violations (0)`, `kicad-cli` ERC passed, saved schematic scan found 0 unresolved `?` references and 0 duplicate references.

Still out of scope:

- PCB update, placement, routing, copper zones, or manufacturing output.
- Visual layout cleanup through this annotation layer.
- Saving a dirty `*` GUI state without explicit user approval and backup.

## Auto-Open Scripts

Dry-run open target project:

```powershell
.\33_KICAD_GUI_AUTOMATION\scripts\windows\open_kicad_project.ps1 -ProjectPath "C:\path\project.kicad_pro" -SchematicPath "C:\path\project.kicad_sch"
```

Dry-run ensure Eeschema is open:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\ensure_eeschema_open.py --project "C:\path\project.kicad_pro" --schematic "C:\path\project.kicad_sch"
```

Dry-run native annotation from closed state:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py --project "C:\path\project.kicad_pro" --schematic "C:\path\project.kicad_sch"
```

Live mode requires explicit `--live`; native annotation also requires `--allow-annotation`; saving requires `--allow-save`.

Exact future live workflow:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py `
  --project "C:\path\project.kicad_pro" `
  --schematic "C:\path\project.kicad_sch" `
  --live `
  --allow-annotation `
  --allow-save `
  --allow-gui-erc
```

## Recommended Python Environment

Use:

`03_TOOLS/python_envs/windows_gui/Scripts/python.exe`

That environment currently has `pywinauto`, `pyautogui`, and `PIL` available.

## Read-Only Examples

```powershell
.\33_KICAD_GUI_AUTOMATION\scripts\windows\detect_kicad_windows.ps1 -Json
.\33_KICAD_GUI_AUTOMATION\scripts\windows\detect_eeschema_window.ps1 -ExpectedSchematicPath "C:\path\project.kicad_sch" -Json
.\33_KICAD_GUI_AUTOMATION\scripts\windows\detect_unsaved_kicad_state.ps1 -ExpectedSchematicPath "C:\path\project.kicad_sch" -Json
```

Dry-run annotation helper:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\annotate_schematic_gui.py --expected-schematic "C:\path\project.kicad_sch"
```

Screenshot dry-run:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\screenshot_kicad_window.py --expected-schematic "C:\path\project.kicad_sch"
```

Screenshot capture:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\screenshot_kicad_window.py --expected-schematic "C:\path\project.kicad_sch" --capture --output ".\33_KICAD_GUI_AUTOMATION\reports\before.png"
```

## Hard Stops

Stop if:

- no Eeschema window is found and the task has not explicitly approved safely opening the target `.kicad_pro`
- more than one Eeschema window is found
- the open path does not match the expected active project schematic
- the title starts with `*` and the user has not decided whether the unsaved GUI state should be kept
- no backup exists before a save-capable workflow
- screenshots cannot be captured before and after
