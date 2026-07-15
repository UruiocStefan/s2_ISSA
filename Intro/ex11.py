# 11. Write a function that takes 1 list of numbers as an argument and
# returns the mean and geometric mean of the largest and smallest element.

def fxt_mean_geom(lista_nr: list):
    """Calculate the mean/geometric mean of the smallest and largest element of lista_nr."""
    if len(lista_nr) == 0:
        raise ValueError("The list cannot be empty.")

    smallest = min(lista_nr)
    highest = max(lista_nr)

    media = (smallest + highest) / 2
    print(f' The media of {smallest} and {highest} is: {media}')

    geom = (smallest * highest) ** (1 / 2)
    print(f' The geometric mean of {smallest} and {highest} is: {geom}')

lista = [8, 20, 3, 47, 15]
print('\n Exercise 11')
fxt_mean_geom(lista)