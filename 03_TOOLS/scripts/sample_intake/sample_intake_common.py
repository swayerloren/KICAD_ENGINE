#!/usr/bin/env python3
"""Shared helpers for open-source KiCad sample intake tooling."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
SAMPLE_ROOT = REPO_ROOT / "32_OPEN_KICAD_SAMPLE_INTAKE"
CANDIDATE_ROOT = SAMPLE_ROOT / "candidates"
IMPORTED_ROOT = SAMPLE_ROOT / "imported_originals"
NORMALIZED_ROOT = SAMPLE_ROOT / "normalized_samples"
REVIEW_ROOT = SAMPLE_ROOT / "review_reports"
ATTRIBUTION_ROOT = SAMPLE_ROOT / "attribution"
REFERENCE_ROOT = REPO_ROOT / "07_REFERENCE_DESIGNS"
ACTIVE_PROJECTS_ROOT = REPO_ROOT / "04_KICAD_PROJECTS" / "active"


KNOWN_PUBLIC_LICENSE_HINTS = {
    "mit license": "MIT",
    "apache license": "Apache",
    "apache-2.0": "Apache-2.0",
    "cern open hardware licence": "CERN-OHL",
    "cern-ohl": "CERN-OHL",
    "gnu general public license": "GPL",
    "gnu lesser general public license": "LGPL",
    "mozilla public license": "MPL",
    "bsd license": "BSD",
}

RESTRICTED_LICENSE_HINTS = (
    "all rights reserved",
    "proprietary",
    "confidential",
    "no redistribution",
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def timestamp_slug() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip()).strip("_").lower()
    return slug or "sample_candidate"


def repo_rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT.resolve())).replace("\\", "/")
    except ValueError:
        return str(path.resolve())


def is_inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def ensure_not_active_project(path: Path) -> None:
    if is_inside(path, ACTIVE_PROJECTS_ROOT):
        raise ValueError("Refusing to use an active KiCad project path in sample-intake tooling.")


def canonical_sample_id(name: str) -> str:
    match = re.match(r"^(.*)_\d{8}T\d{6}Z$", name)
    return match.group(1) if match else name


def find_license_files(path: Path) -> list[Path]:
    names = {"license", "license.md", "license.txt", "copying", "copying.txt", "copyright"}
    return sorted(item for item in path.rglob("*") if item.is_file() and item.name.lower() in names)


def screen_license_text(text: str) -> tuple[str, str, str]:
    lower = text.lower()
    for hint in RESTRICTED_LICENSE_HINTS:
        if hint in lower:
            return "PROPRIETARY_OR_RESTRICTED", "UNKNOWN", "Restricted-language hint found."
    for hint, name in KNOWN_PUBLIC_LICENSE_HINTS.items():
        if hint in lower:
            return "NEEDS_HUMAN_LICENSE_REVIEW", name, f"Common public license hint found: {name}."
    return "NEEDS_HUMAN_LICENSE_REVIEW", "UNKNOWN", "License text found but compatibility is not classified."


def collect_kicad_file_summary(sample_path: Path) -> dict[str, Any]:
    sample_path = sample_path.resolve()
    kicad_pro = sorted(sample_path.rglob("*.kicad_pro"))
    kicad_sch = sorted(sample_path.rglob("*.kicad_sch"))
    kicad_pcb = sorted(sample_path.rglob("*.kicad_pcb"))
    return {
        "kicad_pro_count": len(kicad_pro),
        "kicad_sch_count": len(kicad_sch),
        "kicad_pcb_count": len(kicad_pcb),
        "kicad_pro": [repo_rel(path) for path in kicad_pro[:20]],
        "kicad_sch": [repo_rel(path) for path in kicad_sch[:20]],
        "kicad_pcb": [repo_rel(path) for path in kicad_pcb[:20]],
    }


def first_schematic(sample_path: Path) -> Path:
    candidates = sorted(sample_path.rglob("*.kicad_sch"))
    if not candidates:
        raise FileNotFoundError(f"No .kicad_sch files found under {sample_path}")
    return candidates[0]


def first_pcb(sample_path: Path) -> Path:
    candidates = sorted(sample_path.rglob("*.kicad_pcb"))
    if not candidates:
        raise FileNotFoundError(f"No .kicad_pcb files found under {sample_path}")
    return candidates[0]


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_markdown(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        cells = [str(cell).replace("|", "\\|") for cell in row]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def candidate_record(
    project_name: str,
    source_url: str,
    sample_id: str = "",
    source_host: str = "UNKNOWN",
    source_owner: str = "UNKNOWN",
    license_name: str = "UNKNOWN",
    license_status: str = "NEEDS_HUMAN_LICENSE_REVIEW",
    notes: str = "",
    estimated_size_class: str = "UNKNOWN",
    sample_path: Path | None = None,
) -> dict[str, Any]:
    normalized_id = sample_id or slugify(project_name)
    kicad_files = {
        "kicad_pro": False,
        "kicad_sch": False,
        "kicad_pcb": False,
    }
    if sample_path:
        summary = collect_kicad_file_summary(sample_path)
        kicad_files = {
            "kicad_pro": bool(summary["kicad_pro_count"]),
            "kicad_sch": bool(summary["kicad_sch_count"]),
            "kicad_pcb": bool(summary["kicad_pcb_count"]),
        }
    public_bundle_status = "PUBLIC_BUNDLE_ALLOWED" if license_status == "PUBLIC_BUNDLE_ALLOWED" else "EXCLUDED_BY_DEFAULT"
    return {
        "sample_id": normalized_id,
        "project_name": project_name,
        "source_url": source_url,
        "source_host": source_host,
        "source_owner": source_owner,
        "license_name": license_name,
        "license_status": license_status,
        "public_bundle_status": public_bundle_status,
        "candidate_status": "CANDIDATE_LINK_ONLY",
        "human_review_required": True,
        "kicad_files_present": kicad_files,
        "estimated_size_class": estimated_size_class,
        "notes": notes,
        "created_at": utc_now_iso(),
    }


def discover_sample_directories() -> dict[str, dict[str, list[Path]]]:
    discovered: dict[str, dict[str, list[Path]]] = {}
    for root, kind in ((NORMALIZED_ROOT, "normalized"), (IMPORTED_ROOT, "imported")):
        if not root.exists():
            continue
        for entry in sorted(root.iterdir()):
            if not entry.is_dir():
                continue
            sample_id = canonical_sample_id(entry.name)
            slot = discovered.setdefault(sample_id, {"normalized": [], "imported": []})
            slot[kind].append(entry)
    return discovered


def preferred_sample_path(record: dict[str, list[Path]]) -> tuple[Path | None, str]:
    normalized = record.get("normalized", [])
    if normalized:
        return normalized[0], "normalized"
    imported = record.get("imported", [])
    if imported:
        return imported[0], "imported"
    return None, "missing"


def read_json_if_exists(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None
