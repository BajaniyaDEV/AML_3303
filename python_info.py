"""Display basic information about the active Python interpreter."""

import platform
import sys


def main() -> None:
    """Print the Python version and operating system."""
    print(f"Python: {platform.python_version()}")
    print(f"Platform: {sys.platform}")


if __name__ == "__main__":
    main()
