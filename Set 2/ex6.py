# 6. Sa se scrie o functie care primeste ca parametru un numar variabil
# de liste si un numar intreg x. Sa se returneze o lista care sa contina
# elementele care apar de exact x ori in listele primite.
# Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [7, 1, "test"] si
# x = 2 se va returna [1, 2, 3, 4].

def elements_in_exact_lists(x: int, *lists) -> list:
    """Return the elements that appear in exactly x of the given lists."""
    seen_order = []
    seen_set = set()
    for lst in lists:
        for item in lst:
            if item not in seen_set:
                seen_set.add(item)
                seen_order.append(item)

    result = []
    for item in seen_order:
        count = sum(1 for lst in lists if item in lst)
        if count == x:
            result.append(item)
    return result


list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [7, 1, "test"]
print('\n Exercise 6')
print(f' Elements appearing in exactly 2 lists: {elements_in_exact_lists(2, list1, list2, list3, list4)}')