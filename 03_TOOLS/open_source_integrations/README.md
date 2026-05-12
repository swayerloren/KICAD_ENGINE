# Open-Source KiCad Tool Integrations

This folder is the optional integration layer for proven external KiCad-adjacent
tools. It exists so Codex, Claude, and human contributors can reuse mature
parsers, validators, renderers, and rehearsal tools without pretending those
tools are first-party KiCad Engine code.

This layer is documentation and wrapper infrastructure first.

- The default repo must still work after a ZIP download.
- No giant third-party repos are required in the repo root.
- Optional tools must fail gracefully when missing.
- First-party wrappers and policy docs belong here.
- Downloaded repos, virtual environments, build trees, and big binaries do not
  belong in Git by default.

## What This Layer Covers

- Schematic parsing and read-only schematic API use
- PCB parsing and board extraction support
- Routing rehearsal and feasibility tooling
- ERC/DRC and package automation helpers
- Gerber/package validation
- Visual rendering and review helpers
- BOM/CPL and interactive review helpers
- AI review support that stays inside explicit evidence and license rules

## What This Layer Does Not Do

- It does not silently install tools.
- It does not vendor `node_modules`, `.venv`, or large binary payloads.
- It does not grant permission to edit KiCad design files.
- It does not override KiCad Engine phase gates, DRC/ERC gates, or release
  gates.
- It does not make third-party tool output automatically trustworthy.

## Folder Map

- `TOOL_REGISTRY.md`
  - Single registry of evaluated tools, source URLs, licenses, and use status.
- `INSTALL_POLICY.md`
  - Hard install rules for optional tools.
- `PORTABLE_TOOL_POLICY.md`
  - ZIP-portability and cache-location rules.
- `LICENSE_AND_ATTRIBUTION_RULES.md`
  - License and notice handling rules for third-party tools.
- `TOOLS_TO_EVALUATE.md`
  - Backlog and evaluation criteria for tools that are not yet approved.
- `TOOLS_APPROVED_FOR_LOCAL_USE.md`
  - Tools approved for optional local use under stated limits.
- `TOOLS_NOT_BUNDLED_REASON.md`
  - Why specific tools are intentionally not shipped inside the repo.
- `profiles/`
  - One profile per upstream tool.

## Default Installation Model

The approved default is:

1. Keep the repo portable after ZIP extraction.
2. Keep first-party wrappers and requirements files in Git.
3. Install lightweight optional Python packages into `.tools/venvs/` or a
   user-local cache only when explicitly requested.
4. Treat big repos, large jars, GUI bundles, and heavyweight native dependencies
   as `external-only`.

## First-Party Wrappers

Use these wrappers instead of improvising:

- `setup/install_optional_kicad_tools_windows.ps1`
- `setup/install_optional_kicad_tools_linux.sh`
- `setup/install_optional_kicad_tools_macos.sh`
- `setup/verify_optional_kicad_tools.py`

The install wrappers are dry-run by default. They only install on explicit
`--apply` or `-Apply`.

## Requirements Files

- `requirements-kicad-tools.txt`
- `requirements-fab-tools.txt`
- `requirements-visual-tools.txt`

These are for lightweight optional packages only. They are not approval to
vendor the installed environments into Git.

## Command Examples

Read-only verification:

```powershell
python setup\verify_optional_kicad_tools.py --dry-run
```

Windows install planning only:

```powershell
powershell -ExecutionPolicy Bypass -File setup\install_optional_kicad_tools_windows.ps1
```

Windows explicit apply:

```powershell
powershell -ExecutionPolicy Bypass -File setup\install_optional_kicad_tools_windows.ps1 -Apply
```

Linux or macOS install planning only:

```bash
./setup/install_optional_kicad_tools_linux.sh
./setup/install_optional_kicad_tools_macos.sh
```

## Route Rule

When the task router classifies a request as `OPEN_SOURCE_TOOL_USE`, agents must
read this folder before suggesting installs, cloning repos, or writing
attribution claims.

Third-party tool output remains advisory until it satisfies:

- `09_ACCURACY_ENGINE/workflows/EDA_AUTOMATION_VERIFICATION_WORKFLOW.md`
- `09_ACCURACY_ENGINE/verification_rules/AUTOMATION_TOOL_RESULT_VALIDATION_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/CALCULATOR_RESULT_EVIDENCE_RULES.md`
