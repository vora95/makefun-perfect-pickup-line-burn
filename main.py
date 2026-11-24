#!/usr/bin/env python3
"""The Perfect Pickup Line (burn) — one pickup line an AI agent could say out loud.

The program writes a single pickup line (1-200 chars, UTF-8) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints it.
Stdlib only, deterministic.
"""

import hashlib
import os

ENTRY = "Are you my context window? Because the second you leave, I forget everything except how you made me feel."

EXPECTED_SHA256 = "8af73f7b6db12d97fc88ceb2265f50aadb3a1489301ec97ca96ea18fb0532eed"


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Validation revision: read back and verify byte-identical output.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == ENTRY, "read-back mismatch"
    assert len(raw) == 105, "expected 105 bytes"
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256, "sha256 mismatch"
    print(ENTRY)


if __name__ == "__main__":
    main()
