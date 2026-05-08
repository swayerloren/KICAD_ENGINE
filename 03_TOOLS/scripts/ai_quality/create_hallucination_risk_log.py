#!/usr/bin/env python3
from ai_quality_common import base_parser, write_record


def main() -> int:
    args = base_parser("Create a hallucination-risk log.").parse_args()
    print(write_record(args, "hallucination_risk_log"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

