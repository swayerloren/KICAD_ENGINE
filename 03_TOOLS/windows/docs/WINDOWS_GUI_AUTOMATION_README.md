# Windows GUI Automation README

This folder is for Windows desktop GUI automation experiments around KiCad and related review tools.

## Installed Environment

Python environment:

`03_TOOLS/python_envs/windows_gui`

Installed packages:

- `pywinauto`
- `pyautogui`
- `pygetwindow`
- `pyperclip`
- `pillow`
- `opencv-python`
- `psutil`

## Tool Roles

- `pywinauto` is the primary Windows UI automation library. Use it first for window discovery, UI Automation control trees, window metadata, and safer structured interactions.
- `PyAutoGUI` is a fallback visual, keyboard, mouse, and screenshot automation layer. It is less structured and must be treated as higher risk.
- `OpenCV` is for image matching and screenshot comparison.
- `Pillow` supports image loading, saving, cropping, and screenshot processing.
- `pygetwindow` helps locate windows and bounding boxes.
- `pyperclip` may help clipboard workflows only when clipboard use is explicitly approved.
- `psutil` helps map process names and process IDs.

Optional later tools:

- AutoHotkey for Windows hotkey/window automation.
- FlaUI and FlaUInspect for .NET UI Automation inspection.
- SikuliX for image-driven GUI automation.
- Microsoft Inspect.exe and Accessibility Insights for manual UI Automation discovery notes.

## Safety Rules

- Codex must not randomly click KiCad.
- Codex must not type into KiCad without explicit approval.
- Codex must not move, resize, or close KiCad windows unless explicitly approved.
- Codex must discover windows and take screenshots before any control attempt.
- KiCad GUI discovery must classify windows by process name first.
- Only `kicad.exe`, `eeschema.exe`, and `pcbnew.exe` are high-confidence KiCad processes.
- Title-only matches such as VS Code with `KICAD_ENGINE` in the title are low-confidence and must not be inspected, screenshotted, or controlled.
- Coordinate-based clicks are not allowed unless screenshot, window title, window bounds, DPI/scaling assumptions, and target location are verified first.
- Prefer `kicad-cli`, KiBot, `pcbnew`, MCP analysis tools, or static file inspection before GUI automation.
- Do not use GUI automation on real project files until active project, backup plan, verification plan, and rollback plan are confirmed.

## Passive Scripts

- `03_TOOLS\windows\scripts\window_discovery\discover_windows.py`
  - Lists visible windows.
  - Writes markdown logs to `03_TOOLS\windows\logs`.
  - Does not click, type, or move windows.

- `03_TOOLS\windows\scripts\window_discovery\discover_kicad_windows.py`
  - Classifies visible windows as high-confidence KiCad, low-confidence title-only, or excluded non-KiCad.
  - High confidence requires process name `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`.
  - Supports `--allow-title-only-review`, `--target-pid <PID>`, and `--output-dir <PATH>`.
  - Does not click, type, move windows, inspect low-confidence candidates, or control KiCad.

- `03_TOOLS\windows\scripts\pywinauto\inspect_kicad_uia.py`
  - Performs read-only UIA inspection only for high-confidence KiCad process windows.

- `03_TOOLS\windows\scripts\pywinauto\inspect_kicad_win32.py`
  - Performs read-only Win32 inspection only for high-confidence KiCad process windows.

- `03_TOOLS\windows\scripts\screenshots\capture_kicad_window.py`
  - Captures screenshots only for high-confidence KiCad process windows.

- `03_TOOLS\windows\scripts\screenshots\take_screenshot.py`
  - Captures a screenshot only.
  - Saves PNG files under `03_TOOLS\windows\logs\screenshots`.
  - Does not click, type, or move windows.
