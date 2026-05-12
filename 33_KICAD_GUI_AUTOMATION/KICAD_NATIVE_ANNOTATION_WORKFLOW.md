# KiCad Native Annotation Workflow

Status: `DRY_RUN_DEFAULT_LIVE_GATED`

## Purpose

Use this workflow when annotation must be proven by KiCad's native GUI state,
not by raw `.kicad_sch` text edits.

Native KiCad GUI annotation is authoritative.

## Hard Rules

1. Raw `.kicad_sch` text edits are not accepted as annotation proof.
2. Default mode is dry-run only.
3. Live GUI opening/control requires `--live`.
4. Native annotation requires `--allow-annotation`.
5. GUI save requires `--allow-save`.
6. GUI ERC requires `--allow-gui-erc`.
7. If Eeschema is open for a different project, stop.
8. If the Eeschema title starts with `*`, stop unless the workflow was
   explicitly allowed to preserve/save that dirty GUI state.
9. Before any live annotation/save, create a backup.
10. After annotation, save from KiCad GUI, run GUI ERC, run post-save
    `kicad-cli` ERC, then scan the saved schematic for unresolved `?` and
    duplicate references.

## Required Inputs

- exact target `.kicad_pro`
- exact target `.kicad_sch`
- active project confirmation
- backup path for live actions

## Workflow

1. Detect the current Eeschema state.
2. If the exact target schematic is already open and clean, continue.
3. If Eeschema is not open, use the auto-open workflow to dry-run or live-open
   the exact target `.kicad_pro`, then open/focus the schematic editor.
4. If Eeschema is open with a different project, stop.
5. If the matching Eeschema window is dirty with `*`, stop unless explicitly
   allowed.
6. Capture a before screenshot.
7. Run KiCad native `Tools -> Annotate Schematic...`.
8. Save from KiCad GUI.
9. Run GUI ERC when safely automatable.
10. Capture an after screenshot.
11. Run post-save `kicad-cli sch erc`.
12. Scan the saved schematic for unresolved `?` references.
13. Scan the saved schematic for duplicate references.

## Dry-Run Command

```powershell
$repo = (Resolve-Path ".").Path
$project = Join-Path $repo "04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro"
$schematic = Join-Path $repo "04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch"

.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py `
  --project $project `
  --schematic $schematic
```

## Exact Future Live Command

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py `
  --project $project `
  --schematic $schematic `
  --live `
  --allow-annotation `
  --allow-save `
  --allow-gui-erc
```

If the already-open matching Eeschema window is dirty and LJ explicitly wants
that GUI state preserved/saved, add:

```powershell
--allow-unsaved-existing
```

## Pass Criteria

The authoritative annotation gate passes only when all of the following exist:

- exact open schematic path match
- backup path
- before screenshot
- native annotation action evidence
- schematic saved from KiCad GUI
- after screenshot
- GUI ERC 0 violations
- post-save `kicad-cli` ERC pass
- saved schematic scan with `0` unresolved `?` references
- saved schematic scan with `0` duplicate references

## Failure Criteria

Fail if:

- no Eeschema window is open and live open was not allowed
- a wrong-project Eeschema window is open
- the title starts with `*` and that state was not explicitly allowed
- backup is missing for live actions
- before or after screenshot capture fails
- native annotation dialog/action fails
- GUI save fails
- GUI ERC fails
- post-save `kicad-cli` ERC fails
- unresolved `?` references remain
- duplicate references remain

## Manual Fallback

If GUI automation is unsafe, tell LJ exactly:

```text
In KiCad: Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC.
Then confirm the GUI no longer shows question-mark references.
```

After LJ confirms, still run post-save `kicad-cli` ERC and saved-schematic
reference scans.
