# freerouting

- Tool name: `freerouting`
- GitHub/source URL: `https://github.com/freerouting/freerouting`
- License: `GPL-3.0`
- Purpose: autorouting and routing-feasibility experimentation
- Install method: upstream release package, jar, Docker image, or local manual
  install
- Distribution mode: `external-only`
- Supported OS: Windows, Linux, macOS, Docker-capable systems
- Codex use cases:
  - copied-board routing rehearsal
  - feasibility scoring between placement variants
  - congestion comparison, never blind production approval
- Exact commands if known:
  - `docker run --rm -v <host-dir>:<container-dir> ghcr.io/freerouting/freerouting:<VERSION>`
- Risks and limitations:
  - can generate routes that still fail style, geometry, or project-specific
    constraints
  - GPL redistribution review is required before bundling
  - not acceptable as final routing proof by itself
- Can edit KiCad files: `yes`
- Read-only safe: `no by default`
- Allowed in CI: `conditional`
- Allowed in ZIP release: `no`
