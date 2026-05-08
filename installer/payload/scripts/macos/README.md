# macOS Payload Scripts

Support scripts for the installer payload. The Electron app uses the dependency manifests first; these scripts are here for transparent manual fallback.

No script should silently install tools or store credentials.

`check_environment.sh` is read-only and checks the KiCad app bundle, app-bundle `kicad-cli`, command-line tools, VS Code, and Homebrew.
