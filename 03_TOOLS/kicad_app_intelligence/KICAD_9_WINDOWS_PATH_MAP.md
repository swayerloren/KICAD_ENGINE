# KiCad 9 Windows Path Map

Date: 2026-05-02
Audited install root: `C:\Program Files\KiCad\9.0`
KiCad CLI version tested: `9.0.7`

## Confirmed Install Roots

The requested KiCad 9 Windows install paths exist on this machine:

| Path | Role | Agent posture |
| --- | --- | --- |
| `C:\Program Files\KiCad\9.0\bin` | KiCad executables, DLLs, bundled Python, KiCad Python API wrapper, command prompt helper | Read and execute approved read-only commands only |
| `C:\Program Files\KiCad\9.0\share` | KiCad stock data, symbols, footprints, 3D models, templates, demos, scripting files, schemas, resources | Read-only reference |
| `C:\Program Files\KiCad\9.0\etc` | Fontconfig configuration used by the KiCad runtime | Read-only reference |
| `C:\Program Files\KiCad\9.0\lib` | Link libraries, Crashpad CMake files, ngspice code models | Read-only reference |

Codex and Claude must not write into any `C:\Program Files\KiCad` folder.

## `bin`

Primary executables observed:

| Executable | Observed role | Version metadata |
| --- | --- | --- |
| `kicad.exe` | Main KiCad project manager GUI | 9.0.7 |
| `kicad-cli.exe` | CLI entry point for version, ERC, DRC, exports, and related automation | 9.0.7 |
| `eeschema.exe` | Schematic editor GUI | 9.0.7 |
| `pcbnew.exe` | PCB editor GUI | 9.0.7 |
| `gerbview.exe` | Gerber viewer GUI | 9.0.7 |
| `bitmap2component.exe` | Bitmap conversion utility | 9.0.7 |
| `pcb_calculator.exe` | Calculator GUI | 9.0.7 |
| `pl_editor.exe` | Page layout editor GUI | 9.0.7 |
| `python.exe` | Bundled KiCad Python | 3.11.5 |
| `pythonw.exe` | Bundled GUI/no-console Python | 3.11.5 |
| `dxf2idf.exe`, `idf2vrml.exe`, `idfcyl.exe`, `idfrect.exe` | IDF/DXF/VRML helper utilities | No KiCad product version metadata observed |
| `kicad-cmd.bat` | KiCad command-prompt setup helper | Batch file |

Important Python/API files:

- `C:\Program Files\KiCad\9.0\bin\Lib\site-packages\pcbnew.py`
- `C:\Program Files\KiCad\9.0\bin\_pcbnew.dll`
- `C:\Program Files\KiCad\9.0\bin\python.exe`
- `C:\Program Files\KiCad\9.0\bin\pythonw.exe`

Use the bundled Python only for KiCad-specific workflows that need KiCad's Python environment. Do not install packages into this bundled Python unless the user explicitly approves it. Prefer separate workspace virtual environments under `03_TOOLS\python_envs`.

## `share\kicad`

Observed top-level folders:

| Folder | Observed contents |
| --- | --- |
| `symbols` | 224 `.kicad_sym` stock symbol library files |
| `footprints` | 155 `.pretty` footprint library folders containing 15,415 `.kicad_mod` footprints |
| `3dmodels` | 105 `.3dshapes` folders containing 14,043 STEP/WRL-style model files |
| `template` | 19 stock project templates plus global default library table templates |
| `demos` | 19 demo/example groups, including simulation and Python-script examples |
| `scripting` | Python shell/editor helpers and footprint wizard/plugin scripts |
| `schemas` | `api.v1.schema.json` and `pcm.v1.schema.json` |
| `resources` | `images.tar.gz` |
| `internat` | Internationalization support assets |

## `share\kicad\symbols`

The stock symbol library folder contains `.kicad_sym` files referenced through `${KICAD9_SYMBOL_DIR}` in the symbol library table.

Examples:

- `Device.kicad_sym`
- `power.kicad_sym`
- `Connector.kicad_sym`
- `Connector_Generic.kicad_sym`
- `Interface_USB.kicad_sym`
- `Interface_CAN_LIN.kicad_sym`
- `MCU_Espressif.kicad_sym`
- `MCU_Module.kicad_sym`
- `Regulator_Linear.kicad_sym`
- `Regulator_Switching.kicad_sym`

Agents may read these files for symbol names, units, fields, and pin names. Agents must not edit stock symbol libraries.

## `share\kicad\footprints`

The stock footprint library folder contains `.pretty` folders referenced through `${KICAD9_FOOTPRINT_DIR}` in the footprint library table.

Large and important observed library families include:

- `Connector_JST.pretty`
- `Connector_Molex.pretty`
- `Connector_USB.pretty`
- `Connector_PinHeader_2.54mm.pretty`
- `Package_DFN_QFN.pretty`
- `Package_SO.pretty`
- `Package_TO_SOT_SMD.pretty`
- `Capacitor_SMD.pretty`
- `Resistor_SMD.pretty`
- `RF_Module.pretty`
- `MountingHole.pretty`

Agents may read footprint geometry, pad names, 3D model links, courtyard, mask, paste, and silkscreen data. Agents must not edit stock footprint libraries.

## `share\kicad\3dmodels`

The stock 3D model folder contains `.3dshapes` folders referenced through `${KICAD9_3DMODEL_DIR}` in footprint model paths.

Common model extensions observed:

- `.step`
- `.stp`
- `.wrl`

Agents may use this folder to verify whether a referenced stock 3D model exists. Missing 3D models do not always block fabrication, but they do block final mechanical/visual confidence until reviewed.

## `share\kicad\template`

Observed stock project templates include:

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

Important default library table templates:

- `C:\Program Files\KiCad\9.0\share\kicad\template\sym-lib-table`
- `C:\Program Files\KiCad\9.0\share\kicad\template\fp-lib-table`

These are stock templates. Do not edit them.

## `share\kicad\demos`

Observed demo/example groups include:

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

These are useful as read-only examples and disposable copy sources. Do not edit the installed demo folders. Copy a demo into `04_KICAD_PROJECTS\active` or `05_OUTPUTS` before experiments.

## `share\kicad\scripting`

Observed scripting/plugin files:

- `kicad_pyshell\__init__.py`
- `kicad_pyshell\kicad_pyeditor.py`
- Footprint wizard/plugin scripts such as `bga_wizard.py`, `qfn_wizard.py`, `qfp_wizard.py`, `FPC_wizard.py`, `qrcode_footprint_wizard.py`, and `zip_wizard.py`

These installed scripts are stock references. Agents may read them to understand KiCad scripting patterns. Do not modify them.

## `etc`

Observed role:

- Fontconfig configuration under `etc\fonts`.

Agents generally do not need this folder for PCB workflows. Treat it as runtime support data and read-only.

## `lib`

Observed role:

- Crashpad static libraries and CMake support under `lib` and `lib\cmake`.
- ngspice code models under `lib\ngspice`.

Agents generally do not need to read these files for ordinary schematic/PCB tasks except to note that the installed app includes ngspice runtime support. Treat as read-only.

## User Config And Library Table Locations

Observed current-user KiCad 9 config root:

- `%APPDATA%\kicad\9.0`
- On this machine: `C:\Users\LJ\AppData\Roaming\kicad\9.0`

Observed files include:

- `sym-lib-table`
- `fp-lib-table`
- `design-block-lib-table`
- `kicad_common.json`
- `kicad.json`
- `eeschema.json`
- `pcbnew.json`
- `3d_viewer.json`
- `user.hotkeys`

Other observed user paths:

- `%LOCALAPPDATA%\kicad\9.0`
- `%USERPROFILE%\Documents\KiCad\9.0`

Agents may read user library tables and preferences when necessary for path resolution. Do not edit user-global KiCad config unless the user explicitly requests it and a backup is created.

## Environment Variables And Path Assumptions

Stock library tables and footprints use these path variables:

- `${KICAD9_SYMBOL_DIR}` for stock symbols.
- `${KICAD9_FOOTPRINT_DIR}` for stock footprints.
- `${KICAD9_3DMODEL_DIR}` for stock 3D models.

Common project-local variable:

- `${KIPRJMOD}` resolves to the current project directory and is the preferred base for project-local libraries and models.

The installed `kicad-cmd.bat` sets a KiCad command-prompt environment:

- Adds `C:\Program Files\KiCad\9.0\bin` to `PATH`.
- Adds KiCad Python `Scripts` paths to `PATH`.
- Sets `PYTHONHOME` to the KiCad `bin` folder.
- Sets `PYTHONUTF8=1`.
- Uses `KIPRJMOD` as the starting directory when defined; otherwise starts under `%USERPROFILE%\Documents\KiCad\9.0`.

Current process environment did not expose `KICAD*` variables during this audit. Agents should not assume those variables are present in the shell. Resolve paths from KiCad config/library tables, known install roots, or explicit script parameters.

## Future KiCad Versions

For KiCad 10 or later:

- Detect `C:\Program Files\KiCad\<version>` dynamically.
- Prefer the highest installed version only when the project does not specify a required version.
- Use version-specific stock variables such as `${KICAD10_SYMBOL_DIR}` if KiCad adopts the same naming pattern.
- Capture `kicad-cli version` in every report.
- Do not hardcode `9.0` except in KiCad 9-specific documentation or examples.
