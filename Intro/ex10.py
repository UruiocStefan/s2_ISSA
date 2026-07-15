# 10.	Write a function that takes 1 list argument
# and prints its elements using a for loop.

def fct_print(lista: list):
    """Print the list."""
    print('\n Exercise 10')
    print(f'The list: {lista}')
    print(f'The elements: ')
    for num in lista:
        print(num, end=' ')


lista = [11, 6, 27, 3, 45, 18, 9]
fct_print(lista)