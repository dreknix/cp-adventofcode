#!/usr/bin/env python3

import re
import sys


# Find the first and the last digit in a string (line) and form a two-digit
# number from these to digits. Sum the values of all lines.
def main() -> int:
    sum: int = 0
    with open("input_a.txt", "r") as file:
        for line in file:
            line = line.strip()
            print(f"{line}")

            result = re.search(r"\d", line)  # search first digit in string
            if result:
                first = (int)(result.group(0))
            else:
                first = 0

            line = line[::-1]  # mirror string

            result = re.search(r"\d", line)  # search first digit in string
            if result:
                last = (int)(result.group(0))
            else:
                last = 0

            value = (first * 10) + last
            print(f"value = {value}")

            sum = sum + value
        print(f"sum = {sum}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
