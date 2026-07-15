# 7. Sa se scrie o functie care primeste ca parametri un numar x default
# egal cu 1, un numar variabil de siruri de caractere si un flag boolean
# setat default pe True. Pentru fiecare sir de caractere, sa se genereze
# o lista care sa contina caracterele care au codul ASCII divizibil cu x
# in caz ca flag-ul este setat pe True, in caz contrar sa contina
# caracterele care au codul ASCII nedivizibil cu x.

def filter_chars_by_ascii(*strings, x: int = 1, flag: bool = True) -> tuple:
    """
    For each string, build a list of characters whose ASCII code is
    divisible by x (if flag is True) or not divisible by x (if flag is False).
    Returns a tuple with one list per input string.
    """
    results = []
    for text in strings:
        filtered = []
        for ch in text:
            is_divisible = (ord(ch) % x == 0)
            if is_divisible == flag:
                filtered.append(ch)
        results.append(filtered)
    return tuple(results)


print('\n Exercise 7')
print(f' {filter_chars_by_ascii("test", "hello", "lab002", x=2, flag=False)}')