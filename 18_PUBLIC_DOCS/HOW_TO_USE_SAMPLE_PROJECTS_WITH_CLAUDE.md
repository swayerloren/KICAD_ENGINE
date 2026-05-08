# How To Use Sample Projects With Claude

Status: `PUBLIC_CLAUDE_SAMPLE_GUIDE`

## Goal

Use sample projects with Claude from VS Code as controlled KiCad workflow
fixtures. The sample project area is for review, reporting, and safe workflow
testing, not manufacturing approval.

## Start Claude In The Repo

Open this repository in VS Code and ask Claude to read:

1. `AGENTS.md`
2. `README_GPT.md`
3. `FOR CHAT GPT.MD`
4. `19_TEST_PROJECTS/README.md`
5. `03_TOOLS/scripts/project_gate/README.md`
6. `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md`

## Safe Prompt

```text
Use the KiCad Engine one-command project gate runner on:
19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board

This is read-only. Do not edit KiCad files, do not run ERC/DRC, and do not
generate fabrication outputs. Summarize the gate report and blockers.
```

Expected current result:

```text
BLOCKED_UNTIL_HUMAN_REVIEW
```

## What Claude Should Preserve

- Source attribution and license files.
- Existing reports and history.
- The distinction between imported originals and controlled sample copies.
- `NOT_FINAL` labels for generated review artifacts.

## What Claude Should Avoid

- Treating a blocked sample as a clean pass.
- Recommending fabrication while ERC/DRC/footprint blockers remain.
- Editing imported originals.
- Claiming unverified footprints, connector orientation, or polarity are correct.
- Making unsupported comparisons to Flux or any cloud PCB AI tool.
