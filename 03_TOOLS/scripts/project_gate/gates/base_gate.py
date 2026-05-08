"""Shared types and helpers for the KiCad Engine project gate runner.

The project gate runner is intentionally read-only. Gate modules inspect
existing project files and existing verification reports, then return a
structured result. They do not run KiCad commands, edit KiCad files, or create
fabrication outputs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from time import perf_counter
from typing import Any


PASS = "PASS"
FAIL = "FAIL"
PARTIAL = "PARTIAL"
INCOMPLETE = "INCOMPLETE"
BLOCKED = "BLOCKED_UNTIL_HUMAN_REVIEW"
NOT_APPLICABLE = "NOT_APPLICABLE"


@dataclass
class GateBlocker:
    """A single issue that prevents or limits gate passage."""

    id: str
    severity: str
    message: str
    evidence_path: str = ""
    remediation: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "severity": self.severity,
            "message": self.message,
            "evidence_path": self.evidence_path,
            "remediation": self.remediation,
        }


@dataclass
class GateEvidence:
    """A source file or directory used as gate evidence."""

    label: str
    path: str
    exists: bool
    kind: str = "file"
    summary: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "label": self.label,
            "path": self.path,
            "exists": self.exists,
            "kind": self.kind,
            "summary": self.summary,
        }


@dataclass
class GateResult:
    """Structured result for one project gate."""

    gate_id: str
    gate_name: str
    status: str
    summary: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    execution_seconds: float = 0.0
    blockers: list[GateBlocker] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    evidence: list[GateEvidence] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "gate_id": self.gate_id,
            "gate_name": self.gate_name,
            "status": self.status,
            "summary": self.summary,
            "timestamp": self.timestamp,
            "execution_seconds": self.execution_seconds,
            "blockers": [blocker.to_dict() for blocker in self.blockers],
            "warnings": self.warnings,
            "evidence": [evidence.to_dict() for evidence in self.evidence],
            "details": self.details,
        }


class BaseGate:
    """Base class for read-only report aggregation gates."""

    gate_id = "BASE_GATE"
    gate_name = "Base Gate"
    stage = 0

    def __init__(self, project_root: Path, output_dir: Path, repo_root: Path):
        self.project_root = Path(project_root).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.repo_root = Path(repo_root).resolve()

    def run(self) -> GateResult:
        start = perf_counter()
        try:
            result = self.evaluate()
        except Exception as exc:  # Defensive: gate runner must not crash on bad/missing reports.
            result = self.make_result(
                FAIL,
                f"{self.gate_name} failed with an internal parser error.",
                [
                    GateBlocker(
                        id="GATE_PARSER_ERROR",
                        severity="CRITICAL",
                        message=str(exc),
                        remediation="Fix the gate parser or malformed evidence file, then rerun the gate runner.",
                    )
                ],
            )
        result.execution_seconds = round(perf_counter() - start, 3)
        return result

    def evaluate(self) -> GateResult:
        raise NotImplementedError

    def make_result(
        self,
        status: str,
        summary: str,
        blockers: list[GateBlocker] | None = None,
        warnings: list[str] | None = None,
        evidence: list[GateEvidence] | None = None,
        details: dict[str, Any] | None = None,
    ) -> GateResult:
        return GateResult(
            gate_id=self.gate_id,
            gate_name=self.gate_name,
            status=status,
            summary=summary,
            blockers=blockers or [],
            warnings=warnings or [],
            evidence=evidence or [],
            details=details or {},
        )

    def project_file(self, *parts: str) -> Path:
        return self.project_root.joinpath(*parts)

    def first_existing(self, *relative_paths: str) -> Path | None:
        for rel_path in relative_paths:
            candidate = self.project_file(*Path(rel_path).parts)
            if candidate.exists():
                return candidate
        return None

    def find_project_files(self, pattern: str) -> list[Path]:
        direct = sorted(self.project_root.glob(pattern))
        if direct:
            return direct
        return sorted(self.project_root.rglob(pattern))

    def read_text(self, path: Path | None) -> str:
        if not path or not path.exists():
            return ""
        return path.read_text(encoding="utf-8", errors="ignore")

    def rel(self, path: Path | str | None) -> str:
        if not path:
            return ""
        candidate = Path(path)
        try:
            return str(candidate.resolve().relative_to(self.repo_root)).replace("\\", "/")
        except Exception:
            try:
                return str(candidate.resolve()).replace("\\", "/")
            except Exception:
                return str(candidate).replace("\\", "/")

    def evidence_path(
        self,
        label: str,
        path: Path | None,
        kind: str = "file",
        summary: str = "",
    ) -> GateEvidence:
        return GateEvidence(
            label=label,
            path=self.rel(path) if path else "",
            exists=bool(path and path.exists()),
            kind=kind,
            summary=summary,
        )

    def missing_evidence_blocker(self, label: str, path_hint: str) -> GateBlocker:
        return GateBlocker(
            id="MISSING_EVIDENCE",
            severity="CRITICAL",
            message=f"Required evidence is missing: {label}.",
            evidence_path=path_hint.replace("\\", "/"),
            remediation="Run the appropriate upstream KiCad Engine workflow step and rerun the gate runner.",
        )
