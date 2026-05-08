#!/usr/bin/env python3
from ai_quality_common import base_parser, write_record


def main() -> int:
    args = base_parser("Create a quality-gate failure record.").parse_args()
    print(write_record(args, "quality_gate_failure"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

