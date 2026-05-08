# Security Model

Status: implemented as first security model draft for the Electron installer project.

## Threat Model

Installer risks include:

- Tampered installer or payload.
- Silent installation of unwanted tools.
- Accidental storage of AI credentials.
- Modification of installed KiCad app folders.
- Overwriting user KiCad projects.
- Bundling restricted datasheets.
- Mislabeling manufacturing outputs as final.
- Executing untrusted third-party scripts.

## Security Principles

- Transparent changes.
- User confirmation before installs.
- User-writable workspace by default.
- No hidden services.
- No credential collection.
- No KiCad app modification.
- Do not modify installed KiCad folders.
- No fabrication finality claims.
- Logs without secrets.

## Privilege Model

Default installer flow should not require administrator/root privileges.

Elevation may be needed only when the user explicitly chooses to install missing tools through a package manager. The installer must show the exact command before elevation or package-manager handoff.

## Credential Model

The installer must not request, store, or transmit:

- OpenAI API keys.
- Anthropic API keys.
- Codex credentials.
- Claude credentials.
- GitHub tokens.
- Distributor API keys.
- Fab-house API keys.
- SSH private keys.
- License keys.

Users must log in to their own AI tools outside the installer.

## KiCad Safety

The installer may read:

- Installed KiCad executable paths.
- `kicad-cli version`.
- Installed KiCad symbol, footprint, template, and 3D model folder metadata.

The installer must not write:

- Installed KiCad app folders.
- User-global KiCad library tables.
- Production KiCad project files.
- Manufacturing outputs marked final.

## Filesystem Safety

The installer must:

- Refuse installation into installed KiCad folders.
- Refuse installation into obvious system folders by default.
- Warn before using a non-empty target folder.
- Never delete user projects during install, repair, update, or uninstall.
- Back up before overwriting existing repo-controlled files in an update.

## Supply Chain

Before public release:

- Sign release artifacts.
- Publish checksums.
- Publish payload manifest.
- Generate SBOM if practical.
- Pin build dependencies for installer generation.
- Avoid bundling third-party repos in the installer payload unless reviewed.

## Payload Security

The generated payload template is built by `installer/payload/build_payload.py`.

The builder:

- uses allowlists and explicit exclusions;
- omits `.codex/config.toml` and writes `.codex/config.example.toml` instead;
- omits third-party cloned repositories and virtual environments;
- omits PDFs, generated outputs, KiCad project source files, backups, and logs;
- scans copied text for blocking secret-like patterns;
- replaces developer-specific local paths with placeholders;
- writes `payload.manifest.json` with relative paths, sizes, and SHA-256 hashes only.

## Health Check Gate

The installer should run `health_check` after setup and display:

- Pass count.
- Warn count.
- Fail count.
- Report path.
- Any blockers.

The installer should not proceed to final "ready" messaging when health check failures exist.
