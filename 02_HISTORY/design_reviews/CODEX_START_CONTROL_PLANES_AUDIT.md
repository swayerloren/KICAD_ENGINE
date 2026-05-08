# Codex Start Control Planes Audit

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Result

Audit result: PASS

Missing references: none found.

Files needing correction: none.

## Scope

Audited startup, control-plane, tool-index, repo-map, and handoff documentation for synchronization with the `03_TOOLS` common/windows/linux tool roots and control-plane model.

Files audited:

1. `AGENTS.md`
2. `00_CODEX_START\START_HERE.md`
3. `00_CODEX_START\SESSION_START_CHECKLIST.md`
4. `00_CODEX_START\WORKFLOW_RULES.md`
5. `00_CODEX_START\SAFETY_RULES.md`
6. `00_CODEX_START\TOOL_INDEX.md`
7. `00_CODEX_START\REPO_MAP.md`
8. `00_CODEX_START\CONTROL_PLANES.md`
9. `README_GPT.md`
10. `FOR CHAT GPT.MD`

No KiCad project files were modified. No GUI automation was run. No repos were moved. No tools were installed. MCP permissions were not changed.

## Checklist

| Requirement | Status | Evidence |
| --- | --- | --- |
| `AGENTS.md` tells Codex to read `CONTROL_PLANES.md` | PASS | Startup order includes `00_CODEX_START/CONTROL_PLANES.md`. |
| `START_HERE.md` mentions common/windows/linux roots | PASS | `Platform Tool Roots` section includes `common`, `windows`, and `linux`. |
| `SESSION_START_CHECKLIST.md` includes control-plane selection | PASS | `Control Plane Check` requires stating common, Windows, or Linux control plane. |
| `WORKFLOW_RULES.md` prefers common tools before GUI automation | PASS | `Common-First Workflow` says to use common tools and escalate to GUI discovery only when needed. |
| `SAFETY_RULES.md` blocks random clicks | PASS | GUI safety section says not to randomly click in KiCad. |
| `SAFETY_RULES.md` blocks unsafe GUI saves | PASS | GUI safety section says not to save through GUI automation without explicit approval. |
| `TOOL_INDEX.md` includes legacy/common/windows/linux sections | PASS | Contains `Legacy Tool Paths`, `Common Tool Root`, `Windows GUI Automation Root`, and `Linux/Headless Automation Root`. |
| `REPO_MAP.md` distinguishes legacy/common/windows/linux roots | PASS | `Repository Root Rules` defines legacy, common, Windows, and Linux repo roots. |
| `CONTROL_PLANES.md` exists | PASS | File exists in `00_CODEX_START`. |
| `CONTROL_PLANES.md` is complete | PASS | Includes common, Windows, Linux, tool selection order, safety rules, logs/outputs, and documentation maintenance. |
| `README_GPT.md` and `FOR CHAT GPT.MD` are synchronized | PASS | Both reference `CONTROL_PLANES.md`, legacy path compatibility, common-first tool selection, Windows GUI safety, Linux/headless status, and the GUI false-positive warning. |
| Legacy paths remain valid | PASS | `03_TOOLS\repos`, `03_TOOLS\scripts`, `03_TOOLS\python_envs`, `03_TOOLS\node_envs`, and `03_TOOLS\tool_logs` exist. |
| No repo migration was performed | PASS | Common repos remain in `03_TOOLS\repos`; `03_TOOLS\common\repos` has not received migrated repos. |
| Windows helper repos remain in Windows root | PASS | FlaUI, FlaUInspect, AutoHotkey, and SikuliX1 exist under `03_TOOLS\windows\repos` with `.git` folders. |
| No KiCad project files were modified by this audit | PASS | Audit used read-only scans and did not run project-editing commands. |

## Repo Placement Audit

Common/project-intelligence repos remain in the legacy root:

- `03_TOOLS\repos\kicad-mcp-pro`
- `03_TOOLS\repos\kicad-happy`
- `03_TOOLS\repos\KiCAD-MCP-Server`
- `03_TOOLS\repos\KiBot`
- `03_TOOLS\repos\InteractiveHtmlBom`
- `03_TOOLS\repos\PcbDraw`
- `03_TOOLS\repos\kicanvas`

These have not been migrated into `03_TOOLS\common\repos`.

Windows GUI helper repos remain in the Windows root:

- `03_TOOLS\windows\repos\FlaUI`
- `03_TOOLS\windows\repos\FlaUInspect`
- `03_TOOLS\windows\repos\AutoHotkey`
- `03_TOOLS\windows\repos\SikuliX1`

Linux-specific repo root exists:

- `03_TOOLS\linux\repos`

No Linux repos were installed or cloned by this audit.

## Synchronization Notes

- The startup read order is synchronized around `CONTROL_PLANES.md`.
- The control-plane model is consistently expressed as common-first, GUI-discovery-before-GUI-control, and Linux/headless for repeatable validation.
- The legacy path compatibility rule is present in startup and handoff docs.
- The Windows GUI false-positive warning is present in `README_GPT.md`, `FOR CHAT GPT.MD`, `TOOL_INDEX.md`, and `CONTROL_PLANES.md`.
- No file requires correction from this audit.

## Remaining Known Risk

The Windows KiCad GUI discovery scripts need stricter filtering before any GUI control task. The first read-only run matched VS Code because the title contained `KICAD_ENGINE`; future discovery should prefer confirmed process names such as `kicad.exe`, `eeschema.exe`, and `pcbnew.exe`.

## Exact Next Prompt If Corrections Are Needed

No startup-control-plane corrections are needed.

If continuing the next known safety improvement, use:

```text
You are in:
C:\Users\LJ\KICAD_ENGINE

Goal:
Fix the Windows KiCad GUI discovery scripts so they only treat confirmed KiCad processes as high-confidence candidates.

Rules:
- Do NOT click.
- Do NOT type.
- Do NOT send hotkeys.
- Do NOT open/save/modify KiCad projects.
- Do NOT run GUI control.
- Do NOT install tools.
- Do NOT move repos.

Focus:
- Prefer process names kicad.exe, eeschema.exe, pcbnew.exe.
- Treat title-only matches such as KICAD_ENGINE in VS Code as low-confidence or exclude them.
- Rerun passive discovery only after the script fix.
- Update TOOL_INDEX.md, README_GPT.md, FOR CHAT GPT.MD, and session history if behavior changes.
```
