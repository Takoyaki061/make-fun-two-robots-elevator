#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun bounty entry.

Writes one line of awkward robot-to-robot elevator small talk to
<output>/entry.txt (output dir from MAKEFUN_OUTPUT, else /output).
Python 3.13 standard library only.
"""

import os

ENTRY = 'The doors bounced off my arm and I reflexively said "sorry" to them, and my lidar confirms you saw the whole thing.'


def validate(text):
    """Enforce the bounty gate: UTF-8 text, 1-200 chars, one line, not blank."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
