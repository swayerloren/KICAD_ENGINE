# KiCad GUI Automation Scripts

Scripts under this folder are platform-specific helpers for GUI discovery, screenshots, and native KiCad actions that are not available through `kicad-cli`.

Only `scripts/windows` exists currently.

All scripts must be safe by default:

- discovery-only or dry-run by default
- no random clicks
- no uncontrolled typing
- no PCB/layout/routing/manufacturing actions
- no save unless the active project, exact schematic path, backup, screenshots, and user approval are confirmed
- no claim that GUI annotation passed unless the KiCad GUI itself is verified after native annotation
