# Common KiCad Tools

`03_TOOLS\common` is for OS-neutral KiCad tooling and project intelligence.

Use this area for tools that analyze, validate, render, export, or inspect KiCad project files without depending on Windows-only or Linux-only GUI control.

Examples:

- KiBot
- `kicad-cli` wrappers
- InteractiveHtmlBom
- KiCanvas
- PcbDraw
- `pcbnew` scripts
- MCP servers
- Validators and static analyzers

Current legacy paths remain valid. Existing repos are still in `03_TOOLS\repos`, scripts are still in `03_TOOLS\scripts`, Python environments are still in `03_TOOLS\python_envs`, and Node environments are still in `03_TOOLS\node_envs`.

Do not move repos into this folder until a migration is explicitly approved.
