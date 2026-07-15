# 9. Sa se scrie o functie ce va ordona o lista de tuple de string-uri in
# functie de al 3-lea caracter al celui de-al 2-lea element din tupla.
# Exemplu: [('abc', 'bcd'), ('abc', 'zza')] => [('abc', 'zza'), ('abc', 'bcd')]

def sort_by_third_char_of_second(data: list) -> list:
    """Sort a list of string tuples by the 3rd character of the 2nd element."""
    return sorted(data, key=lambda pair: pair[1][2])


data = [('abc', 'bcd'), ('abc', 'zza'), ('xyz', 'qmc')]
print('\n Exercise 9')
print(f' Sorted result: {sort_by_third_char_of_second(data)}')