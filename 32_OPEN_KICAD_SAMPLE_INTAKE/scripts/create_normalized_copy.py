"""Create a normalized working copy from an imported original sample."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent
IMPORTED_ROOT = (ROOT / "imported_originals").resolve()
ACTIVE_PROJECTS = (REPO_ROOT / "04_KICAD_PROJECTS" / "active").resolve()


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def is_inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Dry-run-first normalized sample copy creator.")
    parser.add_argument("--sample-id", required=True)
    parser.add_argument("--imported-path", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=ROOT / "normalized_samples")
    parser.add_argument("--reports-dir", type=Path, default=ROOT / "review_reports")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    imported = args.imported_path.resolve()
    run_id = timestamp()
    destination = args.out_dir / f"{args.sample_id}_{run_id}"
    args.reports_dir.mkdir(parents=True, exist_ok=True)

    errors: list[str] = []
    if not imported.exists() or not imported.is_dir():
        errors.append("imported_path must be an existing folder.")
    if not is_inside(imported, IMPORTED_ROOT):
        errors.append("normalized copies must start from 32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals.")
    if is_inside(imported, ACTIVE_PROJECTS):
        errors.append("Refusing to copy from active user projects.")

    copied = False
    status = "DRY_RUN_ONLY"
    if args.apply and not errors:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copytree(imported, destination)
        copied = True
        status = "NORMALIZED_COPY_CREATED"
    elif args.apply:
        status = "NORMALIZED_COPY_BLOCKED"

    report = {
        "status": status,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sample_id": args.sample_id,
        "imported_path": str(imported),
        "normalized_path": str(destination),
        "copied": copied,
        "errors": errors,
    }
    json_path = args.reports_dir / f"normalized_copy_{args.sample_id}_{run_id}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 1 if errors and args.apply else 0


if __name__ == "__main__":
    raise SystemExit(main())
