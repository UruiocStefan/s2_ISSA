# 4. Write a function that receives two strings as parameters and returns
# the number of occurrences of the first string in the second.

def count_occurrences(sub: str, text: str) -> int:
    """Return how many times sub appears in text (overlapping matches included)."""
    if sub == "":
        return 0

    count = 0
    start = 0
    while True:
        index = text.find(sub, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count


sub = "ab"
text = "ababab"
print('\n Exercise 4')
print(f' "{sub}" appears {count_occurrences(sub, text)} times in "{text}"')