# KiCad Installed App Deep Audit

Date: 2026-05-02
Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`
Installed KiCad root audited: `C:\Program Files\KiCad\9.0`

## Scope

This audit inspected the installed KiCad app so KiCad Engine can teach Codex, Claude, and similar VS Code-based agents how to reliably use a user's installed KiCad application.

No files were modified under `C:\Program Files\KiCad`. No tools were installed. No repositories were cloned. No KiCad project design files were modified. The only KiCad executable command run was:

```powershell
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" version
```

Observed output:

```text
9.0.7
```

Note: KiCad executable launches can update user-level KiCad config timestamps even when only checking version. Avoid unnecessary KiCad executable calls during future audits.

## Requested Paths

All requested install paths exist:

| Path | Exists | Role |
| --- | --- | --- |
| `C:\Program Files\KiCad\9.0\etc` | Yes | Fontconfig/runtime configuration |
| `C:\Program Files\KiCad\9.0\lib` | Yes | Crashpad link libraries, CMake support, ngspice code models |
| `C:\Program Files\KiCad\9.0\share` | Yes | Stock data, symbols, footprints, 3D models, templates, demos, scripting, schemas |
| `C:\Program Files\KiCad\9.0\bin` | Yes | KiCad executables, DLLs, bundled Python, KiCad Python API |

## Executables In `bin`

Primary executable inventory:

| Executable | Role | Observed version metadata |
| --- | --- | --- |
| `kicad.exe` | Main KiCad project manager GUI | 9.0.7 |
| `kicad-cli.exe` | Command-line automation | 9.0.7 |
| `eeschema.exe` | Schematic editor GUI | 9.0.7 |
| `pcbnew.exe` | PCB editor GUI | 9.0.7 |
| `gerbview.exe` | Gerber viewer GUI | 9.0.7 |
| `bitmap2component.exe` | Bitmap conversion utility | 9.0.7 |
| `pcb_calculator.exe` | Calculator GUI | 9.0.7 |
| `pl_editor.exe` | Page layout editor GUI | 9.0.7 |
| `python.exe` | Bundled KiCad Python | 3.11.5 |
| `pythonw.exe` | Bundled GUI/no-console Python | 3.11.5 |
| `dxf2idf.exe`, `idf2vrml.exe`, `idfcyl.exe`, `idfrect.exe` | IDF/DXF/VRML helpers | Present |
| `kicad-cmd.bat` | KiCad command-prompt environment setup | Present |

Important API/runtime files:

- `C:\Program Files\KiCad\9.0\bin\Lib\site-packages\pcbnew.py`
- `C:\Program Files\KiCad\9.0\bin\_pcbnew.dll`
- `C:\Program Files\KiCad\9.0\bin\_eeschema.dll`
- `C:\Program Files\KiCad\9.0\bin\_kipython.dll`
- `C:\Program Files\KiCad\9.0\bin\ngspice.dll`

Agent rule: read metadata and run approved commands only. Do not install Python packages into the KiCad bundled Python without explicit approval.

## Installed Scripts And Plugins

Installed scripting root:

`C:\Program Files\KiCad\9.0\share\kicad\scripting`

Observed scripting/plugin files include:

- `kicad_pyshell\__init__.py`
- `kicad_pyshell\kicad_pyeditor.py`
- `plugins\arc_test.py`
- `plugins\bga_wizard.py`
- `plugins\circular_pad_array_wizard.py`
- `plugins\FootprintWizardBase.py`
- `plugins\FPC_wizard.py`
- `plugins\kicad_qrcode.py`
- `plugins\microMatch_connectors.py`
- `plugins\qfn_wizard.py`
- `plugins\qfp_wizard.py`
- `plugins\qrcode_footprint_wizard.py`
- `plugins\zip_wizard.py`

These are installed stock scripts. They are safe to read as examples. They must not be modified.

## Default Symbol Libraries

Stock symbol root:

`C:\Program Files\KiCad\9.0\share\kicad\symbols`

Observed:

- 224 `.kicad_sym` files.
- Stock symbol table template: `C:\Program Files\KiCad\9.0\share\kicad\template\sym-lib-table`
- Stock table uses `${KICAD9_SYMBOL_DIR}`.
- Stock table has 223 entries.
- Current user-global table has 227 entries at `%APPDATA%\kicad\9.0\sym-lib-table`.

Representative stock symbol libraries:

- `Device.kicad_sym`
- `power.kicad_sym`
- `Connector.kicad_sym`
- `Connector_Generic.kicad_sym`
- `Connector_Generic_MountingPin.kicad_sym`
- `Interface_USB.kicad_sym`
- `Interface_CAN_LIN.kicad_sym`
- `MCU_Espressif.kicad_sym`
- `MCU_Module.kicad_sym`
- `RF_Module.kicad_sym`
- `Regulator_Linear.kicad_sym`
- `Regulator_Switching.kicad_sym`

Agent use: read for pin names, symbol fields, units, and footprint field hints. Never edit stock symbols.

## Default Footprint Libraries

Stock footprint root:

`C:\Program Files\KiCad\9.0\share\kicad\footprints`

Observed:

- 155 `.pretty` folders.
- 15,415 `.kicad_mod` files.
- Stock footprint table template: `C:\Program Files\KiCad\9.0\share\kicad\template\fp-lib-table`
- Stock table uses `${KICAD9_FOOTPRINT_DIR}`.
- Stock table has 155 entries.
- Current user-global table has 158 entries at `%APPDATA%\kicad\9.0\fp-lib-table`.

Large/high-value footprint families:

- `Connector_JST.pretty`: 558 footprints.
- `Connector_Molex.pretty`: 812 footprints.
- `Connector_USB.pretty`: 75 footprints.
- `Package_DFN_QFN.pretty`: 766 footprints.
- `Package_SO.pretty`: 398 footprints.
- `Package_TO_SOT_SMD.pretty`: 137 footprints.
- `Inductor_SMD.pretty`: 690 footprints.
- `Capacitor_SMD.pretty`: 103 footprints.
- `Resistor_SMD.pretty`: 67 footprints.
- `MountingHole.pretty`: 167 footprints.

Agent use: read for pad names, pad numbers, geometry, layers, courtyard, paste/mask, silkscreen, fab data, and 3D model references. Never edit stock footprints.

## 3D Model Folders

Stock 3D model root:

`C:\Program Files\KiCad\9.0\share\kicad\3dmodels`

Observed:

- 105 `.3dshapes` folders.
- 14,043 files.
- Model references in stock footprints use `${KICAD9_3DMODEL_DIR}`.
- Common extensions: `.step`, `.stp`, `.wrl`.

Representative 3D model folders:

- `Connector_USB.3dshapes`
- `Connector_PinHeader_2.54mm.3dshapes`
- `Package_DFN_QFN.3dshapes`
- `Package_SO.3dshapes`
- `Package_TO_SOT_SMD.3dshapes`
- `Capacitor_SMD.3dshapes`
- `Resistor_SMD.3dshapes`
- `RF_Module.3dshapes`

Agent use: verify whether referenced models exist. Missing model files are visual/mechanical review items, not automatic electrical failures.

## Templates, Demos, And Examples

Template root:

`C:\Program Files\KiCad\9.0\share\kicad\template`

Observed template folders include:

- `Arduino_Uno`
- `Arduino_Mega`
- `Arduino_Nano`
- `Arduino_Micro`
- `Arduino_Pro_Mini`
- `RaspberryPi-HAT`
- `RaspberryPi-uHAT`
- `BeagleBone-Black-Cape`
- `STM32_Nucleo-64_Morpho`
- `STM32H7_DevEBox`
- `TI-LaunchPad-BoosterPack-20pin`
- `TI-LaunchPad-BoosterPack-40pin`
- `Hammond_1593K_Enclosure`
- `EuroCard160mmX100mm`

Demo root:

`C:\Program Files\KiCad\9.0\share\kicad\demos`

Observed demo/example folders include:

- `complex_hierarchy`
- `custom_pads_test`
- `flat_hierarchy`
- `multichannel`
- `simulation`
- `python_scripts_examples`
- `test_pads_inside_pads`
- `royalblue54L_feather`
- `tiny_tapeout`
- `vme-wren`

Agent rule: use installed templates and demos as read-only examples. Copy them into an approved workspace before any experiment.

## Environment Variables And Path Assumptions

Observed stock table/model variables:

- `${KICAD9_SYMBOL_DIR}` for stock symbols.
- `${KICAD9_FOOTPRINT_DIR}` for stock footprints.
- `${KICAD9_3DMODEL_DIR}` for stock 3D models.
- `${KIPRJMOD}` for current project directory and project-local assets.

The current shell did not expose `KICAD*` environment variables during the audit. Agents should not assume they exist in PowerShell.

`kicad-cmd.bat` behavior:

- Derives `KICAD_VERSION` from `kicad.exe` metadata.
- Adds KiCad `bin` to `PATH`.
- Adds KiCad Python script paths to `PATH`.
- Sets `PYTHONHOME` to the KiCad `bin` folder.
- Sets `PYTHONUTF8=1`.
- Starts in `%USERPROFILE%\Documents\KiCad\<version>` unless `KIPRJMOD` is defined.

KiCad user config file observed:

- `%APPDATA%\kicad\9.0\kicad_common.json`

The `environment.vars` field is currently `null`, so no user-overridden KiCad environment variables were observed in that file.

## Global User Library Tables On Windows

Typical KiCad 9 user-global library tables:

- `%APPDATA%\kicad\9.0\sym-lib-table`
- `%APPDATA%\kicad\9.0\fp-lib-table`
- `%APPDATA%\kicad\9.0\design-block-lib-table`

Observed current-user config root:

`C:\Users\LJ\AppData\Roaming\kicad\9.0`

Observed additional user roots:

- `%LOCALAPPDATA%\kicad\9.0`
- `%USERPROFILE%\Documents\KiCad\9.0`

Agent rule: read user-global tables only when needed to resolve libraries. Do not edit them unless explicitly requested and backed up.

## Project-Specific Library Tables

Project-specific library tables may live with a KiCad project:

- `sym-lib-table`
- `fp-lib-table`
- `design-block-lib-table`

Project-specific tables should reference project-local assets using `${KIPRJMOD}` instead of absolute paths. Example:

```text
${KIPRJMOD}/symbols/ProjectSymbols.kicad_sym
${KIPRJMOD}/footprints/ProjectFootprints.pretty
${KIPRJMOD}/3dmodels/Connector.step
```

Project-local libraries are the right place for project-specific verified symbols, exact footprints, embedded reference footprints, and local 3D models. Do not patch stock installed libraries to make a project work.

## What Codex Should Read

Codex may read:

- `bin` executable metadata.
- `kicad-cli version` output when requested.
- Stock symbol, footprint, and 3D model files.
- Stock template and demo names.
- Stock library table templates.
- User-global library tables for path resolution.
- Project-local library tables after active project scope is confirmed.
- `kicad-cmd.bat` for command-prompt environment behavior.
- `pcbnew.py` as an API reference.

## What Codex Must Never Modify

Codex must never modify:

- `C:\Program Files\KiCad\9.0\bin`
- `C:\Program Files\KiCad\9.0\etc`
- `C:\Program Files\KiCad\9.0\lib`
- `C:\Program Files\KiCad\9.0\share`
- Stock symbols.
- Stock footprints.
- Stock 3D models.
- Installed templates/demos.
- Installed scripting plugins.
- KiCad bundled Python or packages.
- User-global library tables unless explicitly requested and backed up.

## Deliverables Created

Architecture/intelligence docs:

- `03_TOOLS/kicad_app_intelligence/KICAD_9_WINDOWS_PATH_MAP.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_CLI_COMMANDS_REFERENCE.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_LIBRARY_DISCOVERY_GUIDE.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_DO_NOT_TOUCH_RULES.md`

Read-only audit scripts:

- `03_TOOLS/scripts/kicad_app_audit/audit_kicad_windows.ps1`
- `03_TOOLS/scripts/kicad_app_audit/check_kicad_cli.ps1`
- `03_TOOLS/scripts/kicad_app_audit/inventory_kicad_libraries.ps1`

## Risk Notes

- Do not assume `KICAD9_*` variables exist in the shell. Resolve them from install-root knowledge or KiCad tables.
- Do not assume user-global tables equal stock tables. This machine has more user-global symbol/footprint table entries than the stock templates.
- Do not use installed demo folders as writable test projects.
- Do not install Python packages into KiCad's bundled Python without explicit approval.
- Treat KiCad version drift as real: library paths, CLI options, file formats, ERC/DRC behavior, and package manager state can change between major/minor versions.

## Bottom Line

The installed KiCad 9 app provides a rich local asset base: executables, CLI, bundled Python/pcbnew API, stock symbol libraries, stock footprint libraries, 3D models, templates, demos, scripting examples, schemas, and simulation support. KiCad Engine should teach agents to read these assets as local evidence while keeping all generated outputs, project-specific fixes, and audit reports outside the installed app.
