# KiCad Paths: Windows, macOS, Linux, And AppImage

Date: 2026-05-03

Purpose: give AI agents expected KiCad app path patterns while requiring local detection on every machine.

## Prime Rule

Detect paths on the user's machine. Treat the paths below as expected patterns, not proof.

Run:

```bash
kicad-cli version
```

or use a full detected path to `kicad-cli`.

## Windows KiCad 9

Audited path on this machine:

```text
C:\Program Files\KiCad\9.0
```

Expected KiCad 9 layout:

| Resource | Expected path |
| --- | --- |
| Executables | `C:\Program Files\KiCad\9.0\bin` |
| `kicad-cli` | `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe` |
| Main GUI | `C:\Program Files\KiCad\9.0\bin\kicad.exe` |
| Schematic GUI | `C:\Program Files\KiCad\9.0\bin\eeschema.exe` |
| PCB GUI | `C:\Program Files\KiCad\9.0\bin\pcbnew.exe` |
| Stock data root | `C:\Program Files\KiCad\9.0\share\kicad` |
| Symbols | `C:\Program Files\KiCad\9.0\share\kicad\symbols` |
| Footprints | `C:\Program Files\KiCad\9.0\share\kicad\footprints` |
| 3D models | `C:\Program Files\KiCad\9.0\share\kicad\3dmodels` |
| Templates | `C:\Program Files\KiCad\9.0\share\kicad\template` |
| Demos | `C:\Program Files\KiCad\9.0\share\kicad\demos` |
| Scripting | `C:\Program Files\KiCad\9.0\share\kicad\scripting` |
| Runtime libraries | `C:\Program Files\KiCad\9.0\lib` |
| Runtime config | `C:\Program Files\KiCad\9.0\etc` |

Expected user-global config:

```text
%APPDATA%\kicad\9.0
%LOCALAPPDATA%\kicad\9.0
%USERPROFILE%\Documents\KiCad\9.0
```

Important: never write into `C:\Program Files\KiCad`.

## macOS App Bundle

Common KiCad app location:

```text
/Applications/KiCad/KiCad.app
```

Expected app-bundle patterns:

| Resource | Expected pattern |
| --- | --- |
| Executables | `/Applications/KiCad/KiCad.app/Contents/MacOS/` |
| `kicad-cli` | `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli` |
| Main GUI | `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad` |
| Stock data root | `/Applications/KiCad/KiCad.app/Contents/SharedSupport/` or `.../Contents/SharedSupport/kicad/` |
| Symbols | `.../Contents/SharedSupport/symbols` or `.../Contents/SharedSupport/kicad/symbols` |
| Footprints | `.../Contents/SharedSupport/footprints` or `.../Contents/SharedSupport/kicad/footprints` |
| 3D models | `.../Contents/SharedSupport/3dmodels` or `.../Contents/SharedSupport/kicad/3dmodels` |
| Templates | `.../Contents/SharedSupport/template` or `.../Contents/SharedSupport/kicad/template` |

Expected user config patterns:

```text
~/Library/Preferences/kicad/<version>/
~/Library/Application Support/kicad/<version>/
```

macOS packaging has varied across versions. Agents must detect the actual `Contents/SharedSupport` layout before indexing.

Do not modify the KiCad app bundle.

## Linux Package Installs

Common package install patterns:

| Resource | Expected pattern |
| --- | --- |
| `kicad` GUI | `/usr/bin/kicad` or `/usr/local/bin/kicad` |
| `kicad-cli` | `/usr/bin/kicad-cli` or `/usr/local/bin/kicad-cli` |
| Stock data root | `/usr/share/kicad` or `/usr/local/share/kicad` |
| Symbols | `/usr/share/kicad/symbols` |
| Footprints | `/usr/share/kicad/footprints` |
| 3D models | `/usr/share/kicad/3dmodels` |
| Templates | `/usr/share/kicad/template` |
| Demos | `/usr/share/kicad/demos` |
| Scripting | `/usr/share/kicad/scripting` |
| Runtime libraries | `/usr/lib`, `/usr/lib64`, `/usr/local/lib`, or distro-specific KiCad paths |

Expected user config:

```text
~/.config/kicad/<version>/
~/.local/share/kicad/<version>/
~/Documents/KiCad/<version>/
```

Linux package layout depends on distro and packaging source. Detect with:

```bash
which kicad
which kicad-cli
kicad-cli version
```

Do not modify `/usr`, `/usr/local`, `/app`, `/opt`, or package-managed KiCad folders unless the user is intentionally administering the system outside this repo workflow.

## Linux Flatpak

Common Flatpak patterns:

```text
/var/lib/flatpak/app/org.kicad.KiCad/
~/.local/share/flatpak/app/org.kicad.KiCad/
```

Flatpak apps may run in a sandbox and expose data paths differently from distro packages.

Agent rule:

- Prefer `flatpak run org.kicad.KiCad --version` only for user-requested app checks.
- Prefer normal `kicad-cli` if exposed on `PATH`.
- Do not modify Flatpak app installation data.

## Linux AppImage

An AppImage is commonly a single executable file, for example:

```text
~/Applications/KiCad-<version>-x86_64.AppImage
```

Possible inspection modes:

- Run the AppImage's normal commands if supported by that package.
- Mount or extract the AppImage into a temporary folder only if the user explicitly requests it.
- Inventory the extracted/mounted root, often with internal paths resembling `usr/bin` and `usr/share/kicad`.

Agent rule:

- Do not assume AppImage internals are available as normal filesystem paths.
- Do not modify a mounted/extracted AppImage resource tree.
- Treat extracted AppImage contents as read-only system resources.

## Cross-Platform Path Variables

Common KiCad variables:

| Variable | Meaning |
| --- | --- |
| `${KIPRJMOD}` | Current project directory; preferred base for project-local libraries. |
| `${KICAD9_SYMBOL_DIR}` | KiCad 9 stock symbol directory. |
| `${KICAD9_FOOTPRINT_DIR}` | KiCad 9 stock footprint directory. |
| `${KICAD9_3DMODEL_DIR}` | KiCad 9 stock 3D model directory. |

For other KiCad versions, detect the actual variable names and resolved paths instead of guessing.

## Scripted Inventory

Use:

```bash
python 03_TOOLS/scripts/kicad_app_audit/deep_kicad_folder_inventory.py --kicad-root "<installed-kicad-root>"
```

Examples:

```powershell
python 03_TOOLS\scripts\kicad_app_audit\deep_kicad_folder_inventory.py --kicad-root "C:\Program Files\KiCad\9.0" --platform-name windows
```

```bash
python 03_TOOLS/scripts/kicad_app_audit/deep_kicad_folder_inventory.py --kicad-root /Applications/KiCad/KiCad.app --platform-name macos
```

```bash
python 03_TOOLS/scripts/kicad_app_audit/deep_kicad_folder_inventory.py --kicad-root /usr --platform-name linux
```

## External Reference Links

- KiCad downloads: https://www.kicad.org/download/
- KiCad documentation: https://docs.kicad.org/
- AppImage overview: https://docs.appimage.org/
