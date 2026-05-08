# Using KiCad Engine With Claude

Claude can use the same local-first KiCad workflow when started from the prompt pack.

## Start

1. Open `KICAD_ENGINE` in VS Code.
2. Log in to Claude with your own account.
3. Open `.prompts/claude/00_START_SESSION.md`.
4. Paste it into Claude.
5. Use task-specific prompts from `.prompts/claude/`.

## Recommended Tasks

- KiCad install audit.
- Component research.
- Datasheet summary drafting.
- Schematic review.
- PCB review.
- ERC/DRC workflow guidance.
- NOT_FINAL package review.
- Repo memory and history updates.

## Safety Expectations

Claude should follow the same rules as Codex:

- No unbacked KiCad source edits.
- No fabricated datasheet claims.
- No unverified footprint approval.
- No hidden credential storage.
- No final fabrication claims without evidence and human approval.

## Cross-Agent Use

If using both Codex and Claude, keep durable decisions in `01_MEMORY/` and command or review history in `02_HISTORY/` so each agent can read the same local context.
