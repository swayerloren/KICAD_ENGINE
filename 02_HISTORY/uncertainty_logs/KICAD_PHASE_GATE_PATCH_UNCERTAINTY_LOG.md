# Uncertainty Log - KiCad Phase Gate Patch

Date: `2026-05-07`

## Uncertainties

- The checker does not run KiCad ERC/DRC; it only inspects existing evidence files.
- The checker cannot know whether LJ approved a task unless the agent passes an explicit flag such as `--lj-approval`.
- Agents can still ignore instructions if they do not read startup docs, so the rule was duplicated in startup docs and prompt-pack files.

## Required Human/Agent Behavior

Agents must run or manually apply the checker before starting PCB phases. If blocked, they must redirect to the next required phase.

