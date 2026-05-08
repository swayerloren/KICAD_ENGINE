# Sample Promotion Rules

Status: `MANDATORY_BEFORE_REFERENCE_BENCHMARK_OR_PAYLOAD_USE`

## Promotion Targets

| Target | Required Status |
| --- | --- |
| `12_REFERENCE_DESIGN_LIBRARY` link record | Source URL, license status, attribution, and review notes. |
| `15_BENCHMARKS/benchmark_candidates` | Normalized copy, file audit, license screen, benchmark usefulness note, no fake results. |
| Public release payload | `PUBLIC_BUNDLE_ALLOWED`, attribution complete, generated outputs excluded, payload manifest updated. |

## Promotion Gates

1. Source URL and owner recorded.
2. License screened.
3. Attribution preserved.
4. KiCad source file inventory passed.
5. Original import preserved.
6. Normalized copy created for analysis.
7. Review report created.
8. Any ERC/DRC/visual results recorded honestly.
9. No generated manufacturing outputs are labeled final.
10. Public bundle decision is explicit.

## Blockers

Do not promote if:

- license is missing or restricted,
- attribution is incomplete,
- original source is not preserved,
- sample lacks KiCad source files,
- sample includes unclear third-party PDFs/models/assets,
- generated outputs are unlabeled or treated as final,
- benchmark result would be inferred instead of run.
