# Installer User Flow

Status: `PLANNED`

## Flow

1. User launches installer.
2. Installer explains that KiCad Engine uses the user's installed KiCad app.
3. User selects workspace install path.
4. Installer checks dependencies.
5. Installer shows missing dependencies and manual/install-helper options.
6. User approves or skips each optional install.
7. Installer copies the approved payload.
8. Installer runs the health check.
9. Installer writes setup logs and report.
10. Installer opens VS Code in the new workspace if available.

## Required User Messages

- KiCad Engine is not official KiCad.
- KiCad Engine does not replace KiCad.
- Users must log in to their own AI tools.
- AI review is not fabrication approval.
- No credentials are collected or stored.

## Failure Behavior

If a dependency is missing or install is declined, the installer should finish with a clear report and manual next steps instead of failing destructively.

