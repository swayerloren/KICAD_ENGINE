# KiCad Annotation Do And Do Not

Status: `MANDATORY`

## Do

- Use KiCad native `Annotate Schematic` as the authoritative annotation action.
- Use the dry-run-first auto-open workflow if Eeschema is closed.
- Open only the exact target `.kicad_pro` and exact target `.kicad_sch`.
- Stop if Eeschema is already open for a different project.
- Treat a title beginning with `*` as unsaved GUI state.
- Create a backup before any live annotation/save workflow.
- Capture before and after screenshots for live workflows.
- Save from KiCad GUI after annotation.
- Run GUI ERC after save.
- Run post-save `kicad-cli` ERC.
- Scan the saved schematic for unresolved `?` references.
- Scan the saved schematic for duplicate references.

## Do Not

- Do not treat raw `.kicad_sch` text edits as annotation proof.
- Do not treat file regex scans alone as authoritative proof.
- Do not annotate, save, or run GUI ERC in a wrong-project Eeschema window.
- Do not continue when multiple Eeschema windows make the target ambiguous.
- Do not save a dirty `*` window unless that state was explicitly allowed and a
  backup exists.
- Do not combine annotation proof with PCB update, routing, zones, or
  manufacturing outputs.

## Required Live Flags

| Action | Required flags |
| --- | --- |
| open project/schematic | `--live` |
| native annotation | `--live --allow-annotation` |
| GUI save | `--live --allow-save` |
| GUI ERC | `--live --allow-gui-erc` |
| preserve already-dirty matching GUI state | `--allow-unsaved-existing` |

## Required Annotation Evidence

| Evidence | Required |
| --- | --- |
| exact open schematic path match | `YES` |
| backup path | `YES` |
| before screenshot | `YES` |
| native annotation action evidence | `YES` |
| schematic saved from KiCad GUI | `YES` |
| after screenshot | `YES` |
| GUI ERC 0 violations | `YES` |
| post-save `kicad-cli` ERC pass | `YES` |
| unresolved `?` reference scan | `0` |
| duplicate reference scan | `0` |

## Exact Future Live Command

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py `
  --project "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro" `
  --schematic "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch" `
  --live `
  --allow-annotation `
  --allow-save `
  --allow-gui-erc
```
