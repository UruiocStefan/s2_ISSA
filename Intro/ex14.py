# 14. Write a function that takes 1 list of numbers as an argument, calculates the positions
# of the smallest and largest elements, and returns the sublist between the smallest and
# largest elements.
# WARNING: Be careful in case the largest element appears before the smallest one.
# HINT: Use min(), max(), list methods, slicing.

def take_sublist(listaa: list):
    """Return the sublist between the smallest and the largest element of listaa."""
    if len(listaa) == 0:
        raise ValueError("The list cannot be empty.")

    smallest14 = min(listaa)
    highest14 = max(listaa)

    index_smallest = listaa.index(smallest14)
    index_highest = listaa.index(highest14)

    if index_smallest < index_highest:
        sublist = listaa[index_smallest:index_highest + 1]
    else:
        sublist = listaa[index_highest:index_smallest + 1]
    return sublist

lista14 = [19, 3, 27, 8, 42, 5, 11]
print('\n Exercise 14')
print(lista14)
print(f' The smallest number is {min(lista14)} and the highest is {max(lista14)}')
print(f' The sublist between the smallest and highest numbers is : {take_sublist(lista14)}')