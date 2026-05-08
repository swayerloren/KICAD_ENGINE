#!/usr/bin/env python3
from pathlib import Path

from memory_history_common import common_record_parser, ensure_project_root, ensure_safe_output_path, slugify, now_stamp, build_record_markdown


def main() -> int:
    parser = common_record_parser("Create a timestamped project memory update stub.")
    parser.set_defaults(scope="project")
    args = parser.parse_args()
    if not args.project_path:
        raise SystemExit("--project-path is required.")
    project_root = Path(args.project_path).resolve()
    ensure_project_root(project_root)
    target_dir = project_root / "memory"
    target_dir.mkdir(parents=True, exist_ok=True)
    output = target_dir / f"MEMORY_UPDATE_{now_stamp()}_{slugify(args.title)}.md"
    ensure_safe_output_path(output)
    output.write_text(build_record_markdown("project_memory_update", args), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

