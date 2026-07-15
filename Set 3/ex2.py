# 2. Scrieti o functie care primeste ca parametru un sir de caractere si
# returneaza un dictionar in care cheile sunt caracterele din componenta
# sirului de caractere iar valorile sunt reprezentate de numarul de
# aparitii ale caracterului respectiv in textul dat.
# Exemplu: "Ana are mere." => {'A': 1, ' ': 2, 'n': 1, 'a': 2, 'r': 2,
# 'e': 3, 'm': 1, '.': 1}

def char_frequency(text: str) -> dict:
    """Return a dictionary mapping each character to its number of occurrences."""
    frequency = {}
    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1
    return frequency


text = "Ana are mere."
print('\n Exercise 2')
print(f' Character frequency of "{text}": {char_frequency(text)}')