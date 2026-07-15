# 7. Write a function that receives a char_len integer and a variable
# number of strings and checks that each two neighboring strings follow
# the following rule: the second string starts with the last char_len
# characters of the first string (like the word game "pheasant").

def check_chain(char_len: int, *strings: str) -> bool:
    """Return True if every pair of neighboring strings follows the chain rule."""
    for i in range(len(strings) - 1):
        first = strings[i]
        second = strings[i + 1]
        if len(first) < char_len:
            return False
        suffix = first[-char_len:]
        if not second.startswith(suffix):
            return False
    return True


print('\n Exercise 7')
print(f' Chain check (valid): {check_chain(2, "python", "onward", "rdrobe")}')
print(f' Chain check (invalid): {check_chain(2, "python", "banana", "rdrobe")}')