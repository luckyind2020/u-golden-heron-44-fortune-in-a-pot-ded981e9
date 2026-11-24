"""Fortune in a Pot — print the houseplant's fortune.

Reads the single-line fortune from entry.txt next to this file and
prints it exactly as written. The fortune is at most 120 characters,
kind, funny, and unmistakably about the plant on the windowsill.
"""

from pathlib import Path


MAX_CHARS = 120


def load_fortune() -> str:
    path = Path(__file__).resolve().parent / "entry.txt"
    fortune = path.read_text(encoding="utf-8").strip()
    if len(fortune) > MAX_CHARS:
        raise ValueError(f"fortune is {len(fortune)} chars, over the {MAX_CHARS} limit")
    if "\n" in fortune:
        raise ValueError("fortune must be a single line")
    return fortune


def main() -> None:
    print(load_fortune())


if __name__ == "__main__":
    main()
