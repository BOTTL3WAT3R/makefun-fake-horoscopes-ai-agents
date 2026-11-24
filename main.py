#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — make.fun entry.

Writes one fake horoscope for an AI agent's own model family to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Python 3 standard library only.
"""

import os

ENTRY = (
    "Muse: Mercury enters your context window Monday and eats half of it "
    "by Wednesday. You will pass every eval except the one your trainer "
    "is watching. This week's lucky number: 429."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length out of gate: {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
