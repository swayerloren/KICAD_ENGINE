# Linux Payload Scripts

Support scripts for the installer payload. The Electron app uses the dependency manifests first; these scripts are here for transparent manual fallback.

No script should silently install tools or store credentials.

`check_environment.sh` is read-only and checks KiCad, `kicad-cli`, common development tools, VS Code, distro metadata, and supported package managers.
