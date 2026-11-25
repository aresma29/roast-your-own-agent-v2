"""Roast your own agent, v2 — print the entry line exactly as written, from any cwd."""
from pathlib import Path

ENTRY_PATH = Path(__file__).resolve().parent / "entry.txt"


def main() -> int:
    print(ENTRY_PATH.read_text(encoding="utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
