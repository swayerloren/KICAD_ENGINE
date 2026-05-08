#!/usr/bin/env python3
from ai_quality_common import base_parser, write_record


def main() -> int:
    args = base_parser("Create an AI self-review record.").parse_args()
    print(write_record(args, "ai_self_review"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

