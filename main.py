"""CLI entry point — greets the user and tracks run count."""

import argparse

from counter import increment, reset
from greeting import build_greeting


def main() -> None:
    parser = argparse.ArgumentParser(description="Greet and count.")
    parser.add_argument("--name", default="World", help="Your name")
    parser.add_argument(
        "--reset", action="store_true", help="Reset the run counter"
    )
    args = parser.parse_args()

    if args.reset:
        reset()
        print("Counter reset.")
        return

    count = increment()
    print(build_greeting(args.name, count))


if __name__ == "__main__":
    main()
