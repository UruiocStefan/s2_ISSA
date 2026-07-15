# 6.	Write a function that takes 3 numeric arguments and
# return the highest one without using the max() function.

def maxim_number(a: int, b: int, c: int) -> int:
    """Return the highest of a, b, c without using max()."""
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum

print('\n Exercise 6')
print(f' The highest is {maxim_number(14, 31, 22)}')