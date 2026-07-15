# 3. Scrieti o functie care returneaza numarul de cuvinte care exista
# intr-un string. Cuvintele sunt separate de spatii, si/sau semne de
# punctuatie (, ; ? ! .). Intre 2 cuvinte pot aparea in orice combinatie
# spatii si semne de punctuatie.

import re


def count_words(text: str) -> int:
    """Return the number of words in text, split by spaces and/or punctuation."""
    words = re.split(r'[\s,;?!.]+', text.strip())
    words = [word for word in words if word]
    return len(words)


sentence = "Salut,  ce mai faci?! Sper ca esti bine..."
print('\n Exercise 3')
print(f' The string "{sentence}" has {count_words(sentence)} words.')