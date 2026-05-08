# KiCad Folder Role Matrix

Date: 2026-05-03

Purpose: quick AI-agent decision matrix for installed KiCad folders.

## Windows KiCad 9 Matrix

| Folder | Role | Safe to read | Safe to index | Safe to execute | Safe to copy from | Never modify | Project-local copy target |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `C:\Program Files\KiCad\9.0\bin` | Executables, DLLs, bundled Python, helper tools | Yes | Metadata only | `kicad-cli version/help` only by default | No, except documenting paths | Yes | None |
| `C:\Program Files\KiCad\9.0\share` | Shared installed resources | Yes | Yes | No | Yes, after license/relevance check | Yes | `04_KICAD_PROJECTS/...` or project-local libs |
| `...\share\kicad\symbols` | Stock symbol libraries | Yes | Yes | No | Yes, selected symbols only | Yes | `project/libs/symbols/*.kicad_sym` |
| `...\share\kicad\footprints` | Stock footprint libraries | Yes | Yes | No | Yes, selected footprints only | Yes | `project/libs/footprints/*.pretty` |
| `...\share\kicad\3dmodels` | Stock 3D models | Yes | Yes | No | Yes, selected models only | Yes | `project/libs/3dmodels` or project model folder |
| `...\share\kicad\template` | Stock templates and stock library table templates | Yes | Yes | No | Copy templates before use | Yes | New project workspace |
| `...\share\kicad\demos` | Demo/example projects | Yes | Yes | No | Copy before experiments | Yes | Disposable project copy |
| `...\share\kicad\scripting` | Python shell helpers and footprint wizards | Yes | Names/source only | No | Copy before modification | Yes | `03_TOOLS/scripts` or project tools |
| `...\share\kicad\schemas` | JSON schemas for KiCad API/package metadata | Yes | Yes | No | Usually no need | Yes | Repo docs/tools if needed |
| `...\share\doc` | Installed documentation | Yes | Optional | No | Link or cite only unless license reviewed | Yes | Repo docs only when allowed |
| `...\share\locale` | Localization resources | Yes | No practical need | No | No | Yes | None |
| `C:\Program Files\KiCad\9.0\lib` | Runtime/link libraries and ngspice code models | Yes | Usually no | No | No | Yes | None |
| `C:\Program Files\KiCad\9.0\etc` | Runtime configuration reference files | Yes | Usually no | No | No | Yes | None |

## Agent Defaults

- Read installed KiCad folders as system reference material.
- Index stock symbols, footprints, and 3D models to find candidates.
- Resolve project-local libraries before global or stock libraries.
- Copy selected stock resources into project-local libraries only when the project needs stability or customization.
- Never edit installed KiCad resources in place.

## Copy Decision Rules

Copy a stock resource into a project-local library when:

- The design requires a frozen symbol/footprint version.
- The resource must be customized.
- The project must remain reproducible without relying on a user's global library state.
- A high-risk footprint needs reviewed project-specific notes.

Do not copy:

- Whole stock symbol or footprint library trees without a reason.
- Installed runtime files.
- DLLs, executables, bundled Python files, or system config.
- Demos unless creating an explicit disposable copy.

## Indexing Risk Levels

| Resource type | Indexing risk | Main caution |
| --- | --- | --- |
| Symbol library names | Low | Name match is not pinout verification. |
| Symbol pins/fields | Medium | Compare to datasheet before use. |
| Footprint names | Low | Name match is not package verification. |
| Footprint pads/geometry | Medium | Compare to exact manufacturer drawing. |
| 3D model paths | Low | 3D model presence is not mechanical approval. |
| Templates/demos | Medium | Examples may be old or not applicable. |
| Runtime files | High | Usually unnecessary and never writable. |
