# How To Add A Component

Adding a component should begin with research, not schematic placement.

## Research Checklist

1. Find the official vendor product page or datasheet.
2. Record source URL and document type.
3. Check voltage, current, package, pin count, lifecycle, and errata.
4. Identify required external components.
5. Identify layout rules.
6. Find KiCad symbol candidates.
7. Find KiCad footprint candidates.
8. Verify the exact package drawing before approving a footprint.
9. Add or update the component record.

## Prompt Pack

Use:

- `.prompts/codex/03_RESEARCH_COMPONENT.md`
- `.prompts/codex/04_ADD_COMPONENT_TO_DATABASE.md`
- `.prompts/claude/03_RESEARCH_COMPONENT.md`
- `.prompts/claude/04_ADD_COMPONENT_TO_DATABASE.md`

## Component Record Location

Use the appropriate category under `08_COMPONENT_DATABASE/`.

For unknown or unverified parts, use `99_UNVERIFIED_INBOX/` and mark the record `UNVERIFIED_PLACEHOLDER`.

## Do Not Invent Specs

If a value is not verified, write:

```text
Unknown - requires source verification
```
