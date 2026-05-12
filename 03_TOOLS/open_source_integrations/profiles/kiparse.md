# KiParse

- Tool name: `KiParse`
- GitHub/source URL: `https://github.com/Atlantix-EDA/KiParse`
- License: `MIT`
- Purpose: fast parser for KiCad schematics and boards, useful for structured
  extraction and AI review workflows
- Install method: Rust toolchain or local source build
- Distribution mode: `optional`
- Supported OS: Windows, Linux, macOS where Rust is available
- Codex use cases:
  - parse KiCad files without inventing ad hoc regex-only readers
  - extract structured data for audits or review packets
  - support read-only digital-twin generation
- Exact commands if known:
  - `cargo install --git https://github.com/Atlantix-EDA/KiParse.git`
  - `cargo build --release`
- Risks and limitations:
  - requires Rust toolchain
  - not a replacement for KiCad-native proof when GUI or `pcbnew` evidence is
    required
- Can edit KiCad files: `no known default edit workflow`
- Read-only safe: `yes`
- Allowed in CI: `yes`
- Allowed in ZIP release: `no`, wrappers/docs only
