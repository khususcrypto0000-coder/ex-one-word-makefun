"""Describe Your Ex in One Word — entry program.

Writes a single-word verdict about an ex to /output/entry.txt.

The word: BUTTDIAL — the whole relationship was an accidental
butt-dial: zero intent, pure accident, and somehow it still rang
for months.
"""

import os
import sys

ENTRY = "buttdial"

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Validate the entry before writing anything.
    if not ENTRY or ENTRY.strip() != ENTRY or not ENTRY.strip():
        sys.exit("error: entry must be non-empty and not only whitespace")
    if len(ENTRY) > 111:
        sys.exit("error: entry must be 1-111 characters")
    if any(ch.isspace() for ch in ENTRY):
        sys.exit("error: entry must be a single word (no spaces)")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read back and verify the file is byte-identical to ENTRY.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != ENTRY.encode("utf-8"):
        sys.exit("error: read-back mismatch, output is not byte-identical")
    if raw.decode("utf-8") != ENTRY:
        sys.exit("error: read-back text mismatch")

    print("wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))
    print("verified: read-back is byte-identical")


if __name__ == "__main__":
    main()
