# Installer Security Model

The installer is a local workspace bootstrapper. It must stay transparent and conservative.

## Guarantees

- It does not replace KiCad.
- It does not bundle KiCad.
- It does not collect credentials.
- It does not store Codex, Claude, ChatGPT, OpenAI, Anthropic, GitHub, distributor, or fab-house API keys.
- It does not write into installed KiCad app folders.
- It does not modify system KiCad libraries or user-global KiCad library tables.
- It does not mark fabrication outputs final.

## Write Scope

Allowed writes:

- The selected `KICAD_ENGINE` workspace folder.
- Setup logs under `05_OUTPUTS/setup_reports`.
- Health check reports under `05_OUTPUTS/health_checks`.

Disallowed writes:

- Installed KiCad folders.
- Program Files or system app folders.
- System KiCad libraries.
- User-global KiCad library tables.
- Existing user projects unless explicitly selected later by the user inside KiCad Engine.

## Dependency Installs

The installer detects missing dependencies and presents package-manager commands. It only runs install commands after explicit user confirmation.

Supported package-manager paths:

- Windows: `winget`.
- macOS: Homebrew.
- Linux: `apt`, `dnf`, `pacman`, `flatpak`, or `snap`.

If no supported package manager exists, the installer shows manual install URLs.

## Payload Integrity

The installer ships `payload/manifests/payload.manifest.json` with relative paths, sizes, and SHA-256 hashes for the clean repo template. Public release should add signed artifacts and checksums.

## Remaining Security Work

- Add artifact signing.
- Add notarization for macOS.
- Add checksum publication.
- Add reproducible build notes.
- Add clean-machine smoke-test logs.
