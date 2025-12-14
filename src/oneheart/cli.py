"""Command-line interface for ONEHEART."""

from __future__ import annotations

import argparse
from typing import Iterable, Optional

from . import greet


def main(argv: Optional[Iterable[str]] = None) -> None:
    parser = argparse.ArgumentParser(prog="oneheart", description="ONEHEART CLI")
    parser.add_argument("-n", "--name", default="ONEHEART", help="Name to greet")
    args = parser.parse_args(list(argv) if argv is not None else None)
    print(greet(args.name))


if __name__ == "__main__":
    main()
"""Command-line entry for ONEHEART."""
import sys
from . import greet


def main() -> int:
    print(greet())
    return 0


if __name__ == "__main__":
    sys.exit(main())
