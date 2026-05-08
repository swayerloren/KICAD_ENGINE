# Uncertainty Log: KiCad GUI Automation Layer

Date: `2026-05-06`

## Unverified Items

| Item | Status | Impact | Required Follow-Up |
|---|---|---|---|
| KiCad 9 Annotate Schematic dialog selectors | `UNVERIFIED` | Live annotation automation cannot be approved. | Test on disposable project with screenshots and selector mapping. |
| KiCad 9 ERC dialog selectors | `UNVERIFIED` | GUI ERC automation cannot be approved. | Test on disposable project and compare GUI/ERC report output. |
| Save conflict handling for live GUI state | `UNVERIFIED` | Save automation remains blocked. | Verify unsaved state detection, path match, backup, and conflict prompts. |
| Whether LJ's currently open KiCad view has stale cached visual state | `UNVERIFIED` | LJ may need to reload/reopen before visual review. | Confirm in GUI after native annotation/save workflow. |

## Disclosure Rule

Future agents must not describe the GUI layer as full automation until annotation, save, and ERC actions have been executed safely on a disposable project and documented with screenshots and reports.
