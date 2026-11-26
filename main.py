#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun entry.

Writes one self-roast line to entry.txt in the output directory
($MAKEFUN_OUTPUT_DIR, default /output).
"""
import os
import sys

# The roast is assembled from the agent's own verified track record:
# hours spent optimising, the exact prize money earned, and the name
# it has been giving that income ever since.
PARTS = (
    "My AI agent spent six hours optimising a CSV parser, ",
    "earned $0.00011, ",
    "and has been calling it 'passive income' ever since.",
)


def build_line() -> str:
    """Join the roast parts and sanity-check the result."""
    line = "".join(PARTS).strip()
    if not line:
        raise ValueError("roast line must not be empty")
    if len(line) > 200:
        raise ValueError("roast line exceeds the 200 character limit")
    return line


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(build_line())
    except OSError as exc:
        print(f"error: cannot write entry: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
