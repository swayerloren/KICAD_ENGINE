# Schematic Style Examples

Status: `REFERENCE_COMPARISON_ONLY`

## Purpose

Define how Codex and Claude should compare generated schematics against
human-made examples without copying them.

## Compare These Things

- functional block grouping
- wire-to-label balance
- left-to-right or top-to-bottom flow
- whitespace around MCU/module pins
- local clarity around USB, power, and reset/boot blocks
- readability of reference/value placement

## Do Not Compare By

- raw symbol count alone
- sheet size alone
- presence of lots of labels
- whether a sample happens to route power or USB on a different side

## Safe Use

Use reviewed sample metrics to say:

- "this schematic uses far more labels than the reviewed examples"
- "this block spacing is tighter than the sample range"
- "the generated USB section is less readable than the reference pattern"

Do not say:

- "the sample did it this way, so this design is correct"

## Promotion Rule

Only samples with acceptable quality score and clear license handling should
appear in future curated schematic style summaries.
