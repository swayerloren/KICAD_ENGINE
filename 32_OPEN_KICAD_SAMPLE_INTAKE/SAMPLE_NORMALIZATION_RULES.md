# Sample Normalization Rules

Status: `ACTIVE_NORMALIZATION_RULES`

## Purpose

Protect upstream originals while giving Codex and Claude a safe working copy
for analysis, cleanup planning, and benchmark preparation.

## Rules

1. Never edit `imported_originals/`.
2. Create a working copy under `normalized_samples/` before any repair or
   cleanup experiment.
3. Normalization must preserve the upstream directory identity in the record.
4. Normalization must refuse paths inside `04_KICAD_PROJECTS/active/`.
5. Normalization must support dry-run mode before copying files.
6. Large binaries and generated fabrication outputs should not be promoted into
   public payloads by default even if they exist in the original sample.

## Allowed Normalization Actions

- copy source KiCad files into a working sample folder
- preserve source metadata
- add review reports next to the normalized sample
- create read-only metric outputs

## Prohibited Actions

- overwriting imported originals
- normalizing directly from active user projects
- deleting upstream files as part of normalization
- treating normalized copies as license proof

## Engineering Meaning

Normalization only creates a safe working copy. It does not prove:

- ERC quality
- DRC quality
- readable schematic style
- acceptable routing
- public payload eligibility
