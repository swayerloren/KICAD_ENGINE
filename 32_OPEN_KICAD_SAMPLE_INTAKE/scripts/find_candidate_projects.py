"""Create a dry-run candidate intake plan from user-provided source lists.

This script does not search the live web, clone repositories, or download files.
It reads a local CSV/JSON list of candidate source URLs and writes a timestamped
Markdown/JSON plan for human review.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    if path.suffix.lower() == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [dict(row) for row in csv.DictReader(handle)]
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return [dict(item) for item in data]
        if isinstance(data, dict) and isinstance(data.get("candidates"), list):
            return [dict(item) for item in data["candidates"]]
    raise ValueError("Input must be CSV or JSON with candidate rows.")


def classify_url(url: str) -> dict[str, str]:
    parsed = urlparse(url or "")
    if parsed.scheme not in {"http", "https"}:
        return {"url_status": "INVALID_OR_LOCAL", "source_host": parsed.netloc or "UNKNOWN"}
    return {"url_status": "SOURCE_LINK_ONLY", "source_host": parsed.netloc}


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an open KiCad sample candidate plan.")
    parser.add_argument("--input", type=Path, help="Local CSV/JSON with source_url and project_name fields.")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "review_reports")
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    run_id = timestamp()
    rows = load_rows(args.input) if args.input else []
    candidates: list[dict[str, object]] = []

    for index, row in enumerate(rows, start=1):
        source_url = (row.get("source_url") or row.get("url") or "").strip()
        project_name = (row.get("project_name") or row.get("name") or f"candidate_{index}").strip()
        url_info = classify_url(source_url)
        candidates.append(
            {
                "project_name": project_name,
                "source_url": source_url,
                "source_host": url_info["source_host"],
                "candidate_status": "CANDIDATE_LINK_ONLY" if url_info["url_status"] == "SOURCE_LINK_ONLY" else "NEEDS_REVIEW",
                "license_status": row.get("license_status") or "NEEDS_HUMAN_LICENSE_REVIEW",
                "public_bundle_status": "EXCLUDED_BY_DEFAULT",
                "human_review_required": True,
                "notes": row.get("notes") or "Dry-run candidate only; no import performed.",
            }
        )

    payload = {
        "status": "DRY_RUN_ONLY",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input": str(args.input) if args.input else None,
        "candidate_count": len(candidates),
        "candidates": candidates,
        "safety": {
            "downloaded": False,
            "cloned": False,
            "scraped": False,
            "public_bundle_allowed": False,
        },
    }

    json_path = args.out_dir / f"candidate_plan_{run_id}.json"
    md_path = args.out_dir / f"candidate_plan_{run_id}.md"
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Open KiCad Sample Candidate Plan",
        "",
        f"Generated: {payload['generated_at']}",
        "",
        "Status: `DRY_RUN_ONLY`",
        "",
        "No repositories were cloned, downloaded, scraped, or imported.",
        "",
        "| Project | Source URL | Host | Candidate Status | License Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in candidates:
        lines.append(
            f"| {item['project_name']} | {item['source_url']} | {item['source_host']} | {item['candidate_status']} | {item['license_status']} |"
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote dry-run candidate plan: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
