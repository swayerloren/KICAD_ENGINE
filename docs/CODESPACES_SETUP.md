# Codespaces Setup

KiCad Engine supports GitHub Codespaces and VS Code devcontainers for repo tooling, validation, and documentation work.

Codespaces is optional. It is not required for local KiCad engineering work, and it is not a replacement for a local KiCad installation.

If you do not want Codespaces, you can download the repo ZIP or clone the repo, open it locally in VS Code, and use the same startup docs and workflow rules from the local checkout.

## Good Uses For Codespaces

- reading the repo and startup docs
- editing Markdown, JSON, YAML, and Python helper scripts
- running safe validation scripts
- reviewing reports and workflow outputs
- preparing pull requests

## Not A Good Fit For

- full KiCad GUI schematic or PCB work
- native Windows-only KiCad GUI automation
- final fabrication judgment
- pretending a Codespace is the live design authority

## Start A Codespace

1. Open the GitHub repo.
2. Choose `Code -> Codespaces`.
3. Create a new Codespace on the target branch.
4. Wait for the devcontainer bootstrap to complete.
5. Run `python health_check.py --no-write`.
6. Open the repo root and read `README.md`, `ONE_PROMPT_START.md`, `CURRENT_STATUS.md`, and `AGENTS.md` before changing anything significant.

## Important Limitation

KiCad GUI review still happens on the user's local machine with KiCad installed. Codespaces should be treated as a docs/script environment, not as full KiCad workstation replacement.

Missing KiCad in Codespaces is expected. `health_check.py` should report that as a warning, not a failure, unless `--require-kicad` is explicitly requested.
