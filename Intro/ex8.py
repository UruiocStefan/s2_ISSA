# 8.	Write a function that takes 1 numeric argument and checks
# if it is a palindrome.

def check_palindrome(num_arg: int) -> bool:
    """Return True if num_arg reads the same forwards and backwards."""
    num_arg = str(num_arg)
    if num_arg == num_arg[::-1]:
        return True
    else:
        return False

num_arg = 4884
print('\n Exercise 8')
print(f' The affirmation that "{num_arg} is a palindrome" is {check_palindrome(num_arg)}')