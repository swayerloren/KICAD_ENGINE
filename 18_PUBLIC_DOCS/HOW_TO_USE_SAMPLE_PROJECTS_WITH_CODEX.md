# How To Use Sample Projects With Codex

Status: `PUBLIC_CODEX_SAMPLE_GUIDE`

## Goal

Use sample projects to test KiCad Engine workflows from VS Code without risking
active user designs.

## Start Codex In The Repo

Open your local `KICAD_ENGINE` repo root in VS Code, then ask Codex to read:

1. `AGENTS.md`
2. `README_GPT.md`
3. `FOR CHAT GPT.MD`
4. `19_TEST_PROJECTS/README.md`
5. `03_TOOLS/scripts/project_gate/README.md`
6. `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md`

## Safe Prompt

```text
Run the read-only KiCad Engine project gate runner on:
19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board

Do not edit KiCad design files.
Do not run ERC/DRC.
Do not generate fabrication outputs.
Report the final classification, blockers, and output report paths.
```

Expected current result:

```text
BLOCKED_UNTIL_HUMAN_REVIEW
```

## What Codex Should Explain

Codex should summarize:

- which gates passed
- which gates failed
- which gates require human review
- exact blocker list
- evidence paths
- why outputs are `NOT_FINAL`

## What Codex Must Not Do

- Do not edit `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, libraries, or footprints
  unless a later repair task explicitly approves edits and backup.
- Do not touch imported originals.
- Do not generate manufacturing outputs from a blocked sample.
- Do not claim the sample is a passing design.
- Do not claim KiCad Engine is better than a cloud PCB AI tool from this demo.

## Repair Tasks

If a future Codex task repairs a sample, it must use the controlled copy under
`19_TEST_PROJECTS/`, create a backup, preserve attribution, document each fix,
rerun evidence generation, and keep outputs `NOT_FINAL`.
