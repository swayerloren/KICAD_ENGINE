# Projects Index

This file indexes the current, archived, and template KiCad projects inside KiCad Engine.

It is not the identity of the whole repo. The repo itself is `KiCad Engine`. The projects listed here are examples, current workspaces, and reusable starting points inside that larger workflow engine.

## Workspace Layout

| Folder | Purpose |
| --- | --- |
| `04_KICAD_PROJECTS/active` | current working KiCad projects |
| `04_KICAD_PROJECTS/archive` | older, demo, reference, or historical projects |
| `04_KICAD_PROJECTS/templates` | templates and scaffolds for new projects |

## Active Projects

### ESP32_CSI_WIFI_NODE

- Path: [04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE)
- Role: current active example/work-in-progress project
- Current status: live PCB exists, placement exists, partial routing exists, not fabrication-ready

Important:

- `ESP32_CSI_WIFI_NODE` is the current active example project only
- it is not the main purpose or identity of the repo
- future users can create their own active projects beside it under `04_KICAD_PROJECTS/active`

## Archived Projects

### CLEAN_KICAD_PASSING_SAMPLE

- Path: `04_KICAD_PROJECTS/archive/CLEAN_KICAD_PASSING_SAMPLE`
- Role: archived sample/reference workspace

### SAMPLE_KICAD_TEST_PROJECT

- Path: `04_KICAD_PROJECTS/archive/SAMPLE_KICAD_TEST_PROJECT`
- Role: archived demo/test project with historical reports and NOT_FINAL artifacts

## Templates

- Path: `04_KICAD_PROJECTS/templates`
- Role: starting templates, standard scaffolds, and reusable project setup patterns

## Using This Workspace

1. Put current live work under `04_KICAD_PROJECTS/active/<PROJECT_NAME>`.
2. Move old or frozen examples under `04_KICAD_PROJECTS/archive`.
3. Keep reusable starting points under `04_KICAD_PROJECTS/templates`.
4. Ask Codex or Claude to read `00_CODEX_START/` before doing project work.
