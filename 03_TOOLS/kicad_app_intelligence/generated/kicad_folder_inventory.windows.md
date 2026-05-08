# Deep KiCad Folder Inventory

Generated UTC: `2026-05-03T01:26:41.763459+00:00`
KiCad root: `C:\Program Files\KiCad\9.0`

## Resource Counts

- Symbol library files: `223`
- Footprint library folders: `155`
- Footprint files: `15415`
- 3D model library folders: `105`
- 3D model files: `14043`
- Template folders: `19`
- Demo/example folders: `19`
- Scripting Python files: `20`

## Folder Summary

| Key | Role | Exists | Files | Dirs | Path |
| --- | --- | ---: | ---: | ---: | --- |
| `root` | install root | True | 37293 | 1145 | `C:\Program Files\KiCad\9.0` |
| `bin` | executables and runtime DLLs | True | 6590 | 604 | `C:\Program Files\KiCad\9.0\bin` |
| `share` | shared installed resources | True | 30659 | 532 | `C:\Program Files\KiCad\9.0\share` |
| `share_kicad_or_data_root` | KiCad stock libraries, templates, demos, scripts, schemas | True | 30567 | 435 | `C:\Program Files\KiCad\9.0\share\kicad` |
| `symbols` | stock symbol libraries | True | 224 | 0 | `C:\Program Files\KiCad\9.0\share\kicad\symbols` |
| `footprints` | stock footprint libraries | True | 15415 | 155 | `C:\Program Files\KiCad\9.0\share\kicad\footprints` |
| `3dmodels` | stock 3D model libraries | True | 14043 | 105 | `C:\Program Files\KiCad\9.0\share\kicad\3dmodels` |
| `template` | stock project templates and library table templates | True | 180 | 43 | `C:\Program Files\KiCad\9.0\share\kicad\template` |
| `demos` | installed demos and examples | True | 659 | 98 | `C:\Program Files\KiCad\9.0\share\kicad\demos` |
| `scripting` | installed Python scripting helpers and footprint wizards | True | 20 | 2 | `C:\Program Files\KiCad\9.0\share\kicad\scripting` |
| `schemas` | KiCad JSON schemas | True | 2 | 0 | `C:\Program Files\KiCad\9.0\share\kicad\schemas` |
| `resources` | images and runtime resources | True | 1 | 0 | `C:\Program Files\KiCad\9.0\share\kicad\resources` |
| `lib` | runtime/link libraries and ngspice code models | True | 19 | 3 | `C:\Program Files\KiCad\9.0\lib` |
| `etc` | runtime configuration reference files | True | 23 | 2 | `C:\Program Files\KiCad\9.0\etc` |
| `doc` | installed documentation | True | 0 | 2 | `C:\Program Files\KiCad\9.0\share\doc` |
| `locale` | localization files | True | 92 | 92 | `C:\Program Files\KiCad\9.0\share\locale` |

## Executables

- KiCad CLI: `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`
- Runtime DLL count: `199`

| Name | Role | Size | Path |
| --- | --- | ---: | --- |
| `_freeze_module.exe` | runtime or helper executable | 2962272 | `C:\Program Files\KiCad\9.0\bin\_freeze_module.exe` |
| `bitmap2component.exe` | bitmap-to-component utility | 2608480 | `C:\Program Files\KiCad\9.0\bin\bitmap2component.exe` |
| `crashpad_handler.exe` | runtime or helper executable | 656736 | `C:\Program Files\KiCad\9.0\bin\crashpad_handler.exe` |
| `dxf2idf.exe` | runtime or helper executable | 145248 | `C:\Program Files\KiCad\9.0\bin\dxf2idf.exe` |
| `eeschema.exe` | schematic editor GUI | 994656 | `C:\Program Files\KiCad\9.0\bin\eeschema.exe` |
| `gerbview.exe` | Gerber viewer GUI | 383840 | `C:\Program Files\KiCad\9.0\bin\gerbview.exe` |
| `idf2vrml.exe` | runtime or helper executable | 300896 | `C:\Program Files\KiCad\9.0\bin\idf2vrml.exe` |
| `idfcyl.exe` | runtime or helper executable | 63328 | `C:\Program Files\KiCad\9.0\bin\idfcyl.exe` |
| `idfrect.exe` | runtime or helper executable | 56672 | `C:\Program Files\KiCad\9.0\bin\idfrect.exe` |
| `kicad-cli.exe` | KiCad command-line automation entry point | 2629984 | `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe` |
| `kicad-cmd.bat` | Windows KiCad command prompt environment helper | 2694 | `C:\Program Files\KiCad\9.0\bin\kicad-cmd.bat` |
| `kicad.exe` | main KiCad project manager GUI | 6036832 | `C:\Program Files\KiCad\9.0\bin\kicad.exe` |
| `pcb_calculator.exe` | PCB calculator GUI | 384352 | `C:\Program Files\KiCad\9.0\bin\pcb_calculator.exe` |
| `pcbnew.exe` | PCB editor GUI | 994656 | `C:\Program Files\KiCad\9.0\bin\pcbnew.exe` |
| `pl_editor.exe` | page layout editor GUI | 689504 | `C:\Program Files\KiCad\9.0\bin\pl_editor.exe` |
| `python.exe` | bundled KiCad Python | 103776 | `C:\Program Files\KiCad\9.0\bin\python.exe` |
| `pythonw.exe` | bundled KiCad Python without console | 102240 | `C:\Program Files\KiCad\9.0\bin\pythonw.exe` |
| `venvlauncher.exe` | runtime or helper executable | 114016 | `C:\Program Files\KiCad\9.0\bin\venvlauncher.exe` |
| `venvwlauncher.exe` | runtime or helper executable | 111968 | `C:\Program Files\KiCad\9.0\bin\venvwlauncher.exe` |

## Command Behavior

Only `kicad-cli` version/help discovery was run. No project commands, exports, ERC, or DRC were run by this inventory script.

### `version`

Exit code: `0`

```text
9.0.7
```

### `help`

Exit code: `0`

```text
Usage: kicad-cli [--version] [--help] {fp,jobset,pcb,sch,sym,version}

Optional arguments:
  -v, --version  prints version information and exits 
  -h, --help     Shows help message and exits 

Subcommands:
  fp            Footprint and Footprint Libraries
  jobset        Jobset
  pcb           PCB
  sch           Schematics
  sym           Symbol and Symbol Libraries
  version       Reports the version info in various formats
```

### `sch_help`

Exit code: `0`

```text
Usage: sch [--help] {erc,export}

Schematics

Optional arguments:
  -h, --help  Shows help message and exits 

Subcommands:
  erc        Runs the Electrical Rules Check (ERC) on the schematic and creates a report
  export     Export utilities (netlist, pdf, bom, etc)
```

### `pcb_help`

Exit code: `0`

```text
Usage: pcb [--help] {drc,export,render}

PCB

Optional arguments:
  -h, --help  Shows help message and exits 

Subcommands:
  drc        Runs the Design Rules Check (DRC) on the PCB and creates a report
  export     Export utilities (Gerbers, drill, position files, etc)
  render     Renders the PCB in 3D view to PNG or JPEG image
```

### `fp_help`

Exit code: `0`

```text
Usage: fp [--help] {export,upgrade}

Footprint and Footprint Libraries

Optional arguments:
  -h, --help  Shows help message and exits 

Subcommands:
  export     Export utilities (svg)
  upgrade    Upgrades the footprint library to the current kicad version format
```

### `sym_help`

Exit code: `0`

```text
Usage: sym [--help] {export,upgrade}

Symbol and Symbol Libraries

Optional arguments:
  -h, --help  Shows help message and exits 

Subcommands:
  export     Export utilities (svg)
  upgrade    Upgrades the symbol library to the current kicad version format
```

### `jobset_help`

Exit code: `0`

```text
Usage: jobset [--help] {run}

Jobset

Optional arguments:
  -h, --help  Shows help message and exits 

Subcommands:
  run        Runs a jobset file
```

### `version_help`

Exit code: `0`

```text
Usage: version [--help] [--format VAR]

Reports the version info in various formats

Optional arguments:
  -h, --help  Shows help message and exits 
  --format    version info format (plain, commit, about) [nargs=0..1] [default: "plain"]
```
