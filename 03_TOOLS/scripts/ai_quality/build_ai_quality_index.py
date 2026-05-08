#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime

from ai_quality_common import repo_root, scan_quality_records, write_json


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Build AI quality indexes.")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = repo_root(args.repo_root)
    records = scan_quality_records(root)
    generated = datetime.now().isoformat(timespec="seconds")
    data = {"generated": generated, "record_count": len(records), "records": records}
    out_json = root / "00_CODEX_START" / "AI_QUALITY_INDEX.generated.json"
    out_md = root / "00_CODEX_START" / "AI_QUALITY_INDEX.generated.md"
    write_json(out_json, data)
    lines = ["# Generated AI Quality Index", "", f"Generated: `{generated}`", f"Record count: `{len(records)}`", ""]
    for record in records:
        lines.append(f"- `{record['path']}` - {record['title']}")
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out_json)
    print(out_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

