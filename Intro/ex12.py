# 12. Write a function that takes 1 list of numbers as an argument and returns the largest
# element in the 1st half of the list and the smallest element in the 2nd half of the list.
# HINT: Use min(), max(), slicing.

def fct_slicing(lista12: list):
    """The function returns the largest element in the 1st half of the list and the smallest element in the 2nd half of the list."""
    if len(lista12) < 2:
        raise ValueError("The list must contain at least two elements.")
    # For an odd-sized list, the middle element is included in the second half.
    middle = len(lista12) // 2
    first_half = lista12[:middle]
    second_half = lista12[middle:]
    return max(first_half), min(second_half)

lista12 = [6, 25, 13, 4, 30, 9, 17, 2, 21]
print('\n Exercise 12')
print(f' The highest of the first half and the smallest of the second half are : {fct_slicing(lista12)}')