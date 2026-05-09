# One Prompt Start

This is the fastest startup path for using KiCad Engine as a general AI-assisted KiCad workflow repo.

Historical reports may still show original local paths; current work must use repo-relative paths and live discovery.

## Use It Like This

1. Download the GitHub ZIP or clone the repo.
2. Open the `KICAD_ENGINE` folder in VS Code.
3. Open Codex or Claude from that workspace.
4. Paste the prompt below.

## Starter Prompt

```text
You are working inside the KICAD_ENGINE repo. Before doing any work, read README.md, ONE_PROMPT_START.md if present, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, 03_TOOLS/TOOLS_INDEX.md, EXTERNAL_DEPENDENCIES.md, and 00_CODEX_START/START_HERE.md. Run python health_check.py --no-write if available. Use portable repo docs and live discovery scripts as tool truth. Treat 00_CODEX_START/TOOL_INDEX.md as machine-specific inventory only. Use repo-relative paths only. Do not assume the original author's local paths. Detect the local KiCad install if needed. Do not edit KiCad schematic or PCB files until you identify the active project, task type, live project state, and validation requirements. For PCB/routing work, obey the routing rules: no 90-degree bends, no acute angles, no ugly zig-zag traces, no bad pad-entry geometry, and no fabrication outputs without human review. Summarize the current repo/project status and ask what task to run next.
```

## What This Prompt Assumes

- the repo is the AI workflow engine
- the active project can change over time
- `ESP32_CSI_WIFI_NODE` is only the current example/current active project
- the user may create or bring their own project under `04_KICAD_PROJECTS/active`
- KiCad itself is installed locally when GUI schematic or PCB work is required
- `00_CODEX_START/TOOL_INDEX.md` is machine-specific inventory, not portable setup truth
- historical reports and generated evidence may contain old machine paths and are not current config
