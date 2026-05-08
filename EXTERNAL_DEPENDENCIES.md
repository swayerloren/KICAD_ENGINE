# External Dependencies

| Item | Class | Notes |
| --- | --- | --- |
| KiCad | REQUIRED | Required for actual schematic and PCB GUI work. |
| Python | REQUIRED | Required for repo scripts, validation, maintenance, and index builders. |
| VS Code | OPTIONAL | Recommended local workspace shell. |
| Codex or Claude | OPTIONAL | Recommended AI agent interface for this repo workflow. |
| Git | OPTIONAL | Recommended for clone/sync/branch workflows; ZIP users can still read and use the repo locally. |
| GitHub CLI | OPTIONAL | Useful for GitHub automation and review tasks. |
| Codespaces | OPTIONAL | Useful for docs/scripts/review work, not full KiCad GUI design work. |
| FreeRouting | OPTIONAL | Only needed when a routing-feasibility or external-router workflow explicitly calls for it. |
| Node/npm | OPTIONAL | Only needed when a specific optional helper workflow requires it. |
| `03_TOOLS/node_envs` | LOCAL_ONLY | Local Node workspaces and dependencies; do not commit generated contents. |
| `03_TOOLS/python_envs` | LOCAL_ONLY | Local Python virtual environments; do not commit generated contents. |
| `03_TOOLS/repos` | LOCAL_ONLY | Local third-party cloned repos; not required for first use. |
| `03_TOOLS/tool_logs` | LOCAL_ONLY | Local tool logs and machine-specific notes. |
| `99_BACKUPS` | LOCAL_ONLY | Local backups before edits. |
| `routing_work` / `routing_rehearsals` scratch runs | LOCAL_ONLY | Future copied-board and scratch routing runs should stay local unless a specific sanitized evidence set is intentionally tracked. |
| Extra cloned GitHub repos | NOT_INCLUDED | Not required for the repo's basic workflow unless a specific optional workflow says otherwise. |
