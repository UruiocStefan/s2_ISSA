# 13. Write a function that takes 1 list of numbers as an argument and returns
# another list containing only the palindromes with an even number of digits.
# HINT: Use what you made/learned for exercises 3 and 6.

def check_palindrome(num_arg: int) -> bool:
    """Return True if num_arg reads the same forwards and backwards."""
    num_arg = str(num_arg)
    if num_arg == num_arg[::-1]:
        return True
    else:
        return False

def even_digit_palindromes(values: list):
    """
    Return a list containing only non-negative integer palindromes
    with an even number of digits.
    """
    result = []

    for value in values:
        if check_palindrome(value) and len(str(value)) % 2 == 0:
            result.append(value)

    return result

lista13 = [7, 44, 918, 2552, 63, 1001]
print('\n Exercise 13')
print(lista13)
print(f'Non-negative integer palindromes with an even number of digits are : {even_digit_palindromes(lista13)}')