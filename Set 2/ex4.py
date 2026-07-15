# 4. Sa se scrie o functie care primeste ca parametri doua liste a si b
# si returneaza: a intersectat cu b, a reunit cu b, a - b, b - a
# fara a folosi set-uri.

def list_operations(a: list, b: list):
    """Return (intersection, union, a - b, b - a) computed without using sets."""
    intersection = []
    for item in a:
        if item in b and item not in intersection:
            intersection.append(item)

    union = list(a)
    for item in b:
        if item not in union:
            union.append(item)

    a_minus_b = []
    for item in a:
        if item not in b and item not in a_minus_b:
            a_minus_b.append(item)

    b_minus_a = []
    for item in b:
        if item not in a and item not in b_minus_a:
            b_minus_a.append(item)

    return intersection, union, a_minus_b, b_minus_a


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print('\n Exercise 4')
intersection, union, a_minus_b, b_minus_a = list_operations(a, b)
print(f' a intersected with b: {intersection}')
print(f' a united with b: {union}')
print(f' a - b: {a_minus_b}')
print(f' b - a: {b_minus_a}')