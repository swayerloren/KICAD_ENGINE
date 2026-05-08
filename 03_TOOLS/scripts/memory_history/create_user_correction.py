#!/usr/bin/env python3
from memory_history_common import common_record_parser, write_record


def main() -> int:
    parser = common_record_parser("Create a timestamped user-correction record.")
    args = parser.parse_args()
    output = write_record("user_correction", args)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

