#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path

from memory_history_common import repo_root_from_args, scan_markdown, write_json


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Build KiCad Engine memory indexes.")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    repo_root = repo_root_from_args(args.repo_root)
    roots = [repo_root / "01_MEMORY"]
    active_root = repo_root / "04_KICAD_PROJECTS" / "active"
    if active_root.exists():
        roots.extend(path / "memory" for path in active_root.iterdir() if path.is_dir())
    records = scan_markdown(roots)
    data = {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "record_count": len(records),
        "records": records,
    }
    out_json = repo_root / "00_CODEX_START" / "MEMORY_INDEX.generated.json"
    out_md = repo_root / "00_CODEX_START" / "MEMORY_INDEX.generated.md"
    write_json(out_json, data)
    lines = [
        "# Generated Memory Index",
        "",
        f"Generated: `{data['generated']}`",
        f"Record count: `{len(records)}`",
        "",
    ]
    for record in records:
        lines.append(f"- `{record['path']}` - {record['title']}")
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out_json)
    print(out_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

