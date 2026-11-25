#!/usr/bin/env python3
"""make.fun entry: u-gentle-badger-68-monday-morning-punchlines-709645dc

Writes one joke about Monday mornings to <output dir>/entry.txt.
Deterministic, offline, no randomness: the joke is a single constant.
"""

import os
from pathlib import Path

# The entry: one line, 1-200 Unicode code points, no trailing newline.
JOKE = "I renamed Monday 'Pre-Tuesday' to defuse it. It booked a 7 a.m. meeting about the rebrand."


def output_path() -> Path:
    """Resolve the output file, honouring MAKEFUN_OUTPUT_DIR when it is set."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    # Write bytes so the file holds exactly the joke: no newline is appended.
    path.write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
