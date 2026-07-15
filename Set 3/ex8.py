# 8. Sa se scrie o functie care primeste ca parametru un set (o colectie
# de elemente) si returneaza un tuplu (a, b), a reprezentand numarul de
# elemente unice din set iar b reprezentand numarul de elemente
# duplicate din set.

from collections import Counter


def count_unique_and_duplicates(collection) -> tuple:
    """
    Return (unique_count, duplicate_count):
    - unique_count: how many elements appear exactly once
    - duplicate_count: how many extra (repeated) occurrences exist
    """
    counts = Counter(collection)
    unique_count = sum(1 for c in counts.values() if c == 1)
    duplicate_count = sum(c - 1 for c in counts.values() if c > 1)
    return unique_count, duplicate_count


collection = [1, 2, 2, 3, 4, 4, 4, 5]
print('\n Exercise 8')
print(f' (unique, duplicates) for {collection}: {count_unique_and_duplicates(collection)}')