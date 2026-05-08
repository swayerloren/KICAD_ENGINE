# KiCad GUI Failure Modes

## Unsaved GUI State

Symptom: Eeschema title starts with `*`.

Risk: GUI state differs from disk. Saving may overwrite disk with stale or unintended data.

Response: stop unless LJ explicitly decides the GUI state should be kept and a backup exists.

## Disk/GUI Mismatch

Symptom: CLI/file parse says annotation passes, but GUI shows question-mark references.

Risk: agent is checking disk while user sees live GUI state.

Response: require KiCad-native annotation and GUI verification.

## Path Mismatch

Symptom: process command line path differs from active project path.

Risk: agent may edit/review the wrong schematic.

Response: stop.

## Multiple Eeschema Windows

Symptom: multiple `eeschema.exe` windows found.

Risk: wrong window gets controlled.

Response: stop unless exact path and screenshot identify one target.

## Missing GUI Libraries

Symptom: `pywinauto` or `pyautogui` unavailable.

Risk: scripts cannot safely control GUI.

Response: use manual fallback.

## Selector Map Not Verified

Symptom: script cannot identify KiCad menu/dialog controls by stable selectors.

Risk: random clicks/hotkeys.

Response: do not automate; provide exact manual steps.

## GUI ERC Does Not Match CLI ERC

Symptom: KiCad GUI reports errors but CLI report is clean.

Risk: unsaved state, stale markers, or project context mismatch.

Response: preserve GUI evidence, run native GUI workflow, save only after approval, re-run both checks.
