# KiCad Safe Automation Rules

Date: 2026-05-02

Audience: AI agents and automation scripts working from VS Code in KICAD_ENGINE.

Status: Safety rules. These rules restrict automation; they do not grant edit authority.

## Prime Rule

Do not modify KiCad project source, installed KiCad files, user global KiCad settings, or manufacturing outputs unless the user explicitly requested that scope and the repo safety gates are satisfied.

KiCad design files include:

- `.kicad_pro`
- `.kicad_sch`
- `.kicad_pcb`
- `.kicad_sym`
- `.kicad_mod`
- `sym-lib-table`
- `fp-lib-table`
- `design-block-lib-table`
- Gerber, drill, pick-and-place, and manufacturing package files

## Automation Order

Choose control planes in this order:

1. Read-only file inspection.
2. Existing guarded scripts in `03_TOOLS/scripts`.
3. Direct `kicad-cli` commands with explicit paths and logs.
4. Read-only `pcbnew` Python analysis.
5. Passive GUI screenshots and UI discovery.
6. GUI control only after explicit task approval and full safeguards.

Stop at the earliest control plane that can answer the task.

## Required Gates Before Project Commands

Before any project-targeted command, confirm:

- Active project name.
- Active project path.
- Target file path is inside the active project folder.
- Whether the command is read-only or writes outputs.
- Output folder.
- Backup state if source edits were made or are about to be made.
- Verification purpose.
- Log destination.

## Read-Only Allowed Actions

Allowed for documentation, audit, and review tasks:

- Read repo documents.
- Read installed KiCad metadata and libraries.
- Read project files when the user asked for inspection or review.
- Read global user library tables to resolve references.
- Run `kicad-cli version` when version confirmation is needed.
- Generate reports into `02_HISTORY` or `05_OUTPUTS` when requested and safe.
- Capture screenshots of already-open KiCad windows when the user asked for visual discovery.

Read-only still requires care. Some applications may update user preference timestamps when launched. Avoid unnecessary app launches.

## Project Validation Script Rules

Use `03_TOOLS/scripts/project_validation/validate_kicad_project.ps1` or `validate_kicad_project.py` for read-only project preflight and review reports.

Allowed validation checks:

- Project, schematic, and PCB file presence.
- Project-local library table presence.
- Missing symbol libraries.
- Missing footprint libraries and assigned footprint files.
- Missing 3D model references.
- ERC, DRC, and BOM export availability.
- Datasheet and component database coverage.
- Connector, polarity, RF, USB, CAN, LIN, and automotive human-review flags.

Rules:

- Validation scripts must not edit KiCad source files.
- Validation scripts must not fix library tables, symbols, footprints, or PCB data automatically.
- Validation reports should be written under `05_OUTPUTS/project_validation` by default.
- Do not write validation output inside a project folder unless the user explicitly approved that output location.
- Treat `PASS` as a scoped script result, not as design approval.
- Treat `WARN` and `FAIL` as `HUMAN_REVIEW_REQUIRED` until resolved.

Primary command:

```powershell
& ".\03_TOOLS\scripts\project_validation\validate_kicad_project.ps1" -ProjectPath "C:\path\to\project"
```

## Write Actions That Need Explicit Approval

The following need explicit user scope and normal repo gates:

- Editing schematic, PCB, project, symbol, footprint, or library-table files.
- Creating or changing project-local symbols or footprints.
- Updating footprint assignments.
- Changing board rules, stackup, net classes, or constraints.
- Generating fabrication-style outputs from a project.
- Writing into a project folder.
- Running scripts that create files inside a project.
- Editing global KiCad library tables or preferences.
- Launching GUI control that may save, export, or modify state.

## Installed KiCad Folder Rules

The installed KiCad app is read-only source material for agents.

Never write to:

- `C:\Program Files\KiCad\<version>\bin`
- `C:\Program Files\KiCad\<version>\etc`
- `C:\Program Files\KiCad\<version>\lib`
- `C:\Program Files\KiCad\<version>\share`
- Any future KiCad install folder under `Program Files`

Allowed:

- Enumerate files.
- Read help/docs/examples.
- Inspect stock symbol libraries.
- Inspect stock footprint libraries.
- Inspect stock 3D model references.
- Check executable existence and version.

Not allowed:

- Install packages there.
- Patch stock libraries.
- Copy generated project files there.
- Change KiCad examples or templates in place.
- Treat Program Files as a writable cache.

## User Global KiCad Config Rules

User global KiCad data on Windows typically lives under:

- `%APPDATA%\kicad\9.0`

Agents may read global library tables to resolve a project reference. Agents must not edit global user tables or preferences unless the user explicitly requests global KiCad configuration changes and a backup plan is stated.

Do not make local project automation depend silently on private global libraries. If a dependency exists, document it.

## Project-Local Library Rules

Project-local libraries are project source.

Rules:

- Resolve `${KIPRJMOD}` paths relative to the project root.
- Inspect `sym-lib-table` and `fp-lib-table` before using global or stock libraries.
- Do not edit project-local libraries without active project approval.
- Do not "fix" missing libraries by changing global KiCad settings.
- If project-local copies are created for reproducibility, document why.

## kicad-cli Rules

Use explicit, quoted paths:

```powershell
kicad-cli version
```

If KiCad is installed but not on `PATH`, use `03_TOOLS/scripts/kicad_discovery/find_kicad.py` or `validate_kicad_install.py` to locate the actual CLI path first.

For real project workflows, prefer repo wrappers:

```powershell
& ".\03_TOOLS\scripts\run_erc.ps1" -ProjectPath "C:\path\to\project"
& ".\03_TOOLS\scripts\run_drc.ps1" -ProjectPath "C:\path\to\project"
```

Rules:

- Detect KiCad path where possible.
- Record KiCad version when command behavior matters.
- Do not assume KiCad 9 CLI options apply to KiCad 10 or later.
- Log command, exit code, and output location.
- Keep generated outputs outside source folders unless explicitly approved.

## pcbnew Python Rules

Use `pcbnew` Python for board-aware read-only analysis when direct text parsing is insufficient.

Rules:

- Do not use `pcbnew` scripts to save boards unless explicitly approved.
- Do not assume `pcbnew` is importable in arbitrary Python environments.
- Treat geometry and net reports as evidence to combine with DRC, datasheets, and visual review.
- Keep generated reports in `02_HISTORY` or `05_OUTPUTS`.

## GUI Screenshot Rules

Screenshots are allowed when:

- The user requested visual inspection or GUI discovery.
- A real KiCad process/window is identified.
- The screenshot target is verified as KiCad, not VS Code, a browser, or an editor.
- No click, typing, hotkey, drag, file picker, or save operation is involved.

Record screenshot outputs in `02_HISTORY`, `05_OUTPUTS`, or an approved review folder.

## GUI Control Rules

GUI control is disabled by default.

Before any GUI control:

- The user must explicitly authorize GUI control for the specific task.
- The active project and backup plan must be confirmed if a project is open.
- Window identity and size must be verified.
- A current screenshot must be captured.
- The intended UI action sequence must be stated.
- A rollback or abort plan must be available.
- The command log must record what happened.

Do not use:

- Blind coordinate clicks.
- Random typing.
- Unverified hotkeys.
- GUI control to bypass CLI errors.
- GUI control on production project files without approval and backup.

## Export Rules

Review exports:

- BOM, PDF, SVG, STEP, screenshots, and reports can support review.
- They remain review-only until cross-checked.

Fabrication-style exports:

- Gerbers, drills, pick-and-place, and manufacturing packages must be marked `NOT_FINAL` unless all release gates are recorded.
- Use timestamped folders.
- Include a manifest or summary.
- Do not overwrite prior packages.

## Verification Gate

A fabrication package is not final until all relevant gates pass:

- ERC.
- DRC.
- BOM review.
- Footprint-to-datasheet review.
- Symbol-to-datasheet review.
- Netlist and schematic-to-PCB comparison.
- Connector pinout and orientation review.
- Polarity and assembly orientation review.
- Mechanical and 3D clearance review where applicable.
- Fab output review with the target board house requirements.
- Human review for high-risk assumptions.

If any gate is incomplete, classify the package as `NOT_FINAL` or `HUMAN_REVIEW_REQUIRED`.

## False Confidence Rules

Never collapse one passing check into full approval.

Use precise status language:

- `READ_ONLY_INSPECTION`
- `REPORT_GENERATED`
- `PASS_BY_KICAD_CLI`
- `FAILED_OR_VIOLATIONS_REPORTED`
- `EXPORTED_REQUIRES_REVIEW`
- `EXPORTED_NOT_FINAL`
- `HUMAN_REVIEW_REQUIRED`
- `FAB_READY_BY_USER_APPROVAL`

Do not use `FAB_READY` unless the user explicitly accepts the completed verification evidence.

## Stop Conditions

Stop and ask the user before proceeding when:

- The requested action would edit project source but the active project is unclear.
- The target file is outside the active project.
- A global KiCad config edit would be needed.
- A missing datasheet prevents pinout or footprint verification.
- A connector orientation or pinout is ambiguous.
- A script would overwrite an existing output.
- KiCad CLI syntax differs from the documented version.
- The task requires installing tools.
