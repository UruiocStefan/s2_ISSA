# 1. Find the largest common divisor of multiple numbers.
# Define a function with variable number of parameters to resolve this.

import math


def gcd_multiple(*numbers: int) -> int:
    """Return the greatest common divisor of all given numbers."""
    if not numbers:
        raise ValueError("At least one number is required.")

    result = numbers[0]
    for number in numbers[1:]:
        result = math.gcd(result, number)
    return result


print('\n Exercise 1')
print(f' The GCD of 24, 36, 48 is: {gcd_multiple(24, 36, 48)}')