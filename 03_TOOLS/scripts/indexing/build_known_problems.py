#!/usr/bin/env python3
"""Build the startup known-problems summary.

The summary is intentionally conservative. It lists current risk and issue
sources so future agents see unresolved problems before making KiCad claims.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


SOURCE_PATTERNS = [
    "01_MEMORY/*MISTAKES*.md",
    "01_MEMORY/*FAILED*.md",
    "01_MEMORY/*HALLUCINATION*.md",
    "01_MEMORY/*UNVERIFIED*.md",
    "02_HISTORY/failed_attempts/*.md",
    "02_HISTORY/issue_logs/*.md",
    "02_HISTORY/known_agent_mistakes/*.md",
    "02_HISTORY/hallucination_risk_logs/*.md",
    "02_HISTORY/quality_gate_failures/*.md",
    "02_HISTORY/uncertainty_logs/*.md",
    "04_KICAD_PROJECTS/active/*/memory/OPEN_DESIGN_RISKS.md",
    "04_KICAD_PROJECTS/active/*/memory/PROJECT_HALLUCINATION_RISKS.md",
    "04_KICAD_PROJECTS/active/*/memory/PROJECT_UNVERIFIED_CLAIMS.md",
    "04_KICAD_PROJECTS/active/*/history/issue_logs/*.md",
    "04_KICAD_PROJECTS/active/*/history/user_corrections/*.md",
    "04_KICAD_PROJECTS/active/*/history/quality_gate_failures/*.md",
    "04_KICAD_PROJECTS/active/*/history/uncertainty_logs/*.md",
]


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("/", "\\")


def title_for(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass
    return path.stem.replace("_", " ").title()


def collect_sources(root: Path) -> list[dict[str, object]]:
    seen: set[Path] = set()
    records: list[dict[str, object]] = []
    for pattern in SOURCE_PATTERNS:
        for path in sorted(root.glob(pattern), key=lambda item: str(item).lower()):
            if path in seen or not path.is_file():
                continue
            seen.add(path)
            text = path.read_text(encoding="utf-8", errors="replace")
            records.append(
                {
                    "path": rel(path, root),
                    "title": title_for(path),
                    "size_bytes": path.stat().st_size,
                    "contains_example_only": "EXAMPLE_ONLY" in text,
                    "contains_unresolved": any(
                        token in text.upper()
                        for token in ("UNRESOLVED", "OPEN", "BLOCKED", "HUMAN_REVIEW", "UNVERIFIED")
                    ),
                }
            )
    return records


def build_markdown(data: dict[str, object]) -> str:
    records = data["sources"]  # type: ignore[index]
    lines = [
        "# Current Known Problems",
        "",
        "Status: `AUTO_BUILT`",
        "",
        f"Generated: `{data['generated_at']}`",
        "",
        "This startup file summarizes risk signals so the next AI agent sees what not to repeat.",
        "",
        "## Required Startup Behavior",
        "",
        "- Read this file before making KiCad engineering claims.",
        "- Treat listed problems as unresolved unless the linked source says otherwise.",
        "- Create issue logs, uncertainty logs, or quality-gate failures for unresolved high-risk work.",
        "- Do not approve datasheets, symbols, footprints, pinouts, connector orientation, ERC/DRC, BOM, or manufacturing outputs from this summary alone.",
        "",
        "## Sources Reviewed",
        "",
    ]
    for record in records:
        tags = []
        if record["contains_example_only"]:
            tags.append("EXAMPLE_ONLY")
        if record["contains_unresolved"]:
            tags.append("risk-signal")
        suffix = f" ({', '.join(tags)})" if tags else ""
        lines.append(f"- `{record['path']}` - {record['title']}{suffix}")
    lines.extend(
        [
            "",
            "## Startup Reminder",
            "",
            "Use `00_CODEX_START/SESSION_START_CHECKLIST.md` for startup and "
            "`00_CODEX_START/SESSION_CLOSEOUT_CHECKLIST.md` for closeout.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build KiCad Engine known-problems summary.")
    parser.add_argument("--repo-root", default=".", help="Repository root path.")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    startup_dir = root / "00_CODEX_START"
    startup_dir.mkdir(parents=True, exist_ok=True)

    data = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "repo_root": str(root),
        "sources": collect_sources(root),
    }
    (startup_dir / "CURRENT_KNOWN_PROBLEMS.generated.json").write_text(
        json.dumps(data, indent=2), encoding="utf-8"
    )
    (startup_dir / "CURRENT_KNOWN_PROBLEMS.md").write_text(
        build_markdown(data), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
