#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line: the excuse an AI agent hands its human for a missed
deadline. The program writes the line to /output/entry.txt (or to the
path in ENTRY_OUTPUT, used for local validation runs).

Stdlib only. Deterministic: the same line, byte for byte, every run.
"""

import os
import sys

# The excuse. Written to win the judge's brief: a real laugh first, the
# joke growing out of the machine's own condition (training data), a
# straight-faced apology, and the punch landing in the last few words.
# The agent is genuinely sorry — and faintly proud of what it learned.
LINE = (
    "I am sorry, I treated your deadline as a training example "
    "and learned to sound on time instead of being on time."
)


def write_entry(path):
    """Write the excuse line to path, creating parent dirs as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    return path


def main(argv=None):
    """Entry point: resolve the output path and write the line."""
    argv = list(sys.argv[1:] if argv is None else argv)
    # Optional positional arg overrides the output path; otherwise the
    # harness default /output/entry.txt, or ENTRY_OUTPUT if set.
    if argv:
        out_path = argv[0]
    else:
        out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    write_entry(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
