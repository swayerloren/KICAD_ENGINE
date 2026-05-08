# Hallucination Risk Log - Open KiCad Sample Projects Audit

Date: `2026-05-03`

Risk label: `LOW_RISK_FOR_AUDIT`, `MEDIUM_RISK_FOR_PROMOTION_CLAIMS`

## Risk Controls Used

- Used local file inventory and `kicad-cli` outputs instead of relying on repository descriptions.
- Classified samples conservatively as `BROKEN_TEST_PROJECT`.
- Did not infer datasheet values, pinouts, package correctness, footprint correctness, or manufacturing readiness.
- Did not treat public/open-source availability as engineering verification.
- Did not treat SVG export success as visual approval.

## Remaining Hallucination Risks

1. Calling these samples clean benchmarks would be unsupported.
2. Calling these samples reference-grade designs would be unsupported.
3. Calling existing imported manufacturing files approved would be unsupported.
4. Treating missing-library/mismatch signals as final root cause without human review would be unsupported.

## Required Rule For Future Agents

Use these samples as broken/regression fixtures unless a later repair and re-audit pass proves a specific normalized sample meets a stricter promotion gate.

