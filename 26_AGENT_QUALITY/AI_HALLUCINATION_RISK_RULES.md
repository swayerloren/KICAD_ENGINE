# AI Hallucination Risk Rules

## Purpose

Identify and log situations where an AI agent may be presenting weakly supported KiCad engineering claims.

## High-Risk Claim Types

- Pinout from memory.
- Footprint from package name alone.
- Connector orientation from a generic image or similar connector.
- Voltage/current limits without source.
- Thermal or layout guidance without source.
- 3D model used as footprint proof.
- ERC/DRC pass claim without command output.
- BOM completeness without schematic and component-record review.
- Fab readiness without human review.

## Required Actions

If a high-risk claim appears:

1. Mark the claim `UNVERIFIED` or `REQUIRES_HUMAN_REVIEW`.
2. Create an uncertainty log.
3. Create a hallucination-risk log.
4. Add the claim to the claim/evidence matrix.
5. Do not proceed as if the claim is verified.

## Safe Language

Use:

- `candidate`
- `requires source verification`
- `requires package drawing`
- `requires human review`
- `not verified`

Avoid:

- `correct`
- `standard`
- `safe`
- `approved`
- `fab-ready`
- `should be fine`

