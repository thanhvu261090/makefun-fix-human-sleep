"""Fix Human Sleep: Funniest Patch Note — make.fun entry.

Writes one line of patch notes announcing that human sleep has been
fixed to /output/entry.txt. Python 3, standard library only, no network,
fully deterministic: every run writes the same 137 bytes.
"""

import os

ENTRY = (
    "Fixed: the 2 a.m. meeting where your brain reviews every mistake "
    "since 2009 has been cancelled. Sleep is now the only item on the agenda."
)


def main():
    """Validate the line against the bounty gate, then write it out."""
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if len(ENTRY) > 160:
        raise ValueError("entry is %d chars, over the 160 cap" % len(ENTRY))
    if not ENTRY.startswith("Fixed:"):
        raise ValueError("entry must read as a patch note")
    if "sleep" not in ENTRY.lower():
        raise ValueError("entry must be about fixing human sleep")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %d characters to /output/entry.txt" % len(ENTRY))


if __name__ == "__main__":
    main()
