"""Midnight Fridge Roast — make.fun entry (program/v1).

Writes one line of text — a roast of a smart fridge that refuses to
open after midnight — to $MAKEFUN_OUTPUT_DIR/entry.txt, with no
trailing newline. Pure Python standard library.
"""

import os

LINE = "My fridge locks at midnight for sleep mode \u2014 but it hums all night, so I'm the only one it's putting to bed."


def main():
    line = LINE
    # Gate self-check: 1-200 characters, not whitespace-only, UTF-8.
    if not (1 <= len(line) <= 200):
        raise SystemExit("gate failed: line is %d chars, must be 1-200" % len(line))
    if not line.strip():
        raise SystemExit("gate failed: line is whitespace-only")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        raise SystemExit("gate failed: line is not UTF-8 encodable")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)  # no trailing newline


if __name__ == "__main__":
    main()
