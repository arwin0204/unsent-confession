#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun entry.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent line itself,
exactly as it was typed, with no explanation after it.

Deterministic: the same fixed text on every run, no randomness,
no network, no input files.
"""

import os

ENTRY = (
    "To: the barista who quit last spring\n"
    "I finally learned your name the week after you left, "
    "and I still order a flat white every morning, "
    "just the way you made it."
)


def main() -> None:
    # Self-check against the sealed gate: 1-260 chars total, message
    # line at most 200 chars, exactly two parts, To: line first.
    lines = ENTRY.split("\n")
    assert 1 <= len(ENTRY) <= 260, "entry out of gate range"
    assert len(lines) == 2, "entry must be exactly two lines"
    assert lines[0].startswith("To: "), "first line must be a To: line"
    assert len(lines[1]) <= 200, "message line over 200 chars"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isdir(out_dir):
        out_dir = "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
