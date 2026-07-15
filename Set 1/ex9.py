# 9. Write a function that returns the largest prime number from a string
# given as a parameter or -1 if the character string contains no prime
# number.
# Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271

import re


def is_prime(number: int) -> bool:
    """Return True if number is prime."""
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def largest_prime_in_string(text: str) -> int:
    """Return the largest prime number found in text, or -1 if there is none."""
    numbers = re.findall(r'\d+', text)
    primes = [int(num) for num in numbers if is_prime(int(num))]
    return max(primes) if primes else -1


sample = 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'
print('\n Exercise 9')
print(f' The largest prime in "{sample}" is: {largest_prime_in_string(sample)}')