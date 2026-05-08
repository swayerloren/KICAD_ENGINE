#!/usr/bin/env python3
from pathlib import Path

from memory_history_common import common_record_parser, repo_root_from_args, ensure_safe_output_path, slugify, now_stamp, build_record_markdown


def main() -> int:
    parser = common_record_parser("Create a timestamped global memory update stub.")
    parser.set_defaults(scope="global")
    args = parser.parse_args()
    repo_root = repo_root_from_args(args.repo_root)
    target_dir = repo_root / "01_MEMORY"
    target_dir.mkdir(parents=True, exist_ok=True)
    output = target_dir / f"MEMORY_UPDATE_{now_stamp()}_{slugify(args.title)}.md"
    ensure_safe_output_path(output)
    output.write_text(build_record_markdown("global_memory_update", args), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

