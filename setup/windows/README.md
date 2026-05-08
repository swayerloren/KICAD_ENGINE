# Windows Setup

These scripts prepare KiCad Engine on Windows without making silent system changes.

## Scripts

- `setup_windows.ps1` runs safe repo setup helpers and health checks.
- `check_windows_requirements.ps1` runs the top-level health check.
- `install_missing_windows_tools.ps1` defaults to dry-run. It optionally installs missing tools with `winget` only when `-Apply` is passed and the user types `YES` for each install.

## Safe First Run

From the repo root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup\windows\check_windows_requirements.ps1
```

Then:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup\windows\setup_windows.ps1
```

## Optional Installs

To be offered installs for missing free tools:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup\windows\setup_windows.ps1 -OfferInstall
```

The installer uses `winget` when available and asks you to type `YES` for each install. Running `install_missing_windows_tools.ps1` directly without `-Apply` prints proposed commands and installs nothing.

## Safety

- No tools are installed unless you explicitly confirm.
- Paid tools are not installed.
- API keys, passwords, tokens, and license keys must never be stored in this repo.
- KiCad project files are not edited by setup.
- Fabrication-style outputs remain `NOT_FINAL` until the full verification gate passes.
