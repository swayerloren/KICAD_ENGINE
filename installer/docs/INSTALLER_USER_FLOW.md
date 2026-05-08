# Installer User Flow

## Flow

1. Open KiCad Engine Installer.
2. Installer detects Windows, macOS, or Linux.
3. Installer proposes a default workspace path:
   - Windows: `C:\Users\<user>\KICAD_ENGINE`
   - macOS/Linux: `~/KICAD_ENGINE`
4. User may choose another user-writable folder.
5. Installer checks dependencies:
   - KiCad
   - `kicad-cli`
   - Git
   - Python
   - Node.js
   - npm
   - VS Code
6. Installer shows missing dependencies.
7. User chooses whether to run package-manager install commands.
8. Installer copies the clean `repo-template` payload into the workspace.
9. Installer writes a setup log.
10. Installer runs the KiCad Engine health check.
11. Installer writes a health check report.
12. Installer opens VS Code if available and selected.

## User Choices

- Workspace folder.
- Whether to install missing tools.
- Whether to open VS Code after setup.

## Safety Interrupts

The installer refuses obvious system paths and installed KiCad app folders. It does not silently install tools and does not request credentials.
