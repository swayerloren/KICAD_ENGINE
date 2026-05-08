# Reference Design Verification Levels

## Required Public Statuses

Every reference item must be marked with one of these public statuses:

- `VERIFIED`
- `PARTIALLY_VERIFIED`
- `LINK_ONLY`
- `UNVERIFIED`

These statuses are intentionally conservative. They describe the reference record, not approval to copy or reuse a circuit.

## UNVERIFIED

The record is a placeholder or candidate source. Source URL, owner, license, design files, schematic accuracy, layout quality, or reuse safety may be unknown.

Use only as a research lead.

## LINK_ONLY

The record stores a public source link, summary, and metadata. Local design files are not copied into KiCad Engine.

Use for summaries, review questions, and source discovery. Do not copy schematic, layout, BOM, library, or manufacturing files from a link-only record.

## PARTIALLY_VERIFIED

Some source facts were checked, such as source owner, design type, source URL, or license status. Other items still require review.

Typical remaining review items include source revision, exact components, package drawings, connector orientation, license details, layout transferability, and human engineering review.

## VERIFIED

The record has documented source URL, owner, license or redistribution status, source date/revision when available, design format, extracted lesson, known limitations, and remaining review gates.

This is evidence, not automatic approval. Applying the pattern to a new design still requires exact part, symbol, footprint, connector, layout, ERC, DRC, and human review.

## Internal Review Notes

Agents may add internal notes such as `license-reviewed`, `files-allowed`, `technically-reviewed`, or `rejected-or-unsafe`, but the public status field must still be one of the four required statuses above.

## Rejected Or Unsafe Sources

The reference has license, technical, sourcing, safety, or quality issues that make it unsuitable for KiCad Engine reuse.

Keep a record only to prevent future agents from reusing it accidentally, and mark the public status `UNVERIFIED` with a clear rejection note.
