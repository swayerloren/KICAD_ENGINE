# External Dependencies

| Item | Class | Needed For Basic Use | Included In Repo | Install Needed | Notes |
| --- | --- | --- | --- | --- | --- |
| KiCad | REQUIRED | No for docs-only use; yes for live schematic/PCB GUI work | No | Yes | Required for actual schematic and PCB GUI work. |
| Python | REQUIRED | Yes | No | Yes | Required for repo scripts, validation, maintenance, and health checks. |
| VS Code | RECOMMENDED | No, but strongly recommended | No | Optional | Recommended local workspace shell. |
| Codex or Claude | RECOMMENDED | No, but strongly recommended for the AI workflow | No | Optional | Recommended AI agent interface for this repo workflow. |
| Git | OPTIONAL | No for ZIP users | No | Optional | Recommended for clone/sync/branch workflows. |
| GitHub CLI | OPTIONAL | No | No | Optional | Useful for GitHub automation and review tasks. |
| Codespaces | OPTIONAL | No | No | Optional | Useful for docs/scripts/review work, not full KiCad GUI design work. |
| FreeRouting | OPTIONAL | No | No | Optional | Only needed when a routing-feasibility or external-router workflow explicitly calls for it. |
| Node/npm | OPTIONAL | No | No | Optional | Only needed when a specific optional helper workflow requires it. |
| Windows GUI helper pip packages | OPTIONAL | No | Metadata only | Optional | Install with `python -m pip install \".[windows-gui]\"` only when Windows GUI automation is explicitly needed. |
| `03_TOOLS/node_envs` | LOCAL_ONLY | No | Placeholder only | No | Local Node workspaces and dependencies; do not commit generated contents. |
| `03_TOOLS/python_envs` | LOCAL_ONLY | No | Placeholder only | No | Local Python virtual environments; do not commit generated contents. |
| `03_TOOLS/repos` | LOCAL_ONLY | No | Placeholder only | No | Local third-party cloned repos; not required for first use. |
| `03_TOOLS/tool_logs` | LOCAL_ONLY | No | Placeholder only | No | Local tool logs and machine-specific notes. |
| `99_BACKUPS` | LOCAL_ONLY | No | Placeholder only | No | Local backups before edits. |
| `routing_work` / `routing_rehearsals` scratch runs | LOCAL_ONLY | No | Placeholder only | No | Copied-board and scratch routing runs should stay local unless a sanitized evidence subset is intentionally promoted. |
| Extra cloned GitHub repos | NOT_INCLUDED | No | No | No | Not required for the repo's basic workflow unless a specific optional workflow says otherwise. |
