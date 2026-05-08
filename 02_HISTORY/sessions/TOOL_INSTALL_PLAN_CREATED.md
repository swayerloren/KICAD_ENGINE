# Tool Install Plan Created

Date: 2026-04-30

## Summary
Inspected cloned KiCad/Codex support repositories and created a safe installation plan without installing dependencies, running setup scripts, configuring MCP, or modifying third-party repository files.

## Files Created Or Updated
- `03_TOOLS\tool_logs\INSTALL_PLAN.md`
- `00_CODEX_START\TOOL_INDEX.md`
- `02_HISTORY\sessions\TOOL_INSTALL_PLAN_CREATED.md`

## Repositories Inspected
- `03_TOOLS\repos\kicad-mcp-pro`
- `03_TOOLS\repos\kicad-happy`
- `03_TOOLS\repos\KiCAD-MCP-Server`
- `03_TOOLS\repos\KiBot`
- `03_TOOLS\repos\InteractiveHtmlBom`
- `03_TOOLS\repos\PcbDraw`
- `03_TOOLS\repos\kicanvas`

## Materials Inspected
- README files.
- Documentation and install guidance.
- `pyproject.toml`.
- `package.json`.
- `requirements.txt` and development requirements where present.
- `setup.py` and `setup.cfg` where present.
- Windows setup/troubleshooting notes where present.
- MCP configuration examples where present.

## Local Prerequisite Checks
- Git available.
- `py` available and reports Python 3.12.10.
- `python` missing from PATH.
- Node.js available at v22.15.0.
- npm available at 10.9.2.
- KiCad and `kicad-cli` missing from PATH.
- Docker missing from PATH.
- `uv` and `uvx` missing from PATH.

## Constraints Followed
- No dependencies installed.
- No setup scripts run.
- No MCP configuration performed.
- No third-party repository files modified.
- No KiCad project files edited.

## Verification
- Confirmed `03_TOOLS\tool_logs\INSTALL_PLAN.md` exists and covers all seven repositories.
- Confirmed `00_CODEX_START\TOOL_INDEX.md` links to the install plan and preserves `CLONED_NOT_INSTALLED` status.
- Confirmed cloned repository worktrees still report clean branch status.

## Recommended Install Order
1. Baseline prerequisites: KiCad/`kicad-cli`, KiCad Python/`pcbnew`, PATH decisions, optional Docker and `uv`.
2. `kicad-happy`.
3. `kicanvas`.
4. `InteractiveHtmlBom`.
5. `PcbDraw`.
6. `KiBot`.
7. `kicad-mcp-pro`.
8. `KiCAD-MCP-Server`.

## Blockers
- KiCad and `kicad-cli` are missing from PATH.
- `uv`/`uvx` are missing for `kicad-mcp-pro` quick runtime.
- Docker is missing for Docker-based KiBot/Freerouting paths.
- `python` is missing from PATH, though `py -3.12` is available.
- MCP tools must remain analysis-only/read-only until tested on disposable projects.
