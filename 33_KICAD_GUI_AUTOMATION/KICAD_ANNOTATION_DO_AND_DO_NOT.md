# KiCad Annotation Do And Do Not

Status: `MANDATORY`

## Do

- Use KiCad native `Annotate Schematic` through the GUI automation gate when available.
- Confirm `eeschema.exe` is running or safely open the target `.kicad_pro` only when the task explicitly allows it.
- Confirm the open schematic path exactly matches the active project target schematic.
- Stop if Eeschema is open with a different project.
- Treat a title beginning with `*` as `UNSAVED_GUI_STATE`.
- Create a backup before any annotation/save-capable action.
- Capture screenshots before and after native GUI actions.
- Save from KiCad GUI after annotation when the task approves it and safety gates pass.
- Run GUI ERC when safely automatable.
- Run `kicad-cli` ERC after GUI save.
- Generate or update a placed-symbol reference table after GUI save.
- Keep PCB update blocked until the full schematic-to-PCB gate is exactly `PASS`.

## Do Not

- Do not use raw `.kicad_sch` text edits as proof of annotation success.
- Do not rely on regex scans alone.
- Do not treat saved-file CLI ERC as proof of live GUI state when LJ reports GUI-visible unresolved refs.
- Do not save a dirty `*` GUI state unless LJ explicitly approves and a backup exists.
- Do not annotate the wrong open project.
- Do not continue if multiple Eeschema windows make the target ambiguous.
- Do not combine annotation repair with visual layout cleanup unless the user explicitly asks for both and the annotation gate already passes.
- Do not update PCB, place parts, route, create zones, or generate manufacturing outputs from the annotation workflow.
- Do not claim `READY_FOR_LJ_VISUAL_REVIEW` from annotation success alone.

## Required Annotation Evidence

The annotation gate can pass only when these are recorded:

| Evidence | Required |
|---|---|
| exact open schematic path match | `YES` |
| backup path | `YES` |
| before screenshot | `YES` |
| native annotation dialog/action evidence | `YES` |
| schematic saved from KiCad GUI | `YES` |
| after screenshot | `YES` |
| GUI ERC 0 violations when safely automatable | `YES` |
| post-save `kicad-cli` ERC pass | `YES` |
| unresolved `?` reference scan | `0` |
| duplicate reference scan | `0` |

## Manual Fallback

If GUI automation is unsafe, tell LJ exactly:

```text
In KiCad: Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC.
Then confirm the GUI no longer shows question-mark references.
```

After LJ confirms, still run saved-file `kicad-cli` ERC and saved schematic reference/duplicate checks.

