# Hallucination Risk Log - Open KiCad Sample Candidate Discovery

Date: 2026-05-03

Risk label: `MEDIUM_RISK`

## Risk Sources

- Candidate complexity and usefulness are partly inferred from repository descriptions, file presence, and category fit.
- GitHub file-tree metadata verifies file presence, not actual KiCad project health.
- License names are source-backed, but compatibility for public bundling requires human review.
- Source-included Gerbers and STEP files may have separate third-party or manufacturing assumptions.

## Mitigations Used

- Did not clone, download, or import repositories.
- Marked candidates as `CANDIDATE_LINK_ONLY`.
- Kept first-import recommendations separate from import approval.
- Marked KiCad official demo as `NEEDS_HUMAN_LICENSE_REVIEW` due larger source-repo license context.
- Recorded uncertainty and human review requirements.

## Required Next Gate

Before import, the user must explicitly approve the candidate list and the agent must run the sample import workflow under `32_OPEN_KICAD_SAMPLE_INTAKE/`.
