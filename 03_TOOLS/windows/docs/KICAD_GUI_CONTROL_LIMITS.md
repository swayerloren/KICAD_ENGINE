# KiCad GUI Control Limits

Windows GUI automation is experimental support for cases where safer KiCad automation paths are insufficient.

## Limits

- KiCad's drawing canvas may not expose all objects through Windows UI Automation.
- Schematic and PCB canvas content may need file-level analysis, `kicad-cli`, KiBot, `pcbnew`, screenshots, or visual inspection rather than UI Automation control trees.
- GUI automation is less safe than `kicad-cli`, KiBot, `pcbnew`, static KiCad file parsing, or read-only MCP analysis.
- GUI state can depend on focus, window size, DPI scaling, theme, monitor layout, modal dialogs, and user input timing.
- Coordinate clicks are fragile and can affect the wrong project, wrong file, or wrong dialog if context is stale.

## Required Control Gate

Use GUI automation only when CLI/API/MCP approaches are insufficient for the task.

Before any control action:

1. Confirm the active project and exact KiCad window.
2. Confirm the target process name is `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`.
3. Confirm backups and rollback plan.
4. Run window discovery.
5. Take screenshots only for high-confidence KiCad process windows.
6. Verify window title, process ID, bounds, monitor/DPI assumptions, and target location.
7. State the intended action and expected result.
8. Avoid coordinate clicks unless there is no structured alternative.

## Candidate Filtering Rule

- High-confidence KiCad windows require process name `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`.
- Window-title-only matches are `LOW_CONFIDENCE_TITLE_ONLY`.
- Low-confidence candidates are not eligible for UIA inspection, Win32 inspection, screenshots, or control.
- VS Code, browser, editor, or file-manager windows must not become high-confidence targets just because the title contains `KICAD_ENGINE`, `KiCad Engine`, `README_GPT`, `.kicad`, or `kicad`.
- `eligible_for_control` defaults to `false`.

## Prohibited By Default

- Random clicking.
- Blind typing.
- Closing windows.
- Saving files.
- Changing project settings.
- Exporting manufacturing files.
- Running GUI actions against real KiCad projects without active-project approval.

## Preferred Order

1. Static file inspection.
2. `kicad-cli`.
3. KiBot.
4. `pcbnew` scripts.
5. MCP analysis/safe tools.
6. Structured UI Automation through `pywinauto`.
7. Screenshot/image matching.
8. Coordinate mouse/keyboard control only after explicit approval and verification.
