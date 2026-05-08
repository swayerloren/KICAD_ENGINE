# Platform Control Layers Audit

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Result

Overall audit result: PASS

Readiness score: 94 / 100

The common, Windows, and Linux control-layer structure is present and documented. Legacy tool paths still exist. Existing PowerShell verification scripts parse cleanly. Windows GUI automation assets are present but remain passive/discovery-only. Linux/headless assets are planning and starter-script assets only.

## Scope

This audit checked the KiCad Engine control-layer setup after adding:

- common/project-intelligence tooling paths
- Windows GUI hands/eyes tooling paths
- Linux/headless/CI tooling paths
- Windows GUI Python environment and passive discovery scripts
- Windows GUI helper repos
- Linux/headless planning docs and starter scripts
- Codex startup and handoff documentation for control-plane selection

No KiCad project files were edited. No GUI automation was run against KiCad. No tools were installed. No repos were moved.

## Audit Checklist

| Check | Status | Notes |
| --- | --- | --- |
| `03_TOOLS\common` structure exists | PASS | `common`, `common\repos`, `common\scripts`, and `common\docs` exist. |
| `03_TOOLS\windows` structure exists | PASS | Windows root, repos, scripts, docs, logs, and script subfolders exist. |
| `03_TOOLS\linux` structure exists | PASS | Linux root, repos, scripts, docs, logs, and tool-specific script subfolders exist. |
| Legacy paths still exist | PASS | `03_TOOLS\repos`, `03_TOOLS\scripts`, `03_TOOLS\python_envs`, `03_TOOLS\node_envs`, and `03_TOOLS\tool_logs` still exist. |
| Existing verification scripts are not broken by new structure | PASS | All 12 PowerShell scripts in `03_TOOLS\scripts` parsed with zero syntax errors. |
| Windows GUI venv exists | PASS | `03_TOOLS\python_envs\windows_gui\Scripts\python.exe` exists and reports Python 3.12.10. |
| Windows GUI passive scripts exist | PASS | Discovery, UIA inspection, Win32 inspection, and screenshot scripts exist. |
| Windows GUI passive scripts compile | PASS | Python `py_compile` passed for all checked Windows GUI Python scripts. |
| Windows GUI repos exist | PASS | FlaUI, FlaUInspect, AutoHotkey, and SikuliX1 exist with `.git` folders. |
| Windows GUI repos are not locally modified | PASS | `git status --short --branch` showed branch-only output for all checked Windows GUI repos. |
| Linux docs and starter scripts exist | PASS | Expected Linux docs and `.sh` starter scripts exist. |
| Linux starter scripts are safe drafts | PASS | Safety scan found no `sudo`, install commands, delete commands, KiCad exports, ERC, or DRC actions in starter scripts. |
| `README_GPT.md` explains platform split | PASS | It references platform roots, control planes, Windows GUI, and Linux/headless workflow. |
| `FOR CHAT GPT.MD` explains platform split | PASS | It references platform roots, control-plane model, Windows GUI automation, and Linux/headless automation. |
| `START_HERE.md` explains control planes | PASS | It includes common, Windows GUI, and Linux/headless control-plane rules. |
| `AGENTS.md` explains control planes | PASS | It includes common, Windows GUI, and Linux/headless control-plane rules. |
| `TOOL_INDEX.md` is current | PASS | It records platform-aware roots, legacy path validity, Windows GUI assets, and Linux/headless assets. |
| `REPO_MAP.md` is current | PASS | It records legacy repos and Windows GUI helper repos under `03_TOOLS\windows\repos`. |
| Original KiCad project files were not modified by this audit | PASS | This audit used read-only file scans and did not run KiCad, ERC, DRC, exports, or GUI automation. |
| Third-party repos were not modified by this audit | PASS | Only read-only `git status` and metadata checks were run. |

## Checked Repos

Legacy KiCad/Codex repos:

- `03_TOOLS\repos\kicad-mcp-pro`: clean branch-only status
- `03_TOOLS\repos\kicad-happy`: clean branch-only status
- `03_TOOLS\repos\KiCAD-MCP-Server`: clean branch-only status
- `03_TOOLS\repos\KiBot`: clean branch-only status
- `03_TOOLS\repos\InteractiveHtmlBom`: clean branch-only status
- `03_TOOLS\repos\PcbDraw`: clean branch-only status
- `03_TOOLS\repos\kicanvas`: clean branch-only status

Windows GUI helper repos:

- `03_TOOLS\windows\repos\FlaUI`: clean branch-only status
- `03_TOOLS\windows\repos\FlaUInspect`: clean branch-only status
- `03_TOOLS\windows\repos\AutoHotkey`: clean branch-only status
- `03_TOOLS\windows\repos\SikuliX1`: clean branch-only status

## Remaining Risks

- Windows GUI automation has not been exercised against KiCad yet. Use discovery-only scripts first.
- GUI automation remains less safe than CLI/API/MCP/KiBot workflows. It must not click, type, send hotkeys, open projects, or save files without explicit approval.
- Coordinate-based GUI automation is not approved. Any future coordinate action needs a current screenshot and verified window dimensions.
- Linux/headless automation is planning-only. WSL, Linux KiCad, Xvfb, xdotool, wmctrl, dogtail, Docker, and other Linux-side dependencies are not installed or verified here.
- Windows GUI helper repos are cloned references only. FlaUI, FlaUInspect, AutoHotkey, and SikuliX1 are not built or approved for KiCad control.
- KiBot and visual review tools are installed or cloned, but production trust still requires controlled validation on copied/non-production projects.
- No real active project is selected. KiCad design-file edits remain blocked until active project, backup plan, verification plan, and rollback plan are confirmed.

## Readiness Assessment

The platform control-layer structure is ready for controlled use as documentation and scaffolding:

- Common/project-intelligence tools should remain the default first choice.
- Windows GUI tooling is ready only for passive discovery and screenshots.
- Linux/headless tooling is ready only as planning docs and safe starter scripts.
- Legacy paths remain valid and should not be moved until a dedicated migration task updates scripts, docs, and indexes together.

## Exact Next Prompt For KiCad GUI Discovery

Use this only after KiCad is opened manually and LJ confirms read-only discovery is intended:

```text
You are in:
C:\Users\LJ\KICAD_ENGINE

Goal:
Run read-only KiCad GUI discovery only.

Rules:
- Do NOT click inside KiCad.
- Do NOT type into KiCad.
- Do NOT send hotkeys.
- Do NOT open or save KiCad projects.
- Do NOT modify KiCad files.
- Save all reports/screenshots under 03_TOOLS\windows\logs.

Use venv:
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui

Run only these discovery commands:
1. discover_kicad_windows.py
2. inspect_kicad_uia.py
3. inspect_kicad_win32.py
4. capture_kicad_window.py

After running, summarize visible KiCad windows, UIA/Win32 inspection quality, screenshot path, blockers, and whether GUI control is still unsafe.
```
