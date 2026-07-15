# 3. Sa se compare doua dictionare fara a folosi operatorul "==" sau
# "!=" pentru altceva decat tipuri primitive (int, float, str) si sa se
# returneze un tuplu de liste de diferente astfel:
# (chei_comune_dar_cu_valori_diferite, chei_doar_in_primul,
# chei_doar_in_al_doilea). Dictionarele trebuiesc parcurse recursiv.

def values_equal(value1, value2) -> bool:
    """Recursively compare two values, using '==' only for primitives."""
    if isinstance(value1, dict) and isinstance(value2, dict):
        diff, only_first, only_second = compare_dicts(value1, value2)
        return not diff and not only_first and not only_second

    if isinstance(value1, (list, tuple)) and isinstance(value2, (list, tuple)):
        if len(value1) != len(value2):
            return False
        return all(values_equal(v1, v2) for v1, v2 in zip(value1, value2))

    if isinstance(value1, set) and isinstance(value2, set):
        if len(value1) != len(value2):
            return False
        return all(item in value2 for item in value1)

    if type(value1) != type(value2):
        return False

    # primitives (int, float, str, bool, None, ...)
    return value1 == value2


def compare_dicts(dict1: dict, dict2: dict) -> tuple:
    """Return (common_keys_different_values, only_in_first, only_in_second)."""
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())

    only_in_first = list(keys1 - keys2)
    only_in_second = list(keys2 - keys1)

    common_diff = []
    for key in keys1 & keys2:
        if not values_equal(dict1[key], dict2[key]):
            common_diff.append(key)

    return common_diff, only_in_first, only_in_second


dict1 = {"a": 1, "b": {"x": 1, "y": [1, 2]}, "c": 3}
dict2 = {"a": 1, "b": {"x": 1, "y": [1, 3]}, "d": 4}
print('\n Exercise 3')
print(f' Differences: {compare_dicts(dict1, dict2)}')