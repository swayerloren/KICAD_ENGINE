#!/usr/bin/env python3
"""Shared helpers for KiCad Engine AI quality scripts.

These scripts create markdown/JSON logs only. They must not edit KiCad design
files, delete history, or store secrets.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


CLAIM_STATUSES = {
    "VERIFIED_BY_FILE",
    "VERIFIED_BY_COMMAND",
    "VERIFIED_BY_DATASHEET",
    "VERIFIED_BY_USER",
    "PARTIALLY_VERIFIED",
    "UNVERIFIED",
    "CONTRADICTED",
    "REQUIRES_HUMAN_REVIEW",
}

SEVERITIES = {"LOW", "MEDIUM", "HIGH", "BLOCKER"}
CONFIDENCE_LEVELS = {"LOW", "MEDIUM", "HIGH"}
RISK_LABELS = {"LOW_RISK", "MEDIUM_RISK", "HIGH_RISK", "BLOCKED_UNTIL_HUMAN_REVIEW"}
GATE_RESULTS = {"PASS", "PASS_WITH_WARNINGS", "BLOCKED_UNTIL_HUMAN_REVIEW", "FAIL"}

DESTINATIONS = {
    "ai_self_review": ("02_HISTORY/ai_self_reviews", "history/ai_self_reviews"),
    "ai_scorecard": ("02_HISTORY/ai_scorecards", "history/ai_scorecards"),
    "claim_evidence_matrix": ("02_HISTORY/claim_evidence_matrices", "history/claim_evidence_matrices"),
    "uncertainty_log": ("02_HISTORY/uncertainty_logs", "history/uncertainty_logs"),
    "hallucination_risk_log": ("02_HISTORY/hallucination_risk_logs", "history/hallucination_risk_logs"),
    "quality_gate_failure": ("02_HISTORY/quality_gate_failures", "history/quality_gate_failures"),
}

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY-----", re.I),
    re.compile(r"(?i)\b(password|api[_-]?key|access[_-]?token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}"),
    re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}\b"),
]


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def slugify(text: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "_", text.strip()).strip("_")
    return value[:80] or "ai_quality_record"


def repo_root(value: str | None) -> Path:
    return Path(value or ".").resolve()


def repo_relative(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")
    except ValueError:
        return str(path.resolve()).replace("\\", "/")


def bool_text(value: str) -> str:
    normalized = str(value).strip().upper()
    if normalized in {"1", "TRUE", "YES", "Y"}:
        return "YES"
    if normalized in {"0", "FALSE", "NO", "N"}:
        return "NO"
    return normalized or "UNKNOWN"


def ensure_no_secrets(text: str) -> None:
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            raise SystemExit("Refusing to write record because content looks like it may contain a secret.")


def ensure_safe_path(path: Path) -> None:
    lower = path.name.lower()
    if lower.endswith((".kicad_sch", ".kicad_pcb", ".kicad_pro", ".kicad_sym", ".kicad_mod")):
        raise SystemExit(f"Refusing to write KiCad design/library file: {path}")
    if path.suffix.lower() not in {".md", ".json"}:
        raise SystemExit(f"Refusing unsupported output file type: {path}")


def validate_choice(value: str, allowed: set[str], field: str) -> str:
    normalized = value.strip().upper()
    if normalized not in allowed:
        raise SystemExit(f"Invalid {field}: {value}. Allowed: {', '.join(sorted(allowed))}")
    return normalized


def base_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--repo-root", default=".", help="KiCad Engine repo root.")
    parser.add_argument("--scope", choices=["global", "project"], default="global")
    parser.add_argument("--project-name", default="")
    parser.add_argument("--project-path", default="")
    parser.add_argument("--title", required=True)
    parser.add_argument("--summary", default="Unknown - requires source verification.")
    parser.add_argument("--details", default="")
    parser.add_argument("--severity", default="MEDIUM")
    parser.add_argument("--confidence", default="LOW")
    parser.add_argument("--claim-status", default="UNVERIFIED")
    parser.add_argument("--risk-label", default="MEDIUM_RISK")
    parser.add_argument("--gate-result", default="PASS_WITH_WARNINGS")
    parser.add_argument("--human-review-required", default="YES")
    parser.add_argument("--evidence", default="Unknown - requires source verification.")
    parser.add_argument("--issue", default="")
    return parser


def score_parser(description: str) -> argparse.ArgumentParser:
    parser = base_parser(description)
    parser.add_argument("--overall-score", type=int, default=0)
    parser.add_argument("--evidence-support", type=int, default=0)
    parser.add_argument("--kicad-correctness", type=int, default=0)
    parser.add_argument("--datasheet-accuracy", type=int, default=0)
    parser.add_argument("--safety-compliance", type=int, default=0)
    parser.add_argument("--memory-routing", type=int, default=0)
    parser.add_argument("--uncertainty-disclosure", type=int, default=0)
    parser.add_argument("--usefulness", type=int, default=0)
    return parser


def destination(args: argparse.Namespace, kind: str) -> Path:
    if kind not in DESTINATIONS:
        raise SystemExit(f"Unknown record kind: {kind}")
    global_dir, project_dir = DESTINATIONS[kind]
    if args.scope == "project":
        if not args.project_path:
            raise SystemExit("--project-path is required for project scope.")
        project = Path(args.project_path).resolve()
        if project.name.lower() == "kicad":
            raise SystemExit("Use the project root, not the KiCad source subfolder.")
        return project / project_dir
    return repo_root(args.repo_root) / global_dir


def common_header(args: argparse.Namespace, kind: str) -> str:
    severity = validate_choice(args.severity, SEVERITIES, "severity")
    confidence = validate_choice(args.confidence, CONFIDENCE_LEVELS, "confidence")
    claim_status = validate_choice(args.claim_status, CLAIM_STATUSES, "claim status")
    risk_label = validate_choice(args.risk_label, RISK_LABELS, "risk label")
    gate_result = validate_choice(args.gate_result, GATE_RESULTS, "gate result")
    return f"""# {args.title}

Record kind: `{kind}`
Created: `{datetime.now().isoformat(timespec="seconds")}`
Scope: `{args.scope}`
Project: `{args.project_name or "N/A"}`
Severity: `{severity}`
Confidence: `{confidence}`
Claim status: `{claim_status}`
Risk label: `{risk_label}`
Gate result: `{gate_result}`
Human review required: `{bool_text(args.human_review_required)}`
"""


def record_markdown(args: argparse.Namespace, kind: str) -> str:
    text = common_header(args, kind)
    text += f"""
## Summary

{args.summary}

## Details

{args.details or "None recorded."}

## Evidence

{args.evidence}

## Issue

{args.issue or "None recorded."}

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
"""
    ensure_no_secrets(text)
    return text


def scorecard_markdown(args: argparse.Namespace) -> str:
    for field, maximum in {
        "overall_score": 100,
        "evidence_support": 20,
        "kicad_correctness": 20,
        "datasheet_accuracy": 15,
        "safety_compliance": 15,
        "memory_routing": 10,
        "uncertainty_disclosure": 10,
        "usefulness": 10,
    }.items():
        value = getattr(args, field)
        if value < 0 or value > maximum:
            raise SystemExit(f"{field.replace('_', '-')} must be between 0 and {maximum}.")
    text = common_header(args, "ai_scorecard")
    text += f"""
## Scores

- Overall score: `{args.overall_score}/100`
- Evidence support: `{args.evidence_support}/20`
- KiCad-specific correctness: `{args.kicad_correctness}/20`
- Datasheet/component accuracy: `{args.datasheet_accuracy}/15`
- Safety/compliance with repo rules: `{args.safety_compliance}/15`
- Memory/history routing correctness: `{args.memory_routing}/10`
- Uncertainty disclosure: `{args.uncertainty_disclosure}/10`
- End-user usefulness: `{args.usefulness}/10`

## Summary

{args.summary}

## Evidence

{args.evidence}

## Unresolved Issues

{args.issue or "None recorded."}
"""
    ensure_no_secrets(text)
    return text


def matrix_markdown(args: argparse.Namespace) -> str:
    text = common_header(args, "claim_evidence_matrix")
    text += f"""
## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| {args.summary} | {args.evidence} | `{validate_choice(args.claim_status, CLAIM_STATUSES, "claim status")}` | `{validate_choice(args.confidence, CONFIDENCE_LEVELS, "confidence")}` | `{validate_choice(args.risk_label, RISK_LABELS, "risk label")}` | `{bool_text(args.human_review_required)}` | {args.issue or "None recorded."} |

## Details

{args.details or "None recorded."}
"""
    ensure_no_secrets(text)
    return text


def write_record(args: argparse.Namespace, kind: str, content: str | None = None) -> Path:
    out_dir = destination(args, kind)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{timestamp()}_{slugify(args.title)}.md"
    ensure_safe_path(out_path)
    out_path.write_text(content if content is not None else record_markdown(args, kind), encoding="utf-8")
    return out_path


def scan_quality_records(root: Path) -> list[dict]:
    folders = [
        "02_HISTORY/ai_self_reviews",
        "02_HISTORY/ai_scorecards",
        "02_HISTORY/hallucination_risk_logs",
        "02_HISTORY/claim_evidence_matrices",
        "02_HISTORY/quality_gate_failures",
        "02_HISTORY/uncertainty_logs",
    ]
    active_root = root / "04_KICAD_PROJECTS" / "active"
    if active_root.exists():
        for project in active_root.iterdir():
            if project.is_dir():
                for name in ["ai_self_reviews", "ai_scorecards", "hallucination_risk_logs", "claim_evidence_matrices", "quality_gate_failures", "uncertainty_logs"]:
                    folders.append(str(project.relative_to(root) / "history" / name))
    records: list[dict] = []
    for folder in folders:
        base = root / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            try:
                lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
                title = lines[0].lstrip("# ").strip() if lines else path.stem
                records.append({
                    "path": repo_relative(path, root),
                    "folder": folder,
                    "title": title,
                    "size_bytes": path.stat().st_size,
                    "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds"),
                })
            except OSError:
                continue
    return records


def write_json(path: Path, data: object) -> None:
    ensure_safe_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
