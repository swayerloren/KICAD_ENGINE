# Deep KiCad App Folder Breakdown

Date: 2026-05-03

Audience: Codex, Claude, and similar AI coding agents using a user's installed KiCad app from VS Code.

Status: Read-only installed-app intelligence. This file does not grant permission to edit KiCad projects or installed KiCad folders.

## Audited Windows Install

Observed KiCad root:

```text
C:\Program Files\KiCad\9.0
```

Observed KiCad CLI:

```text
C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
```

Observed `kicad-cli version`:

```text
9.0.7
```

Generated machine-readable inventory:

- `03_TOOLS/kicad_app_intelligence/generated/kicad_folder_inventory.windows.json`
- `03_TOOLS/kicad_app_intelligence/generated/kicad_executables.windows.json`
- `03_TOOLS/kicad_app_intelligence/generated/kicad_resource_summary.windows.json`
- `03_TOOLS/kicad_app_intelligence/generated/kicad_folder_inventory.windows.md`

## Summary Counts

| Resource | Observed count |
| --- | ---: |
| Stock symbol library files | 223 |
| Stock footprint library folders | 155 |
| Stock footprint files | 15,415 |
| Stock 3D model library folders | 105 |
| Stock 3D model files | 14,043 |
| STEP 3D model files | 7,200 |
| WRL 3D model files | 6,843 |
| Stock template folders | 19 |
| Stock template files | 39 |
| Demo/example folders | 19 |
| Installed scripting Python files | 20 |
| JSON schema files | 2 |
| Runtime DLLs in `bin` | 199 |

## `bin`

Windows path:

```text
C:\Program Files\KiCad\9.0\bin
```

Role:

- GUI entry points.
- `kicad-cli`.
- Runtime DLLs.
- Bundled Python.
- KiCad Python API loader files.
- IDF/DXF/VRML helper tools.
- Crashpad helper.
- Windows command-prompt helper batch file.

Observed runnable files include:

| File | AI role |
| --- | --- |
| `kicad.exe` | Main KiCad project manager GUI. Use only when GUI inspection/control is explicitly needed. |
| `kicad-cli.exe` | Preferred command-line entry for version checks, ERC, DRC, exports, renders, symbol/footprint utility commands, and jobsets. |
| `eeschema.exe` | Schematic editor GUI. Do not automate unless explicitly approved. |
| `pcbnew.exe` | PCB editor GUI. Do not automate unless explicitly approved. |
| `gerbview.exe` | Gerber viewer GUI. Useful for manual/visual output review. |
| `bitmap2component.exe` | Bitmap conversion utility. Not part of normal review flow. |
| `pcb_calculator.exe` | Calculator GUI. Reference only. |
| `pl_editor.exe` | Page layout editor GUI. Reference only. |
| `python.exe` / `pythonw.exe` | Bundled KiCad Python runtime. Use only for KiCad-specific Python workflows when necessary. |
| `dxf2idf.exe`, `idf2vrml.exe`, `idfcyl.exe`, `idfrect.exe` | Mechanical/IDF conversion helpers. Treat as specialized helper tools. |
| `kicad-cmd.bat` | Windows command prompt environment helper. Read-only reference unless user explicitly asks to start that shell. |

Safe agent actions:

- Check existence.
- Read file metadata.
- Run `kicad-cli version`.
- Run `kicad-cli --help` and subcommand `--help` for command discovery.

Do not:

- Install Python packages into KiCad's bundled Python.
- Copy scripts or project files into `bin`.
- Modify DLLs, EXEs, batch files, or KiCad Python files.
- Use GUI executables for blind automation.

## `kicad-cli` Behavior

Observed top-level help exposes these command families:

```text
fp, jobset, pcb, sch, sym, version
```

Observed subcommands:

| Command | Observed subcommands | Safe use posture |
| --- | --- | --- |
| `sch` | `erc`, `export` | Use through guarded repo wrappers for real projects. |
| `pcb` | `drc`, `export`, `render` | Use through guarded repo wrappers for real projects. |
| `fp` | `export`, `upgrade` | Export can be read/review oriented; upgrade modifies formats and must not be run on stock libraries. |
| `sym` | `export`, `upgrade` | Export can be read/review oriented; upgrade modifies formats and must not be run on stock libraries. |
| `jobset` | `run` | Jobsets may write outputs; use only with explicit output paths and logs. |
| `version` | `--format plain, commit, about` | Safe for version discovery. |

Agent rule: help/version discovery is not project approval. ERC, DRC, export, render, and jobset commands require an explicit project path, output path, and verification purpose.

## `share`

Windows top-level path:

```text
C:\Program Files\KiCad\9.0\share
```

Observed top-level children:

- `doc`
- `kicad`
- `locale`

The main KiCad stock data root is:

```text
C:\Program Files\KiCad\9.0\share\kicad
```

### `share\kicad\symbols`

Role: stock symbol libraries.

Observed examples:

- `Device.kicad_sym`
- `power.kicad_sym`
- `Connector.kicad_sym`
- `Connector_Generic.kicad_sym`
- `Interface_CAN_LIN.kicad_sym`
- `Interface_USB.kicad_sym`
- `MCU_Espressif.kicad_sym`
- `MCU_Module.kicad_sym`
- `Regulator_Linear.kicad_sym`
- `Regulator_Switching.kicad_sym`

Safe to index:

- Library file names.
- Symbol names.
- Pin names and pin numbers.
- Pin electrical types.
- Units.
- Datasheet and footprint fields.

Never modify stock symbol files. If a project needs a customized symbol, copy the required symbol into a project-local library and point `sym-lib-table` at that project-local file.

### `share\kicad\footprints`

Role: stock footprint libraries.

Observed important libraries include:

- `Connector_USB.pretty`
- `Connector_JST.pretty`
- `Connector_Molex.pretty`
- `Connector_PinHeader_2.54mm.pretty`
- `Package_DFN_QFN.pretty`
- `Package_SO.pretty`
- `Package_TO_SOT_SMD.pretty`
- `Capacitor_SMD.pretty`
- `Resistor_SMD.pretty`
- `RF_Module.pretty`
- `MountingHole.pretty`

Safe to index:

- Footprint library names.
- Footprint file names.
- Pad count and pad numbering.
- Pad geometry.
- Drill data.
- Courtyard, fab, and silkscreen layers.
- 3D model references.

Never modify stock `.pretty` folders. If a project needs a modified footprint, copy the footprint into a project-local `.pretty` library and verify it against the exact manufacturer drawing.

### `share\kicad\3dmodels`

Role: stock STEP/WRL 3D models.

Model paths are commonly referenced through `${KICAD9_3DMODEL_DIR}` from footprints.

Safe to index:

- Model existence.
- Model library folder names.
- Model filename matches.

Limits:

- A present 3D model does not prove footprint correctness.
- A visually aligned 3D model does not prove connector orientation.
- Mechanical fit still needs human review.

### `share\kicad\template`

Role:

- Stock project templates.
- Stock worksheet templates.
- Default `sym-lib-table`.
- Default `fp-lib-table`.

Observed template folders include Arduino, Raspberry Pi HAT, BeagleBone cape, STM32 Nucleo, LaunchPad, Eurocard, and enclosure-oriented examples.

Safe use:

- Read templates.
- Copy a template into a user project area before experiments.
- Read default library tables to understand stock KiCad path variables.

Never edit installed template folders in place.

### `share\kicad\demos`

Role: installed demos and examples.

Observed examples include:

- `complex_hierarchy`
- `flat_hierarchy`
- `multichannel`
- `simulation`
- `python_scripts_examples`
- `tiny_tapeout`
- `vme-wren`

Safe use:

- Read for examples.
- Copy a demo to a writable workspace before running experiments.

Never edit installed demo folders.

### `share\kicad\scripting`

Role:

- KiCad Python shell/editor helpers.
- Installed footprint wizard/plugin examples.

Observed plugin examples include:

- `bga_wizard.py`
- `qfn_wizard.py`
- `qfp_wizard.py`
- `FPC_wizard.py`
- `qrcode_footprint_wizard.py`
- `zip_wizard.py`

Safe use:

- Read as examples.
- Index names and roles.
- Copy a script into a project or repo tool area before modifying.

Never patch installed scripts.

### `share\kicad\schemas`

Observed files:

- `api.v1.schema.json`
- `pcm.v1.schema.json`

Safe use:

- Read for API/package-manager schema reference.
- Do not assume these schemas cover every KiCad source file format.

### `share\doc` And `share\locale`

Roles:

- Installed documentation.
- Localization data.

Safe use:

- Read for local reference.
- Do not edit.

## `lib`

Windows path:

```text
C:\Program Files\KiCad\9.0\lib
```

Observed roles:

- Crashpad static libraries and CMake support.
- `ngspice` code models such as `analog.cm`, `digital.cm`, `table.cm`, and transmission-line/event models.

Agent posture:

- Usually not needed for schematic/PCB review.
- Read-only runtime support.
- Do not index deeply unless diagnosing installation/runtime issues.
- Never modify.

## `etc`

Windows path:

```text
C:\Program Files\KiCad\9.0\etc
```

Observed role:

- Fontconfig configuration under `etc\fonts`.

Agent posture:

- Runtime support and reference config.
- Not normally relevant to KiCad project engineering.
- Never modify.

## Library Table Mechanics

KiCad resolves library nicknames through library tables.

Common files:

- Project-local `sym-lib-table`
- Project-local `fp-lib-table`
- Project-local `design-block-lib-table`
- User-global `sym-lib-table`
- User-global `fp-lib-table`
- User-global `design-block-lib-table`

Resolution priority for agents:

1. Project-local tables beside the `.kicad_pro`.
2. User-global tables, read-only.
3. Stock library table templates and stock install folders.

Observed stock KiCad 9 variables:

- `${KICAD9_SYMBOL_DIR}`
- `${KICAD9_FOOTPRINT_DIR}`
- `${KICAD9_3DMODEL_DIR}`

Common project-local variable:

- `${KIPRJMOD}`

Agent rule: prefer project-local references for reproducible designs. Do not silently make a project depend on a private global library.

## What To Copy Into A Project

Copy into project-local libraries when:

- A stock symbol needs a custom pin field, footprint field, alias, or datasheet field.
- A stock footprint needs any pad, courtyard, fab, silkscreen, paste, mask, or 3D model adjustment.
- A design must remain stable across KiCad library updates.
- A footprint has been verified against a specific manufacturer drawing and should be frozen for release.
- A connector or module footprint is high-risk and project-specific.

Do not copy entire stock libraries by default. Copy only the symbols, footprints, and models the project needs.

## High-Risk Installed Resource Assumptions

- Stock symbol presence does not prove pinout suitability.
- Stock footprint presence does not prove exact manufacturer part compatibility.
- Stock 3D model presence does not prove mechanical fit.
- KiCad 9 stock path variables do not automatically apply to KiCad 8, KiCad 10, or custom installs.
- Installed demo projects are examples, not templates for production without review.
- `fp upgrade` and `sym upgrade` can change file formats and must not be run on installed stock libraries.

## External Reference Links

- KiCad 9 documentation: https://docs.kicad.org/9.0/
- KiCad 10 documentation, path variable and library context: https://docs.kicad.org/10.0/en/kicad/kicad.html
- KiCad downloads: https://www.kicad.org/download/
