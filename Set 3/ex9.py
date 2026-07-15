# 9. Sa se scrie o functie care primeste un numar variabil de seturi si
# returneaza un dictionar cu urmatoarele operatii dintre toate seturile
# doua cate doua: reuniune, intersectie, a-b, b-a. Cheia va avea forma
# "a op b", unde op este operatorul aplicat: |, &, -.
# Ex: {1,2}, {2, 3} => {"{1, 2} | {2, 3}": 3, "{1, 2} & {2, 3}": 1,
# "{1, 2} - {2, 3}": 1, ...}

def pairwise_set_operations(*sets) -> dict:
    """Return a dict with the size of |, &, - between every pair of sets."""
    result = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a = sets[i]
            b = sets[j]
            result[f"{a} | {b}"] = len(a | b)
            result[f"{a} & {b}"] = len(a & b)
            result[f"{a} - {b}"] = len(a - b)
            result[f"{b} - {a}"] = len(b - a)
    return result


set1 = {1, 2}
set2 = {2, 3}
print('\n Exercise 9')
print(f' {pairwise_set_operations(set1, set2)}')