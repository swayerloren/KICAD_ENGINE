# KiCad Agent Operating Manual

Date: 2026-05-02

Audience: Codex, Claude, and similar AI coding agents working from VS Code in this repo.

Status: Agent guidance only. This file does not grant permission to edit KiCad project files.

## Core Position

KICAD_ENGINE is a local-first KiCad AI engineering workspace. It does not replace KiCad. It helps agents understand and use the user's installed KiCad app more safely, repeatably, and transparently.

The agent's job is to:

- Use the local repo workflow, memory, history, and tools before guessing.
- Use the installed KiCad app through documented CLI/API paths whenever possible.
- Treat KiCad project files as engineering source, not casual text.
- Keep outputs auditable, timestamped, and clearly marked `NOT_FINAL` until verification is complete.
- Avoid claiming fabrication readiness from one tool result or one visual check.
- Use `09_ACCURACY_ENGINE` before schematic creation, PCB creation, component adds, footprint verification, and release-package work.

## Startup Discipline

Before KiCad project inspection or edits, follow `AGENTS.md` and the startup files in `00_CODEX_START`.

For documentation, tool, and audit tasks:

1. Read the requested context files.
2. Stay out of KiCad project source files unless the user explicitly asks for project work.
3. Record meaningful work in `02_HISTORY`.

For KiCad project work:

1. Confirm active project from `00_CODEX_START/CURRENT_PROJECT.md`.
2. Confirm the target files are inside the active project path.
3. Create or confirm a backup in `99_BACKUPS/pre_codex_edits`.
4. State the files likely to change, verification plan, and rollback plan.
5. Only then inspect or edit project source, and only within the approved scope.

## Accuracy Engine

Before creating or changing schematic, PCB, component, footprint, or manufacturing-output content, read the relevant files under `09_ACCURACY_ENGINE`.

Minimum rule mapping:

- Schematic creation: `09_ACCURACY_ENGINE/schematic_rules/SCHEMATIC_CREATION_STANDARD.md`
- Symbol choice: `09_ACCURACY_ENGINE/schematic_rules/SYMBOL_SELECTION_RULES.md`
- Pinout checks: `09_ACCURACY_ENGINE/schematic_rules/PINOUT_VERIFICATION_RULES.md`
- Power and decoupling: `POWER_NET_RULES.md` and `DECOUPLING_RULES.md`
- Connector risk: `CONNECTOR_PIN_NUMBERING_RULES.md` and `pcb_rules/CONNECTOR_ORIENTATION_RULES.md`
- PCB work: `09_ACCURACY_ENGINE/pcb_rules/PCB_CREATION_STANDARD.md`
- Footprint work: `09_ACCURACY_ENGINE/pcb_rules/FOOTPRINT_SELECTION_RULES.md`
- ERC/DRC/BOM/output interpretation: `09_ACCURACY_ENGINE/verification_rules/`
- Repeatable task workflows: `09_ACCURACY_ENGINE/workflows/`

Accuracy rules:

- Every component needs a source or `SOURCE_MISSING`.
- Every symbol needs pinout verification or `SYMBOL_PINOUT_UNVERIFIED`.
- Every footprint needs exact package drawing verification or `UNVERIFIED_FOOTPRINT`.
- Every connector orientation remains `HUMAN_REVIEW_REQUIRED` unless exact drawing, mating, footprint, and mechanical evidence are verified.
- Every polarity-sensitive part must be flagged.
- Every RF, USB, and CAN part must trigger interface-specific layout review.
- Generated manufacturing-style outputs remain `NOT_FINAL` until final human review.

## Control Plane Choice

Use the safest control plane that can answer the user's request.

### Use kicad-cli When

Use `kicad-cli` for deterministic KiCad-native checks and exports:

- Confirm installed KiCad version with `kicad-cli version`.
- Run schematic ERC.
- Run PCB DRC.
- Export BOMs for review.
- Export Gerbers, drills, PDFs, STEP, or other review artifacts.
- Produce repeatable command logs from VS Code or PowerShell.

Prefer the repo's guarded scripts in `03_TOOLS/scripts` over raw CLI on real projects:

- `run_erc.ps1`
- `run_drc.ps1`
- `export_bom.ps1`
- `export_gerbers.ps1`
- `export_drill.ps1`
- `export_step.ps1`
- `full_verify_project.ps1`

Use raw `kicad-cli` only when the wrapper does not cover the task, and log the exact command, version, exit code, output folder, and source-file impact.

### Parse Files Directly When

Direct parsing is appropriate for read-only understanding:

- Inspect `.kicad_pro` project metadata.
- Inspect `.kicad_sch` symbols, fields, nets, hierarchical sheets, and library references.
- Inspect `.kicad_pcb` footprints, pads, nets, zones, board outline, design settings, and plot settings.
- Inspect `sym-lib-table`, `fp-lib-table`, and `design-block-lib-table`.
- Search `.kicad_sym` and `.kicad_mod` libraries for candidate symbols and footprints.
- Compare schematic and PCB references, values, footprints, and nets.

Rules for direct parsing:

- Prefer structured S-expression-aware parsing when available.
- Use direct text search for discovery, not source rewriting.
- Do not modify KiCad S-expression files by ad hoc string replacement unless the active project, backup, and verification gates are satisfied and the change is narrow enough to review.
- Treat direct file inspection as evidence, not proof of electrical correctness.

### Use pcbnew Python When

Use `pcbnew` Python for board-aware analysis that is awkward or risky with plain text:

- Board geometry, pads, tracks, vias, zones, and nets.
- Footprint placement, orientation, side, courtyard, and bounding-box checks.
- Connector orientation and mechanical clearance review helpers.
- 3D model reference discovery from footprints.
- Custom reports that need KiCad's board object model.

Rules for `pcbnew` Python:

- Treat it as KiCad-version-sensitive.
- Prefer read-only scripts unless the user explicitly asks for an approved board edit.
- Run against copied or active-approved projects only.
- Log generated reports in `02_HISTORY` or `05_OUTPUTS`.
- Do not assume the current Python environment can import `pcbnew`; use the installed KiCad environment or existing repo scripts when available.

### Use GUI Screenshots When

Use GUI screenshots as read-only eyes when CLI/API/file inspection cannot answer a question:

- Confirm how KiCad visually renders a board, schematic, dialog, or warning.
- Capture a screenshot for human review.
- Compare what the GUI shows against parsed or CLI output.
- Investigate a UI-only error state after command-line checks are insufficient.

GUI screenshots are discovery. They are not authority to click, type, save, or export.

### Do Not Use GUI Automation When

Do not automate KiCad GUI control when:

- The task can be done by `kicad-cli`, direct parsing, `pcbnew`, or a wrapper script.
- The active project and backup plan are not confirmed.
- Window identity, size, focus, and screenshot state are not verified.
- The workflow depends on blind coordinates.
- A modal dialog, save prompt, or file picker could appear unexpectedly.
- The action could modify a project, global library table, user preference, or installed KiCad file.
- The user has not explicitly authorized GUI control for the specific task.

For this repo, GUI automation starts with passive discovery only.

## Installed KiCad App Knowledge

The installed KiCad app audit found KiCad 9 under:

- `C:\Program Files\KiCad\9.0\bin`
- `C:\Program Files\KiCad\9.0\etc`
- `C:\Program Files\KiCad\9.0\lib`
- `C:\Program Files\KiCad\9.0\share`

`kicad-cli version` reported `9.0.7` during the audit.

Agents should use this as a known local baseline, but still detect paths dynamically where possible. Future KiCad versions can change CLI options, library locations, output formats, and Python behavior.

Read from installed KiCad folders:

- Executable names and versions.
- Stock symbol libraries.
- Stock footprint libraries.
- Stock 3D models.
- Templates, demos, examples, and documentation.
- Environment variable assumptions and path variable names.

Never modify installed KiCad folders:

- Do not write to `C:\Program Files\KiCad`.
- Do not edit stock symbols, footprints, 3D models, templates, scripts, or examples in place.
- Do not install packages into the KiCad install tree.

## Project Inspection Pattern

For a user project, inspect in this order:

1. Project root contents.
2. `.kicad_pro`.
3. Project-local library tables: `sym-lib-table`, `fp-lib-table`, `design-block-lib-table`.
4. Main `.kicad_sch`.
5. Hierarchical sheets referenced by the schematic.
6. Main `.kicad_pcb`.
7. Project-local libraries under paths using `${KIPRJMOD}`.
8. Reports and generated outputs, clearly separated from source.

Do not treat generated files as source of truth unless the project has no source files and the user explicitly asks for reverse review.

## Symbol Inspection

When inspecting symbols:

1. Identify the library nickname and symbol name from the schematic.
2. Resolve the nickname through project-local `sym-lib-table` first.
3. If not found, resolve through the user's global table in `%APPDATA%\kicad\9.0`.
4. If still not found, inspect stock libraries under the installed KiCad `share` tree.
5. Open the `.kicad_sym` file read-only.
6. Check pin count, pin names, pin numbers, electrical types, hidden power pins, fields, datasheet links, and default footprint property.
7. Compare the symbol to the datasheet before treating it as correct.

Important symbol risks:

- Power pins hidden in the symbol.
- Pin numbering mismatches versus package drawings.
- Alternate units or De Morgan variants.
- Generic symbols with incomplete footprint or datasheet fields.
- User symbols shadowing stock symbols under the same nickname.

## Footprint Inspection

When inspecting footprints:

1. Identify the footprint reference from the schematic field or PCB footprint assignment.
2. Resolve the library nickname through project-local `fp-lib-table` first.
3. If not found, resolve through the user's global table in `%APPDATA%\kicad\9.0`.
4. If still not found, inspect stock `.pretty` folders under the installed KiCad `share` tree.
5. Open the `.kicad_mod` file read-only.
6. Check pad count, pad numbering, pad type, drill sizes, courtyard, fab outline, silkscreen, pin-1 marking, 3D model references, and orientation.
7. Compare against the datasheet land pattern and package drawing.

Important footprint risks:

- Connector pin-1 orientation.
- USB-C receptacle pad mapping and shell treatment.
- CAN transceiver package variants.
- Regulator exposed pad and thermal via assumptions.
- Header pitch, shrouding, keying, and board-edge orientation.
- 3D model presence does not prove footprint correctness.

## Project-Local Libraries

Project-local library tables usually live beside the `.kicad_pro` file:

- `sym-lib-table`
- `fp-lib-table`
- `design-block-lib-table`

They commonly use `${KIPRJMOD}` to point at libraries inside the project folder.

Agent rules:

- Resolve project-local libraries before global and stock libraries.
- Treat project-local libraries as project source files.
- Do not edit them without active project approval, backup, and verification plan.
- If a project embeds fixed footprints to remove library drift, document that in `01_MEMORY` or project history as appropriate.

## Global Libraries

On Windows, user global KiCad tables typically live under:

- `%APPDATA%\kicad\9.0\sym-lib-table`
- `%APPDATA%\kicad\9.0\fp-lib-table`
- `%APPDATA%\kicad\9.0\design-block-lib-table`

Agent rules:

- Read global tables only when needed to resolve references.
- Never edit global tables as a side effect of project work.
- Do not make a project depend on a user's private global library without documenting the dependency.
- Prefer project-local library entries for reproducible project handoff.

## Running ERC

ERC is the first schematic verification gate.

Preferred wrapper:

```powershell
& ".\03_TOOLS\scripts\run_erc.ps1" -ProjectPath "C:\path\to\project"
```

The current wrapper uses KiCad CLI arguments equivalent to:

```text
sch erc --output <report> --format report --exit-code-violations <main_schematic.kicad_sch>
```

Before running ERC on a project:

- Confirm active project and path.
- Confirm the target schematic is inside that path.
- Confirm backup state if the task includes or follows edits.
- Choose a report output folder under `02_HISTORY` or approved `05_OUTPUTS`.
- Log the command and result.

Do not claim schematic correctness from ERC alone. ERC does not prove symbol pinout, datasheet match, power budget, connector orientation, or component suitability.

## Running DRC

DRC is the first PCB layout verification gate.

Preferred wrapper:

```powershell
& ".\03_TOOLS\scripts\run_drc.ps1" -ProjectPath "C:\path\to\project"
```

The current wrapper uses KiCad CLI arguments equivalent to:

```text
pcb drc --output <report> --format report --exit-code-violations <board.kicad_pcb>
```

Before running DRC on a project:

- Confirm active project and path.
- Confirm the target board is inside that path.
- Confirm backup state if the task includes or follows edits.
- Choose a report output folder under `02_HISTORY` or approved `05_OUTPUTS`.
- Log the command and result.

Do not claim PCB correctness from DRC alone. DRC does not prove datasheet footprint accuracy, connector mating direction, assembly polarity, controlled impedance, fab capability, enclosure fit, or manufacturability.

## Review-Only Outputs

Review-only outputs are useful for inspection and communication. They must not be treated as release packages.

Examples:

- BOM CSV for component review.
- Schematic PDF.
- PCB PDF or SVG plots.
- STEP model for mechanical review.
- Screenshots.
- Interactive HTML BOM if available.
- ERC and DRC reports.

Rules:

- Write review outputs to `05_OUTPUTS`, `02_HISTORY`, or an approved project output folder.
- Do not overwrite older outputs.
- Include command logs or summaries.
- Mark unclear or unverified exports as review-only.

## NOT_FINAL Fabrication Outputs

Fabrication-style outputs can be generated for review, but they must be marked `NOT_FINAL` until the full release gate passes.

Examples:

- Gerbers.
- Excellon drill files.
- Pick-and-place CSV.
- Fabrication BOM.
- Assembly drawings.
- STEP model.
- Package manifest.

Preferred wrappers:

```powershell
& ".\03_TOOLS\scripts\export_gerbers.ps1" -ProjectPath "C:\path\to\project"
& ".\03_TOOLS\scripts\export_drill.ps1" -ProjectPath "C:\path\to\project"
& ".\03_TOOLS\scripts\export_bom.ps1" -ProjectPath "C:\path\to\project"
& ".\03_TOOLS\scripts\export_step.ps1" -ProjectPath "C:\path\to\project"
```

Before generating fabrication-style outputs:

- Confirm active project and path.
- Confirm source files are the intended files.
- Run or review ERC and DRC status.
- Ensure output path includes or contains a `NOT_FINAL` marker.
- Include a manifest that states what was generated and what remains unverified.

Never tell the user a package is fab-ready unless ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, mechanical, and visual review gates have all been completed and recorded.

## Avoiding False Confidence

Avoid these weak claims:

- "ERC passed, so the schematic is correct."
- "DRC passed, so the PCB is manufacturable."
- "The symbol exists, so the pinout is correct."
- "The footprint name matches, so the land pattern is correct."
- "The 3D model aligns, so the connector orientation is correct."
- "Gerbers exported, so the board is ready."
- "The AI reviewed it, so fabrication is safe."

Use stronger engineering language:

- "ERC reported no violations in this KiCad version."
- "DRC reported no violations with the current board rules."
- "The footprint resolves to this library path and should still be checked against the datasheet."
- "The package is `NOT_FINAL` pending connector, polarity, BOM, and visual review."

## Agent Closeout Checklist

For every meaningful KiCad task, record:

- What files or folders were inspected.
- What tools or scripts were used.
- KiCad version if KiCad CLI or app behavior matters.
- Whether source files were modified.
- Where reports or outputs were written.
- Remaining verification gaps.
- Whether outputs are review-only, `NOT_FINAL`, `HUMAN_REVIEW_REQUIRED`, or approved by the user.
