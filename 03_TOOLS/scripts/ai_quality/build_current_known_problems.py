#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from ai_quality_common import repo_root


SOURCE_FOLDERS = [
    "01_MEMORY/AGENT_MISTAKES_TO_AVOID.md",
    "01_MEMORY/FAILED_WORKFLOWS.md",
    "01_MEMORY/GLOBAL_HALLUCINATION_RISKS.md",
    "01_MEMORY/GLOBAL_UNVERIFIED_CLAIMS.md",
    "02_HISTORY/failed_attempts",
    "02_HISTORY/issue_logs",
    "02_HISTORY/known_agent_mistakes",
    "02_HISTORY/hallucination_risk_logs",
    "02_HISTORY/quality_gate_failures",
    "02_HISTORY/uncertainty_logs",
]


def first_heading(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("#"):
                return line.lstrip("# ").strip()
    except OSError:
        pass
    return path.stem


def newest_markdown(path: Path, limit: int = 20) -> list[Path]:
    try:
        files = [candidate for candidate in path.rglob("*.md") if candidate.is_file()]
    except OSError:
        return []
    return sorted(files, key=lambda candidate: candidate.stat().st_mtime)[-limit:]


def collect(root: Path) -> list[Path]:
    paths: list[Path] = []
    for item in SOURCE_FOLDERS:
        path = root / item
        if path.is_file():
            paths.append(path)
        elif path.is_dir():
            paths.extend(newest_markdown(path))
    active = root / "04_KICAD_PROJECTS" / "active"
    if active.exists():
        for project in active.iterdir():
            if not project.is_dir():
                continue
            for rel in [
                "memory/OPEN_DESIGN_RISKS.md",
                "memory/PROJECT_HALLUCINATION_RISKS.md",
                "memory/PROJECT_UNVERIFIED_CLAIMS.md",
                "history/issue_logs",
                "history/user_corrections",
                "history/quality_gate_failures",
                "history/uncertainty_logs",
            ]:
                path = project / rel
                if path.is_file():
                    paths.append(path)
                elif path.is_dir():
                    paths.extend(newest_markdown(path))
    return paths


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Build CURRENT_KNOWN_PROBLEMS.md from memory/history risk signals.")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = repo_root(args.repo_root)
    sources = collect(root)
    generated = datetime.now().isoformat(timespec="seconds")
    out = root / "00_CODEX_START" / "CURRENT_KNOWN_PROBLEMS.md"
    lines = [
        "# Current Known Problems",
        "",
        "Status: `AUTO_BUILT`",
        "",
        f"Generated: `{generated}`",
        "",
        "This startup file summarizes risk signals so the next AI agent sees what not to repeat.",
        "",
        "## Sources Reviewed",
        "",
    ]
    for path in sources:
        try:
            rel = path.relative_to(root)
        except ValueError:
            rel = path
        lines.append(f"- `{rel}` - {first_heading(path)}")
    if not sources:
        lines.append("- No source risk files found.")
    lines.extend([
        "",
        "## Required Startup Behavior",
        "",
        "- Read this file before making KiCad engineering claims.",
        "- Treat listed problems as unresolved unless the linked source says otherwise.",
        "- Create issues, uncertainty logs, or quality-gate failures for unresolved high-risk work.",
        "",
    ])
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
