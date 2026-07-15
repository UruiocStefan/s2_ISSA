# 9.	Write a function that takes 1 numeric argument and checks if it is a prime.

def check_prime(nr: int) -> bool:
    """Return True if number is prime."""
    if nr < 2:
        return False
    divisor = 2
    while divisor ** 2 <= nr:
        if nr % divisor == 0:
            return False
        divisor += 1
    return True

nr = 41
print('\n Exercise 9')
if check_prime(nr):
    print(f'The number {nr} is prime.')
else:
    print(f'The number {nr} is not prime.')