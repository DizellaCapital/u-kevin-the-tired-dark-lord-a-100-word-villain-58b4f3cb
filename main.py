#!/usr/bin/env python3
"""The Tired Dark Lord - a 100-word villain monologue.

Writes the monologue to entry.txt in MAKEFUN_OUTPUT_DIR (fallback /output).
Stdlib only. The monologue is a first-person villain speech: Lord Varric
at the war table at three in the morning, moving Sorrel's wooden horseman
back and forth while the plan waits, the robe unwashed since Aldergate,
the third cup of tea gone cold, the throne creaking - and the boy king's
latest plea folded into a paper bird instead of burned.
"""

import os

MONOLOGUE = (
    "Three in the morning, and the war table burns. I slide the wooden "
    "horseman \u2014 Sorrel's cavalry \u2014 back and forth, because the plan "
    "only works while my hands stay busy. My robe, unwashed since "
    "Aldergate, smells of smoke and old rain. The third cup of tea has "
    "gone cold by the map. The throne creaks when I shift. My spies bring "
    "the same lies. The boy king sends one more plea. I should burn it. "
    "Instead I fold it into a paper bird and set it on the sill \u2014 so "
    "something in this castle gets to leave."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = MONOLOGUE.strip()
    words = len(text.split())
    if not 1 <= len(text) <= 600:
        raise SystemExit("entry length %d outside gate 1-600" % len(text))
    if not 80 <= words <= 120:
        raise SystemExit("entry word count %d outside brief ~100" % words)
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        raise SystemExit("read-back mismatch")
    print("wrote %d chars, %d words to %s" % (len(text), len(text.split()), path))


if __name__ == "__main__":
    main()
