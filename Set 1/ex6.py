# 6. Write a function that converts a string of characters written in
# UpperCamelCase into snake_case.

import re


def camel_to_snake(text: str) -> str:
    """Convert an UpperCamelCase string into snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()


camel_text = "ThisIsUpperCamelCase"
print('\n Exercise 6')
print(f' "{camel_text}" in snake_case is: "{camel_to_snake(camel_text)}"')