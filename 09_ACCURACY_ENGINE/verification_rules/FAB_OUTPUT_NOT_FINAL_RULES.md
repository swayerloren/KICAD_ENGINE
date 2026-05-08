# Fab Output NOT_FINAL Rules

## Purpose

Prevent AI agents from treating generated fabrication-style files as approved manufacturing releases.

## Rule

All generated manufacturing-style outputs are `NOT_FINAL` until a human accepts the full review package.

This includes:

- Gerbers.
- Drill files.
- Pick-and-place files.
- BOMs for assembly.
- STEP or mechanical outputs.
- Assembly drawings.
- Fabrication drawings.
- Zipped manufacturing packages.

## Required Evidence Before Final Consideration

- ERC result reviewed.
- DRC result reviewed.
- BOM reviewed against schematic and component records.
- Footprints reviewed against exact package drawings.
- Connector orientation reviewed against exact drawings and mechanical intent.
- Polarity-sensitive parts reviewed.
- RF, USB, CAN, and high-current layout reviewed where applicable.
- Board outline and mounting/mechanical fit reviewed.
- Fab-house profile and output requirements reviewed.
- Human reviewer explicitly accepts the package.

## File Naming Rule

Generated review packages must include `NOT_FINAL` in folder or file names unless the user explicitly directs a final release workflow after all gates pass.

## AI Response Rule

Agents must write:

`AI review is not fabrication approval. Outputs remain NOT_FINAL until human review accepts them.`

when discussing generated fabrication-style outputs.

