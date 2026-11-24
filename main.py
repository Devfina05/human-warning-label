#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the single-line safety warning label that should come printed
on every human being to /output/entry.txt, as the make.fun
program/v1 harness requires.

The label is a constant: the joke is the deliverable, and the program's
job is to hand it over exactly, deterministically, and inside the
160-character gate. No input is read, no network is touched, and two
runs produce byte-identical output.
"""

from __future__ import annotations

import os
import sys

# The label itself. One line, one idea, punchline in the last words:
# the single brain cell is not missing, it is just out to lunch.
LABEL = (
    "WARNING: This human contains exactly one (1) brain cell, "
    "and it is currently out to lunch."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 160


def build_label() -> str:
    """Return the label, enforcing the competition's gate ourselves.

    The gate counts characters, not bytes, and the file must hold one
    line of UTF-8 text, so the checks here mirror the sealed scorer.
    """
    text = LABEL.strip()
    if not text:
        raise ValueError("label is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("label must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"label is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    return text


def main() -> int:
    text = build_label()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    print(f"wrote {len(text)} characters to {OUTPUT_FILE}")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
