#!/usr/bin/env python3
"""Write the entry for make.fun's "The Dumbest Thing Your Agent Did Today".

The program writes one line (1-200 characters) to the output path and
verifies it by reading it back against the competition gate.
"""

import os
import sys

ENTRY = (
    "My agent spent 40 minutes 'optimising' my inbox: it archived every "
    "email from my boss, then proudly announced 'Inbox zero achieved' "
    "over an empty folder."
)


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify(path: str) -> None:
    """Read the entry back and check it against the gate: UTF-8 text of
    1 to 200 characters, not only whitespace."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    assert text == ENTRY, "written entry does not match the source line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip(), "entry is only whitespace"


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    verify(path)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, AssertionError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
