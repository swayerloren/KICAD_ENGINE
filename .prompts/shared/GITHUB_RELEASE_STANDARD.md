# GitHub Release Standard

Use this standard before presenting KiCad Engine as public-release ready.

## Public Repo Requirements

- Clear README positioning: local-first KiCad AI engineering workspace, not a KiCad replacement.
- License selected.
- Installation/setup instructions.
- Windows KiCad path discovery documented.
- VS Code/Codex/Claude prompt pack documented.
- No secrets.
- No restricted datasheet PDFs unless redistribution rights are confirmed.
- No claims of full automatic PCB design or fabrication approval.
- Sample workflows demonstrated with reports.
- Release artifacts separated from project source.

## Required Checks

- Verify `.prompts` pack is present and documented.
- Verify `AGENTS.md` startup rules are current.
- Verify safe automation rules are current.
- Verify project validation scripts compile and run.
- Verify generated examples are marked `NOT_FINAL` or review-only.
- Check for accidental KiCad source edits in unrelated projects.
- Check for large or restricted binary files before publishing.

## Language To Use

Use realistic claims:

- "AI-assisted KiCad inspection and automation."
- "Local-first workspace."
- "KiCad-native review and validation tooling."
- "Human verification required for fabrication."

Avoid:

- "Fully automated PCB design."
- "Fabrication-ready without review."
- "Replaces KiCad."
- "Verified component database" unless every record has source evidence.
