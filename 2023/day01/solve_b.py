#!/usr/bin/env python3

import re
import sys


def get_digit_from_string(s: str) -> int:
    match s:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
    return (int)(s)


# Find the first and the last digit or spelled out digit in a string (line)
# and form a two-digit number from these to digits. Sum the values of all
# lines.
def main() -> int:
    sum: int = 0
    with open("input_a.txt", "r") as file:
        for line in file:
            line = line.strip()
            print(f"{line}")

            result = re.search(r"one|two|three|four|five|six|seven|eight|nine|\d", line)
            if result:
                first = get_digit_from_string(result.group(0))
            else:
                first = 0

            line = line[::-1]  # mirror string

            result = re.search(r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d", line)
            if result:
                last = get_digit_from_string(result.group(0)[::-1])
            else:
                last = 0

            value = (first * 10) + last
            print(f"value = {value}")

            sum = sum + value
        print(f"sum = {sum}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
