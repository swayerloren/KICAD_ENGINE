# KiCad Installed App Do Not Touch Rules

Date: 2026-05-02

## Primary Rule

Codex, Claude, and other AI agents must treat `C:\Program Files\KiCad` as installed application state. It is not a workspace. It is not a scratch folder. It is not a place for generated reports, scripts, downloaded datasheets, project libraries, temporary files, or patched KiCad assets.

## Never Modify These Installed-App Paths

Never create, edit, move, rename, or delete files under:

- `C:\Program Files\KiCad\9.0\bin`
- `C:\Program Files\KiCad\9.0\etc`
- `C:\Program Files\KiCad\9.0\lib`
- `C:\Program Files\KiCad\9.0\share`
- Any future `C:\Program Files\KiCad\<version>` install folder

This includes:

- KiCad executables.
- DLLs and Python files.
- Stock symbols.
- Stock footprints.
- Stock 3D models.
- Stock templates.
- Installed demos.
- Scripting plugins and footprint wizards.
- Fontconfig files.
- ngspice runtime support files.
- Package-manager schemas/resources.

## Read-Only Is Allowed

Agents may read installed KiCad app files to understand:

- Which executables exist.
- Which KiCad version is installed.
- Where stock symbols, footprints, and 3D models live.
- Which stock templates and demos are available.
- How stock library tables reference environment variables.
- How the KiCad command prompt helper sets PATH/Python behavior.
- Whether a stock model or footprint file exists.

## Executable Use Rules

Allowed without project scope:

- `kicad-cli version` when the user asks to confirm the installed version.

Avoid unless explicitly requested:

- Running KiCad GUI executables.
- Running `kicad-cli --help` or broad command discovery if the user specifically asked for version-only testing.
- Running KiCad's bundled `python.exe`.
- Running package-manager or plugin actions.

Project-targeted commands require active project, backup, output path, and verification gates.

## User Config Caution

User-global KiCad config lives outside Program Files, typically:

- `%APPDATA%\kicad\<version>`
- `%LOCALAPPDATA%\kicad\<version>`
- `%USERPROFILE%\Documents\KiCad\<version>`

These folders are not installed-app folders, but they are still user state. Agents may read them for discovery. Agents must not edit user-global tables or preferences unless the user explicitly requests it and a backup is created.

Observed note from this audit: `kicad-cli version` is allowed and read-only with respect to Program Files, but KiCad executable launches may update user-level config timestamps. Avoid unnecessary executable calls.

## Project Library Rules

Use project-local libraries for project-specific symbols, footprints, and 3D models. Do not patch stock KiCad libraries to make a project work.

Preferred project-local locations:

- `PROJECT/kicad/symbols`
- `PROJECT/kicad/footprints`
- `PROJECT/kicad/3dmodels`
- Or the project template's established equivalent folders

Preferred variable:

- `${KIPRJMOD}`

## Output Rules

Write reports to:

- `02_HISTORY`
- `05_OUTPUTS`
- Approved project-local `reports`, `bom`, `fabrication`, or `renders` folders

Never write reports or exports into:

- `C:\Program Files\KiCad`
- Stock library folders
- Installed demo folders

## If A Stock Library Looks Wrong

Do not edit the stock file. Instead:

1. Record the issue in `02_HISTORY/design_reviews` or project history.
2. Copy or create a project-local replacement only after active project and backup gates are complete.
3. Point the project-local library table to the replacement using `${KIPRJMOD}`.
4. Run ERC/DRC and footprint review as appropriate.
5. Document why the project-local override exists.

## If KiCad Is Missing Or Moved

Scripts should fail gracefully and report:

- Which paths were checked.
- Whether `kicad-cli.exe` was found on `PATH`.
- Which output report was written.
- What the user should configure or install manually.

Do not install KiCad automatically unless a future explicit installer task is approved.
