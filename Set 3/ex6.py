# 6. Fie un dictionar global:
# {"+": lambda a, b: a + b, "*": lambda a, b: a * b,
#  "/": lambda a, b: a / b, "%": lambda a, b: a % b}
# Sa se construiasca o functie apply_operator(operator, a, b) care va
# aplica peste a si b regula specificata de dictionarul global. Sa se
# implementeze astfel incat, in cazul adaugarii unui operator nou, sa nu
# fie necesara modificarea functiei.

OPERATIONS = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b,
}


def apply_operator(operator: str, a, b):
    """Apply the operation stored in OPERATIONS under the given key."""
    if operator not in OPERATIONS:
        raise ValueError(f"Unknown operator: {operator}")
    return OPERATIONS[operator](a, b)


print('\n Exercise 6')
print(f' apply_operator("+", 4, 5) = {apply_operator("+", 4, 5)}')
print(f' apply_operator("%", 10, 3) = {apply_operator("%", 10, 3)}')

# Adding a new operator does NOT require changing apply_operator:
OPERATIONS["-"] = lambda a, b: a - b
print(f' apply_operator("-", 9, 4) = {apply_operator("-", 9, 4)}')