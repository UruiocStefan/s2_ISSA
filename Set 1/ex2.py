# 2. Write a function that calculates how many vowels are in a string.

def count_vowels(text: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in text."""
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


sentence = "Astazi invatam Python la laborator"
print('\n Exercise 2')
print(f' The string "{sentence}" has {count_vowels(sentence)} vowels.')