# Linux Package Manager Matrix

Status: planning and implementation guide for first Linux installer support.

Linux package availability varies by distro and version. The installer must detect the package manager, show the proposed command, and ask before installing anything.

## Detection Order

| Priority | Manager | Command | Primary Distros |
| ---: | --- | --- | --- |
| 1 | apt | `apt-get` | Ubuntu, Debian, Linux Mint, Pop!_OS |
| 2 | dnf | `dnf` | Fedora, modern RHEL-family |
| 3 | yum | `yum` | Older RHEL/CentOS-family |
| 4 | pacman | `pacman` | Arch, Manjaro |
| 5 | Flatpak | `flatpak` | Cross-distro desktop apps |
| 6 | snap | `snap` | Ubuntu and snap-enabled distros |

## Tool Matrix

| Tool | apt | dnf | yum | pacman | Flatpak | snap | Manual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KiCad / kicad-cli | `kicad` | `kicad` | `kicad` | `kicad` | `org.kicad.KiCad` | `kicad` | https://www.kicad.org/download/linux/ |
| Git | `git` | `git` | `git` | `git` | Not preferred | `git` | https://git-scm.com/download/linux |
| Python 3 | `python3` | `python3` | `python3` | `python` | Not preferred | `python` | https://www.python.org/downloads/ |
| Node.js/npm | `nodejs npm` | `nodejs npm` | `nodejs npm` | `nodejs npm` | Not preferred | `node --classic` | https://nodejs.org/ |
| VS Code | `code` after Microsoft repo setup | `code` after Microsoft repo setup | `code` after Microsoft repo setup | `code` or AUR/manual depending distro | `com.visualstudio.code` | `code --classic` | https://code.visualstudio.com/ |

## Notes

- Some distros require adding vendor repositories before `code` is available through `apt`, `dnf`, or `yum`.
- Flatpak is a useful fallback for VS Code and KiCad on desktop Linux, but command-line integration may differ.
- Snap command-line paths may live under `/snap/bin`.
- AppImage installer support should not assume any package manager.
- The setup scripts do not modify global KiCad libraries or user-global KiCad library tables.

## Install Safety

- Ask before every install command.
- Prefer official distro/package-manager paths.
- Do not collect credentials.
- Do not silently elevate privileges.
- If root is required and the script is not running as root, print the exact command for the user to review and run manually.
- Keep all generated fabrication outputs marked `NOT_FINAL`.
