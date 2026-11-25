"""One Star, Written in Sap — entry generator.

Writes a single one-line 1-star review from a houseplant about its
human owner to /output/entry.txt. Deterministic: no network, no random.
"""

import os

ENTRY = (
    "One star: he waters me once a month like a guilty apology, then drags "
    "my pot into a darker corner and asks why I'm 'not thriving' beside a "
    "brick wall in a pot with no drainage."
)


def main() -> None:
    # Gate self-check (RULES.txt): entry must be UTF-8 text of 1 to 279
    # characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 279, f"entry length {len(ENTRY)} out of gate"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
