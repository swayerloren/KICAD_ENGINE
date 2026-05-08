# Uncertainty Log - Post Sample Project Production Audit

Date: `2026-05-06`

| Uncertainty | Status | Required Resolution |
| --- | --- | --- |
| Whether the ATtiny85 sample source may be bundled publicly | `UNVERIFIED_PENDING_HUMAN_REVIEW` | Final license/release review must record `PUBLIC_BUNDLE_ALLOWED`. |
| Whether broad repo contains real credentials | `UNVERIFIED` | Run a proper secret scanner excluding virtualenvs/tool repos or inspect flagged paths safely. |
| Whether payload rules are enforceable | `PARTIAL` | Build `17_RELEASE_BUILD/build_public_payload.py` and run dry-run validation. |
| Whether the ATtiny85 sample can become a passing demo | `UNVERIFIED` | Resolve ERC/DRC/footprint/visual blockers and rerun gates. |
| Whether upstream sample licenses cover all copied hardware files | `NEEDS_HUMAN_LICENSE_REVIEW` | Human legal/attribution review. |
