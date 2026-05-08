# KiCad Window State Rules

## States

| State | Meaning | Agent Response |
| --- | --- | --- |
| `NO_EESCHEMA_WINDOW` | No schematic editor process found. | Do not run GUI actions. Ask LJ to open the schematic or use CLI-only checks. |
| `PATH_MATCH_CLEAN_TITLE` | Eeschema open path matches expected schematic and title does not start with `*`. | Read-only screenshot/discovery is acceptable. Save/annotation still requires gates. |
| `UNSAVED_GUI_STATE` | Eeschema title starts with `*`. | Do not save or annotate through automation unless LJ explicitly decides the GUI state should be kept and a backup exists. |
| `PATH_MISMATCH` | GUI open path differs from expected active schematic. | Stop. Do not click, save, annotate, or run GUI ERC. |
| `MULTIPLE_EESCHEMA_WINDOWS` | More than one schematic editor is open. | Stop unless the target window is unambiguously selected by exact path and screenshot. |

## Exact Path Rule

The open path must exactly match the active project schematic path after path normalization. Similar filenames or backup paths are not enough.

## Unsaved `*` Rule

If the Eeschema title starts with `*`, treat the GUI document as the current source of what LJ sees and the disk file as a separate saved state. File/CLI checks may be true for disk while false for GUI.

## Evidence Rule

Window state must be recorded in command logs before any GUI control request.
