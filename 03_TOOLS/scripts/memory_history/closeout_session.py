#!/usr/bin/env python3
from memory_history_common import common_record_parser, write_record


CHECKLIST = """## Closeout Checklist

- [ ] Session log written.
- [ ] Command logs written if commands were run.
- [ ] Failed attempts recorded if anything failed.
- [ ] User corrections recorded if the user corrected the work.
- [ ] Project memory updated only for durable project-specific facts.
- [ ] Global memory updated only for reusable facts.
- [ ] Open issues created for unresolved problems.
- [ ] Memory/history indexes updated.
- [ ] No secrets recorded.
"""


def main() -> int:
    parser = common_record_parser("Create a session closeout record.")
    args = parser.parse_args()
    args.details = (args.details + "\n\n" + CHECKLIST).strip()
    output = write_record("session", args)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

