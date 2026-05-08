# WSL Setup Notes

These notes are planning notes only. Do not assume WSL is configured.

## Current Status

- WSL configuration is not assumed.
- No WSL commands were run during creation of these notes.
- No Linux packages were installed.
- No Windows PATH, WSL distribution, or interop settings were changed.

## Questions To Confirm Before WSL Setup

- Which WSL distribution should be used?
- Should KiCad run inside WSL, Windows, or both?
- Is GUI support required through WSLg, X11, or headless-only CLI?
- Should projects be stored on the Windows filesystem or inside the Linux filesystem?
- Will this be used for CI-like checks, GUI automation, or both?

## Cautions

- Avoid editing KiCad projects from both Windows and Linux at the same time.
- Be careful with line endings and filesystem permissions.
- Keep generated outputs in `05_OUTPUTS` or project report/output folders.
- Do not install packages or configure WSL without an explicit setup prompt.
- Do not run Linux GUI automation against production projects first.

## Future Setup Checklist

1. Confirm WSL is installed.
2. Confirm distribution and version.
3. Confirm GUI/display mode if needed.
4. Confirm KiCad install approach.
5. Confirm `kicad-cli` availability.
6. Confirm Python/pip/Git availability.
7. Run `check_linux_kicad_env.sh`.
8. Test only on disposable sample projects first.
