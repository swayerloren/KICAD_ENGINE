# installer Index

## PURPOSE
AI-readable index for the current Electron installer source and payload builder implementation root.

## WHAT_BELONGS_HERE
- Installer source.
- Payload builder.
- Platform dependency manifests.
- Installer documentation.

## WHAT_DOES_NOT_BELONG_HERE
- AI credentials.
- User secrets.
- Installed KiCad app files.
- Random development junk in payload templates.

## AI_AGENT_RULES
- Do not claim production readiness until builds and smoke tests pass.
- Installer must use the user's installed KiCad app and must not modify installed KiCad folders.

## SAFE_EDIT_RULES
- Do not install system tools silently.
- Do not store credentials.
- Keep payload rules strict.

## PUBLIC_RELEASE_NOTES
- Public installer releases need checksums, artifact logs, platform smoke tests, and signing/notarization notes where applicable.
