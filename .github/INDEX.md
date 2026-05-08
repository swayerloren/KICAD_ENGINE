# .github Index

## PURPOSE
AI-readable index for GitHub automation files.

## WHAT_BELONGS_HERE
- `.github/workflows/` release, installer, and CI workflows.
- GitHub release workflow documentation.

## WHAT_DOES_NOT_BELONG_HERE
- API keys, signing certificates, or deployment credentials.
- Generated installer binaries.

## AI_AGENT_RULES
- Treat release publishing as opt-in and gated.
- Keep checksums and artifact names explicit.

## SAFE_EDIT_RULES
- Do not add secrets.
- Do not auto-publish public releases by default.

## PUBLIC_RELEASE_NOTES
- Release workflows should build payloads, run checks, upload artifacts, and draft releases only.
