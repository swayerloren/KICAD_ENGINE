#!/usr/bin/env python3
from ai_quality_common import base_parser, matrix_markdown, write_record


def main() -> int:
    args = base_parser("Create a claim/evidence matrix.").parse_args()
    print(write_record(args, "claim_evidence_matrix", matrix_markdown(args)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

