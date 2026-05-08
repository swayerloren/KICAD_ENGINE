# Using KiCad Engine With Codex

Codex can help with KiCad Engine from VS Code when it starts with the repo's rules and prompt pack.

## Start

1. Open `KICAD_ENGINE` in VS Code.
2. Log in to Codex with your own account.
3. Open `.prompts/codex/00_START_SESSION.md`.
4. Paste it into Codex.
5. For task-specific work, use prompts from `.prompts/codex/`.

## What To Ask Codex

Good tasks:

- Audit the installed KiCad app.
- Review a schematic or PCB.
- Run ERC or DRC through repo scripts.
- Create a component research summary.
- Add a verified component record.
- Check footprint candidates.
- Generate a `NOT_FINAL` review package.
- Improve documentation or scripts.

## What To Require

Require Codex to:

- Read `AGENTS.md`.
- Read startup files before KiCad project work.
- Avoid KiCad source edits until the active project and backup plan are confirmed.
- Log meaningful work in `02_HISTORY/`.
- Mark uncertain datasheet values as unknown.
- Keep fabrication-style outputs `NOT_FINAL`.

## What Not To Ask

Do not ask Codex to certify a board for production. Codex can help gather evidence, but final manufacturing decisions remain with the user.
