"""
Simple CLI entry point for the project.
"""

from config import DEFAULT_NAME
from utils import greet


def main() -> None:
    print(greet(DEFAULT_NAME))


if __name__ == "__main__":
    main()
