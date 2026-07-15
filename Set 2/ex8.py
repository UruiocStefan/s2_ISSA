# 8. Sa se scrie o functie care primeste un numar variabil de liste si
# returneaza o lista de tuple astfel: primul tuplu sa contina primele
# elemente din liste, al doilea sa contina elementele de pe pozitia 2
# din liste, etc. Elementele lipsa vor fi inlocuite cu None.
# Pe scurt: implementati zip! (fara sa folositi zip)

def my_zip(*lists) -> list:
    """Reimplements zip(), padding missing values with None."""
    if not lists:
        return []

    max_len = max(len(lst) for lst in lists)
    result = []
    for i in range(max_len):
        row = []
        for lst in lists:
            row.append(lst[i] if i < len(lst) else None)
        result.append(tuple(row))
    return result


list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c", "d"]
print('\n Exercise 8')
print(f' my_zip result: {my_zip(list1, list2, list3)}')