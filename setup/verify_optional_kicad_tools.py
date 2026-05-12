from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class ToolCheck:
    tool_id: str
    category: str
    distribution_mode: str
    check_type: str
    target: str | None
    note: str


@dataclass
class ToolResult:
    tool_id: str
    category: str
    distribution_mode: str
    status: str
    detail: str


TOOLS = [
    ToolCheck("kiparse", "kicad", "optional", "command", "kiparse", "Rust-installed CLI"),
    ToolCheck("kicad_python_pcbnew", "kicad", "external-only", "command", "kicad-cli", "KiCad CLI on PATH"),
    ToolCheck("pcbnew_module", "kicad", "external-only", "module", "pcbnew", "KiCad Python module"),
    ToolCheck("kicad_sch_api", "kicad", "optional", "module", "kicad_sch_api", "PyPI module"),
    ToolCheck("skidl", "kicad", "optional", "module", "skidl", "PyPI module"),
    ToolCheck("circuit_synth", "kicad", "optional", "module", "circuit_synth", "PyPI module"),
    ToolCheck("freerouting", "kicad", "external-only", "command", "freerouting", "Upstream executable if manually installed"),
    ToolCheck("kicad_routing_tools", "kicad", "external-only", "manual", None, "Upstream repo checkout required"),
    ToolCheck("kicad_component_layout", "kicad", "external-only", "manual", None, "Upstream repo checkout required"),
    ToolCheck("kikit", "fab", "optional", "command", "kikit", "PyPI CLI"),
    ToolCheck("kibot", "fab", "optional", "command", "kibot", "PyPI or system install"),
    ToolCheck("gerbonara", "fab", "optional", "module", "gerbonara", "PyPI module"),
    ToolCheck("pygerber", "visual", "optional", "module", "pygerber", "PyPI module"),
    ToolCheck("interactive_html_bom", "visual", "optional", "command", "generate_interactive_bom", "PyPI CLI"),
    ToolCheck("pcbdraw", "visual", "optional", "command", "pcbdraw", "PyPI CLI"),
    ToolCheck("kicad_happy", "kicad", "optional", "module", "kicad_happy", "PyPI module"),
    ToolCheck("kicad_library_utils", "kicad", "external-only", "manual", None, "External upstream checkout required"),
]


def check_tool(tool: ToolCheck) -> ToolResult:
    if tool.check_type == "command":
        path = shutil.which(tool.target or "")
        if path:
            return ToolResult(tool.tool_id, tool.category, tool.distribution_mode, "PRESENT", path)
        status = "NOT_INSTALLED" if tool.distribution_mode == "optional" else "EXTERNAL_NOT_FOUND"
        return ToolResult(tool.tool_id, tool.category, tool.distribution_mode, status, tool.note)

    if tool.check_type == "module":
        if importlib.util.find_spec(tool.target or "") is not None:
            return ToolResult(tool.tool_id, tool.category, tool.distribution_mode, "PRESENT", tool.target or "")
        status = "NOT_INSTALLED" if tool.distribution_mode == "optional" else "EXTERNAL_NOT_FOUND"
        return ToolResult(tool.tool_id, tool.category, tool.distribution_mode, status, tool.note)

    return ToolResult(tool.tool_id, tool.category, tool.distribution_mode, "MANUAL_CHECK_REQUIRED", tool.note)


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only verification for optional KiCad Engine tool integrations.")
    parser.add_argument("--dry-run", action="store_true", help="Read-only mode. No installations or downloads occur.")
    parser.add_argument("--category", choices=["all", "kicad", "fab", "visual"], default="all")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    selected = [
        tool
        for tool in TOOLS
        if args.category == "all" or tool.category == args.category
    ]

    results = [check_tool(tool) for tool in selected]

    if args.json:
        payload = {
            "repo_root": str(repo_root),
            "dry_run": args.dry_run,
            "category": args.category,
            "results": [asdict(result) for result in results],
        }
        print(json.dumps(payload, indent=2))
        return 0

    print("KiCad Engine optional-tool verification")
    print(f"repo_root: {repo_root}")
    print(f"dry_run: {args.dry_run}")
    print(f"category: {args.category}")
    print("writes: disabled")
    print("")

    for result in results:
        print(f"{result.tool_id}: {result.status} :: {result.detail}")

    present = sum(1 for result in results if result.status == "PRESENT")
    missing = len(results) - present
    print("")
    print(f"summary: present={present} missing_or_manual={missing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
