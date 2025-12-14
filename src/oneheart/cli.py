"""Command-line entry for ONEHEART."""
import sys
from . import greet


def main() -> int:
    print(greet())
    return 0


if __name__ == "__main__":
    sys.exit(main())
