#!/usr/bin/env python3
"""One-command KiCad Engine project gate runner.

This runner is intentionally read-only. It aggregates existing KiCad Engine
gate evidence from a project directory and writes a Markdown and JSON report
under ``05_OUTPUTS/gate_runs/<timestamp>/`` by default.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((p for p in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (p / "AGENTS.md").exists()), Path.cwd())
sys.path.insert(0, str(SCRIPT_DIR))

from gates import BLOCKED, FAIL, GATE_SEQUENCE, INCOMPLETE, NOT_APPLICABLE, PARTIAL, PASS, GateResult  # noqa: E402


FINAL_PASS = "PASS"
FINAL_FAIL = "FAIL"
FINAL_PARTIAL = "PARTIAL"
FINAL_BLOCKED = "BLOCKED_UNTIL_HUMAN_REVIEW"


class GateRunner:
    """Read-only gate orchestrator."""

    def __init__(
        self,
        project_path: Path,
        output_dir: Path | None = None,
        gates_to_run: list[str] | None = None,
        verbose: bool = False,
    ):
        self.repo_root = REPO_ROOT.resolve()
        self.project_root = self._resolve_project_path(project_path)
        if not self.project_root.exists():
            raise ValueError(f"Project path does not exist: {self.project_root}")
        if not self.project_root.is_dir():
            raise ValueError(f"Project path is not a directory: {self.project_root}")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = output_dir.resolve() if output_dir else self.repo_root / "05_OUTPUTS" / "gate_runs" / timestamp
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.verbose = verbose
        self.gate_classes = self._select_gates(gates_to_run)
        self.started_at = datetime.now()
        self.finished_at: datetime | None = None
        self.results: list[GateResult] = []

    def run(self) -> int:
        self._print("KiCad Engine Project Gate Runner")
        self._print(f"Mode: read-only evidence aggregation")
        self._print(f"Project: {self._rel(self.project_root)}")
        self._print(f"Output: {self._rel(self.output_dir)}")
        self._print("")

        for gate_class in self.gate_classes:
            gate = gate_class(self.project_root, self.output_dir, self.repo_root)
            self._print(f"Running {gate.gate_id}...")
            result = gate.run()
            self.results.append(result)
            self._print(f"  {result.status}: {result.summary}")
            if self.verbose:
                for blocker in result.blockers:
                    self._print(f"    blocker: {blocker.id} - {blocker.message}")

        self.finished_at = datetime.now()
        final = self.final_classification()
        self._write_reports(final)
        self._print("")
        self._print(f"Final classification: {final}")
        self._print(f"Markdown report: {self._rel(self.output_dir / 'PROJECT_GATE_REPORT.md')}")
        self._print(f"JSON report: {self._rel(self.output_dir / 'PROJECT_GATE_REPORT.json')}")
        return 0 if final == FINAL_PASS else 1

    def final_classification(self) -> str:
        statuses = [result.status for result in self.results]
        if any(status == BLOCKED for status in statuses):
            return FINAL_BLOCKED
        if any(status in {FAIL, INCOMPLETE} for status in statuses):
            return FINAL_FAIL
        if any(status in {PARTIAL, NOT_APPLICABLE} for status in statuses):
            return FINAL_PARTIAL
        return FINAL_PASS

    def _write_reports(self, final: str) -> None:
        json_report = self._json_report(final)
        (self.output_dir / "PROJECT_GATE_REPORT.json").write_text(
            json.dumps(json_report, indent=2),
            encoding="utf-8",
        )
        (self.output_dir / "PROJECT_GATE_REPORT.md").write_text(
            self._markdown_report(json_report),
            encoding="utf-8",
        )

    def _json_report(self, final: str) -> dict[str, Any]:
        blockers = []
        for result in self.results:
            for blocker in result.blockers:
                blockers.append(
                    {
                        "gate_id": result.gate_id,
                        "gate_name": result.gate_name,
                        **blocker.to_dict(),
                    }
                )
        status_counts: dict[str, int] = {}
        for result in self.results:
            status_counts[result.status] = status_counts.get(result.status, 0) + 1

        finished_at = self.finished_at or datetime.now()
        return {
            "metadata": {
                "schema_version": "1.0",
                "generated_at": finished_at.isoformat(timespec="seconds"),
                "runner_mode": "READ_ONLY_EVIDENCE_AGGREGATOR",
                "repo_root": self._rel(self.repo_root),
                "project_path": self._rel(self.project_root),
                "output_dir": self._rel(self.output_dir),
                "duration_seconds": round((finished_at - self.started_at).total_seconds(), 3),
                "final_classification": final,
                "safe_actions": [
                    "No KiCad files edited",
                    "No ERC/DRC command executed by this runner",
                    "No fabrication outputs generated",
                ],
            },
            "summary": {
                "gate_count": len(self.results),
                "status_counts": status_counts,
                "blocker_count": len(blockers),
                "final_classification": final,
            },
            "gates": [result.to_dict() for result in self.results],
            "blockers": blockers,
        }

    def _markdown_report(self, report: dict[str, Any]) -> str:
        meta = report["metadata"]
        summary = report["summary"]
        lines = [
            "# KiCad Engine Project Gate Report",
            "",
            f"Generated: `{meta['generated_at']}`",
            f"Project: `{meta['project_path']}`",
            f"Runner mode: `{meta['runner_mode']}`",
            f"Final classification: `{meta['final_classification']}`",
            "",
            "## Safety",
            "",
            "- This runner is read-only.",
            "- It did not edit KiCad files.",
            "- It did not run ERC/DRC; it parsed existing evidence reports.",
            "- It did not generate fabrication outputs.",
            "",
            "## Summary",
            "",
            "| Metric | Value |",
            "| --- | --- |",
            f"| Gate count | {summary['gate_count']} |",
            f"| Blocker count | {summary['blocker_count']} |",
            f"| Status counts | `{json.dumps(summary['status_counts'], sort_keys=True)}` |",
            f"| Final classification | `{summary['final_classification']}` |",
            "",
            "## Gate Results",
            "",
            "| Gate | Status | Summary | Evidence |",
            "| --- | --- | --- | --- |",
        ]
        for gate in report["gates"]:
            evidence_paths = [
                item["path"]
                for item in gate["evidence"]
                if item.get("exists") and item.get("path")
            ]
            evidence_text = "<br>".join(f"`{path}`" for path in evidence_paths) if evidence_paths else "`MISSING`"
            lines.append(
                f"| `{gate['gate_id']}` | `{gate['status']}` | {self._escape_table(gate['summary'])} | {evidence_text} |"
            )

        lines.extend(["", "## Blockers", ""])
        if report["blockers"]:
            lines.extend(["| Gate | Severity | Blocker | Evidence | Required Fix |", "| --- | --- | --- | --- | --- |"])
            for blocker in report["blockers"]:
                lines.append(
                    "| "
                    f"`{blocker['gate_id']}` | "
                    f"`{blocker['severity']}` | "
                    f"{self._escape_table(blocker['message'])} | "
                    f"`{blocker.get('evidence_path', '')}` | "
                    f"{self._escape_table(blocker.get('remediation', ''))} |"
                )
        else:
            lines.append("No blockers detected.")

        lines.extend(["", "## Per-Gate Details", ""])
        for gate in report["gates"]:
            lines.extend(
                [
                    f"### `{gate['gate_id']}`",
                    "",
                    f"- Status: `{gate['status']}`",
                    f"- Summary: {gate['summary']}",
                    f"- Execution seconds: `{gate['execution_seconds']}`",
                    "",
                ]
            )
            if gate["warnings"]:
                lines.append("Warnings:")
                for warning in gate["warnings"]:
                    lines.append(f"- {warning}")
                lines.append("")
            if gate["evidence"]:
                lines.append("Evidence:")
                for evidence in gate["evidence"]:
                    existence = "exists" if evidence["exists"] else "missing"
                    lines.append(f"- `{evidence['path']}` ({evidence['label']}, {existence})")
                lines.append("")

        return "\n".join(lines).rstrip() + "\n"

    def _select_gates(self, gates_to_run: list[str] | None):
        if not gates_to_run:
            return GATE_SEQUENCE
        aliases = {}
        for gate_class in GATE_SEQUENCE:
            aliases[gate_class.gate_id.upper()] = gate_class
            aliases[gate_class.gate_id.lower()] = gate_class
            aliases[gate_class.__name__.lower()] = gate_class
            aliases[gate_class.gate_id.replace("_GATE", "").lower() + "_gate"] = gate_class
        selected = []
        unknown = []
        for requested in gates_to_run:
            key = requested.strip()
            gate_class = aliases.get(key) or aliases.get(key.upper()) or aliases.get(key.lower())
            if gate_class:
                selected.append(gate_class)
            else:
                unknown.append(requested)
        if unknown:
            valid = ", ".join(gate.gate_id for gate in GATE_SEQUENCE)
            raise ValueError(f"Unknown gate(s): {', '.join(unknown)}. Valid gates: {valid}")
        return selected

    def _resolve_project_path(self, project_path: Path) -> Path:
        candidate = Path(project_path)
        if candidate.is_absolute():
            return candidate.resolve()
        cwd_candidate = (Path.cwd() / candidate).resolve()
        if cwd_candidate.exists():
            return cwd_candidate
        return (self.repo_root / candidate).resolve()

    def _rel(self, path: Path | str) -> str:
        candidate = Path(path)
        try:
            return str(candidate.resolve().relative_to(self.repo_root)).replace("\\", "/")
        except Exception:
            return str(candidate.resolve()).replace("\\", "/")

    def _print(self, message: str = "") -> None:
        print(message)

    def _escape_table(self, value: str) -> str:
        return str(value).replace("|", "\\|").replace("\n", " ")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run KiCad Engine project gates by aggregating existing verification evidence.",
    )
    parser.add_argument(
        "-p",
        "--project-path",
        "--project",
        dest="project_path",
        required=True,
        help="Project directory to inspect.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        "--output",
        dest="output_dir",
        help="Optional output directory. Default: 05_OUTPUTS/gate_runs/<timestamp>/",
    )
    parser.add_argument(
        "--gates",
        help="Optional comma-separated gate IDs to run. Default: all gates.",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Print blockers while running.")
    args = parser.parse_args()

    gates_to_run = [item.strip() for item in args.gates.split(",")] if args.gates else None
    output_dir = Path(args.output_dir) if args.output_dir else None
    runner = GateRunner(
        project_path=Path(args.project_path),
        output_dir=output_dir,
        gates_to_run=gates_to_run,
        verbose=args.verbose,
    )
    return runner.run()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
