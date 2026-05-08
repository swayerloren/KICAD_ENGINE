# Linux KiCad Headless Plan

This plan describes a future Linux/headless KiCad automation lane. It is documentation only. No Linux installation or WSL configuration is performed by this file.

## Goals

- Validate KiCad CLI workflows in a Linux environment.
- Support repeatable ERC/DRC/export checks in CI or headless sessions.
- Use virtual display tooling only when a GUI component requires it.
- Keep generated artifacts in approved `05_OUTPUTS` or project `reports`/`fabrication` folders and mark them `NOT_FINAL` unless the fabrication gate passes.

## Phases

### Phase 1: Environment Discovery

- Confirm whether WSL, Linux VM, Docker, or a native Linux machine is being used.
- Confirm Linux distribution and version.
- Confirm KiCad and `kicad-cli` availability.
- Confirm Python, pip, Git, Node, and npm availability if needed.
- Confirm display stack: headless only, X11, Wayland, or Xvfb.
- Run `03_TOOLS\linux\scripts\check_linux_kicad_env.sh`.

### Phase 2: Headless KiCad CLI

- Run `kicad-cli version`.
- Test ERC/DRC only on disposable sample projects first.
- Do not generate fabrication outputs for real projects until active project and backup gates are complete.
- Compare Linux results with Windows results before relying on Linux as a release path.

### Phase 3: Virtual Display

- Check `Xvfb` and `xvfb-run` availability.
- Use Xvfb only for tools requiring a display.
- Keep GUI workflows read-only until validated on disposable projects.
- Run `03_TOOLS\linux\scripts\xvfb\run_kicad_headless_check.sh` only inside Linux.

### Phase 4: GUI Discovery

- Use `wmctrl` and `xdotool` only to list windows first.
- Use `dogtail` only for read-only accessibility inspection first.
- Do not send keys, mouse clicks, or window-manager commands until a future gated task explicitly allows it.

### Phase 5: CI/Container Candidate

- Create a disposable project fixture.
- Run Linux KiCad CLI checks in a container or CI environment.
- Save logs and reports outside source project files.
- Treat all outputs as review artifacts until the full verification gate passes.

## Known Risks

- KiCad GUI behavior may differ between Windows and Linux.
- X11 automation does not represent Wayland behavior.
- Xvfb rendering may differ from a real desktop.
- KiCad plugin paths and Python package paths may differ by distribution.
- KiBot and visual tools can have display or font dependencies in Linux.

## Approval Gate

Before using Linux automation on a real project:

1. Confirm active project.
2. Confirm backup path.
3. Confirm exact commands.
4. Confirm output folders.
5. Confirm rollback plan.
6. Confirm no generated output will be marked final without ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, mechanical, and visual review.
