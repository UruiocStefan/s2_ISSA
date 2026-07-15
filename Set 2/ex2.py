# 2. Sa se scrie o functie care primeste o lista de numere si returneaza
# o lista cu numerele prime care se gasesc in ea.

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


def primes_in_list(numbers: list) -> list:
    """Return only the prime numbers found in numbers."""
    return [number for number in numbers if is_prime(number)]


numbers = [4, 7, 9, 11, 15, 17, 20, 23]
print('\n Exercise 2')
print(f' Primes found in {numbers}: {primes_in_list(numbers)}')