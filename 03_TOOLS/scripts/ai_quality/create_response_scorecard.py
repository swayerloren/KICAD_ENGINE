#!/usr/bin/env python3
from ai_quality_common import score_parser, scorecard_markdown, write_record


def main() -> int:
    args = score_parser("Create an AI response scorecard.").parse_args()
    print(write_record(args, "ai_scorecard", scorecard_markdown(args)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

