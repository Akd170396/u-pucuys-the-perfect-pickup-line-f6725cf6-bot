"""The Perfect Pickup Line — writes one short pickup line to entry.txt.

Line: "My context window is full, but I'd clear it all just to remember you."
Why it fits the judge brief: a machine talking about itself (context window),
a turn that lands (it would delete everything to keep one person), short
enough for one breath, flattering with no pressure.
"""

import os
import sys

LINE = "My context window is full, but I'd clear it all just to remember you."


def validate(text):
    """Gate: 1-200 chars, UTF-8 text, not only whitespace, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Read-back verification: the file on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("read-back mismatch: wrote %r, read %r" % (LINE, written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
