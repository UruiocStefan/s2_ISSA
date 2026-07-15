# 1. Sa se scrie o functie care primeste ca parametri doua liste a si b
# si returneaza un tuplu de seturi care sa contina:
# (a intersectat cu b, a reunit cu b, a - b, b - a)

def set_operations(a: list, b: list) -> tuple:
    """Return (a & b, a | b, a - b, b - a) as sets."""
    set_a = set(a)
    set_b = set(b)
    return set_a & set_b, set_a | set_b, set_a - set_b, set_b - set_a


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print('\n Exercise 1')
intersection, union, a_minus_b, b_minus_a = set_operations(a, b)
print(f' a & b: {intersection}')
print(f' a | b: {union}')
print(f' a - b: {a_minus_b}')
print(f' b - a: {b_minus_a}')