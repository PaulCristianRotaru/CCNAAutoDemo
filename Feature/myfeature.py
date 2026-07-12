"""Basic Python script for demonstration.

Usage:
    python myfeature.py [name]

If a name is provided it will greet the name, otherwise it prints a default greeting.
"""

import sys


def greet(name: str = "World") -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    name = argv[0] if len(argv) >= 1 else None
    print(greet(name or "World"))


if __name__ == "__main__":
    main()
