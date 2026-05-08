# macOS Notarization Notes

Status: planning notes. No signing or notarization credentials are stored in this repo.

## Why Notarization Matters

Public macOS installer artifacts should be signed with an Apple Developer ID certificate and submitted to Apple notarization. Without signing and notarization, users may see Gatekeeper warnings or blocked launches.

## Required Apple Assets

These must be provided by the release maintainer through secure CI secrets or local keychain setup:

- Apple Developer ID Application certificate.
- Apple Developer ID Installer certificate if producing signed PKG installers.
- Apple Team ID.
- Apple ID or App Store Connect API key suitable for notarization.
- Keychain password or CI keychain unlock secret.

Do not commit any certificate, private key, app-specific password, issuer ID, key ID, API key, or keychain password to this repo.

## CI Secret Names

Recommended future GitHub Actions secret names:

- `APPLE_TEAM_ID`
- `APPLE_ID`
- `APPLE_APP_SPECIFIC_PASSWORD`
- `MACOS_CERTIFICATE_P12`
- `MACOS_CERTIFICATE_PASSWORD`
- `MACOS_KEYCHAIN_PASSWORD`

Alternative App Store Connect API secret names:

- `APPLE_API_KEY`
- `APPLE_API_KEY_ID`
- `APPLE_API_ISSUER_ID`

## Unsigned Build Mode

For source validation and internal smoke tests:

```bash
CSC_IDENTITY_AUTO_DISCOVERY=false npm run build:mac
```

Unsigned artifacts are not production release artifacts.

## Signed Release Flow

High-level release flow for a future signed build:

1. Import certificate into a temporary CI keychain.
2. Build payload.
3. Install npm dependencies with `npm ci`.
4. Build macOS artifacts with electron-builder signing enabled.
5. Notarize DMG/PKG artifacts.
6. Staple notarization tickets.
7. Run `spctl` and `xcrun stapler validate`.
8. Upload artifacts and checksums.
9. Record release report under `02_HISTORY/design_reviews`.

## Validation Commands

Use on macOS release machines:

```bash
codesign --verify --deep --strict --verbose=2 "path/to/KiCad Engine Installer.app"
spctl --assess --type execute --verbose "path/to/KiCad Engine Installer.app"
xcrun stapler validate "path/to/KiCad-Engine-Installer.dmg"
pkgutil --check-signature "path/to/KiCad-Engine-Installer.pkg"
```

## Security Rules

- Never collect Codex, Claude, ChatGPT, OpenAI, Anthropic, GitHub, distributor, or fab-house credentials.
- Never store Apple credentials in repo files.
- Never write into `/Applications/KiCad` or KiCad app-bundle internals.
- Never write to global KiCad libraries during installer setup.
- Keep public artifacts separate from local unsigned smoke builds.
