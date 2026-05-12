# Reference Designs

## PURPOSE

Store curated reference-design metadata, links, summaries, style-comparison
rules, and review notes that help AI agents learn from real circuit examples
without blindly copying them.

## WHAT_BELONGS_HERE

- link-first reference design records
- schematic-style comparison rules
- PCB layout-style comparison rules
- subsystem-specific reference notes for USB-C, ESP32 dev boards, and buck
  regulators
- source, license, and attribution notes
- human-review notes about reusable design patterns

## WHAT_DOES_NOT_BELONG_HERE

- proprietary design files without permission
- active KiCad project source files
- manufacturing outputs treated as final
- downloaded vendor archives unless redistribution is verified
- copied sample projects without controlled intake
- secrets or credentials

## AI_AGENT_RULES

- Treat reference designs as evidence, not automatic approval.
- Read `32_OPEN_KICAD_SAMPLE_INTAKE/` before promoting sample lessons here.
- Prefer reviewed metrics and summaries over copying source files.
- Mark uncertain details `UNVERIFIED`.
- Route more formal structured records to `12_REFERENCE_DESIGN_LIBRARY/` when
  they become stable library entries.

## SAFE_EDIT_RULES

- Add links, summaries, review notes, and style rules only.
- Do not edit active project files from here.
- Do not delete or overwrite prior records.

## PUBLIC_RELEASE_NOTES

Prefer links, metrics, and summaries for public release. Copied design files
require license and attribution review.
