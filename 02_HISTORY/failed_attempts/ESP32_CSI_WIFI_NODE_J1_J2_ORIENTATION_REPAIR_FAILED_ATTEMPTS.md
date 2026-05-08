# Failed Attempts - ESP32_CSI_WIFI_NODE J1/J2 Orientation Repair

Status: `ACTIVE_EVIDENCE`

Date: `2026-05-07`

## Records

| Attempt | Result | Follow-up |
|---|---|---|
| Bash-style `python - <<'PY'` in PowerShell | Failed with PowerShell redirection parse error. | Used PowerShell here-string piped to Python. |
| `git diff` in workspace | Failed because Git did not detect the checkout as a repository. | Continued with direct file inspection and reports. |
| J2 parent rotation `0 deg` before restoring embedded pad geometry | DRC showed J2 pad shorts because the embedded footprint copy had local pad rotations inherited from the previous placement. | Restored J2 local pad/marker rotations to installed KiCad footprint geometry. |
| `kicad-cli pcb render --pivot` with negative first component | CLI parsed the negative vector component as an unknown option. | Used a bottom-edge centered pivot for J1 blocker evidence. |

## Status

All failed attempts were worked around. Remaining blocker is not a failed command: J1 3D proof is blocked because the referenced barrel-jack STEP model is missing from the installed KiCad model library.
