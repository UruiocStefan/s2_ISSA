# 5. Write a function that checks whether a string contains special
# characters (\r, \t, \n, \a, \b, \f, \v)

def has_special_characters(text: str) -> bool:
    """Return True if text contains any of \\r \\t \\n \\a \\b \\f \\v."""
    special_chars = ['\r', '\t', '\n', '\a', '\b', '\f', '\v']
    for ch in text:
        if ch in special_chars:
            return True
    return False


text_with_tab = "Hello\tWorld"
text_without = "Hello World"
print('\n Exercise 5')
print(f' "Hello\\tWorld" has special characters: {has_special_characters(text_with_tab)}')
print(f' "Hello World" has special characters: {has_special_characters(text_without)}')