# Part Lifecycle Status Rules

Status: `ACTIVE_RULES`

## Lifecycle Is Time-Sensitive

Lifecycle and availability can change. Do not claim a part is active, NRND, obsolete, or recommended for new designs unless a current source is recorded.

## Allowed Status Values

- `ACTIVE_VERIFIED_DATE`
- `NRND_VERIFIED_DATE`
- `OBSOLETE_VERIFIED_DATE`
- `DISCONTINUED_VERIFIED_DATE`
- `UNKNOWN_REQUIRES_SOURCE_VERIFICATION`
- `UNVERIFIED_PLACEHOLDER`

## Required Evidence

- Official vendor lifecycle status or authorized distributor status.
- Source URL.
- Review date.
- Notes on regional or distributor-specific availability.

## AI Rule

If lifecycle status matters to a design decision, verify it live or ask the user to confirm the accepted risk.

