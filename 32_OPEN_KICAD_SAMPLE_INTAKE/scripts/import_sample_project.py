"""Import a local open KiCad sample into imported_originals.

This script never downloads or clones projects. It copies a user-provided local
folder only when --apply is passed and preserves the original import as read-only
source material for later normalized copies.
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent
ACTIVE_PROJECTS = (REPO_ROOT / "04_KICAD_PROJECTS" / "active").resolve()


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def is_inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def count_kicad_files(path: Path) -> dict[str, int]:
    return {
        "kicad_pro": len(list(path.rglob("*.kicad_pro"))),
        "kicad_sch": len(list(path.rglob("*.kicad_sch"))),
        "kicad_pcb": len(list(path.rglob("*.kicad_pcb"))),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Dry-run-first local sample import.")
    parser.add_argument("--sample-id", required=True)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--source-path", type=Path, required=True, help="Local folder already obtained by approved means.")
    parser.add_argument("--license-status", default="NEEDS_HUMAN_LICENSE_REVIEW")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "imported_originals")
    parser.add_argument("--reports-dir", type=Path, default=ROOT / "review_reports")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    source = args.source_path.resolve()
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    run_id = timestamp()
    report = {
        "status": "DRY_RUN_ONLY",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sample_id": args.sample_id,
        "source_url": args.source_url,
        "source_path": str(source),
        "license_status": args.license_status,
        "apply": args.apply,
        "copied": False,
        "errors": [],
        "kicad_files_present": {},
        "destination": None,
    }

    if not source.exists() or not source.is_dir():
        report["errors"].append("source_path must be an existing local folder; remote downloads are not implemented.")
    if is_inside(source, ACTIVE_PROJECTS):
        report["errors"].append("Refusing to import from active user projects.")
    report["kicad_files_present"] = count_kicad_files(source) if source.exists() and source.is_dir() else {}
    if source.exists() and source.is_dir() and not any(report["kicad_files_present"].values()):
        report["errors"].append("No .kicad_pro, .kicad_sch, or .kicad_pcb files found.")

    destination = args.out_dir / f"{args.sample_id}_{run_id}"
    report["destination"] = str(destination)

    if args.apply and not report["errors"]:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination)
        report["status"] = "IMPORTED_ORIGINAL_PRESERVED"
        report["copied"] = True
    elif not args.apply:
        report["status"] = "DRY_RUN_ONLY"
    else:
        report["status"] = "IMPORT_BLOCKED"

    json_path = args.reports_dir / f"sample_import_{args.sample_id}_{run_id}.json"
    md_path = args.reports_dir / f"sample_import_{args.sample_id}_{run_id}.md"
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(
        "\n".join(
            [
                "# Sample Import Report",
                "",
                f"Status: `{report['status']}`",
                f"Sample: `{args.sample_id}`",
                f"Source URL: {args.source_url}",
                f"Source path: `{source}`",
                f"Destination: `{destination}`",
                f"Copied: `{report['copied']}`",
                "",
                "## Errors",
                "",
                *(f"- {error}" for error in report["errors"]),
                "",
                "Imported originals must not be edited directly.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote import report: {md_path}")
    return 1 if report["errors"] and args.apply else 0


if __name__ == "__main__":
    raise SystemExit(main())
