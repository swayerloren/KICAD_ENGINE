# Sample Review Workflow

Status: `REQUIRED_BEFORE_PROMOTION`

## Review Goals

Determine whether an imported sample is useful as:

- link-only reference evidence,
- a local private study sample,
- a normalized sample for AI workflow testing,
- a benchmark candidate,
- a public-bundle sample.

## Required Checks

| Check | Required Before Promotion |
| --- | --- |
| Source URL | Yes |
| License status | Yes |
| Attribution record | Yes |
| KiCad file inventory | Yes |
| Original preserved | Yes |
| Normalized copy exists | Yes for analysis/benchmark use |
| ERC | Required if schematic exists and KiCad tools are available |
| DRC | Required if PCB exists and KiCad tools are available |
| Visual review | Required before layout/fab claims |
| Generated outputs | `NOT_FINAL` only |
| Human review | Required for public bundle, benchmark promotion, or reusable engineering claims |

## Review Statuses

- `REVIEW_NOT_STARTED`
- `FILE_AUDIT_ONLY`
- `LICENSE_BLOCKED`
- `ERC_DRC_PENDING`
- `REVIEWED_NOT_VERIFIED`
- `BENCHMARK_CANDIDATE`
- `REFERENCE_LINK_ONLY`
- `PUBLIC_BUNDLE_ALLOWED`
- `REJECTED`

## Hard Rule

A sample being complete enough to open in KiCad does not mean it is correct, verified, fabrication-ready, reusable, or safe to publish.
