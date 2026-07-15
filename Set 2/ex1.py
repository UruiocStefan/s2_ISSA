# 1. Sa se scrie o functie care sa returneze o lista cu primele n numere
# din sirul lui Fibonacci.
# 1*. Sa se scrie o functie care ia ca parametru 2 numere intregi,
# num_terms, n. Sirul este asemanator Fibonacci cu mentiunea ca fiecare
# termen este suma ultimilor n termeni. Sirul initial este format din
# n-1 0-uri si un 1. (e.g. n=5 sirul initial este 0 0 0 0 1)

def fibonacci(n: int) -> list:
    """Return a list with the first n numbers of the Fibonacci sequence."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def generalized_fibonacci(num_terms: int, n: int) -> list:
    """
    Generalized Fibonacci: each term is the sum of the last n terms.
    The initial sequence is made of (n - 1) zeros followed by a 1.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    sequence = [0] * (n - 1) + [1]
    while len(sequence) < num_terms:
        next_term = sum(sequence[-n:])
        sequence.append(next_term)
    return sequence[:num_terms]


print('\n Exercise 1')
print(f' First 10 Fibonacci numbers: {fibonacci(10)}')
print(f' Generalized Fibonacci (num_terms=10, n=5): {generalized_fibonacci(10, 5)}')