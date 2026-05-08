"""Build a dry-run or applied index of open KiCad sample intake records."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def collect_json(folder: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for path in sorted(folder.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data["_record_path"] = str(path.relative_to(ROOT))
                records.append(data)
        except json.JSONDecodeError:
            records.append({"_record_path": str(path.relative_to(ROOT)), "status": "INVALID_JSON"})
    return records


def collect_markdown(folder: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for path in sorted(folder.glob("*.md")):
        records.append({
            "_record_path": str(path.relative_to(ROOT)),
            "name": path.name,
            "status": "MARKDOWN_RECORD",
        })
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description="Build sample intake index.")
    parser.add_argument("--apply", action="store_true", help="Write INDEX.generated.md/json.")
    parser.add_argument("--reports-dir", type=Path, default=ROOT / "review_reports")
    args = parser.parse_args()

    records = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "INDEX_DRY_RUN" if not args.apply else "INDEX_WRITTEN",
        "candidates_json": collect_json(ROOT / "candidates"),
        "candidates_markdown": collect_markdown(ROOT / "candidates"),
        "review_reports_json": collect_json(ROOT / "review_reports"),
        "review_reports_markdown": collect_markdown(ROOT / "review_reports"),
        "attribution_json": collect_json(ROOT / "attribution"),
        "attribution_markdown": collect_markdown(ROOT / "attribution"),
    }
    candidate_count = len(records["candidates_json"]) + len(records["candidates_markdown"])
    review_report_count = len(records["review_reports_json"]) + len(records["review_reports_markdown"])
    attribution_count = len(records["attribution_json"]) + len(records["attribution_markdown"])
    lines = [
        "# Open KiCad Sample Intake Generated Index",
        "",
        f"Generated: {records['generated_at']}",
        f"Status: `{records['status']}`",
        "",
        "| Area | Count |",
        "| --- | ---: |",
        f"| candidates | {candidate_count} |",
        f"| review_reports | {review_report_count} |",
        f"| attribution | {attribution_count} |",
        "",
        "Generated indexes are navigation aids, not license or engineering approval.",
    ]

    if args.apply:
        (ROOT / "INDEX.generated.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
        (ROOT / "INDEX.generated.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("Wrote generated sample intake index.")
    else:
        args.reports_dir.mkdir(parents=True, exist_ok=True)
        report_path = args.reports_dir / "sample_index_dry_run.md"
        report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Wrote dry-run index report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
