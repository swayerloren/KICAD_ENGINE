# Package Profiles Index

Status: `ACTIVE_SCAFFOLD`

## Folder Map

- `00_INDEX/`: schemas, package-to-footprint rules, and verification checklists.
- `QFN/`: generic and sourced QFN package profiles.
- `QFP/`: generic and sourced QFP package profiles.
- `SOIC/`: generic and sourced SOIC package profiles.
- `SOT/`: generic and sourced SOT package profiles.
- `DFN/`: generic and sourced DFN package profiles.
- `BGA/`: generic and sourced BGA package profiles.
- `MODULES/`: module package and keepout profile records.
- `CONNECTORS/`: connector package and mechanical-orientation profile records.
- `THROUGH_HOLE/`: through-hole package and drill profile records.
- `GENERIC_PACKAGES/`: common generic placeholders that are not approved until sourced.

## Core Files

- `00_INDEX/PACKAGE_PROFILE_SCHEMA.md`
- `00_INDEX/PACKAGE_TO_FOOTPRINT_RULES.md`
- `00_INDEX/PACKAGE_VERIFICATION_CHECKLIST.md`

## Starter Placeholder Profiles

- `QFN/QFN_GENERIC_PROFILE.md`
- `QFP/QFP_GENERIC_PROFILE.md`
- `SOIC/SOIC_GENERIC_PROFILE.md`
- `SOT/SOT_23_GENERIC_PROFILE.md`
- `MODULES/ESP32_MODULE_GENERIC_PROFILE.md`
- `CONNECTORS/USB_C_CONNECTOR_GENERIC_PROFILE.md`

## PURPOSE

Define package inclusion/exclusion profiles for release archives, installer payloads, review bundles, and docs bundles.

## WHAT_BELONGS_HERE

Profile docs, manifests, naming rules, inclusion rules, and exclusion rules.

## WHAT_DOES_NOT_BELONG_HERE

Large generated packages unless intentionally staged, secrets, final fab outputs, or private logs.

## AI_AGENT_RULES

- Read this folder's README.md and INDEX.md before adding or relying on content here.
- Mark unverified engineering claims explicitly.
- Keep source links, verification status, and human-review requirements visible.
- Route generated logs and reports to `02_HISTORY/`, `05_OUTPUTS/`, or project history unless this folder explicitly calls for generated indexes.

## SAFE_EDIT_RULES

- Preserve existing user work.
- Do not delete or overwrite files without explicit approval.
- Do not edit KiCad design files from this folder.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- Review this folder for secrets, personal paths, copyrighted documents, unsupported claims, and large generated files before public release.
- Folder existence is not a completeness or production-readiness claim.
